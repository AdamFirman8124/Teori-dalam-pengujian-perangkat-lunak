

# Generated at 2022-06-13 15:06:54.031205
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    tqm = Mock()
    iterator = Mock()
    play_context = Mock()
    strategyModule = StrategyModule(tqm)
    strategyModule._tqm = Mock()
    iterators = []
    for i in range(5000):
        iterator1 = Mock()
        iterator1.get_next_task_for_host.return_value = i
        iterators.append(iterator1)
    strategyModule._queue_task.return_value = None
    strategyModule._wait_on_pending_results.return_value = iterators
    strategyModule._process_pending_results.return_value = iterators
    strategyModule.get_hosts_left.return_value = iterators
    strategyModule.run(iterator, play_context)

# Generated at 2022-06-13 15:07:05.664496
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    import copy
    import mock
    import unittest2
    from ansible import errors
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.included_file import IncludedFile
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_result import TaskResult
    from ansible.vars.manager import VariableManager

   

# Generated at 2022-06-13 15:07:09.219078
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    module_strategy = StrategyModule(tqm)
    assert module_strategy.tqm == tqm
    assert module_strategy._host_pinned == False


# Generated at 2022-06-13 15:07:16.532413
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    tqm = TaskQueueManager()
    tqm.host_list = [Host(name='dummy1')]
    strategyModule = StrategyModule(tqm)
    it = Iterator()
    strategyModule.run(it, None)
    tqm.cleanup()
    tqm.send_callback('v2_playbook_on_stats', tqm._stats)
    tqm._terminated = True
    strategyModule.run(it, None)


# Generated at 2022-06-13 15:07:19.257203
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Create a test Strategy
    strategy = StrategyModule()
    assert strategy is not None
    assert isinstance(strategy, StrategyBase)

# Generated at 2022-06-13 15:07:21.716507
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    _tqm = None
    _iterator = None  # type: Iterator
    _play_context = None  # type: PlayContext
    tm = StrategyModule(_tqm)
    tm.run(_iterator, _play_context)



# Generated at 2022-06-13 15:07:22.442932
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:07:22.960663
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:07:31.060610
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.vars.manager import VariableManager
    from ansible.plugins.test.test_strategy_plugin import TestTaskQueueManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.display import Display
    import ansible.plugins.loader as plugin_loader
    plugin_loader.add_directory('./plugins/')
    display = Display()

    hosts = ['shichao.i']
    tasks = [Task()]
    role = Role()

    block = Block(
        role=role,
        tasks=tasks
    )

# Generated at 2022-06-13 15:07:40.556732
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    config_data = {} # need to be initialized
    config_data['ANSIBLE_DISPLAY_OK_HOSTS'] = True
    config_data['ANSIBLE_HOST_KEY_CHECKING'] = True
    config_data['ANSIBLE_CALLABLE_WHITELIST'] = ['module_name']
    config_data['ANSIBLE_CALLABLE_PLUGINS'] = ['module_name']
    #config_data['ANSIBLE_ROLES_PATH'] = '/home/tungtt/Documents/mygit/git_ansible_plugins/ansible-redfish-modules/lib/ansible/modules'
    config_data['DEFAULT_ROLES_PATH'] = '/home/tungtt/Documents/mygit/git_ansible_plugins/ansible-redfish-modules/lib/ansible/modules'


# Generated at 2022-06-13 15:08:12.606557
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.loader import action_loader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_result import TaskResult
    from ansible.inventory.host import Host
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.included_file import IncludedFile
    from ansible.playbook.handler import Handler
    from ansible.template import Templar
    import json
    import unittest
    import sys
    import copy

    reload(sys)
    sys.setdefaultencoding('utf8')


# Generated at 2022-06-13 15:08:13.413156
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
	pass



# Generated at 2022-06-13 15:08:15.288087
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    sm = StrategyModule(tqm)
    assert sm.run(None, None) != None

# Generated at 2022-06-13 15:08:17.048140
# Unit test for method run of class StrategyModule

# Generated at 2022-06-13 15:08:24.540030
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.playbook import Playbook
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.runner.return_data import ReturnData
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_result import TaskResult
    task = Task()
    task_result = TaskResult(host=Inventory(loader=DataLoader()), task=task)

# Generated at 2022-06-13 15:08:36.433392
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():


    ###############################################
    #
    # Run Method Test Case #1
    #
    ###############################################
    work_to_do = True
    last_host = 1
    iterator = 2
    play_context = 3
    last_host = 4
    hosts_left = 5
    host = 6
    host_name = 7
    state = 8
    task = 9
    workers_free = 10
    starting_host = 11
    host_results = 12
    task_vars = 13
    run_once = 14
    action = 15
    task_name = 17
    throttle = 18
    same_tasks = 19
    worker = 20
    host_results = 21
    task_vars = 22
    run_once = 23
    action = 24
    workers_free = 25

# Generated at 2022-06-13 15:08:38.158083
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    c= StrategyModule(None)
    assert c.__class__.__name__ == 'StrategyModule'


# Generated at 2022-06-13 15:08:46.432871
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    m_send_callback = MagicMock()
    m_filter_notified_hosts = MagicMock(return_value=[1, 2])
    m_filter_notified_failed_hosts = MagicMock(return_value=[3, 4])
    m_get_hosts_left = MagicMock(return_value=[1, 2])
    m_queue_task = MagicMock()
    m_process_pending_results = MagicMock(return_value=[5, 6])
    m_execute_meta = MagicMock(return_value=True)
    m_get_hosts_cache = MagicMock()
    m_take_step = MagicMock(return_value=True)
    m_wait_on_pending_results = MagicMock()
    m_run = MagicMock()
   

# Generated at 2022-06-13 15:08:50.249496
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # test parameters
    # expected result
    # set up context
    # TODO: fix this test, it's not even close
    # result = run(iterator, play_context)
    # assert result ==
    pass


# Generated at 2022-06-13 15:08:54.772217
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Test 1. firstly we need to test whether the function run is finished without any error
    # Test 2. secondly we need to test whether the function run returns the correct value
    strategyModule = StrategyModule(tqm="")
    assert strategyModule.run(iterator="", play_context="") == None

    assert strategyModule.run(iterator="", play_context="") == None


# Generated at 2022-06-13 15:10:02.108459
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():

    # Variables
    # _tqm =
    # _fallbacks =
    # _final_q =
    # _failed_hosts =
    # _tasks_per_host =
    # _failed_hosts_q =
    # _workers =
    # _worker_prc =
    # _blocked_hosts =
    # _cur_worker =
    # _hosts_cache =
    # _hosts_cache_all =
    # _variable_manager =

    # Declare strategy module object
    strategy_module = StrategyModule(tqm)

    # run
    result = strategy_module.run(iterator, play_context)
    # Workflow testing
    if play_context.verbosity > 0:
        display.banner('PLAY: %s' % iterator._play.name)

# Generated at 2022-06-13 15:10:09.600175
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    tqm = TaskQueueManager(
        inventory=InventoryManager(loader=DataLoader(), sources=''),
        variable_manager=VariableManager(),
        loader=DataLoader(),
    )

    sm = StrategyModule(tqm)
    assert sm
    assert sm.get_hosts_left(None) is None
    assert sm._take_step(None, None) is False
    assert not sm._host_pinned
    assert sm.ALLOW_BASE_THROTTLING is False

# Generated at 2022-06-13 15:10:19.789515
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from mock import Mock
    from ansible.module_utils.common.removed import removed_class

    # test StrategyBase inherit from StrategyModule
    obj = StrategyModule(Mock())
    assert isinstance(obj, StrategyBase)
    assert isinstance(obj, removed_class)  # StrategyModule is removed and temporarily replaced by StrategyBase

    assert obj._host_pinned == False

    # test StrategyBase.__init__
    assert obj._blocked_hosts is None
    assert obj._hosts_cache is None
    assert obj._hosts_cache_all is None
    assert obj._workers is None

# Generated at 2022-06-13 15:10:26.242975
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    '''
    Unit test of _run_async_wrap
    '''
    import ansible.plugins.strategy.free as free
    import ansible.module_utils.basic as basic
    import ansible.module_utils.facts.virtual as virtual
    import ansible.module_utils.facts.system as system
    import ansible.module_utils.facts.collector as collector
    import ansible.module_utils.facts.network as network
    import ansible.module_utils.facts.platform as platform
    import ansible.module_utils.facts.distribution as distribution
    import ansible.module_utils.facts.other as other
    import ansible.module_utils.facts.processor as processor
    import ansible.module_utils.facts.package_manager as package_manager

# Generated at 2022-06-13 15:10:27.205775
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass
# Unit tests for class StrategyModule

# Generated at 2022-06-13 15:10:30.586016
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    tqm = AnsibleTaskQueueManager('inventory', 'playbook', 'VarManager', 'Loader', 'null', 'null')
    strategy_module = StrategyModule(tqm, None)
    assert strategy_module.run([], {}) == ('strategy.run', None, None)

# Generated at 2022-06-13 15:10:31.471880
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    assert False # TODO: create test


# Generated at 2022-06-13 15:10:38.389365
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # initialize the test environment
    args = dict(
        connection='smart',
        become_method=None,
        become_user=None,
        check=False,
        diff=False,
        extra_vars=[],
        listhosts=None,
        listtags=None,
        listtasks=None,
        module_path=None,
        new_vault_password_file=None,
        one_line=None,
        output_file=None,
        output_lock=None,
        poll_interval=15,
        verbosity=0,
    )

# Generated at 2022-06-13 15:10:42.239995
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager

    tqm = TaskQueueManager(None, None)
    task_obj = StrategyModule(tqm)
    assert isinstance(task_obj, StrategyBase)



# Generated at 2022-06-13 15:10:42.915626
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:12:56.748923
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:12:58.520507
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # call without required args
    results = StrategyModule.run(None, iterator=None, play_context=None)
    assert(results == None)



# Generated at 2022-06-13 15:12:59.880235
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule('')
    assert (module!=None)

# Generated at 2022-06-13 15:13:01.900134
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Asserting module StrategyModule exists and has been successfully imported
    assert 'action_loader.get' in globals()
    assert 'action_loader' in globals()



# Generated at 2022-06-13 15:13:04.299552
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
  strategy = StrategyModule(tqm)
  strategy.run(iterator, play_context)


# Generated at 2022-06-13 15:13:13.397508
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    import ansible.constants as C
    # Create a task queue manager
    tqm = TaskQueueManager(
        inventory=InventoryManager(loader=DataLoader(), sources='localhost,'),
        variable_manager=VariableManager(),
        loader=DataLoader(),
        options=None,
        passwords=None,
        stdout_callback=None,
    )
    # Create a strategy object
    strategy = StrategyModule(tqm)
    print(strategy)
    assert strategy


# Generated at 2022-06-13 15:13:15.616981
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    tqm = TaskQueueManager(1,1,1)
    StrategyModule(tqm).run("iterator","play_context")

# Generated at 2022-06-13 15:13:25.514332
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Check if StrategyModule's run method raises AnsibleError when AnsibleError occurs in if statement
    # which checks if strategy is set to 'free' and host is not in self._tqm._unreachable_hosts.
    mocker.patch('ansible.plugins.strategy.free.StrategyFree.run')
    mocker.patch('ansible.errors.AnsibleError')
    mocker.patch('ansible.plugins.strategy.free.StrategyFree._set_hosts_cache')
    mocker.patch('ansible.plugins.strategy.free.StrategyFree.get_hosts_left')
    mocker.patch('ansible.plugins.strategy.free.StrategyFree._tqm.RUN_OK')

# Generated at 2022-06-13 15:13:36.272810
# Unit test for method run of class StrategyModule

# Generated at 2022-06-13 15:13:37.586929
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    target = StrategyModule(tqm)
    assert target.run(iterator, play_context) is None