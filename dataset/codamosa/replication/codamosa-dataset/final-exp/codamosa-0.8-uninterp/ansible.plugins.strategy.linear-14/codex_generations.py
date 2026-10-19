

# Generated at 2022-06-13 15:18:01.949704
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule()


# unit test for update_active_connections() of class StrategyModule

# Generated at 2022-06-13 15:18:03.176804
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategyModule = StrategyModule()
    assert strategyModule is not None


# Generated at 2022-06-13 15:18:04.100987
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    r=StrategyModule()
    pass

# Generated at 2022-06-13 15:18:09.295871
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Instantiate a mock object for the iterator function
    Iterator = mock.Mock()
    strategy_obj = StrategyModule()
    # Instantiate a mock object for the play_context function
    PlayContext= mock.Mock()
    strategy_obj.run(Iterator, PlayContext)
    # This will invoke the magic method __str__() on the mock object
    assert str(Iterator) == '<Mock id=1>'
    assert str(PlayContext) == '<Mock id=2>'


# Generated at 2022-06-13 15:18:15.083195
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    import mock
    import ansible.playbook.play_context
    import ansible.playbook.task
    import ansible.executor.task_result
    import ansible.playbook.block
    import ansible.playbook.included_file
    import ansible.playbook.play
    import ansible.playbook.templar
    import ansible.template.safe_eval
    import ansible.template.vars
    import ansible.template.jinja2_native
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.stats import AggregateStats
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

# Generated at 2022-06-13 15:18:19.209695
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    return True
# unit tests go here
if __name__ == '__main__':
    print("Running unit tests")
    print("Running test StrategyModule" + test_StrategyModule())
    print("Unit tests complete")

# Generated at 2022-06-13 15:18:30.044959
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.playbook.play_iterator import PlayIterator
    from ansible.executor import task_queue_manager
    from ansible.utils.vars import combine_vars
    import ansible.parsing.dataloader
    import ansible.inventory
    import ansible.playbook.task
    import ansible.playbook.play
    import ansible.playbook.block
    import ansible.plugins
    import ansible.plugins.loader
    loader_class=ansible.parsing.dataloader.DataLoader
    from ansible.playbook.play_context import PlayContext
    loader = loader_class('/')
    inventory = ansible.inventory.Inventory(loader=loader, variable_manager=None, host_list='tests/inventory')

# Generated at 2022-06-13 15:18:31.438177
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass


# Generated at 2022-06-13 15:18:32.967816
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    mod = StrategyModule()
    iterator = None
    iterator = StrategyModule()
    play_context = None
    play_context = StrategyModule()
    mod.run(play_context, iterator)

# Generated at 2022-06-13 15:18:37.486789
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule()
    assert repr(s) == "<ansible.executor.task_queue_manager.StrategyModule object at 0x%x>" % id(s)


# Generated at 2022-06-13 15:19:30.907290
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # noinspection PyUnusedLocal
    def mock_get_hosts_left(self, iterator):
        return [1,2,3]
    # noinspection PyUnusedLocal
    def mock_get_next_task_lockstep(self, hosts_left, iterator):
        return {(1,2),(3,4),(5,6)}

    def mock_set_hosts_cache(self, play):
        return

    play_context = {}
    iterator = Iterator({},[])
    self = StrategyModule(None, None, 0, None, None)
    self._get_hosts_left = mock_get_hosts_left.__get__(self,StrategyModule)

# Generated at 2022-06-13 15:19:38.468713
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert TypeError is not None
    try:
        StrategyModule(None, None, None, None,
                                   None, None, None, None, None, None)
    except (TypeError,ValueError) as e:
        assert False, 'Invalid Argument Type is not allowed, Error: ' + str(e)
    tqm = TaskQueueManager(None, None, None, None, None)
    strategy_module = StrategyModule(tqm, None, None, None,
                                   None, None, None, None, None, None)
    assert tqm == strategy_module._tqm

# test for _set_hosts_cache() of class StrategyModule

# Generated at 2022-06-13 15:19:49.647508
# Unit test for constructor of class StrategyModule

# Generated at 2022-06-13 15:20:01.609739
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule(
        tqm=Mock(name='tqm'),
        inventory=Mock(name='inventory'),
        variable_manager=Mock(name='variable_manager'),
        loader=Mock(name='loader'),
        options=Mock(name='options'),
        passwords=Mock(name='passwords'),
    )

    assert module._tqm == 'tqm'
    assert module._inventory == 'inventory'
    assert module._variable_manager == 'variable_manager'
    assert module._loader == 'loader'
    assert module._options == 'options'
    assert module._passwords == 'passwords'
    assert module._blocked_hosts == {}
    assert module._workers_available == []
    assert module._pending_results == 0
    assert module._hosts_cache == {}


# Generated at 2022-06-13 15:20:08.462851
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule()
    assert strategy._tqm is None
    assert strategy._inventory is None
    assert strategy._variable_manager is None
    assert strategy._loader is None
    assert strategy._shared_loader_obj is None
    assert strategy._final_q is None
    assert strategy._blocked_hosts is None
    assert strategy._pending_results is None
    assert strategy._workers is None
    assert strategy._notified_handlers is None
    assert strategy._step is None
    assert strategy._hosts_cache is None
    assert strategy._hosts_cache_all is None


# Unit tests for add_tqm_variables function in class StrategyModule

# Generated at 2022-06-13 15:20:17.504875
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # create a fake loader
    loader_mock = MagicMock()
    loader_mock.path_dwim.return_value = "/data/ansible/playbooks/playbook.yml"

    # create a fake inventory, playbook and iterator
    inventory_mock = MagicMock()
    inventory_mock.get_hosts.return_value = []
    playbook_mock = MagicMock()
    playbook_mock.get_vars.return_value = {}
    play_iterator_mock = MagicMock()
    play_iterator_mock._play = playbook_mock

    # create a fake variable manager
    variable_manager_mock = MagicMock()
    variable_manager_mock.get_vars.return_value = {}
    variable_manager_mock.extra_vars = {}

# Generated at 2022-06-13 15:20:29.786387
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    options = {'_private': False, '_ansible_version': None, '_ansible_verbosity': 0}
    ansible_dir = tempfile.mkdtemp()
    display_name = 'test_host'
    environment = Environment(loader=DictDataLoader({}), variable_manager=VariableManager())
    inventory = InventoryManager(loader=DictDataLoader({}), sources=['localhost'])
    variable_manager = VariableManager(loader=DictDataLoader({}), inventory=inventory)
    ansible_playbook_basedir = '/tmp'
    ansible_playbook_path = None
    ansible_play_basedir = None

# Generated at 2022-06-13 15:20:33.074374
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Initializing the test
    strategymodule_instance = StrategyModule()

    # Check for false positives 
    assert strategymodule_instance.run() == False 

    # Check for false negatives
    assert strategymodule_instance.run() == True


# Generated at 2022-06-13 15:20:35.572525
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    module = AnsibleModule({})
    StrategyModule.run(module, module,module)

# ********************** class StrategyBase ************************

# Generated at 2022-06-13 15:20:44.968782
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    fake_iterator = MagicMock()
    fake_play_context = MagicMock()
    fake_host = MagicMock()
    fake_host.get_name = MagicMock(return_value="test_host")
    fake_task = MagicMock()
    fake_task.action = MagicMock(return_value="test_action")
    fake_task.any_errors_fatal = MagicMock(return_value=False)
    fake_task.ignore_errors = MagicMock(return_value=True)
    fake_task.args = MagicMock(return_value={"_raw_params": "one_task"})
    fake_task.collections = MagicMock(return_value="collection_list")

    fake_task_vars = MagicMock()
    fake_templar = MagicMock

# Generated at 2022-06-13 15:22:15.485113
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(1, 2, 3, 4, 5, 6, 7, 8)
    assert strategy_module.name == 'linear'
    assert strategy_module._tqm == 1
    assert strategy_module._inventory == 2
    assert strategy_module._variable_manager == 3
    assert strategy_module._loader == 4
    assert strategy_module._options == 5
    assert strategy_module._passwords == 6
    assert strategy_module._stdout_callback == 7
    assert strategy_module._run_additional_callbacks == 8
    assert strategy_module._task_queue_manager == None
    assert strategy_module._blocked_hosts == {}
    assert strategy_module._pending_results == 0
    assert strategy_module._hosts_cache == None
    assert strategy_module._hosts_cache_all == None

# Generated at 2022-06-13 15:22:23.259838
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    '''
    Unit test for method run of class StrategyModule
    '''

    # Create a mock object for a temporary file
    mock_file = MagicMock(spec=_io.TextIOWrapper)
    mock_file.write = MagicMock(name="write")
    mock_file.close = MagicMock(name="close")
    mock_file.seek = MagicMock(name="seek")
    mock_file.read = MagicMock(return_value=str("\x00\x00\x00\x00"), name="read")

    # Create a mock object for a task
    mock_task = MagicMock(spec=Task)
    mock_task.action = "test"
    mock_task.async_val = None
    mock_task.args = {}

# Generated at 2022-06-13 15:22:33.181965
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    iterator = "iterator"
    play_context = "play_context"
    BaseStrategy.run.__dict__.__setitem__('stypy_call_defaults', defaults)
    StrategyModule.run.__dict__.__setitem__('stypy_call_varargs', varargs)
    StrategyModule.run.__dict__.__setitem__('stypy_call_kwargs', kwargs)
    StrategyModule.run.__dict__.__setitem__('stypy_declared_arg_number', 3)
    arguments = process_argument_values(localization, type_of_self, module_type_store, 'StrategyModule.run', ['iterator', 'play_context'], None, None, defaults, varargs, kwargs)


# Generated at 2022-06-13 15:22:35.638445
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """
    Test the constructor of the StrategyModule class
    """
    tqm = TaskQueueManager()
    strategymodule = StrategyModule(tqm, tqm._host_manager)



# Generated at 2022-06-13 15:22:36.815438
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  strategy = StrategyModule(Tqm())
  assert strategy != None


# Generated at 2022-06-13 15:22:48.725400
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play

    # Create play, variable manager, and Data loader object
    variable_manager = VariableManager()
    loader = DataLoader()
    play = Play()
    # Create playbook variable manager
    variable_manager = VariableManager()
    variable_manager.set_inventory(InventoryManager(loader=loader, sources='localhost,'))
    loader = DataLoader()
    # Create task queue manager object

# Generated at 2022-06-13 15:22:56.479780
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Mock class for iterator
    class MockIterator:
        def __init__(self):
            pass

        def __iter__(self):
            return self

        def __next__(self):
            raise StopIteration

    # Mock class for play_context
    class MockPlayContext(object):
        def __init__(self):
            self.remote_addr = 'remote_addr'
            self.password = 'password'
            self.port = 'port'
            self.become = 'become'
            self.become_method = 'become_method'
            self.become_user = 'become_user'
            self.connection = 'connection'
            self.timeout = 'timeout'
            self.network_os = 'network_os'
            self.remote_user = 'remote_user'

# Generated at 2022-06-13 15:23:02.987067
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    fake_loader = DictDataLoader({})
    fake_play = Play().load(dict(
        name = "test",
        hosts = 'localhost',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(__ansible_module__='shell', __ansible_arguments__=dict(cmd='/bin/false'))),
            dict(action=dict(__ansible_module__='shell', __ansible_arguments__=dict(cmd='/bin/false')))
        ]
    ), loader=fake_loader)

    results = []

    def fake_queue_task(host, task, task_vars, play_context):
        results.append(FakeTaskResult(host, task, task_vars, play_context))


# Generated at 2022-06-13 15:23:11.795359
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(tqm=None)
    assert sm._step == False
    assert sm._last_task_banner == None
    assert sm._tqm == None
    assert sm._variable_manager == None
    assert sm._hosts_cache == None
    assert sm._hosts_cache_all == None
    assert sm._loader == None

# Generated at 2022-06-13 15:23:13.824715
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule()
    assert(sm is not None)

if __name__ == "__main__":
    test_StrategyModule()

# Generated at 2022-06-13 15:26:29.035964
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule()

# Generated at 2022-06-13 15:26:32.105314
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from units.mock.loader import DictDataLoader
    from units.mock.inventory import MockInventory

    loader = DictDataLoader({})
    inventory = MockInventory()
    tqm = MockTaskQueueManager(inventory=inventory, loader=loader, options=None)
    strategy = StrategyModule(tqm)
    play_context = {'verbosity': 3}
    iterator = TaskIterator()
    strategy.run(iterator, play_context)


# Generated at 2022-06-13 15:26:35.004506
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule()
    assert strategy_module.get_name() == 'linear'


# Generated at 2022-06-13 15:26:43.712359
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    TASKS = [
        dict(action=dict(_raw_params="echo 'hello'"), register='out'),
        dict(action=dict(_raw_params="echo 'world'"), register='out'),
    ]

    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.loader import action_loader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.vars.manager import VariableManager

    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()

    # create inventory, and populate with hosts
    inventory = InventoryManager(loader=loader, sources=['localhost,'])
    variable_manager = Variable

# Generated at 2022-06-13 15:26:50.325051
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from units.mock.loader import DictDataLoader
    from units.mock.inventory import Host, Inventory

    loader = DictDataLoader({})
    variable_manager = VariableManager()

    hosts = []
    host = Host(name='host1', variable_manager=variable_manager)
    hosts.append(host)
    inventory = Inventory(loader=loader, variable_manager=variable_manager, hosts=hosts)

    _ = StrategyModule(loader=loader, inventory=inventory)


# Generated at 2022-06-13 15:26:57.844284
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # setup test
    class TestTask1(Task):
        def __init__(self,name='test_task_1', module_args=None,):
            self.action = 'test_module'
            self.name = name
    class TestTask2(Task):
        def __init__(self,name='test_task_2', module_args=None,):
            self.action = 'test_module'
            self.name = name
    class TestTask3(Task):
        def __init__(self,name='test_task_3', module_args=None,):
            self.action = 'test_module'
            self.name = name

# Generated at 2022-06-13 15:27:00.523171
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule(None)

    assert module is not None

# Generated at 2022-06-13 15:27:01.217693
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass


# Generated at 2022-06-13 15:27:08.474006
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    loader_mock = unittest.mock.Mock()
    inventory_mock = unittest.mock.Mock()
    variable_manager_mock = unittest.mock.Mock()
    stdout_callback_mock = unittest.mock.Mock()
    runner_callbacks = RunnerCallbacks()
    logger = unittest.mock.Mock()
    tqm = unittest.mock.Mock()
    stdout_callback_mock = unittest.mock.Mock()

    plugin_mock = unittest.mock.Mock()
    plugin_mock.run = unittest.mock.Mock()


    strategy_module = StrategyModule(tqm, variable_manager=variable_manager_mock)

    strategy_module

# Generated at 2022-06-13 15:27:19.511605
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    '''
    Test case for method run of class StrategyModule
    '''
    loader_mock = MagicMock()
    tqm_mock = MagicMock()
    strategy_module = StrategyModule(loader_mock, tqm_mock)
    iterator_mock = MagicMock()
    play_context_mock = MagicMock()
    strategy_module.run(iterator_mock, play_context_mock)
    assert strategy_module._set_hosts_cache.called
    assert strategy_module.get_hosts_left.called
    assert strategy_module._get_next_task_lockstep.called
    assert strategy_module._step.called
    assert strategy_module._take_step.called
    assert strategy_module._execute_meta.called