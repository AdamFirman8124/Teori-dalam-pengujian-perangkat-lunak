

# Generated at 2022-06-13 14:55:29.986878
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    s = StrategyModule(tqm)
    assert isinstance(s, StrategyModule)


#==============================================================================
#    Debugger main class
#==============================================================================


# Generated at 2022-06-13 14:55:31.548804
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = DummyTQM()
    strategy = StrategyModule(tqm)


# Generated at 2022-06-13 14:55:34.022330
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategyModuleObject = StrategyModule("tqm")
    assert True == strategyModuleObject.debugger_active


if __name__ == '__main__':
    test_StrategyModule()
    print('All tests passed')

# Generated at 2022-06-13 14:55:36.036331
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_tqm = "Test"
    strategy_module = StrategyModule(test_tqm)
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 14:55:41.813892
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = {'tasks': ['tasks'],
           'results_callback': 'results_callback'}
    strategy = StrategyModule(tqm)

    assert strategy.tqm == tqm
    assert strategy.tqm['tasks'] == tqm['tasks']
    assert strategy.tqm['results_callback'] == tqm['results_callback']
    assert strategy.debugger_active == True

# Test main method of class StrategyModule

# Generated at 2022-06-13 14:55:44.045233
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        # If it's OK, constructor don't raise any errors
        StrategyModule(None)
    except:
        assert False



# Generated at 2022-06-13 14:55:46.410244
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule


# --------
# unit tests for class Cmd

# class Cmd()

# Generated at 2022-06-13 14:55:47.481891
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    return True


# Generated at 2022-06-13 14:55:51.106870
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    strategy = StrategyModule(tqm)
    assert strategy.tqm == tqm
    assert strategy.debugger_active is True
    assert strategy.host_result_map == {}



# Generated at 2022-06-13 14:55:58.502317
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.executor.task_queue_manager
    from ansible.vars.unsafe_proxy import UnsafeProxy

    tqm = ansible.executor.task_queue_manager.TaskQueueManager(
        hosts = UnsafeProxy({}),
        inventory = mock.Mock(),
        variable_manager = mock.Mock(),
        loader = mock.Mock(),
        options = mock.Mock(),
        passwords = mock.Mock(),
        stdout_callback = mock.Mock()
    )

    StrategyModule(tqm)



# Generated at 2022-06-13 14:56:02.853595
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Python 2.6 doesn't have mock module.
    import sys
    if sys.version_info < (2, 7):
        return
    from mock import Mock
    tqm = Mock()
    StrategyModule(tqm)



# Generated at 2022-06-13 14:56:05.777791
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class Tqm:
        pass

    tqm = Tqm()
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active


# Generated at 2022-06-13 14:56:09.357525
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TQM():
        def __init__(self):
            self.name = 'tqm'
    tqm = TQM()
    assert StrategyModule(tqm).name == 'tqm'



# Generated at 2022-06-13 14:56:11.813070
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = []
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active == True


# Generated at 2022-06-13 14:56:12.717556
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    return StrategyModule


# Generated at 2022-06-13 14:56:13.618624
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True == False


# Generated at 2022-06-13 14:56:14.102325
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True



# Generated at 2022-06-13 14:56:15.859828
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__doc__ is not None

if __name__ == '__main__':
    sys.exit(test_StrategyModule())

# Generated at 2022-06-13 14:56:18.113559
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 1
    expected_result = True
    actual_result = StrategyModule(tqm).debugger_active
    assert expected_result == actual_result


# Generated at 2022-06-13 14:56:20.586969
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = ansible.runner.AnsibleRunner(host_list=["host1"])
    sm = StrategyModule(tqm)
    assert sm.debugger_active


# Generated at 2022-06-13 14:56:34.447797
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.block import Block
    from ansible.playbook import role
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.play_iterator import PlayIterator
    from ansible.inventory.manager import InventoryManager

    p = Play()
    p.name = 'debug test play'
    p.hosts = 'all'
    p.tasks = [
        Task(),
        Task(),
        Task(),
        Task(),
        Task()
    ]
    p.tasks[0].name = 'task0'
    p.tasks[1].name = 'task1'
    p.tasks[2].name = 'task2'
    p.tasks

# Generated at 2022-06-13 14:56:36.438771
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = "tqm"
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True


# Generated at 2022-06-13 14:56:42.357606
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    TASK1 = {'debugger': 'A'}
    TASK2 = {'debugger': 'B'}
    HOSTS = ['foo.bar.com']
    module = StrategyModule(TASK1, TASK2, HOSTS)
    assert module.debugger_active is True

# Generated at 2022-06-13 14:56:42.915568
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 14:56:49.606485
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Preparation
    class AnsibleStrategyModule_none(StrategyModule):
        def __init__(self, tqm):
            StrategyModule.__init__(self, tqm)
    class AnsibleStrategyModule_any(StrategyModule):
        def __init__(self, tqm):
            StrategyModule.__init__(self, tqm)

    # Test
    assert isinstance(AnsibleStrategyModule_none(), StrategyModule)
    assert isinstance(AnsibleStrategyModule_any(), StrategyModule)



# Generated at 2022-06-13 14:56:52.222970
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    assert sm.debugger_active



# Generated at 2022-06-13 14:56:55.109260
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert type(strategy_module) == StrategyModule
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 14:56:59.883166
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class A:
        def __init__(self, b, c=[]):
            self.b = b
            self.c = c
        def __add__(self, other):
            other.c.append(self.b)
            return other

    tm = A('tm')
    sm = StrategyModule(tm)
    assert(sm.debugger_active)


# Generated at 2022-06-13 14:57:01.010552
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    st = StrategyModule(None)
    assert st.debugger_active == True
    assert st.tqm == None

# Generated at 2022-06-13 14:57:02.357261
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    task_queue_manager = 'task_queue_manager'
    StrategyModule(task_queue_manager)



# Generated at 2022-06-13 14:57:08.622474
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    my_obj = StrategyModule(None)
    assert my_obj.debugger_active

TASK_SECTION = None
STEP = False



# Generated at 2022-06-13 14:57:11.753028
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = LinearStrategyModule(tqm=True)
    assert strategy.debugger_active == True


# Generated at 2022-06-13 14:57:13.573816
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True


# Generated at 2022-06-13 14:57:16.010775
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = mock.MagicMock()
    strategy_module = StrategyModule(tqm)
    strategy_module.debugger_active = True
# End of unit test for constructor of class StrategyModule


# Generated at 2022-06-13 14:57:17.273634
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert(StrategyModule.__doc__ is StrategyModule.__init__.__doc__)


# Generated at 2022-06-13 14:57:17.724074
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:57:19.741997
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = TqmFake()
    strategy_module = StrategyModule(tqm)
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 14:57:21.971151
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'test'
    strategy_module = StrategyModule(tqm)
    assert strategy_module.tqm == 'test'



# Generated at 2022-06-13 14:57:27.735550
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Create object
    tqm = type('FakeTqm', (), dict(stats=type('FakeStats', (), dict(increment=lambda s, id: True)))())
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True
    assert isinstance(sm, LinearStrategyModule)



# Generated at 2022-06-13 14:57:30.433869
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = TQM(inventory=None, loader=None, options=None, passwords=None, stdout_callback=None)
    strategy = StrategyModule(tqm)



# Generated at 2022-06-13 14:57:48.562908
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test = StrategyModule(None)
    assert test.debugger_active is True

# class Debugger(cmd.Cmd):

#     def __init__(self, strategy):
#         cmd.Cmd.__init__(self)
#         self.strategy = strategy
#         self.saved_stdout = sys.stdout
#         self.saved_stderr = sys.stderr
#         sys.stdout = self.stdout
#         sys.stderr = self.stderr
#         self.prompt = ' > '

#     def stdout(self, data):
#         sys.__stdout__.write(data)

#     def stderr(self, data):
#         sys.__stderr__.write(data)

#     def emptyline(self):


# Generated at 2022-06-13 14:57:53.857087
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    # Create Dummy TaskQueueManager
    tqm = DummyTaskQueueManager()

    # Test constructor
    obj = StrategyModule(tqm)
    assert obj.tqm == tqm
    assert obj.debugger_active == True

# TODO use unittest.mock

# Generated at 2022-06-13 14:57:58.287122
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class FakeTQM:
        def __init__(self):
            self.runners = {}

    tqm = FakeTQM()

    strategy = StrategyModule(tqm)

    assert isinstance(strategy, LinearStrategyModule)
    assert strategy.debugger_active


# Generated at 2022-06-13 14:58:00.107627
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Tests for constructor of class StrategyModule
    # Creating a mock taskQueueManager for that purpose
    return



# Generated at 2022-06-13 14:58:04.683806
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    #init the class
    s = StrategyModule(tqm=None)
    #test it
    assert s.debugger_active != None

# Unit test of execute
# Below code is not a unit test. It is only a way to verify that debugger indeed starts
# To actually test execute, use debugger_test plugin

# Generated at 2022-06-13 14:58:14.546967
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    host = "test"
    port = 2222
    user = "root"
    passwd = "root"

    tqm = Ansible()
    tqm._sshpass = passwd
    tqm._connection_info = dict(
        host=host, port=port, user=user, passwd=passwd
    )
    tqm._extra_vars = dict(
        ansible_ssh_pass=passwd,
        ansible_ssh_port=port,
        ansible_ssh_user=user,
        ansible_ssh_host=host,
        ansible_connection='local'
    )

    s = StrategyModule(tqm)
    assert s._tqm == tqm
    assert s.debugger_active
    assert s._inventory == tqm.get_inventory()

# Generated at 2022-06-13 14:58:15.589010
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(1)



# Generated at 2022-06-13 14:58:22.814191
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Note: In order to run unit tests, you need to add the following line in ./test/sanity/code-smell/test_code_smell.py
    # directory = os.path.join(os.environ['TEST_DIR'], 'unit/plugins/strategies')
    import ansible.plugins.strategy.debug
    sm = ansible.plugins.strategy.debug.StrategyModule(None)
    assert sm.debugger_active == True


# Generated at 2022-06-13 14:58:26.677852
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('Testing __init__()...')
    x = StrategyModule(None)
    assert x.tqm == None, \
        'FAIL: tqm should be None'
    assert x.debugger_active == True, \
        'FAIL: debugger_active should be True'
    print('PASSED')


# Generated at 2022-06-13 14:58:27.469329
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True



# Generated at 2022-06-13 14:58:44.404278
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 14:58:48.261822
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    if len(sys.argv) > 1 and sys.argv[1] == '-u': # unit test
        strategy_module = StrategyModule(None)
        assert(strategy_module.debugger_active == True)

# Overrides run() method of class StrategyModule

# Generated at 2022-06-13 14:58:58.812030
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class Options:
        run_once = False
    class TQM:
        options = Options()
        inventory = None
        loader = None
        variable_manager = None
        stdout_callback = None
        callback_loader = None
        passwords = None
        stats = None
        stdout_callback = None
    tqm = TQM()
    strategy_module = StrategyModule(tqm)
    assert strategy_module.debugger_active == True
    assert strategy_module.tqm == tqm

# In the main method, StrategyModule will be executed. 
# If the code does not throw any exception, then StrategyModule is executed normally.
if __name__ == '__main__':
    test_StrategyModule()

# If this code is executed as a file, then a debug session will be activated.
# The

# Generated at 2022-06-13 14:59:00.520664
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy = StrategyModule(tqm)
    return strategy


# Generated at 2022-06-13 14:59:07.932441
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import sys
    import os
    import mock
    from ansible.plugins.strategy import debug

    try:
        table = os.path.dirname(os.path.dirname(sys.argv[0]))
    except IndexError:
        table = None


# Generated at 2022-06-13 14:59:08.901388
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert False


# Generated at 2022-06-13 14:59:16.485550
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("\nUNIT TEST: test_StrategyModule()")
    # Create temp LinearStrategyModule (super class) to test on
    tqm = LinearStrategyModule("/some/path/ansible/inventory.py")
    # Create instance of StrategyModule class to test on
    m = StrategyModule(str(tqm))

    print("Testing StrategyModule constructor")
    # Test StrategyModule.debugger_active
    if not (hasattr(m, 'debugger_active') and isinstance(m.debugger_active, bool)):
        print("    ! Did not get bool in StrategyModule.debugger_active")
        sys.exit(1)
    elif not m.debugger_active:
        print("    ! Debugger is not active")
        sys.exit(1)

# Generated at 2022-06-13 14:59:19.508097
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Test constructor
    task_queue_manager = None
    strategy_module = StrategyModule(task_queue_manager)
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 14:59:20.561864
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None


# Generated at 2022-06-13 14:59:21.339211
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    return


# Generated at 2022-06-13 14:59:58.212534
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import mock
    import ansible.plugins.strategy.debug

    assert ansible.plugins.strategy.debug.StrategyModule\
        (mock.Mock()) is not None



# Generated at 2022-06-13 15:00:03.089356
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class tqm:
        def __init__(self):
            self.stats = {}
    tqm = tqm()
    strategy = StrategyModule(tqm)
    assert isinstance(strategy, LinearStrategyModule)
    assert strategy.debugger_active



# Generated at 2022-06-13 15:00:09.375007
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TestTQM(object):
        def __init__(self):
            self.initial_task_block = None
            self.inventory = None
    tqm = TestTQM()
    sm = StrategyModule(tqm)

    assert sm.debugger_active is True, "Debugger value is not True"
    assert isinstance(sm, LinearStrategyModule), "Declared class is not a subclass of LinearStrategyModule"

test_StrategyModule()



# Generated at 2022-06-13 15:00:10.470957
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None)



# Generated at 2022-06-13 15:00:11.504364
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    module = StrategyModule()
    assert module.debugger_active


# Generated at 2022-06-13 15:00:14.787197
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    strategy = StrategyModule(tqm)
    assert strategy.tqm == tqm
    assert strategy.debugger_active
# End of test_StrategyModule



# Generated at 2022-06-13 15:00:18.048487
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TaskQueueManager:
        pass

    tqm = TaskQueueManager()
    strategy_module = StrategyModule(tqm)

    assert strategy_module.debugger_active is True


# Generated at 2022-06-13 15:00:29.947700
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    global debugger_active
    debugger_active = False

# Generated at 2022-06-13 15:00:31.305367
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert issubclass(StrategyModule, Stageable) and issubclass(StrategyModule, LinearStrategyModule)


# Generated at 2022-06-13 15:00:33.284588
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager(host_list=[])
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active is True


# Generated at 2022-06-13 15:01:52.690240
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:01:54.956415
# Unit test for constructor of class StrategyModule

# Generated at 2022-06-13 15:01:56.080634
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("---- test_StrategyModule ----")
    tqm = None
    obj = StrategyModule(tqm)
    assert obj.debugger_active == True


# Generated at 2022-06-13 15:02:02.675379
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = dict()
    for i in range(10):
        tqm[i] = i
    lsm = StrategyModule(tqm)
    assert lsm.debugger_active
    assert lsm._tqm == tqm

if __name__ == "__main__":
    test_StrategyModule()



# Generated at 2022-06-13 15:02:05.785442
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # pass in test values for 'tqm' parameter for constructor of class StrategyModule
    strategy_module_instance = StrategyModule("tqm")
    # if 'debugger_active' attribute is True, it means constructor of class StrategyModule works as expected
    assert strategy_module_instance.debugger_active is True


# Generated at 2022-06-13 15:02:12.960691
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.playbook import PlayBook
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.inventory import Inventory
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.inventory.ini import InventoryParser

    pb = PlayBook(callbacks=None)
    play = Play.load(dict(
        name="Ansible Debug Play",
        hosts=None,
        gather_facts='no',
        tasks=[],
    ), variable_manager=pb._variable_manager, loader=pb._loader)
    pb._plays.append(play)

    host = Host(name='host')
    group = Group(name='group')
    group.add_host(host)

# Generated at 2022-06-13 15:02:17.355007
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = "tqm"
    strategy_module = StrategyModule(tqm)
    assert strategy_module.result_q is not None
    assert strategy_module.out_q is not None
    assert strategy_module.tqm is not None
    assert strategy_module.debugger_active is True



# Generated at 2022-06-13 15:02:18.516948
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  print("Test - Strategy Module")
  return StrategyModule


# Generated at 2022-06-13 15:02:20.255930
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(tqm)
    assert strategy_module != None


# Generated at 2022-06-13 15:02:22.613700
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = True
    str_obj = StrategyModule(tqm)
    assert isinstance(str_obj, LinearStrategyModule)


# Generated at 2022-06-13 15:05:19.909218
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass
    #print("IN test_StrategyModule")

    #tqm = None
    #strategy_module = StrategyModule(tqm)
    #assert()


# Generated at 2022-06-13 15:05:26.949096
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TaskQueueManager:
        def __init__(self):
            self.hostvars = {'host1': {'ansible_host': '127.0.0.1'}}

    try:
        strategy = StrategyModule(TaskQueueManager())
        print('==== StrategyModule ===')
        pprint.pprint(vars(strategy))
        print('=======================')
        print('                    PASS')
        print('=======================')
    except Exception as e:
        print('=======================')
        print('                    FAIL')
        print('=======================')
        print(e)
