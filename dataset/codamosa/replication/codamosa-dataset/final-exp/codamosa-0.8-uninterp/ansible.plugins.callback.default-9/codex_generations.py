

# Generated at 2022-06-13 11:40:18.362758
# Unit test for method v2_runner_on_async_poll of class CallbackModule
def test_CallbackModule_v2_runner_on_async_poll():
    """
    Test case for ``CallbackModule.v2_runner_on_async_poll``.

    """
    obj = CallbackModule()
    result = mock_result()
    obj.v2_runner_on_async_poll(result)


# Generated at 2022-06-13 11:40:26.655800
# Unit test for method v2_runner_on_unreachable of class CallbackModule
def test_CallbackModule_v2_runner_on_unreachable():
    """
    Test v2_runner_on_unreachable method
    """
    callback = CallbackModule()

    # Test with result._host set on result
    host = Host()
    result = Result(host)

    # Test with result._task.action set to 'GATHER FACTS'
    result._task.action = 'GATHER FACTS'
    callback.v2_runner_on_unreachable(result)

    # Test with result._task.action set to 'TEST'
    result._task.action = 'TEST'
    callback.v2_runner_on_unreachable(result)

    # Test with result._task.action set to 'TEST_2'
    result._task.action = 'TEST_2'
    callback.v2_runner_on_unreachable(result)

    # Test

# Generated at 2022-06-13 11:40:35.313665
# Unit test for method v2_playbook_on_play_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_play_start():
    import unittest2 as unittest
    from ansible.module_utils.six.moves import StringIO
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task import TaskInclude
    from ansible.parsing.mod_args import ModuleArgsParser
    from ansible.executor.task_result import TaskResult
    from ansible.executor.process.result import ResultProcessor
    from ansible.plugins.callback.human_log import CallbackModule
    from ansible.utils.color import stringc
    
    class TestCallbackModule(unittest.TestCase):

        def setUp(self):
            pass

        def tearDown(self):
            pass


# Generated at 2022-06-13 11:40:38.466800
# Unit test for method v2_runner_on_async_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_async_failed():
    result = {'ansible_job_id': 123}
    callback = CallbackModule()
    callback.v2_runner_on_async_failed(result)


# Generated at 2022-06-13 11:40:40.660607
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    os.chdir('../')
    fake_callback = CallbackModule()
    fake_ansible_playbook = FakeAnsiblePlaybook()
    fake_callback.v2_playbook_on_start(fake_ansible_playbook)
    assert fake_ansible_playbook

# Generated at 2022-06-13 11:40:52.011230
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    playbook_path=get_cur_dir()+'/data/ansible/test_result_analyse_playbook.yml'
    # 2.测试 v2_playbook_on_start函数的输出
    bkObj= CallbackModule()
    bkObj.v2_playbook_on_start(playbook_path)
    bkObj.v2_playbook_on_stats({})
    bkObj.v2_playbook_on_start(playbook_path)
    bkObj.v2_playbook_on_play_start('play')
    bkObj.v2_playbook_on_cleanup_task_start('play')
    bkObj.v2_playbook_on_handler_task_start('play')


# Generated at 2022-06-13 11:40:58.968786
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():

    # initialize
    cb = CallbackModule()

    # args is just a dummy
    args = True
    result = 'result'
    result._task = 'task'
    result._task.action = 'action'
    result._task._uuid = 'uuid'
    result._host = 'host'

    # call method
    cb.v2_runner_on_failed(result=result)

    # check output!


# Generated at 2022-06-13 11:41:09.473162
# Unit test for method v2_runner_item_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_item_on_failed():
    from unittest.mock import call
    from jinja2.exceptions import UndefinedError
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task

    callback = CallbackModule()
    result = dict(invocation=dict(module_args=dict(path="file.txt")))
    result["_ansible_verbose_always"] = True
    result["_ansible_fail_on_undefined"] = False
    result["exception"] = UndefinedError("error")
    result["warnings"] = []
    result["changed"] = False

# Generated at 2022-06-13 11:41:16.065069
# Unit test for method v2_runner_on_async_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_async_failed():
    # Set up test objects
    host = Host(name="localhost")
    result = Result(host=host, task=Task(), task_result=dict(ansible_job_id="1234567890"))
    callback = CallbackModule()

    # Test
    callback.v2_runner_on_async_failed(result)

    # Check
    assert "ASYNC FAILED on localhost: jid=1234567890" in callback.callback_buffer
    assert "color=1" in callback.callback_buffer


# Generated at 2022-06-13 11:41:20.270617
# Unit test for method v2_runner_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_on_skipped():
    cb = CallbackModule()
    stats = {"unreachable": 1, "failures": 1, "ok": 1, "skipped": 1,
             "changed": 1, "ignored": 1, "rescued": 1, "dark": {}}
    cb.v2_playbook_on_stats(stats)
    assert stats == 1


# Generated at 2022-06-13 11:41:45.609061
# Unit test for method v2_runner_item_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_item_on_skipped():
    # Test with short connection
    #runner = Runner(host_list=['127.0.0.1'], private_key_file=PRIVATE_KEY_FILE, become=True, verbosity=0)
    #runner.run(task=dict(action=dict(module='shell', args='ls'), register='shell_out'),
    #           play_context=PlayContext(check_conditional_items=True))
    pass

# Generated at 2022-06-13 11:41:48.903050
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    fake_task = Task(Mock(),Mock(),Mock())
    fake_result = Result(Mock(),Mock(),Mock())
    fake_result.task = fake_task
    fake_result.task_name = 'fake_task_name'
    fake_result._result = 'fake_result'
    ansible_playbook_callback = AnsiblePlaybookCallback()
    ansible_playbook_callback.v2_runner_on_ok(fake_result)


# Generated at 2022-06-13 11:41:52.644469
# Unit test for method set_options of class CallbackModule
def test_CallbackModule_set_options():

    # test1: unit test for method set_options
    # initialize the callback module
    options = {'display_skipped_hosts': True}
    cm = CallbackModule(display=None, options=options)

    # invoke the method
    cm.set_options(options)
    assert cm.display_skipped_hosts is True
    return True

# Generated at 2022-06-13 11:42:02.433159
# Unit test for method v2_on_file_diff of class CallbackModule
def test_CallbackModule_v2_on_file_diff():
    # Create an instance of CallbackModule
    cb = CallbackModule()
    result = {}
    result['_task'] = {}
    result['_task']['loop'] = False
    result['_result'] = {}
    result['_result']['diff'] = {}
    result['_result']['diff']['after'] = 'test'
    result['_result']['diff']['before'] = 'test'
    result['_result']['changed'] = True
    cb.v2_on_file_diff(result)

    # unit test for v2_on_file_diff with loop
    result['_task']['loop'] = True

# Generated at 2022-06-13 11:42:06.121020
# Unit test for method v2_runner_retry of class CallbackModule
def test_CallbackModule_v2_runner_retry():
    module_name = "..ansible.plugins.callback.default.CallbackModule"
    cb_module = callbacks.CallbackModule(None, None, None, None)
    result = callbacks.CallbackModule(None, None, None, None).v2_runner_retry(result)
    print(result)


# Generated at 2022-06-13 11:42:12.116911
# Unit test for method v2_runner_retry of class CallbackModule
def test_CallbackModule_v2_runner_retry():
    from ansible.utils.display import Display
    from ansible.plugins.callback import CallbackBase
    from ansible.vars.manager import VariableManager
    from ansible.vars.hostvars import HostVars
    from ansible.vars.hostvars import HostVarsVars
    from ansible.vars.unsafe_proxy import UnsafeProxy
    from ansible.module_utils.six import PY2, PY36, with_metaclass
    from abc import ABCMeta
    import collections

    class HostVarsVars(collections.Mapping):
        def __len__(self):
            return 2

        def __iter__(self):
            return iter(['default', 'vars'])

        def __getitem__(self, item):
            return item


# Generated at 2022-06-13 11:42:14.876963
# Unit test for method v2_playbook_on_include of class CallbackModule
def test_CallbackModule_v2_playbook_on_include():
    self = CallbackModule()
    included_file = object()

    result = self.v2_playbook_on_include(included_file)


# Generated at 2022-06-13 11:42:21.306090
# Unit test for method v2_runner_item_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_item_on_skipped():
    runner_item_on_skipped = CallbackModule()
    # mock_result
    mock_result = MagicMock()

    # mock_result._host
    mock_result._host = MagicMock()
    mock_result._host.get_name.return_value = 'some_host'

    # mock_result._task
    mock_result._task = MagicMock()
    mock_result._task.action = 'some action'

    runner_item_on_skipped.v2_runner_item_on_skipped(mock_result)

    # assert that the action executed in v2_runner_item_on_skipped(result) is expected



# Generated at 2022-06-13 11:42:29.364334
# Unit test for method v2_runner_item_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_item_on_ok():

    mocked_result = MagicMock()
    mocked_result.task_name = "Test task"
    mocked_result._host = "Test host"
    mocked_result._result = {
        'changed': False,
    }
    mocked_result._task = MagicMock()
    mocked_result._task.action = 'test'
    mocked_result._task._uuid = '1234567890'

    ansible_run = CallbackModule()
    ansible_run.display_failed_stderr = False
    ansible_run._last_task_banner = ''
    ansible_run.get_option = MagicMock(return_value=True)
    ansible_run.display_ok_hosts = True
    ansible_run._display.verbosity = 1
    ansible_run._clean_results = Magic

# Generated at 2022-06-13 11:42:39.529867
# Unit test for method v2_runner_retry of class CallbackModule
def test_CallbackModule_v2_runner_retry():
    callback = CallbackModule()
    task = Mock()

# Generated at 2022-06-13 11:43:25.713297
# Unit test for method v2_runner_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_on_skipped():
    from ansible.playbook.play import Play
    from ansible.playbook.task import Task
    from ansible.playbook.task.include import TaskInclude

    hostname = 'my-host'
    task_uuid = 'uuid'
    result = {'ansible_facts': {'current_time': '2018-01-12 13:22:30.057791'}, 'changed': False}
    task = Task()
    task.action = 'shell'
    task.args = {}
    task._uuid = task_uuid
    task.loop = False
    play = Play()
    play.hosts = [hostname]
    play.name = 'my-play'
    tn = 'my-task'
    task.set_loader(None)
    task.name = tn

# Generated at 2022-06-13 11:43:28.221146
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    playbook = CallbackModule('colorized',display=Display())
    playbook.v2_playbook_on_start(playbook)
    

# Generated at 2022-06-13 11:43:37.205981
# Unit test for method set_options of class CallbackModule
def test_CallbackModule_set_options():
    from ansible.utils.color import stringc
    import sys
    import io
    import contextlib

    @contextlib.contextmanager
    def captured_output():
        new_out, new_err = io.StringIO(), io.StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err


# Generated at 2022-06-13 11:43:41.332628
# Unit test for method v2_runner_retry of class CallbackModule
def test_CallbackModule_v2_runner_retry():
    module = CallbackModule()
    result = Mock(spec=Result)
    result.task_name = ''
    result._result = {'attempts': 0, 'retries': 0}
    result._task = 'test_task_name'
    result._host = 'test_host'
    module.v2_runner_retry(result)

# Generated at 2022-06-13 11:43:48.356488
# Unit test for method v2_runner_item_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_item_on_skipped():
    import os
    import sys
    import tempfile
    import shutil
    import json
    import yaml

    path = os.path.dirname(os.path.realpath(__file__))
    sys.path.insert(0, path)

    from ansible import constants as C

    results_dir = tempfile.mkdtemp()
    results_file = os.path.join(results_dir, 'results.yml')

    task_uuid = '4'
    last_task_banner = '3'
    task_name = 'foo'
    vars = {'baz': 'bat'}

    result = _create_result('1.1.1.1', task_uuid)
    result['ansible_job_id'] = '12345.12'


# Generated at 2022-06-13 11:43:59.676560
# Unit test for method v2_runner_retry of class CallbackModule
def test_CallbackModule_v2_runner_retry():
    c = CallbackModule()
    c.display = Display()
    c.display.verbosity = 2
    ansi_escape = re.compile(r'\x1b[^m]*m')
    result = Mock()
    result.task_name = 'task_name'
    result._task = 'some_task'
    result.result_template = {'retries': 5, 'attempts': 1}

    def reset_attempts():
        result.result_template['attempts'] = 0

    result.result_template_copy = reset_attempts
    for i in range(5):
        result.result_template['attempts'] += 1
        c.v2_runner_retry(result)

# Generated at 2022-06-13 11:44:07.852850
# Unit test for method v2_runner_on_async_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_async_failed():
    result = get_mock_result()
    result.results_file = None
    result.start_line = 0
    result.end_line = 0

# Generated at 2022-06-13 11:44:20.430392
# Unit test for method v2_runner_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_on_ok():
    runner = Runner()
    task = Task(name='test_CallbackModule_v2_runner_on_ok')
    task.action = 'setup'
    task.no_log = False
    task.loop = False
    task.args = {}
    task.check_mode = False
    task.notify = ()
    task.when = True
    task.run_once = False
    task._uuid = '924a9e6c'
    result = Result(host=Host(name='host'), task=task)

# Generated at 2022-06-13 11:44:29.690336
# Unit test for method v2_playbook_on_play_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_play_start():
    from ansible.playbook.task import Task
    from ansible.playbook.task_include import TaskInclude
    from ansible.playbook import Playbook
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.callback import CallbackBase
    # The following tests require setting an env variable (ANSIBLE_HOST_KEY_CHECKING) that is unique to the tests.
    # Set the env variable below to False so we don't get a false positive result
    # when running these tests.
    os.environ['ANSIBLE_HOST_KEY_CHECKING'] = 'False'
    # Test Case 1 of v2

# Generated at 2022-06-13 11:44:33.530928
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
    # Create an instance of CallbackModule with default values
    callback_plugin_instance = CallbackModule()
    # Check the correct return
    assert callback_plugin_instance.v2_playbook_on_start(playbook=None) is None


# Generated at 2022-06-13 11:45:48.829122
# Unit test for method v2_runner_on_unreachable of class CallbackModule
def test_CallbackModule_v2_runner_on_unreachable():
    pass

# Generated at 2022-06-13 11:46:01.336928
# Unit test for method v2_runner_retry of class CallbackModule
def test_CallbackModule_v2_runner_retry():
    mock_result_get_name = mocker.patch('ansible.plugins.callback.CallbackBase.v2_runner_retry', new_callable=mocker.MagicMock)
    mock_result_get_name.return_value = (False, True)

    mock_self = mocker.patch('ansible.plugins.callback.ActionBase._dump_results', new_callable=mocker.MagicMock)
    mock_self.return_value = 'test_result'

    callback = CallbackModule()
    result = mocker.MagicMock()
    result.attempts = 1
    result.retries = 3
    result._host = mocker.MagicMock()
    result._host.get_name.return_value = 'test_host'
    result._result = mocker.MagicMock()
    result

# Generated at 2022-06-13 11:46:03.403407
# Unit test for method v2_runner_retry of class CallbackModule
def test_CallbackModule_v2_runner_retry():
    callback = CallbackModule()
    #pass


# Generated at 2022-06-13 11:46:06.432238
# Unit test for method v2_playbook_on_include of class CallbackModule
def test_CallbackModule_v2_playbook_on_include():
    callback_module = CallbackModule()
    assert callback_module.v2_playbook_on_include(None) == None


# Generated at 2022-06-13 11:46:15.440628
# Unit test for method v2_runner_on_async_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_async_failed():
    cb = CallbackModule()
    result = FakeResult(
        host=FakeHost(name='test.example.org'), 
        result={'ansible_job_id': '12345'},
        _task=FakeTask(name='test task', action='test action'),
    )
    try:
        cb.v2_runner_on_async_failed(result)
    except Exception as e:
        assert False, "Unexpected exception: {}".format(e)
    assert True



# Generated at 2022-06-13 11:46:22.627177
# Unit test for method v2_playbook_on_play_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_play_start():
    # Initializing the callback plugin to test
    callback_plugin = CallbackModule()
    # Initializing the playbook object
    playbook = "Playbook object"
    # Calling the method v2_playbook_on_play_start of the callback plugin with the playbook object as argument
    callback_plugin.v2_playbook_on_play_start(playbook)
    # Asserting if the '_play' attribute of the callback_plugin is assigned with the playbook object
    assert callback_plugin._play is playbook

# Generated at 2022-06-13 11:46:25.825183
# Unit test for method v2_playbook_on_notify of class CallbackModule
def test_CallbackModule_v2_playbook_on_notify():
    callbackinstance = CallbackModule()
    handler = 'handler'
    host = 'host'
    callbackinstance.v2_playbook_on_notify(handler, host)


# Generated at 2022-06-13 11:46:28.420329
# Unit test for method v2_runner_item_on_ok of class CallbackModule
def test_CallbackModule_v2_runner_item_on_ok():
    # TODO: Comment out or update
    # callback = CallbackModule()
    # callback.v2_runner_item_on_ok(result=None)
    pass


# Generated at 2022-06-13 11:46:33.009614
# Unit test for method v2_runner_item_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_item_on_skipped():
    host = 'test_host'
    task_name = 'test_task'
    action = 'test_action'

    task_result = {}

    result = {'_host': host, '_task': _task(task_name, action)}

    plugin = CallbackModule()
    plugin.action_writeables = []

    plugin.v2_runner_item_on_ok(result)


# Generated at 2022-06-13 11:46:44.880755
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    # mock callback module
    mock_callback_module = CallbackModule()

    # mock runner result
    mock_result = mock.MagicMock()

    # mock stats
    mock_stats = mock.MagicMock()

    # mock task result
    mock_task_result = mock.MagicMock()
    
    # create mock task result
    mock_task_result.name = 'test_task'
    mock_task_result.exception = None
    mock_task_result.result = {}
    mock_task_result.action = 'test_action'
    mock_task_result.module_name = 'test_module_name'

    # create mock runner result
    mock_result.task_name.return_value = mock_task_result.name
    mock_result.exception.return_value = mock_task_result

# Generated at 2022-06-13 11:47:59.274963
# Unit test for method v2_playbook_on_start of class CallbackModule
def test_CallbackModule_v2_playbook_on_start():
  # prepare parameters
  playbook = ""

  # launch method and test the result
  result = CallbackModule()
  #unit test code
  raise NotImplementedError()


# Generated at 2022-06-13 11:48:02.197164
# Unit test for method set_options of class CallbackModule
def test_CallbackModule_set_options():
    # Create instace
    cb = CallbackModule()
    # Set options
    cb.set_options(check=True, check_mode_markers="any")
    # Asserts
    assert cb.check_mode_markers == "any"


# Generated at 2022-06-13 11:48:08.237416
# Unit test for method v2_runner_on_unreachable of class CallbackModule
def test_CallbackModule_v2_runner_on_unreachable():
    '''W0212: Access to a protected member _display of a client class'''
    test = CallbackModule()
    test._display = mock.MagicMock()
    test._display.display = mock.MagicMock()
    test.verbose = False
    result = mock.MagicMock()
    result._result = {
        'msg': 'n/a',
        'unreachable': True,
        '_ansible_no_log': False,
        '_ansible_item_result': False,
        'changed': False,
        'failed': True,
    }

    test.v2_runner_on_unreachable(result)
    r = test._dump_results(result._result)

# Generated at 2022-06-13 11:48:19.221385
# Unit test for method set_options of class CallbackModule
def test_CallbackModule_set_options():
    test_object = CallbackModule()
    # Unit test: Test set_options() with only default parameters
    assert test_object.set_options() == {'display_skipped_hosts': 'False', 'display_ok_hosts': 'True', 'remote_user': 'None', 'host_key_checking': 'True', 'display_custom_stats': 'True'}
    # Unit test: Test set_options() with only custom parameters

# Generated at 2022-06-13 11:48:22.253525
# Unit test for method v2_runner_on_skipped of class CallbackModule
def test_CallbackModule_v2_runner_on_skipped():
    runner_on_skipped = lambda result: result._host.get_name()
    assert runner_on_skipped(result) == 'example.com'


# Generated at 2022-06-13 11:48:23.815029
# Unit test for method v2_runner_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_on_failed():
    cb = CallbackModule()
    cb.v2_runner_on_failed(None)

# Generated at 2022-06-13 11:48:31.398322
# Unit test for method v2_playbook_on_include of class CallbackModule
def test_CallbackModule_v2_playbook_on_include():
    """
    Test the CallbackModule._playbook_on_include() method with the following conditions:
        - Check for CallbackModule.v2_playbook_on_include() method call
        - Check if the method returns None
    """
    # Define a dict of parameters to be used in the ansible.playbook.PlaybookExecutor().run() method
    extra_vars = {'test_param': 'I am a test!'}

    # Create a CallbackModule() object
    callback_module = CallbackModule()

    # Create a PlaybookExecutor() object

# Generated at 2022-06-13 11:48:38.645464
# Unit test for method v2_runner_item_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_item_on_failed():
    # tests_file = 'ansible/plugins/callback/default.py'
    tests_file = 'ansible/plugins/callback/default.py'
    m = imp.load_source('unit_test', tests_file)

    class Object(object):
        pass

    # setting up the testinstance
    callback = m.CallbackModule() 
    result = Object()
    result._task = Object()
    result._host = Object()
    result._task.action = "debug"
    result._result = {"msg": "test_message_1"}
    result._host.name = "test.example.com"
    result._task._uuid = "u1"
    # result._task.loop  = "args"
    # result._result = {"loop": "args"}

    # calling tested method
    callback.v2_runner

# Generated at 2022-06-13 11:48:47.591548
# Unit test for method v2_playbook_on_stats of class CallbackModule
def test_CallbackModule_v2_playbook_on_stats():
    playbook, test_dir = make_playbook()

# Generated at 2022-06-13 11:48:56.893679
# Unit test for method v2_runner_item_on_failed of class CallbackModule
def test_CallbackModule_v2_runner_item_on_failed():
    import ansible_runner
    job = ansible_runner.run()
    assert job.status == 'successful'
    for idx, host_result in enumerate(job.stats):
        assert list(job.stats.keys())[idx] == 'localhost'
        assert job.stats[list(job.stats.keys())[idx]]['failures'] == 0
        assert job.stats[list(job.stats.keys())[idx]]['ok'] == 2
        assert job.stats[list(job.stats.keys())[idx]]['changed'] == 0
        assert job.stats[list(job.stats.keys())[idx]]['unreachable'] == 0
        assert job.stats[list(job.stats.keys())[idx]]['skipped'] == 0

    # unit test for output