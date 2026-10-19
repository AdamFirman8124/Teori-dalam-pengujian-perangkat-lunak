

# Generated at 2022-06-13 15:06:52.667920
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Initialize mocks
    tqm = MagicMock()
    iterator = MagicMock()
    play_context = MagicMock()

    # Create instance of class StrategyModule
    strategy_module_obj = StrategyModule(tqm=tqm)

    strategy_module_obj._tqm = MagicMock()
    strategy_module_obj._tqm.RUN_OK = 'RUN_OK'
    strategy_module_obj._tqm._terminated = False
    strategy_module_obj._workers = ['worker1', 'worker2']
    strategy_module_obj._set_hosts_cache = MagicMock()
    strategy_module_obj._set_hosts_cache.return_value = 'set_hosts_cache_ret_val'
    strategy_module_obj.get_hosts_left

# Generated at 2022-06-13 15:06:53.351488
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:06:54.009172
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 15:06:59.459588
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    iter = None
    play_context = None
    data = { '_tqm': None, '_variables': None, '_loader': None, '_inventory': None, '_variable_manager': None, '_blocked_hosts': None, '_workers': None, '_final_q': None, '_failed_queue': None, '_queue_terms': None, '_hosts_cache': None }
    obj = StrategyModule(**data)
    obj.run(iter, play_context)


# Generated at 2022-06-13 15:07:05.602454
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # Check if StrategyModule.run does not execute on a empty play
    from ansible.playbook import Playbook

    from ansible.executor.task_queue_manager import TaskQueueManager
    import ansible.constants as C

    tqm = TaskQueueManager(inventory=None, variable_manager=None, loader=None, options=None, passwords=None, stdout_callback=None)

    play = Playbook().load('test/files/playbooks/strategy_module/strategy_module.yml', variable_manager=None, loader=None)
    # Check if StrategyModule.run does not execute a play having only hosts
    # host_list = [hosts : localhost]
    if not C.STRATEGY == 'free':
        assert play.run(task_queue_manager=tqm) == None

    # Check

# Generated at 2022-06-13 15:07:09.135208
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    strategy_module = StrategyModule(tqm=tqm)
    strategy_module.run(iterator, play_context)
# Module class StrategyModule end


################################################################################
#
#         Class StrategyBlock
#
################################################################################

# Generated at 2022-06-13 15:07:13.385232
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    def run_mock(iterator, play_context):
        return 0

    strategy = StrategyModule(run_mock)
    assert strategy.run(None, None) == 0



# Generated at 2022-06-13 15:07:26.349247
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    import ansible.playbook
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.playbook.block
    import ansible.playbook.included_file
    import ansible.plugins.loader
    import ansible.inventory.manager
    import ansible.template
    import ansible.vars.manager

    loader = ansible.plugins.loader.ActionModuleLoader(None, '/Users/ansibot/ansible-rst/lib/ansible/plugins/action', None)
    module_list = loader.all(class_only=True)

    module_list[0].doc = "test_module"
    module_list[0]._action = ansible.plugins.action.ActionModule({'module_name': 'test_module'})

    host_list = []
    host

# Generated at 2022-06-13 15:07:29.338214
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
	play_context = None
	iterator = None
	tqm = None
	test_StrategyModule = StrategyModule(tqm)
	test_StrategyModule.run(iterator,play_context)

# Generated at 2022-06-13 15:07:30.461060
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
  assert True

# Generated at 2022-06-13 15:08:01.983141
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.plugins.strategy import StrategyBase
    import ansible.plugins.strategy.free as free
    import json
    import unittest

    # Test scenario is the following:
    #   2 hosts with the _hosts_cache defined (Setup)
    #   RUN_OK = 0
    #   _host_pinned = False
    #   tqm._terminated = False

    # Class ansible.plugins.strategy.free.StrategyModule is a subclass of ansible.plugins.strategy.StrategyBase and
    # implements the method run. Thus, it is necessary to define a mock class to
    # test the method run (method run of Class ansible.plugins.strategy

# Generated at 2022-06-13 15:08:13.832094
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    import unittest.mock as mock
    from ansible.errors import AnsibleError
    from ansible import constants as C
    import time

    tqm = mock.MagicMock()
    iterator = mock.MagicMock()
    play_context = mock.MagicMock()
    _workers = mock.MagicMock()
    _flushed_hosts = mock.MagicMock()
    _hosts_cache = mock.MagicMock()
    _hosts_cache_all = mock.MagicMock()
    _blocked_hosts = mock.MagicMock()
    _host_pinned = mock.MagicMock()
    _tqm = mock.MagicMock()
    _tqm._terminated = mock.MagicMock()
    _tqm.get_hosts_left = mock.Magic

# Generated at 2022-06-13 15:08:21.853590
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # test class to mock the objects needed for strategy_module.py
    class TestModule(object):
        def __init__(self,name,action,any_errors_fatal,conditionals,collections,role):
            self.name = name
            self.action = action
            self.any_errors_fatal = any_errors_fatal
            self.conditionals = conditionals
            self.collections = collections
            self.role = role
    
    class TestTMQ(object):
        def __init__(self):
            pass
        
        def send_callback(self, msg):
            pass

    # create __main__ objects
    test_tmq = TestTMQ()

# Generated at 2022-06-13 15:08:22.974113
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    tqm = TaskQueueManager()
    strategy = StrategyModule(tqm)
    strategy.run(iterator,play_context)


# Generated at 2022-06-13 15:08:35.519694
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
  from ansible_collections.notstdlib.moveitallout.tests.unit.mock.loader import DictDataLoader
  from ansible.vars.manager import VariableManager
  from ansible.inventory.manager import InventoryManager
  from ansible.playbook.play import Play
  from ansible.executor.task_queue_manager import TaskQueueManager
  my_var = dict(
  host_one = 'ok',
  host_two = 'ok',
)

  inventory = InventoryManager(loader=DictDataLoader({'hosts':my_var}))
  variable_manager = VariableManager(loader=DictDataLoader({'host_vars':my_var}))

# Generated at 2022-06-13 15:08:36.039893
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 15:08:36.549484
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert(True)

# Generated at 2022-06-13 15:08:39.280937
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    test_strategyModule_run=StrategyModule()
    test_strategyModule_run.run()

# Generated at 2022-06-13 15:08:39.977554
# Unit test for method run of class StrategyModule

# Generated at 2022-06-13 15:08:40.658267
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    assert True

# Generated at 2022-06-13 15:09:29.180749
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    assert sm is not None

# Generated at 2022-06-13 15:09:35.949234
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    '''
    Test for running a set of module steps
    '''
    # create a mock_iterator class
    class mock_iterator(object):
        def is_failed(self, host):
            return False

        def get_next_task_for_host(self, host, peek=True):
            return (True, True)

    # create a mock_play_context class
    class mock_play_context(object):
        def __init__(self):
            self.max_fail_percentage = None
            self.remote_addr = None
            self.remote_user = None
            self.connection = None
            self.become = None
            self.become_method = None
            self.become_user = None
            self.become_pass = None
            self.no_log = None
            self.verb

# Generated at 2022-06-13 15:09:42.116583
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    
    # test inputs
    tqm = self.tqm
    iterator = self.iterator
    play_context = self.play_context

    # test setup
    self.setup_global_objects()

    # Create instance of StrategyModule
    strategymodule_instance = StrategyModule(tqm)
    # test call of run method
    result = strategymodule_instance.run(iterator, play_context)

    # assert return code
    self.assertEqual(result, True)

# Generated at 2022-06-13 15:09:49.148765
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    results = []
    def mock_send_callback(self, key, value,  *args,  **kwargs):
        results.append({key: value})
    StrategyModule._send_callback = mock_send_callback
    def mock_send_callback2(self, key, value,  *args,  **kwargs):
        results.append({key: value})
    StrategyBase._send_callback = mock_send_callback2
    class mock_action_loader():
        def get(self, action, class_only=True, collection_list=None):
            return None
    action_loader.get = mock_action_loader.get
    mock_StragegyModule = StrategyModule()
    mock_StragegyModule._tqm = StrategyModule

# Generated at 2022-06-13 15:09:53.749003
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    import mock
    mock_tqm = mock.create_autospec(TaskQueueManager)
    mock_iterator = mock.create_autospec(BaseIterator)
    mock_play_context = mock.create_autospec(PlayContext)

    sm = StrategyModule.run(mock_tqm, mock_iterator, mock_play_context)

    return sm

# Generated at 2022-06-13 15:10:04.775693
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    try:
        import unittest2 as unittest
    except:
        import unittest
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.handler import Handler
    from ansible.playbook.block import Block
    from ansible.playbook.included_file import IncludedFile
    from ansible.playbook.role_include import RoleInclude
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.role import Role
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

# Generated at 2022-06-13 15:10:11.145660
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # test case 1
    # PlayContext.new(name='test')
    play_context = PlayContext(name='test')
    play_context.new(name='test')
    # BaseHost(name='fake_host', group=None, port=None)
    host = BaseHost(name='fake_host', group=None, port=None)
    # fake iterator
    iterator = Iterator('fake_iterator')
    iterator.set_task_state(task=iterator._task, result=None, state='fake')
    
    # StrategyModule.__init__(self, tqm)
    # threading.Thread.__init__(self)
    # super(StrategyModule, self).__init__(tqm)
    # self.name = 'StrategyModule'
    # self._blocked_hosts = {}


# Generated at 2022-06-13 15:10:23.135079
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.utils.vars import load_extra_vars
    import ansible.constants as C
    inventory = InventoryManager(host_list='localhost')
    variable_manager = VariableManager(inventory=inventory)
    loader = DataLoader()
    tqm = TaskQueueManager(
            inventory=inventory,
            variable_manager=variable_manager,
            loader=loader,
            passwords=dict(),
            stdout_callback="default",
        )

# Generated at 2022-06-13 15:10:30.978739
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
  # unit test without parameter
  try:
    # create an object of class StrategyModule
    strategy_module = StrategyModule(tqm)
    # call method run of class StrategyModule without parameter
    strategy_module.run(iterator, play_context)
  except Exception as e:
    display.warning(e)
  # unit test with parameter
  try:
    # create an object of class StrategyModule
    strategy_module = StrategyModule(tqm)
    # call method run of class StrategyModule with parameter
    strategy_module.run(iterator, play_context)
  except Exception as e:
    display.warning(e)

# Generated at 2022-06-13 15:10:41.638251
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    from ansible.playbook import Playbook
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.inventory import Inventory, Host, Group
    import ansible.plugins.loader as plugin_loader
    import ansible.plugins.action as action_plugin
    import ansible.plugins.callback as callback_plugin
    import ansible.plugins.connection as connection_plugin
    import ansible.plugins.lookup as lookup_plugin
    import ansible.plugins.filter as filter_plugin
    import ansible.plugins.module_loader as module_loader_plugin
    import ansible.plugins.strategy as strategy_plugin

# Generated at 2022-06-13 15:13:01.245990
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
  from ansible.utils.vars import combine_vars
  from ansible.parsing.dataloader import DataLoader
  from ansible.playbook.play import Play
  from ansible.template import Templar
  my_dl= DataLoader()
  my_play= Play().load(dict(name="Ansible Play 0",
                            hosts="all",
                            gather_facts="no",
                            tasks=[dict(action=dict(module='setup',args=''), register='shell_out'),
                                   dict(action=dict(module='debug',
                                                    args=dict(msg='{{shell_out.stdout}}')))]))

  variable_manager= VariableManager()
  variable_manager.extra_vars= {'hostvars': {}}


# Generated at 2022-06-13 15:13:05.671543
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    tqm_obj = TaskQueueManager()
    strategy_obj = StrategyModule(tqm_obj)
    play_context_obj = PlayContext()
    iterator_obj = BlockIterator()
    strategy_obj.run(iterator_obj, play_context_obj)


# Generated at 2022-06-13 15:13:06.713209
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    # TODO: Add unit test for method run of class StrategyModule
    pass

# Generated at 2022-06-13 15:13:09.150487
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Testing private variable
    assert StrategyModule._host_pinned == False, "The variable should be False"


# Generated at 2022-06-13 15:13:10.287797
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    pass

# Generated at 2022-06-13 15:13:13.890376
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    tqm = None
    iterator = None
    play_context = None
    obj = StrategyModule(tqm)
    result = obj.run(iterator, play_context)
    assert result is None

# Generated at 2022-06-13 15:13:23.007996
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TempClass(object):
        def __init__(self, value):
            self.value = value

    class TestStrategyModule(StrategyModule):
        def __init__(self, tqm):
            super(TestStrategyModule, self).__init__(tqm)
            self.temp_class = TempClass(value=123)

    temp = TempClass(value=123)
    assert temp.value == 123

    # tqm = TempClass(value=123)
    # test_StrategyModule = TestStrategyModule(tqm)
    # assert test_StrategyModule.temp_class.value == 123

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:13:24.521207
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
  tqm = None
  iterator = None
  play_context = None
  return_value = StrategyModule(tqm).run(iterator, play_context)
  assert return_value == None

# Generated at 2022-06-13 15:13:25.929387
# Unit test for method run of class StrategyModule
def test_StrategyModule_run():
    module = AnsibleModule(argument_spec=dict())
    module.exit_json = lambda: None


# Generated at 2022-06-13 15:13:28.985781
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy = StrategyModule(tqm)
    assert(tqm == strategy._tqm)