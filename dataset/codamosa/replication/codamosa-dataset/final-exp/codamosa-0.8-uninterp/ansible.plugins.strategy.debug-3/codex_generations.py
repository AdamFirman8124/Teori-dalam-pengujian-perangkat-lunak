

# Generated at 2022-06-13 14:55:25.102471
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None
    assert StrategyModule.__init__ is not None



# Generated at 2022-06-13 14:55:29.414321
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == "StrategyModule"
    assert len(StrategyModule.__bases__) == 1
    assert StrategyModule.__bases__[0].__name__ == "LinearStrategyModule"

    tqm = []
    StrategyModule(tqm)


# Generated at 2022-06-13 14:55:29.947385
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 14:55:33.089534
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    task_queue_manager = "task_q_m"

    debug_module = StrategyModule(task_queue_manager)

    assert debug_module.debugger_active == True
    assert debug_module.tqm == task_queue_manager


# Generated at 2022-06-13 14:55:33.944317
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None)


# Generated at 2022-06-13 14:55:40.787761
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.vars import VariableManager
    import ansible.inventory
    from ansible.parsing.dataloader import DataLoader
    from ansible.playbook.play import Play
    from ansible.vars.manager import VariableManager
    from ansible.executor.playbook_executor import PlaybookExecutor

    variable_manager = VariableManager()
    loader = DataLoader()
    variable_manager._extra_vars = dict()
    variable_manager._options_vars = dict()
    variable_manager._extra_vars['hostvars'] = dict()
    inv = ansible.inventory.Inventory(loader=loader, variable_manager=variable_manager,  host_list='/dev/null')
    variable_manager.set_inventory

# Generated at 2022-06-13 14:55:42.779396
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    cmd = StrategyModule(object)
    assert cmd.debugger_active == True

DEFAULT_PROMPT = 'ansible debugger> '


# Generated at 2022-06-13 14:55:43.881656
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert 'True' == str(StrategyModule())

# Generated at 2022-06-13 14:55:46.228269
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = {}
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active


# Generated at 2022-06-13 14:55:48.984224
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    '''Test for constructor of class StrategyModule'''
    debug_instance = StrategyModule(None)
    assert debug_instance.debugger_active

# Class for strategy debugger

# Generated at 2022-06-13 14:55:51.825611
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(None)
    assert strategy.debugger_active == True

# unit test for constructor

# Generated at 2022-06-13 14:55:54.674337
# Unit test for constructor of class StrategyModule
def test_StrategyModule():

    tqm = None
    s = StrategyModule(tqm)
    assert isinstance(s, StrategyModule)
    assert s.debugger_active



# Generated at 2022-06-13 14:55:56.837884
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import mock
    tqm = mock.Mock()
    sm = StrategyModule(tqm)
    assert sm.debugger_active is True


# Generated at 2022-06-13 14:56:00.479818
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class FakeTQM:
        def __init__(self):
            self.options = None

    strategy_module = StrategyModule(FakeTQM())
    assert strategy_module.debugger_active == True


# Generated at 2022-06-13 14:56:00.900348
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass


# Generated at 2022-06-13 14:56:01.494377
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True


# Generated at 2022-06-13 14:56:03.437779
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule()

# check to see if this is being run directly
if __name__ == '__main__':
    ''' unit test for StrategyModule '''
    
    test_StrategyModule()

# Generated at 2022-06-13 14:56:05.820549
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert isinstance(StrategyModule(None), StrategyModule) and \
        isinstance(StrategyModule(None), LinearStrategyModule) and \
        StrategyModule(None).debugger_active


# ----------
# Debugger Commands
# ----------

# Generated at 2022-06-13 14:56:08.607819
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'tqm'
    strategy_module = StrategyModule(tqm)
    assert strategy_module.tqm == tqm


# Generated at 2022-06-13 14:56:21.121118
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Execute unit test for StrategyModule")
    from ansible.plugins.loader import strategy_loader
    from ansible.executor.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager(
        inventory=None,
        variable_manager=None,
        loader=None,
        options=None,
        passwords=None,
        stdout_callback="default",
        run_additional_callbacks=True,
        run_tree=False,
    )
    strategy_class = strategy_loader.get('debug')
    strategy_instance = strategy_class(tqm)
    print(strategy_instance)
    assert(strategy_instance.get_host_keys_ref()) is None
    assert(strategy_instance.should_display_skipped_hosts) is False

# Generated at 2022-06-13 14:56:27.954254
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    try:
        tqm = StrategyModule(tqm)
    except:
        print("Exception in StrategyModule")
        raise
    else:
        print("StrategyModule.__init__ passed")



# Generated at 2022-06-13 14:56:34.101637
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible_collections.notmintest.not_a_real_collection.tests.unit.compat.mock import MagicMock
    from ansible_collections.notmintest.not_a_real_collection.tests.unit.plugins.strategy import TestLinearStrategyModule
    tqm = MagicMock()
    try:
        StrategyModule(tqm)
    except Exception:
        assert False



# Generated at 2022-06-13 14:56:35.431590
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None).debugger_active == True


# Generated at 2022-06-13 14:56:39.146588
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class FakeTQM():
        def __init__(self):
            self.stats = {}
            self.tqm_variables = {}

    tqm = FakeTQM()
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active is True


# Generated at 2022-06-13 14:56:44.222057
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import Queue
    sys.modules['ansible.plugins.strategy.linear'] = __import__('ansible.plugins.strategy.linear', globals(), locals(), ['StrategyModule'], -1)
    assert StrategyModule
    tqm = Queue.Queue()
    assert StrategyModule(tqm)


# Generated at 2022-06-13 14:56:47.855215
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    sys.argv = ['ansible-playbook', '-C', '/tmp/ansible-playbook-yNPDcH']
    tqm = None
    strategy = StrategyModule(tqm)
    assert strategy.debugger_active is True


# Generated at 2022-06-13 14:56:49.101194
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    return


# Generated at 2022-06-13 14:56:50.616965
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    main()

# Unit test of main method

# Generated at 2022-06-13 14:56:56.915907
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # When I create an instance of StrategyModule
    strategy_module = StrategyModule(None)
    # Then self.debugger_active should be True
    assert strategy_module.debugger_active


    # When I create an instance of StrategyModule with argument 123
    strategy_module = StrategyModule(123)
    # Then self.debugger_active should be True
    assert strategy_module.debugger_active



# Generated at 2022-06-13 14:56:58.496891
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # assert_equal(expected, StrategyModule(tqm))
    raise SkipTest # TODO: implement your test here



# Generated at 2022-06-13 14:57:06.059628
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__name__ == 'StrategyModule'
    assert len(StrategyModule.__bases__) == 1
    assert StrategyModule.__bases__[0].__name__ == 'LinearStrategyModule'
    assert len(LinearStrategyModule.__bases__) == 1
    assert LinearStrategyModule.__bases__[0].__name__ == 'BaseStrategyModule'
    assert len(BaseStrategyModule.__bases__) == 1
    assert BaseStrategyModule.__bases__[0].__name__ == 'object'
    assert StrategyModule.debugger_active == True


# Generated at 2022-06-13 14:57:08.494339
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    test_class = StrategyModule(tqm)
    print(test_class.debugger_active)


# Generated at 2022-06-13 14:57:12.411130
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        _ = StrategyModule(None)
    except Exception as e:
        raise AssertionError('Exception raised: %s' % str(e))


# Generated at 2022-06-13 14:57:17.068260
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 'tqm'
    s = StrategyModule(tqm)
    assert s.tqm == tqm
    assert s.tqm_tasks == []
    assert s.name == 'debug'
    assert s.done == False
    assert s.next_task == None
    assert s.current_task == None
    assert s.debugger_active == True


# Generated at 2022-06-13 14:57:20.387369
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # create instance of class StrategyModule
    # for unit test,it doesn't need to create a task queue manager
    test_strategy_module = StrategyModule(None)
    assert test_strategy_module.__class__.__name__ == 'StrategyModule'
    assert isinstance(test_strategy_module, LinearStrategyModule)



# Generated at 2022-06-13 14:57:31.452058
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    playbook_path = "/home/travis/build/ansible/ansible/test/sanity/playbook.yml"
    inventory_path = "/home/travis/build/ansible/ansible/test/sanity/inventory"
    loader = None
    variable_manager = None
    variable_manager = None
    play = None

# Generated at 2022-06-13 14:57:33.419280
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(tqm=None)
    assert strategy.debugger_active == True


# Generated at 2022-06-13 14:57:39.264466
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        import mock
        from ansible.plugins.strategy import linear

        strategy_module = StrategyModule()

        assert strategy_module.debugger_active == True
    except:
        sys.stdout.write("Exception in user code:\n")
        sys.stdout.write(traceback.format_exc())
        raise
# end unit test


# Generated at 2022-06-13 14:57:43.507980
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    lsm = LinearStrategyModule(None)
    lsm.debugger_active = True
    sm = StrategyModule(None)
    assert sm.debugger_active
    assert type(sm) is type(lsm)


# Generated at 2022-06-13 14:57:45.701565
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert(StrategyModule._usage is None and
           StrategyModule._supports_check_mode is False and
           StrategyModule._supports_async is False and
           StrategyModule._supports_workspace is False)
#


# Generated at 2022-06-13 14:57:56.559002
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # test
    s = StrategyModule(None)
    # assert
    assert s.debugger_active

# This is a debug session which is used to control the execution of tasks.
# It is not used in production.

# Generated at 2022-06-13 14:57:57.528232
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule is not None


# Generated at 2022-06-13 14:57:58.511424
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule(None)


# Generated at 2022-06-13 14:58:06.706925
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Test constructor of StrategyModule
    test_tqm = "TEST_tqm"
    test_strategy_module = StrategyModule(test_tqm)
    assert test_strategy_module.tqm == test_tqm
    assert test_strategy_module.inventory == None
    assert test_strategy_module.variable_manager == None
    assert test_strategy_module.loader == None
    assert test_strategy_module.options == None
    assert test_strategy_module.shared_loader_obj == None
    assert test_strategy_module.passwords == None
    assert test_strategy_module.iterator == None
    assert test_strategy_module.play_context == None
    assert test_strategy_module.host_list == None
    assert test_strategy_module.play

# Generated at 2022-06-13 14:58:08.685310
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    test_instance = StrategyModule('test')
    assert test_instance.debugger_active == True


# Generated at 2022-06-13 14:58:09.709779
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert callable(StrategyModule)



# Generated at 2022-06-13 14:58:12.691948
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = null
    objStrategyModule = StrategyModule(tqm)

    assert objStrategyModule.debugger_active == True
# end of Unit Test for constructor of class StrategyModule


# Generated at 2022-06-13 14:58:15.258032
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        s = StrategyModule()
    except:
        assert False
    assert type(s) is StrategyModule



# Generated at 2022-06-13 14:58:17.439350
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    pass

    # cmd.Cmd class that defines the debugger prompt
    # Tests are done in StrategyModule class

# Generated at 2022-06-13 14:58:20.116654
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = {}
    test_strategy = StrategyModule(tqm)
    assert test_strategy.debugger_active == True


# Generated at 2022-06-13 14:58:35.646004
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # creating an instance of class StrategyModule
    assert(StrategyModule)



# Generated at 2022-06-13 14:58:36.619952
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule(None)
    assert strategy.debugger_active == True


# Generated at 2022-06-13 14:58:38.136825
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = None
    try:
        sm = StrategyModule(tqm)
    except:
        assert False

    assert True


# Generated at 2022-06-13 14:58:39.092533
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule('tqm')


# Generated at 2022-06-13 14:58:39.813967
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule(object)



# Generated at 2022-06-13 14:58:45.432214
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("Unittest for constructor of class StrategyModule")
    tqm = None
    strategy_module = StrategyModule(tqm)
    # TODO: we don't have enough information to test more?
    assert strategy_module.debugger_active == True
# end of unit test for constructor of class StrategyModule


# Generated at 2022-06-13 14:58:46.857517
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
	# TODO: Write unit test
	print("test")


# Generated at 2022-06-13 14:58:50.602839
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = "tqm"
    strategy_module = StrategyModule(tqm)
    assert strategy_module.debugger_active == True

if __name__ == '__main__':
    print("test_strategy_debug.py")
    test_StrategyModule()
    print("Done testing strategy_debug.py")

# Generated at 2022-06-13 14:58:53.758929
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    """ Constructor for class StrategyModule """
    try:
        s = StrategyModule(None)
    except:
        assert False, 'Constructor for class StrategyModule failed'
    assert s != None, 'Constructor for class StrategyModule failed'
    assert s.debugger_active==True, 'Constructor for class StrategyModule failed'


# Generated at 2022-06-13 14:59:01.667681
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest
    from ansible.plugins.strategy import debug

    class TestStrategyModule(unittest.TestCase):

        def test_constructor(self):
            tqm = 'tqm'
            x = debug.StrategyModule(tqm)
            self.assertEqual(x.tqm, tqm)
            self.assertEqual(x.module_name, 'debug')
            self.assertEqual(x.debugger_active, True)

    unittest.main()


# Generated at 2022-06-13 14:59:36.488818
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    debugger_active = True
    strategymodule = StrategyModule(tqm=None)
    assert strategymodule.debugger_active == debugger_active


# Generated at 2022-06-13 14:59:38.222547
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    StrategyModule.__init__(None)


# Generated at 2022-06-13 14:59:43.393810
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.utils.collection_loader import AnsibleCollectionLoader
    from ansible.executor.task_queue_manager import TaskQueueManager
    loader = AnsibleCollectionLoader()
    tqm = TaskQueueManager(loader=loader)
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True



# Generated at 2022-06-13 14:59:47.518280
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    print("[test] start")

    # create instance of class TaskQueueManager
    tqm = get_TaskQueueManager()

    # create instance of class StrategyModule
    strategy_module = StrategyModule(tqm)

    print("[test] succeeded")



# Generated at 2022-06-13 14:59:52.826404
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Create a fake tqm object
    class tqm():
        def __init__(self):
            self.stats = {}
            self.hostvars = {}

    # Create a fake results object
    class results():
        def __init__(self):
            self.is_failed = True

    fake_tqm = tqm()
    fake_results = results()
    sm = StrategyModule(fake_tqm)


# Generated at 2022-06-13 14:59:58.211545
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Test constructor of class StrategyModule
    # Output: A StrategyModule object
    # A StrategyModule object is created because the class has no attribute debugger_active

    import ansible.plugins.strategy.debug

    fileName = sys.argv[0]
    class_name = fileName.split('/')[-1].split('.')[0]

    class_ = getattr(globals()[class_name], 'StrategyModule')
    instance = class_()
    assert hasattr(instance, 'debugger_active')



# Generated at 2022-06-13 15:00:07.050515
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    ref_dict = {'body': 'test'}
    ref_dict['body'] = 'test'
    class _tqm:
        def __init__(self):
            self.variable_manager = ref_dict

    tqm = _tqm()
    test_obj = StrategyModule(tqm)
    assert hasattr(test_obj, 'debugger_active')
    assert hasattr(test_obj, '_debugger')
    assert hasattr(test_obj, '_last_task_banner')
    assert hasattr(test_obj, 'tqm')



# Generated at 2022-06-13 15:00:09.055515
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy_module = StrategyModule(None)
    assert strategy_module is not None
    assert strategy_module.debugger_active is True


# Generated at 2022-06-13 15:00:10.088019
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    strategy = StrategyModule()
    assert strategy.debugger_active == True


# Generated at 2022-06-13 15:00:11.115761
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert True  


# Generated at 2022-06-13 15:01:27.260042
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import mock
    import ansible.plugins.strategy.debug
    tqm = mock.MagicMock('Tqm')
    strategy_module = ansible.plugins.strategy.debug.StrategyModule(tqm)
    assert strategy_module.debugger_active


# Generated at 2022-06-13 15:01:29.104740
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    my_strategy_module = StrategyModule(None)
    assert(my_strategy_module.debugger_active == True)


# Generated at 2022-06-13 15:01:32.497420
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Create a StrategyModule object
    linear_strategy_module = StrategyModule(None)
    # Check that debugger_active is set to True
    assert linear_strategy_module.debugger_active


# Generated at 2022-06-13 15:01:38.147890
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    task = {'action': {'__ansible_module__': 'setup', '__ansible_arguments__': ['host_list=localhost']}}
    #plugin = StrategyModule(tqm=tqm)
    #plugin.debugger_active = True
    #plugin._tqm.send_callback(event='v2_playbook_on_task_start', task=task)



# Generated at 2022-06-13 15:01:46.642357
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    execution_queue = [{"name": "task-name", "action": {"__ansible_no_log": False, "__ansible_module__": "shell", "__ansible_arguments__": "echo -n Hi", "__ansible_action_wrapper__": "/usr/bin/python /home/user/.ansible/tmp/ansible-tmp-1416368182.78-231749574597676/shell", "__ansible_modulenamemodulename__": "shell"}}]
    class mock_tqm(object):
        def __init__(self):
            self.shared_loader_obj = None
            self.host_hash_val = ""
            self.host_hash = ""
            self.set_host_hash = ""
            self.cur_tqm_iteration = ""


# Generated at 2022-06-13 15:01:55.165866
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # Create a test task queue manager.
    from ansible.executor.task_queue_manager import TaskQueueManager
    tqm = TaskQueueManager(None, None, None, None)
    sm = StrategyModule(tqm)
    assert sm.debugger_active == True
    assert sm.hosts_left == None
    assert sm.hosts_remaining == None
    assert sm.max_fail_pct == 0.0
    assert sm.serialized_queue == []
    assert sm.task_queue == []
    assert sm.tqm == None
    assert sm.variable_manager == None

# Generated at 2022-06-13 15:02:01.134419
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    obj = StrategyModule('tqm')
    assert type(obj) == StrategyModule
    assert obj.debugger_active == True
    assert obj.tqm == 'tqm'


# Generated at 2022-06-13 15:02:04.950222
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  # Create fake tqm and config to pass to StrategyModule constructor
  tqm = (None)
  config = (None)
  # Create StrategyModule object
  strategy = StrategyModule(tqm)
  # Get the debug flag
  debug_flag = strategy.debugger_active
  # Assert that the flag is true
  assert(debug_flag == True)


# Generated at 2022-06-13 15:02:06.043854
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
	assert StrategyModule.__doc__ == "Executes tasks in interactive debug session."


# Generated at 2022-06-13 15:02:12.345582
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    class MyTqm:
        def __init__(self):
            self.stats = {}
            self.host_failed = {}
            self.host_ok = {}
            self.host_unreachable = {}
            self.host_skipped = {}
            self.variable_manager = {}
            self.responder = {}

    class MyVarMgr:
        def __init__(self):
            self.extra_vars = {}

    class MyResponder:
        def __init__(self):
            self.on_failed_task = 0
            self.on_unreachable = 0
            self.on_ok = 0
            self.on_skipped = 0

    tqm = MyTqm()
    tqm.variable_manager = MyVarMgr()
    tqm.responder = My

# Generated at 2022-06-13 15:04:57.698182
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    # class StrategyModule, no unit test for now
    pass



# Generated at 2022-06-13 15:04:59.742201
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        from ansible.plugins.strategy import debug
        assert debug.hasattr('StrategyModule')
    except Exception as e:
        print(e)
        assert False



# Generated at 2022-06-13 15:05:00.450848
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
  sm = StrategyModule(None)


# Generated at 2022-06-13 15:05:01.947903
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    try:
        StrategyModule()
    except:
        print("Cannot instantiate StrategyModule object")



# Generated at 2022-06-13 15:05:03.475780
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = 1
    host = StrategyModule(tqm)
    print(host.debugger_active)



# Generated at 2022-06-13 15:05:04.865995
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert StrategyModule.__class__.__bases__ == (LinearStrategyModule,)
    assert StrategyModule.debugger_active == True


# Generated at 2022-06-13 15:05:07.190546
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    from ansible.executor.task_queue_manager import TaskQueueManager
    print("***** testing constructor of class StrategyModule *****")
    tqm = TaskQueueManager(None, None, None, None, None, None, None, None)
    StrategyModule(tqm)
    

# Generated at 2022-06-13 15:05:08.310856
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    assert callable(StrategyModule)


# Generated at 2022-06-13 15:05:19.309271
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    import __builtin__
    from Queue import Empty
    from ansible.plugins.multiprocessing.multiprocessing import TQMProcess
    from ansible.errors import AnsibleError
    from ansible.inventory.host import Host
    from ansible.inventory.group import Group
    from ansible.playbook.task import Task

    class FakeTarget(object):
        def __init__(self):
            self.qsize = 0
            self.task_queue = __builtin__.queue.Queue()

    class FakeQueueManager(object):
        def __init__(self):
            self.fake_target = FakeTarget()
            self.targets = dict()
            self.targets['fake'] = self.fake_target
            self.terminated = False


# Generated at 2022-06-13 15:05:22.246309
# Unit test for constructor of class StrategyModule
def test_StrategyModule():
    tqm = object()
    strategy_module = StrategyModule(tqm)

    assert strategy_module.tqm == tqm
    assert strategy_module.debugger_active == True
