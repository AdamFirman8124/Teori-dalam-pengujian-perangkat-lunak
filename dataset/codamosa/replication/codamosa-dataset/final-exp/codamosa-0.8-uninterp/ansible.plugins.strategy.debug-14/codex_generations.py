

# Generated at 2022-06-13 14:55:28.516495
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True



# Generated at 2022-06-13 14:55:29.743312
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = {}
    x = StrategyModule(tqm)


# Generated at 2022-06-13 14:55:30.907124
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Representation of StrategyModule object to CLI

# Generated at 2022-06-13 14:55:32.418884
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert strategy_module.debugger_active == True



# Generated at 2022-06-13 14:55:34.256619
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(tqm=None)
    print(sm.tqm)
    print(sm.debugger_active)


# Generated at 2022-06-13 14:55:43.494365
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.utils.display import Display
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.playbook.play import Play

    display = Display()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=None, sources=[])
    variable_manager.set_inventory(inventory)
    playbooks = [Playbook()]
    play_iterator = PlayIterator(playbooks, variable_manager, loader=None)
    play = Next()
    play.hosts = ['localhost']
    play.tasks = [Task()]


# Generated at 2022-06-13 14:55:47.284464
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class debug_class():
        def __init__(self):
            self.debugger_active = True

    obj = StrategyModule(debug_class())

    assert obj.debugger_active



# Generated at 2022-06-13 14:55:48.723475
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)

# Main debug prompt class

# Generated at 2022-06-13 14:55:50.198200
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    global StrategyModule
    StrategyModule.__init__(StrategyModule)


# Generated at 2022-06-13 14:55:51.451103
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule('tqm')
    assert strategy_module
    assert strategy_module.tqm == 'tqm'
    assert strategy_module.debugger_active



# Generated at 2022-06-13 14:55:52.918678
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:56:00.776887
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Set-up for the test
    class TaskQueueManager:
        def __init__(self, hosts=None, tasks=None, task_queues=None, variable_manager=None, loader=None, options=None, passwords=None, stdout_callback=None, run_additional_callbacks=None, run_tree=None, inventory=None, variable_manager_args=None, pass_words=None, default_vars=None):
            self.hosts = hosts
            self.tasks = tasks
            self.task_queues = task_queues
            self.variable_manager = variable_manager
            self.loader = loader
            self.options = options
            self.passwords = passwords
            self.stdout_callback = stdout_callback
            self.run_additional_callbacks = run_additional_callbacks

# Generated at 2022-06-13 14:56:02.260778
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule("tqm")
    assert sm.debugger_active == True


# Generated at 2022-06-13 14:56:12.689365
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Param: tqm = TaskQueueManager
    tqm = ''
    # StrategyModule constructor
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active == True
    assert strategy.host_list == []
    assert strategy.module_name == 'debug'
    assert strategy.module_args == ''
    assert strategy.pattern == 'all'
    assert strategy.start_at_done == False
    assert strategy.step == False
    assert strategy.step_args == {}
    assert strategy.strategy == 'linear'
    assert strategy.strategy_args == {}
    assert strategy.tags == 'all'
    assert strategy.task_list == []
    assert strategy.step_list == []
    assert strategy.task_to_run == None
    assert strategy.valide_task_list == []
    assert strategy

# Generated at 2022-06-13 14:56:14.241817
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(None)
    assert strategy
    assert strategy.debugger_active



# Generated at 2022-06-13 14:56:15.399517
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'



# Generated at 2022-06-13 14:56:19.116695
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager(None, None, None, None, None, None, None)
    sm = StrategyModule(tqm)
    assert sm is not None
    assert sm.debugger_active is True


# Generated at 2022-06-13 14:56:24.659785
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.utils.display import Display
    from ansible.plugins.loader import module_loader
    # create dummy class for unit test
    class DummyTqm(object):
        stats = DummyStats()
        def __init__(self):
            self.display = Display()
            self.loader = module_loader
            self.global_vars = dict()
        def _final_q_unlocked(self):
            pass
        def _failed_hosts_unlocked(self):
            pass
    assert StrategyModule(DummyTqm())



# Generated at 2022-06-13 14:56:30.517297
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Can use multiple times with different task_queue_manager
    s = StrategyModule('task_queue_manager')
    assert s.debugger_active

# Make available to import
strategy_plugins = {
    'debug': StrategyModule,
}

HOST = ''

# The localhost command class.

# Generated at 2022-06-13 14:56:32.038649
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert hasattr(StrategyModule, '__init__')



# Generated at 2022-06-13 14:56:42.339440
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class FakeTQM:
        def __init__(self):
            self.inventory = Inventory
            self.var_manager = VariableManager
            self.loader = None
            self.options = None
            self.passwords = None
            self.stdout_callback = None
            self.run_tree = None
            self.stats = None

    class FakeInventory:
        def __init__(self):
            self.hosts = {
                'host1': {},
                'host2': {}
                }

    class FakeVariableManager:
        def __init__(self):
            self.hostvars = {
                'host1': {},
                'host2': {}
                }

    tqm = FakeTQM()
    sm = StrategyModule(tqm)

# Generated at 2022-06-13 14:56:51.197566
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Initialization
    class tqm_obj:
        def __init__(self):
            self.hosts = tqm_hosts_obj()

    class tqm_hosts_obj:
        def __init__(self):
            self.keys = ['1.2.3.4', '1.2.3.5']

    tqm = tqm_obj()

    # New object creation
    t = StrategyModule(tqm)

    # Tests
    assert t
    assert t.tqm == tqm
    assert len(t.tqm.hosts.keys) == 2
    assert t.tqm.hosts.keys[0] == '1.2.3.4'

# Generated at 2022-06-13 14:56:54.764536
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    tqm=TaskQueueManager()
    sm=StrategyModule(tqm)
    assert sm.debugger_active


# Generated at 2022-06-13 14:56:56.916890
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    s_m = StrategyModule(tqm)
    assert s_m.debugger_active



# Generated at 2022-06-13 14:56:59.344123
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    sm = StrategyModule(tqm)
    assert sm.tqm == tqm
    assert sm.debugger_active == True



# Generated at 2022-06-13 14:57:00.591064
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    return

# -----------------------------
# Module Execution.
#


# Generated at 2022-06-13 14:57:07.853738
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'test_tqm'
    strategy = StrategyModule(tqm)
    assert strategy.tqm == tqm
    assert strategy.debugger_active == True   # debugger_active = True 


# class DebuggerCmd(cmd.Cmd):
#     ''' A simple interactive session example '''
#     intro = 'Debugger session. Type ? to list commands.'
#     prompt = 'debug> '

#     def __init__(self, inventory, play, task_vars, play_context):
#         cmd.Cmd.__init__(self)
#         self.inventory = inventory
#         self.play = play
#         self.task_vars = task_vars
#         self.play_context = play_context

#     def default(self, line):
#         ''' Just

# Generated at 2022-06-13 14:57:08.759234
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule()
    

# Generated at 2022-06-13 14:57:12.661815
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # create StrategyModule instance
    strategy = StrategyModule(tqm=None)

    # check members initialized correctly
    assert strategy.debugger_active == True
# end


# Generated at 2022-06-13 14:57:14.464583
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert strategy_module.debugger_active == True



# Generated at 2022-06-13 14:57:19.222559
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule()
    assert obj


# Generated at 2022-06-13 14:57:20.551311
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    result = StrategyModule(None)
    assert result != None
    assert result.debugger_active == True


# Generated at 2022-06-13 14:57:31.609295
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TaskQueueManager:
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    class MockDisplay:
        color = True
        verbosity = 3
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
        def warning(self, msg):
            print(msg)
        def display(self, msg, color=None):
            print(msg)

    class MockVarManager:
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
        def add_host_vars(self, host, vars):
            self.host = host
            self.vars = vars


# Generated at 2022-06-13 14:57:43.646856
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        from ansible.playbook.play_context import PlayContext
    except:
        from ansible.playbook.play import PlayContext
    from ansible.playbook.task import Task

    try:
        from ansible.inventory.host import Host
    except:
        from ansible.inventory.host import Host as Host

    try:
        from ansible.inventory.manager import InventoryManager
    except:
        from ansible.inventory.manager import InventoryManager as InventoryManager

    try:
        from ansible.vars.manager import VariableManager
    except:
        from ansible.vars.manager import VariableManager as VariableManager

    try:
        from ansible.executor.task_queue_manager import TaskQueueManager
    except:
        from ansible.executor.task_queue_manager import TaskQueueManager as TaskQueueManager

# Generated at 2022-06-13 14:57:44.192338
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 14:57:51.469049
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestTQM():
        def __init__(self, hostvars, *args, **kwargs):
            self.hostvars = hostvars
        def get_host(self, hostname):
            return self.hostvars[hostname]
    hostvars = {
                 'localhost': {
                               'ansible_connection': 'local',
                               'ansible_host': 'localhost'
                              }
               }
    tqm = TestTQM(hostvars)
    strategy = StrategyModule(tqm)
    # check private attribute
    assert strategy._hosts_cache == {}


# Generated at 2022-06-13 14:58:01.586261
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

    # Create a command module
    # Determine if the commands that set variables work
    # Determine all the commands that will be useful for the user
    # Determine the order that the commands should be presented
    # Write out the player

    # TODO:
    # Determine if the commands that set variables work
    # Determine all the commands that will be useful for the user
    # Determine the order that the commands should be presented
    # Write out the player
    # Determine what variables to store and write them out
    # Write out the python code that will start this whole thing
    # Have it offer to write out the playbook file
    # Have it offer to write out the inventory file
    # Have it offer to write out a file with the list of hosts
    # Have it offer to run ansible

# Generated at 2022-06-13 14:58:02.071634
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 14:58:04.720959
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None 
    t = StrategyModule(tqm)  # Test if constructor works
    return t


# Generated at 2022-06-13 14:58:14.287556
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class Test:
        strategy = "Debug"
        module_path = None
        forks = 10
        become = False
        become_method = None
        become_user = None
        check = False
        remote_user = "test"
        remote_pass = "test"
        remote_port = 22
        private_key_file = "test"
        host_key_checking = False
        look_for_keys = False
        inventory = None
        verbosity = 0
        timeout = 10
        module_paths = None
        adhoc_poll_interval = 5
        connection_type = "smart"
        diff = False

    tqm = Test()
    strategy_module = StrategyModule(tqm)
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 14:58:22.746107
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)


# Generated at 2022-06-13 14:58:25.431017
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    obj = TaskQueueManager(list())
    s = StrategyModule(obj)
    assert s.debugger_active is True


# Generated at 2022-06-13 14:58:26.602891
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm = 'Test').debugger_active


# Generated at 2022-06-13 14:58:29.762974
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule(None)
    assert not s.debugger_active
    s.debugger_active = True
    assert s.debugger_active
    s.debugger_active = False
    assert not s.debugger_active


# Generated at 2022-06-13 14:58:33.335541
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('test Strategy Module')
    # Get a strategy object
    strategy = StrategyModule([])
    # Check the task queue manager object
    assert strategy.tqm
    assert strategy.get_next_task_lock
    assert strategy.debugger_active
    assert not strategy.stats



# Generated at 2022-06-13 14:58:34.103772
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:58:35.749547
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy_module = StrategyModule(tqm)
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 14:58:47.213133
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task

    play_context = PlayContext()
    play_source = dict(
        name="Ansible Play",
        hosts='localhost',
        gather_facts='no',
        tasks=[
            dict(action=dict(module='setup', args=dict())),
            dict(action=dict(module='shell', args='/bin/true'))
        ]
    )

    play = Play().load(play_source, variable_manager=None, loader=None)

    play._inject_facts = dict()

    # Fake the tqm
    class Tqm(): pass
    tqm = Tqm()

    s = StrategyModule(tqm)
    assert s

# Generated at 2022-06-13 14:58:47.779072
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 14:58:50.485569
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    assert sm.module_name == 'debug'
    assert sm.debugger_active is True



# Generated at 2022-06-13 14:59:12.531082
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Override sys.argv such as to contain "-vvv",
    # so that we can debug the 'load_callback_plugins' function
    prev_sys_argv = sys.argv
    sys.argv = prev_sys_argv + ['-vvv']
    tqm_object = FakeTaskQueueManager()
    sm = StrategyModule(tqm_object)
    sm.run()
    sys.argv = prev_sys_argv


# Generated at 2022-06-13 14:59:13.892471
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

    # create a test strategy module
    # module = StrategyModule()


# Generated at 2022-06-13 14:59:15.564657
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    assert sm.debugger_active == True



# Generated at 2022-06-13 14:59:17.811905
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # __init__(self, tqm):
    # TODO
    pass


# Generated at 2022-06-13 14:59:20.107529
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule(tqm=None)
    assert isinstance(s, StrategyModule)



# Generated at 2022-06-13 14:59:24.821360
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = {'test': 'test'}
    sm = StrategyModule(tqm)
    assert sm != None
    assert StrategyModule.__name__ == 'StrategyModule'
    assert sm.debugger_active

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 14:59:26.585007
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy_module = StrategyModule(tqm)

# Test for method get_host_list of class StrategyModule

# Generated at 2022-06-13 14:59:29.686172
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert strategy_module.debugger_active

###############################################################################
# code from http://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-in-python

# Generated at 2022-06-13 14:59:31.198260
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print(StrategyModule)


# Generated at 2022-06-13 14:59:33.004486
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy = StrategyModule(tqm)
    assert(strategy.debugger_active == True)


# Generated at 2022-06-13 15:00:05.117672
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = LinearStrategyModule()
    assert strategy.debugger_active == True

# Generated at 2022-06-13 15:00:14.656871
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.play import Play
    from ansible.playbook import Playbook
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars.manager import VariableManager


# Generated at 2022-06-13 15:00:17.877686
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = StrategyModule()
    assert bool(tqm) == True
    assert isinstance(tqm, StrategyModule)
    assert tqm.debugger_active == True



# Generated at 2022-06-13 15:00:24.722330
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager(inventory=None, variable_manager=None, loader=None, options=None, passwords=None, stdout_callback=None, run_additional_callbacks=True, run_tree=True)
    sm = StrategyModule(tqm)
    if sm.debugger_active == True:
        pass
    else:
        assert False



# Generated at 2022-06-13 15:00:25.926630
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:00:28.329151
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy_module = StrategyModule(tqm)
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 15:00:30.981458
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert strategy_module.tqm is None
    assert strategy_module.debugger_active is True



# Generated at 2022-06-13 15:00:32.482840
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(None)
    assert strategy is not None
    assert strategy.debugger_active is True


# Generated at 2022-06-13 15:00:33.525689
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule('test_tqm')
    assert(module.debugger_active == True)



# Generated at 2022-06-13 15:00:36.063203
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = DummyTQM()
    strategy_module = StrategyModule(tqm)
    assert isinstance(strategy_module, StrategyModule)
    assert isinstance(strategy_module, LinearStrategyModule)
    assert strategy_module.tqm == tqm
    assert strategy_module.debugger_active is True



# Generated at 2022-06-13 15:02:00.545376
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert LinearStrategyModule.__name__ == 'StrategyModule'  # constructor without __init__
    assert StrategyModule.__name__ == 'StrategyModule'  # constructor without __init__
    assert LinearStrategyModule.__mro__[0].__name__ == 'StrategyModule'  # constructor without __init__
    assert StrategyModule.__mro__[0].__name__ == 'StrategyModule'  # constructor without __init__
    assert LinearStrategyModule.__bases__[0].__name__ == 'object'  # constructor without __init__
    assert StrategyModule.__bases__[0].__name__ == 'object'  # constructor without __init__
    assert StrategyModule.__mro__[1].__name__ == 'LinearStrategyModule'
    tqm = None
    strategy_module = Strategy

# Generated at 2022-06-13 15:02:01.344439
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule()



# Generated at 2022-06-13 15:02:06.097920
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest

    class TestStrategyModule(unittest.TestCase):
        def test_class_definition(self):
            self.assertTrue(StrategyModule.__bases__[0], LinearStrategyModule)

    unittest.main()


# Generated at 2022-06-13 15:02:06.980553
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm)

# Generated at 2022-06-13 15:02:17.649909
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.utils import context_objects as co
    from ansible.plugins.strategy import StrategyBase
    from ansible.executor.task_queue_manager import TaskQueueManager

    class MockStrategyBase(StrategyBase):
        def __init__(self, tqm):
            super(MockStrategyBase, self).__init__(tqm)
                 
    class MockTaskQueueManager(TaskQueueManager):
        def __init__(self):
            self.tasks = []

    class MockTask:
        def __init__(self, name='debug_task'):
            self.name = name

    tqm = MockTaskQueueManager()
    tqm.tasks = [MockTask()]

    strategy = MockStrategyBase(tqm)

    # context_manager is a global
    co

# Generated at 2022-06-13 15:02:18.857233
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule(None)
    assert obj.debugger_active


# Generated at 2022-06-13 15:02:21.288604
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active == True
    assert strategy.tqm is tqm


# Generated at 2022-06-13 15:02:24.467034
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class Test_TQM(object):
        def set_isolation_level(self, level):
            pass

    t = Test_TQM()
    s = StrategyModule(t)
    assert s.debugger_active

# Class to handle commands issued by user in debug mode

# Generated at 2022-06-13 15:02:33.377333
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import unittest
    class test_StrategyModule(unittest.TestCase):
        def test__init__(self):
            from ansible.plugins.strategy.debug import StrategyModule
            from ansible.plugins.strategy.linear import StrategyModule as LinearStrategyModule
            from ansible.vars.manager import VariableManager

            from ansible.executor.task_queue_manager import TaskQueueManager
            from ansible.executor.play_iterator import PlayIterator
            from ansible.executor.process.worker import WorkerProcess
            from ansible.inventory.manager import InventoryManager

            from ansible.plugins.callback import CallbackBase
            import ansible.playbook.play
            import ansible.playbook.task
            import ansible.playbook.task_include
            import ansible.playbook.handler


# Generated at 2022-06-13 15:02:33.854253
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:05:21.874812
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = []
    sm = StrategyModule(tqm)
    print (sm.__class__.__name__)
    print (sm.debugger_active)
    assert sm
    assert sm.debugger_active

# Generated at 2022-06-13 15:05:22.702401
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 15:05:26.087353
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('\nTesting StrategyModule() constructor')
    tqm = 'some_tqm'
    strategy = StrategyModule(tqm)
    assert strategy.tqm == tqm
    assert strategy.debugger_active == True
    print('PASS')



# Generated at 2022-06-13 15:05:27.097622
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("\n")
    StrategyModule(None)
    print("Constructor: StrategyModule")

