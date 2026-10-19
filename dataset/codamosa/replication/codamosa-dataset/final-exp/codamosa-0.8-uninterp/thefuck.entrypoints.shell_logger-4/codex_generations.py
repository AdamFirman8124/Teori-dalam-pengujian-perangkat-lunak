

# Generated at 2022-06-14 09:04:01.337505
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile
    temp = tempfile.mkdtemp()
    print(temp)
    out = os.path.join(temp, 'out.txt')
    shell_logger(out)
    print('File created: {}'.format(out))

# Generated at 2022-06-14 09:04:03.630730
# Unit test for function shell_logger
def test_shell_logger():
    print("Unit test for function shell_logger")
    shell_logger("log_files/log.sh")

# Generated at 2022-06-14 09:04:12.919328
# Unit test for function shell_logger
def test_shell_logger():
    # Test: Write output file and check that it exist.
    import tempfile
    tempdir = tempfile.mkdtemp()
    output_path = os.path.join(tempdir, 'output')
    shell_logger(output_path)
    assert(os.path.exists(output_path))
    os.remove(output_path)
    os.rmdir(tempdir)
    # Test: Check that shell_logger doesn't crash when `output` is a directory
    shell_logger('/')
    # Test: Check that it doesn't crash when `output` is a directory which doesn't exist
    shell_logger('/thish-directory-is-impossible')
    # Test: Check that it doesn't crash when `output` is a regular file which doesn't exist

# Generated at 2022-06-14 09:04:23.625195
# Unit test for function shell_logger
def test_shell_logger():
    # Create a fake file
    with open('test_logger.log', 'w') as output_file:
        output_file.write('1234567890')
    # Run function
    shell_logger('test_logger.log')
    # Check log file
    with open('test_logger.log', 'r') as output_file:
        temp = output_file.read()
    # Check the result
    assert len(temp) == const.LOG_SIZE_IN_BYTES
    assert temp[-10:] == '1234567890'
    os.remove('test_logger.log')


if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:04:24.344559
# Unit test for function shell_logger
def test_shell_logger():
    pass

# Generated at 2022-06-14 09:04:25.025714
# Unit test for function shell_logger
def test_shell_logger():
    # TODO
    pass

# Generated at 2022-06-14 09:04:30.182563
# Unit test for function shell_logger
def test_shell_logger():
    try:
        shell_logger('test.log')
    except SystemExit:
        pass
    except:
        raise
    finally:
        if os.path.isfile('test.log'):
            os.remove('test.log')


# Generated at 2022-06-14 09:04:32.703616
# Unit test for function shell_logger
def test_shell_logger():
    try:
        shell_logger('test.log')
    except NotImplementedError:
        pass

# Generated at 2022-06-14 09:04:38.745344
# Unit test for function shell_logger
def test_shell_logger():
    def mock_spawn(shell, master_read):
        return 0

    logs.warn.side_effect = ValueError
    prev_spawn = pty.spawn
    pty.spawn = mock_spawn
    with pytest.raises(SystemExit):
        shell_logger('/tmp/testshell.log')
    pty.spawn = prev_spawn

# Generated at 2022-06-14 09:04:42.966746
# Unit test for function shell_logger
def test_shell_logger():
    print("Test shell logger runs fully automatic and interactively.")
    shell_logger('/tmp/inner.log')

# Run the test when module is called as main
if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:05:01.893697
# Unit test for function shell_logger
def test_shell_logger():
    # Run shell_logger in a separate process, because it forks and that causes
    # the parent process to hang.
    from multiprocessing import Process
    import select
    import time
    import os

    def run_shell():
        shell_logger('/tmp/test.log')

    def wait_for_output(file, timeout):
        """
        Waits for the specified file to appear and returns its content
        """
        timeout_count = 0
        while timeout_count < timeout:
            if os.path.exists(file):
                with open(file, 'r') as content_file:
                    content = content_file.read()
                    content_file.close()
                    break
            time.sleep(1)
            timeout_count += 1
        else:
            raise TimeoutError

        return content


# Generated at 2022-06-14 09:05:03.923389
# Unit test for function shell_logger
def test_shell_logger():
    """
    This function works fine.
    """
    shell_logger('./test_shell_logger.log')

# Generated at 2022-06-14 09:05:17.914770
# Unit test for function shell_logger
def test_shell_logger():
    import time
    import subprocess
    import os
    import tempfile

    temp_fh = tempfile.NamedTemporaryFile(delete=False)
    temp_fh.close()
    temp_path = temp_fh.name
    print('temporary file name: %s' % temp_path)
    temp_path2 = temp_path + '2'
    print('temporary file name: %s' % temp_path2)
    try:
        import shell_logger
        reload(shell_logger)
    except:
        import sys
        src_path = os.path.abspath(sys.argv[0])
        if '.py' == src_path[-3:]:
            src_path = src_path[:-3]

# Generated at 2022-06-14 09:05:22.929691
# Unit test for function shell_logger
def test_shell_logger():
    with open('.test_shell_logger', 'w') as f:
        f.write('some data that shouldn\'t be here')
    shell_logger('.test_shell_logger')
    with open('.test_shell_logger') as f:
        assert f.read(const.LOG_SIZE_IN_BYTES) == b'\x00' * const.LOG_SIZE_IN_BYTES

# Generated at 2022-06-14 09:05:35.778811
# Unit test for function shell_logger
def test_shell_logger():
    class FakeFile(object):
        def __init__(self):
            self.data = []

        def write(self, data):
            self.data.append(data)

        def move(self, *a, **kw):
            pass

        def seek(self, *a, **kw):
            pass

    fake_file = FakeFile()

    data = [
        'abcdefg' * 1000,
        'abcdefg' * 1000,
        'abcdefg' * 1000,
        'abcdefg' * 150,
    ]

    def test_read(f, fd):
        d = data.pop(0)
        if not len(d):
            return ''
        f.write(d)
        return d

    _read(fake_file, 0, test_read)

# Generated at 2022-06-14 09:05:48.552382
# Unit test for function shell_logger
def test_shell_logger():
    import click
    import os
    import sys
    import subprocess
    
    @click.command()
    @click.option('--output', '-o', 'output', type=click.Path(dir_okay=False), required=True)
    def main(output):
        shell_logger(output)
    
    output = 'test.log'
    process = subprocess.Popen(['/usr/bin/env', 'python3', '-m', 'logs', 'shell', '-o', output], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process.stdin.write(b'test output')
    process.stdin.close()
    os.waitpid(process.pid, 0)
    assert(open(output).read() == 'test output')
    os

# Generated at 2022-06-14 09:05:53.669278
# Unit test for function shell_logger
def test_shell_logger():
    """Unit test for function shell_logger"""
    assert shell_logger(__file__) == 0, \
        "Function shell_logger works incorrect"


if __name__ == "__main__":
    shell_logger(sys.argv[1])

# Generated at 2022-06-14 09:06:01.516175
# Unit test for function shell_logger
def test_shell_logger():
    fd = os.open("test_shell.log", os.O_CREAT | os.O_TRUNC | os.O_RDWR)
    os.write(fd, b'\x00' * const.LOG_SIZE_IN_BYTES)
    buffer = mmap.mmap(fd, const.LOG_SIZE_IN_BYTES, mmap.MAP_SHARED, mmap.PROT_WRITE)
    return_code = _spawn("sh", partial(_read, buffer))

# Generated at 2022-06-14 09:06:10.961995
# Unit test for function shell_logger
def test_shell_logger():
    class _MockLogs(object):
        def warn(self, *args, **kwargs):
            self.warn_called = True

    logs = _MockLogs()
    def _spawn(*args, **kwargs):
        _spawn.called = True
        return 1

    def _kill_proc(*args, **kwargs):
        _kill_proc.called = True
        return 1

    sys.exit = lambda exit_code: exit_code
    sys.platform = 'win32'
    shell_logger('/tmp/test_shell_logger.log', logs=logs)
    assert logs.warn_called

    sys.platform = 'linux2'
    _spawn.called = False
    _kill_proc.called = False

# Generated at 2022-06-14 09:06:24.222241
# Unit test for function shell_logger
def test_shell_logger():
    original_shell = os.environ['SHELL']
    original_argv = sys.argv[:]

    os.environ['SHELL'] = 'cat'
    sys.argv = [sys.argv[0]]

    def exit_error(*args, **kwargs):
        raise SystemExit("test passed")

    sys.exit = exit_error
    shell_logger("/dev/null")

    sys.argv = original_argv
    os.environ['SHELL'] = original_shell

# Generated at 2022-06-14 09:06:33.002321
# Unit test for function shell_logger
def test_shell_logger():
    sys.argv[1] = 'shell_logger.log'
    shell_logger(sys.argv[1])

# Generated at 2022-06-14 09:06:42.653498
# Unit test for function shell_logger
def test_shell_logger():
    """Function should return return code of the program.

    We cant run shell to assert the output because shell_logger function
    starts new process with new tty.

    """
    with tempfile.NamedTemporaryFile() as f:
        exit_code = shell_logger(f.name)
        assert exit_code == 0
        with open(f.name, 'r') as f:
            assert f.read() == '\x00' * const.LOG_SIZE_IN_BYTES

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:06:46.132613
# Unit test for function shell_logger
def test_shell_logger():
    """Unit test for function shell_logger"""
    shell_logger("./test.log")

# Generated at 2022-06-14 09:06:53.857465
# Unit test for function shell_logger
def test_shell_logger():
    import subprocess
    import time
    from .. import logs as _logs
    from . import _tests
    from . import _coverage

    def _write_more(fd, data):
        os.write(fd, data.encode('utf8'))
        return b'\x00' * len(data.encode('utf8'))

    def _write_less(fd, data):
        return os.write(fd, data.encode('utf8'))

    def _test_shell_logger(shell_logger, master_read):
        fd = os.open(_tests.TEST_LOG,
                     os.O_CREAT | os.O_TRUNC | os.O_RDWR)

# Generated at 2022-06-14 09:06:55.529025
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('/tmp/test_shell_logger.log')

# Generated at 2022-06-14 09:06:56.188485
# Unit test for function shell_logger
def test_shell_logger(): pass

# Generated at 2022-06-14 09:06:56.922177
# Unit test for function shell_logger
def test_shell_logger():
    pass

# Generated at 2022-06-14 09:06:59.685852
# Unit test for function shell_logger
def test_shell_logger():
    """Test function shell_logger.

    If test fails, ValueError will be raised.

    """
    try:
        shell_logger('/tmp/shell_logger.log')
    except ValueError:
        pass

# Generated at 2022-06-14 09:07:00.263275
# Unit test for function shell_logger
def test_shell_logger():
    return True

# Generated at 2022-06-14 09:07:01.191887
# Unit test for function shell_logger
def test_shell_logger():
    """Do nothing
    """
    assert True

# Generated at 2022-06-14 09:07:08.452562
# Unit test for function shell_logger
def test_shell_logger():
    pass

# Generated at 2022-06-14 09:07:16.103776
# Unit test for function shell_logger
def test_shell_logger():
    """Check that shell_logger writes data from shell session to a file."""
    from ..utils import generate_temp_file
    from . import test_shell

    shell = test_shell.TestShell()
    output = generate_temp_file()
    shell_logger(output)

    with open(output, 'r') as r:
        assert r.readline() == const.EXAMPLE_INPUT_STRING + '\n'

# Generated at 2022-06-14 09:07:20.738010
# Unit test for function shell_logger
def test_shell_logger():
    def invoke():
        shell_logger('/tmp/test_shell_logger')
    os.environ['SHELL'] = '/bin/bash'
    invoke()
    assert os.path.exists('/tmp/test_shell_logger')
    os.unlink('/tmp/test_shell_logger')



# Generated at 2022-06-14 09:07:31.648433
# Unit test for function shell_logger
def test_shell_logger():
    # Use tty as a file for the logs.
    f = open('/dev/tty', 'r+b')
    # Set the log file size to 0 bytes.
    f.seek(0)
    # Write long sequence of zeros to the file.
    f.write(b'\x00' * const.LOG_SIZE_IN_BYTES)
    # Set the cursor to the beginning of the file.
    f.seek(0)
    # Create mapping from a file to a buffer.
    buffer = mmap.mmap(f.fileno(), const.LOG_SIZE_IN_BYTES, mmap.MAP_SHARED, mmap.PROT_WRITE)
    # Call shell_logger with a buffer as a parameter.

# Generated at 2022-06-14 09:07:32.212541
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger("/tmp/test_shell_logger.txt")
    assert True

# Generated at 2022-06-14 09:07:33.664333
# Unit test for function shell_logger
def test_shell_logger():
    from .logs import logger
    from .const import LOG_SIZE_IN_BYTES
    from .logs import LOG_FILE_NAME
    from .shells import shell_logger
    assert shell_logger == shell_logger



# Generated at 2022-06-14 09:07:34.737045
# Unit test for function shell_logger
def test_shell_logger():
    """Pytest unit test for function shell_logger"""
    assert shell_logger("test.log") is True

# Generated at 2022-06-14 09:07:42.094865
# Unit test for function shell_logger
def test_shell_logger():
    import subprocess
    import io
    import random
    import string
    import os

    F = io.StringIO()

    pid = os.fork()
    if pid == 0:
        fd = os.open('shell_logger_test', os.O_CREAT | os.O_TRUNC | os.O_RDWR)
        os.write(fd, b'\x00' * const.LOG_SIZE_IN_BYTES)
        buffer = mmap.mmap(fd, const.LOG_SIZE_IN_BYTES, mmap.MAP_SHARED, mmap.PROT_WRITE)
        return_code = _spawn(os.environ['SHELL'], partial(_read, buffer))

        sys.exit(return_code)
    else:
        new_env = os.environ

# Generated at 2022-06-14 09:07:43.897740
# Unit test for function shell_logger
def test_shell_logger():
    logger = shell_logger('/tmp/shell_logger.log')
    pass

# Generated at 2022-06-14 09:07:56.763383
# Unit test for function shell_logger
def test_shell_logger():
    """Test both logging and session recording.

    1. Start logging and recording session and perform some commands.
    2. Terminate session and check output log.
    3. Start new session and check the tty size.

    """
    shell = os.environ.get('SHELL', '/bin/sh')
    commands = ('echo "hello"\n', 'echo "world"\n', 'echo "foo"\n', 'echo "bar"\n')

    # Create script file
    script_name = 'test_login.log'
    pid = os.fork()
    if not pid:
        shell_logger(script_name)

    # Open script file
    path = os.path.join(os.getcwd(), script_name)
    fd = os.open(path, os.O_RDWR)

# Generated at 2022-06-14 09:08:12.719659
# Unit test for function shell_logger
def test_shell_logger():
    # Test for shell logger with no stdin
    logs.clear_logs_path()
    shell_logger(logs.log_path('test_shell'))

    with open(logs.log_path('test_shell'), 'rb') as f:
        lines = f.readlines()
    assert lines[-1].endswith(b'\n')
    assert lines[-2].endswith(b'\n')
    assert lines[-1].startswith(b'exit')
    assert lines[-2].startswith(b'ls')

    # Test for shell logger with stdin
    logs.clear_logs_path()

# Generated at 2022-06-14 09:08:22.250742
# Unit test for function shell_logger
def test_shell_logger():
    import unittest
    import os
    import mmap
    import subprocess
    import tempfile
    import shutil
    import time
    import pty

    class ShellLoggerTest(unittest.TestCase):
        def __init__(self, methodName='runTest'):
            super().__init__(methodName)
            self.tmpdir = None

        def setUp(self):
            self.tmpdir = tempfile.mkdtemp()

        def tearDown(self):
            shutil.rmtree(self.tmpdir)

        def test_log(self):
            log_path = os.path.join(self.tmpdir, 'shell.log')
            pty.spawn(os.path.abspath(sys.argv[0]) + ' shell_logger ' + log_path)
           

# Generated at 2022-06-14 09:08:32.082650
# Unit test for function shell_logger
def test_shell_logger():
  from ..logs import get_output_folder
  from ..console import _command_is_available
  from ..console import BOLD, ENDC
  sys.argv = ['shell_logger.py']
  logs.init(debug_mode=True, output_folder=get_output_folder())
  print("%sHello world!%s" % (BOLD, ENDC))
  if len(sys.argv) == 1:
    logs.warn("No input file to process.")
    sys.exit(1)
  input_file = 'shell.out'
  shell_logger(input_file)

# Generated at 2022-06-14 09:08:43.257268
# Unit test for function shell_logger
def test_shell_logger():
    from ...test import assert_error, assert_not_error, assert_equal
    from ...utils import std_streams
    assert_not_error(shell_logger, 'log.txt')
    assert std_streams.stderr.getvalue().startswith('Shell logger doesn\'t support your platform.')
    del std_streams.stderr.buffer[:]

    assert_not_error(shell_logger, 'log.txt', env={'SHELL': '/bin/bash'})
    assert os.path.exists('log.txt')
    assert os.path.getsize('log.txt') == const.LOG_SIZE_IN_BYTES
    for _ in range(3):
        assert_equal(shell_logger('log.txt', env={'SHELL': '/bin/bash'}), 0)

# Generated at 2022-06-14 09:08:55.846576
# Unit test for function shell_logger
def test_shell_logger():
    os.environ['SHELL'] = 'sh'
    with tempfile.NamedTemporaryFile() as output:
        with patch('os.execvp') as execvp:
            shell_logger(output.name)
        execvp.assert_called_once_with('sh', ['sh'])

        size_in_bytes = const.LOG_SIZE_IN_BYTES
        os.write(execvp.call_args[0][1][1], b'1'*size_in_bytes)
        output.flush()
        output.seek(0)
        assert output.read() == b'1' * const.LOG_SIZE_TO_CLEAN + b'\x00' * (size_in_bytes - const.LOG_SIZE_TO_CLEAN)

# Generated at 2022-06-14 09:09:08.443666
# Unit test for function shell_logger
def test_shell_logger():
    def assert_file_eq(path, expected):
        with open(path, 'r') as f:
            assert f.read() == expected

    def assert_file_contains(path, expected):
        with open(path, 'r') as f:
            assert expected in f.read()

    def remove_file(path):
        os.remove(path)


# Generated at 2022-06-14 09:09:11.423335
# Unit test for function shell_logger
def test_shell_logger():
    print('Testing shell_logger')
    os.environ['SHELL'] = '/bin/bash'
    # if this fails, the tests will fail
    assert(os.environ.get('SHELL')) 
    shell_logger('test_shell_logger.txt')

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:09:12.576264
# Unit test for function shell_logger
def test_shell_logger():
    pass
# === shell_logger ===

# Generated at 2022-06-14 09:09:20.106894
# Unit test for function shell_logger
def test_shell_logger():
    """Tests shell_logger function.
    """
    from .. import cli
    from . import utils

    with utils.redirect_stdout_to_memory() as stdout:
        cli.main(['shell-logger', 'test_file'])
        assert stdout.getvalue().strip() == logs.warning("Shell logger doesn't support your platform.")


# Generated at 2022-06-14 09:09:21.718763
# Unit test for function shell_logger
def test_shell_logger():
    assert shell_logger('log') == 0

# Generated at 2022-06-14 09:09:33.367478
# Unit test for function shell_logger
def test_shell_logger():
    filename = os.path.dirname(__file__) + '/test_output'
    stdout_file = os.open(filename, os.O_CREAT | os.O_TRUNC | os.O_RDWR)
    os.dup2(stdout_file, 1)
    shell_logger(filename)
    #os.close(stdout_file)

# Generated at 2022-06-14 09:09:35.944528
# Unit test for function shell_logger
def test_shell_logger():
    assert shell_logger(__file__) == 0



# Generated at 2022-06-14 09:09:47.840933
# Unit test for function shell_logger
def test_shell_logger():
    from io import StringIO
    from .. import logs
    from . import utils

    test_file = utils.TestFile('test_shell_logger_tmp')

    # no shell
    logger = logs.get_logger('tests.modules.logs')
    logger.info('start')
    logger.remove_all_handlers()

    os.environ.pop('SHELL', None)

    with StringIO() as buf:
        with logs.redirect_stdout(buf):
            shell_logger(test_file.path)
        assert buf.getvalue().startswith('Shell logger doesn\'t support your platform')

    assert os.path.isfile(test_file.path)
    os.remove(test_file.path)

    # simple test

# Generated at 2022-06-14 09:09:55.314197
# Unit test for function shell_logger
def test_shell_logger():
    message = b'Hello world\n'
    with NamedTemporaryFile() as f:
        with mock.patch('os.read', return_value=message):
            with mock.patch('os.execlp'):
                shell_logger(f.name)
        f.seek(0)
        assert f.read() == message

if __name__ == "__main__":
    test_shell_logger()

# Generated at 2022-06-14 09:10:07.545319
# Unit test for function shell_logger
def test_shell_logger():
    import sys, subprocess
    sys.stdout.write(b'foo\n')
    sys.stderr.write(b'bar\n')
    subprocess.Popen(
        '{} -c "import sys, gdbgui.logs; sys.stdout.write(b\'foo\n\'); '
        'sys.stderr.write(b\'bar\n\'); sys.exit(1)"'.format(
            sys.executable
        ),
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    ).communicate()

    try:
        import tempfile
        with tempfile.NamedTemporaryFile() as temp:
            shell_logger(temp.name)
    except:
        pass


# Generated at 2022-06-14 09:10:11.174469
# Unit test for function shell_logger
def test_shell_logger():
    """Main function for unit testing"""
    file_name = 'shell_logger.test'
    shell_logger(file_name)
    content = open(file_name).readlines()
    os.remove(file_name)
    return content

if __name__ == "__main__":
    test_shell_logger()

# Generated at 2022-06-14 09:10:12.887786
# Unit test for function shell_logger
def test_shell_logger():
    assert shell_logger('unit.test.log')==0

# Generated at 2022-06-14 09:10:19.798488
# Unit test for function shell_logger
def test_shell_logger():
    """Test `shell_logger`.

    Create a new process, which logs it's shell output to a file.
    Then checks if this file has the correct size, and has something
    in it.

    """
    import os
    import signal
    import subprocess
    import time
    import unittest
    LOG_FILE = 'testlog.log'

    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

    process = subprocess.Popen(['python', __file__, LOG_FILE])

    time.sleep(3)
    os.kill(process.pid, signal.SIGKILL)
    process.wait()

    class Test(unittest.TestCase):
        def test_shell(self):
            print(os.stat(LOG_FILE))
            self.assertTrue

# Generated at 2022-06-14 09:10:23.203756
# Unit test for function shell_logger
def test_shell_logger():
    """The unit test for the shell_logger function
    """
    # TODO: to be written
    print("test_shell_logger:")
    pass

# Generated at 2022-06-14 09:10:29.669526
# Unit test for function shell_logger
def test_shell_logger():
    # type: () -> None
    """Unit test for function shell_logger"""
    import os
    import shutil
    import tempfile
    import unittest
    from ..logs import set_verbosity

    from .. import test_utils

    try:
        import pty
    except ImportError:
        raise unittest.SkipTest("pty not available on this system")

    try:
        import mmap
    except ImportError:
        raise unittest.SkipTest("mmap not available on this system")

    try:
        import fcntl
    except ImportError:
        raise unittest.SkipTest("fcntl not available on this system")

    try:
        import termios
    except ImportError:
        raise unittest.SkipTest("termios not available on this system")

    import tty
   

# Generated at 2022-06-14 09:10:42.080710
# Unit test for function shell_logger
def test_shell_logger():
    filename = "test.log"
    shell_logger(filename)
    with open(filename, "r") as file:
        assert(file.read()=='')
    os.remove(filename)

# Generated at 2022-06-14 09:10:42.964909
# Unit test for function shell_logger
def test_shell_logger():
    assert True

# Generated at 2022-06-14 09:10:54.213095
# Unit test for function shell_logger
def test_shell_logger():
    """Test case for shell logger."""
    import subprocess

    filename = '/tmp/ptyrec/test_shell_logger'
    output_data = b'Test message'
    env = os.environ.copy()
    env['SHELL'] = '/bin/bash'
    env['PYTHONPATH'] = '.'
    cmd = ['python', '-m', 'ptyrec.api.loggers', filename]
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE, env=env)
    process.stdin.write(output_data)
    process.stdin.close()
    process.wait()
    assert process.returncode == 0
    assert os.path.exists(filename)
    assert os.stat(filename).st

# Generated at 2022-06-14 09:10:58.308113
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile
    from . import _test_logger_log
    output = tempfile.mkstemp()[1]
    shell_logger(output)
    assert _test_logger_log(output)

# Generated at 2022-06-14 09:11:07.732708
# Unit test for function shell_logger
def test_shell_logger():
    import subprocess
    import time
    import select

    print("Unit test for function shell_logger")
    response = b"Are you root ?\n"
    proc = subprocess.Popen(
        ['python -m archinfo.shell_logger archinfo/test.log'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        shell=True)

    proc.stdin.write(response)
    end_time = time.time() + 2
    while time.time() <= end_time:
        if select.select([proc.stdout], [], [], 0.0)[0]:
            try:
                print(proc.stdout.read(1))
            except:
                pass
    proc.kill()

# Generated at 2022-06-14 09:11:18.378850
# Unit test for function shell_logger
def test_shell_logger():
    import io
    import unittest
    import random
    import contextlib
    import os.path

    def execute(text):
        return text.encode('utf-8')

    class TestCase(unittest.TestCase):

        def __init__(self, *args, **kwargs):
            super(TestCase, self).__init__(*args, **kwargs)
            self.output = None
            self.buffer = None
            self.__create_file()

        def __create_file(self):
            _, self.output = tempfile.mkstemp()
            self.buffer = array.array('h', [0] * const.LOG_SIZE_IN_BYTES)

        def __get_buffer_text(self):
            with open(self.output, 'rb') as f:
                f.read

# Generated at 2022-06-14 09:11:27.337421
# Unit test for function shell_logger
def test_shell_logger():
    os.environ['SHELL'] = 'ls'
    buffer_fd = os.open(logs._LOG_NAME, os.O_CREAT | os.O_TRUNC | os.O_RDWR)
    os.write(buffer_fd, b'\x00' * const.LOG_SIZE_IN_BYTES)
    buffer = mmap.mmap(buffer_fd, const.LOG_SIZE_IN_BYTES, mmap.MAP_SHARED, mmap.PROT_WRITE)
    return_code = _spawn(os.environ['SHELL'], partial(_read, buffer))
    assert return_code == 0

# Generated at 2022-06-14 09:11:31.541931
# Unit test for function shell_logger
def test_shell_logger():
    """Tests shell logging function."""
    assert shell_logger('./test_shell_output.log') == 0


if __name__ == '__main__':
    shell_logger('./test_shell_output.log')

# Generated at 2022-06-14 09:11:43.465977
# Unit test for function shell_logger
def test_shell_logger():
    import shutil
    import subprocess
    import tempfile

    # Create temporary test directory.
    workdir = tempfile.mkdtemp(prefix='srptest_')

    # Create temporary output file.
    logs_path = os.path.join(workdir, 'output')

    # Start shell logger.
    try:
        p = subprocess.Popen([
            'python', '-c',
            'from srp import main; main.shell_logger("{}")'.format(logs_path)
        ])
        p.wait()
    except KeyboardInterrupt:
        pass

    # Check if logs are stored in temporary output file.
    with open(logs_path, 'rb') as f:
        logs_content = f.read()
        assert b'srptest_' in logs_content

# Generated at 2022-06-14 09:11:51.281663
# Unit test for function shell_logger
def test_shell_logger():
    import mock
    import subprocess

    with mock.patch('pexpect.spawn') as mock_spawn:
        shell_logger('./log_test')
        mock_spawn.assert_called_once_with(['bash'])

    def _test():
        return_code = subprocess.call(['bash'])
        if return_code != 0:
            return False
        return True

    assert _test()

# Generated at 2022-06-14 09:12:03.505657
# Unit test for function shell_logger
def test_shell_logger():
    for shell in const.SUPPORTED_SHELLS:
        os.environ['SHELL'] = shell
        return_code = shell_logger('some_file')
        assert return_code == 0

# Generated at 2022-06-14 09:12:15.723222
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile
    import shutil
    import subprocess

    temp_dir = tempfile.mkdtemp()
    output = os.path.join(temp_dir, 'output')

    def run_shell(command):
        subprocess.call(
            command,
            shell=True,
            executable=os.environ['SHELL']
        )

    def parse_log(output):
        with open(output, 'rb') as f:
            data = f.read(const.LOG_SIZE_IN_BYTES)
            return data.replace(b'\x00', b'').decode('utf-8')


# Generated at 2022-06-14 09:12:16.777759
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('test.log')

# Generated at 2022-06-14 09:12:32.873303
# Unit test for function shell_logger
def test_shell_logger():
    """shell_logger(str) => void"""
    import traceback
    import unittest
    import shutil
    from tempfile import mkdtemp

    class TempDirTest(unittest.TestCase):
        def setUp(self):
            self.tempdir = mkdtemp()

        def tearDown(self):
            shutil.rmtree(self.tempdir)

    class TestShellLogger(TempDirTest):
        def test_shell_logger(self):
            tempfile = self.tempdir + '/log.txt'
            shell_logger(tempfile)
            with open(tempfile) as f:
                self.assertEqual(b'\0' * const.LOG_SIZE_IN_BYTES, f.read())


# Generated at 2022-06-14 09:12:35.511970
# Unit test for function shell_logger
def test_shell_logger():
    # TODO implement
    return

if __name__ == "__main__":
    test_shell_logger()

# Generated at 2022-06-14 09:12:49.118448
# Unit test for function shell_logger
def test_shell_logger():
    def read(file, size):
        return os.read(file, size)

    buffer = []
    def _read(f, fd):
        data = os.read(fd, 1024)
        try:
            buffer.append(data)
        except ValueError:
            pass
        return data

    import tempfile

    with tempfile.TemporaryDirectory() as tmpdirname:
        output = os.path.join(tmpdirname, 'shell.log')
        fd = os.open(output, os.O_CREAT | os.O_TRUNC | os.O_RDWR)
        os.write(fd, b'\x00' * const.LOG_SIZE_IN_BYTES)

# Generated at 2022-06-14 09:13:01.192921
# Unit test for function shell_logger
def test_shell_logger():
    """Units tests for function shell_logger.

    To run it:

        python -m lgr.main test_shell_logger

    """
    import os
    import pty
    import signal
    import sys
    import termios
    import tty

    from . import logs

    DEV_NULL = os.devnull
    if sys.version_info >= (3, 3):
        DEV_NULL = os.null
    if os.path.isabs(DEV_NULL):
        DEV_NULL = DEV_NULL[1:]

    logs.debug('Running shell_logger test...')

    pid, master_fd = pty.fork()
    if pid == pty.CHILD:
        os.execlp('lgr', 'lgr', 'shell_logger', DEV_NULL)

# Generated at 2022-06-14 09:13:02.373971
# Unit test for function shell_logger
def test_shell_logger():
    assert False, "Test was not implemented"

# Generated at 2022-06-14 09:13:03.085542
# Unit test for function shell_logger
def test_shell_logger():
    assert False

# Generated at 2022-06-14 09:13:04.802716
# Unit test for function shell_logger
def test_shell_logger():
    assert shell_logger('/tmp/test.script') == 0

# Generated at 2022-06-14 09:13:15.381447
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('/tmp/test_shell.log')

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:13:16.052017
# Unit test for function shell_logger
def test_shell_logger():
    pass

# Generated at 2022-06-14 09:13:24.494244
# Unit test for function shell_logger
def test_shell_logger():
    get_size = lambda file: os.stat(file).st_size
    size_to_remove = 32

    fd = os.open('shell.log', os.O_CREAT | os.O_WRONLY | os.O_TRUNC)
    os.write(fd, b'\x00' * (const.LOG_SIZE_IN_BYTES + size_to_remove))
    buffer = mmap.mmap(fd, const.LOG_SIZE_IN_BYTES + size_to_remove, mmap.MAP_SHARED, mmap.PROT_WRITE)
    os.close(fd)

    buffer.write(b'1' * (const.LOG_SIZE_IN_BYTES + size_to_remove - const.LOG_SIZE_TO_CLEAN + 1))

    _read

# Generated at 2022-06-14 09:13:33.976101
# Unit test for function shell_logger
def test_shell_logger():
    """Tests `shell_logger` function.

    1. Starts shell logger.
    2. Starts opened shell in the background.
    3. Sends a few commands to the second shell.
    4. Checks output for "commands"

    """
    import subprocess

    # 1. Starts shell logger.
    command = ['python', '-c', 'from ecrterm import logging; logging.shell_logger("{}")'.format(const.LOG_FILE)]
    process = subprocess.Popen(
        command, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    # 2. Starts opened shell in the background.
    command = ['bash']

# Generated at 2022-06-14 09:13:44.008524
# Unit test for function shell_logger
def test_shell_logger():
    filesize = const.LOG_SIZE_IN_BYTES - const.LOG_SIZE_TO_CLEAN - 1
    f = open('test_data', 'w')
    f.write('0123456789')
    f.seek(0)
    buffer = mmap.mmap(f.fileno(), filesize, mmap.MAP_SHARED, mmap.PROT_WRITE)
    _read(buffer, f.fileno())
    buffer.seek(const.LOG_SIZE_TO_CLEAN)
    assert buffer.read(10) == b'0123456789'

# Generated at 2022-06-14 09:13:54.487455
# Unit test for function shell_logger
def test_shell_logger():
    import io
    import os
    import tempfile


    def log_file(filename):
        def decorator(func):
            def wrapper(*args, **kwargs):
                with tempfile.TemporaryDirectory() as tmpdir:
                    with io.open(os.path.join(tmpdir, filename), 'wb') as f:
                        func(f)

            return wrapper

        return decorator


    @log_file('log')
    def _(f):
        shell_logger(f.name)

    @log_file('log.gz')
    def _(f):
        shell_logger(f'{f.name}{const.COMPRESS_EXTENSION}')
