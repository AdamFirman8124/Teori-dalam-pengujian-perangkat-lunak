

# Generated at 2022-06-13 11:40:27.946789
# Unit test for method v2_playbook_on_stats of class CallbackModule
def test_CallbackModule_v2_playbook_on_stats():
    # Initialize test environment
    #####################################################
    #   This is done automatically when calling the class
    #   or here for testing purposes
    #####################################################
    test_module = 'ansible.plugins.callback.default'
    test_module_path = os.path.join(
        os.getcwd(), 'lib/ansible/plugins/callback/default.py')
    sys.modules[test_module] = imp.load_source(test_module, test_module_path)
    test_module = 'ansible.plugins.callback.default.CallbackModule'
    test_module_path = os.path.join(
        os.getcwd(), 'lib/ansible/plugins/callback/default.py')

# Generated at 2022-06-13 11:40:40.153506
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    from ansible.plugins.callback import CallbackBase
    from ansible.playbook.play import Play
    from ansible import context
    import json
    import pytest
    myplaybook = Play()
    myplaybook._file_name = 'test'

# Generated at 2022-06-13 11:40:48.777473
# Unit test for method v2_runner_item_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_item_on_skipped():
    cbm = CallbackModule()
    cbm.display_skipped_hosts = True

    result = DummyResult(action="show", _task=DummyTask(), _host=DummyHost())

    cbm._last_task_banner = "foo"
    cbm.v2_runner_item_on_skipped(result)
    assert cbm._last_task_banner == "foo"

    result._task._uuid = "foo"
    with patch("ansible.plugins.callback.human_log.CallbackModule._print_task_banner") as \
            mock_print_task_banner:
        cbm._last_task_banner = None
        cbm.v2_runner_item_on_skipped(result)
        assert mock_print_task_banner.call_count == 1



# Generated at 2022-06-13 11:40:49.676823
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    assert True==False

# Generated at 2022-06-13 11:40:53.559988
# Unit test for method v2_runner_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_on_skipped():
    runner_result = {
    "_result": {
        "item": {
            "key1": "value1",
            "key2": "value2"
        }
    },
    "_task": {
        "action": "test_action"
    }
}
    module = CallbackModule()
    result = module.v2_runner_item_on_skipped(runner_result)
    assert result == None

# Generated at 2022-06-13 11:41:06.330609
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    """
    Test whether CallbackModule.v2_runner_on_failed
    works as expected or not
    """

    # Testcase 1: Unreachable host
    # Expected result: Host name followed by an error
    callback = CallbackModule()
    result = namedtuple('Result', ['_host', '_task',
                                   '_result', '_task_fields',
                                   '_task_vars'])
    host = namedtuple('Host', ['get_name'])
    task = namedtuple('Task', [])
    res = {'msg': 'An error occurred when communicating with the remote host.',
           'unreachable': True}
    test_result = result(host(get_name='Host'), task(), res, [], {})

# Generated at 2022-06-13 11:41:08.916581
# Unit test for method set_options of class CallbackModule
def test_CallbackModule_set_options():
    module = CallbackModule()
    result = module.set_options({'test': 'option'})
    assert result is None
    assert module.options['test'] == 'option'

# Generated at 2022-06-13 11:41:10.761674
# Unit test for method v2_playbook_on_play_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_play_start():
  pass



# Generated at 2022-06-13 11:41:18.992192
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # Simple unit test of class method v2_runner_on_failed.
    # This unit test needs class CallbackModule to be defined in the
    # ansible.plugins.callback.default file.
    from ansible.plugins.callback.default import CallbackModule
    cm = CallbackModule()
    # Create a result with a fake results dict that looks like the result of a
    # failed task.
    result = {'_result': {'failed': True, 'msg': 'Test failed.'}}
    cm.v2_runner_on_failed(result)
    # Check the results.
    # TODO: check that the results have been logged.
    assert result['_result']['failed'] is False
    assert result['_result']['msg'] == 'Test failed.'


# Generated at 2022-06-13 11:41:21.324897
# Unit test for method v2_runner_on_unreachable of class CallbackModule
def test_CallbackModule_v2_runner_on_unreachable():
    runner_on_unreachable = getattr(CallbackModule(), 'v2_runner_on_unreachable')
    assert type(runner_on_unreachable) is types.MethodType

# Generated at 2022-06-13 11:41:45.388997
# Unit test for method v2_playbook_on_play_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_play_start():
    import ansible.plugins.callback.default; ansible.plugins.callback.default
    import ansible.plugins.callback
    cb = ansible.plugins.callback.default.CallbackModule()
    cb.playbook_on_play_start(play=None)



# Generated at 2022-06-13 11:41:53.353520
# Unit test for method v2_playbook_on_stats of class CallbackModule
def test_CallbackModule_v2_playbook_on_stats():
    # Test with non-existent inventory file
    options = create_options_mock()
    loader = create_loader_mock()
    display = create_display_mock()
    callback = CallbackModule(display, options, loader)

    # Generate stats

# Generated at 2022-06-13 11:42:08.815471
# Unit test for method v2_runner_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_on_skipped():
    ###
    # Test with display_skipped_hosts=True, expected should be the message of 'OK'
    ###
    # Initialize a CallbackModule object
    cb = CallbackModule()
    # Initialize a HostResult object with the message of 'OK'
    result = HostResult(host='hostname', task=MockTask(), result={'changed': False, 'msg': 'OK'})
    # Call the method
    cb.v2_runner_on_skipped(result)
    # Get the message from the class attribute
    output = cb.test_result

    expected = "skipping: [hostname] => (item=None) => {'msg': 'OK', 'changed': False, 'skip_reason': 'Conditional result was False'}\n"
    assert output == expected
    ###
    # Test with

# Generated at 2022-06-13 11:42:17.058807
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    one_result = dict(
        _task = object(),
        _result = dict(
            diff = "testing"
        )
    )
    dummy_runner = object()
    dummy_inventory = object()
    dummy_variable_manager = object()

    plugin = CallbackModule(dummy_runner, dummy_inventory, dummy_variable_manager)
    plugin.v2_on_file_diff(one_result)

    # one_result._task is a mock
    one_result._task.loop = True
    plugin.v2_on_file_diff(one_result)

    # _result as a list

# Generated at 2022-06-13 11:42:21.847996
# Unit test for method v2_playbook_on_include of class CallbackModule
def test_CallbackModule_v2_playbook_on_include():
    msg = 'included: %s for %s' % (included_file._filename, ", ".join([h.name for h in included_file._hosts]))
    label = callbackModule._get_item_label(included_file._vars)
    if label:
        msg += " => (item=%s)" % label
    callbackModule._display.display(msg, color=C.COLOR_SKIP)


# Generated at 2022-06-13 11:42:29.698974
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    if __name__ == "__main__":
        obj = CallbackModule()

# Generated at 2022-06-13 11:42:34.390529
# Unit test for method v2_runner_item_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_item_on_failed():
    # Initiate instance of CallbackModule with verbosity
    C = CallbackModule(verbosity=50)
    # Initiate test result
    result = TestResult()
    # Initiate TestResult.value
    result.value = {}
    
    # Test with result.value equal to {'stderr': 'Test stderr'}
    result.value = {'stderr': 'Test stderr'}
    C.display_failed_stderr = True
    C.v2_runner_item_on_failed(result)
    
    # Test with result.value equal to None
    result.value = None
    C.v2_runner_item_on_failed(result)


# Generated at 2022-06-13 11:42:36.591166
# Unit test for method v2_playbook_on_play_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_play_start():
    c = CallbackModule()
    c.v2_playbook_on_play_start(None)
    return True


# Generated at 2022-06-13 11:42:38.670577
# Unit test for method v2_runner_on_start of class CallbackModule

# Generated at 2022-06-13 11:42:46.392787
# Unit test for method v2_runner_on_unreachable of class CallbackModule
def test_CallbackModule_v2_runner_on_unreachable():
    '''
    CallbackModule.v2_runner_on_unreachable
    '''
    logger = logging.getLogger(__name__)

    # set logging for this method
    logger.setLevel(logging.DEBUG)

    # Initialize callback and results
    callback = CallbackModule(display=Display())

    # set up some results
    results = dict(
        _task = 'AnsiblePlaybook',
        _host = 'localhost',
        _result = dict(
            msg = 'unreachable or unreachable',
            failed = False,
            changed = False,
            skipped = False,
        )
    )

    # Test no output
    callback.set_options(verbosity=0)
    callback.v2_runner_on_unreachable(results)

    # Test verbose output, expecting 1

# Generated at 2022-06-13 11:43:32.028901
# Unit test for method v2_runner_on_async_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_async_failed():
    class MockDisplay:
        def __init__(self):
            self.display_called = False
        def display(self, msg, color=None):
            self.display_called = True
            assert msg.startswith("ASYNC FAILED on ")

    class MockAsynchronousResult:
        def __init__(self):
            self.async_result = None
        def get_result(self):
            return self.async_result

    class MockHost:
        def __init__(self, hostname):
            self.hostname = hostname
        def get_name(self):
            return self.hostname

    class MockTaskResult:
        def __init__(self, hostname, async_result):
            self._host = MockHost(hostname)
            self._result = async_result


# Generated at 2022-06-13 11:43:41.087264
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    cb = CallbackModule()

# Generated at 2022-06-13 11:43:45.455103
# Unit test for method v2_runner_on_start of class CallbackModule
def test_CallbackModule_v2_runner_on_start():
    result1 = {
        
    }
    obj = CallbackModule()
    obj.v2_runner_on_start(host=result1)



# Generated at 2022-06-13 11:43:52.025037
# Unit test for method v2_runner_retry of class CallbackModule
def test_CallbackModule_v2_runner_retry():
    result = dict()
    result['task_name'] = 'Task Name'
    result['_host'] = 'Host Name'
    result['_result'] = dict()
    result['_result']['retries'] = 5
    result['_result']['attempts'] = 3
    cb_modl = CallbackModule()
    cb_modl.v2_runner_retry(result)

# Generated at 2022-06-13 11:43:52.691049
# Unit test for method v2_runner_on_start of class CallbackModule
def test_CallbackModule_v2_runner_on_start():
    pass

# Generated at 2022-06-13 11:43:56.108243
# Unit test for method v2_playbook_on_notify of class CallbackModule
def test_CallbackModule_v2_playbook_on_notify():
    instance = CallbackModule()
    handler = 'handler'
    host = 'host'
    expected = "NOTIFIED HANDLER handler for host"
    assert instance.v2_playbook_on_notify(handler, host) == expected


# Generated at 2022-06-13 11:44:03.995087
# Unit test for method v2_runner_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_on_skipped():
    kwargs = dict(
        display=mock.Mock(),
        display_skipped_hosts=True,
    )
    result = mock.Mock()
    result.task_name = 'task_name'
    result._result = dict(
        skipped=True,
    )
    result._host = dict(
        name='runner_on_skipped',
    )
    callback = CallbackModule(**kwargs)
    callback.v2_runner_on_skipped(result)
    assert kwargs['display'].display.call_count == 0


# Generated at 2022-06-13 11:44:12.588028
# Unit test for method set_options of class CallbackModule
def test_CallbackModule_set_options():
    d = {"verbosity": 3, "show_custom_stats": True, "check_mode_markers": True, "display_skipped_hosts": True, "display_ok_hosts": True}
    c = CallbackModule()
    c.set_options(d)
    assert c.verbosity == 3
    assert c.show_custom_stats
    assert c.check_mode_markers
    assert c.display_skipped_hosts
    assert c.display_ok_hosts


# Generated at 2022-06-13 11:44:19.342172
# Unit test for method v2_runner_on_async_poll of class CallbackModule
def test_CallbackModule_v2_runner_on_async_poll():
    # Test Cases
    callback = CallbackModule()
    result = type('', (), {
        '_host': type('', (), {
            'get_name': lambda: ''
        }),
        '_result': {
            'ansible_job_id': '',
            'finished': '',
            'started': ''
        }
    })()
    callback.v2_runner_on_async_poll(result)

# Generated at 2022-06-13 11:44:23.346284
# Unit test for method v2_playbook_on_play_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_play_start():
    test_callback_plugin = CallbackModule()
    test_play = Play()
    test_play.set_name("test-play")
    assert test_callback_plugin.v2_playbook_on_play_start(test_play) == None

# Generated at 2022-06-13 11:45:07.873716
# Unit test for method v2_runner_item_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_item_on_failed(): 
    # callback = CallbackModule()
    # result = ()
    # callback.v2_runner_item_on_failed(result)
    # Please, add some real tests
    pass

# Generated at 2022-06-13 11:45:13.787470
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    cb = CallbackModule()
    class SampleResult:
        def __init__(self):
            self._task = SampleTask()
            self._host = SampleHost()
            self._result = "V2_RUNNER_ON_OK"
            self._task._uuid = 'some-uuid'
    
    result = SampleResult()
    cb.v2_runner_on_ok(result)
    assert type(cb.display_ok_hosts) is bool


# Generated at 2022-06-13 11:45:25.236391
# Unit test for method v2_playbook_on_play_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_play_start():
    # mock objects that are passed as params
    play = Mock()
    play.get_name.return_value = "Mock Play"
    # mock objects used within the tested method
    MockDisplay = Mock()
    MockDisplay.banner = Mock()
    # mock this module and patching
    mock_module = Mock()
    mock_module.CallbackModule = type('CallbackModule', (object,), {
        "__init__": lambda x: None,
        "_display": MockDisplay
    })
    with patch.multiple(builtins, __name__="__main__", display=MockDisplay, CallbackModule=mock_module):
        import __main__ as main
        # initialize the class we are testing
        main.CallbackModule()
        # call the method we are testing
        main.CallbackModule().v2_playbook_on_play

# Generated at 2022-06-13 11:45:29.320815
# Unit test for method v2_playbook_on_play_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_play_start():
    playbook = Play()
    callback = CallbackModule()
    callback.v2_playbook_on_play_start(playbook)
    assert(callback._play is not None)
    assert(callback._play is not None)


# Generated at 2022-06-13 11:45:31.626642
# Unit test for method v2_playbook_on_stats of class CallbackModule
def test_CallbackModule_v2_playbook_on_stats():
    stats = {}
    cb = CallbackModule()
    cb.v2_playbook_on_stats(stats)

# Generated at 2022-06-13 11:45:42.359975
# Unit test for method v2_runner_item_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_item_on_skipped():
    c = CallbackModule({})
    res = Result()

# Generated at 2022-06-13 11:45:55.598995
# Unit test for method v2_runner_on_async_failed of class CallbackModule

# Generated at 2022-06-13 11:46:04.317308
# Unit test for method v2_playbook_on_stats of class CallbackModule
def test_CallbackModule_v2_playbook_on_stats():
    # Instantiate object
    cb_obj = CallbackModule()

    cb_obj.show_custom_stats = False
    cb_obj._display.verbosity = 2
    stats_obj = AnsibleCallbackStats()
    print(type(stats_obj))
    stats_obj.processed = {}
    stats_obj.processed['host1'] = {'failures':1, 'unreachable':1, 'ok':1, 'changed':1, 'skipped':1, 'rescued':1, 'ignored':1}
    stats_obj.custom = {}
    stats_obj.custom['host1'] = {'key1':1, 'key2':2}
    stats_obj.custom['_run'] = {'key1':1, 'key2':2}

    cb_obj.v2_

# Generated at 2022-06-13 11:46:17.515607
# Unit test for method v2_runner_item_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_item_on_failed():
    # Instantiate a module object
    test_module = CallbackModule()

    # Make sure we have a result object
    class Result:
        pass
    result = Result()

    # Make sure we have a task object
    class Task:
        pass
    task = Task()
    task.action = 'dummy'
    result._task = task

    # Create a test host
    class Host:
        def get_name(self):
            return 'localhost'
    host = Host()
    result._host = host

    # Create a test warning
    warning = { 'warning' : 'This is a test warning.' }

    # Create a test result
    result._result = dict(warnings = [])
    test_module.v2_runner_item_on_failed(result)

    # Add a warning

# Generated at 2022-06-13 11:46:27.169698
# Unit test for method v2_playbook_on_include of class CallbackModule
def test_CallbackModule_v2_playbook_on_include():
    template_dict = dict(
        x = 5,
        y = "somevalue",
        z = 10.1,
        s = "someOtherValue"
    )

    answer_dict = dict(
        x = 5,
        y = "somevalue",
        z = 10.1,
        s = "someOtherValue"
    )
    assert template_dict == answer_dict

    # create an instance of the Ansible callback module class to test
    callback = CallbackModule()
    # create an instance of the ansible included file class to test
    # we only want to test the v2_playbook_on_include method so we don't need to create a complete object
    included_file = object()
    # create a list of hosts to test
    included_file._hosts = ["host1", "host2", "host3"]

# Generated at 2022-06-13 11:47:50.742217
# Unit test for method set_options of class CallbackModule
def test_CallbackModule_set_options():
    # CallbackModule_set_options() => None
    # unit test for method set_options of class CallbackModule
    pass

# Generated at 2022-06-13 11:47:56.741668
# Unit test for method set_options of class CallbackModule
def test_CallbackModule_set_options():
    """
    Test set_options

    Test setting options of the CallbackModule class under various acceptible conditions
    """
    test_callback = CallbackModule()
    assert test_callback.set_options({'display_failed_stderr': True, 'display_skipped_hosts': True, 'display_ok_hosts': True, 'show_custom_stats': True}) is None

# Generated at 2022-06-13 11:48:00.518867
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    playbook = MagicMock()
    
    ansible_runner = CallbackModule()
    
    ansible_runner.v2_playbook_on_start(playbook)
    
    assert ansible_runner._display.banner.call_count == 1
    
# Unit tests for method _print_task_banner of class CallbackModule

# Generated at 2022-06-13 11:48:06.466569
# Unit test for method v2_runner_on_ok of class CallbackModule

# Generated at 2022-06-13 11:48:10.430334
# Unit test for method v2_runner_on_unreachable of class CallbackModule
def test_CallbackModule_v2_runner_on_unreachable():
    from ansible.plugins.callback.default import CallbackModule
    c = CallbackModule()
    c.v2_runner_on_unreachable(None)
    assert True



# Generated at 2022-06-13 11:48:21.734578
# Unit test for method v2_runner_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_on_skipped():
    cb = CallbackModule()
    result = {}
    fake_task = Factory.create_task(action='fake_action')
    result.update(task=fake_task, _task=fake_task, _result=dict(changed=False))
    cb.display_skipped_hosts = True
    assert cb.v2_runner_on_skipped(result) == None
    result.update(_result=dict(changed=True))
    cb.display_skipped_hosts = False
    assert cb.v2_runner_on_skipped(result) == None
    result.update(_result=dict(changed=False))
    cb.display_skipped_hosts = True
    assert cb.v2_runner_on_skipped(result) == None

# Generated at 2022-06-13 11:48:24.308800
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    CallbackModule.v2_playbook_on_start()
    assert CallbackModule.v2_playbook_on_start()._display.verbosity > 1


# Generated at 2022-06-13 11:48:31.686800
# Unit test for method v2_runner_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_on_skipped():
    from ansible.playbook.task import Task
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager

    loader = DataLoader()

# Generated at 2022-06-13 11:48:38.192188
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    global C
    C = ansible.utils.get_config(configfile=None, defaults=DEFAULTS)

    if sys.version_info >= (2, 7):
        from .compat27 import mock
    else:
        from .compat25 import mock

    from ansible.vars import VariableManager
    from ansible.parsing.vault import VaultLib
    from ansible.module_utils.six.moves import StringIO
    from ansible.utils.color import colorize, HostColor
    from ansible.module_utils._text import to_bytes
    from ansible.playbook.play_context import PlayContext

    v = VaultLib([])
    output = StringIO()
    play_context = PlayContext()


# Generated at 2022-06-13 11:48:41.265368
# Unit test for method v2_runner_on_async_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_async_ok():
    testCallbackModule = CallbackModule()
    assert testCallbackModule.v2_runner_on_async_ok("instance") == None