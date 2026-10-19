

# Generated at 2022-06-13 15:18:08.176099
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    '''
    Test method run of class StrategyModule
    '''
    mock_loader = MagicMock(spec=DataLoader)
    mock_variable_manager = MagicMock(spec=VariableManager)
    mock_task_queue_manager = MagicMock(spec=TaskQueueManager(loader=mock_loader, variable_manager=mock_variable_manager, options=Options()))
    mock_task_queue_manager.RUN_OK = 0
    mock_task_queue_manager.RUN_UNKNOWN_ERROR = 1
    mock_task_queue_manager.RUN_FAILED_BREAK_PLAY = 2
    mock_task_queue_manager._workers = MagicMock()
    mock_task_queue_manager._tqm_has_run = False
    mock_task_queue_manager._workers_lock = Magic

# Generated at 2022-06-13 15:18:17.502748
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    def helper(result, iterator, play_context, next_task, to_text_conversion):
        # Setup parameters
        class Tqm():
            RUN_OK = 0
        class IncludedFile(object):
            load_result = None
            def load_file_vars(self, file_name, loader, play, variable_manager):
                return IncludedFile.load_result
            def process_include_results(self, host_results, iterator, loader, variable_manager):
                return IncludedFile.process_include_results_result
        class Iterator(object):
            debug_enabled = False
            included_file = IncludedFile()
            iterating_result = True
            is_failed_result = False
            mark_host_failed_result = False
            def get_active_state(self, s):
                return self.get_active

# Generated at 2022-06-13 15:18:28.291913
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    config = ConfigParser.ConfigParser()
    config.read('ansible.cfg')
    vault_secret = None
    loader = DataLoader()
    variable_manager = VariableManager()


# Generated at 2022-06-13 15:18:39.394611
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # create a mock inventory object
    inventory = MockInventory()

    # create a mock options object
    options = MockOptions()

    # create a mock loader object
    loader = MockLoader()

    # create a mock variable manager object
    variable_manager = MockVariableManager()

    # create a mock shared plugin loader object
    shared_plugin_loader = MockPluginLoader()

    def dummy_callback(*args, **kwargs):
        return 0

    # create a mock callback plugin
    callback_plugin = MockCallbackPlugin()
    callback_plugin.v2_on_any = dummy_callback
    callback_plugin.v2_runner_on_failed = dummy_callback
    callback_plugin.v2_runner_on_ok = dummy_callback
    callback_plugin.v2_runner_on_skipped = dummy_callback
    callback_plugin.v

# Generated at 2022-06-13 15:18:39.998503
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:18:41.881602
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule()
    assert isinstance(obj, StrategyModule)

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:18:42.907619
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass


# Generated at 2022-06-13 15:18:53.975698
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Create TASK_MAP
    run_once_task = dict()
    run_once_task['action'] = 'ping'
    run_once_task['async'] = 1
    run_once_task['any_errors_fatal'] = False
    run_once_task['always_run'] = False
    run_once_task['become'] = False
    run_once_task['become_user'] = ''
    run_once_task['become_method'] = ''
    run_once_task['become_flags'] = ''
    run_once_task['register'] = ''
    run_once_task['notify'] = ''
    run_once_task['tags'] = []
    run_once_task['when'] = ''
    run_once_task['sudo_user'] = ''
   

# Generated at 2022-06-13 15:18:56.238418
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # mock data
    loader = None
    tqm = None
    variables = None
    iterator = None
    play_context = None
    strategy = StrategyModule(loader=loader, tqm=tqm, variables=variables)
    assert strategy.run(iterator, play_context) == Result.FAILURE


# Generated at 2022-06-13 15:19:07.748000
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.module_utils.six import PY3
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play_context import PlayContext

    inventory1 = InventoryManager(loader=DataLoader(), sources='localhost,')
    variable_manager1 = VariableManager()
    play_context1 = PlayContext()

    strategy_module1 = StrategyModule()
    result1 = strategy_module1.run(iterator, play_context1)

    assert result1 in [1,2,3,4,5]

    # if PY3:
    #     assert isinstance(result1, int)
    # else:
    #     assert isinstance(result1, long)

# Unit test

# Generated at 2022-06-13 15:19:47.463393
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(TQM())
    print(strategy_module)
    assert strategy_module.__class__.__name__ == 'StrategyModule'

# Generated at 2022-06-13 15:19:53.752543
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    """
    Test run() of StrategyModule.
    """
    strategy_module = StrategyModule(
        tqm = None,
        strategy = None,
        strategy_hash = None,
        loader = None,
        variable_manager = None,
        host_list = None,
        play = None,
        options = None,
        passwords = None,
    )
    assert strategy_module.run(iterator = None, play_context = None) == None


# Generated at 2022-06-13 15:19:57.433874
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    task_queue_manager = TaskQueueManager()
    variable_manager = VariableManager()
    loader = DataLoader()
    strategy_module = StrategyModule(task_queue_manager=task_queue_manager, variable_manager=variable_manager, loader=loader)
    assert (strategy_module._tqm is task_queue_manager and strategy_module._variable_manager is variable_manager and strategy_module._loader is loader)


# Generated at 2022-06-13 15:20:02.547075
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    task = MagicMock()
    iterator = MagicMock()
    play_context = MagicMock()
    s = StrategyModule()
    s.run(iterator, play_context)


#  the strategy class is the main entry point for executing plays
#  the strategy classes must override the strategy() method to call
#  the correct strategy callback(s)

# Generated at 2022-06-13 15:20:04.421877
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Arrange
    # Act
    # Assert
    pass

# Generated at 2022-06-13 15:20:06.265533
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule()
    assert strategy_module.__class__.__name__ == 'StrategyModule'


# Generated at 2022-06-13 15:20:16.068490
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    mock_iter = MagicMock()
    mock_iter.run_state = 'test'
    mock_iter.batch_size = 1
    mock_iter.hostvars = MagicMock()
    mock_iter.hostvars.get.return_value = 'test'
    mock_iter._play = MagicMock()
    mock_iter._play._included_filenames = []

# Generated at 2022-06-13 15:20:19.728011
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  t = StrategyModule()
  if t:
     print('StrategyModule() constructor test passed')
  else:
     print('StrategyModule() constructor test failed')

test_StrategyModule()


# Generated at 2022-06-13 15:20:31.400051
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    l1 = ['module1', 'module2', 'module3']
    l2 = ['task1', 'task2', 'task3']
    l3 = ['host1', 'host2', 'host3']
    l4 = {'host1':'host1', 'host2':'host2'}
    l5 = ['host1', 'host2', 'host3']

    obj = StrategyModule()

    obj.add_tqm_variables = MagicMock(return_value=None)
    obj._execute_meta = MagicMock(return_value='test')
    obj._variable_manager = MagicMock()
    obj._get_next_task_lockstep = MagicMock(return_value=l1)
    obj._queue_task = MagicMock(return_value=None)
    obj._process_p

# Generated at 2022-06-13 15:20:37.745403
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # test case 1
    iterator = None
    play_context = PlayContext(play=None, options=Options(), passwords={})
    strategy_module = StrategyModule(tqm=None)
    result = strategy_module.run(iterator, play_context)
    assert result == 0

    # test case 2
    iterator = Iterator(play=None, play_context=None, hosts=None, variable_manager=None, all_vars=None,
                        run_tree=None, loader=None, path_loader=None)
    play_context = PlayContext(play=None, options=Options(), passwords=None)
    strategy_module = StrategyModule(tqm=None)
    result = strategy_module.run(iterator, play_context)
    assert result == None

    # test case 3
    iterator = None
    play_context

# Generated at 2022-06-13 15:21:54.601193
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from units.mock.loader import DictDataLoader
    loader = DictDataLoader({})
    iterator = PassThroughUnsafeIterable()


# Generated at 2022-06-13 15:22:06.958856
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    loader_mock = MagicMock()
    host_mock = Host(name='127.0.0.1')
    host_mock.get_name.return_value = "127.0.0.1"
    role_metadata_mock = MetaData()
    role_metadata_mock = role_metadata_mock
    role_mock = MagicMock()
    role_mock.has_run.return_value = True
    role_mock._metadata.allow_duplicates = False
    action_mock = ActionBase()
    action_mock.BYPASS_HOST_LOOP = True
    loader_mock.get.return_value = action_mock
    iterator = MagicMock()
    iterator._play = MagicMock()
    iterator._play.max_fail_percentage = 1

# Generated at 2022-06-13 15:22:13.874936
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    strategy_module = StrategyModule()
    strategy_module.set_loader()
    strategy_module.set_variable_manager()
    strategy_module.set_inventory()
    strategy_module.set_tqm()
    strategy_module.set_queue_manager()

    module_args = {'name': 'ping', '_original_file': 'ping.yml'}
    play_context = magicmock()

    task = Task(action=dict(module='ping', args=module_args))
    iterator = BaseIterator(play=play, play_context=play_context)

    result = strategy_module.run(iterator, play_context)
    assert result == 1


# Generated at 2022-06-13 15:22:22.168475
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    host_list, target_list = [], []
    test_strategy_module = StrategyModule(loader=None, templar=None, hosts=host_list, queue=None,
                                          variable_manager=None, loader_cache=None, shared_loader_obj=False,
                                          run_additional_callbacks=None, callbacks=None, stdout_callback=None,
                                          options=None, default_vars=None, passwords=None, index=None, iterator=None,
                                          connection_info=None, subset=target_list, run_tree=False,
                                          S=1, R=1, start_at_step=None, step_count=None)

    test_strategy_module._initialize_processes(1)

# Generated at 2022-06-13 15:22:23.729224
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    my_play = Play()
    my_play._role = None
    my_play._hosts = 'host1,host2,host3'
    pass



# Generated at 2022-06-13 15:22:33.577972
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    m_module_utils_basic.AnsibleModule = mock.Mock()
    m_module_utils_basic.AnsibleModule.fail_json.__name__ = 'fail_json'
    m_module_utils_basic.AnsibleModule.exit_json.__name__ = 'exit_json'

    strategy_module = StrategyModule()

    m_module_utils_basic.AnsibleModule.run_command.return_value = (1, "a", "b")
    m_module_utils_basic.AnsibleModule.get_bin_path.return_value = "a"
    m_module_utils_basic.AnsibleModule.boolean.return_value = False

    m_module_utils_basic.AnsibleModule.fail_json.assert_not_called()
    m_module_utils

# Generated at 2022-06-13 15:22:40.525892
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestStrategyModule(StrategyModule):
        def __init__(self):
            self._tqm = TaskQueueManager(0)
            self._inventory = FakeMain()
            self._play_context = FakeMain()
            self._variable_manager = FakeMain()
            self._loader = FakeMain()
            self._shared_loader_obj = FakeMain()
            self._final_q = FakeMain()
            self._blocked_hosts = FakeMain()
            self._tqm._stdout_callback = FakeMain()
            self._tqm._failed_hosts = FakeMain()
            self._tqm._stats = FakeMain()
            self._tqm._host_failed_checked = FakeMain()
            self._tqm._host_failed_started = FakeMain()


# Generated at 2022-06-13 15:22:42.981401
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategyModule = StrategyModule()


# test_StrategyModule()

# Generated at 2022-06-13 15:22:45.194884
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    '''
    This is a unit test for testing StrategyModule.run
    '''
    pass

# Generated at 2022-06-13 15:22:46.913494
# Unit test for constructor of class StrategyModule

# Generated at 2022-06-13 15:25:33.231360
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    global options
    strategy_module = StrategyModule(get_connection=get_connection, load_callback_plugins=load_callback_plugins, runner_callbacks=runner_callbacks)
    strategy_module.run(iterator, play_context)
    assert True



# Generated at 2022-06-13 15:25:34.255508
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:25:44.256941
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # test StrategyModule.__init__()
    loader = DictDataLoader({})
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager)

    hosts = inventory.get_hosts()
    inventory.add_hosts(hosts)
    host_list = [host.name for host in hosts]


# Generated at 2022-06-13 15:25:53.193600
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    opts = namedtuple('opts', ['connection','module_path','forks','become','become_method','become_user','check','listhosts','listtasks','listtags','syntax'])
    opts.connection='smart'
    opts.module_path=None
    opts.forks=5
    opts.become=None
    opts.become_method=None
    opts.become_user=None
    opts.check=False
    opts.listhosts=False
    opts.listtasks=False
    opts.listtags=False
    opts.syntax=False
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager,  host_list='tests/inventory')

# Generated at 2022-06-13 15:26:04.031733
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    module = AnsibleModule(
        argument_spec = dict(
            module=dict(type='str'),
            group=dict(type='list'),
            order=dict(default='linear', choices=['linear']),
            _hosts=dict(type='list'),
        )
    )

    module_mock = MagicMock(module)
    module_mock.params = dict(
            module=dict(type='str'),
            _hosts=dict(type='list'),
    )
    module_mock.check_mode = False
    module_mock.debug = False
    module_mock.no_log = False
    module_mock.changed = True
    module_mock.diff = True

    strategy_module = StrategyModule(module_mock)

# Generated at 2022-06-13 15:26:10.801669
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    """
    Unit test for method run of class StrategyModule
    """
    tqm = TaskQueueManager(inventory=InventoryManager(loader=None, sources="localhost"))
    play = Play().load(dict(
        name = "Ansible Play",
        hosts = "all",
        gather_facts = "no",
        tasks = [dict(action=dict(module="command", args=dict(cmd="ls")))]
    ), variable_manager=VariableManager(), loader=DataLoader())
    StrategyModule(tqm).run(iterator=play.get_iterator(), play_context=play._play_context)


# Generated at 2022-06-13 15:26:15.179781
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():

    # create an instance of the class to be tested
    strategy_instance = StrategyModule()

    strategy_instance._initialize()
    strategy_instance.set_connection_info()

    # define test input data
    iterator = iterator()
    play_context = play_context()



# Generated at 2022-06-13 15:26:17.630371
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategyModule = StrategyModule(tqm = None, all_vars = None)
    assert strategyModule.get_name() == 'LINUX_RULES'

# Generated at 2022-06-13 15:26:26.061046
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager

    loader = None
    variable_manager = None
    ansible_vars = {"test_variable": "test_value"}

    playtest = Play().load(dict(
        name="Ansible Play Test",
        hosts='webservers',
        gather_facts='no',
        tasks=[
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
         ]
    ), loader=loader, variable_manager=variable_manager)

    iterator = playtest.get_iterator()

    play_

# Generated at 2022-06-13 15:26:31.085767
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.template import Templar
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.process.result import TaskResult
    
    
    tqm = mock.MagicMock()
    tqm._terminated = False
    loader = mock.MagicMock()
    inventory = InventoryManager(loader=loader, sources=["unit.test"])
    variable_manager = mock.MagicMock()
    play_context = PlayContext(play=Play())
    iterator = mock.MagicMock()
    iterator._play = Play()
    iterator.iterator_good_for_pipelining = False
    iterator.iterator_good_for_