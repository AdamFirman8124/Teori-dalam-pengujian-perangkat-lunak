

# Generated at 2022-06-13 15:06:49.206514
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager

    tqm = TaskQueueManager(
        inventory=None,
        variable_manager=None,
        loader=None,
        passwords=None,
        stdout_callback=None,
        run_additional_callbacks=True,
        run_tree=False,
    )
    sc = StrategyModule(tqm)
    assert isinstance(sc, StrategyBase)



# Generated at 2022-06-13 15:07:00.425026
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    
    import unittest
    from unittest.mock import Mock,patch,call

    sys.modules['ansible'] = Mock()

    import ansible.plugins.strategy.free as sut

    class TestStrategyModuleRun(unittest.TestCase):

        def setUp(self):
            self.connection = Mock()
            self.play_context = Mock()

            self.play = Mock()
            self.play_context.password = None
            self.play_context.become_password = None
            self.play_context.become = False
            self.play_context.become_method = 'sudo'
            self.play_context.remote_user = 'user'
            self.play_context.connection = 'ssh'
            self.play_context.timeout = 10

# Generated at 2022-06-13 15:07:03.563376
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # TaskQueueManager instance to be used for unit test
    tqm = TaskQueueManager(None, None)
    # StrategyModule instance to be tested
    strategy_module = StrategyModule(tqm)
    # PlayContext instance to be used for unit test
    play_context = PlayContext()

    # Run method under test
    result = strategy_module.run(None, play_context)

# Generated at 2022-06-13 15:07:06.921405
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
   tqm = dict()
   iterator = dict()
   play_context = dict()
   strategy_module = StrategyModule(tqm)
   strategy_module.run(iterator, play_context)

# Generated at 2022-06-13 15:07:17.618896
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    
    from ansible.vars.manager import VariableManager
    from ansible.vars.unsafe_proxy import UnsafeProxy

    templar = Templar(loader=None, variables=self._variable_manager.get_vars())
    templar.template(task.name)
    templar.template(task.run_once)
    

# Generated at 2022-06-13 15:07:20.119148
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    test_module = StrategyModule(None)
    test_module.run('iterator','play_context')

# Generated at 2022-06-13 15:07:20.909805
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    StrategyModule.run()

# Generated at 2022-06-13 15:07:29.620125
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy import StrategyModule
    from ansible.plugins.loader import action_loader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.process.worker import WorkerProcess
    from ansible.errors import AnsibleError
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars

# Generated at 2022-06-13 15:07:31.944141
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    strategy_module = StrategyModule(tqm=None)
    strategy_module.run(iterator=None, play_context=None)

# Generated at 2022-06-13 15:07:32.623884
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:07:53.208155
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:08:03.760120
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.plugins.strategy.free import StrategyModule
    from ansible.plugins.strategy import StrategyBase
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_result import TaskResult
    from ansible.inventory.host import Host
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.executor.play_iterator import PlayIterator
    import pytest
    import os
    import json

    tqm = TaskQueueManager(
        inventory=None,
        variable_manager=None,
        loader=None,
        options=None,
        passwords=None,
        stdout_callback=None,
    )
    strategy = StrategyModule(tqm)
    strategy._initialize_work_queue

# Generated at 2022-06-13 15:08:07.137661
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

    # attempt to find a better host to
    # start the free-form search at so we don't keep favoring earlier hosts
    # in the list.

# Generated at 2022-06-13 15:08:17.580690
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task
    from ansible.playbook.included_file import IncludedFile
    from ansible.vars.manager import VariableManager

    #Create test data
    #Create a TaskQueueManager object with a Unique id to test StrategyModule constructor

# Generated at 2022-06-13 15:08:23.128906
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.playbook import Play
    from ansible.playbook import Playbook
    from ansible.playbook import PlayContext
    from ansible.playbook import PlaybookExecutor
    from ansible.playbook import PlaybookIOErrorHandler
    from ansible.playbook.play_iterator import PlayIterator

    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    from ansible.plugins.loader import module_loader
    from ansible.plugins.strategy import StrategyBase

    pb = Playbook.load('/etc/ansible/roles/nxos_vxlan/tests/test_pb.yml', variable_manager=None, loader=None)

    inventory = InventoryManager(loader=None, sources='testhosts')


# Generated at 2022-06-13 15:08:24.142704
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:08:36.145674
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    ## StrategyModule
    # result = self._tqm.RUN_OK #HAS_CHANGED
    # hosts_left = self.get_hosts_left(iterator) #HAS_CHANGED
    # work_to_do = False #HAS_CHANGED
    # last_host = 0 #HAS_CHANGED
    # workers_free = len(self._workers) #HAS_CHANGED
    # self._set_hosts_cache(iterator._play) #HAS_CHANGED
    # play_context = iterator #HAS_CHANGED
    # host_results = [] #HAS_CHANGED
    # starting_host = last_host #HAS_CHANGED

    # Change the return value of get_hosts_left(iterator) to HAS_CHANGED
    hosts

# Generated at 2022-06-13 15:08:37.026083
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():

    # FIXME Function not implemented
    return dict()

# Generated at 2022-06-13 15:08:46.162407
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.strategy import StrategyBase

    tqm = TaskQueueManager(
        inventory=None,
        variable_manager=None,
        loader=None,
        options=None,
        passwords=None,
        stdout_callback=None,
    )
    pbex = PlaybookExecutor(
        playbooks=None,
        inventory=None,
        variable_manager=None,
        loader=None,
        options=None,
        passwords=None,
    )
    strategy

# Generated at 2022-06-13 15:08:46.972454
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:09:45.578255
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.playbook.play_context
    import ansible.playbook.task_queue_manager
    import ansible.playbook.play

    mock_play_context = ansible.playbook.play_context.PlayContext()
    mock_tqm = ansible.playbook.task_queue_manager.TaskQueueManager(
        inventory=None,
        variable_manager=None,
        loader=None,
        passwords=None,
        stdout_callback=None,
        run_additional_callbacks=None,
        run_tree=False,
        timeout=C.DEFAULT_TIMEOUT
    )
    mock_play = ansible.playbook.play.Play().load({}, variable_manager=None, loader=None)

    # call StrategyModule constructor to generate object

# Generated at 2022-06-13 15:09:46.221519
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:09:51.544503
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.handler import Handler
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.process.worker import WorkerProcess
    from ansible.executor.stats import AggregateStats
    from ansible.plugins.strategy import StrategyBase
    from ansible.vars.hostvars import HostVars
    from ansible.vars.manager import VariableManager
    from ansible.vars.reserved import Reserved
    import mock
    from collections import namedtuple

# Generated at 2022-06-13 15:09:52.137351
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:09:52.766446
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:10:03.861443
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.play import Play
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader

    class FakeHost(object):
        def __init__(self):
            return

        def get_name(self):
            return "Fake host"

    class FakeInventory(object):
        def __init__(self):
            self.hosts = list()
            self.hosts.append(FakeHost())

        def hosts(self):
            return self.hosts

    class FakePlay(object):
        def __init__(self):
            return

        def get_hosts(self):
            return ["Fake host"]


# Generated at 2022-06-13 15:10:11.403486
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    
    ################################################################################
    # Unit test for method run of class StrategyModule.
    # Test when we have an Ansible Error (templating error).
    ################################################################################
    strategy = StrategyModule()
    
    # Call the method under test
    strategy._wait_on_pending_results("")
    
    ################################################################################
    # Unit test for method run of class StrategyModule.
    # Test when we have an Ansible Error (action not found).
    ################################################################################
    strategy = StrategyModule()
    
    # Call the method under test
    strategy.add_tqm_variables("")
    
    ################################################################################
    # Unit test for method run of class StrategyModule.
    # Test when we have an Ansible Error (unreachable_hosts).


# Generated at 2022-06-13 15:10:23.171043
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():

    class TASK:
        def __init__(self):
            pass
    class LOADER:
        def __init__(self):
            pass
    class PLAY_CONTEXT:
        def __init__(self):
            pass
    class ITERATOR:
        def __init__(self):
            pass
    class VARIABLE_MANAGER:
        def __init__(self):
            pass
    class CALLBACK_MODULE:
        def __init__(self):
            pass
    class QUEUE_MANAGER:
        def __init__(self):
            pass
    class HOST:
        def __init__(self):
            pass
    class OPTIONS:
        def __init__(self):
            pass

    class RESULT:
        def __init__(self):
            pass


# Generated at 2022-06-13 15:10:24.249345
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    assert False



# Generated at 2022-06-13 15:10:26.596040
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

if __name__ == '__main__':
    test_StrategyModule_run()

# Generated at 2022-06-13 15:12:33.450124
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.inventory.manager import InventoryManager

    def test_get_hosts_in_unreachable(self):
        return [u'192.168.56.104 (test_free_strategy)', u'192.168.56.101 (test_free_strategy)', u'192.168.56.103 (test_free_strategy)', u'192.168.56.102 (test_free_strategy)', u'192.168.56.105 (test_free_strategy)']


# Generated at 2022-06-13 15:12:45.008607
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    args = None
    if not args:
        args = parse_args()
    else:
        print("parsed args: %s" % args)
    inven = InventoryManager(loader=DataLoader(), sources=args.inventory)
    inven.subset(args.subset)
    if args.host:
        host = inven._inventory.get_host(args.host)
        inven.filter_hosts([host], subset=None)
    variables = VariableManager(loader=DataLoader(), inventory=inven)
    if args.extra_vars:
        variables.extra_vars = load_extra_vars(loader=DataLoader(), options=args.extra_vars)

# Generated at 2022-06-13 15:12:45.542319
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:12:48.952635
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    tqm=MockTQM()
    strategyModule = StrategyModule(tqm)
    iterator=MockIterator()
    play_context=MockPlayContext()
    strategyModule.run(iterator, play_context)


# Generated at 2022-06-13 15:12:49.573108
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
  pass

# Generated at 2022-06-13 15:12:58.520791
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    fake_loader = FakeLoader()
    m_playbook = FakePlaybook(loader=fake_loader)
    m_play = FakePlay(playbook=m_playbook)
    m_play.max_fail_percentage = None
    iterator = FakeIterator()
    
    m_tqm = FakeTQM(loader=fake_loader, play=m_play)
    m_tqm._terminated = False
    m_tqm._terminated = False
    
    
    
    
    m_tqm._tqm_stdout_callback = FakeCallbackModule(sys.stdout)
    m_tqm._callback_plugins = [m_tqm._tqm_stdout_callback]
    m_tqm._stats = 'FakeStats'
    m_tqm._not

# Generated at 2022-06-13 15:13:03.608948
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins import strategy_loader
    import ansible.playbook.play_context
    import ansible.executor.task_queue_manager
    import ansible.inventory
    import ansible.parsing.dataloader
    import ansible.vars.manager
    import ansible.utils.plugin_docs
    import ansible.inventory.manager
    loader = ansible.parsing.dataloader.DataLoader()
    variable_manager = ansible.vars.manager.VariableManager()
    inventory = ansible.inventory.manager.InventoryManager(loader=loader, sources=["/etc/ansible/hosts"])
    variable_manager.set_inventory(inventory)
    play_context = ansible.playbook.play_context.PlayContext()
    all_vars = dict()
    tq

# Generated at 2022-06-13 15:13:12.625411
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    host_name = 'test_host'
    result = {
              "changed": False,
              "msg": "All items completed",
              "results": [
                          {
                              "ansible_loop_var": "item",
                              "changed": False,
                              "item": "1",
                              "msg": "test_task"
                          }
                          ],
              "skipped": False
          }
    task = {"task": "test_task", "task_action": "test_action"}
    tqm = {"_blocked_hosts": {host_name: False},
           "_terminated": False}

# Generated at 2022-06-13 15:13:23.010115
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # pylint: disable=no-self-use
    tqm = AnsibleTest_TaskQueueManager()
    im = AnsibleTest_InventoryModule()
    vm = AnsibleTest_VariableManager()
    sm = StrategyModule(tqm)
    sm._tqm = tqm
    sm._inventory = im
    sm._variable_manager = vm
    display = AnsibleTest_Display()
    sm.display = display
    im.hosts = [AnsibleTest_Host(), AnsibleTest_Host()]
    iterator = AnsibleTest_Iterator()
    play_context = AnsibleTest_PlayContext()
    play_context._play = "play"
    play_context._play_hosts = ['host1', 'host2']
    iterator._play = "play"

# Generated at 2022-06-13 15:13:23.602335
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass