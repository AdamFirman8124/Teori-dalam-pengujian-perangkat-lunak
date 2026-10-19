

# Generated at 2022-06-13 11:40:20.061777
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    cb = CallbackModule()
    cb.v2_runner_on_ok({"host": "127.0.0.1", "ansible_stats": {}, "changed": False, "result": {"stdout": " ", "stderr": " "}})


# Generated at 2022-06-13 11:40:23.578584
# Unit test for method v2_runner_on_async_poll of class CallbackModule
def test_CallbackModule_v2_runner_on_async_poll():
    # create an instance of the Ansible callback module
    ansible_callback_module_instance = CallbackModule()
    # test the method v2_runner_on_async_poll
    ansible_callback_module_instance.v2_runner_on_async_poll(result=None)



# Generated at 2022-06-13 11:40:25.522363
# Unit test for method v2_playbook_on_play_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_play_start():
    callb = CallbackModule()
    play = Play()
    callb.v2_playbook_on_play_start(play)
    assert callb._play == play

# Generated at 2022-06-13 11:40:31.228400
# Unit test for method v2_playbook_on_play_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_play_start():
    callback = CallbackModule()
    play = "Play"

    # testing with no name
    callback.v2_playbook_on_play_start(play)
    assert callback._play == play
    assert callback._last_task_banner == None
    assert callback._last_task_name == None
    assert callback.playbook == play

    # testing with name
    play = playbook.Play()
    play._attributes = {'name': "Test name"}
    callback.v2_playbook_on_play_start(play)
    assert callback._play == play
    assert callback._last_task_banner == None
    assert callback._last_task_name == None
    assert callback.playbook == play


# Generated at 2022-06-13 11:40:41.572451
# Unit test for method v2_runner_on_async_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_async_failed():
    # Parameters
    result = ""
    # Configuration
    display = object()

    # Mocking
    class MockDisplay(object):
        def __init__(self):
            self._display = None
        def display(self, msg, color=None):
            self._display = msg
    mock_display = MockDisplay()
    # Patching
    with patch.dict('sys.modules', {'ansible.plugins.callback.default': MockDisplay()}):
        # Unit test
        callback = CallbackModule()
        callback.display = mock_display
        callback.v2_runner_on_async_failed(result)
        # Assertion
        assert mock_display._display == "ASYNC FAILED on : jid="

# Generated at 2022-06-13 11:40:50.261588
# Unit test for method v2_runner_retry of class CallbackModule
def test_CallbackModule_v2_runner_retry():
    result = RunnerResult()
    result.task_name = 'test_task'
    result.result = {'exception': 'test', 'stderr': 'test', 'stdout': 'test', 'stdout_lines': ['test1', 'test2'], 'warnings': ['test1', 'test2']}
    result.host = Host('hostname')
    result.host.name = 'hostname'
    result.host.get_name.return_value = 'hostname'
    result.host.get_vars.return_value = {'ansible_user': 'user', 'ansible_host': '127.0.0.1'}
    result.task = Task()
    result.task._uuid = 'uuid'

    class Play:
        def __init__(self):
            self.get_

# Generated at 2022-06-13 11:40:55.222367
# Unit test for method v2_runner_retry of class CallbackModule
def test_CallbackModule_v2_runner_retry():
    runner_retry = CallbackModule(display=None)

    result = MagicMock(spec=ResultCallback)
    result.task_name = None
    result._task = ''
    result._result = {
        "attempts": 1,
        "retries": 2,
    }

    runner_retry.v2_runner_retry(result)



# Generated at 2022-06-13 11:40:57.640459
# Unit test for method v2_runner_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_on_skipped():
    pass # TODO: implement test_CallbackModule_v2_runner_on_skipped


# Generated at 2022-06-13 11:41:08.841390
# Unit test for method v2_runner_on_async_poll of class CallbackModule

# Generated at 2022-06-13 11:41:09.732807
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    pass


# Generated at 2022-06-13 11:41:38.746521
# Unit test for method v2_runner_item_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_item_on_failed():
    
    mocked_result_item = Mock(spec=ResultItem)
    mocked_host = Mock(spec=Host)
    mocked_host.get_name.return_value = 'host1'
    
    mocked_result_item.result._task = 'task'
    mocked_result_item.result._host = mocked_host
    mocked_result_item.result._result = {'failed': 'yes'}
    
    
    mocked_self = Mock(spec=CallbackModule)
    mocked_self.display_failed_stderr = False
    mocked_self.display = Mock()
    mocked_self.display.verbosity = 2
    
    mocked_self.v2_runner_item_on_failed(mocked_result_item)
    

# Generated at 2022-06-13 11:41:50.136691
# Unit test for method v2_runner_item_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_item_on_failed():
    result = namedtuple("Result", ["_task", "_host", "_result", "_play_context"])
    result._host = namedtuple("Host", ["get_name"])
    result._host.get_name.return_value = "TEST_HOST"
    result._result = dict()
    result._result["exception"] = "TEST_EXCEPTION"
    result._result["msg"] = "TEST_MESSAGE"
    
    callback = CallbackModule()
    
    stdout_old = sys.stdout
    

# Generated at 2022-06-13 11:41:52.113374
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():

    # TODO: Return a specific result
    result = None
    callback_module = CallbackModule()
    callback_module.v2_runner_on_ok(result)



# Generated at 2022-06-13 11:41:55.617915
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
  print("Testing CallbackModule.v2_runner_on_failed()")
  callback = CallbackModule()
  result = type('obj', (object,), {"_host": "host", "_result": {"msg": "msg"}, "_task": type('obj', (object,), {"action": "action"})})
  callback.v2_runner_on_failed(result)
  print("Testing CallbackModule.v2_runner_on_failed() - Done")


# Generated at 2022-06-13 11:42:09.369778
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # set up
    display = Mock()
    runner = Mock()
    result = Mock()
    result.task_name = "test task name"
    result._result = "test result"
    result._host = Mock()
    result._host.get_name.return_value = "test host"
    runner.action = "test action"
    callback = CallbackModule(display)
    callback._dump_results = Mock()
    callback._dump_results.return_value = "test result"
    callback._clean_results = Mock()
    callback._clean_results.return_value = None
    callback._run_is_verbose = Mock()
    callback._run_is_verbose.return_value = True
    callback._last_task_banner = "test task banner"

# Generated at 2022-06-13 11:42:15.382193
# Unit test for method v2_runner_on_async_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_async_failed():
    a = CallbackModule()
    result = {'async_result':{'ansible_job_id':123}}
    result = type('result', (object,), {'_result':result})
    def mocked_display(s, color=None):
        x = color
    a._display.display = mocked_display
    a.v2_runner_on_async_failed(result)


# Generated at 2022-06-13 11:42:22.203598
# Unit test for method v2_runner_on_unreachable of class CallbackModule
def test_CallbackModule_v2_runner_on_unreachable():

    # Tests that if the display_failed_stderr option is:
    # - not set, then stderr isn't used
    # - set, then stderr is used
    def test_display_failed_stderr_explicit_options(unreachable_result, monkeypatch):

        class FakeDisplay(object):
            def __init__(self):
                self.message = ''

            def display(self, msg, color=None, stderr=False, log_only=False):
                self.message = msg
                self.stderr = stderr

        fake_display = FakeDisplay()

        # Monkeypatch
        monkeypatch.setattr(CallbackModule, '_display', fake_display)

        callback = CallbackModule()
        callback.display_failed_stderr = True
        callback.v2_runner_

# Generated at 2022-06-13 11:42:23.592824
# Unit test for method v2_playbook_on_stats of class CallbackModule
def test_CallbackModule_v2_playbook_on_stats():
    x = CallbackModule()
    pass


# Generated at 2022-06-13 11:42:33.588610
# Unit test for method v2_runner_item_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_item_on_failed():
    # Instanciating the class
    callback_object = CallbackModule()
    # Creating a fake result object
    result = FakeResult()
    # Setting up the parameters
    callback_object._last_task_banner = '123'
    result._task._uuid = '123'
    result._result['changed'] = True
    # Setting up the mocked out display object
    callback_object._display = MagicMock()
    # Calling the method
    callback_object.v2_runner_item_on_failed(result)
    # Making assertions
    assert callback_object._display.display.call_count == 2

# Generated at 2022-06-13 11:42:35.839462
# Unit test for method v2_runner_item_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_item_on_failed():
    """Unit test for CallbackModule.v2_runner_item_on_failed method."""
    # FIXME:
    pass


# Generated at 2022-06-13 11:43:23.095634
# Unit test for method v2_runner_item_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_item_on_failed():
    output = []
    callback = CallbackModule(display=Mock(Display=Mock(display=Mock(side_effect=lambda x,y,z: output.append({'x':x,'y':y,'z':z})))))
    task = Mock()
    task._uuid = 'test'
    task.args = {'test':'test'}
    result = Mock(result={'changed':False})
    result._task = task
    result._host = Mock(get_name=Mock(return_value='host'))
    callback.v2_runner_item_on_failed(result)
    assert output == [{'x': 'failed: [host]', 'y': 'ERROR', 'z': False}]


# Generated at 2022-06-13 11:43:28.870345
# Unit test for method v2_runner_item_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_item_on_ok():
    print("""|--- test_CallbackModule_v2_runner_item_on_ok start ---|""")
    x = CallbackModule()
    print("""|--- test_CallbackModule_v2_runner_item_on_ok end ---|""")
    print("\n")

# Generated at 2022-06-13 11:43:36.578194
# Unit test for method v2_runner_item_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_item_on_failed():
    callback_module_instance = CallbackModule()
    task_result = TaskResult('failed', 'item', 'host', 'result', 'task')
    expected_output_string = "ERROR! "
    actual_output_string = callback_module_instance.v2_runner_item_on_failed(task_result)
    assert actual_output_string == expected_output_string


# Generated at 2022-06-13 11:43:41.453023
# Unit test for method v2_runner_on_async_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_async_ok():
    mock_result = mock.Mock()
    mock_result.async_result = mock.Mock()
    mock_display = mock.Mock()
    mock_callback = CallbackModule(display=mock_display)
    mock_callback.v2_runner_on_async_ok(mock_result)
    mock_result.async_result.assert_called_once()


# Generated at 2022-06-13 11:43:45.141828
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    host = ''
    result = ''
    cb = CallbackModule()
    assert(cb.v2_runner_on_failed(host, result)) == None


# Generated at 2022-06-13 11:43:45.835063
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    pass

# Generated at 2022-06-13 11:43:52.040297
# Unit test for method v2_runner_retry of class CallbackModule
def test_CallbackModule_v2_runner_retry():
    my_object = CallbackModule()
    result = {}
    result['_result'] = {}
    result['_task'] = 'Test'
    result['_result']['retries'] = 2
    result['_result']['attempts'] = 1
    result['task_name'] = "Test"
    my_object.v2_runner_retry(result)


# Generated at 2022-06-13 11:44:03.505336
# Unit test for method v2_runner_on_async_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_async_ok():
    # No error

    cb = CallbackModule()
    result = Result()
    result._host = '10.1.1.1'
    result._result = {'ansible_job_id': 0}
    
    with patch('logger.CallbackModule.v2_display.display') as display:
        cb.v2_runner_on_async_ok(result)
        assert display.call_count == 1
        args, kwargs = display.call_args
        assert args == ('ASYNC OK on %s: jid=%s' % (result._host.get_name(), result._result.get('ansible_job_id')),)
        assert kwargs == {'color': 'green'}

    # Exception

    with pytest.raises(StandardError):
        cb.v2_

# Generated at 2022-06-13 11:44:16.137576
# Unit test for method v2_playbook_on_play_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_play_start():
    mock_self = Mock()
    mock_play = Mock()
    mock_play.get_name.return_value = 'foo'
    mock_display = Mock()
    CallbackModule.display = mock_display
    CallbackModule.check_mode_markers = True
    CallbackModule.v2_playbook_on_play_start(mock_self, mock_play)
    mock_display.banner.assert_called_with('PLAY [foo] [CHECK MODE]')
    mock_display.banner.reset_mock()

    CallbackModule.check_mode_markers = False
    CallbackModule.v2_playbook_on_play_start(mock_self, mock_play)
    mock_display.banner.assert_called_with('PLAY [foo]')
    mock_display.ban

# Generated at 2022-06-13 11:44:19.137109
# Unit test for method v2_runner_on_async_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_async_failed():
    # Test cases that fail without an exception
    pass # test_CallbackModule_v2_runner_on_async_failed is implemented as a no-op.



# Generated at 2022-06-13 11:45:00.281350
# Unit test for method v2_runner_on_unreachable of class CallbackModule
def test_CallbackModule_v2_runner_on_unreachable():
    testCallbackModule = CallbackModule()

    assert testCallbackModule.v2_runner_on_unreachable(None) == None


# Generated at 2022-06-13 11:45:07.986168
# Unit test for method set_options of class CallbackModule

# Generated at 2022-06-13 11:45:15.087255
# Unit test for method v2_runner_retry of class CallbackModule
def test_CallbackModule_v2_runner_retry():
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory

    from ansible.playbook.play_context import PlayContext
    from ansible.runner.return_data import ReturnData

    from ansible.plugins.callback import CallbackModule

    result_obj = ReturnData(host=dict(name='test_host'),
                            task=dict(name='test_task'),
                            result=dict(retries=5, attempts=2))
    callback_module_obj = CallbackModule()
    callback_module_obj._display.verbosity = 1
    callback_module_obj.v2_runner_retry(result_obj)

# Generated at 2022-06-13 11:45:20.908099
# Unit test for method v2_playbook_on_include of class CallbackModule
def test_CallbackModule_v2_playbook_on_include():
    callback = CallbackModule()
    result = ""
    result += "included: "
    result += "test_filename"
    result += " for "
    result += ", ".join([h.name for h in "test_hosts"])
    assert(callback.v2_playbook_on_include("test_included_file") == result)


# Generated at 2022-06-13 11:45:23.692475
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    module = CallbackModule()
    result = {}
    module.v2_runner_on_ok(result)

# Generated at 2022-06-13 11:45:38.893846
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():

    host = Mock(ansible_ssh_user='ansible_ssh_user', get_name=Mock(return_value='get_name'), get_variables=Mock(return_value='get_variables'))
    task = Mock(get_name=Mock(return_value='get_name'))
    display = Mock(display=Mock(return_value='display'), verbosity=Mock(return_value=1), colorize=Mock(return_value='colorize'))
    ansi = Mock(wrap=Mock(return_value='wrap'))
    play = Mock()
    runner = Mock(get_host_variables=Mock(return_value='get_host_variables'))

# Generated at 2022-06-13 11:45:43.151946
# Unit test for method v2_playbook_on_include of class CallbackModule
def test_CallbackModule_v2_playbook_on_include():
    callback_plugin = CallbackModule()
    stats = {'ok':0, 'changed':1, 'failures':0, 'skipped':0, 'unreachable':0, 'rescued':0, 'ignored':0}
    stats.update(custom={'successful':0, 'failed':1})
    callback_plugin.v2_playbook_on_stats(stats)

# Generated at 2022-06-13 11:45:54.797099
# Unit test for method v2_playbook_on_play_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_play_start():  
    # Read test file and get parameters to create the Ansible Playbook instance
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAnsiblePlaybook)
    res = unittest.TextTestRunner(verbosity=2).run(suite)
    ansible_playbook_impl_instance = res.tests[0]._tests[0]._ansible_playbook_impl_instance
    impl = ansible_playbook_impl_instance._impl

    # Test method
    impl.v2_playbook_on_play_start(ansible_playbook_impl_instance._play)


# Class to test method v2_playbook_on_playbook_on_notify

# Generated at 2022-06-13 11:46:01.152560
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    from ansible.vars import VariableManager
    from ansible.utils.vars import load_extra_vars
    from ansible.utils.vars import load_options_vars
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.inventory.host import Host
    from ansible.playbook.task import Task
    from ansible.utils.display import Display
    from ansible.plugins.callback.default import CallbackModule

    variable_manager = VariableManager()
    loader = DataLoader()
    display = Display()

    inventory = InventoryManager(loader=loader, variable_manager=variable_manager, sources='')
    variable_manager.add_inventory(inventory)

    testhost = Host(name="testhost")

# Generated at 2022-06-13 11:46:15.088744
# Unit test for method v2_runner_item_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_item_on_failed():
 
    # setup
    mock_result = Mock()
    mock_result._task = Mock()
    mock_result._task.action = 'command'
    mock_result._result = {'changed': True, 'failed': False}
    c = DefaultCallbackModule()
    
    # test
    c.v2_runner_item_on_failed(mock_result)
    
    # assert
    assert c._last_task_banner == None
    assert c._last_task_name == None
    assert c._task_start
    assert c.display_failed_stderr
    assert c.display_ok_hosts
    assert c.display_skipped_hosts
    assert c.display_task_item
    assert c.show_custom_stats
    assert c.stats
    assert c.task_output
   

# Generated at 2022-06-13 11:47:36.272182
# Unit test for method v2_runner_on_async_poll of class CallbackModule
def test_CallbackModule_v2_runner_on_async_poll():
    result = ResultCallbackForTesting()
    CallbackModule = get_CallBackModule()
    c = CallbackModule()
    c.v2_runner_on_async_poll(result)


# Generated at 2022-06-13 11:47:40.155926
# Unit test for method set_options of class CallbackModule
def test_CallbackModule_set_options():
    print("Testing set_options for CallbackModule")
    options = {'foo': 'bar'}
    a = CallbackModule()
    a.set_options(options)
    assert a._options == {'foo':'bar'}


# Generated at 2022-06-13 11:47:43.702700
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    args = MagicMock()
    args.verbosity = 3
    args.check = False
    context.CLIARGS = args
    callbacks = CallbackModule()
    playbook = MagicMock()
    playbook._file_name = './playbooks/sample.yml'
    callbacks.v2_playbook_on_start(playbook)
    assert callbacks._display.verbosity == 3
    assert callbacks._display.check == False


# Generated at 2022-06-13 11:47:45.637201
# Unit test for method v2_runner_on_async_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_async_ok():
    module = AnsibleCallbackModule()
    result = object()
    module.v2_runner_on_async_ok(result)


# Generated at 2022-06-13 11:47:57.454919
# Unit test for method v2_runner_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_on_skipped():
    # create the instance of CallbackModule to invoke the method v2_runner_on_skipped
    # create the parameters for the method
    callback_module = CallbackModule()
    result =  HostVars({'ansible_version': '2.4.3.0'}, {'var1': 'foo', 'var2': 'bar'}, 'dbserver.example.com')
    result._host = Host('dbserver.example.com')
    result._task = Task()
    result._task = Task()
    result._task.action = 'shell'
    result._task._uuid = 'b6d21c6e-9c66-4d1e-a0d6-7934a09a4823'
    result._task.loop = None

# Generated at 2022-06-13 11:48:04.004724
# Unit test for method v2_playbook_on_notify of class CallbackModule
def test_CallbackModule_v2_playbook_on_notify():

    # Mock class object to simulate the ansible object being passed in
    class MockDisplay():
        def __init__(self):
            self.verbosity = 2
            self.display = True
        def display(self, msg, color, screen_only):
            pass

    class MockHandler():
        def __init__(self):
            self.name = 'test'
        def get_name(self):
            return self.name

    callback = CallbackModule()
    callback._display = MockDisplay()
    handler = MockHandler()
    host = 'localhost'
    callback.v2_playbook_on_notify(handler, host)
    #assert 1 == 1

    return

# Generated at 2022-06-13 11:48:05.742700
# Unit test for method v2_runner_item_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_item_on_ok():
    c = CallbackModule()
    c.v2_runner_item_on_ok('result')


# Generated at 2022-06-13 11:48:17.212044
# Unit test for method v2_runner_item_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_item_on_skipped():
    test = CallbackModule()
    test.display_skipped_hosts = True

# Generated at 2022-06-13 11:48:23.575786
# Unit test for method v2_runner_on_async_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_async_failed():
    cb = CallbackModule()
    result = {}
    result['_host'] = {}
    result['_host']['get_name'] = MagicMock(return_value='127.0.0.1')
    result['_result'] = {}
    result['_result']['ansible_job_id'] = ''
    cb.v2_runner_on_async_failed(result)


# Generated at 2022-06-13 11:48:25.686860
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    callbackModule = CallbackModule({}, {}, {}, {}, {}, {})
    callbackModule.v2_runner_on_ok(None)