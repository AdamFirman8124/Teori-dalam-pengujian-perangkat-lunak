

# Generated at 2022-06-14 09:04:08.573429
# Unit test for function shell_logger
def test_shell_logger():
    """Unit test for function shell_logger."""
    import tempfile
    import multiprocessing
    import os

# Generated at 2022-06-14 09:04:11.253385
# Unit test for function shell_logger
def test_shell_logger():
    """ test function shell_logger
    """
    os.environ['SHELL'] = '/bin/bash'
    shell_logger('/tmp_shell_logger_test.log')

# Generated at 2022-06-14 09:04:23.638462
# Unit test for function shell_logger
def test_shell_logger():
    import os
    import uuid

    file_path = '/tmp/' + str(uuid.uuid4())
    try:
        shell_logger(file_path)

        assert os.path.isfile(file_path) is True, 'File not created.'

        file_size = os.stat(file_path).st_size
        assert file_size >= const.LOG_SIZE_TO_CLEAN, 'File is too small.'

        buffer = mmap.mmap(os.open(file_path, os.O_RDONLY), file_size)
        assert buffer.readline().startswith(b'Script started'), 'Script output is different.'
    finally:
        os.remove(file_path)

# Generated at 2022-06-14 09:04:25.953048
# Unit test for function shell_logger
def test_shell_logger():
    import doctest
    return doctest.testmod()

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:04:37.412203
# Unit test for function shell_logger
def test_shell_logger():
    from .. import logs

    def tty_size():
        if os.environ.get('SHELL'):
            buf = array.array('h', [0, 0, 0, 0])
            fcntl.ioctl(pty.STDOUT_FILENO, termios.TIOCGWINSZ, buf, True)
            return buf[:2]

    test_output = '/tmp/test_shell_logger_'

# Generated at 2022-06-14 09:04:42.198757
# Unit test for function shell_logger
def test_shell_logger():
    from . import messages

    def get_shell_logger_output(output):
        return open(output, 'r').read()

    messages.program_start_msg(messages.program_name)
    output = '/tmp/shell_logger.log'
    messages.shell_logger_message(output)
    proc = subprocess.Popen('shell_logger /tmp/shell_logger.log',
                            stdout=subprocess.PIPE,
                            shell=True)
    output = get_shell_logger_output(output)
    assert b"$ " in output
    os.remove(output)
    proc.terminate()

# Generated at 2022-06-14 09:04:48.745881
# Unit test for function shell_logger
def test_shell_logger():
    # create output file
    output = "test_shell_logger_" + str(int(time.time()))
    os.system("touch " + output)
    shell_logger(output)
    with open(output) as file:
        data = file.read()
    assert "test_command_logger" in data
    os.system("rm -rf " + output)

# Generated at 2022-06-14 09:05:02.883139
# Unit test for function shell_logger
def test_shell_logger():
    "Tests the shell logger"
    import unittest
    import tempfile
    import os

    class TestShellLogger(unittest.TestCase):
        """Test class"""

        def __init__(self, *args, **kwargs):
            super(TestShellLogger, self).__init__(*args, **kwargs)
            self.echo = 'hello world'
            self.output = tempfile.mkstemp()[1]

        def tearDown(self):
            os.unlink(self.output)

        def test_shell_logger(self):
            """Test shell logger"""
            shell_logger(output=self.output)

# Generated at 2022-06-14 09:05:13.961373
# Unit test for function shell_logger
def test_shell_logger():
    command = 'echo string'

    # Create dummy file to write resulting output
    fd = os.open(shell_logger.__module__ + '_output.txt', os.O_CREAT | os.O_TRUNC | os.O_RDWR)
    os.write(fd, b'\x00' * const.LOG_SIZE_IN_BYTES)
    buffer = mmap.mmap(fd, const.LOG_SIZE_IN_BYTES, mmap.MAP_SHARED, mmap.PROT_WRITE)

    # Run command
    return_code = _spawn(command, partial(_read, buffer))

    # Assert that return code is zero
    assert(return_code == 0)

    # Assert that command was written to file

# Generated at 2022-06-14 09:05:21.814046
# Unit test for function shell_logger
def test_shell_logger():
    """Method to unit test shell_logger function"""
    try:
        output="myoutput.txt"
        if os.path.exists(output):
            os.remove(output)
        shell_logger(output)
        assert os.path.exists(output)
        f = open(output)
        data = f.read()
        assert 'terminal-recorder' in data
        assert 'shell_logger.py' in data
        f.close()
    except:
        assert 0

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:05:31.522750
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('test_shell_logger.txt')

if __name__ == '__main__':
    print('Run unit tests for this module: python -m unittest -v storjnode.shell_logger')

# Generated at 2022-06-14 09:05:43.153769
# Unit test for function shell_logger
def test_shell_logger():
    import subprocess
    import os
    import time
    import mmap
    import platform

    # Linux and Mac OS X only support
    if platform.system() == "Linux":
        test_path = os.path.join(os.getcwd(), 'test.txt')
        if (os.path.isfile(test_path)):
            os.remove(test_path)
        subprocess.Popen(['python', '-c', 'from shell_logger import shell_logger; shell_logger("test.txt")'], shell=False)
        cmd = ['echo', 'test']
        subprocess.call(cmd)
        time.sleep(1)
        fd = os.open(test_path, os.O_RDWR)

# Generated at 2022-06-14 09:05:51.848879
# Unit test for function shell_logger
def test_shell_logger():
    import os

    output = 'shell.log'

    if os.path.exists(output):
        os.remove(output)

    assert not os.path.exists(output)

    try:
        shell_logger(output)
    except SystemExit as e:
        return_code = e.code

    assert return_code == 0
    assert os.path.exists(output)


if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:05:55.091890
# Unit test for function shell_logger
def test_shell_logger():
    os.environ['SHELL'] = '/bin/bash'
    shell_logger('test_shell_logger_output.txt')

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:06:06.969162
# Unit test for function shell_logger
def test_shell_logger():
    from .. import __version__
    from . import utils

    logs.silence()
    output = utils.tmp_file()
    shell_logger(output)
    buffer = mmap.mmap(os.open(output, os.O_RDONLY), const.LOG_SIZE_IN_BYTES, mmap.MAP_SHARED, mmap.PROT_READ)
    assert utils.find_between(buffer, b'Starting ', b' ') == __version__
    assert buffer.find(b'$ ') > 0
    assert utils.find_between(buffer, b'Switching to directory: ', b'\n') == os.getcwd()


if __name__ == '__main__':
    utils.execute_only_in_main()
    test_shell_logger()


# Generated at 2022-06-14 09:06:13.437283
# Unit test for function shell_logger
def test_shell_logger():
    """
    Unit test for shell logging
    """
    with tempfile.NamedTemporaryFile() as tmpfile:
        shell_logger(tmpfile.name)
        with open(tmpfile.name, 'r') as logfile:
            data = logfile.read()
            assert data

# Generated at 2022-06-14 09:06:18.878041
# Unit test for function shell_logger
def test_shell_logger():
    from .. import utils

    name = utils.create_random_file()
    try:
        shell_logger(name)
    except SystemExit as e:
        pass
    assert const.LOG_SIZE_IN_BYTES == os.path.getsize(name)
    os.unlink(name)

# Generated at 2022-06-14 09:06:27.912915
# Unit test for function shell_logger
def test_shell_logger():
    from . import temp
    import shutil
    file_path = temp.new_file()
    with open(file_path, 'wb') as _file:
        _file.write(b'\x00' * const.LOG_SIZE_IN_BYTES)
    shell_logger(file_path)
    assert os.stat(file_path).st_size == const.LOG_SIZE_IN_BYTES
    shutil.rmtree(os.path.dirname(file_path), ignore_errors=True)

# Generated at 2022-06-14 09:06:32.306957
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile
    name = tempfile.mkstemp()[1]

    os.system("echo 'Hello world!' | python -m logbook.scripts.shell_logger " + name)

    f = open(name, 'r')
    data = f.read()
    f.close()

    os.remove(name)

    assert data == 'Hello world!\n', 'Failed to log output.'

# Generated at 2022-06-14 09:06:33.833862
# Unit test for function shell_logger
def test_shell_logger():
    logs.debug("Testing shell_logger")
    assert shell_logger(const.CATCHALL_LOG) == 1

# Generated at 2022-06-14 09:06:44.969436
# Unit test for function shell_logger
def test_shell_logger():
    import os
    import tempfile
    try:
        tmpf = tempfile.NamedTemporaryFile(delete=False)
        filename = tmpf.name
        shell_logger(filename)
        filesize = os.path.getsize(filename)
    finally:
        os.unlink(filename)
    assert(1048576 == filesize)

# Generated at 2022-06-14 09:06:53.207837
# Unit test for function shell_logger
def test_shell_logger():
    """Create a spawned process.

    Modified version of pty.spawn with terminal size support.

    """

    import fcntl
    import os
    import pty
    import sys
    import termios
    import tty
    import unittest

    class TestShellLogger(unittest.TestCase):
        """Shell logger tests"""

        def test_shell_logger(self, shell='/bin/bash'):
            """Shell logger test"""

            fd = os.open('/tmp/shell_logger_test', os.O_CREAT | os.O_TRUNC | os.O_RDWR)
            os.write(fd, b'\x00' * const.LOG_SIZE_IN_BYTES)

# Generated at 2022-06-14 09:06:54.964871
# Unit test for function shell_logger
def test_shell_logger():
    with tempfile.NamedTemporaryFile() as temp:
        shell_logger(temp.name)
        eq_(temp.read(), '\x00' * const.LOG_SIZE_IN_BYTES)



# Generated at 2022-06-14 09:07:02.653692
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile
    import shutil
    import time
    import subprocess

    def check(path):
        with open(path) as f:
            contents = f.read()
        assert contents == 'test_shell_logger'

    path = tempfile.mkstemp()[1]
    try:
        time.sleep(1)
        subprocess.call(['sudo', sys.executable, __file__, 'shell_logger', path])
        time.sleep(1)
        check(path)
    finally:
        shutil.rmtree(path)


if __name__ == '__main__':
    shell_logger(sys.argv[2])

# Generated at 2022-06-14 09:07:10.579702
# Unit test for function shell_logger
def test_shell_logger():
    """Unit test for shell_logger"""
    import subprocess
    import tempfile
    import time
    with tempfile.NamedTemporaryFile(prefix='vitables-test-') as shell_file:
        subprocess.Popen(['python', '-m', 'vitables.logs.shell', shell_file.name])
        time.sleep(1)
        subprocess.call('echo test-logs-shell-logger', shell=True)
        time.sleep(1)
        print(shell_file.read().decode())

if __name__ == '__main__':
    shell_logger(sys.argv[1])

# Generated at 2022-06-14 09:07:21.516432
# Unit test for function shell_logger
def test_shell_logger():
    with mock.patch('sys.exit') as se, mock.patch.object(logs, 'warn') as warn, mock.patch.dict(os.environ):
        os.environ['SHELL'] = False
        shell_logger('/some/path/file')
        warn.assert_called_once_with("Shell logger doesn't support your platform.")
        se.assert_called_once_with(1)
        warn.reset_mock()
        se.reset_mock()

        def raise_tty_error(*args):
            raise tty.error

        # NOTE: pytest.monkeypatch.setenv is used instead of os.environ.get
        # to pass check for fork() in pty.spawn
        pytest.monkeypatch.setenv('SHELL', 'a')

# Generated at 2022-06-14 09:07:25.594284
# Unit test for function shell_logger
def test_shell_logger():
    import os
    import tempfile

    with tempfile.NamedTemporaryFile() as tmp:
        shell_logger(tmp.name)
        assert os.stat(tmp.name).st_size == 10 * 1024 * 1024


# Generated at 2022-06-14 09:07:34.473902
# Unit test for function shell_logger
def test_shell_logger():
    # This tests will spawn a subshell, so you need to run it manually.
    # Shell logger doesn't support TravisCI well, so it will be enabled
    # after the build system is changed.
    if 'TRAVIS' in os.environ:
        return
    output = 'out.log'
    if os.path.isfile(output):
        os.unlink(output)
    shell_logger(output)
    if os.path.isfile(output):
        os.unlink(output)

# Generated at 2022-06-14 09:07:34.910926
# Unit test for function shell_logger
def test_shell_logger():
    pass

# Generated at 2022-06-14 09:07:46.004710
# Unit test for function shell_logger
def test_shell_logger():
    import os
    import sys

    fname = 'shell_logger.log'
    if os.path.isfile(fname):
        os.remove(fname)

    args = [ sys.executable ]
    args.extend([ '-c', 'from py_shell_logger import command; command.shell_logger("{}")'.format(fname) ])
    p = os.spawnlpe(os.P_WAIT, args[0], args[0], *args[1:])

    if os.path.isfile(fname):
        os.remove(fname)
    else:
        assert False

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:07:53.401050
# Unit test for function shell_logger
def test_shell_logger():
    os.environ = {'SHELL':'/bin/bash'}
    assert shell_logger('output.text') == 0

# Generated at 2022-06-14 09:08:06.605920
# Unit test for function shell_logger
def test_shell_logger():
    import random

    class MockArgs:
        output = 'mock_args'

    def mock_sys_exit(status):
        assert status == 0

    def mock_warn(msg):
        pass

    def mock_spawn(shell, master_read):
        assert shell == 'bash'
        return 0

    def mock_os_write(fd, data):
        assert fd == 42
        assert data == b'\x00' * const.LOG_SIZE_IN_BYTES

    def mock_mmap(fd, size, *args):
        class MockMMap(object):
            def write(self, data):
                assert data == b'This is a test'

        assert fd == 42
        assert size == const.LOG_SIZE_IN_BYTES
        return MockMMap()

    globals()['os']

# Generated at 2022-06-14 09:08:13.970426
# Unit test for function shell_logger
def test_shell_logger():
    stdout_fd = os.dup(sys.stdout.fileno())
    stderr_fd = os.dup(sys.stderr.fileno())
    tmp_fd = os.open('/tmp/out', os.O_CREAT | os.O_TRUNC | os.O_RDWR)
    os.dup2(tmp_fd, sys.stdout.fileno())
    os.dup2(tmp_fd, sys.stderr.fileno())

    shell_logger('/tmp/log')

    os.dup2(stdout_fd, sys.stdout.fileno())
    os.dup2(stderr_fd, sys.stderr.fileno())
    os.close(stdout_fd)
    os.close(stderr_fd)


# Generated at 2022-06-14 09:08:27.354186
# Unit test for function shell_logger
def test_shell_logger():
    import subprocess
    import os
    import mmap
    import os
    import time
    import sys
    import shutil
    import tempfile
    import string
    import ddt
    import traceback

    @ddt.ddt
    class ShellLoggerTest(object):
        """Test class for shell_logger."""
        log_size_in_bytes = const.LOG_SIZE_IN_BYTES
        log_size_to_clean = const.LOG_SIZE_TO_CLEAN
        output_file = "/tmp/log_test_output"
        log_file = output_file + ".log"

        def setUp(self):
            os.environ['SHELL'] = "/bin/bash"
            self.output_file = self.__class__.output_file

# Generated at 2022-06-14 09:08:35.238343
# Unit test for function shell_logger
def test_shell_logger():
    import pytest
    import os
    import subprocess
    import tempfile
    import datetime
    import time
    import mmap
    import itertools
    import shutil
    import binascii
    import io

    # Enable logs
    import app.logs
    app.logs.set_verbosity(app.logs.DEBUG)

    def load_mmap(file, max_len):
        mmap_file = mmap.mmap(file.fileno(), max_len,
                              mmap.MAP_SHARED, mmap.PROT_READ)
        file_content = bytearray(os.read(file.fileno(), max_len))
        file_content.extend(mmap_file)
        return file_content

    # Temporary directory for test files

# Generated at 2022-06-14 09:08:36.412796
# Unit test for function shell_logger
def test_shell_logger():
    assert shell_logger('/dev/null') == None

# Generated at 2022-06-14 09:08:39.251323
# Unit test for function shell_logger
def test_shell_logger():
    fd, path = mkstemp()
    try:
        os.close(fd)
        shell_logger(path)
    finally:
        os.remove(path)

# Generated at 2022-06-14 09:08:43.353355
# Unit test for function shell_logger
def test_shell_logger():
    assert 1 == shell_logger('test_output')
    assert 1 == shell_logger('test_output')

# vim: sw=4 sts=4 et

# Generated at 2022-06-14 09:08:51.498738
# Unit test for function shell_logger
def test_shell_logger():
    # Execute shell_logger
    output_file_name = 'test_shell_logger_output'
    shell_logger(output_file_name)

    # Check if output file exists
    assert os.path.isfile(output_file_name)

    # Read output file
    with open(output_file_name, 'r') as output_file:
        output_content = output_file.read()

    # Errors
    if not output_content:
        error_msg = 'Empty shell logger output.'
        print(error_msg)
        raise Exception(error_msg)

# Generated at 2022-06-14 09:08:53.574106
# Unit test for function shell_logger
def test_shell_logger():
    """Test to see if shell_logger works."""
    shell_logger("/tmp/shell_log")


# Generated at 2022-06-14 09:09:00.839558
# Unit test for function shell_logger
def test_shell_logger():
    assert False, "TODO: Write tests for shell_logger()"

# Generated at 2022-06-14 09:09:04.703460
# Unit test for function shell_logger
def test_shell_logger():
    assert shell_logger("test.log") == 1


if __name__ == "__main__":
    shell_logger("log.txt")

# Generated at 2022-06-14 09:09:10.545048
# Unit test for function shell_logger
def test_shell_logger():
    with tempfile.NamedTemporaryFile() as tempfile_handle:
        tempfile_path = tempfile_handle.name
    # Basic case
    shell_logger(tempfile_path)
    with open(tempfile_path, 'rb') as output_handle:
        assert output_handle.read() != b''

    # case for opening non existent file
    with pytest.raises(IOError):
        shell_logger("/idonotexist")

# Generated at 2022-06-14 09:09:24.427454
# Unit test for function shell_logger
def test_shell_logger():
    import os
    import shutil
    import time
    import sys
    import contextlib
    import unittest
    import tempfile

    @contextlib.contextmanager
    def temp_chdir(path):
        cwd = os.getcwd()
        os.chdir(path)
        yield
        os.chdir(cwd)

    # code taken from https://stackoverflow.com/a/1769305
    class StreamCapturer(object):
        def __init__(self, stream):
            self._stream = stream
            self._buffer = ''
            self._old_stream_position = None
            self._capturing = False

        def capture(self):
            if self._capturing:
                return
            self._capturing = True
            self._old_stream_position = self._stream.tell()
           

# Generated at 2022-06-14 09:09:33.776319
# Unit test for function shell_logger
def test_shell_logger():
    from subprocess import PIPE
    from subprocess import Popen

    def set_pty_size(master_fd):
        buf = array.array('h', [const.TEST_COLS, const.TEST_ROWS, 0, 0])
        fcntl.ioctl(pty.STDOUT_FILENO, termios.TIOCGWINSZ, buf, True)
        fcntl.ioctl(master_fd, termios.TIOCSWINSZ, buf)

    pid, master_fd = pty.fork()

    if pid == pty.CHILD:
        shell_logger(const.TEST_FILE)

# Generated at 2022-06-14 09:09:39.800853
# Unit test for function shell_logger
def test_shell_logger():
    sys.argv = ['pssh', 'shell_logger', 'test.log']
    try:
        shell_logger('test.log')
        assert False
    except SystemExit as e:
        assert e.code != 0

if __name__ == '__main__':
    shell_logger(sys.argv[1])

# Generated at 2022-06-14 09:09:42.315033
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('/tmp/test.log')

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:09:47.870163
# Unit test for function shell_logger
def test_shell_logger():
    if os.path.exists('test_shell_logger'):
        os.remove('test_shell_logger')
    os.system("echo 'hello' | python -m logster --logger shell_logger --output 'test_shell_logger'")
    f = open('test_shell_logger')
    f.seek(const.LOG_SIZE_IN_BYTES - const.LOG_SIZE_TO_CLEAN)
    assert f.read(const.LOG_SIZE_TO_CLEAN) == b'hello\n'

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:09:52.899992
# Unit test for function shell_logger
def test_shell_logger():
    fd, fname = tempfile.mkstemp()
    os.close(fd)

# Generated at 2022-06-14 09:09:55.423010
# Unit test for function shell_logger
def test_shell_logger():
    with tempfile.NamedTemporaryFile() as fd:
        returncode = shell_logger(fd.name)
        assert returncode == 0

# Generated at 2022-06-14 09:10:13.360696
# Unit test for function shell_logger
def test_shell_logger():
    import pytest
    import subprocess
    import os
    import pty
    import time
    import io

    from .. import const
    from .. import logs

    logs.set_debug()

    if not os.environ.get('SHELL'):
        pytest.skip("Shell logger doesn't support your platform.")

    pid, master_fd = pty.fork()

    if pid == pty.CHILD:
        shell_logger('/tmp/log.txt')

    os.write(master_fd, b'1234567890')
    os.fsync(master_fd)
    time.sleep(0.5)
    with io.open('/tmp/log.txt', 'r+b') as f:
        f.seek(const.LOG_SIZE_IN_BYTES - 10)

# Generated at 2022-06-14 09:10:17.307315
# Unit test for function shell_logger
def test_shell_logger():
    """
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile() as tf:
    ...     shell_logger(tf.name)
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 09:10:30.704812
# Unit test for function shell_logger
def test_shell_logger():
    """ First of all we check that everything works fine if we don't do
    anything with configuration. In other words, if we change nothing
    in configuration, shell_logger will work exactly as a script command.

    """
    command_logger = ['./script --timing=results.time --command=\'',
                      os.environ['SHELL'], '\' --return=',
                      'results.ret results.log']
    command = ' '.join(command_logger)
    os.system(command)
    script_log = open('results.log', 'r')
    script_time = open('results.time', 'r')
    script_ret = open('results.ret', 'r')
    script_log_contents = script_log.read()
    script_time_contents = script_time.read()
    script

# Generated at 2022-06-14 09:10:31.462827
# Unit test for function shell_logger
def test_shell_logger():
    from . import tests

    tests.test_shell_logger()

# Generated at 2022-06-14 09:10:38.092214
# Unit test for function shell_logger
def test_shell_logger():
    """Unit test for shell_logger."""
    try:
        shell_logger('log')
    except SystemExit as e:
        assert e.code == 0
    finally:
        try:
            os.remove('log')
        except OSError:
            pass

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:10:49.678200
# Unit test for function shell_logger

# Generated at 2022-06-14 09:11:01.705886
# Unit test for function shell_logger
def test_shell_logger():
    """
    Function Type: Bound method

    Returns:
    1. Directly exists the program if no $SHELL environment variable is present.
    2. Creates a log file of size 5MB with all the shell output with unix script command.
    3. Logs the output to PyLog.

    NOTE:
    1. Depends on the shell environment variable.
    2. Tested on Mac OS 10.9.4 with zsh terminal.
    """
    output = './logs/test_shell_logger.log'

# Generated at 2022-06-14 09:11:11.456287
# Unit test for function shell_logger
def test_shell_logger():
    import os
    import pytest
    import subprocess
    import time

    @pytest.fixture(scope="module")
    def temp_file(tmpdir_factory):
        file_name = tmpdir_factory.mktemp('data').join('test.log')
        return str(file_name)

    def test_vim_nvim(temp_file):
        # Test that the expected shell is spawned.
        env = os.environ.copy()
        env['SHELL'] = '/bin/bash'
        subprocess.Popen(['python', 'shell_logger.py', '--output', temp_file], env=env)
        time.sleep(1) # Wait for the process to start up.
        os.system('ps -p $(pgrep -f "python shell_logger.py")')


# Generated at 2022-06-14 09:11:14.157841
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger("/tmp/log")

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:11:26.649429
# Unit test for function shell_logger
def test_shell_logger():
    fd = os.open('~/test.log', os.O_CREAT | os.O_TRUNC | os.O_RDWR)
    os.write(fd, b'\x00' * const.LOG_SIZE_IN_BYTES)
    buffer = mmap.mmap(fd, const.LOG_SIZE_IN_BYTES, mmap.MAP_SHARED, mmap.PROT_WRITE)
    os.environ['SHELL'] = '/bin/bash'
    return_code = _spawn(os.environ['SHELL'], partial(_read, buffer))
    assert return_code

# Generated at 2022-06-14 09:11:38.677210
# Unit test for function shell_logger
def test_shell_logger():
    from .. import app
    from ..utils import temporary_file

    with temporary_file() as f:
        app.main(['shell_logger', f])


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 09:11:43.683200
# Unit test for function shell_logger
def test_shell_logger():
    with tempfile.TemporaryDirectory() as tmpdirname:
        with open(os.path.join(tmpdirname, 'test_file'), 'w') as f:
            f.write('test\n')
        os.environ['SHELL'] = 'cat'
        shell_logger(os.path.join(tmpdirname, 'test_file'))

# Generated at 2022-06-14 09:11:44.404672
# Unit test for function shell_logger
def test_shell_logger():
    assert True

# Generated at 2022-06-14 09:11:51.281594
# Unit test for function shell_logger
def test_shell_logger():
    try:
        shell = os.environ['SHELL']
    except KeyError:
        logs.warn("Shell logger doesn't support your platform.")
        return

    output = 'output.log'
    try:
        shell_logger(output)
    finally:
        try:
            os.remove(output)
        except FileNotFoundError:
            pass

# Generated at 2022-06-14 09:12:00.661304
# Unit test for function shell_logger
def test_shell_logger():
    """Tests shell_logger function works as expected."""
    import subprocess
    import shutil
    import time
    import pwd
    import tempfile
    import glob
    import re

    stdout_file = tempfile.mktemp()
    with open(stdout_file, 'w+b') as c:
        c.write(b'\x00' * const.LOG_SIZE_IN_BYTES)
        c.flush()
        pty_process = subprocess.Popen(['env', 'python', '-c', 'import pty; pty.spawn(u"%s")' % os.environ['SHELL']],
                                       stdin=c, stdout=c, stderr=c, close_fds=True)
        time.sleep(0.05)


# Generated at 2022-06-14 09:12:08.576301
# Unit test for function shell_logger
def test_shell_logger():
    buffer = bytearray(const.LOG_SIZE_IN_BYTES)
    read = partial(logs.mock_read, buffer)
    return_code = _spawn(os.environ['SHELL'], partial(_read, read))

    assert return_code == 0

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:12:16.703843
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile
    log_file = tempfile.TemporaryFile()
    # os.environ['SHELL'] = '/bin/sh'
    #
    # shell = os.environ['SHELL']
    # buf = array.array('h', [0, 0, 0, 0])
    # fcntl.ioctl(pty.STDOUT_FILENO, termios.TIOCGWINSZ, buf, True)
    # fcntl.ioctl(pty.STDOUT_FILENO, termios.TIOCSWINSZ, buf)
    # print log_file
    # logs.error('test ')
    # _spawn(shell, log_file)


if __name__=="__main__":
    test_shell_logger()

# Generated at 2022-06-14 09:12:22.402383
# Unit test for function shell_logger
def test_shell_logger():
    assert shell_logger('/tmp/test_output') == 0

# Generated at 2022-06-14 09:12:23.650025
# Unit test for function shell_logger
def test_shell_logger():
    # TBD
    return


# Generated at 2022-06-14 09:12:34.791673
# Unit test for function shell_logger
def test_shell_logger():
    '''
    Execute shell_logger as a separate process, then check if the log file has been created.
    '''
    temp_log = 'temp_shell_logger.txt'
    def _check_result():
        buffer = mmap.mmap(fd, const.LOG_SIZE_IN_BYTES, mmap.MAP_SHARED, mmap.PROT_WRITE)
        buffer.seek(0)
        assert buffer.read() == b'\x00' * (const.LOG_SIZE_IN_BYTES - const.LOG_SIZE_TO_CLEAN)
        buffer.close()

    for i in range(1, 100):
        with open(temp_log, 'w') as f:
            pass

# Generated at 2022-06-14 09:12:50.254133
# Unit test for function shell_logger
def test_shell_logger():
    logger_pid = os.fork()
    if logger_pid == 0:
        shell_logger('../output/shell.log')
    else:
        os.system('sleep 1')
        os.system('whoami>../output/whoami.txt')
        os.system('sleep 1')
        file = open('../output/shell.log', 'r')
        assert file.read() == 'whoami\r\nyamu\r\n'
        os.kill(logger_pid, signal.SIGKILL)
        return 0
    return 1

# Generated at 2022-06-14 09:12:55.596534
# Unit test for function shell_logger
def test_shell_logger():
    from . import Fixture
    from .output_tester import OutputTester
    from . import const

    f = Fixture()
    logger = shell_logger
    ot = OutputTester(f)
    ot.test_shell_logger(logger, const.LOG_SIZE_IN_BYTES)

# Generated at 2022-06-14 09:13:00.637430
# Unit test for function shell_logger
def test_shell_logger():
    temp_filename = 'shell_logger.tmp'
    try:
        shell_logger(temp_filename)
    finally:
        os.remove(temp_filename)

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:13:04.803108
# Unit test for function shell_logger
def test_shell_logger():
    def check(cnd):
        assert cnd, "Failed test"

    logs.set_verbose(False)
    # check if the code returned with error
    check(shell_logger("~/output.txt") == 0)

# Generated at 2022-06-14 09:13:12.526935
# Unit test for function shell_logger
def test_shell_logger():
    from subprocess import Popen, PIPE, STDOUT
    from . import const, logs

    # Clear output file
    open(const.DEFAULT_LOG_FILE, 'w').close()

    # Run logger in background
    logs.info("Running shell logger")
    pid = Popen(['python3', '-c', 'from shell_logger import shell_logger; shell_logger("{}")'.format(const.DEFAULT_LOG_FILE)]).pid

    # Run command and close logger
    command = "echo 'Hello world'"
    output = Popen([os.environ['SHELL'], '-c', command], stdout=PIPE, stderr=STDOUT).communicate()[0]
    Popen(['kill', '-s', 'SIGINT', str(pid)]).communicate()
    logs

# Generated at 2022-06-14 09:13:19.020599
# Unit test for function shell_logger
def test_shell_logger():
    import shutil
    from os.path import isfile
    from tempfile import NamedTemporaryFile

    with NamedTemporaryFile(delete=False) as f:
        f_name = f.name
    shell_logger(f_name)
    assert isfile(f_name)
    assert os.stat(f_name).st_size == const.LOG_SIZE_IN_BYTES
    shutil.rmtree(f_name)

# Generated at 2022-06-14 09:13:22.345359
# Unit test for function shell_logger
def test_shell_logger():
    location = 'shell.log'
    shell_logger(location)
    with open(location) as file:
        assert file.read() == '\x00' * const.LOG_SIZE_IN_BYTES
    os.remove(location)

# Generated at 2022-06-14 09:13:24.633923
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('shell.log')

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:13:34.094273
# Unit test for function shell_logger
def test_shell_logger():
    """
    Run tests on shell_logger.
    """

    def get_log(name):
        path = os.path.join(os.path.dirname(__file__), '..', '..', 'logs', name)
        f = open(path, 'rb')
        data = f.read()
        f.close()
        return data.decode('utf-8')

    try:
        output = os.path.join(os.path.dirname(__file__), '..', '..', 'logs', 'test_shell_logger.txt')

        # This function call should raise a ValueError exception, because log size is 1024 bytes and we write 1124 bytes.
        shell_logger(output)
    except ValueError:
        pass

    # Second function call should pass

# Generated at 2022-06-14 09:13:37.646038
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger("./test.txt")


if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:13:50.107357
# Unit test for function shell_logger
def test_shell_logger():
    os.environ['SHELL'] = '/bin/bash'
    output = '/tmp/logger.tmp'
    try:
        shell_logger(output)
    finally:
        if os.path.exists(output):
            os.remove(output)