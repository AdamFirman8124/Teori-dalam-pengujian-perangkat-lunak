

# Generated at 2022-06-13 15:06:50.873197
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    it = Iterator(play=None)
    pc = PlayContext()
    tqm = TaskQueueManager(inventory=None, variable_manager=None, loader=None, options=None, passwords=None, stdout_callback=None, run_tree=True, )
    t = StrategyModule(tqm=tqm)
    t.run(it, pc)

# unit test for method get_hosts_left of class StategyModule

# Generated at 2022-06-13 15:06:52.798769
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule("tqm") is not None

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:06:53.578396
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:06:54.611191
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
	assert True == False

# Generated at 2022-06-13 15:07:06.502363
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    """
    This test method will run with unittest framework.
    """

    # Define a fake ansible.internal.inventory.host.Host
    class FakeHost(object):
        def __init__(self, name):
            self.name = name

        def get_name(self):
            return self.name

    # Define a fake ansible.playbook.play.PlayContext
    class FakePlayContext(object):
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

    # Define a fake ansible.plugins.loader.action_loader.ActionModule
    class FakeActionModule(object):
        def __init__(self, name):
            self._name = name

        def get_name(self):
            return self

# Generated at 2022-06-13 15:07:10.148627
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    my_obj = StrategyModule(tqm=[{'tasks': [{'task': 'a'}]}])
    result = my_obj.run(iterator={'_play': True}, play_context={'context': True})
    assert(result == False)


# Generated at 2022-06-13 15:07:15.727438
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.playbook.play import Play
    from modules.backend.ansible_runner import AnsibleRunner
    tqm = AnsibleRunner
    strategy_module = StrategyModule(tqm)
    play = Play()
    iterator = strategy_module.get_iterator(play)
    play_context = strategy_module.get_play_context(iterator)
    strategy_module.run(iterator, play_context)

# Generated at 2022-06-13 15:07:27.059720
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.vars import VariableManager
    from ansible.executor.task_executor import TaskExecutor
    from ansible.executor.playbook_executor import PlaybookExecutor

    playbook = Playbook.load('hpe3par_facts.yml', variable_manager=VariableManager(), loader=None)

    #create instance of TaskQueueManager which will be used to create instance of HostManager

# Generated at 2022-06-13 15:07:29.920919
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    '''
    Unit test for method run of class StrategyModule
    '''
    print('')
    print('Testing method run of class StrategyModule')
    print('')
    print('TEST NOT IMPLEMENTED')

# Generated at 2022-06-13 15:07:30.647891
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:08:00.767983
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_result import TaskResult
    from ansible.executor.worker.worker import Worker
    from ansible.executor.task_executor import TaskExecutor
    from ansible.plugins.strategy.linear import StrategyModule

    class MockPlay(Play):

        def __init__(self):
            pass

    class MockPlayContext(PlayContext):

        def __init__(self):
            pass

    class MockTaskQueueManager(TaskQueueManager):

        def __init__(self, host_list):
            self.host_list = host_list
            self.workers = []


# Generated at 2022-06-13 15:08:12.253713
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # pylint: disable=W0621
    module = AnsibleModule(
        argument_spec=dict(
            msg=dict(required=True, type='str')
        ),
        supports_check_mode=False,
        add_file_common_args=True
    )
    result = dict(
        changed=False,
        failed=False,
    )

    m_get_hosts_left = Mock(return_value=[])
    with patch.object(AnsibleModule, 'get_hosts_left', m_get_hosts_left):
        module.run()
    m_get_hosts_left.assert_called_with(module, require_all_hosts=False)

    m_get_hosts_left = Mock(return_value=[])

# Generated at 2022-06-13 15:08:21.143693
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    import mock
    import unittest
    from ansible.utils.display import Display
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.plugins.strategy import StrategyModule
    from ansible.plugins.callback import CallbackBase
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_result import TaskResult
    from ansible.executor.play_context import PlayContext
    from ansible.utils.vars import combine_vars

    class AnsibleModule:

        def __init__(self, name='', *args, **kwargs):
            self

# Generated at 2022-06-13 15:08:21.911225
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule("tqm")
    assert module is not None


# Generated at 2022-06-13 15:08:22.404594
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:08:27.761384
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    import mock
    import unittest
    import yaml
    with mock.patch('__main__.StrategyBase.run') as m_run:
        with mock.patch('__main__.StrategyBase.__init__') as m_init:
            with open('/home/alexandre/ansible/hacking/test/units/lib/ansible/playbook/tests/test_helpers/yaml/v2_inventory.yml') as f:
                hosts = yaml.load(f)


# Generated at 2022-06-13 15:08:39.448309
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    #
    # Tests for class StrategyModule (in Ansible/lib/ansible/plugins/strategy/free.py)
    #
    class FakeLoader:
        pass

    class FakeVariableManager:
        pass

    class FakeHost:
        def __init__(self, host_name):
            self.name = host_name

        def get_name(self):
            return self.name

    class FakeTask:
        pass

    class FakePlayContext:
        pass

    class FakeWorker:
        def __init__(self, task):
            self._task = task

        def is_alive(self):
            return True

    class FakeTQM:
        class RUN_OK:
            pass
        RUN_OK = RUN_OK()

        class RUN_ERROR:
            pass
        RUN_ERROR = RUN_ERROR

# Generated at 2022-06-13 15:08:46.933622
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    mock_self = mock.Mock(spec=StrategyModule)
    mock_self.get_hosts_left.return_value = mock.MagicMock()
    mock_self._variable_manager.get_vars.return_value = mock.MagicMock()
    mock_self.add_tqm_variables.return_value = mock.MagicMock()
    #mock_self._loader.return_value = mock.MagicMock()
    #mock_self._variable_manager.get_vars.return_value = mock.MagicMock()
    mock_self._queue_task.return_value = mock.MagicMock()
    mock_self._execute_meta.return_value = mock.MagicMock()
    #mock_self._loader.return_value = mock.MagicMock()
    #

# Generated at 2022-06-13 15:08:56.373474
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass


# Generated at 2022-06-13 15:09:02.986475
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  from ansible.playbook.play_context import PlayContext
  from ansible.playbook_iterator import PlaybookIterator
  from ansible.vars.manager import VariableManager
  from ansible.template import Templar
  from ansible.inventory.manager import InventoryManager
  from ansible.plugins.loader import module_loader, action_loader
  from ansible.utils.display import Display

  from ansible.module_utils.basic import AnsibleModule

  from ansible.plugins.callback.default import CallbackModule
  import ansible.constants as C

  class MockTask:
    """Mock class of AnsibleTask"""

# Generated at 2022-06-13 15:10:04.280042
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.plugins.callback import CallbackBase

    tqm = TaskQueueManager(
        inventory=InventoryManager(loader=DataLoader(), sources=['localhost,']),
        variable_manager=VariableManager(),
        loader=DataLoader(),
        passwords={},
        stdout_callback=CallbackBase(),
    )

    play_context = Play().set_context(tqm.options)

    strategy = StrategyModule(tqm)
    assert strategy

# Generated at 2022-06-13 15:10:04.811882
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:10:09.712686
# Unit test for constructor of class StrategyModule

# Generated at 2022-06-13 15:10:14.877309
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    #This is a hardcoded test. Should be improved
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.strategy import StrategyModule
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_result import TaskResult
    from ansible.utils.vars import combine_vars
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.vars.hostvars import HostVars
    from ansible.vars.reserved import Reserved

   

# Generated at 2022-06-13 15:10:26.375515
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    mod = strategy
    target_module_name = 'ansible.parsing.dataloader.DataLoader'
    target_module = __import__(target_module_name)
    imp_module = importlib.import_module(target_module_name + '.tests')
    target_method = getattr(imp_module, 'test_DataLoader_load_file')
    if not target_method:
        raise ValueError("Method test_DataLoader_load_file not found")
    args = inspect.getargspec(target_method).args
    kwargs = dict()
    if args:
        if args[0] in kwargs:
            del kwargs[args[0]]
        args = (target_method,) + tuple([kwargs[x] for x in args if x != 'self'])
        target_method

# Generated at 2022-06-13 15:10:30.164771
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    play = Play().load({}, variable_manager=VariableManager(), loader=DataLoader())
    tqm = TaskQueueManager(inventory=None, variable_manager=VariableManager(), loader=DataLoader(), options=None, passwords=None, stdout_callback="default")
    strategyModule = StrategyModule(tqm)
    assert strategyModule.__class__.__name__ == "StrategyModule"

test_StrategyModule()

# Generated at 2022-06-13 15:10:35.658434
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader

    play_context = PlayContext()
    stats = dict(processed=0, ok=0, failed=0, dark=dict(failures=0, ok=0, processed=0))
    loader = DataLoader()
    variable_manager = VariableManager()
    host = Host('localhost')

# Generated at 2022-06-13 15:10:45.820104
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    task_ser = Task()
    task_arch = Task()
    task_arch.action = 'setup'
    task_arch.name = 'setup'
    task_arch.args = {}
    task_ser.action = 'setup'
    task_ser.name = 'setup'
    task_ser.args = {}
    info_task_ser = TaskInfo()
    info_task_ser.name = 'setup'
    info_task_ser.action = 'setup'
    info_task_arch = TaskInfo()
    info_task_arch.name = 'setup'
    info_task_arch.action = 'setup'
    host_ser = Host()
    host_ser.name = "test"
    host_arch = Host()
    host_arch.name = "test"
    play_ser = Play()
   

# Generated at 2022-06-13 15:10:46.774078
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass



# Generated at 2022-06-13 15:10:52.508608
# Unit test for method run of class StrategyModule

# Generated at 2022-06-13 15:13:00.030635
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Init arguments for constructor
    tqm = {'ansible_playbook_python': '/Users/vivas/Dev/GitRepos/python/venv/bin/python'}

    # Init class instance
    obj = StrategyModule(tqm)
    # Init arguments
    iterator = {}
    play_context = {}
    val = obj.run(iterator, play_context)
    # Check method output
    # Return value does not require validation
    pass

# Generated at 2022-06-13 15:13:02.888866
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    tqm = TaskQueueManager()
    tqm.RUN_OK = 2
    tqm._terminated = True
    iterator = None
    play_context = None
    sm = StrategyModule(tqm)
    sm.run(iterator, play_context)

# Generated at 2022-06-13 15:13:03.883679
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass


# Generated at 2022-06-13 15:13:12.985724
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    host = {'hostname': 'hostname', 'name': 'test_host'}
    iterator = {}
    play_context = {}
    tqm = {'RUN_OK':1, '_terminated': False, 'send_callback': lambda x,y: 1,
           '_unreachable_hosts': set(), '_workers': [],}
    action_loader = {'get' : lambda x,y: None}
    task = {'action': 'action', 'collections': ['test_collection',]}
    task_vars = {'test_key': 'test_value'}
    strategy_module = StrategyModule(tqm)
    strategy_module._worker_threads = 1
    strategy_module._workers = [1]
    strategy_module._hosts_cache = {1: 1}
   

# Generated at 2022-06-13 15:13:14.564271
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
	StrategyModule_1 = StrategyBase()
	results = StrategyModule_1.run()

# Generated at 2022-06-13 15:13:15.989007
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    Strategy_Module = StrategyModule()

    Strategy_Module.run()



# Generated at 2022-06-13 15:13:25.227580
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    
    # Create a mock PlayContext class.
    class MockPlayContext:
        pass

    # Create a mock Iterator class.
    class MockIterator:
        pass

    # Create a mock TaskQueueManager class.
    class MockTaskQueueManager:
        pass

    # Instantiate a mock task queue manager.
    tqm = MockTaskQueueManager()

    # Instantiate an instance of class StrategyModule.
    strategy_module = StrategyModule(tqm)
   
    # Instantiate a mock iterator.
    iterator = MockIterator()

    # Instantiate a mock play context.
    play_context = MockPlayContext()
    
    # Call method run.
    strategy_module.run(iterator, play_context)



# Generated at 2022-06-13 15:13:35.995240
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    my_options = Options()
    my_options.listtags = False
    my_options.listtasks = False
    my_options.listhosts = False
    my_options.syntax = False
    my_options.connection = 'smart'
    my_options.module_path = None
    my_options.forks = 5
    my_options.remote_user = None
    my_options.private_key_file = None
    my_options.ssh_common_args = None
    my_options.ssh_extra_args = None
    my_options.sftp_extra_args = None
    my_options.scp_extra_args = None
    my_options.become = True
    my_options.become_method = 'sudo'
    my_options.become_user = None
    my

# Generated at 2022-06-13 15:13:46.697626
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Unit test for method run of class StrategyModule
    # Create an strategy module
    strategyModule = StrategyModule(None)

    # Add two hosts to the hostcache
    strategyModule._hosts_cache_all_unfiltered.append("host1")
    strategyModule._hosts_cache_all_unfiltered.append("host2")

    # Add two tasks to the task queue of host1
    strategyModule._blocked_hosts["host1"] = True
    strategyModule._blocked_hosts["host2"] = True
    strategyModule._workers.append(1)
    strategyModule._workers.append(1)
    strategyModule._tasks = ["task1", "task2"]
    # run the module, expected result --> return true
    assert strategyModule.run() == False


# Generated at 2022-06-13 15:13:56.625385
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    s = StrategyModule(tqm)
    # with self.assertRaises(AnsibleError) as cm:
    assert s.run(iterator, play_context) == localhost.vars.put('ansible_' + ansible_user, ansible_ssh_user)

    assert s.run(iterator, play_context) == localhost.vars.put('ansible_' + ansible_password, ansible_ssh_pass)

    assert s.run(iterator, play_context) == localhost.vars.put('ansible_' + ansible_key_file, ansible_private_key_file)

    assert s.run(iterator, play_context) == localhost.vars.put('ansible_' + ansible_pyyaml, has_pyyaml)
