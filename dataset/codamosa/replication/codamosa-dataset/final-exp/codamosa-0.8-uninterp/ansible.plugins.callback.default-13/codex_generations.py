

# Generated at 2022-06-13 11:40:20.024547
# Unit test for method set_options of class CallbackModule
def test_CallbackModule_set_options():
    # Unit test for method set_options of class CallbackModule
    config = get_config(parse_cli=False)
    callback_module = CallbackModule()

    callback_module.set_options(config.get_plugin_options("callback"))

    assert callback_module.display_failed_stderr is False

# Generated at 2022-06-13 11:40:28.170376
# Unit test for method v2_runner_item_on_ok of class CallbackModule

# Generated at 2022-06-13 11:40:38.673836
# Unit test for method v2_playbook_on_play_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_play_start():
    # assert test with arguments that should pass
    test_args = [
        # format:
        # (positional_args, kwargs, expected_result)
        #
        # positional args are those that can be passed as-is.
        # kwargs are those that can be passed with a keyword.
        #
        # * check None arguments
        (
            [None],
            {},
            None
        ),
    ]
    for args, kwargs, expected_result in test_args:
        assert_equal(CallbackModule.v2_playbook_on_play_start(*args, **kwargs), expected_result)

# Generated at 2022-06-13 11:40:39.247940
# Unit test for method set_options of class CallbackModule
def test_CallbackModule_set_options():
    pass

# Generated at 2022-06-13 11:40:44.508884
# Unit test for method set_options of class CallbackModule
def test_CallbackModule_set_options():
    callback_module = CallbackModule()
    options = {"stdout_callback": "dummy", "show_custom_stats": "dummy", "display_skipped_hosts": "dummy", "display_failed_stderr": "dummy", "display_ok_hosts": "dummy", "verbosity": "dummy"}
    callback_module.set_options(options)
    assert callback_module._display.verbosity == 0


# Generated at 2022-06-13 11:40:55.306647
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    result = dict()
    result['_host'] = dict()
    result['_host']['get_name'] = lambda : 'host01.example.org'
    result['_task'] = dict()
    result['_task']['action'] = 'shell'
    result['_task']['no_log'] = False
    result['_task']['args'] = dict()
    result['_result'] = dict()
    result['_result']['stdout'] = ''
    result['_result']['stderr'] = ''
    result['_result']['cmd'] = ''
    result['_result']['rc'] = 0
    result['_result']['changed'] = False
    result['_result'] = dict()

# Generated at 2022-06-13 11:41:04.209944
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    display = Display()
    callback = CallbackModule(display)
    result = RunnerResult()
    result._task = Task()
    result._host = Host("host")
    result._result = {"changed": False}
    basic._ANSIBLE_ARGS = None
    stdout_backup = sys.stdout
    sys.stdout = io.StringIO()
    callback.v2_runner_on_ok(result)
    sys.stdout = stdout_backup
    assert not sys.stdout.getvalue()



# Generated at 2022-06-13 11:41:12.599913
# Unit test for method v2_runner_item_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_item_on_skipped():
    '''
    Unit test for method v2_runner_item_on_skipped of class CallbackModule
    '''
    # Create a mock object to contain the test result
    result = MagicMock()
    # Create a class so we can set some of the class variables
    mock_class = type('MockClass', (CallbackModule,), {'result': result})

    # Not sure why there is a space in the front of these strings
    #my_result = { 'stdout': '  stdout_message\n', 'stderr': '  stderr_message\n', 'rc': 0 }
    my_result = { 'stdout': '', 'stderr': '', 'rc': 0 }
    # Get the module instance
    my_module = mock_class()
    # Set some attributes
    my_module.display

# Generated at 2022-06-13 11:41:13.158467
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    pass

# Generated at 2022-06-13 11:41:15.672906
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    callback_module = CallbackModule()
    callback_module.v2_on_file_diff("result")
    callback_module.v2_on_file_diff("result")

# Generated at 2022-06-13 11:41:46.883915
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    mock_display = mock.MagicMock()
    mock_playbook = mock.MagicMock()
    adhoc_callbackmodule = CallbackModule(mock_display)
    adhoc_callbackmodule.show_custom_stats = False

    adhoc_callbackmodule.v2_playbook_on_start(mock_playbook)
    mock_playbook.assert_called_once()



# Generated at 2022-06-13 11:41:54.071172
# Unit test for method v2_runner_on_start of class CallbackModule
def test_CallbackModule_v2_runner_on_start():
    # Testing simple case
    test_object = CallbackModule()
    test_object._display.verbosity = 0
    test_object.show_custom_stats = False
    test_object.show_task_output = False
    test_object.nocolor = False
    test_object.display_failed_stderr = False
    test_object.display_skipped_hosts = False
    test_object.display_ok_hosts = False
    test_object._last_task_name = "check-cpu-usage"
    test_object._task_status_cache = {"check-cpu-usage":dict()}
    test_object._task_status_cache["check-cpu-usage"]["CHECK MODE"] = 0
    test_object._task_status_cache["check-cpu-usage"]["TASK"]

# Generated at 2022-06-13 11:42:09.046127
# Unit test for method v2_playbook_on_include of class CallbackModule
def test_CallbackModule_v2_playbook_on_include():
    # TODO: consider renaming to get_ansible_result
    def _get_ansible_result(task):
        try:
            return task._result
        except AttributeError:
            return None
    # TODO: consider renaming to get_ansible_task
    def _get_ansible_task(task):
        try:
            return task._task
        except AttributeError:
            return task

    # TODO: consider renaming get_ansible_result_field
    def _get_ansible_result_field(result, field):
        ansible_result = _get_ansible_result(result)
        if isinstance(result, dict):
            return result.get(field)
        if ansible_result is None:
            return None

# Generated at 2022-06-13 11:42:17.201913
# Unit test for method v2_runner_on_start of class CallbackModule
def test_CallbackModule_v2_runner_on_start():
    # Read input file
    original_stdout = sys.stdout
    sys.stdout = StringIO()
    test_input = open('./tests/input/v2_runner_on_start.json', 'r')
    test_input_content = test_input.read()
    
    # Create objects for test
    runner_result = RunnerResult() 
    runner_result_obj = json.loads(test_input_content)
    callback_module_obj = CallbackModule()
    
    # Run test
    runner_result.update(runner_result_obj, './tests/input/v2_runner_on_start.json')
    callback_module_obj.v2_runner_on_start(host=host, task=task)
    expected_stdout = sys.stdout
    sys.stdout = original

# Generated at 2022-06-13 11:42:26.526400
# Unit test for method v2_runner_retry of class CallbackModule
def test_CallbackModule_v2_runner_retry():
    from mock import Mock
    from collections import namedtuple
    from ansible.utils.color import stringc
    from ansible.plugins.callback.default import CallbackModule
    from ansible import constants as C
    cb = CallbackModule()
    cb._display.verbosity = 2
    cb._display.output = ''
    cb._display.colorize = stringc
    cb._display.columns = 80
    cb._display.display = Mock()
    result = namedtuple('Result', ('task_name', '_host', '_task', '_result', '_play'))
    host = namedtuple('Host', ('get_name', 'name'))
    result._host = host()
    result._task = None
    result._result = {'retries': 3, 'attempts': 1}

# Generated at 2022-06-13 11:42:31.158816
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    #Instantiate an object
    test_CallbackModule = CallbackModule()
    #Construct an object of class Result
    result = Result()
    #Call the method under test
    test_CallbackModule.v2_runner_on_ok(result)


# Generated at 2022-06-13 11:42:33.011585
# Unit test for method set_options of class CallbackModule
def test_CallbackModule_set_options():
  plugin=CallbackModule()
  assert plugin.set_options() == None


# Generated at 2022-06-13 11:42:38.173604
# Unit test for method v2_playbook_on_include of class CallbackModule
def test_CallbackModule_v2_playbook_on_include():
    included_file = Dict()
    included_file._filename = "filename1"
    included_file._hosts = ["host1", "host2"]

    module = CallbackModule()
    result = module.v2_playbook_on_include(included_file)

    assert result == None

if __name__ == '__main__':
    pytest.main(sys.argv[1:])

# Generated at 2022-06-13 11:42:48.266729
# Unit test for method v2_runner_item_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_item_on_failed():
    check_obj = CallbackModule()
    result = mock.Mock()
    result._task = mock.Mock()
    result._task.action = 'action'
    result._host = mock.Mock()
    result._host.get_name.return_value = 'host'
    result._result = {}
    result._result['changed'] = 'changed'
    result._result['stderr_lines'] = 'stderr_lines'
    result._result['msg'] = 'msg'
    result._result['warnings'] = 'warnings'
    result._result['results'] = 'results'
    context.CLIARGS = {'verbosity':5}
    state.output = {}
    check_obj.v2_runner_item_on_failed(result)

# Generated at 2022-06-13 11:42:49.512813
# Unit test for method v2_runner_on_async_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_async_ok():
    pass


# Generated at 2022-06-13 11:43:45.336782
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
  # Create a CallbackModule object and assign it to the var "callback_module"
  callback_module = CallbackModule()
  # Create a Result object and assign it to the var "result"
  result = Result()
  # Assign value to the _result attribute of the var "result"
  result._result = {'123': '456'}
  # Assign value to the _task attribute of the var "result"
  result._task = {'action': 'test_action'}
  # Execute the method v2_runner_on_ok
  callback_module.v2_runner_on_ok(result)



# Generated at 2022-06-13 11:43:54.640673
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    results1 = {'msg': 'i am the stdout'}
    results2 = {'msg': 'i am the stderr'}
    item1 = Mock(name='item1')
    item2 = Mock(name='item2')
    task1 = Mock(name='task1', action='action1', module_name='module1', no_log=False)
    task2 = Mock(name='task2', action='action2', module_name='module2', no_log=True)
    host1 = Mock(name='host1', get_name=Mock(return_value='name1'))
    host2 = Mock(name='host2', get_name=Mock(return_value='name2'))

# Generated at 2022-06-13 11:44:05.307775
# Unit test for method v2_runner_item_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_item_on_failed():
    # Passing mock object as the first parameter
    with patch.object(CallbackModule, 'get_option', return_value = True, autospec = True):
        # Passing mock object as the first parameter
        with patch.object(CallbackModule, 'host_label', return_value = True, autospec = True):
            # Passing mock object as the first parameter
            with patch.object(CallbackModule, '_run_is_verbose', return_value = True, autospec = True):
                result = MagicMock(spec = ['_task', '_host', '_result'])
                result.task_name = "test data"
                result._task = "test data"
                result._host = 'test data'
                result._result = {'invocation': {'module_name': 'setup', 'module_args': {}}}
                ansible_play

# Generated at 2022-06-13 11:44:11.464352
# Unit test for method v2_runner_item_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_item_on_ok():    
    # create an instance of the CallbackModule class
    cb = CallbackModule()

    # create an instance of the Result class
    result = Result(host=None, task=None, result={'changed': False}, _task_fields=['action'])
    result._task = object()
    result._task.action = 'setup'

    # invoke the v2_runner_item_on_ok method
    cb.v2_runner_item_on_ok(result)

    # check that the result has been captured
    assert isinstance(result, Result)
    assert result.host == None
    assert result.task == None
    assert result.result == {'changed': False}
    assert result._task_fields == ['action']
    assert result._task.action == 'setup'
    

# Generated at 2022-06-13 11:44:15.086110
# Unit test for method v2_playbook_on_play_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_play_start():
    module = CallbackModule()
    play = play_ds()
    module.v2_playbook_on_play_start(play)
    expected = u'PLAY'
    assert module.result == expected


# Generated at 2022-06-13 11:44:17.650847
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    c = CallbackModule()
    r = RunnerResult()
    c.v2_runner_on_failed(r)


# Generated at 2022-06-13 11:44:20.109559
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    testobj = CallbackModule()
    playbook = Mock()
    testobj.v2_playbook_on_start(playbook)

# Generated at 2022-06-13 11:44:27.321310
# Unit test for method v2_playbook_on_stats of class CallbackModule
def test_CallbackModule_v2_playbook_on_stats():
    # Testing data
    stats = Mock()

# Generated at 2022-06-13 11:44:38.911871
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    """
    Test method v2_on_file_diff() of class CallbackModule
    """

    # Init class
    CallbackModule_obj = CallbackModule(display=None)

    # Test default argument with valid value

# Generated at 2022-06-13 11:44:43.075013
# Unit test for method v2_playbook_on_stats of class CallbackModule
def test_CallbackModule_v2_playbook_on_stats():
    """
        Ansible callback plugin to summarize json output.
        """
    callback = CallbackModule()
    stats = False
    # call the method via a try block, as it might throw an exception
    try:
        callback.v2_playbook_on_stats(stats)
    except Exception:
        # check if the exception is expected
        assert True

# Generated at 2022-06-13 11:46:28.805790
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    runner_result = {'failed': False, 'changed': False}
    action = 'action'
    task = 'tasks'
    host = 'hosts'
    test = 'test'
    cm = CallbackModule()
    # This is how we set the attributes of the object.
    cm._last_task_banner = 1
    cm._last_task_name = 'task'
    cm._display = 'display'
    cm._task_type_cache = {'cache': 'cache'}
    cm._last_task_path = 'path'

    cm.v2_runner_on_ok('', runner_result)

    cm.v2_runner_on_ok(task, runner_result)

    cm.v2_runner_on_ok(task, action, host)

    cm.v2_runner_on

# Generated at 2022-06-13 11:46:32.058749
# Unit test for method v2_runner_on_start of class CallbackModule
def test_CallbackModule_v2_runner_on_start():
    # TODO: construct object for test
    with pytest.raises(NotImplementedError):
        CallbackModule().v2_runner_on_start(None, None)


# Generated at 2022-06-13 11:46:35.553023
# Unit test for method v2_runner_on_async_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_async_ok():
    '''test of method v2_runner_on_async_ok of class CallbackModule'''
    pass # TODO: implement your test here


# Generated at 2022-06-13 11:46:40.949466
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    print("test_CallbackModule_v2_playbook_on_start")
    # Test for
    # v2_playbook_on_start
    # Test for args
    # Test for no args
    # Test for verbosity > 1

    CallbackModule(None)
    print("Not implemented")



# Generated at 2022-06-13 11:46:49.946673
# Unit test for method v2_runner_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_on_skipped():
    from ansible_module_test import AnsibleModule
    from ansible.plugins.callback import CallbackBase
    from ansible.playbook.play import Play

    play = Play()
    play._hosts = 'hostname'
    play._tasks = dict()
    play._tasks["task_name"] = dict()
    play._tasks["task_name"]["action"] = "action_name"
    play._tasks["task_name"]["async_val"] = "async_val"
    play._tasks["task_name"]["async_jid"] = "async_jid"
    play._tasks["task_name"]["become"] = "become"
    play._tasks["task_name"]["become_method"] = "become_method"
    play

# Generated at 2022-06-13 11:46:53.102877
# Unit test for method v2_runner_item_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_item_on_failed():
    # Create instance of the class under test
    obj = CallbackModule()
    #TODO: replace with mock
    result = None

    # Call the method under test
    obj.v2_runner_item_on_failed(result)  # No error



# Generated at 2022-06-13 11:47:04.748018
# Unit test for method v2_playbook_on_stats of class CallbackModule
def test_CallbackModule_v2_playbook_on_stats():
    test_stats = Stats()
    test_play = Play()
    test_play.name = "test_play"
    test_play.hosts = [
        "test_host_0",
        "test_host_1",
        "test_host_2",
        "test_host_3",
        "test_host_4",
        "test_host_5",
        "test_host_6",
    ]
    test_play._variable_manager = VariableManager()
    test_play._variable_manager.extra_vars = {"ansible_check_mode":True}

# Generated at 2022-06-13 11:47:13.854192
# Unit test for method v2_runner_on_async_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_async_failed():
    # Create callback object
    callback_obj = CallbackModule()
    # Create fake result object
    result_obj = namedtuple('Result', ['_result', '_host'])
    # Create fake host object
    host_obj = namedtuple('Host', ['get_name'])
    # Set value of result object
    result_obj._result = {'ansible_job_id': 10, 'async_result': {'ansible_job_id': 8}}
    # Set value of host object
    host_obj.get_name.return_value = 'test_host'
    # Set value of result object
    result_obj._host = host_obj
    # Call method
    callback_obj.v2_runner_on_async_failed(result_obj)



# Generated at 2022-06-13 11:47:25.118254
# Unit test for method v2_runner_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_on_skipped():
    # We need a module so we can set up _last_task_banner and _last_task_name
    module = PlaybookResultsCollector()
    module._last_task_banner = None
    module._last_task_name = None

    # The Play need to have a name
    playbook = mock.MagicMock()
    playbook.get_name.return_value = 'PlayName'
    # The Task need to have a name
    task = mock.MagicMock()
    task.get_name.return_value = 'TaskName'

    # The Task need to have a name
    host = mock.MagicMock()
    host.get_name.return_value = 'hostname'

    # The Task need to have a name
    result = mock.MagicMock()
    result._host = host

# Generated at 2022-06-13 11:47:40.338767
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    #arrange
    import os
    import sys
    import pprint
    import ansible.constants as C
    from ansible.plugins.callback import CallbackModule
    from ansible.playbook.play_context import PlayContext
    from ansible.inventory.manager import InventoryManager
    from ansible import context
    from ansible.vars.manager import VariableManager

    result = {}
    result['playbook_returncode'] = 0
    result['playbook_cb'] = None
    result['playbook_cb_results'] = None

    basedir = './tests/'
    playbook = 'test_playbook.yml'
    inventory = './tests/test_inventory.ini'
    result['playbook_dir'] = os.path.dirname(os.path.abspath(playbook))