

# Generated at 2022-06-13 14:55:24.403110
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
	return True


# Generated at 2022-06-13 14:55:25.964686
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__ == 'Debug session'


# Generated at 2022-06-13 14:55:28.331603
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True


# Generated at 2022-06-13 14:55:30.228839
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active == True


# Generated at 2022-06-13 14:55:30.754290
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:55:33.607800
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = TaskQueueManager()
    sm = StrategyModule(tqm)
    assert isinstance(sm, StrategyModule)
    assert isinstance(sm, LinearStrategyModule)
    assert sm.debugger_active is True


# Generated at 2022-06-13 14:55:34.757740
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    s = StrategyModule(tqm)


# Generated at 2022-06-13 14:55:35.265360
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:55:37.135831
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy_module = StrategyModule(tqm)
    assert strategy_module.debugger_active == True



# Generated at 2022-06-13 14:55:42.057083
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    test = StrategyModule(tqm)
    assert(test.debugger_active)

# If StrategyModule is imported as main module, the constructor of class Debugger is called
# DEBUGGER will be replaced by the debugger after loading
# DEBUGGER is used by function debug_break() in ansible-playbook, ansible and ansible-vault
DEBUGGER = None


# Generated at 2022-06-13 14:55:54.114282
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        from ansible import context
    except ImportError:
        # If ansible.utils.context is not available, exit
        sys.exit()
    import ansible.utils.display
    import ansible.plugins.loader
    import ansible.executor.task_queue_manager
    import ansible.executor.playbook_executor

    context.CLIARGS._parse_cli()
    cliargs = context.CLIARGS
    ansible.utils.display.Display.verbosity = cliargs.verbosity


# Generated at 2022-06-13 14:55:55.344020
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule()
    assert strategy_module is not None



# Generated at 2022-06-13 14:55:57.688619
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert hasattr(StrategyModule, '__init__')
    assert len(str(StrategyModule.__init__).split(', ')) == 5


# Generated at 2022-06-13 14:56:06.989194
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.task import Task
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.task_result import TaskResult
    from ansible.playbook.block import Block
    from ansible.playbook.play import Play
    from ansible.executor.play_iterator import PlayIterator
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager

    loader = DataLoader()
    Options = lambda x: None
    options = Options(connection='smart')

# Generated at 2022-06-13 14:56:08.938851
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    x = StrategyModule(None)
    assert(x.debugger_active == True)


# Generated at 2022-06-13 14:56:10.448785
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule()
    assert sm.debugger_active


# Generated at 2022-06-13 14:56:15.973919
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm_obj = DummyTqm()
    strategy_obj = StrategyModule(tqm_obj)
    assert strategy_obj._tqm == tqm_obj
    assert strategy_obj.get_host_list() == tqm_obj.host_list
    assert strategy_obj.get_variable_manager() == tqm_obj.variable_manager
    assert strategy_obj.get_loader() == tqm_obj.loader


# Generated at 2022-06-13 14:56:17.209796
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

    #strategy_module = StrategyModule()



# Generated at 2022-06-13 14:56:23.951240
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import __builtin__
    mock_tqm = type('', (), {})()
    # mock_tqm.hostvars = {}

# Generated at 2022-06-13 14:56:27.673642
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_StrategyModule = StrategyModule(tqm='')
    assert test_StrategyModule.debugger_active == True


# Generated at 2022-06-13 14:56:31.485188
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy = StrategyModule(tqm)
    assert strategy


# Generated at 2022-06-13 14:56:36.048787
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Unit test for constructor of class StrategyModule
    # # Initialize AnsibleEngine object
    # class TQM:
    #   pass
    # tqm = TQM()

    # # Initialize StrategyModule object
    # strategy = StrategyModule(tqm)
    # assert isinstance(strategy, StrategyModule)
    return


# Generated at 2022-06-13 14:56:37.400187
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:56:39.221536
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.debugger_active == True
# end of unit test


# Generated at 2022-06-13 14:56:44.322447
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test = cmd.Cmd()
    test.tqm = {'stdout_callback': 'json',
                '_run_progress_callbacks': []}
    strategy = StrategyModule(test.tqm)
    assert isinstance(strategy, StrategyModule)
    assert not strategy.debugger_active


# Generated at 2022-06-13 14:56:45.692261
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # TODO: Implement unit test
    print("Not implemented")


# Generated at 2022-06-13 14:56:48.112902
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Initialize debugger
    debugger = StrategyModule(tqm=None)
    assert debugger.debugger_active == True


# Executes tasks in interactive debug session

# Generated at 2022-06-13 14:56:49.887658
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule().debugger_active is True


# Generated at 2022-06-13 14:56:57.337478
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.strategy.debug

    # mock
    class MockTqm():
        def __init__(self):
            self.stats = []
            self.stdout_callback = ""

    tqm = MockTqm()
    strategy_module = ansible.plugins.strategy.debug.StrategyModule(tqm)

    assert tqm.get_host_list == strategy_module.get_host_list


# Generated at 2022-06-13 14:57:00.555601
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert(isinstance(strategy_module, LinearStrategyModule))
    assert(isinstance(strategy_module, StrategyModule))
    assert(strategy_module.debugger_active)


# Generated at 2022-06-13 14:57:15.840225
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Starting dummy TQM")
    class DummyTQM:
        def __init__(self, variables=dict()):
            pass
    class DummyRunner:
        def __init__(self, hosts, module_name, module_args, job_vars, check=False, become=False, become_method=None, become_user=None, verbosity=0, extra_vars=dict(), inventory=None):
            self.hosts = hosts
            self.module_name = module_name
            self.module_args = module_args
            self.job_vars = job_vars
            self.check = check
            self.become = become
            self.become_method = become_method
            self.become_user = become_user
            self.verbosity = verbosity
            self.extra_

# Generated at 2022-06-13 14:57:18.180641
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = TaskQueueManager()
    stratey_module = StrategyModule(tqm)
    assert strategy_module.tqm == tqm
    assert strategy_module.debugger_active == True
    assert strategy_module.host_pinned == False
    assert strategy_module.step == True


# Generated at 2022-06-13 14:57:22.565824
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = dict(
        stats=dict(
            dark=dict(skipped=dict(hosts=[])),
            failures=dict(hosts=[]),
            ok=dict(hosts=[]),
            processed=dict(hosts=[]),
        )
    )
    strategy_module = StrategyModule(tqm)
    assert strategy_module.debugger_active



# Generated at 2022-06-13 14:57:25.600136
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule(None)
    assert obj.debugger_active == True

# Constructor of class Debugger

# Generated at 2022-06-13 14:57:26.674687
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None).debugger_active

# Generated at 2022-06-13 14:57:28.407328
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    assert isinstance(StrategyModule(tqm), StrategyModule)


# Generated at 2022-06-13 14:57:28.912382
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True

# Generated at 2022-06-13 14:57:30.259782
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('In StrategyModule_test')
    # TODO



# Generated at 2022-06-13 14:57:42.242129
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('\n*** unit test for StrategyModule constructor')
    import collections
    import logging
    import threading
    from ansible.plugins.loader import callback_loader
    Class_TQM = collections.namedtuple('TQM', ['host_list', 'stats', 'failed_hosts'])
    Class_Host = collections.namedtuple('Host', ['name'])
    Class_Task = collections.namedtuple('Task', ['name'])
    tqm = Class_TQM(
        host_list=['foo', 'bar'],
        stats=Class_Task(name='stats'),
        failed_hosts=Class_Host(name='failed_hosts')
    )
    Class_VarManager = collections.namedtuple('VarManager', ['hostvars'])

# Generated at 2022-06-13 14:57:43.157018
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule(tqm = "None" )
    assert obj.debugger_active == True



# Generated at 2022-06-13 14:57:57.268908
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import unittest
    from ansible.playbook.task_include import TaskInclude

    class TaskQueueManagerMock(object):
        def __init__(self):
            self.host_failed = False
            self.host_unreachable = False
            self.host_skipped = False
            self.host_ok = False
            self.host_ok_with_data = False
            self.host_ok_fail_inventory_always = False

        def update_success_stats(self, host, result):
            host_result = result._result
            if host_result.get('unreachable'):
                self.host_unreachable = True
            elif host_result.get('failed'):
                self.host_failed = True
            elif host_result.get('skipped'):
                self.host_

# Generated at 2022-06-13 14:58:00.842420
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy.debug import StrategyModule
    tqm = "test_tqm"
    strategy_module = StrategyModule(tqm)
    assert True == isinstance(strategy_module.tqm, (str))


# Generated at 2022-06-13 14:58:04.093638
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins
    tqm.setup_loader()
    assert ansible.plugins.set_classpath_plugin(tqm, 'strategy', 'debugger')
    assert StrategyModule(tqm)



# Generated at 2022-06-13 14:58:04.842757
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:58:14.686071
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_mod = StrategyModule()
    assert strategy_mod.debugger_active == True


    def run(self, iterator, play_context):
        '''
        Main entry point for the plugin, calls the strategy specific code
        to run the given iterator.
        '''

        # Initialize the shared dictionary containing the variables (results of
        # the tasks, host facts, etc.)
        self._shared_loader_obj.update_basedir('/ABS/PATH')

        # get the hosts filtered out on the base of the subset parameter
        self._tqm.get_filtered_hosts()
        self._tqm.write_playbook_origins_to_hosts()

        # cache the fact data from disc
        self._tqm.add_tasks(iterator)
        self._tqm.run_cache()

# Generated at 2022-06-13 14:58:17.800880
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        tqm = FakeTqm()
    except Exception:
        pass
    strategy_module = StrategyModule(tqm)
    assert strategy_module


# Generated at 2022-06-13 14:58:23.109290
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(tqm)
    pass

    '''
    def run_tasks(self, iterator):
        '''

# Generated at 2022-06-13 14:58:23.685623
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule()
    return type(obj) == StrategyModule



# Generated at 2022-06-13 14:58:26.888627
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True
    sm.debugger_active = False
    assert sm.debugger_active == False

# Task execution is 'linear' but controlled by an interactive debug session.

# Generated at 2022-06-13 14:58:28.281981
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    StrategyModule(tqm)


# Generated at 2022-06-13 14:59:34.960591
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule



# Generated at 2022-06-13 14:59:36.237734
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm='something')


# Generated at 2022-06-13 14:59:36.804073
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None


# Generated at 2022-06-13 14:59:37.285193
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__



# Generated at 2022-06-13 14:59:41.039334
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        test_tqm = None
        StrategyModule(test_tqm)
    except Exception:
        pass
    else:
        assert False, "test_StrategyModule test failed."


# Generated at 2022-06-13 14:59:45.532840
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    parm1 = StrategyModule('task result manager')
    #parm1.__init__('task result manager')
    assert parm1.tqm == 'task result manager'
    assert parm1.debugger_active == True
    #assert parm1.tqm.debugger_active == 'task result manager'



# Generated at 2022-06-13 14:59:48.088797
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Try to test the constructor of class StrategyModule
    strategy = StrategyModule(None)
    assert strategy.debugger_active == True
    


# Generated at 2022-06-13 14:59:56.747220
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestStrategyModule:
        def __init__(self, tqm):
            self.tasks_in_play = tqm.play
            self.tasks_in_play.name = 'test_play'
            self.task_notify = [1, 2]
            self.task_notified = self.task_notify
            self.task_failed = False
            self.cur_task_name = ''
            self.task_failed = None
            self.cur_task = None
            self.queue = self.tasks_in_play.get_next_task_for_host(None)
            self.tasks_notified = set()
            self.debugger_active = True

    class TestTqm:
        tasks_in_play = [1, 2, 3]
        play = TestT

# Generated at 2022-06-13 15:00:07.793455
# Unit test for constructor of class StrategyModule

# Generated at 2022-06-13 15:00:09.092226
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    a=StrategyModule()
    assert a.debugger_active


# Generated at 2022-06-13 15:02:05.364463
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('\n***** Started unit testing for constructor of class StrategyModule *****')
    print('\n***Initializing StrategyModule***')
    tqm = None
    strategy_module = StrategyModule(tqm)
    assert strategy_module.debugger_active == True
    assert isinstance(strategy_module, LinearStrategyModule)
    del strategy_module
    print('\n***** Ended unit testing for constructor of class StrategyModule *****\n')
    
    
   

# Generated at 2022-06-13 15:02:06.589338
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = {} 
    print(StrategyModule(tqm))



# Generated at 2022-06-13 15:02:07.211210
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:02:17.645342
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.play import Play
    play_source =  dict(
            name = "Ansible Play 0",
            hosts = 'localhost',
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module='shell', args='ls'), register='shell_out'),
                dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
             ]
        )
    play = Play().load(play_source, variable_manager={}, loader=None)
    tqm = None
    StrategyModule(tqm).run(play)

if __name__ == '__main__':
    print('*** Module execution ***')
    test_StrategyModule()
    print('*** Done ***')

# Generated at 2022-06-13 15:02:19.793470
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__ is not None
    assert StrategyModule.__init__.__doc__ is not None


# Generated at 2022-06-13 15:02:28.283833
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import json
    import sys
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager

    class Options:
        def __init__(self):
            self.connection = 'local'
            self.forks = 1
            self.inventory = './tests/inventory'
            self.become = False
            self.check = False
            self.module_path = './lib'
            self.become_method = 'sudo'
            self.become_user = 'root'
            self.module_name = ''
            self.listhosts = None

# Generated at 2022-06-13 15:02:35.934792
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = TaskQueueManager(
        inventory=Inventory(),
        variable_manager=VariableManager(),
        loader=DataLoader(),
        options=Options(),
        passwords=dict(vault_pass='secret'),
        stdout_callback=None,
    )
    strategy = StrategyModule(tqm)
    tqm.strategy = strategy
    assert strategy.debugger_active is True
    assert strategy.name == 'debug'


# TODO: make sure the following are a subset of existing plugins
# class DebugCmd(cmd.Cmd):
#     """
#     Simple Shell that executes tasks in order
#     """
#     def __init__(self, tqm=None, play=None):
#         cmd.Cmd.__init__(self)
#         self.tqm = tqm
#         self.

# Generated at 2022-06-13 15:02:37.426587
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  assert(True)


# Generated at 2022-06-13 15:02:38.740090
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == "StrategyModule"


# Generated at 2022-06-13 15:02:48.043402
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.cli.playbook.play_context import PlayContext
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.playbook.play import Play

    loader = DataLoader()
    variable_manager = VariableManager()
    inventory = InventoryManager(loader=loader, variable_manager=variable_manager)
    variable_manager.set_inventory(inventory)
    
    inventory.clear_pattern_cache()
    #inventory.add_host(host='host1', port=22)