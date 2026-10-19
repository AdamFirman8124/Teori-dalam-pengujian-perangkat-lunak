

# Generated at 2022-06-13 14:55:28.526780
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None

# =================================================================================


# Generated at 2022-06-13 14:55:40.456506
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.playbook.play
    import ansible.playbook.task
    import ansible.playbook.task_include
    import ansible.plugins.strategy
    import ansible.template
    import ansible.template.template

    import ansible.utils
    from ansible.errors import AnsibleError

    import ansible.inventory.host
    import ansible.inventory.group

    # Imports for unit test
    m = StrategyModule(None)
    try:
        ansible.template.template.AnsibleEnvironment('/')
    except AnsibleError:
        print('AnsibleEnvironment works properly')

    my_play = ansible.playbook.play.Play()
    my_play.hosts = 'all'
    my_play.vars = {'var1': 'value1'}
    my_

# Generated at 2022-06-13 14:55:41.483597
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 14:55:47.078865
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    s = StrategyModule(tqm)
    assert s.debugger_active is True

# This class is used to drive debugger and actual task execution.
# Note that debugger is readline() and stdin enabled (i.e. use readline library, if available).
# It also handle command completion and history, if readline is enabled.
#


# Generated at 2022-06-13 14:55:50.643334
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TQM:
        def __init__(self):
            pass
    tqm = TQM()
    s = StrategyModule(tqm)
    assert s.debugger_active == True


# Generated at 2022-06-13 14:55:52.437176
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(tqm=None)

    assert sm
    assert sm.debugger_active



# Generated at 2022-06-13 14:55:54.500256
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # test_StrategyModule is a dummy test case
    # to suppress "No tests found." error message
    pass


# debug class

# Generated at 2022-06-13 14:55:55.687979
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    a = StrategyModule(None)
    assert a.debugger_active



# Generated at 2022-06-13 14:55:56.610128
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)



# Generated at 2022-06-13 14:55:58.557846
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm=None)
    assert strategy.debugger_active == True


# Generated at 2022-06-13 14:56:01.488667
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategyModule = StrategyModule(None)
    assert strategyModule.debugger_active == True


# Generated at 2022-06-13 14:56:02.423101
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)

# vim: set et ts=4 sw=4 :

# Generated at 2022-06-13 14:56:11.859328
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestTaskQueueManager():
        def __init__(self):
            self.counts = dict()
            self.counts['foo'] = 1
            self.counts['bar'] = 2

        def get_host_objs(self):
            return []

        def cleanup(self):
            pass

    test_tqm = TestTaskQueueManager()
    test_tqm.counts['foo'] = 1
    test_tqm.counts['bar'] = 2

    sm = StrategyModule(test_tqm)
    assert isinstance(sm, StrategyModule)

    assert sm.tqm == test_tqm
    assert sm.debugger_active == True


# Generated at 2022-06-13 14:56:14.447931
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(tqm=None)
    assert strategy_module.get_playbook_checksum() is None
    assert strategy_module.get_inventory_checksum() is None



# Generated at 2022-06-13 14:56:22.889854
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.utils.plugin_docs as utils
    import ansible.plugins.strategy.debug as m_debug
    import ansible.plugins.strategy.linear as m_linear
    import ansible.utils.module_docs as utils
    import ansible.utils.template as utils

    # StragegyModule(tqm)
    #    def __init__(self, tqm):
    #        super(StrategyModule, self).__init__(tqm)
    #        self.debugger_active = True
    def __init__(self, tqm):
        super(StrategyModule, self).__init__(tqm)
        self.debugger_active = True


# Generated at 2022-06-13 14:56:24.721158
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(None)
    assert strategy.debugger_active == True


# Generated at 2022-06-13 14:56:30.570050
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_int_tqm = 123
    test_obj_strategy_module = StrategyModule(test_int_tqm)
    assert test_obj_strategy_module.tqm == test_int_tqm
    assert test_obj_strategy_module.debugger_active == True



# Generated at 2022-06-13 14:56:31.276609
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    return True



# Generated at 2022-06-13 14:56:31.907670
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 14:56:34.205157
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  strategy_module = StrategyModule('tqm')
  assert(strategy_module.debugger_active == True)


# Generated at 2022-06-13 14:56:40.670134
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_tqm= {}
    assert isinstance(StrategyModule(test_tqm), LinearStrategyModule)

# Test abstract class of class StrategyModule

# Generated at 2022-06-13 14:56:42.023063
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = FakeTQM()
    sm = StrategyModule(tqm)


# Generated at 2022-06-13 14:56:45.931613
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    lin_st_mod = LinearStrategyModule(tqm = None)
    st_mod = StrategyModule(tqm = None)
    assert not lin_st_mod.debugger_active
    assert st_mod.debugger_active
    
    


# Generated at 2022-06-13 14:56:46.725309
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('test_StrategyModule')
    StrategyModule(None)
    assert True



# Generated at 2022-06-13 14:56:47.265495
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule != None


# Generated at 2022-06-13 14:56:52.072197
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestClass(object):
        pass
    tqm = TestClass()
    strategy = StrategyModule(tqm)

    assert strategy is not None
    assert strategy.debugger_active == True


# Generated at 2022-06-13 14:56:54.294087
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Begin unit test for constructor of class StrategyModule")
    dummy_tqm = None
    sm = StrategyModule(dummy_tqm)
    assert sm.tqm == dummy_tqm
    assert sm.debugger_active
    print("End of unit test for constructor of class StrategyModule")


# Generated at 2022-06-13 14:56:57.611507
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert type(StrategyModule) == type(object)
    assert issubclass(StrategyModule, LinearStrategyModule)
    assert StrategyModule.__name__ == 'StrategyModule'
    assert StrategyModule.__module__ == __name__


# Generated at 2022-06-13 14:56:58.555469
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule # Exists


# Generated at 2022-06-13 14:57:01.852248
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'dummy'
    strategy_module = StrategyModule(tqm)
    assert strategy_module is not None
    assert strategy_module.tqm is tqm
    assert strategy_module.debugger_active is True


# Generated at 2022-06-13 14:57:09.179436
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Now testing constructor of class StrategyModule...")

try:
    print("Trying to create StrategyModule...")
    test_StrategyModule()
    print("Passed!")
except:
    print("Failed!")
    raise



# Generated at 2022-06-13 14:57:17.179111
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass
        #print(cmd.cmd.Cmd)
        #print("Debug: str_module.__init__()")

    #def __exit__(self, *args):
        #pass
        #print("Debug: str_module.__exit__()")

    #def _queue_task(self, host, task, task_vars, play_context):
        #pass
        #print("Debug: str_module._queue_task()")

    #def run(self, iterator, play_context):
        #pass
        #print("Debug: str_module.run()")



# Generated at 2022-06-13 14:57:19.495760
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = type('test', (object,), {'callback':{'debug':'test'},'stats':False})
    test = StrategyModule(tqm)
    assert test.debugger_active == True


# Generated at 2022-06-13 14:57:20.252708
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    FormatStrategyModule()


# Generated at 2022-06-13 14:57:21.829240
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert strategy_module.debugger_active


# Generated at 2022-06-13 14:57:27.983960
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

    # def execute(self, iterator, play_context, new_stdin):
    #     '''
    #     Run the iterator until completion or until a task in the iterator
    #     fails or is to be retried.
    #     '''
    #     super(StrategyModule, self).execute(iterator, play_context, new_stdin)



# Generated at 2022-06-13 14:57:31.248426
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Mock some objects
    class Tqm(object):
        def __init__(self):
            self.tqm_variables = {}
    tqm = Tqm()

    StrategyModule(tqm)

# Tests

# Generated at 2022-06-13 14:57:32.443807
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule()



# Generated at 2022-06-13 14:57:35.834875
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm_instance = None
    debug_result = StrategyModule.__init__(StrategyModule, tqm_instance)
    assert debug_result.debugger_active == True



# Generated at 2022-06-13 14:57:36.715985
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 14:57:49.425575
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        from ansible.module_utils.common._collections_compat import MutableMapping
    except ImportError:
        raise SkipTest("collections.MutableMapping available in Python 2.6 and later")
    test_StrategyModule = StrategyModule(MutableMapping)
    assert isinstance(test_StrategyModule, StrategyModule)

# DO NOT EDIT. BOILERPLATE CODE FOR TESTS

# Generated at 2022-06-13 14:57:52.431978
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    #TODO: to be implemented
    strategy_mod = StrategyModule('tqm')
    assert True


# Generated at 2022-06-13 14:57:57.243576
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class tqm():
        def __init__(self, hosts, **kwargs):
            self.hosts = hosts
            self.workers = 2
            self.vars = dict()
            self.vars['hostvars'] = dict()
            self.settings = dict()
            self.settings['hostfile'] = 'hosts'
            self.settings['host_list'] = 'hosts'
            self.settings['subset'] = 'all'
            self.settings['module_name'] = 'ping'
            self.settings['module_path'] = 'modules'
            self.settings['module_args'] = dict()
            self.settings['module_args']['data'] = 'pingpingpingpingpingpingpingxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
            self.variables = dict()


# Generated at 2022-06-13 14:58:01.429030
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.strategy.debug as debug_module
    strategy_module = debug_module.StrategyModule(None)
    assert strategy_module.debugger_active == True
    assert isinstance(strategy_module, debug_module.StrategyModule)
    assert isinstance(strategy_module, LinearStrategyModule)


# Generated at 2022-06-13 14:58:03.026695
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module_object = StrategyModule(None)
    assert strategy_module_object.debugger_active == True


# Generated at 2022-06-13 14:58:13.720384
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    if __name__ == '__main__':
      from ansible.inventory.manager import InventoryManager
      from ansible.vars.manager import VariableManager
      from ansible.playbook.play import Play
      from ansible.executor.task_queue_manager import TaskQueueManager
      from ansible.parsing.dataloader import DataLoader
      from ansible.module_utils.common.collections import ImmutableDict
      from ansible.utils.display import Display

      display = Display()
      loader = DataLoader()

      c = InventoryManager(loader=loader, sources=['localhost'])
      v = VariableManager()

# Generated at 2022-06-13 14:58:24.980226
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.host import Host
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block


# Generated at 2022-06-13 14:58:33.718984
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible import constants as C
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory import Inventory

    class MockRunnerOptions:
        def __init__(self):
            self.connection = 'local'
            self.remote_user = 'user'
            self.private_key_file = 'key'
            self.host_key_checking = True
            self.module_path = 'path'
            self.forks = 10
            self.become = True
            self.become_method = 'sudo'
            self.become_user = 'sudo'
            self.verbosity = 3
            self.check = True
            self.timeout = 10
            self.extra_vars = ['extra']


# Generated at 2022-06-13 14:58:36.343607
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_module = StrategyModule(None)
    assert (test_module.debugger_active == True)

    #print(test_module)
    assert True


# Generated at 2022-06-13 14:58:37.762353
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule(tqm=None)
    assert obj.debugger_active is True


# Generated at 2022-06-13 14:58:55.586195
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(tqm=None)
    assert strategy_module.debugger_active == True
    return "test_StrategyModule pass"



# Generated at 2022-06-13 14:58:57.986656
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Only initialize StrategyModule to make sure it works
    # TODO: add test for the two methods below
    StrategyModule(None)


# Generated at 2022-06-13 14:59:00.385687
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule(tqm=None)
    assert(s.tqm == None)
    assert(s.debugger_active == True)


# Generated at 2022-06-13 14:59:01.669109
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    assert isinstance(sm, StrategyModule)



# Generated at 2022-06-13 14:59:04.908935
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    class DummyTQM():
        def __init__(self):
            pass
        pass

    strategyModule = StrategyModule(DummyTQM())
    assert strategyModule.debugger_active == True


# Generated at 2022-06-13 14:59:07.119094
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule(None)
    assert(s.debugger_active is True)


# Generated at 2022-06-13 14:59:07.676038
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 14:59:11.251664
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # import and create object to test
    from ansible.plugins.strategy.debug import StrategyModule

    # create object to test
    tqm = "Test"
    StrategyModule(tqm)
    pass



# Generated at 2022-06-13 14:59:12.754997
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    st = StrategyModule(tqm = 'test')
    assert st.debugger_active == True



# Generated at 2022-06-13 14:59:13.813749
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule(tqm)

# Generated at 2022-06-13 14:59:56.481766
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy import StrategyBase
    from ansible.plugins.strategy import debug
    from ansible.utils.collection_functions import listize_dict
    from ansible.utils.collection_functions import listize_keys
    
    # Setup
    test_tqm = MockTqm()
    test_option_list = {
        'paramiko': {
            'unknown_host_cb': None,
            'load_system_host_keys': True,
            'key_filename': None,
            'timeout': 10,
            'ssh_args': '-C -o ControlMaster=auto -o ControlPersist=60s',
        }
    }
    
    # Exercise and verify
    test_result = debug.StrategyModule(tqm=test_tqm)

# Generated at 2022-06-13 14:59:57.092194
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:00:03.845499
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Constructor of class StrategyModule should do nothing
    for color in ('on_skipped', 'on_unreachable', 'on_no_hosts', 'on_async_poll', 'on_async_ok', 'on_async_failed', 'on_failed', 'on_ok', 'on_error'):
        if getattr(StrategyModule, color) != getattr(LinearStrategyModule, color):
            raise AssertionError



# Generated at 2022-06-13 15:00:05.978050
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    l = LinearStrategyModule()
    assert isinstance(l, LinearStrategyModule)


# Generated at 2022-06-13 15:00:10.853049
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    host_list = []
    for i in range(5):
        host = "host" + str(i)
        host_list.append(host)
    inventory_list = host_list
    tqm = "tqm"
    strategy_module = StrategyModule(tqm)
    assert isinstance(strategy_module, LinearStrategyModule)


# Generated at 2022-06-13 15:00:14.066376
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy import debug
    strategy = debug.StrategyModule(None)
    assert isinstance(strategy, StrategyModule)
    assert isinstance(strategy, LinearStrategyModule)
    assert strategy.debugger_active == True



# Generated at 2022-06-13 15:00:15.187090
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    t = "test"
    StrategyModule(t)


# Generated at 2022-06-13 15:00:21.174276
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    class FakeTqm():
        def __init__(self):
            self.host_list = [
                "localhost",
            ]

    tqm = FakeTqm()
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active == True


# TODO:
# Add tests for commands (not implemented yet).
# Add tests for debugger loop (not implemented yet).

# Generated at 2022-06-13 15:00:22.451189
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule(None)
    assert isinstance(obj, LinearStrategyModule)
    assert obj.debugger_active == True


# Generated at 2022-06-13 15:00:28.282982
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_StrategyModule.result = 'init'
    class TaskQueueManager: pass
    tqm = TaskQueueManager()
    StrategyModule(tqm)

test_StrategyModule.result = 'not_init'
test_StrategyModule()
if (test_StrategyModule.result != 'init'):
    raise Exception('StrategyModule.__init__ method issue')



# Generated at 2022-06-13 15:01:46.282597
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is no

# Generated at 2022-06-13 15:01:54.682943
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.callbacks
    import ansible.inventory
    import ansible.playbook
    import ansible.vars

    class FakePlay(object):
        def __init__(self):
            self.ROLE_CACHE = {}

    class FakeTask(object):
        def __init__(self):
            self.default_vars = {}
            self.no_log = True
            self.role = None

     # Create instance of StrategyModule class
    tqm = FakeTaskQueueManager()

    sm = StrategyModule(tqm)
    assert sm.debugger_active == True



# Generated at 2022-06-13 15:01:57.122392
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        assert(True)
    except AssertionError:
        print("Test StrategyModule: failed")
    else:
        print("Test StrategyModule: OK")


# Generated at 2022-06-13 15:02:05.599864
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler_task_include import HandlerTaskInclude
    from ansible import errors
    import ansible.constants as C

    try:
        # Create class
        task = StrategyModule(tqm=None)
    except Exception as e:
        print(e)
        assert False

    # test constructor
    assert isinstance(task, LinearStrategyModule)

    # test define return_data is bool
    assert isinstance(task.debugger_active, bool)


# Generated at 2022-06-13 15:02:12.823975
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    data = {
        'action': 'setup',
        'playbook': 'playbook.yml',
        'playbook_path': 'playbook.yml',
        'inventory': 'hosts',
        'hosts': ['host1'],
        'version': '2.1',
        'module_path': 'default_module_path',
        'forks': 10,
        'become': True,
        'become_method': 'sudo',
        'become_user': 'root',
        'remote_user': 'root',
        'vault_password': 'password',
        'passwords': {}
    }
    s = StrategyModule(data)
    assert s.debugger_active == True
    assert s.get_host_list() == ['host1']


# Generated at 2022-06-13 15:02:14.352163
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:02:15.560936
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True


# Generated at 2022-06-13 15:02:23.949857
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.loader import strategy_loader
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    class Options(object):
        def __init__(self):
            self.connection = 'local'
            self.module_path = None
            self.forks = 100
            self.remote_user = 'root'
            self.private_key_file

# Generated at 2022-06-13 15:02:26.003869
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TQM:
        ''' used to test module '''
        pass

    #TODO: test it


# Generated at 2022-06-13 15:02:26.881254
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule("tqm")


# Generated at 2022-06-13 15:05:18.243132
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None).debugger_active is True


# Generated at 2022-06-13 15:05:24.573183
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('Testing class StrategyModule...')
    # Test 1: Constructor Test
    tqm = 'defined'
    test = StrategyModule(tqm)

    assert(test.debugger_active == True)
    assert(test.tqm == tqm)
    print('Passed constructor test')
    print('Passed all tests')
    return

if __name__ == '__main__':
    # If called as unit test, run all tests
    test_StrategyModule()
    sys.exit(0)

# Generated at 2022-06-13 15:05:25.821073
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    global StrategyModule
    StrategyModule = LinearStrategyModule
