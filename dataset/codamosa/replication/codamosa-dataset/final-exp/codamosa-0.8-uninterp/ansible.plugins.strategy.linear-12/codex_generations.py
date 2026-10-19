

# Generated at 2022-06-13 15:18:10.631352
# Unit test for method run of class StrategyModule

# Generated at 2022-06-13 15:18:12.131701
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule()
    assert isinstance(s, StrategyModule)


# Generated at 2022-06-13 15:18:17.946770
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    module = StrategyModule()
    test_hosts = [
        'host1',
        'host2'
    ]
    result = module.run(test_hosts)
    assert result == 'test result'


# Generated at 2022-06-13 15:18:19.672814
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    strategy = StrategyModule()
    strategy.run(iterator, play_context)

# Generated at 2022-06-13 15:18:30.320584
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():

    global variable_manager
    variable_manager = VariableManager()
    variable_manager._extra_vars = {'hosts': 'localhost'}

    loader = DataLoader()
    inventory = Inventory(loader=loader, variable_manager=variable_manager)
    variable_manager.set_inventory(inventory=inventory)

    host = Host(name='localhost')
    group = Group(name='ungrouped')
    group.add_host(host)
    inventory.add_group(group)
    inventory.add_host(host)

    from ansible.playbook import Playbook
    from ansible.playbook.play import Play


# Generated at 2022-06-13 15:18:36.303095
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # test object instantiation with the default settings
    strategy = StrategyModule(tqm=None, hosts=None, runner=None)
    # test object instantiation with some settings
    strategy = StrategyModule(tqm=True, hosts=True, runner=True)
    # test object instantiation with some settings
    strategy = StrategyModule(tqm='tqm', hosts='hosts', runner='runner')


# Generated at 2022-06-13 15:18:43.653208
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('test_StrategyModule')

    cur_path = os.path.split(os.path.realpath(__file__))[0]
    conf_file = os.path.join(cur_path, 'ansible.cfg')

    my_loader = DataLoader()
    my_inventory = InventoryManager(my_loader, None, None)
    my_options = Options()
    my_options.connection_user = 'ansible'
    my_options.tree = './hosts'
    my_variable_manager = VariableManager(loader=my_loader, inventory=my_inventory)


# Generated at 2022-06-13 15:18:50.357830
# Unit test for constructor of class StrategyModule

# Generated at 2022-06-13 15:18:51.746168
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule()
    assert sm is not None


# Generated at 2022-06-13 15:18:59.018479
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Instantiate a StrategyModule
    module = StrategyModule()

    # LINUX_DISTRO_NAMES = ['Arch Linux',
    #                       'Debian',
    #                       'Fedora',
    #                       'Gentoo',
    #                       'Linux Mint',
    #                       'openSUSE',
    #                       'PCLinuxOS',
    #                       'Red Hat',
    #                       'Slackware',
    #                       'SUSE',
    #                       'Ubuntu',
    #                       'CentOS',
    #                       'Oracle',
    #                       'FreeBSD',
    #                       'NetBSD',
    #                       'OpenBSD',
    #                       'DragonFly']
    # LINUX_DISTRO_VERSIONS = ['11.10',
    #                          '12.04',
    #                          '12

# Generated at 2022-06-13 15:19:41.825701
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(task_queue_manager=None, inventory=None, variable_manager=None, loader=None, options=None, passwords=None)


# Generated at 2022-06-13 15:19:42.694505
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    strategyModule = StrategyModule()



# Generated at 2022-06-13 15:19:53.218419
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Init variables
    class_object = StrategyModule()
    class_object._tqm = None
    class_object._hosts_cache = None
    class_object._hosts_cache_all = None
    class_object._step = None
    class_object._loader = None
    class_object._variable_manager = None
    class_object._blocked_hosts = None
    class_object._pending_results = None
    class_object._workers = None
    class_object._worker_prune_output = None

    # call the unit under test
    class_object.run(iterator, play_context)
# Magic methods of class StrategyModule

# Generated at 2022-06-13 15:20:04.376193
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule('dir_name_for_download',
                                     'file_name_for_download',
                                     'dir_name_for_templar',
                                     'file_name_for_templar',
                                     'tasks',
                                     'variable_manager',
                                     'variable_manager')
    assert strategy_module._dir_name_for_download == 'dir_name_for_download'
    assert strategy_module._file_name_for_download == 'file_name_for_download'
    assert strategy_module._dir_name_for_templar == 'dir_name_for_templar'
    assert strategy_module._file_name_for_templar == 'file_name_for_templar'
    assert strategy_module._tasks == 'tasks'
   

# Generated at 2022-06-13 15:20:14.021073
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.shell import Shell
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task

    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.role import Role
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.included_file import IncludedFile


# Generated at 2022-06-13 15:20:17.178243
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    strategy_module = StrategyModule(loader=None, variable_manager=None, shared_loader_obj=None,
                                     options=None, passwords=None)
    strategy_module.set_tqm(None)
    
    return strategy_module.run(iterator=None, play_context=None)


# Generated at 2022-06-13 15:20:17.989762
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
  pass

# Generated at 2022-06-13 15:20:19.680073
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule('s') is not None


# Generated at 2022-06-13 15:20:22.072302
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'


# Generated at 2022-06-13 15:20:28.579353
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    options = Options()
    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = Inventory()
    variable_manager.set_inventory(inventory)
    strategy = StrategyModule(loader=loader, variable_manager=variable_manager, options=options)
    iterator = Iterator()
    play_context = PlayContext()
    strategy.run(iterator=iterator, play_context=play_context)


# Generated at 2022-06-13 15:21:20.604342
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    strategy_module = StrategyModule()
    # Test case with first argument as PlayIterator and second argument as PlayContext
    play_iterator = PlayIterator()
    play_context = PlayContext()
    strategy_module.run(play_iterator,play_context)
    # Test case with first argument as PlayIterator and second argument as None
    play_iterator = PlayIterator()
    strategy_module.run(play_iterator,None)


# This class represents default Strategy to be used for running a Play in playbooks.
# The class is also used as a container for methods which are used by all strategies 
# but apply to a specific host.

# Generated at 2022-06-13 15:21:21.993333
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Calling run on the strategy module object
    pass


# Generated at 2022-06-13 15:21:31.563441
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    host1 = Host("127.0.0.1")
    host2 = Host("127.0.0.2")
    host3 = Host("127.0.0.3")

    # host 3 will be missed
    hosts = [host1, host2, host3]

    strategy = StrategyModule(None)

    strategy._tqm = True

    def get_hosts_left_mock():
        '''
        Mock for method get_hosts_left of class StrategyModule
        '''
        return hosts

    strategy.get_hosts_left = get_hosts_left_mock

    hosts_list = [host1, host2, host3]


# Generated at 2022-06-13 15:21:43.714923
# Unit test for method run of class StrategyModule

# Generated at 2022-06-13 15:21:51.733170
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    _loader = DictDataLoader({})
    _inventory = InventoryManager(loader=_loader, sources="")
    variable_manager = VariableManager(_loader, _inventory)
    password_cache = dict()
    strategy = StrategyModule(tqm=None, variable_manager=variable_manager, loader=_loader, inventory=_inventory,
                              stdout_callback='default', passwords=password_cache)
    assert isinstance(strategy, StrategyBase)
    assert strategy._tqm == None
    assert strategy._variable_manager == variable_manager
    assert strategy._loader == _loader
    assert strategy._inventory == _inventory

# Generated at 2022-06-13 15:22:04.568660
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule()
    assert(module._tqm == None)
    assert(module._tqm._initial_variables == None)
    assert(module._tqm._hostvars == None)
    assert(module._tqm._variable_manager == None)
    assert(module._tqm._notified_handlers == None)
    assert(module._tqm._listeners == None)
    assert(module._tqm._failed_hosts == None)
    assert(module._tqm._ran_once_hosts == None)
    assert(module._tqm._stats == None)
    assert(module._tqm._workers == None)
    assert(module._tqm._inventory == None)
    assert(module._tqm._loader == None)

# Generated at 2022-06-13 15:22:09.967561
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from collections import namedtuple
    from ansible.playbook.play_context import PlayContext

    playbook = namedtuple('playbook', ['tests'])
    host = namedtuple('host', ['name'])
    play = namedtuple('play', ['hosts'])
    iterator = namedtuple('iterator', ['_play', '_tasks'])
    tqm = namedtuple('tqm', ['_failed_hosts'])
    task_result = namedtuple('task_result', ['_host', '_task', 'is_failed', 'is_unreachable', '_result'])

    args = {
        'hostvars': {'host': {}},
        'hostnames': ['host'],
        'inventory': {},
        'playbook': playbook(tests=True)
    }

   

# Generated at 2022-06-13 15:22:15.529227
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
  # set up
  StrategyModule._tqm.RUN_OK = 0
  StrategyModule._tqm.RUN_FAILED_BREAK_PLAY = 0
  StrategyModule._tqm.RUN_UNKNOWN_ERROR = 0
  play_context = PlayContext()
  iterator = IteratorModule()
  StrategyModule.run(StrategyModule(), iterator, play_context)

# Generated at 2022-06-13 15:22:27.434098
# Unit test for method run of class StrategyModule

# Generated at 2022-06-13 15:22:32.131765
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    '''Unit test
    '''
    tqm = TaskQueueManager(
        inventory=InventoryManager(host_list=[]),
        variable_manager=VariableManager(),
        loader=DataLoader(),
    )
    strategy = StrategyModule(tqm)
    assert strategy.name == "Free"


# Generated at 2022-06-13 15:24:04.481358
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule()
    assert strategy_module is not None


# Generated at 2022-06-13 15:24:14.796103
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Setup testing
    self = StrategyModule()
    self.create_tmp_dirs() # we use a tmp dir to store all the temp files that would normally be created by the strategy module
    self.setup_connection_mock() # create the mocks we need to fake the ansible connection.
    self.mock_config_module() # create the mocks we need to fake the ansible connection.

    # Generate the play to test

# Generated at 2022-06-13 15:24:19.949267
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():

    # test case 1
    iterator = Mock()
    p_context = Mock()
    s_module = StrategyModule(Mock())
    # test with only parameter iterator
    result = s_module.run(iterator)
    assert result == s_module._tqm.RUN_OK

    # test case 2
    # test with all parameters
    result = s_module.run(iterator, p_context)
    assert result == s_module._tqm.RUN_OK

# Generated at 2022-06-13 15:24:22.199157
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = TaskQueueManager(inventory=InventoryManager(loader=Loader(), sources='localhost,'))
    strategy = StrategyModule(tqm)


# Generated at 2022-06-13 15:24:23.905266
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule()

    assert(strategy_module is not None)



# Generated at 2022-06-13 15:24:29.658979
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = TaskQueueManager(
        inventory=InventoryManager(loader=DataLoader()),
        variable_manager=VariableManager(),
        loader=DataLoader(),
    )
    host = Host('localhost')
    task = Task()
    task.set_loader(DataLoader())
    strategy = StrategyModule(tqm, host, task)
    strategy2 = StrategyModule(tqm, host, task)
    assert strategy == strategy2

# Generated at 2022-06-13 15:24:32.525220
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    class MyStrategyModule(StrategyModule):
        pass

    module = MyStrategyModule()
    assert isinstance(module, StrategyModule)

# Generated at 2022-06-13 15:24:41.978013
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    playbook_path = '~/ansible-repo/'
    inventory_path = '~/ansible-repo/bin/ansible-inventory'
    variable_manager_path = '~/ansible-repo/bin/python'

    # strategy manager preparation
    # ----------------------------
    strategy_manager = StrategyModule()

# Generated at 2022-06-13 15:24:52.444587
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    display.current_displayer = display.Display(verbosity=1)

    class Dummy:
        pass

    class DummyVariableMgr:
        def __init__(self):
            self.vars = [None, None]

        def get_vars(self, play, task=None, host=None):
            return self.vars

    class DummyLoader:
        pass

    class DummyPlay:
        def __init__(self):
            self.become = False
            self.become_method = 'sudo'
            self.become_user = 'foo'

    # missing params
    with pytest.raises(AssertionError):
        StrategyModule(tqm=Dummy(), inventory=Dummy(), variable_manager=Dummy(), loader=Dummy())

    # missing params

# Generated at 2022-06-13 15:24:58.491960
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(tqm=Mock_tqm())
    assert strategy_module._tqm == Mock_tqm()
    assert strategy_module._inventory == Mock_inventory()
    assert strategy_module._notified_handlers == []
    assert strategy_module._blocked_hosts == {}
    assert strategy_module._tqm.callback_queues == {}
    assert strategy_module._tqm.result_queue == Mock_result_queue()
    assert strategy_module._tqm.default_callback_queue == Mock_result_queue()
    assert strategy_module._tqm.stats == Mock_play_stats()

# Unit test cleaning up