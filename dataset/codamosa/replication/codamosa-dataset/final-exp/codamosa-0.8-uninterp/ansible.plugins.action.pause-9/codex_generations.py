

# Generated at 2022-06-13 10:16:47.735875
# Unit test for function clear_line
def test_clear_line():
    class FakeStdout(object):
        def __init__(self, encoding='utf-8'):
            self.encoding = encoding
            self.output = b''
        def write(self, output):
            self.output += output
        def flush(self):
            pass

    # Output should be a carriage return and then clear to end of line.
    # If terminal supports it then output should also be an ansi escape
    # sequence to move to start of current line and clear to the end of line.
    # If terminal doesn't support it then MOVE_TO_BOL and CLEAR_TO_EOL will
    # be the empty string so output should only be a carriage return.
    fake_stdout = FakeStdout()
    clear_line(fake_stdout)
    assert fake_stdout.output == MOVE_TO_

# Generated at 2022-06-13 10:16:49.725329
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(connection=None, task=None)
    assert isinstance(action, ActionModule)

# Generated at 2022-06-13 10:16:56.402589
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import unittest
    import os
    import sys

    task = dict(
        action=dict(__ansible_module__=u'pause'),
        name=u'Pause for input',
        register=u'pause',
        args=dict(
            prompt=u'Pausing for input',
            seconds=5
        )
    )

    class TestActionModulePause(unittest.TestCase):
        def setUp(self):
            self.stdin = sys.stdin
            self.tmp = '/tmp/testfile'
            try:
                os.remove(self.tmp)
            except OSError as err:
                if err.errno != 2:
                    raise err

        def tearDown(self):
            sys.stdin = self.stdin
            os.remove(self.tmp)


# Generated at 2022-06-13 10:17:05.719955
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.action.pause
    am = ansible.plugins.action.pause.ActionModule(connection=None, task=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    task_vars = {}
    result = am.run(tmp=None, task_vars=task_vars)

    assert isinstance(result, dict) is True
    assert result['changed'] is False
    assert result['rc'] == 0
    assert result['stdout'] == ''
    assert result['stderr'] == ''
    assert result['start'] is None
    assert result['stop'] is None
    assert result['delta'] is None
    assert result['user_input'] == ''
    assert result['echo'] is True


# Generated at 2022-06-13 10:17:12.712583
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(None, None, None)
    assert module._task.args == {}
    assert module._connection._new_stdin is None

    # Test is_interactive function with existing terminal
    assert module._is_interactive()

    # Test is_interactive function with non-existing terminal
    module._connection._new_stdin = poffer_stdin('/dev/null')
    assert not module._is_interactive()

    # Test is_interactive function with TTY but in background
    module._connection._new_stdin = poffer_stdin('/dev/tty')
    assert not module._is_interactive()

    # Test invalid input for echo
    module._task.args['echo'] = 'Bogus'
    module._connection._new_stdin = poffer_stdin('/dev/tty')


# Generated at 2022-06-13 10:17:13.823517
# Unit test for constructor of class ActionModule
def test_ActionModule():
    ActionModule()


# Generated at 2022-06-13 10:17:24.181168
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Declare input parameters to the method
    tmp = ''
    task_vars = dict()
    duration_unit = 'minutes'
    prompt = None
    seconds = None
    echo = True
    echo_prompt = ''
    result = dict()
    result.update(dict(
        changed=False,
        rc=0,
        stderr='',
        stdout='',
        start=None,
        stop=None,
        delta=None,
        echo=echo
    ))

# Generated at 2022-06-13 10:17:25.279715
# Unit test for constructor of class ActionModule
def test_ActionModule():
    assert ActionModule is not None

# Generated at 2022-06-13 10:17:33.399621
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.playbook import Play
    from ansible.playbook import Task
    from ansible.playbook.block import Block
    from ansible.playbook.role import Role
    from ansible.playbook.task import Task as PlaybookTask

    # Test that we can create an instance of ActionModule
    am = ActionModule()

    # The _task attribute must be set so we can call the run() method.  Create a PlaybookTask
    # object and set it to the _task attribute.
    task = PlaybookTask()
    am._task = task

    # Create a Play object to set as the _play attribute

# Generated at 2022-06-13 10:17:36.135135
# Unit test for constructor of class ActionModule
def test_ActionModule():
    mod = ActionModule(None, None)
    assert mod._VALID_ARGS == frozenset(('echo', 'minutes', 'prompt', 'seconds'))

# Generated at 2022-06-13 10:17:57.609994
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Build mock action and task vars
    action = ActionModule()
    task = action._task
    task.args = {'echo': 'false'}
    task_vars = dict()
    action._connection = object()

    # Run the action method
    result = action.run(task_vars=task_vars)
    assert result['user_input'] == ''

# Generated at 2022-06-13 10:18:05.127031
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    x = ActionModule(module, module.params)
    x.env = {}
    x.templar = None
    x._shared_loader_obj = None
    x.connection = None
    x.runner = None
    x.connection_loader = None
    x.play = None
    x.play_context = None
    x.loader = None
    x.data = {}
    x.task_vars = {}
    x.connection_loader = {}
    x._task = {}
    x._task.args = {}
    x._task.args['echo'] = False

# Generated at 2022-06-13 10:18:16.595958
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # create an instance of class ActionModule
    action_module = ActionModule()

    # Use the assertEquals() method to compare the actual output with the expected output
    assert action_module._VALID_ARGS == frozenset(['echo', 'minutes', 'prompt', 'seconds']), \
           'action_module._VALID_ARGS should be frozenset([\'echo\', \'minutes\', \'prompt\', \'seconds\'])'

    # Test that the method run() returns the expected result
    assert action_module.run(tmp=None, task_vars=None) is not None, \
           'action_module.run(tmp=None, task_vars=None) should return a dictionary of results'

    # Test that the method run() returns the expected result

# Generated at 2022-06-13 10:18:25.449697
# Unit test for function is_interactive
def test_is_interactive():
    fm = ActionModule(task=None, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    if not hasattr(fm, '_display'):
        fm._display = Display()
    interactive = is_interactive(sys.stdin.fileno())
    assert interactive == fm._display.verbosity > 1, "is_interactive() failed for verbosity > 1"
    fm._display.verbosity = 1
    interactive = is_interactive(sys.stdin.fileno())
    assert interactive == False, "is_interactive() failed for verbosity = 1"
    fm._display.verbosity = 0
    interactive = is_interactive(sys.stdin.fileno())

# Generated at 2022-06-13 10:18:37.921431
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext
    from ansible.plugins.action import ActionBase

    class DummyConnecton(object):
        class DummyNewStdIn(object):
            def __init__(self):
                self.buffer = io.BytesIO()

        def __init__(self):
            self._new_stdin = self.DummyNewStdIn()

    class ActionModule(ActionBase):
        def run(self, tmp=None, task_vars=None):
            super(ActionModule, self).run(tmp, task_vars)
            return {}

    class Task(object):
        def __init__(self):
            self.name = 'test_task'
            self.args = dict()

        def get_name(self):
            return self.name


# Generated at 2022-06-13 10:18:46.428142
# Unit test for constructor of class ActionModule
def test_ActionModule():
    class Connection(object):
        class _new_stdin(object):
            def fileno(self):
                return 0
    class Task(object):
        def __init__(self, name, minutes, prompt, seconds):
            self.name = name
            self.minutes = minutes
            self.prompt = prompt
            self.seconds = seconds

        def get_name(self):
            return self.name
        def args(self):
            return {'minutes': self.minutes, 'prompt': self.prompt, 'seconds': self.seconds}
    class Runner(object):
        def __init__(self, connection):
            self._connection = connection
    class Play(object):
        def __init__(self, runner):
            self._runner = runner

# Generated at 2022-06-13 10:18:49.322541
# Unit test for function is_interactive
def test_is_interactive():
    fd = sys.stdin.fileno()
    assert is_interactive(fd)
    assert is_interactive(sys.stdout)

# Generated at 2022-06-13 10:18:52.309962
# Unit test for constructor of class ActionModule
def test_ActionModule():
    from ansible.plugins.action.pause import ActionModule

    pause = ActionModule()
    assert pause is not None


# Generated at 2022-06-13 10:18:59.080312
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(task_vars={})
    tmp = {'foo': 'bar','baz': 'qux'}
    task_vars = {'foo': 'bar', 'baz': 'qux'}
    result = module.run(tmp, task_vars)
    assert result['changed'] == False
    assert result['rc'] == 0
    assert result['user_input'] == b'baz'
    assert result['echo'] == True

# Generated at 2022-06-13 10:19:07.399146
# Unit test for constructor of class ActionModule
def test_ActionModule():
    """Unit test for constructor of class ActionModule"""

    # _task.args is set in the constructor.  Bypass it.
    # pylint: disable=protected-access
    #_VALID_ARGS is defined in the class.
    # pylint: disable=no-member
    action_module = ActionModule()
    action_module.ActionBase__init__()
    action_module._task.args = {'seconds': '123', 'prompt': 'foo', 'echo': 'on'}
    action_module._task.get_name = lambda: 'ask'
    action_module._connection = FakeConnection()

    # .action is set in __init__.  Don't call it.
    # pylint: disable=attribute-defined-outside-init
    action_module.action = 'pause'


# Generated at 2022-06-13 10:19:47.308843
# Unit test for constructor of class ActionModule

# Generated at 2022-06-13 10:19:52.243180
# Unit test for constructor of class ActionModule
def test_ActionModule():
    action = ActionModule(None, dict())

    expected = ['failed', 'msg', 'rc', 'start', 'stderr', 'stdout', 'changed', 'delta', 'user_input', 'echo']
    assert sorted(action.run(tmp='foo', task_vars=dict()).keys()) == expected

# Generated at 2022-06-13 10:20:02.367526
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import os
    import tempfile
    import unittest
    from ansible.plugins.action.pause import ActionModule
    from ansible.plugins.action.pause import AnsibleTimeoutExceeded
    from ansible.plugins.action.pause import timeout_handler
    from ansible.plugins.action.pause import clear_line
    from ansible.plugins.action.pause import is_interactive
    import ansible.plugins.action.pause as pause
    from ansible.utils.display import Display

    # Initialize display object
    display.verbosity = True

    # Create a temp file to hold stdin (pipes are not supported on Windows)
    stdin_file = tempfile.TemporaryFile(mode="w+b")

    # Create a temp file to hold stdout (pipes are not supported on Windows)
    stdout_file = temp

# Generated at 2022-06-13 10:20:16.871678
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import curses
    import sys
    import unittest

    # Loadable.run will be properly tested by Ansible itself
    # so we don't need to test it here. It's enough to test the parts which
    # are specific to this module which we can easily mock.
    from ansible.plugins.action.pause import ActionModule
    class MockConnection:
        class MockNewStdin:
            class MockBuffer:
                def __init__(self):
                    pass
                def fileno(self):
                    return 0
            def __init__(self):
                self.buffer = self.MockBuffer()

        def __init__(self):
            self._new_stdin = self.MockNewStdin()

    class MockTask:
        def __init__(self, arguments):
            self.args = arguments

# Generated at 2022-06-13 10:20:23.373091
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.playbook.play_context import PlayContext

    class Connection:
        def __init__(self):
            self._new_stdin = FakeStdin()

    class FakeStdin:
        def __init__(self):
            if PY3:
                import io
                self.buffer = io.BytesIO(b'a')
            else:
                self.buffer = 'a'

        def fileno(self):
            return 0

    class Play:
        def __init__(self):
            self.connection = Connection()
            self.become = False
            self.become_user = None
            self.no_log = False
            self.diff = False
            self.check_mode = False

    class Task:
        def __init__(self):
            self._play = Play()

# Generated at 2022-06-13 10:20:32.521969
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    am = ActionModule()
    am._task.args = {
        'echo' : False,
        'minutes' : 0,
        'prompt': "Press enter to continue",
        'seconds': -1
    }
    result = am.run(tmp='/tmp/tmp', task_vars={})
    assert result['failed'] == False
    assert result['msg'] == ''
    assert result['rc'] == 0
    assert result['stderr'] == ''
    assert result['stdout'] == 'Paused for 0.0 seconds'
    assert result['changed'] == False
    am._task.args = {
        'echo' : False,
        'minutes' : 1,
        'prompt': "Press enter to continue",
        'seconds': -1
    }

# Generated at 2022-06-13 10:20:38.477282
# Unit test for function is_interactive
def test_is_interactive():
    from tempfile import TemporaryFile

    fd = TemporaryFile()
    assert not is_interactive(fd=fd)
    fd.close()

    fd = TemporaryFile()
    assert not is_interactive(fd=fd.fileno())
    fd.close()

    # This is the only way to cause isatty(fd) to return True in
    # this subprocess...
    assert is_interactive(fd=sys.stdin.fileno())

# Generated at 2022-06-13 10:20:40.209484
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule(connection=None)
    module.run()

# Generated at 2022-06-13 10:20:45.237207
# Unit test for constructor of class ActionModule
def test_ActionModule():
    # to add a test, create a dict() and pass it to the class constructor
    test_dict = dict()
    test_instance = ActionModule(task=test_dict, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    assert isinstance(test_instance, ActionModule)

# Generated at 2022-06-13 10:20:55.208949
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    from ansible.module_utils import basic

    # Test case:
    # The pause module is called without 'seconds' or 'minutes'
    # and without 'echo': 'False'
    module = basic.AnsibleModule(
        argument_spec=dict(
            prompt=dict(type='str', default='Press enter to continue, Ctrl+C to interrupt'),
            echo=dict(type='bool', default=True),
            minutes=dict(type='int', default=0),
            seconds=dict(type='int', default=0),
        )
    )

    pause = ActionModule(module, {})
    result = pause.run(tmp=None, task_vars={})


# Generated at 2022-06-13 10:22:18.352799
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    pass

# Generated at 2022-06-13 10:22:25.732497
# Unit test for function is_interactive
def test_is_interactive():
    # Create pipe
    test_pipe_r, test_pipe_w = os.pipe()

    # Test with valid file descriptor
    assert(is_interactive(test_pipe_r))

    # Test with invalid file descriptor
    assert(not is_interactive(-1))

    # Close file descriptor
    os.close(test_pipe_r)
    os.close(test_pipe_w)


# Generated at 2022-06-13 10:22:29.377252
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    # Create a class instance
    task_vars = dict()
    action_plugin = ActionModule(
        task=dict(args=dict()),
        connection=dict(),
        play_context=dict()
    )
    # Test run()
    assert action_plugin.run(task_vars=task_vars)

    # Test run() with task_vars=dict()
    assert action_plugin.run(task_vars=dict())

# Generated at 2022-06-13 10:22:34.769582
# Unit test for function clear_line
def test_clear_line():
    class stdout:
        def __init__(self):
            self.written_bytes = b''

        def write(self, bytes):
            self.written_bytes = b''.join((self.written_bytes, bytes))

    display = stdout()
    clear_line(display)
    assert(display.written_bytes == b'\x1b[\r\x1b[K')

# Generated at 2022-06-13 10:22:35.753587
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    mod = ActionModule()
    mod.run()

# Generated at 2022-06-13 10:22:43.179437
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    test_dict = dict(
        name='test_action_module',
        args=dict(
            prompt='What is the meaning of life?',
            echo=False
        ),
        async_val=25,
        delegate_to='localhost',
        delegate_facts=False,
        register='test_register'
    )
    test_ActionModule = ActionModule(test_dict, connection=None, play_context=None, loader=None, templar=None, shared_loader_obj=None)
    test_ActionModule_run_result = test_ActionModule.run()

# Generated at 2022-06-13 10:22:44.248005
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    module = ActionModule()
    module.run()

# Generated at 2022-06-13 10:22:48.914140
# Unit test for function is_interactive
def test_is_interactive():
    ''' Test behavior of is_interactive() '''
    from tempfile import TemporaryFile
    from os import fdopen

    # test with stdin (a TTY)
    assert is_interactive(0)

    # test with file descriptor for temporary file
    tf = TemporaryFile()
    fd = fdopen(tf)
    assert is_interactive(tf.fileno())

# Generated at 2022-06-13 10:22:54.199141
# Unit test for function is_interactive
def test_is_interactive():
    # The following test is interactive so it is disabled.
    # The test is kept to document the expected behavior.

    # p = subprocess.Popen('echo foo', stdout=subprocess.PIPE)
    # assert not is_interactive(p.stdout.fileno())
    # p.wait()
    pass

# Generated at 2022-06-13 10:23:03.456982
# Unit test for method run of class ActionModule
def test_ActionModule_run():
    import ansible.plugins.loader as plugin_loader
    import ansible.plugins.action as action_plugin

    class TestModule(ActionModule):
        pass

    a_plugin = plugin_loader.get('action', 'TestModule')

    class TestModulePlugin(action_plugin.ActionBase):
        def run(self, tmp=None, task_vars=None):
            return dict()

    a_plugin._setup_action(TestModulePlugin)

    a_conn = 'ansible.plugins.connection.local.Connection'
    a_loader = 'ansible.plugins.loader.connection_loader'
    a_plugin._add_connection_plugin(a_conn, a_loader)

    a_shell = 'ansible.plugins.shell.bash.ShellModule'
    a_loader = 'ansible.plugins.loader.shell_loader'