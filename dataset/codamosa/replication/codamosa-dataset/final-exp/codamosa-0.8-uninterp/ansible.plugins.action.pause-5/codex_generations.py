

# Generated at 2022-06-13 10:16:33.551814
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_result import TaskResult

    fake_task = dict(
        name='Ansible Task',
        args=dict()
    )
    fake_play_context = PlayContext()
    fake_task_result = TaskResult(task=fake_task, host=None)
    fake_play_context.prompt = dict(
        seconds=0
    )
    fake_play_context.timeout = 10
    fake_play_context.new_stdin = sys.stdin

    fake_task_result._task = fake_task
    fake_task_result._host = None
    fake_task_result._task_fields['args'] = dict(prompt='test')

# Generated at 2022-06-13 10:16:41.971700
# Unit test for function clear_line
def test_clear_line():
    display.display("foo")
    # pretend sys.stdout is open and connected to a terminal
    stdout_fd = sys.stdout.fileno()
    class FakeTTY():
        def __init__(self):
            self.stdout = stdout_fd
            self.in_raw = False
            self.settings = termios.tcgetattr(stdout_fd)
            self.new_settings = termios.tcgetattr(stdout_fd)

        def __enter__(self):
            # clear the screen
            display.clear_display()
            # make sure we are in cooked mode (no raw terminal)
            termios.tcsetattr(self.stdout, termios.TCSADRAIN, self.settings)
            # save settings and go into raw mode

# Generated at 2022-06-13 10:16:51.867692
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    display.verbosity = 4
    am = ActionModule(None, None, None, None, None)

    # Test defaults
    am._task.args = {}
    result = am.run(None, None)
    assert result['changed'] == False
    assert result['rc'] == 0
    assert result['stderr'] == ''
    assert result['stdout'] == "Paused for 1.0 minutes"
    assert result['user_input'] == ''

    # Test prompt
    am._task.args = dict(prompt='Press continue or abort:')
    result = am.run(None, None)
    assert result['changed'] == False
    assert result['rc'] == 0
    assert result['stderr'] == ''
    assert result['stdout'] == "Paused for 1.0 minutes"

# Generated at 2022-06-13 10:17:03.185728
# Unit test for function is_interactive
def test_is_interactive():
    from multiprocessing import Process
    from tempfile import TemporaryFile

    def run_test_is_interactive_process(fd, is_interactive_result):
        # Make the process a session and process group leader so that it
        # can call tcgetpgrp().
        if PY3:
            os.setpgrp()
        else:
            os.setpgrp(0, 0)

        # Run is_interactive() with parameters
        result = is_interactive(fd)
        if result != is_interactive_result:
            raise Exception("is_interactive() returned an unexpected value - expected: %s, got: %s" %
                            (is_interactive_result, result))

        # Run is_interactive() without parameters (uses sys.stdin)
        result = is_interactive()


# Generated at 2022-06-13 10:17:11.786347
# Unit test for function is_interactive
def test_is_interactive():
    # The function is_interactive() should return true only if the process is
    # running in the foreground. The best way to test this is to create a child
    # process that is in a different process group and run the function in that
    # child process.

    # Fork the process and only execute is_interactive() in the child process.
    pid = os.fork()
    if pid == 0:
        # Only execute the code to test is_interactive() in the child process.
        # Store the result of is_interactive() before and after changing the
        # process group.
        result_before = is_interactive()
        os.setpgrp()
        result_after = is_interactive()

        # The process group should be different before and after.
        if result_before == result_after:
            sys.exit(1)


# Generated at 2022-06-13 10:17:22.349822
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test case none
    # Expected result
    expected = {}
    expected['changed'] = False
    expected['rc'] = 0
    expected['stderr'] = ''
    expected['stdout'] = ''
    expected['start'] = u'2016-12-26 20:40:43.404062'
    expected['stop'] = u'2016-12-26 20:40:43.404069'
    expected['delta'] = 7
    expected['user_input'] = u''

    # Test case one
    # Expected result
    expected_one = {}
    expected_one['changed'] = False
    expected_one['rc'] = 0
    expected_one['stderr'] = ''
    expected_one['stdout'] = 'Paused for 60 minutes'

# Generated at 2022-06-13 10:17:31.681489
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.utils.connection
    from ansible.utils.path import makedirs_safe
    from ansible.utils.unicode import to_bytes

    from ansible.playbook.play_context import PlayContext

    # create a mock ModuleStdin and stdout
    if PY3:
        stdin = io.BytesIO()
        stdout = io.BytesIO()
    else:
        stdin = io.StringIO()
        stdout = io.StringIO()
    sys.stdout = stdout
    sys.stdin = stdin

    # create a mock connection plugin
    class MockConnection(object):
        def close(self):
            pass


# Generated at 2022-06-13 10:17:40.884550
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # fake some inputs for testing the return code and results of run()
    fake_task_args = dict(
        echo=True,
        minutes=1,
        prompt='fake prompt',
        seconds=2,
    )

    fake_action_module = ActionModule(None, dict(
        args=fake_task_args,
        _ansible_verbosity=4,
    ))

    # fake time.time() for our timeouts
    fake_time = 0.0

    def mock_time():
        return fake_time

    # mock time.time()
    import time
    time.time = mock_time
    import datetime
    start = datetime.datetime.now()

    # mock the is_interactive() method of ActionModule
    # returns False so that pause can timeout

# Generated at 2022-06-13 10:17:51.703239
# Unit test for function is_interactive
def test_is_interactive():
    # Save the current stdin and stdout so that we may restore them later
    old_stdin = sys.stdin
    old_stdout = sys.stdout

    # Create a temporary file and use it as stdin
    sys.stdin = open('/dev/null', 'r')
    sys.stdout = open('/dev/null', 'w')

    # is_interactive should return False when stdin is not a TTY
    assert not is_interactive()

    # Restore the old stdin and stdout
    sys.stdin = old_stdin
    sys.stdout = old_stdout

# Generated at 2022-06-13 10:17:57.972955
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    m_task_vars = 'task_vars'
    m_args = 'm_args'
    m_tmp = 'm_tmp'
    m_super = 'm_super'
    seconds = 10
    duration_unit = 'seconds'
    prompt = 'prompt'
    prompt_with_echo = "[test]\n%s:\n" % prompt
    prompt_without_echo = "[test]\nPress enter to continue, Ctrl+C to interrupt\n"
    expected_stdout_after_10s_pause = "Paused for 10 %s" % duration_unit
    m_start = 100
    m_duration = 10.0
    m_now = 200
    m_delta = int(m_now - m_start)
    m_isatty = 'm_isatty'
    m

# Generated at 2022-06-13 10:18:21.697504
# Unit test for function clear_line
def test_clear_line():
    # Bring up a stream object with a captured stdout.
    stream = io.StringIO()
    tmp = sys.stdout
    try:
        sys.stdout = stream
        clear_line(sys.stdout)
        # Assert that the output of the function is what
        # we expect.
        assert stream.getvalue() == MOVE_TO_BOL + CLEAR_TO_EOL
    finally:
        # Restore stdout in case the unit test fails.
        sys.stdout = tmp

# Generated at 2022-06-13 10:18:22.589269
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()

# Generated at 2022-06-13 10:18:30.026160
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils import connection
    from ansible.executor.task_queue_manager import TaskQueueManager

    class MockConnection(connection.Connection):
        def __init__(self):
            self._new_stdin = None

        def set_new_stdin(self, new_stdin):
            self._new_stdin = new_stdin

    class MockTaskQueueManager(TaskQueueManager):

        def __init__(self, task_vars):
            self._task_vars = task_vars
            self._stats = {}

    class MockTask(object):
        def __init__(self, args):
            self.args = args
            self.name = ''

        def get_name(self):
            return self.name


# Generated at 2022-06-13 10:18:31.153696
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # TODO: Write unit test?
    assert True

# Generated at 2022-06-13 10:18:33.891836
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test the ActionModule.run() method
    # TODO: Add a unit test for the ActionModule.run() method
    pass

# Generated at 2022-06-13 10:18:34.582747
# Unit test for constructor of class ActionModule
def test_ActionModule():
    pass

# Generated at 2022-06-13 10:18:41.398644
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # imports
    from ansible.plugins.action.pause import ActionModule

    # create objects
    am = ActionModule()

    # call the method run to test
    result = am.run(None, None)

    # assert the results
    assert isinstance(result, dict)
    assert result['changed'] is False
    assert result['rc'] == 0
    assert result['stderr'] == ''
    assert result['stdout'] == ''

# Generated at 2022-06-13 10:18:48.137478
# Unit test for function is_interactive
def test_is_interactive():
    if sys.platform != 'darwin':
        # This test only works on OS X right now due to a limitation in curses that causes crashes.
        # curses.setupterm() causes a segmentation fault when there is no terminal available.
        # See https://github.com/python/cpython/issues/2862 for more information
        return
    with open('/dev/null', 'rb+') as devnull:
        old_settings = termios.tcgetattr(devnull)
        devnull_fd = devnull.fileno()
        termios.tcsetattr(devnull_fd, termios.TCSADRAIN, old_settings)
        with open('/dev/tty', 'rb+') as devtty:
            devtty_fd = devtty.fileno()

# Generated at 2022-06-13 10:18:59.829524
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    module = ActionModule()

    class fake_task:
        def __init__(self):
            self.args = {
                'echo': True,
                'prompt': 'Continue [Y/n]?',
                'minutes': '1',
                'seconds': '10'
            }
            self.name = 'Pause'

        def get_name(self):
            return self.name

    module._task = fake_task()
    module._play_context = {}
    module._connection = {}

    class fake_stdin:
        def __init__(self):
            self.buffer = io.BytesIO()

    class fake_stdout:
        def __init__(self):
            self.buffer = io.BytesIO()

    class fake_connection:
        def __init__(self):
            self._new_

# Generated at 2022-06-13 10:19:07.959925
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.common.removed import removed
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.connection.connection_loader import ConnectionLoader
    from ansible.plugins.loader import module_loader
    import ansible.module_utils.connection
    import ansible.plugins.action.pause

    # Create a mock ConnectionLoader and register the plugin
    conn_loader = ConnectionLoader()
    conn_loader.register('TestConnection', 'impl_test_connection', 'Test',
                         ansible.module_utils.connection)

    # Create a mock connection plugin
    class Connection:
        def __init__(self, play_context):
            self.play_context = play_context

    conn = Connection(play_context=PlayContext())

    # Create a mock module loader

# Generated at 2022-06-13 10:19:41.498114
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    mock_self = Mock()
    mock_self._task = Mock()
    mock_self._task.args = {}
    mock_self._task.get_name = Mock(return_value="pause")
    mock_self._connection = Mock()
    mock_self._connection._new_stdin = Mock()
    if PY3:
        mock_self._connection._new_stdin.buffer = Mock()

    mock_self.run = ActionModule.run
    res = mock_self.run('tmp', 'task_vars')
    assert res['stdout'] == 'Paused for 1 minutes', res['stdout']
    assert res['changed'] == False

    mock_self._task.args = dict(minutes=0.5, echo=False)
    res = mock_self.run('tmp', 'task_vars')


# Generated at 2022-06-13 10:19:53.498791
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test the run method of class ActionModule

    #     result = super(ActionModule, self).run(tmp, task_vars)
    #     del tmp  # tmp no longer has any effect

    result = dict()
    result.update(dict(
        failed=False,
        changed=False,
        rc=0,
        stderr='',
        stdout='',
        start=None,
        stop=None,
        delta=None,
        echo=False
    ))

    # duration_unit = 'minutes'
    # prompt = None
    # seconds = None
    # echo = True
    # echo_prompt = ''

    duration_unit = 'seconds'
    prompt = "Press enter to continue, Ctrl+C to interrupt (output is hidden):"
    seconds = 2
    echo = False
    echo_

# Generated at 2022-06-13 10:19:54.915810
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    #AnsibleTimeoutExceeded
    pass



# Generated at 2022-06-13 10:20:01.908356
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # test __new__ method
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert action_module
    assert action_module._task == None
    assert action_module._connection == None
    assert action_module._play_context == None
    assert action_module._loader == None
    assert action_module._templar == None
    assert action_module._shared_loader_obj == None


# Generated at 2022-06-13 10:20:08.859518
# Unit test for function is_interactive
def test_is_interactive():
    # Replace sys.stdin with a file object; this fd is not in an interactive session
    class NotInteractive(object):
        fd = 1

    sys.stdin = NotInteractive()
    assert is_interactive(None) is False
    assert is_interactive(sys.stdin.fd) is False

    # Replace sys.stdin with a file object; this fd is in an interactive session
    class Interactive(object):
        fd = 0

    sys.stdin = Interactive()
    assert is_interactive(None) is False
    assert is_interactive(sys.stdin.fd) is True

# Generated at 2022-06-13 10:20:16.617106
# Unit test for function clear_line
def test_clear_line():
    # Setup test
    class TestStream:
        def __init__(self):
            self.buffer = b''

        def write(self, data):
            self.buffer += data

    old_stdout = sys.stdout
    test_stdout = TestStream()
    sys.stdout = test_stdout

    # Test
    clear_line(sys.stdout)

    # Teardown
    sys.stdout = old_stdout

    # If the clear_line function is working correctly the output will contain
    # the move to beginning-of-line sequence followed by the clear-to-end-of-
    # line sequence.
    assert test_stdout.buffer == b'\x1b[%s\x1b[%s' % (MOVE_TO_BOL, CLEAR_TO_EOL)

# Generated at 2022-06-13 10:20:19.688861
# Unit test for function clear_line
def test_clear_line():
    from io import StringIO
    import mock

    stdout = StringIO()
    with mock.patch('sys.stdout', stdout):
        clear_line(stdout)

    assert stdout.getvalue() == b'\x1b[\r'
    assert stdout.getvalue() == b'\x1b[K'

# Generated at 2022-06-13 10:20:29.699377
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    display = Display()
    action_module = ActionModule(task=dict(args=dict()), connection=None, play_context={}, loader=None, templar=None, shared_loader_obj=None)
    try:
        action_module._c_or_a = lambda x: True
        # Set display.verbosity to 2 (that's the maximum value) so that the output doesn't
        # go to stdout but instead to the display.display buffer.
        display.verbosity = 2
        with display:
            result = action_module.run()
            assert result['user_input'] == ''
    except Exception as e:
        raise(e)
    finally:
        display.verbosity = 0

# Generated at 2022-06-13 10:20:35.890234
# Unit test for function clear_line
def test_clear_line():
    class MockFile(object):
        def __init__(self):
            self.contents = ""
            self.written = []

        def write(self, text):
            self.written.append(text)

        def readline(self):
            return self.contents

    stdout = MockFile()
    clear_line(stdout)
    assert stdout.written == [b'\x1b[', MOVE_TO_BOL, b'\x1b[', CLEAR_TO_EOL]



# Generated at 2022-06-13 10:20:36.991990
# Unit test for constructor of class ActionModule
def test_ActionModule():
    m = ActionModule()
    assert m

# Generated at 2022-06-13 10:21:35.873557
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    '''
    Unit test for method run of class ActionModule
    '''

    raise NotImplementedError

# Generated at 2022-06-13 10:21:46.596691
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule(connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)

    task = dict()
    task['action'] = dict()
    task['name'] = "TESTTASK1234"
    task['args'] = dict()
    task['args']['minutes'] = 1
    task['args']['prompt'] = 'prompt'
    task['args']['echo'] = 'yes'

    mod._task = task

    mod._connection = object
    mod._connection._new_stdin = object()
    mod._connection._new_stdin.write = lambda x: None
    mod._connection._new_stdin.read = lambda x: b'\x03'

# Generated at 2022-06-13 10:21:52.490889
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # initialize our own ActionModule with fake connection
    action_module_run = ActionModule(play_context={}, connection={})
    # call method run with fake parameters
    result = action_module_run.run(tmp=None, task_vars={})
    # check result
    assert not result['changed']
    assert result['rc'] == 0
    assert result['start'] is not None
    assert result['stop'] is not None
    assert result['delta'] is not None


# Generated at 2022-06-13 10:21:59.067039
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    class Connection(object):
        def __init__(self):
            self.returns = [b'', b'', b'a']
            self.index = 0

        def read(self, bytes_to_read):
            return_value = self.returns[self.index]
            self.index += 1
            return return_value

        def fileno(self):
            return 1

    class Task(object):
        def __init__(self):
            self.args = {
                'prompt': 'Press enter to continue, Ctrl+C to interrupt',
                'echo': False
            }

        def get_name(self):
            return 'Pause'

    conn = Connection()
    task = Task()
    action_mod = ActionModule(task, conn, 'ansible.cfg', False)

# Generated at 2022-06-13 10:22:12.270045
# Unit test for function clear_line
def test_clear_line():
    '''Clear the output line, then output some text'''
    class fake_stdout(object):
        """Fake stdout I/O"""
        def __init__(self):
            self.data = b''

        def write(self, data):
            self.data += data

    # Check output (backspace + clear)
    fake_output = fake_stdout()
    fake_output.write(b'hello')
    clear_line(fake_output)
    fake_output.write(b'bye')

    assert fake_output.data == b'\x1b[\r\x1b[Kbye'

    # Check output (clear + move)
    fake_output = fake_stdout()
    fake_output.write(b'hello')
    clear_line(fake_output)
    fake_output.write

# Generated at 2022-06-13 10:22:20.606768
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Test method run of class ActionModule
    # Given
    # - all defaults
    # - a user_input
    # - a seconds argument
    args = dict(echo=False, minutes=2, prompt='user prompt', seconds=None)
    task_vars = dict()
    module = ActionModule(dict())
    module._task = dict(name='pause', args=args)
    module._connection = dict(new_stdin=dict(fileno=dict(return_value=5)))

    old_read = termios.tcgetattr(5)[6][termios.ICRNL]
    old_echo = termios.tcgetattr(5)[3]

    new_read = old_read | termios.ICRNL
    new_echo = old_echo ^ termios.ECHO

    stdin_fd = module._connection

# Generated at 2022-06-13 10:22:27.301548
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.connection.paramiko_ssh import Connection

    # Dummy class for paramiko connection
    class DummySFTPServer():
        def stat(self):
            return

        def get(self):
            return

        def put(self):
            return

    class DummyBaseConnection():
        def __init__(self):
            self.connection = None

    # Create dummy paramiko connection object
    dummy_connection = Connection(ssh_executable='ssh')
    dummy_connection._initialized = True
    dummy_connection._connected = True
    dummy_connection._host = 'host'

    # Create dummy paramiko transport object
    dummy_transport = dummy_connection._create_transport()
    dummy_connection._connected = True
    dummy_transport._active = True
    dummy_transport.use_compression

# Generated at 2022-06-13 10:22:32.450373
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    action_module = ActionModule()

    class MockRPC:
        def __init__(self, path):
            self._path = path
        def _load_name(self):
            return '<Mock RPC>'
        def __getattr__(self, attr):
            class MockConnection:
                def __init__(self, path):
                    self._path = path
                def _connect(self):
                    pass

# Generated at 2022-06-13 10:22:35.067261
# Unit test for function is_interactive
def test_is_interactive():
    assert is_interactive(0) == False
    assert is_interactive(1) == False
    assert is_interactive(2) == False
    assert is_interactive(3) == False

# Generated at 2022-06-13 10:22:37.682728
# Unit test for function clear_line
def test_clear_line():
    class fake_file:
        def __init__(self):
            pass

        def write(self, b):
            assert b == b'\x1b[\r'

    clear_line(fake_file())

# Generated at 2022-06-13 10:25:27.617549
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import datetime
    from ansible.parsing.yaml.dumper import AnsibleDumper
    from ansible.plugins.action.pause import ActionModule
    from ansible.vars.unsafe_proxy import AnsibleUnsafeText
    # Modify the stdlib to meet the test harness's expectations.
    datetime.datetime.now = lambda : datetime.datetime(2012, 12, 12, 12, 12, 12)
    datetime.datetime.strftime = lambda dt, x: dt.strftime(x)
    date_str = datetime.datetime.strftime(datetime.datetime.now(),
                                          "%c %z")
    seconds_str = "%d" % datetime.datetime.timestamp(datetime.datetime.now())
    # The following is a shell-implementation-

# Generated at 2022-06-13 10:25:36.965624
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.plugins.strategy import StrategyBase
    am = ActionModule(
        task=dict(action=dict(module_name='pause', module_args=dict(minutes=1)))
    )

    tqm = TaskQueueManager(
        inventory=dict(),
        variable_manager=dict(),
        loader=dict(),
        passwords=dict(),
        stdout_callback='default',
        run_tree=False,
        done_callback=None,
        connection_options=dict(),
        fork_interval=0
    )

    strategy = StrategyBase('debug', tqm)
    tqm.send_callback = dict()
    tqm._final_q = dict()
    tqm._timeout = dict()
    tqm

# Generated at 2022-06-13 10:25:44.177292
# Unit test for method run of class ActionModule
def test_ActionModule_run():

    setattr(ActionModule, '_connection', None)
    #
    # Mock run implementation
    #
    def _run(self, tmp, task_vars):
        return dict(
            start=None,
            stop=None,
            delta=None,
            user_input='',
            stdout='',
            stderr=''
        )
    setattr(ActionModule, 'run', _run)
    #
    # Create an instance of ActionModule
    #
    action_module = ActionModule()
    #
    # Create a dummy task with args={'prompt': 'Paused...'}
    #
    task = dict(
        args=dict(
            prompt='Paused...'
        )
    )
    result = action_module.run(None, None, task)

# Generated at 2022-06-13 10:25:53.158074
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager

    context = PlayContext()
    context.become = False
    context.become_user = None
    context.remote_addr = None
    context.remote_user = 'remote_user'
    context.port = 2222
    context.connection = 'local'
    tqm = None

    loader = 'loader'
    play_context = context
    new_stdin = 'new_stdin'
    options = 'options'
    variable_manager = 'variable_manager'

    # Create instance of action module

# Generated at 2022-06-13 10:25:56.174206
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(action, ActionModule)

# Generated at 2022-06-13 10:26:03.254540
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest
    import sys
    import unittest.mock

    from ansible.plugins.action.pause import ActionModule

    # Mock class for class ActionModule
    class MockActionModule(ActionModule):
        def __init__(self, task, connection, play_context, loader, templar, shared_loader_obj):
            self._task = task
            self._task._role = None
            self._connection = connection
            self._play_context = play_context
            self._loader = loader
            self._templar = templar
            self._shared_loader_obj = shared_loader_obj

        def run(self, tmp=None, task_vars=None):
            if task_vars is None:
                task_vars = dict()
            # save the old attributes on the existing (duped) std

# Generated at 2022-06-13 10:26:18.236071
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Stub for the _Connection class
    class _Connection:
        def __init__(self):
            self._new_stdin = None

    # Stub for the AnsibleModule class
    class AnsibleModule:
        def __init__(self):
            self._task = None
            self._connection = _Connection()

        def fail_json(self, **kw):
            pass

    # Stub for the Task class
    class Task:
        def __init__(self):
            self._args = None

        def get_name(self):
            return "test_ActionModule_run"

    # Stub for the _display class
    class _display:
        def __init__(self):
            self._output = []
