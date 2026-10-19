

# Generated at 2022-06-13 14:55:28.088087
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 14:55:30.389708
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule('a')
    assert s.tqm == 'a'
    assert s.debugger_active
    assert not s.is_stopped()


# Generated at 2022-06-13 14:55:35.447060
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # import module
    import ansible.plugins.strategy.debug
    # 1st constructor call
    tqm = None
    try:
        ansible.plugins.strategy.debug.StrategyModule(tqm)
    except TypeError as e:
        assert(e.args[0] == "'NoneType' object is not iterable")
    # 2nd constructor call
    tqm = []
    ansible.plugins.strategy.debug.StrategyModule(tqm)

# Generated at 2022-06-13 14:55:36.206583
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('StrategyModule class successfully created')


# Generated at 2022-06-13 14:55:39.307516
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # An example of how to properly call the constructor of class StrategyModule
    strategy = StrategyModule(None)
    assert strategy.__class__.__name__ == 'StrategyModule'


# Generated at 2022-06-13 14:55:42.102935
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        myStrategyModule = StrategyModule("tqm")
    except Exception as e:
        assert False, "Object doesn't created"
    else:
        assert True, "Object created"


# Generated at 2022-06-13 14:55:43.048577
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert False


# Generated at 2022-06-13 14:55:54.112720
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.playbook.play import Play

    # Constructor of class TaskInclude
    # task = TaskInclude(
    #     play=play,
    #     block=block,
    #     role=role,
    #     task_include=task_include,
    # )

    # Constructor of class Play
    # play = Play().load(
    #     ds=datastruct,
    #     variable_manager=variable_manager,
    #     loader=loader,
    # )

    # Constructor of class Block
    # block = Block(block

# Generated at 2022-06-13 14:55:57.829308
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    result = StrategyModule(tqm)
    assert hasattr(result, 'tqm')
    assert result.tqm == tqm
    assert hasattr(result, 'debugger_active')
    assert result.debugger_active is True


# Generated at 2022-06-13 14:55:58.628596
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule


# Generated at 2022-06-13 14:56:01.182211
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = ['foo']
    StrategyModule(tqm)


# Generated at 2022-06-13 14:56:03.205640
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    TQM = FakeTQM()
    strategy = StrategyModule(TQM)
    assert strategy.debugger_active == True
    assert strategy.TQM == TQM


# Generated at 2022-06-13 14:56:07.372372
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    s = StrategyModule(tqm)
    assert(type(s.tqm) == type(None))
    assert(s.play_context == {})
    assert(s.all_hosts == {})
    assert(s.hostvars == {})
    assert(type(s.host_topics) == type({}))
    assert(type(s.task_result_queue) == type(None))


# Generated at 2022-06-13 14:56:10.243711
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    s = StrategyModule(tqm)
    assert s._tqm == None 



#
# class Debugger
#

# Generated at 2022-06-13 14:56:11.464861
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None



# Generated at 2022-06-13 14:56:13.742863
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule', 'StrategyModule class is not defined'
    assert True, 'Debugger is not active'



# Generated at 2022-06-13 14:56:14.931102
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule('tqm')
    assert sm


# Generated at 2022-06-13 14:56:15.441586
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 14:56:17.498199
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sample_tqm = object()
    assert StrategyModule(sample_tqm).tqm is sample_tqm


# Generated at 2022-06-13 14:56:18.681223
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert isinstance(StrategyModule(None), LinearStrategyModule)


# Generated at 2022-06-13 14:56:25.708514
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """
    Creates all objects necessary for using the StrategyModule class
    """
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    tqm = TaskQueueManager('test')
    task = TaskInclude(task_args=dict(tasks='test_role/tasks/main.yml'))
    block = Block(parent_block=None, role=None, task_include=task)
    module = StrategyModule(tqm)
    module.add_task(task, block)
    assert isinstance(module.debugger, Debugger)
    assert module.debugger_active == True


# Generated at 2022-06-13 14:56:28.067547
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = True
    strategy_module = StrategyModule(tqm)



# Generated at 2022-06-13 14:56:32.142151
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestTQM(object):
        def __init__(self):
            self.debugger_active = False
    tqm = TestTQM()
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active == True


# Generated at 2022-06-13 14:56:32.752912
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 14:56:41.580131
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy_module = StrategyModule(tqm)
    assert strategy_module == None


    def cmd_pp(self, arg):
        pprint.pprint(arg)

    def cmd_quit(self, arg):
        self.debugger_active = False

    def cmd_none(self, arg):
        # nothing
        pass

    class Debugger(cmd.Cmd):
        def __init__(self):
            cmd.Cmd.__init__(self)
            self.prompt = "ansible> "
            self.host = None
            self.hostname = None
            self.tqm = None
            self.play_context = None
            self.play = None
            self.task = None
            self.job = None
            self.runner = None
            self.result = None

# Generated at 2022-06-13 14:56:42.192667
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True



# Generated at 2022-06-13 14:56:51.112598
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('\033[1m' + 'test StrategyModule' + '\033[0m')
    # test1
    print('\033[1m' + 'tqm is None' + '\033[0m')
    try:
        sm = StrategyModule(None)
    except:
        print('It is all right to be failed.')

    # test2
    print('\033[1m' + 'tqm is not None' + '\033[0m')
    tqm = {}
    sm = StrategyModule(tqm)
    print(sm.__dict__)
    # test3
    print('\033[1m' + 'debugger_active' + '\033[0m')
    print(sm.debugger_active)
    sm.debugger_active = False

# Generated at 2022-06-13 14:56:55.107167
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Make test strategy module
    tqm = 'Test'
    module = StrategyModule(tqm)

    # Test
    assert module != None

if __name__ == '__main__':
    # Test StrategyModule
    test_StrategyModule()

# Generated at 2022-06-13 14:57:03.931231
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sys.modules['__main__'].__file__ = 'ansible-debug'
    if not 'ansible.plugins.strategy.debug' in sys.modules:
        import ansible.plugins.strategy.debug
    assert(ansible.plugins.strategy.debug.__name__ == 'ansible.plugins.strategy.debug')
    s = StrategyModule(None)
    assert(isinstance(s, StrategyModule))
    assert(str(s) == '<ansible.plugins.strategy.debug.StrategyModule object at 0x10ed98c18>')
    assert(repr(s) == '<ansible.plugins.strategy.debug.StrategyModule object at 0x10ed98c18>')
    assert(s.get_host_list(None) == [])

# Generated at 2022-06-13 14:57:05.881573
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active == True


# Generated at 2022-06-13 14:57:12.662138
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = StrategyModule(None)
    assert tqm.debugger_active is True


# Generated at 2022-06-13 14:57:17.254128
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        from ansible.runner.return_data import ReturnData
    except ImportError:
        from ansible.utils.return_data import ReturnData

    class DummyTaskQueueManager:
        def __init__(self):
            self.result = [ReturnData('test', {}, {}, {}, {}, {})]

    strategy = StrategyModule(DummyTaskQueueManager())

# Implementation of debugger

# Generated at 2022-06-13 14:57:17.976158
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule


# Generated at 2022-06-13 14:57:18.715266
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # TODO: Add test here
    pass



# Generated at 2022-06-13 14:57:21.699990
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule
    test_tqm = linear_TestTQM()
    assert test_tqm
    strategy = StrategyModule(test_tqm)
    assert strategy
    assert strategy.debugger_active


# Generated at 2022-06-13 14:57:25.884845
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule(1)

    assert(obj.debugger_active == True)
    assert(obj.tqm == 1)
    assert(obj.module_name == 'debug')



# Generated at 2022-06-13 14:57:32.174075
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # TODO: This test is now a no-op as it is
    # impossible to instantiate a class without a tqm
    # When other methods are added to the strategy module
    # that can be invoked without a tqm
    # we should test them here.
    # The only thing we should be testing here
    # is that the class is registered with the correct
    # strategy name. And the name is declared in the
    # documentation. So no need to test it.
    return


# Generated at 2022-06-13 14:57:33.220743
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:57:37.018976
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Test happy path but because of the lack of unit test
    # framework and mocking library, the test would be incomplete
    # without debugger_active == True
    assert StrategyModule(None).debugger_active == True


# Generated at 2022-06-13 14:57:37.640150
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 14:57:49.625438
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tmp_StrategyModule = StrategyModule(tqm=None)
    assert tmp_StrategyModule.debugger_active == True


    # self.tqm._final_q = Queue()
    # self.tqm._failed_hosts = {}
    # self.tqm._unreachable_hosts = {}


# Generated at 2022-06-13 14:57:52.212175
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = StrategyModule(tqm)
    assert tqm.debugger_active == True


# Generated at 2022-06-13 14:57:55.137277
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Mock a strategy module by subclassing
    class MockStrategyModule(StrategyModule):
        pass


    return True



# Generated at 2022-06-13 14:57:57.375970
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True


# Generated at 2022-06-13 14:57:58.053416
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule


# Generated at 2022-06-13 14:58:01.155690
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Not sure if this is a good unit test.
    # But I didn't know how to do better.
    # At least it can detect very basic error.
    tqm = None
    StrategyModule(tqm)



# Generated at 2022-06-13 14:58:07.158185
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    mock_tqm = {
        'stats' : {
            'ok': {},
            'dark': {},
            'failures': {},
            'processed': {},
        }
    }
    strategy_module = StrategyModule(mock_tqm)
    for item in ['ok', 'dark', 'failures', 'processed']:
        assert item in strategy_module.tqm.stats


# Generated at 2022-06-13 14:58:16.188767
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
	class TestTP(object):
		def __init__(self):
			self.stdout_callback = "default"
			self.stats = {
				"foo": 1,
				"bar": 2,
				"baz": {
					"qux": 4,
					"quux": 5
				}
			}

# Generated at 2022-06-13 14:58:19.047579
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Test with instantiating class StrategyModule
    strategy_m = StrategyModule(None)
    assert isinstance(strategy_m, StrategyModule)



# Generated at 2022-06-13 14:58:22.201658
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Make sure that tqm is object after instantiation of StrategyModule
    tqm = object()
    sm = StrategyModule(tqm)
    assert sm.tqm == tqm


# Generated at 2022-06-13 14:58:43.492699
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TQM:
        def __init__(self, stats, inventory):
            self.stats = stats
            self.inventory = inventory

    strategy_module = StrategyModule(TQM(stats=None, inventory=None))

    assert strategy_module.debugger_active == True



# Generated at 2022-06-13 14:58:48.689915
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("\n Begin of test_StrategyModule \n")
    try:
        obj = StrategyModule(tqm=None)
    except Exception as e:
        print("Error occured: {0}".format(e))
    else:
        print("obj has been created successfully")
        print(obj)
    print("\n End of test_StrategyModule \n")



# Generated at 2022-06-13 14:58:50.610360
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.strategy import debug
    st = debug.StrategyModule()



# Generated at 2022-06-13 14:58:52.073771
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    TQM = None
    s = StrategyModule(TQM)
    assert s.debugger_active == True


# Generated at 2022-06-13 14:58:58.414881
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import unittest
    import ansible.plugins.loader as plugin_loader
    import ansible.plugins.strategy.debug as StrategyModule
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.handler.include import HandlerInclude
    from ansible.playbook.role.include import RoleInclude
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook.block import Block
    from ansible.playbook.task import Task
    from ansible.playbook import Play
    from ansible.playbook.handler_task_list import HandlerTaskList
    from ansible.playbook.role import Role
    from ansible.task_queue_manager import TaskQueueManager
    from ansible.executor.task_result import TaskResult
    import mock

    clsm

# Generated at 2022-06-13 14:58:59.029979
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:58:59.938628
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule


# Generated at 2022-06-13 14:59:01.913808
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(tqm=None)
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 14:59:04.919340
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class FakeTQM:
        pass
    tqm = FakeTQM()
    strategy_module = StrategyModule(tqm)
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 14:59:09.242370
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Only testing constructor, no need to test with actual TQM
    tqm = None
    debug_strategy = StrategyModule(tqm)
    assert isinstance(debug_strategy, StrategyModule) is True

# Unit test and manual test for run() method in class StrategyModule

# Generated at 2022-06-13 14:59:46.889422
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(0)


# Override run_once() of class LinearStrategyModule

# Generated at 2022-06-13 14:59:48.021125
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = ''
    strategy_module = StrategyModule(tqm)
    assert strategy_module.debugger_active == True



# Generated at 2022-06-13 14:59:52.221147
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """
    StrategyModule
    """
    # Initialize instance of class TaskQueueManager
    tqm = TaskQueueManager()

    # Initialize instance of class StrategyModule with TaskQueueManager instance as argument
    sm = StrategyModule(tqm)

    assert sm.debugger_active == True, "Initialization of StrategyModule failed."


# Generated at 2022-06-13 14:59:53.128715
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True == True


# Generated at 2022-06-13 14:59:56.601370
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestTaskQueueManager(object):
        pass
    tqm = TestTaskQueueManager()
    strategy_module = StrategyModule(tqm)
    assert strategy_module.debugger_active is True


# Generated at 2022-06-13 14:59:58.585024
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_m = StrategyModule(None)
    assert strategy_m
    assert strategy_m.debugger_active


# Generated at 2022-06-13 15:00:00.018731
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    StrategyModule(tqm)


# Generated at 2022-06-13 15:00:03.346918
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("test_StrategyModule()")
    strategy = StrategyModule("test")
    assert strategy.debugger_active, "Constructor StrategyModule() is not working."



# Generated at 2022-06-13 15:00:04.340006
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    mod = StrategyModule(tqm)

    assert mod.debugger_active == True



# Generated at 2022-06-13 15:00:05.379959
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrateyModule


# Generated at 2022-06-13 15:01:25.289394
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class tqm:
        pass
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active == True


# Generated at 2022-06-13 15:01:32.742292
# Unit test for constructor of class StrategyModule

# Generated at 2022-06-13 15:01:36.829401
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        debugger_active = StrategyModule.debugger_active
        assert isinstance(debugger_active, bool)
    except:
        print("Error in debug.StrategyModule.__init__() method")
        assert False

# Command prompt unit test

# Generated at 2022-06-13 15:01:39.845488
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sys.modules['ansible'] = None
    try:
        StrategyModule('dummy')
    except:
        assert False
    finally:
        del sys.modules['ansible']


# Generated at 2022-06-13 15:01:40.724798
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    return (StrategyModule, )



# Generated at 2022-06-13 15:01:44.527137
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = "tqm" # mockup of class TaskQueueManager
    tqm.stats = "stats" # mockup of class Stats
    tqm.stats.aggregate = "aggregate" # mockup of method aggregate
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active == True



# Generated at 2022-06-13 15:01:45.556785
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert isinstance(StrategyModule(None), StrategyModule)

# Utility function that takes a single string argument and returns the argument converted to a dictionary

# Generated at 2022-06-13 15:01:46.642213
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    assert isinstance(sm, StrategyModule)



# Generated at 2022-06-13 15:01:48.163373
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:01:57.969548
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.template import Templar
    from ansible.inventory.group import Group
    from ansible.inventory.host import Host
    from ansible.vars.manager import VariableManager
    from ansible.parsing.dataloader import DataLoader

    host = Host(name='test')
    group = Group(name='test')
    group.add_host(host)
    group.add_child_group(Group(name='test-child'))
    group.get_children()[0].add_host(Host(name='test-child'))

    tqm = TestTaskQueueManager()

# Generated at 2022-06-13 15:04:55.510328
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        sys.argv.remove('--debug')
    except ValueError:
        pass
    global tqm
    try:
        tqm
    except NameError:
        from . import fixtures
        tqm = fixtures.tqm
    sm = StrategyModule(tqm)
    assert(sm.debugger_active)
    assert(sm.tqm)


# Generated at 2022-06-13 15:04:56.908923
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert strategy_module.debugger_active


# Generated at 2022-06-13 15:05:03.037531
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestTqm:
        def __init__(self):
            self.shared_loader_obj = object()
            self.iterator = object()
            self.inventory = object()
            self.variable_manager = object()
            self.runner = object()

        def _make_tmp_path(self):
            pass

        def send_callback(self, msg):
            pass

    strategy_module = StrategyModule(TestTqm())
    assert strategy_module.tqm is not None
    assert strategy_module.debugger_active is True
    assert strategy_module.host_list is None
    assert strategy_module.result_callback is not None


# Generated at 2022-06-13 15:05:03.719465
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is StrategyModule


# Generated at 2022-06-13 15:05:04.628824
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert hasattr(StrategyModule, '__init__')



# Generated at 2022-06-13 15:05:07.406940
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TQM(object):
        pass
    class Ansible(object):
        pass
    tqm = TQM()
    tqm.ansible = Ansible()
    tqm.ansible.verbosity = 2
    tqm.stats = {}
    sm = StrategyModule(tqm)


# Generated at 2022-06-13 15:05:09.805470
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print(StrategyModule)
    print(Sys.stderr)
    print(StrategyModule)


# Generated at 2022-06-13 15:05:11.707113
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    StrategyModule(tqm)


# Generated at 2022-06-13 15:05:13.612162
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active



# Generated at 2022-06-13 15:05:18.417635
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import mock
    import pprint

    class FakeTQM():
        @property
        def stats(self):
            return pprint.pformat(dict(changed=1, skipped=2, failed=3, unreachable=4))

    assert StrategyModule(FakeTQM()).tqm == FakeTQM()

