

# Generated at 2022-06-13 15:18:04.434474
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    strategy_module = StrategyModule(tqm=None)
    strategy_module._tqm._terminated = ""
    strategy_module.run(iterator=None, play_context=None)

# Generated at 2022-06-13 15:18:05.049540
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:18:05.934966
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass


# Generated at 2022-06-13 15:18:10.361269
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = TaskQueueManager(
        inventory=InventoryManager(loader=None, sources='localhost,'),
        variable_manager=VariableManager(loader=None, inventory=None),
        loader=None,
        options=None,
        passwords=None,
        stdout_callback=None,
        run_additional_callbacks=True,
        run_tree=False,
    )
    StrategyModule(tqm)


# Generated at 2022-06-13 15:18:18.777286
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    iterator = [1]
    play_context = [2]

    run_call_order = []
    class FakeTQM(object):
        def __init__(self, callback):
            self.callback = callback
            self.RUN_UNKNOWN_ERROR = 1
            self.RUN_OK = 2
            self._terminated = False

        def send_callback(self, name):
            self.callback(name)

        def run_handlers(self, handler_list):
            run_call_order.append('run_handlers')

        def cleanup_all_tmp_files(self):
            run_call_order.append('cleanup_all_tmp_files')

        def cleanup_artifact_dir(self):
            run_call_order.append('cleanup_artifact_dir')


# Generated at 2022-06-13 15:18:19.484454
# Unit test for method run of class StrategyModule

# Generated at 2022-06-13 15:18:30.200448
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestOptions(object):
        module_path = ''
        connection = 'ssh'
        remote_user = ''
        ack_pass = ''
        sudo = False
        sudo_user = ''
        become = False
        become_method = ''
        become_user = ''
        verbosity = 0
        syntax = False
        check = False

    class TestLoader(object):
        pass

    test_options = TestOptions()
    test_loader = TestLoader()

    class TestVariableManager(object):
        def __init__(self):
            self.extra_vars = None
            self.inventory = None

    test_variable_manager = TestVariableManager()

    class TestHost(object):
        def __init__(self, name):
            self.name = name


# Generated at 2022-06-13 15:18:40.425587
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
  mock_iterator = MagicMock(spec=BaseIterators.HostTaskIterator)
  mock_play_context = MagicMock(spec=PlayContext)
  mock_loader = MagicMock(spec=DataLoader)
  mock_tasks = MagicMock(spec=OrderedDict)
  mock_variable_manager = MagicMock(spec=VariableManager)
  mock_host = MagicMock(spec=Host)
  mock_task = MagicMock(spec=Task)
  mock_task_vars = MagicMock(spec=dict)
  mock_result = MagicMock(spec=TaskResult)
  mock_run_once = MagicMock(spec=bool)
  mock_action = MagicMock(spec=ActionBase)
  mock_action_loader = MagicMock(spec=ActionBase)
  mock_task

# Generated at 2022-06-13 15:18:51.478995
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():

    # basic structure of the playbook
    # play -> task1 -> (task2, task3, task4)
    #                                          |
    #                                          |
    #                                          V
    #                                        task5
    #
    # this tests the behavior of StrategyModule.run where new task needs to be
    # inserted in to the queue of the current play.

    mode = 'linear'

    inventory_file = 'test/units/plugins/inventory/test_inventory'
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=inventory_file)
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    class TQM(object):
        '''
        Helper class to simulate ansible.executor.task_queue_manager.TaskQueueManager
        '''


# Generated at 2022-06-13 15:18:52.850291
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule({}, VariableManager())
    print(strategy)
    assert strategy

if __name__ == "__main__":
    test_StrategyModule()

# Generated at 2022-06-13 15:19:34.091335
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    strategy_module = StrategyModule(
        tqm = None
    )
    try:
        strategy_module.run(iterator=None, play_context=None)
    except NotImplementedError as e:
        print(e)
        assert type(e) == NotImplementedError

# Generated at 2022-06-13 15:19:38.049586
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = TaskQueueManager()
    tqm.add_new_inventory(['localhost'])
    f = open('./yml/test_playbook.yml', 'r')
    play = Play.load(f, variable_manager=tqm.variable_manager, loader=tqm.loader)
    str = StrategyModule(tqm, play)
    assert(str is not None)


# Generated at 2022-06-13 15:19:44.904437
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    '''
    Test function run of class StrategyModule.
    '''
    globals()['ansible_diff'] = True
    globals()['ansible_module_generated'] = None
    options = Options()
    options.module_path = './'
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list='/etc/ansible/hosts')
    variable_manager.set_inventory(inventory)

# Generated at 2022-06-13 15:19:55.614058
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.constants as C
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader
    from ansible.plugins.strategy import StrategyBase
    from ansible.vars.manager import VariableManager
    
    my_var_manager = VariableManager()
    my_loader = 'ansible.plugins.loader.action_loader'
    hosts = ['localhost','172.16.1.1','172.16.1.2','172.16.1.3','172.16.1.4','172.16.1.5','172.16.1.6','172.16.1.7','172.16.1.8','172.16.1.9']

# Generated at 2022-06-13 15:20:06.037558
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    this_host = Host('localhost')
    this_loader = DataLoader()
    this_variable_manager = VariableManager()
    this_play_context = PlayContext()
    this_play = Play().load({
        'name': 'test play',
        'hosts': 'localhost',
        'gather_facts': 'no',
        'tasks': [
            {'action': {'module': 'debug', 'args': {'msg': '{{abc}} {{x}}'}}, 'tags': ['always']}
        ]
    }, loader=this_loader, variable_manager=this_variable_manager)
    this_iterator = PlayIterator(this_play, host=this_host, play_context=this_play_context, all_vars=dict())

# Generated at 2022-06-13 15:20:06.644881
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:20:08.401279
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule()


# unit test the StrategyModule class

# Generated at 2022-06-13 15:20:17.432429
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Test with search_strategy_sequential
    strategy_module = StrategyModule()
    strategy_module.set_options()
    strategy_module._tqm = Dummy()
    strategy_module.set_vars(Dummy())
    strategy_module.setup_loader()
    strategy_module.setup_inventory()
    inventory = Dummy()
    strategy_module._inventory = inventory
    strategy_module._variable_manager = Dummy()
    strategy_module._cwd = Dummy()
    strategy_module._final_q = Dummy()
    strategy_module._host_state_callbacks = Dummy()
    strategy_module._final_q = Dummy()
    strategy_module._step = False
    strategy_module._start_at = None

    play_context = Dummy()
    iterator = Dummy()
    iterator

# Generated at 2022-06-13 15:20:29.709516
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    '''
    Unit test for constructor of class StrategyModule
    '''

    module = StrategyModule()
    res = module.get_name()
    assert res == 'linear', res

    cmd = 'ansible-playbook -i inventory/test/hosts.yml playbooks/test/all.yml'

# Generated at 2022-06-13 15:20:31.837245
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule()
    print(strategy)

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:21:56.417165
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    strategy_module = StrategyModule()
    play = Play()
    iterator = PlayIterator()
    play_context = PlayContext()

    # Test 1: Testing all the happy paths
    def get_hosts_left_mock(arg1):
        return ['host1', 'host2', 'host3', 'host4']

# Generated at 2022-06-13 15:21:58.686557
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule()
    assert strategy_module != None

# Generated at 2022-06-13 15:22:02.454819
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule()
    assert isinstance(module._hosts_cache_all, C.defaultdict)
    assert isinstance(module._hosts_cache, C.defaultdict)


# Generated at 2022-06-13 15:22:04.463789
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    StrategyModule.run()
StrategyModule_run = test_StrategyModule_run()


# Generated at 2022-06-13 15:22:06.241270
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # construct a StrategyModule object
    x = StrategyModule()
    assert isinstance(x, StrategyModule)
    assert isinstance(x, BaseStrategyModule)
    assert isinstance(x, object)

# Generated at 2022-06-13 15:22:06.829094
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:22:14.771540
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategymodule = StrategyModule(
        tqm=None,
        variant='linear',
        all_vars=dict(),
        options=dict(),
        loader=None,
        variable_manager=None,
        host_list=None
    )
    assert isinstance(strategymodule, StrategyModule)
    assert strategymodule.run is not None
    assert strategymodule.add_tqm_variables is not None
    assert strategymodule._get_next_task_lockstep is not None
    assert strategymodule.get_hosts_left is not None
    assert strategymodule.update_active_connections is not None
    return strategymodule


# Generated at 2022-06-13 15:22:22.744619
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    #Creating object instances
    inventory = get_inventory("test/test_inventory")
    variable_manager = VariableManager(loader=get_loader("test/test_inventory"))
    loader = get_loader("test/test_playbook")
    variable_manager.set_inventory(inventory)
    passwords = dict(vault_pass='secret')
    variable_manager.extra_vars = {'customer': 'test', 'disabled': 'yes'}
    pm = Play().load("test/test_playbook", variable_manager=variable_manager, loader=loader)
    tqm = None
    play_context = PlayContext()
    strategyModule = StrategyModule(tqm, play_context, variable_manager, loader)
    #Setting passed variables to test methods
    play_context.become = False
    play_context.become_

# Generated at 2022-06-13 15:22:25.403541
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule()
    assert isinstance(module, StrategyModule)
    assert module.__class__.__name__ == 'StrategyModule'



# Generated at 2022-06-13 15:22:32.865863
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Testing StrategyModule constructor")
    tqm = MagicMock()
    tqm._unreachable_hosts = set()
    tqm._failed_hosts = set()
    tqm._stats = MagicMock()
    strategy = StrategyModule(tqm)
    assert strategy._tqm == tqm
    assert strategy._blocked_hosts == {}
    assert strategy._pending_results == 0


# Generated at 2022-06-13 15:25:23.407691
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(tqm=None, variables=dict(), loader='', options=dict(), passwords=dict())
    assert isinstance(strategy_module, StrategyModule)

# Generated at 2022-06-13 15:25:25.971498
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Test with default parameter
    test_StrategyModule_object = StrategyModule()

    # Test with specified parameter
    test_StrategyModule_object_with_para = StrategyModule(tqm=Tqm())
    assert test_StrategyModule_object_with_para.tqm == Tqm()


# Generated at 2022-06-13 15:25:26.910492
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass



# Generated at 2022-06-13 15:25:37.711104
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # StrategyModule()
    # with: play = Play().load(loader=None, variable_manager=None, use_handlers=None,
    #   task_blocks=None, role_blocks=None, include_role_tasks_keys=None,
    #   role_tasks=None, iterator=None, play_hosts=None, play_context=None)
    print("Test StrategyModule().run() ...")
    temp_play = Play().load(loader=None, variable_manager=None, use_handlers=None, task_blocks=None, role_blocks=None, include_role_tasks_keys=None, role_tasks=None, iterator=None, play_hosts=None, play_context=None)
    temp_strategy = StrategyModule(temp_play)
    temp_iterator = None
    temp_

# Generated at 2022-06-13 15:25:48.044455
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import mock
    tqm = mock.Mock()
    inventory = mock.Mock()
    loader = mock.Mock()
    variable_manager = mock.Mock()
    strategy = StrategyModule(tqm, loader, variable_manager, play='', options='', passwords='', inventory='', stdout_callback='', run_additional_callbacks=[], run_tree='', subset=['all'])
    assert strategy._tqm == tqm
    assert strategy._loader == loader
    assert strategy._variable_manager == variable_manager
    assert strategy._play == ''
    assert strategy._options == ''
    assert strategy._passwords == ''
    assert strategy._inventory == ''
    assert strategy._stdout_callback == ''
    assert strategy._run_additional_callbacks == []
    assert strategy._run_tree == ''


# Generated at 2022-06-13 15:25:54.401486
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    print('Unit test for method run of class StrategyModule')

    #Create an instance of class StrategyModule
    strategyModule = StrategyModule()


    #Test attributes of class StrategyModule


    #Test method run of class StrategyModule
    print('Unit test for method run of class StrategyModule')
    test_strategyModule_run_hosts = ["host1"]
    iterator = iterators.SequentialIterator()
    play_context = object()
    test_strategyModule_run_result = strategyModule.run(iterator, play_context)
    print(test_strategyModule_run_result)
    assert(test_strategyModule_run_result == 0)




# Generated at 2022-06-13 15:25:57.185701
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # test with default args
    strategy_module = StrategyModule()
    assert type(strategy_module) is StrategyModule


# Generated at 2022-06-13 15:26:06.312418
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.utils.vars import combine_vars
    import shutil
    from ansible.vars import VariableManager
    from ansible.inventory.manager import InventoryManager

    # create the TQM instance, which manages and coordinates the
    # PlayExecutors

    import os

    # Hack to not use the config.yml in current user directory
    if os.path.exists(os.environ['HOME'] + '/config.yml'):
        shutil.move(os.environ['HOME'] + '/config.yml', '/tmp/config.yml' + os.environ['USER'])

    tqm = TaskQueueManager(
        inventory=InventoryManager(loader=Loader(), sources='localhost,'),
        variable_manager=VariableManager(),
        loader=Loader()
    )

    import os
    t

# Generated at 2022-06-13 15:26:07.577984
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Throws an exception, not tested
    raise NotImplementedError


# Generated at 2022-06-13 15:26:08.766441
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    '''
    Run method of class StrategyModule
    '''
    pass