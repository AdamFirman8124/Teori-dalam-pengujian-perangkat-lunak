

# Generated at 2022-06-13 11:40:14.415940
# Unit test for method v2_runner_item_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_item_on_ok():
  pass

# Generated at 2022-06-13 11:40:23.142630
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    # Arrange
    result = MagicMock()
    result.task = MagicMock()
    result.task.loop = False
    result.result = {
        "changed": True,
        "diff": {
            "after": "new",
            "before": "old",
            "dst": "file",
            "src": "file"
        }
    }

    callback = CallbackModule()
    callback.get_option = MagicMock(return_value='somedir')
    callback.v2_playbook_on_task_start = MagicMock()
    callback.v2_playbook_on_play_start = MagicMock()
    callback.runner_on_ok = MagicMock()
    callback.runner_on_failed = MagicMock()
    callback.runner_on_unreachable = Magic

# Generated at 2022-06-13 11:40:25.241204
# Unit test for method v2_runner_item_on_skipped of class CallbackModule

# Generated at 2022-06-13 11:40:29.902589
# Unit test for method v2_runner_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_on_skipped():
    # Set up test
    runner_result = 'runner_result'
    instance = CallbackModule()

    # Check for no exception for the following call
    instance.v2_runner_on_skipped(runner_result)


# Generated at 2022-06-13 11:40:38.239266
# Unit test for method v2_runner_item_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_item_on_ok():
    _display = Display()
    _last_task_banner = None
    _play = None
    _task_type_cache = {}
    config = None
    display_skipped_hosts = True
    show_custom_stats = True
    check_mode_markers = True
    display_ok_hosts = True
    display_failed_stderr = True
    display = _display
    _last_task_name = None
    callback = CallbackModule(_display, _last_task_banner, _play, _task_type_cache,
                                                 config, display_skipped_hosts, show_custom_stats, check_mode_markers,
                                                 display_ok_hosts, display_failed_stderr, display, _last_task_name)

    v2_runner_item_on_

# Generated at 2022-06-13 11:40:39.703112
# Unit test for method v2_runner_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_on_skipped():
    cb = CallbackModule()
    result_obj = result.Result()
    cb.v2_runner_on_skipped(result_obj)

# Generated at 2022-06-13 11:40:51.822488
# Unit test for method v2_runner_item_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_item_on_ok():
    host = Mock()
    task = Mock()

    class Result:
        def __init__(self, host, task):
            self.host = host
            self.task = task

    result = Result(host, task)

    callbackModule = CallbackModule()
    callbackModule.get_option = Mock()
    callbackModule.v2_runner_item_on_ok(result)
    assert callbackModule.host_label.call_count == 1
    assert callbackModule._clean_results.call_count == 1
    assert callbackModule._get_item_label.call_count == 1
    assert callbackModule._run_is_verbose.call_count == 1
    assert callbackModule._dump_results.call_count == 1
    assert callbackModule._display.display.call_count == 1

# Generated at 2022-06-13 11:41:00.795281
# Unit test for method v2_runner_on_async_poll of class CallbackModule
def test_CallbackModule_v2_runner_on_async_poll():
    result = dict()
    result['_host'] = dict()
    result['_host']['get_name'] = lambda: 'DummyHost'
    result['_result'] = dict()
    result['_result']['ansible_job_id'] = 'DummyJid'
    result['_result']['started'] = 'DummyStarted'
    result['_result']['finished'] = 'DummyFinished'
    c = CallbackModule()
    c.v2_runner_on_async_poll(result)


# Generated at 2022-06-13 11:41:09.859891
# Unit test for method v2_runner_on_async_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_async_ok():
    # Instanciate a mock display
    display = Display()
    # Instanciate a mock result
    result = Result()
    # Instanciate a mock host
    host = Host()
    # Get the CallbackModule class
    callback = CallbackModule(display)
    # Call the v2_runner_on_async_ok method
    callback.v2_runner_on_async_ok(result)
    # Get the display value retuned by the method
    display_value = display.display_value
    # Test if display_value (the retuned value) is equal to the expected return
    assert display_value == 'ASYNC OK on mock_get_name: jid=mock_ansible_job_id'

# Generated at 2022-06-13 11:41:12.173474
# Unit test for method v2_runner_item_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_item_on_ok():
    import mock
    result = mock.MagicMock()
    callback = CallbackModule()
    # Assert that 
    assert callback.v2_runner_item_on_ok(result) == None

# Generated at 2022-06-13 11:41:37.357454
# Unit test for method v2_runner_item_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_item_on_skipped():
    _result = json.loads("""{
    "invocation": {
        "module_args": "nxos_static_route",
        "_ansible_verbose_always": true
    },
    "_ansible_parsed": true,
    "_ansible_item_result": true,
    "item": {
        "host": "host",
        "port": "port"
    },
    "_ansible_ignore_errors": null,
    "changed": false,
    "_ansible_no_log": false,
    "skipped": true,
    "msg": "skipped",
    "_ansible_item_label": "host",
    "failed": false
}""")


# Generated at 2022-06-13 11:41:49.426948
# Unit test for method v2_runner_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_on_skipped():
    if not os.path.exists(TEST_FILES):
        os.makedirs(TEST_FILES)
    cb = ansible_playbook_callback.CallbackModule()
    task = lambda: None
    task.display_skipped_hosts = True
    task.display_ok_hosts = True
    task.display_failed_stderr = True
    task.no_log = True
    cb._task = task
    cb.display_failed_stderr = True
    cb.display_ok_hosts = True
    cb.display_skipped_hosts = True
    cb.no_log = True
    cb.show_custom_stats = True
    cb.task_type_cache = {}
    cb.task_path_cache = {}
    cb

# Generated at 2022-06-13 11:41:52.642543
# Unit test for method v2_playbook_on_stats of class CallbackModule
def test_CallbackModule_v2_playbook_on_stats():
    cb = CallbackModule()

    stats = MagicMock()
    stats.custom = {}
    cb.v2_playbook_on_stats(stats)
    stats.custom = {'hosts': 'hosts'}
    cb.v2_playbook_on_stats(stats)



# Generated at 2022-06-13 11:42:02.433318
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    # Setup
    results = {
        'changed': False,
        'warnings': [],
    }
    description = 'description of thing'
    result = {'description': description, 'results': results}

# Generated at 2022-06-13 11:42:06.173868
# Unit test for method v2_runner_item_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_item_on_ok():
    # Set up expected results
    expected_msg = 'ok: [%s] => (item=None)' % (hostcolor(host, t, False))
    # Run the command to test
    result = CallbackModule.v2_runner_item_on_ok(result)
    # Check the output
    assert result == expected_msg

# Generated at 2022-06-13 11:42:10.246460
# Unit test for method v2_runner_on_start of class CallbackModule
def test_CallbackModule_v2_runner_on_start():
    args = dict(
        show_per_host_start=1,
    )
    p = MagicMock()
    t = MagicMock()
    h = MagicMock()
    callback = CallbackModule(p, **args)
    callback.get_option = MagicMock(return_value=True)
    callback.display = MagicMock()
    callback.v2_runner_on_start(h, t)
    callback.display.display.assert_called_with(' [started %s on %s]' % (t, h), color=C.COLOR_OK)

# Generated at 2022-06-13 11:42:18.200354
# Unit test for method v2_runner_item_on_skipped of class CallbackModule

# Generated at 2022-06-13 11:42:27.289907
# Unit test for method v2_runner_item_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_item_on_failed():
    host = 'test'
    hostname = "test_host"
    result = {
        "stderr": "test_error",
        "_host": host,
        "verbose_override": False,
        "msg": "test_msg",
        "results_file": "/home/test_user/ansible/logs/test_host/test_playbook_name/test_play_name/test_task_name.json"
    }
    
    runner = Mock()
    runner.exception.side_effect = Exception()
    
    task = Mock()
    task.action = 'test_action'
    task.verbose_always = False
    task._uuid = 'test_uuid'
    task.name = 'test_task_name'

# Generated at 2022-06-13 11:42:38.464302
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    my_mod = CallbackModule()

    # case 1
    result = MagicMock(spec=Result)
    result._host = 'host'
    result._task = 'task'
    result._result = {'rc': 0, 'stdout_lines': ['test'], 'stdout': 'test'}
    result._task.action = 'test_action'

    my_mod.display_ok_hosts = True
    my_mod.display_skipped_hosts = False
    my_mod._last_task_banner = '_last_task_banner'

    my_mod.v2_runner_on_ok(result)

    # case 2
    my_mod.display_ok_hosts = False

# Generated at 2022-06-13 11:42:43.918757
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    # Assign input parameters
    callback_module = CallbackModule()
    result = "''"

    # Actual Ansible execution
    try:
        callback_module.v2_on_file_diff(result)
    except SystemExit:
        pass

    # Expected Ansible results
    assert result == "\'\'\n"

# Generated at 2022-06-13 11:43:17.808583
# Unit test for method v2_runner_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_on_skipped():
    """
    CallbackModule.v2_runner_on_skipped()
    """
    # Setup test environment
    # Setup test fixtures
    runner_results = dict(
    )
    # Exercise test routine
    # Verify expected results
    # Cleanup test environment
    # Return test results


# Generated at 2022-06-13 11:43:26.518399
# Unit test for method v2_runner_on_async_poll of class CallbackModule
def test_CallbackModule_v2_runner_on_async_poll():
    """Test whether _display.display() is called when _display.verbosity is greater than 0."""
    global _display_display_calls

    _display = CallbackModuleTest._display
    _display.verbosity = 1

    # Test with _display.verbosity = 1
    _display_display_calls = 0
    cb = CallbackModule()
    result = CallbackModuleTest._result
    cb.v2_runner_on_async_poll(result)
    assert _display_display_calls == 1
    assert cb._last_task_banner is None
    assert cb._last_task_name is None

    _display.verbosity = 0
    _display_display_calls = 0
    cb = CallbackModule()
    result = CallbackModuleTest._result
    cb.v2

# Generated at 2022-06-13 11:43:32.875031
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.playbook.task import Task
    from ansible.playbook.play import Play
    from ansible.playbook.play_context import PlayContext
    from ansible.playbook.includer import Include
    from ansible.parsing.dataloader import DataLoader
    from ansible.inventory.manager import InventoryManager
    from ansible.vars.manager import VariableManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.executor.playbook_executor import PlaybookExecutor
    from ansible.plugins.callback import CallbackBase
    from ansible.plugins.loader import callback_loader
    import json
    import os
    import sys
    import unittest


# Generated at 2022-06-13 11:43:39.406956
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    playbook = FakePlaybook()
    playbook.set_file_name('FakePlaybook')
    callback_module = CallbackModule()
    callback_module.banner = MagicMock()
    callback_module.display = MagicMock()

    callback_module.v2_playbook_on_start(playbook)

    assert callback_module.display.banner.call_count == 1
    callback_module.display.banner.assert_called_with('PLAYBOOK: FakePlaybook')

    callback_module.display.call_count == 2
    callback_module.display.assert_called_with('Positional arguments: None', color=None, screen_only=True)



# Generated at 2022-06-13 11:43:44.555851
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    playbook = MagicMock()
    callbackModuleInstance = CallbackModule()
    callbackModuleInstance.v2_playbook_on_start(playbook)
    assert callbackModuleInstance._display.verbosity == 0


# Generated at 2022-06-13 11:43:54.022173
# Unit test for method v2_runner_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_on_skipped():
    my_vars = dict(
        ansible_check_mode=False,
        ansible_debug=False,
        ansible_verbosity=0,
        display_skipped_hosts=True,
        display_ok_hosts=True,
        use_verbose_descriptions=True,
        show_custom_stats=False,
        ansible_playbook_python=sys.executable,
        ansible_ssh_executable=None,
        ansible_config=None,
        ANSIBLE_FORCE_COLOR=True,
        stdout_callback = 'minimal',
    )
    my_inventory = InventoryManager(loader=DataLoader())
    my_results_callback = CallbackModule()
    my_results_callback.set_options(my_vars)
    my_results_callback.my

# Generated at 2022-06-13 11:44:02.883531
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    arguments = [
        {"diff": {"after": "", "before": ""}},
        {"diff": {"after": "", "before": ""}}]
    results = [
        {"changed": False},
        {"changed": True}]
    expected_calls = [
        call(arguments[0], results[0]),
        call(arguments[1], results[1])]
    exprected_params = [
        {"diff": "","verbosity":0},
        {"diff": "---\n+++\n@@ -1,2 +0,0 @@\n-\n-\n","verbosity":0}]

    mock_display = Mock()
    mock_display.verbosity = 0
    callback_module = CallbackModule(display=mock_display)
    mock_display.display.side_effect = callback_module

# Generated at 2022-06-13 11:44:05.140491
# Unit test for method v2_runner_on_unreachable of class CallbackModule
def test_CallbackModule_v2_runner_on_unreachable():
    cb = CallbackModule()
    cb.v2_runner_on_unreachable(None)


# Generated at 2022-06-13 11:44:18.111404
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # Set up test objects
    task = AnsibleTask('dummy_task')
    result = AnsibleResult(host={}, task=task, task_fields={}, task_result={})
    test_callback_module = CallbackModule(display=AnsibleDisplay(verbosity=1, log_only=False, log_path=None))

    # Expected output should include display message containing the host label,
    # task name, and the task result
    test_output = StringIO()
    with redirect_stdout(test_output):
        test_callback_module.v2_runner_on_failed(result=result)

    captured_output = test_output.getvalue().strip()
    assert 'failed:' in captured_output
    assert captured_output.endswith(str(result._result))



# Generated at 2022-06-13 11:44:18.833892
# Unit test for method v2_playbook_on_stats of class CallbackModule
def test_CallbackModule_v2_playbook_on_stats():
    pass

# Generated at 2022-06-13 11:44:53.664927
# Unit test for method set_options of class CallbackModule
def test_CallbackModule_set_options():
    c = CallbackModule()
    c.set_options(show_custom_stats = False, display_skipped_hosts = False, display_ok_hosts = False,show_per_host_start = False)


# Generated at 2022-06-13 11:44:58.183994
# Unit test for method v2_playbook_on_include of class CallbackModule
def test_CallbackModule_v2_playbook_on_include():
    # Define test object
    options = {'show_custom_stats': True, 'verbosity': 0}
    callback = CallbackModule(display=None, options=options)

    # Define test data
    stats = {'_run': {'my_var': 'my_value'}}

    # Execute method
    callback.v2_playbook_on_stats(stats)


# Generated at 2022-06-13 11:45:05.384517
# Unit test for method v2_playbook_on_notify of class CallbackModule
def test_CallbackModule_v2_playbook_on_notify():
    import ansible.plugins.callback.default
    import ansible.playbook.task
    class Empty(object):
        def __init__(self):
            pass

    m = ansible.plugins.callback.default.CallbackModule()
    m._display = Empty()
    m._display.display = Empty()
    m._display.display.verbosity = 4
    m._display.display.verbosity = 5
    handler = ansible.playbook.task.Handler()
    handler.get_name = Empty()
    handler.get_name.return_value = 'this.is.a.name'
    host = 'host'
    m.v2_playbook_on_notify(handler, host)



# Generated at 2022-06-13 11:45:14.455172
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    display = lambda *args: None
    cb = CallbackModule(display)
    task = lambda *args: None
    task.action = 'setup'
    cb.v2_runner_on_ok(Result(Host(name='1.1.1.1'), task, {}))
    cb.v2_runner_on_ok(Result(Host(name='1.1.1.1'), task, {'changed': True}))
    cb.v2_runner_on_ok(Result(Host(name='1.1.1.1'), task, {'changed': False}))
    cb.v2_runner_on_ok(Result(Host(name='1.1.1.1'), task, {'changed': True}))
    task.action = 'shell'
    cb.v2_runner_

# Generated at 2022-06-13 11:45:15.871145
# Unit test for method set_options of class CallbackModule
def test_CallbackModule_set_options():
    # TODO: Implement tests for set_options
    pass


# Generated at 2022-06-13 11:45:27.017080
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    from ansible.playbook.task import Task
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import merge_hash

    # instantiate our result object
    result = Result(task=Task(), host=Host('localhost'))

    # instantiate our inventory, just enough to build the variable manager
    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=[])
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # give the result a state

# Generated at 2022-06-13 11:45:34.991760
# Unit test for method set_options of class CallbackModule
def test_CallbackModule_set_options():
    """
    Make sure that no exception will be raised
    when we set callback option using this method
    """
    my_callback = CallbackModule()
    my_callback.set_options({
        'some_option': True,
        'some_other_option': ['ololo', 'trololo']
    })
    assert isinstance(my_callback.some_option, bool)
    assert isinstance(my_callback.some_other_option, list)


# Generated at 2022-06-13 11:45:44.110058
# Unit test for method v2_runner_item_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_item_on_failed():
    # Initialize context
    context._init_global_context(load_plugins=False)
    context.CLIARGS = ImmutableDict(connection='ssh')
    context.C.DEFAULT_MODULE_NAME = 'command'

    # Initialize display
    display = Display()
    display.verbosity = 2

    # Instantiate callback module
    cb_plugin = CallbackModule(display)

    # Initialize vars
    host = Host('127.0.0.1')
    host.name = '127.0.0.1'
    task = Task()
    task.action = 'debug'
    task.no_log = False
    task.args = {'msg': u'Hello World!'}
    task._role_name = 'debug'
    unresolved = dict(failed=False, msg='Hello World!')

# Generated at 2022-06-13 11:45:56.795669
# Unit test for method v2_runner_on_async_poll of class CallbackModule
def test_CallbackModule_v2_runner_on_async_poll():
    import json
    import os
    import tempfile
    import yaml
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    # test setup
    tempdir = tempfile.gettempdir()
    test_dir = os.path.join(tempdir, 'ansible_test')
    if os.path.isdir(test_dir):
        shutil.rmtree(test_dir)
    os.mkdir(test_dir)
    os.chdir(test_dir)

    # create Ansible inventory

# Generated at 2022-06-13 11:45:59.036775
# Unit test for method v2_runner_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_on_skipped():
    m = CallbackModule()
    assert m._get_item_label("STOP") == "START"


# Generated at 2022-06-13 11:46:36.071941
# Unit test for method v2_runner_item_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_item_on_ok():
    # create instance of the object to test.
    obj = CallbackModule()
    # create mock for 'host_label' method of the object.
    # required arguments are created automatically
    mock_host_label = create_autospec(obj.host_label, return_value='host_label')
    obj.host_label = mock_host_label
    # create mock for '_get_item_label' method of the object.
    # required arguments are created automatically
    mock__get_item_label = create_autospec(obj._get_item_label, return_value='_get_item_label')
    obj._get_item_label = mock__get_item_label
    # create mock for '_clean_results' method of the object.
    # required arguments are created automatically
    mock__clean_results = create_autos

# Generated at 2022-06-13 11:46:46.614394
# Unit test for method v2_playbook_on_play_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_play_start():
    C.BECOME_METHODS = ['fake', 'sudo', 'su', 'pbrun', 'pfexec', 'runas', 'dzdo']
    ansible_vars = {u'var1': u'value1', u'var2': [u'value1', u'value2']}
    host = FakeHost(name='myfakehost')
    task = FakeTask(name='myfaketask')
    block = FakeBlock()
    block._uuid = 'fakeuuid'
    block.get_name.return_value = 'fakeblock'
    play = FakePlay()
    play._uuid = 'fakeuuid2'
    play.get_name.return_value = 'fakeplay'
    play.hosts = [host]
    play.name = 'fakeplay'
    play.get_

# Generated at 2022-06-13 11:46:47.995289
# Unit test for method v2_playbook_on_notify of class CallbackModule
def test_CallbackModule_v2_playbook_on_notify():
    assert False, "Test not implemented"

# Generated at 2022-06-13 11:46:55.725815
# Unit test for method v2_runner_on_start of class CallbackModule
def test_CallbackModule_v2_runner_on_start():
   # test case 1
   mock_host = Mock()
   mock_task = Mock()
   mock_self = Mock()
   mock_self.get_option = Mock(return_value=True)
   mock_self.task_type_cache = {}
   mock_self._last_task_banner = -1
   mock_self._last_task_name = None
   mock_self._task_type_cache = {}
   mock_self._play = {}
   mock_self.play = {}
   mock_self.play.hostvars = {}
   mock_self.play.hostvars.get = {}
   mock_self.play.hostvars.get.return_value = {}
   mock_self._display = Mock()
   mock_self._display.columns = {}

# Generated at 2022-06-13 11:47:06.706691
# Unit test for method v2_runner_item_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_item_on_skipped():
    skip_message="message for skipped"
    play_context=PlayContext()
    task=Task()
    task.action="Set"

# Generated at 2022-06-13 11:47:15.554114
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    result_ = CallbackModule() 
    result_._dump_results = MagicMock(name='_dump_results')
    result_._dump_results.return_value = 'foo'
    result_._handle_warnings = MagicMock(name='_handle_warnings')
    result_._display = CallbackModule() 
    result_._display.display = MagicMock(name='_display.display')
    result_._clean_results = MagicMock(name='_clean_results')
    result_._handle_exception = MagicMock(name='_handle_exception')
    result_._run_is_verbose = MagicMock(name='_run_is_verbose')
    result_._run_is_verbose.return_value = False
    result = Mock()

# Generated at 2022-06-13 11:47:18.396041
# Unit test for method v2_runner_on_unreachable of class CallbackModule
def test_CallbackModule_v2_runner_on_unreachable():
    callback = CallbackModule()
    item = FileTransfer()
    callback.v2_runner_on_unreachable(item)


# Generated at 2022-06-13 11:47:27.711545
# Unit test for method v2_runner_item_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_item_on_skipped():
    # Testing all of output with
    # assert_equal (which is not recommended)
    # is slow, so we test only one line

    # For testing we modify the output methods to
    # store the results in an array instead of printing
    class PrintBuffer():
        '''PrintBuffer class used to test output of CallbackModule'''
        def __init__(self):
            self.output_array = []

        def display(self, output, **kwargs):
            self.output_array.append(output)

        def banner(self, banner):
            self.output_array.append(banner)

    mod = CallbackModule()
    mod.display = PrintBuffer()

    # Some required vars to pass tests
    task = Task()
    task.name = 'A name'
    task._uuid = 'A uuid'

   

# Generated at 2022-06-13 11:47:32.738773
# Unit test for method v2_runner_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_on_skipped():
    # Test failure of the method 'v2_runner_on_skipped'
    # of class 'CallbackModule'
    c = CallbackModule()
    c.display_skipped_hosts = False
    c.reset_task_cache()
    res = dict(host=dict(name='host1', tasks=[]), task=dict(name='task1', action='action1'))
    c.v2_runner_on_skipped(res)

# Generated at 2022-06-13 11:47:38.465960
# Unit test for method v2_runner_item_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_item_on_skipped():

    module = CallbackModule()

    result = MagicMock()
    module.display_ok_hosts = True
    module.v2_runner_item_on_skipped(result)
    assert module.display_ok_hosts == True

    result = MagicMock()
    module.display_ok_hosts = False
    module.v2_runner_item_on_skipped(result)
    assert module.display_ok_hosts == False


# Generated at 2022-06-13 11:48:45.794701
# Unit test for method v2_runner_on_start of class CallbackModule
def test_CallbackModule_v2_runner_on_start():
    pass

# Generated at 2022-06-13 11:48:49.163113
# Unit test for method v2_playbook_on_stats of class CallbackModule
def test_CallbackModule_v2_playbook_on_stats():
    stats = mock.Mock()
    callback = CallbackModule()
    callback.v2_playbook_on_stats(stats)


# Generated at 2022-06-13 11:48:58.406822
# Unit test for method v2_runner_on_unreachable of class CallbackModule
def test_CallbackModule_v2_runner_on_unreachable():
    runner = unittest.mock.Mock()
    runner._task = unittest.mock.Mock()
    runner._task.run_state = 'ok'
    runner._task.__class__ = Task
    runner._host = unittest.mock.Mock()
    runner._host.get_name.return_value = "hostname"
    runner._host.name = "hostname"
    runner._host.__class__ = Host
    result = unittest.mock.Mock()
    result._result = "result"
    result.task_name = "task_name"

    display = unittest.mock.Mock()

    callback = CallbackModule()
    callback._last_task_banner = "last_task_banner"

# Generated at 2022-06-13 11:49:00.767182
# Unit test for method v2_runner_item_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_item_on_ok():
    module = CallbackModule()
    assert module.v2_runner_item_on_ok(None) == None


# Generated at 2022-06-13 11:49:08.571709
# Unit test for method v2_runner_item_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_item_on_skipped():
    script_dir = os.path.dirname(__file__)
    data_file = os.path.join(script_dir, 'data/tmp_data')
    handler = CallbackModule()
    result = AnsibleResult(None, None, None)
    result._host = FakeHost("testhost")
    result._task = FakeTask("testtask")
    result._result.update({"_ansible_no_log": False, "exception": False, "module_stdout": "", "module_stderr": "", "msg": "", "rc": 0})
    handler.display_skipped_hosts = False
    handler.v2_runner_item_on_skipped(result)
    assert os.path.isfile(data_file) == False
    handler.display_skipped_hosts = True
   

# Generated at 2022-06-13 11:49:18.411699
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    _host = Mock()
    _host.get_name.return_value = 'test.invalid'
    _result = Mock()
    _result._task = Mock()
    _result._task.loop = True
    _result._result = {
        'changed': True,
        'results': [{
            'diff': {
                'after': 'new test text',
                'before': 'old test text'
            }
        }]
    }
    _result._task.no_log = True

    # Call module method
    callback_module = CallbackModule()
    callback_module.v2_on_file_diff(_result)



# Generated at 2022-06-13 11:49:27.295351
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    from ansible.plugins.callback import CallbackModule
    from ansible.vars import VariableManager
    from ansible.inventory import Inventory
    from ansible.parsing.dataloader import DataLoader

    context._init_global_context(playbook_dir='/home/ansible/playbook/')
    cb = CallbackModule()
    cb._display.verbosity=1
    cb._options = {'display_skipped_hosts': False}
    cb.host_label = lambda x: 'host_id'
    cb._run_is_verbose = lambda x: True
    cb.display_ok_hosts = True

    cb.v2_playbook_on_task_start(None, test_task_name)
    result = Result('role_x', 'role_x')

# Generated at 2022-06-13 11:49:30.159480
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    callback = CallbackModule()
    result = Mock()
    result._result = {True}
    result._host.get_name.return_value = 'TestHost'
    callback.v2_runner_on_failed(result)

# Generated at 2022-06-13 11:49:30.947014
# Unit test for method set_options of class CallbackModule
def test_CallbackModule_set_options():
    pass

# Generated at 2022-06-13 11:49:34.778378
# Unit test for method v2_playbook_on_stats of class CallbackModule
def test_CallbackModule_v2_playbook_on_stats():
    # create a fixture of CallbackModule
    my_object = CallbackModule()
    # set up a PlayStats object
    stats = PlayStats()
    stats.processed['somehost'] = 12
    # do the test
    my_object.v2_playbook_on_stats(stats)