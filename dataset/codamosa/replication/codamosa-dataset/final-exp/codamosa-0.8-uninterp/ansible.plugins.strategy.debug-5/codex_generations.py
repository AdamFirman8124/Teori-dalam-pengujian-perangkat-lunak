

# Generated at 2022-06-13 14:55:34.808872
# Unit test for constructor of class StrategyModule

# Generated at 2022-06-13 14:55:37.004917
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    ob = StrategyModule()
    if ob.debugger_active is True:
        print('successful')
    else:
        print('failed')

test_StrategyModule()


# Generated at 2022-06-13 14:55:37.848719
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule()

# Generated at 2022-06-13 14:55:39.531858
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(None)
    assert strategy.debugger_active == True


# Generated at 2022-06-13 14:55:40.265411
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

    # s = StrategyModule()



# Generated at 2022-06-13 14:55:48.263670
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TQM(object):
        def __init__(self):
            self.stdout_callback = "minimal"
            self.options = Options()
    class Options(object):
        def __init__(self):
            self.module_path = ""

    tqm = TQM()
    sm = StrategyModule(tqm)
    print(sm.stdout_callback)
    print(sm.debugger_active)
    print(sm.tqm.stdout_callback)
    print(sm.tqm.options.module_path)


# Generated at 2022-06-13 14:55:50.592883
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = True
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active


# Generated at 2022-06-13 14:55:50.915249
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True



# Generated at 2022-06-13 14:55:53.279472
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("*** Test if StrategyModule constructor is working fine ***")
    class TestStrategyModule(StrategyModule):
        def run(self, iterator, connection_info, resultCallback):
            return super(StrategyModule, self).run(iterator, connection_info, resultCallback)

    task_queue_manager = {}
    strategy = TestStrategyModule(task_queue_manager)
    assert strategy.name == 'debug'
    assert strategy.debugger_active



# Generated at 2022-06-13 14:55:54.244950
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(tqm=None)



# Generated at 2022-06-13 14:56:04.802299
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import ansible.plugins.strategy
    import ansible.playbook.task

    # test object
    tqm = ansible.plugins.strategy.TaskQueueManager()

    task = ansible.playbook.task.Task()
    tqm._final_q.put(task)

    strategy_module = StrategyModule(tqm=tqm)

    print(strategy_module._tqm)
    assert strategy_module._tqm == tqm, "TaskQueueManager has not been stored."

    assert len(strategy_module._failed_hosts) == 0, "Hosts are not empty."
    assert strategy_module._iterator == tqm._iterator, "Iterator has not been stored."
    assert strategy_module._final_q == tqm._final_q, "Final queue has not been stored."


# Generated at 2022-06-13 14:56:05.870927
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('hello')



# Generated at 2022-06-13 14:56:06.904554
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule("test")


# Generated at 2022-06-13 14:56:07.396259
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule

# Generated at 2022-06-13 14:56:13.369787
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import unittest

    class test_StrategyModule(unittest.TestCase):
        def test_constructor(self):
            strategy = StrategyModule('defaults')
            self.assertTrue(strategy.debugger_active)

    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(test_StrategyModule))
    return test_suite



# Generated at 2022-06-13 14:56:14.568972
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(tqm=None) != None
    

# Generated at 2022-06-13 14:56:21.864618
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class _test_playbook:
        class _test_iterator:
            class _test_hosts:
                def __init__(self):
                    self.Host = dict()

                def all(self):
                    return []

            def __init__(self):
                self.hosts = _test_playbook._test_iterator._test_hosts()

        class _test_variable_manager:
            def set_host_variable(self, task, host, variable):
                pass

            def set_nonpersistent_facts(self, task, host, variable):
                pass
            def set_task_facts(self, task, variable, templar=None, inject=None):
                pass


# Generated at 2022-06-13 14:56:23.794844
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
   sys.stdout = open(os.devnull, 'w')
   tqm = TaskQueueManager()
   strategy = StrategyModule(tqm)
   assert strategy.debugger_active is True

# Generated at 2022-06-13 14:56:30.110914
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_StrategyModule.task_max_count = 2
    test_StrategyModule.tqm = tqm = FakeTaskQueueManager()
    ansible.plugins.strategy.debug.StrategyModule(tqm)
    assert tqm.debugger_active == True

# Dummy TaskQueueManager for unit test
import mock

# Generated at 2022-06-13 14:56:38.786271
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    try:
        x = StrategyModule(tqm)
    except TypeError as err:
        assert type(err) == TypeError
    except Exception as err:
        assert False, "Unexpected exception raised: " + str(err)

#    def _run_debugger(self, task_vars):
#        my_vars = task_vars.copy()
#        my_vars.update(self._play_context.__dict__)
#        my_vars['self'] = self
#        my_vars['debugger'] = Debugger(my_vars)
#        code.interact("** Ansible Debugger ** ", local=my_vars)



# Generated at 2022-06-13 14:56:48.442574
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        # Python2
        import Queue as queue
    except ImportError:
        # Python3
        import queue as queue
    try:
        # Python2
        import __builtin__ as builtins
    except ImportError:
        # Python3
        import builtins as builtins
    class MyTqm(object):
        def __init__(self):
            self.hostvars = {}
            self.taskqueue = queue.Queue()
            self.notified_handlers = {}

    m = MyTqm()
    sm = StrategyModule(m)
    assert isinstance(sm, LinearStrategyModule)



# Generated at 2022-06-13 14:56:50.146212
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = AnsibleUnittest.mock_tqm_ansible_playbook()
    strategy = StrategyModule(tqm)
    assert isinstance(strategy, StrategyModule)
    assert strategy.tqm == tqm
    assert strategy.debugger_active



# Generated at 2022-06-13 14:56:54.721143
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    mock_task_queue_manager = 'foo'
    sm = StrategyModule(mock_task_queue_manager)
    assert(sm.debugger_active)
    assert(sm._tqm == mock_task_queue_manager)


# Generated at 2022-06-13 14:56:55.310591
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

# Generated at 2022-06-13 14:56:57.662281
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class tqm:
        def __init__(self):
            self.hostvars = dict()
    tqm.__name__ = 'tqm'
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active == True

# Generated at 2022-06-13 14:57:00.209887
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class DummyTqm():
        def __init__(self):
            self.logger = None
            pass
    tqm = DummyTqm()
    sm = StrategyModule(tqm)
    assert sm.__class__.__name__ == "StrategyModule"


# Generated at 2022-06-13 14:57:02.498669
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import __builtin__ as builtins
    import mock

    mock_tqm = mock.MagicMock()
    with mock.patch.object(builtins, 'print'):
        StrategyModule(mock_tqm)



# Generated at 2022-06-13 14:57:05.966762
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('Testing StrategyModule constructor')
    try:
        tqm = None
        strategy_module = StrategyModule(tqm)
    except:
        print('StrategyModule constructor test failed')
        return False
    else:
        print('StrategyModule constructor test passed')
        return True


# Generated at 2022-06-13 14:57:12.047184
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print(StrategyModule.__module__)
    print(StrategyModule.__name__)
    print(StrategyModule.__doc__)
    print(Globals.__module__)
    print(Globals.__name__)
    print(Globals.__doc__)

#Unit test for class Debugger

# Generated at 2022-06-13 14:57:12.662924
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 14:57:17.031138
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    assert sm.debugger_active


# Generated at 2022-06-13 14:57:17.722850
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(None)



# Generated at 2022-06-13 14:57:18.111753
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule()

# Generated at 2022-06-13 14:57:20.212612
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class Dummy:
        pass
    tqm = Dummy()
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True



# Generated at 2022-06-13 14:57:21.168335
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:57:22.014087
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    #TODO
    pass

# Generated at 2022-06-13 14:57:32.820387
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = MagicMock()
    strategy_module = StrategyModule(tqm)

    assert strategy_module.debugger_active
    assert strategy_module.runners is None
    assert strategy_module.inventory is None
    assert strategy_module.variable_manager is None
    assert strategy_module.loader is None
    assert strategy_module.play is None
    assert strategy_module.tqm is tqm
    assert strategy_module.stdout_callback is None
    assert strategy_module.action_loader is None
    assert strategy_module.shared_loader_obj is None
    assert strategy_module.host_result_callback is None
    assert strategy_module.task_result_callback is None
    assert strategy_module.options is None
    assert strategy_module.callback is None


# Generated at 2022-06-13 14:57:33.854340
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None)

# Generated at 2022-06-13 14:57:40.659261
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class tqm:
        def __init__(self):
            self.stats = dict()
    s = StrategyModule(tqm())
    assert s.name == 'debug'
    assert s.current_task_name == ''
    assert s.current_task_num == 0
    assert s.incorrect_task_vars == dict()
    assert s.total_tasks == 0
    assert s.debugger_active == True


# Generated at 2022-06-13 14:57:43.878991
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('Test for constructor of class StrategyModule to make sure it is instantiated correctly')
    s = StrategyModule(None)
    print(s.loop_args)


# Generated at 2022-06-13 14:57:54.055671
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tm = StrategyModule(None)
    assert tm.debugger_active == True

    print(1)


# Generated at 2022-06-13 14:58:02.188496
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class Test_TaskQueueManager:
        def __init__(self):
            self.hostvars = {'host1': {'debug_result': 'debug_result_host1', 'debug_vars': 'debug_vars_host1'}}
    tqm = Test_TaskQueueManager()
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True
    assert sm.tqm.hostvars['host1']['debug_result'] == 'debug_result_host1'
    assert sm.tqm.hostvars['host1']['debug_vars'] == 'debug_vars_host1'


# Generated at 2022-06-13 14:58:06.753100
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_tqm = ''
    test_result = StrategyModule(test_tqm)
    actual_result = '<ansible.plugins.strategy.debug.StrategyModule object at 0x7f33dee17f98>'
    assert str(test_result) == actual_result


# Generated at 2022-06-13 14:58:13.750361
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    adhoc = AdHoc('localhost', 'local', '/etc/ansible/hosts')
    adhoc.options.module_path = 'tests/'
    adhoc.run()

# TODO:
# * Add defalut task name
# * When debugger is not active, run all tasks
# * Modify to use ANSIBLE_HOST_KEY_CHECKING env
# * search() should print line number of tasks
# * Invoke play.set_context()
# * Invoke play.set_defaults()


# Generated at 2022-06-13 14:58:14.474437
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:58:19.047747
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule(tqm = None)
    assert obj.__class__.__name__ == "StrategyModule"
    assert isinstance(obj, object)
    assert obj.tqm == None
    assert obj.debugger_active == True



# Generated at 2022-06-13 14:58:23.196514
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    '''
    Unit test for constructor of class StrategyModule
    '''
    sys.modules['ansible'].plugins.strategy.linear.LinearStrategyModule = LinearStrategyModule

    sm = StrategyModule({})
    assert sm.debugger_active == True


# Generated at 2022-06-13 14:58:28.101540
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Simple test to break any code it sees
    # Good test if you use coverage
    from ansible_debug_unit_test import StrategyModule
    import ansible_debug_unit_test
    print(ansible_debug_unit_test)
    x = StrategyModule('tqm')
    assert(x.tqm == 'tqm')
    assert(x.debugger_active)
    assert(type(x.tqm) == str)


# Generated at 2022-06-13 14:58:29.902423
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    s = StrategyModule(tqm)
    assert s.tqm == tqm
    assert s.runner_type == 'debug'



# Generated at 2022-06-13 14:58:31.192990
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert self.debugger_active == True


# Generated at 2022-06-13 14:58:48.647743
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    return
    '{0}()'.format(StrategyModule.__name__)


# Generated at 2022-06-13 14:58:51.460989
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print('class StrategyModule __init__(tqm):')
    print('class StrategyModule(LinearStrategyModule):')

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 14:58:52.488240
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    result = StrategyModule(None)
    assert result.debugger_active is True


# Generated at 2022-06-13 14:58:56.020449
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        tqm = TaskQueueManager(None, None)
        strategy = StrategyModule(tqm)
        assert strategy
    except Exception as e:
        print(e)
    finally:
        del strategy
        del tqm



# Generated at 2022-06-13 14:58:57.178791
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 14:59:00.701746
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    s = StrategyModule(None)
    assert 'StrategyModule' == s.__class__.__name__
    assert 'StrategyModule' == s.__class__.__bases__[0].__name__
    assert True == s.debugger_active



# Generated at 2022-06-13 14:59:02.268418
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # TODO: add test case
    pass

    # Unit test for method run() of class StrategyModule

# Generated at 2022-06-13 14:59:02.906402
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 14:59:04.966938
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert isinstance(StrategyModule(None), StrategyModule)
    assert isinstance(StrategyModule(None), LinearStrategyModule)


# Generated at 2022-06-13 14:59:05.780348
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:59:40.089440
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:59:42.574382
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active == True
    return strategy



# Generated at 2022-06-13 14:59:45.211728
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Testing StrategyModule")
    assert "StrategyModule" in str(StrategyModule)
    assert "tqm" in str(StrategyModule.__init__)



# Generated at 2022-06-13 14:59:54.461485
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__module__ == 'ansible.plugins.strategy.debug'
    assert StrategyModule.__doc__ == 'Executes tasks in interactive debug session.'
    assert hasattr(StrategyModule, '_display')
    assert hasattr(StrategyModule, '_play')
    assert hasattr(StrategyModule, '__init__')
    assert hasattr(StrategyModule, '_step')
    assert hasattr(StrategyModule, '_cleanup_step')
    assert hasattr(StrategyModule, '_wait_on_pending_results')
    assert hasattr(StrategyModule, 'add_tqm_variables')
    assert hasattr(StrategyModule, 'run_handlers')
    assert hasattr(StrategyModule, 'cleanup')


# Generated at 2022-06-13 14:59:56.453663
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        StrategyModule(None)
    except TypeError:
        return False
    return True



# Generated at 2022-06-13 15:00:07.546030
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class Tqm(object):
        def __init__(self, host_list):
            self.host_list = host_list

        def get_host_list(self):
            return self.host_list

    class Play(object):
        def __init__(self, tasks):
            self.tasks = tasks
            self.hosts = ["localhost"]

        def get_tasks(self, hosts=[]):
            return self.tasks

        def get_plays(self):
            return [self]

    class Task(object):
        def __init__(self, name, task_action):
            self.name = name
            self.task_action = task_action

        def get_name(self):
            return self.name

        def get_action(self):
            return self.task_action


# Generated at 2022-06-13 15:00:08.144314
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 15:00:08.628564
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass



# Generated at 2022-06-13 15:00:10.385601
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = {}
    strategy_module = StrategyModule(tqm)


# Generated at 2022-06-13 15:00:13.171734
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    assert(sm.debugger_active == True)

    sm.debugger_active = False
    assert(sm.debugger_active == False)



# Generated at 2022-06-13 15:01:28.671542
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # TBD
    assert(False)



# Generated at 2022-06-13 15:01:33.011865
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    sm = StrategyModule(tqm)

# TODO: Add unit test for added functions

    sm.debugger()
    print(sm.debugger.__doc__)

if __name__ == '__main__':
    test_StrategyModule()

# Generated at 2022-06-13 15:01:35.450852
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Unit test for constructor of class StrategyModule")
    print("TODO: Do it!")

# Main function

# Generated at 2022-06-13 15:01:44.753349
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.utils.display import Display
    from ansible.playbook.play import Play
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager

    display = Display()

# Generated at 2022-06-13 15:01:48.270085
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = "test"
    test1 = StrategyModule(tqm)
    assert test1.tqm == "test"
    
    

# Generated at 2022-06-13 15:01:51.390313
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # The following error is detected when the method is executed
    # and non-zero exit code is returned.
    # TypeError: super() takes at least 1 argument (0 given)
    StrategyModule(None)


# Generated at 2022-06-13 15:01:52.120735
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule, 'Class StrategyModule not found'


# Generated at 2022-06-13 15:01:53.285729
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True


# Generated at 2022-06-13 15:02:01.868392
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.plugins.loader import strategy_loader
    from ansible.playbook import PlayBook
    from ansible.inventory import Inventory
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.module_utils._text import to_bytes

    sys.argv = ['/usr/local/bin/ansible-playbook', '--ask-pass', '-i', 'hosts', '--extra-vars=@extra_vars.yml', '-k', 'playbook.yml']
    play = PlayBook.load(sys.argv[1:], variable_manager=None, loader=None)
    variable_manager = play.get_variable_manager()
    loader = play.get_loader()
    inventory = Inventory(loader, variable_manager, play.host_list)
    variable

# Generated at 2022-06-13 15:02:03.225817
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sm = StrategyModule(None)
    assert sm.debugger_active is True


# Generated at 2022-06-13 15:04:48.707670
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule


# Generated at 2022-06-13 15:04:49.679097
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass
#


# Generated at 2022-06-13 15:04:50.594444
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """Test if constructor of class StrategyModule works as expected."""
    assert StrategyModule is not None, 'returned StrategyModule is None'



# Generated at 2022-06-13 15:04:55.920983
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import mock
    import ansible.executor.task_queue_manager as tqm
    sm = StrategyModule(tqm.TaskQueueManager())
    assert sm.debugger_active == True

# end of Unit test for constructor of class StrategyModule

    def _send_task(self, task, task_vars):
        commands = self._get_commands(task, task_vars)
        return commands, task_vars



# Generated at 2022-06-13 15:04:56.408198
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 15:05:02.713068
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    debugger_active = True
    tqm = None
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active
    assert isinstance(strategy.tqm, object) == False
    assert isinstance(strategy.inventory, object)
    assert isinstance(strategy.variable_manager, object)
    assert isinstance(strategy.loader, object)
    assert isinstance(strategy.host_list, object)
    assert isinstance(strategy.all_vars, object)
    assert isinstance(strategy.hosts_remaining, object)
    assert isinstance(strategy.result_callback, object)


# Generated at 2022-06-13 15:05:08.232745
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class TQM():
        def __init__(self):
            self.____ = "TQM"

    class ActionBase():
        def __init__(self):
            self.____ = "ActionBase"

    class StrategyModule(ActionBase):
        def __init__(self, tqm):
            super(StrategyModule, self).__init__()

            self.____ = "StrategyModule"
            self.____TQM = tqm

    tqm = TQM()
    strategy = StrategyModule(tqm)

    assert hasattr(strategy, '____')
    assert hasattr(strategy, '____TQM')



# Generated at 2022-06-13 15:05:10.185794
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(tqm = 1)


# Generated at 2022-06-13 15:05:13.687009
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import os
    import sys
    TestClass = StrategyModule()
    TestClass.__init__()
    assert TestClass.__class__.__name__ == 'StrategyModule'



# Generated at 2022-06-13 15:05:14.559933
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert callable(StrategyModule)

