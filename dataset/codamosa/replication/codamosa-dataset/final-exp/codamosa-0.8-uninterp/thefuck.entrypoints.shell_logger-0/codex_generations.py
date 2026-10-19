

# Generated at 2022-06-14 09:04:06.355344
# Unit test for function shell_logger
def test_shell_logger():
    import mmap
    import os
    import os.path
    import shutil
    import tempfile

    def get_mapping(path):
        fd = os.open(path, os.O_RDWR | os.O_CREAT)
        os.write(fd, b'\x00' * const.LOG_SIZE_IN_BYTES)
        return mmap.mmap(fd, const.LOG_SIZE_IN_BYTES, mmap.MAP_SHARED, mmap.PROT_WRITE)

    if not os.environ.get('SHELL'):
        logs.warn("Shell logger doesn't support your platform.")
        sys.exit(1)

    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-14 09:04:13.818173
# Unit test for function shell_logger
def test_shell_logger():
    path = os.path.abspath(__file__)
    _path = path.split(os.sep)
    _path.reverse()
    test_path = _path.pop()
    _path.reverse()
    _path.append('test')
    _path.append(test_path)
    test_path = os.sep.join(_path)
    # Don't run this test in CI because it is interactive
    # There will be an acceptability check to use the script
    # with the user's default shell
    if os.environ.get('CI') == 'true':
        const.color_print('WARNING', '\nInteractive test was skipped on CI')
    else:
        os.system('python {} -o {}'.format(test_path, '/tmp/shell_logger.log'))
    os

# Generated at 2022-06-14 09:04:15.061163
# Unit test for function shell_logger
def test_shell_logger():
    assert shell_logger('/tmp/test.log')

# Generated at 2022-06-14 09:04:27.496375
# Unit test for function shell_logger
def test_shell_logger():
    """
    $ python3 -m pytest tests/test_logger.py
    """
    import time
    import tempfile

    shell = os.environ['SHELL']

    def shell_logger_wrapper():
        with tempfile.NamedTemporaryFile() as tmp:
            buffer = shell_logger(tmp.name)
            return buffer, tmp.name

    def assert_content_length(buffer, size):
        assert buffer.tell() == size

    buffer_size = const.LOG_SIZE_IN_BYTES - const.LOG_SIZE_TO_CLEAN

    buffer, file_path = shell_logger_wrapper()
    assert_content_length(buffer, buffer_size)

    buffer, file_path = shell_logger_wrapper()
    assert_content_length(buffer, buffer_size)

   

# Generated at 2022-06-14 09:04:38.661465
# Unit test for function shell_logger
def test_shell_logger():
    import io
    import io
    import io
    import io
    import io
    import io
    import io
    import io
    import io
    import io
    import io
    import io
    import os
    import mmap
    import pytest

    @pytest.mark.skipif(os.getenv('SHELL') is None, reason="Only unix-like systems have env 'SHELL'")
    def test_shell_logger_with_shell():
        test_file_name = "test_shell_logger_with_shell.log"
        with open(test_file_name, "w"):
            pass
        shell_logger(test_file_name)

# Generated at 2022-06-14 09:04:39.428325
# Unit test for function shell_logger
def test_shell_logger():
    pass

# Generated at 2022-06-14 09:04:49.391604
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile

    # Create a temporary file and write "Shell logger works!" to it
    with tempfile.TemporaryFile() as out:
        with open('test_file', 'wb') as f:
            buffer = mmap.mmap(f.fileno(), const.LOG_SIZE_IN_BYTES, mmap.MAP_SHARED, mmap.PROT_WRITE)
        buffer.write(b'Shell logger works!')

    # Read the file and check that the text is the same
    with open('test_file', 'rb') as f:
        assert f.read() == b'Shell logger works!'

# Generated at 2022-06-14 09:04:51.022106
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger(shell_logger)     # TypeError


# Generated at 2022-06-14 09:04:55.875243
# Unit test for function shell_logger
def test_shell_logger():
    output = 'test-shell-logger.txt'
    if os.path.exists(output):
        os.remove(output)
    shell_logger(output)
    assert os.path.exists(output)

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:05:01.987570
# Unit test for function shell_logger
def test_shell_logger():
    output = tempfile.NamedTemporaryFile(mode="wb", delete=False)
    output.close()
    try:
        shell_logger(output.name)
    except IOError:
        pass
    with open(output.name, "rb") as f:
        data = f.read()
    os.remove(output.name)
    assert b"\x00" * const.LOG_SIZE_IN_BYTES == data

# Generated at 2022-06-14 09:05:11.158316
# Unit test for function shell_logger
def test_shell_logger():
    return_code = shell_logger('/tmp/shell_logger_test')
    assert return_code != 0

# Generated at 2022-06-14 09:05:14.627952
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('test/test.log')


# Generated at 2022-06-14 09:05:24.310419
# Unit test for function shell_logger
def test_shell_logger():
    import unittest
    import shutil
    from subprocess import Popen, PIPE
    import tempfile
    import time

    class TestShellLogger(unittest.TestCase):
        def setUp(self):
            self.output = tempfile.mkstemp()[1]
            self.process = Popen(['python', '-m', 'vld.tools.shell_logger', self.output])
            time.sleep(0.3)

        def test_output_file_exist(self):
            self.assertTrue(os.path.exists(self.output))

        def test_output_file_can_be_read(self):
            f = open(self.output, 'r')
            f.read()


# Generated at 2022-06-14 09:05:29.187673
# Unit test for function shell_logger
def test_shell_logger():
    sys.argv = ['', '--debug', '/tmp/logfile']
    try:
        shell_logger('/tmp/logfile')
    except:
        assert True

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:05:35.210076
# Unit test for function shell_logger
def test_shell_logger():
    assert shell_logger("test_file") == 0
    assert os.path.isfile("test_file")
    assert os.path.getsize("test_file") == const.LOG_SIZE_IN_BYTES
    os.remove("test_file")

# Generated at 2022-06-14 09:05:44.906447
# Unit test for function shell_logger
def test_shell_logger():
    import subprocess
    
    # Write the command input to the file
    command = 'cd ../../; ls -al'
    output = 'shell_logger_test'
    f = open(output, 'w')
    f.write(command)
    f.close()

    # Execute the command and get the output
    p = subprocess.Popen(command, stdout=subprocess.PIPE, \
                         shell=True)
    (output_subprocess, err) = p.communicate()
    return_code = p.wait()

    # Copy the `shell_logger` output to the `shell_logger_subprocess`
    shell_logger('shell_logger_subprocess')

    # Check if both the files match

# Generated at 2022-06-14 09:05:49.465920
# Unit test for function shell_logger
def test_shell_logger():
    with open('./temp.txt', 'w') as f:
        shell_logger('./temp.txt')

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:06:00.232527
# Unit test for function shell_logger
def test_shell_logger():
    """Unit test for function shell_logger.
    """
    import tempfile

    fd, fname = tempfile.mkstemp(prefix='shell_logger_test_')
    os.close(fd)

    shell_logger(fname)

    if not os.path.exists(fname):
        print('File with shell output is not created')
    else:
        with open(fname) as f:
            data = f.read()
            if len(data) == 0:
                print('Content of file is empty')
            else:
                print('Content of file is not empty')

    os.remove(fname)


if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:06:10.480725
# Unit test for function shell_logger
def test_shell_logger():
    """
    Unit Test

    Test the command line shell_logger is working as expected

    Note: This test only works on posix systems
    """
    import subprocess
    import time
    import random
    import os
    import logging
    import mmap
    import errno

    # Create a subprocess with a random shell
    # Return the return code of the script command
    subprocess_command = "script -c " + os.environ['SHELL'] + " /dev/null"
    p = subprocess.Popen(subprocess_command, shell=True,
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, close_fds=True)


# Generated at 2022-06-14 09:06:16.079743
# Unit test for function shell_logger
def test_shell_logger():
    """
    # test_shell_logger simulates the shell logger by setting SHELL=cat
    # to write a known amount of characters to a test file.
    # The function then runs the shell logger and reads the test.log
    # file using mmap.
    # The two are then compared. If the shell logger is working,
    # the two strings should be the same. If the shell logger
    # isn't working, the test should fail.
    """
    os.environ['SHELL'] = 'cat'
    shell_logger('test.log')
    with open('test.log', 'r+b') as f:
        file_buffer = mmap.mmap(f.fileno(), const.LOG_SIZE_IN_BYTES, mmap.MAP_SHARED, mmap.PROT_WRITE)


# Generated at 2022-06-14 09:06:27.890148
# Unit test for function shell_logger
def test_shell_logger():
    os.environ['SHELL'] = 'sh'
    os.system('touch huaji')
    shell_logger('/tmp/huaji')


if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:06:37.175450
# Unit test for function shell_logger
def test_shell_logger():
    try:
        import termios
        import tty
        import pty
        import array
    except ImportError:
        logs.warn("Unable to test `shell_logger` function on this platform.")
        return
    import os
    import mmap
    import contextlib
    import stat

    test_filename = 'logger.log'

    @contextlib.contextmanager
    def _pty():
        _master, _slave = pty.openpty()
        try:
            yield _master, _slave
        finally:
            os.close(_master)
            os.close(_slave)
    with _pty() as (master_fd, slave_fd):
        os.write(master_fd, b'a')

# Generated at 2022-06-14 09:06:49.257355
# Unit test for function shell_logger
def test_shell_logger():
    import unittest
    import tempfile
    from time import time

    class TestShellLogger(unittest.TestCase):
        def setUp(self):
            self.shell_logger = shell_logger
            self.tmpfile = tempfile.mkstemp()[1]

            def get_time(): return int(time())

            self.get_time = get_time

        def tearDown(self):
            os.remove(self.tmpfile)

        def test_write_more_than_the_buffer_size(self):
            self.shell_logger(self.tmpfile)
            file = open(self.tmpfile, 'rb')
            data = file.read()

            self.assertTrue(data.endswith(b'\x00' * const.LOG_SIZE_TO_CLEAN))

       

# Generated at 2022-06-14 09:06:56.849751
# Unit test for function shell_logger
def test_shell_logger():
    return_code = shell_logger("/tmp/test.log")
    assert return_code == 0

test_shell_logger()

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        shell_logger(sys.argv[1])
    else:
        print("Usage: " + __file__ + " <output file>")
        sys.exit(1)

# Generated at 2022-06-14 09:07:04.374329
# Unit test for function shell_logger
def test_shell_logger():
    filename = 'shell_logger_test.log'
    shell_logger(filename)
    assert os.path.exists(filename)
    try:
        file_size = os.stat(filename).st_size
    except OSError:
        file_size = 0
    assert file_size >= const.LOG_SIZE_IN_BYTES
    if os.path.exists(filename):
        os.remove(filename)

# Generated at 2022-06-14 09:07:09.406943
# Unit test for function shell_logger

# Generated at 2022-06-14 09:07:18.534401
# Unit test for function shell_logger
def test_shell_logger():
    from . import test

    with test.temp_file() as temp_file:
        shell_logger(temp_file)

        assert os.stat(temp_file).st_size == const.LOG_SIZE_IN_BYTES
        assert mmap.mmap(open(temp_file, 'r+b').fileno(), const.LOG_SIZE_IN_BYTES, mmap.MAP_PRIVATE, mmap.PROT_READ).read(const.LOG_SIZE_IN_BYTES).count(b'\x00') == const.LOG_SIZE_IN_BYTES - 4

# Generated at 2022-06-14 09:07:29.775235
# Unit test for function shell_logger
def test_shell_logger():
    def _test_shell_logger(tmpdir_factory):
        tmpdir = tmpdir_factory.mktemp('shell-logger')

        # replace stdin, stdout and stderr with non-interactive elements
        # to avoid undesired terminal interaction during testing

# Generated at 2022-06-14 09:07:40.768395
# Unit test for function shell_logger

# Generated at 2022-06-14 09:07:52.391142
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile
    import filecmp
    import pexpect
    test_txt = b'12345\n'

    with tempfile.TemporaryFile() as output:
        child = pexpect.spawnu('python', ['-m', 'yatc.plugins.logs.shell', output.name])
        child.expect_exact('% ')
        child.sendline('echo -n 12345')
        child.expect_exact('% ')
        child.sendeof()
        child.wait()
        output.seek(0)
        assert filecmp.cmp(output, test_txt)

    with tempfile.TemporaryFile() as output:
        child = pexpect.spawnu('python', ['-m', 'yatc.plugins.logs.shell', output.name])

# Generated at 2022-06-14 09:08:02.683491
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('logs/test_shell')


# Generated at 2022-06-14 09:08:03.541019
# Unit test for function shell_logger
def test_shell_logger():
    pass

# Generated at 2022-06-14 09:08:11.787549
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile

    fd, path = tempfile.mkstemp()

    # Test with no text
    shell_logger(path)
    os.close(fd)

    with open(path) as file:
        assert file.read() == ''

    # Test with some text
    fd, path = tempfile.mkstemp()

    shell_logger(path)
    os.close(fd)

    with open(path) as file:
        assert file.read() == ''

    os.remove(path)

# Generated at 2022-06-14 09:08:15.355428
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile
    with tempfile.NamedTemporaryFile() as f:
        return_code = shell_logger(f.name)
        assert return_code == 0, return_code



# Generated at 2022-06-14 09:08:27.353073
# Unit test for function shell_logger
def test_shell_logger():
    import unittest

    class TestShellLogger(unittest.TestCase):
        def test_shell_logger(self):
            import subprocess
            with open(const.LOG_FILE, 'w'):
                pass
            subprocess.call(['python3', 'tmuxp/tests/scripts/shell_logger.py'])
            l = os.stat(const.LOG_FILE).st_size
            self.assertEqual(l, const.LOG_SIZE_IN_BYTES)
            os.remove(const.LOG_FILE)

    unittest.main()

if __name__ == '__main__':
    output = os.path.expanduser(const.LOG_FILE)
    shell_logger(output)

# Generated at 2022-06-14 09:08:38.051748
# Unit test for function shell_logger
def test_shell_logger():
    from .. import utils
    from shutil import rmtree

    def get_output(shell_logger):
        return b''.join(x.strip() for x in shell_logger.file.readlines())

    with utils.temporary_directory() as temp_dir:
        with utils.temporary_file() as temp_file:
            shell_logger = logs.ShellLogger(temp_file)

            shell_logger('test')
            assert get_output(shell_logger) == b'test'

            shell_logger.write(b'123')
            assert get_output(shell_logger) == b'123test'

            shell_logger.write(b'456')
            shell_logger.seek(0)

# Generated at 2022-06-14 09:08:48.161190
# Unit test for function shell_logger
def test_shell_logger():
    import shutil
    import time
    import psutil

    time.sleep(1)
    pid = os.fork()

    if pid == 0:
        sys.exit(shell_logger('/tmp/test_shell_logger'))
    else:
        time.sleep(3)
        os.kill(pid, signal.SIGINT)
        os.wait()

    assert os.path.exists('/tmp/test_shell_logger')
    assert os.path.getsize('/tmp/test_shell_logger') > 0

    shutil.move('/tmp/test_shell_logger', './tests/log.txt')

# Generated at 2022-06-14 09:08:50.586903
# Unit test for function shell_logger

# Generated at 2022-06-14 09:08:51.323919
# Unit test for function shell_logger
def test_shell_logger():
    pass

# Generated at 2022-06-14 09:08:53.010429
# Unit test for function shell_logger
def test_shell_logger():
    assert shell_logger('./shell_logger.log')


# Generated at 2022-06-14 09:09:12.167452
# Unit test for function shell_logger
def test_shell_logger():
    if not os.environ.get('SHELL'):
        logs.warn("Shell logger doesn't support your platform.")
        sys.exit(1)

    file = 'shell_logger.txt'
    shell_logger(file)

    # Verify contents
    fd = os.open(file, os.O_CREAT | os.O_TRUNC | os.O_RDWR)
    f = os.fdopen(fd)
    f.seek(const.LOG_SIZE_IN_BYTES - const.LOG_SIZE_TO_CLEAN)
    print(f.read())


# test_shell_logger()

# Generated at 2022-06-14 09:09:19.195408
# Unit test for function shell_logger
def test_shell_logger():
    import os

    file = "/tmp/tmuxlogger.test"
    if os.path.exists(file):
        os.remove(file)

    os.environ['SHELL'] = "bash"
    shell_logger(file)
    assert os.path.exists(file)
    assert os.path.getsize(file) > 0
    os.remove(file)

# Generated at 2022-06-14 09:09:24.494520
# Unit test for function shell_logger
def test_shell_logger():
    print("Test function shell_logger")
    buffer = shell_logger("abc.txt")
    print(buffer)

if __name__ == "__main__":
    test_shell_logger()

# Generated at 2022-06-14 09:09:25.167280
# Unit test for function shell_logger
def test_shell_logger():
    pass

# Generated at 2022-06-14 09:09:29.627314
# Unit test for function shell_logger
def test_shell_logger():
    output = "test_shell_logger.log"
    try:
        shell_logger(output)
    except:
        pass
    finally:
        os.remove(output)

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:09:31.467111
# Unit test for function shell_logger
def test_shell_logger():
    """Tests function shell_logger"""
    assert shell_logger("test") == None

# Generated at 2022-06-14 09:09:39.953279
# Unit test for function shell_logger
def test_shell_logger():
    import random, string
    filename = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    assert not os.path.exists(filename)
    return_code = shell_logger(filename)
    assert os.path.exists(filename)
    assert len(open(filename).read()) == 1048576
    os.remove(filename)
    assert return_code in [0, 1]

# Generated at 2022-06-14 09:09:49.728609
# Unit test for function shell_logger
def test_shell_logger():
    import shlex
    import subprocess
    import os
    filename = '_shell_logger_test' + '.txt'
    cmd = shlex.split('python -m pudb.shell_logger ' + filename)
    process = subprocess.Popen(cmd,
                               shell=False,
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    process.stdin.write('echo "1234567"\n')
    process.stdin.write('exit\n')
    process.wait()
    if not os.path.isfile(filename) or os.stat(filename).st_size != 0:
        raise Exception('File is not empty.')
    os.remove(filename)



# Generated at 2022-06-14 09:09:56.856974
# Unit test for function shell_logger
def test_shell_logger():
    import os
    import shutil
    import tempfile

    try:
        test_file = tempfile.mkstemp()[1]
        os.environ['SHELL'] = '/bin/sh'
        shell_logger(test_file)
        assert os.path.getsize(test_file) == const.LOG_SIZE_IN_BYTES
    finally:
        shutil.rmtree(tempfile.gettempdir())

# Generated at 2022-06-14 09:10:03.997704
# Unit test for function shell_logger
def test_shell_logger():
    import unittest
    import random
    import string

    # Shell logger doesn't support Windows, just pretend the test passed
    if os.name == 'nt':
        unittest.TestCase.skipTest(
            'Shell logger doesn\'t support Windows.')

    class TestShellLogger(unittest.TestCase):
        def test_shell_logger(self):
            import io
            import tempfile

            if not os.environ.get('SHELL'):
                self.skipTest('Test shell logger doesn\'t support your platform.')

            _, output = tempfile.mkstemp()
            p = subprocess.Popen([__file__, output], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Generated at 2022-06-14 09:10:21.103176
# Unit test for function shell_logger
def test_shell_logger():
    # prepare
    logs.DATE_FORMAT = '%Y%m%d.%H%M%S.%f'
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    logs.disable_all()

    # test
    os.environ['SHELL'] = '/bin/bash' # for tests
    filename = 'test_shell_logger.log'
    shell_logger(filename)

    # cleanup
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass

# Generated at 2022-06-14 09:10:33.409241
# Unit test for function shell_logger
def test_shell_logger():
    """ blackbox testing of shell_logger """
    import io
    import os
    import subprocess
    import tempfile


# Generated at 2022-06-14 09:10:34.832617
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger("./output.txt")

# Generated at 2022-06-14 09:10:42.079920
# Unit test for function shell_logger
def test_shell_logger():
    import subprocess
    subprocess.call("touch ./shell_logger.log", shell=True)
    subprocess.call("echo aaaaaaaaaaaaaaaaaa > ./shell_logger.log", shell=True)
    shell_logger("./shell_logger.log")
    subprocess.call("touch ./shell_logger.log", shell=True)

# Generated at 2022-06-14 09:10:53.932597
# Unit test for function shell_logger
def test_shell_logger():
    from . import test_logs
    import os
    import tempfile

    def _shell_logger(stdin, stdout, stderr, **kwargs):
        new_env = dict(os.environ,
                       DEV_LIFE_SHELL_LOGGER_STDOUT=stdout,
                       DEV_LIFE_SHELL_LOGGER_STDERR=stderr)
        return test_logs._check_shell_output(shell_logger, new_env, **kwargs)

    with tempfile.NamedTemporaryFile('w') as temp:
        assert _shell_logger(stdin='echo 1', stdout=temp.name, stderr=os.devnull) == 1
        temp.seek(0)
        assert temp.read().rstrip() == 'echo 1'


# Generated at 2022-06-14 09:11:02.504749
# Unit test for function shell_logger
def test_shell_logger():
    args = ['--logs', 'test.buffer']
    const.ARGS = args
    logs.load_args()
    buffer = const.LOG_BUFFER_FILE
    const.LOG_BUFFER_FILE = 'test.buffer'
    shell_logger(buffer)
    with open('test.buffer', 'rb') as f:
        data = f.read()
    os.remove('test.buffer')
    assert data == '\x00' * const.LOG_SIZE_IN_BYTES

# Generated at 2022-06-14 09:11:04.248585
# Unit test for function shell_logger
def test_shell_logger():
    assert shell_logger('/tmp/test_shell_logger') == -1

# Generated at 2022-06-14 09:11:06.408790
# Unit test for function shell_logger
def test_shell_logger():
    sys.exit(0)

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:11:10.827796
# Unit test for function shell_logger
def test_shell_logger():
    import pytest
    from ..const import LOGS_PATH
    from os import remove

    shell_logger(LOGS_PATH + 'o')

    assert os.path.isfile(LOGS_PATH + 'o')
    remove(LOGS_PATH + 'o')

# Generated at 2022-06-14 09:11:25.848509
# Unit test for function shell_logger
def test_shell_logger():
    """Test shell_logger()."""
    import tempfile
    import shutil

    log_file = tempfile.NamedTemporaryFile(delete=False)
    log_file.close()

    print("Test 'shell_logger' function. CTRL+C for stopping logging.")
    try:
        shell_logger(log_file.name)
    except KeyboardInterrupt:
        pass

    with open(log_file.name) as f:
        print("--------------------------------------------")
        print(f.read())
        print("--------------------------------------------")

    print("End of test")
    shutil.rmtree(os.path.dirname(log_file.name), ignore_errors=True)

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:11:44.818932
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile
    import logging

    logging.basicConfig(level=logging.WARN)
    # See that bytes are written to the file
    with tempfile.NamedTemporaryFile(delete=False) as f:
        file_name = f.name
    try:
        shell_logger(file_name)
        with open(file_name) as f:
            assert f.read()
    finally:
        os.remove(file_name)
    # Check that nothing breaks if file is corrupt
    with tempfile.NamedTemporaryFile(delete=False) as f:
        file_name = f.name

# Generated at 2022-06-14 09:11:55.288960
# Unit test for function shell_logger
def test_shell_logger():
    def shell_logger_internal():
        outfile = 'sysmonitor_tests/out.txt'
        shell_logger(outfile)
        return outfile

    def read_first_chars(filename):
        with open(filename, 'rb') as f:
            return f.read(16)

    outfile = shell_logger_internal()
    first_chars = read_first_chars(outfile)
    os.remove(outfile)

    assert (first_chars == b'\x00' * 16)

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:12:02.767031
# Unit test for function shell_logger
def test_shell_logger():
    import mock
    import shutil
    import time

    # monkey patch of os.write and mmap.mmap
    with mock.patch('os.write', mock.Mock()), mock.patch('mmap.mmap', mock.Mock()) as mm:
        fd = os.open('/tmp/1', os.O_CREAT | os.O_TRUNC | os.O_RDWR)
        mm.return_value.__exit__ = mock.Mock()
        mm.return_value.__enter__.return_value = mm.return_value
        os.environ['SHELL'] = '/bin/sh'
        with mock.patch('pty.spawn', mock.Mock()) as p:
            shell_logger('/tmp/1')

# Generated at 2022-06-14 09:12:15.498424
# Unit test for function shell_logger
def test_shell_logger():
    """
    Test to show shell_logger works

    In order to test the function shell_logger, we need to seperate the stdout from the function to this file.
    Then we can check the content of the output file

    """
    import os
    import subprocess
    import sys
    import time
    import shutil
    import sys, io
    old_stdout = sys.stdout
    redirected_output = io.StringIO()
    sys.stdout = redirected_output

    temp_output_file = './temp.txt'
    if os.path.exists(temp_output_file):
        os.remove(temp_output_file)

    command = ['python', '-m', 'qap_sdk.shell_logger', temp_output_file]

# Generated at 2022-06-14 09:12:21.197916
# Unit test for function shell_logger
def test_shell_logger():
    assert not shell_logger('/tmp/test')

if __name__ == "__main__":
    test_shell_logger()

# Generated at 2022-06-14 09:12:30.701424
# Unit test for function shell_logger
def test_shell_logger():
    import re
    import shutil
    import tempfile

    tmp_dir = tempfile.mkdtemp()
    output = os.path.join(tmp_dir, 'output.log')
    try:
        shell_logger(output)

        with open(output, 'rb') as f:
            data = f.read()

        assert re.search('\d{4}-\d{2}-\d{2} \d{2}\:\d{2}\:\d{2}', data)
    finally:
        shutil.rmtree(tmp_dir)

# Generated at 2022-06-14 09:12:37.456627
# Unit test for function shell_logger
def test_shell_logger():
    import unittest
    import os
    import tempfile
    import subprocess
    import time
    import shutil
    
    class ShellLoggerTest(unittest.TestCase):
        def setUp(self):
            self.tmpdir = tempfile.mkdtemp()
            self.out = os.path.join(self.tmpdir, "out")

        def tearDown(self):
            shutil.rmtree(self.tmpdir)

        def test_empty_logger(self):
            with open(self.out, 'wb') as f:
                f.write('\x00' * const.LOG_SIZE_IN_BYTES)
                f.flush()
            
            # Wait for the file to be opened by logger.
            time.sleep(0.2)

# Generated at 2022-06-14 09:12:39.835688
# Unit test for function shell_logger
def test_shell_logger():
    assert shell_logger('/tmp/test_file') == 0

# Generated at 2022-06-14 09:12:51.157507
# Unit test for function shell_logger
def test_shell_logger():
    """
    Test for shell_logger

    Runs command: python3 -m pwnlib.util.fiddling -c 'python3 -c "print(1)"'

    Expected behaviour:
        1
        0
    """
    import subprocess
    p = subprocess.Popen(["python3", "-m", "pwnlib.util.fiddling", "-c", 'python3 -c "print(1)"'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate()

    assert output.decode() == "1\n"

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()

# Generated at 2022-06-14 09:13:03.903990
# Unit test for function shell_logger
def test_shell_logger():
    # Windows doesn't support unix operations, ignored.
    if os.name == 'nt':
        return

    if os.path.isfile(const.LOG_FILE):
        os.remove(const.LOG_FILE)

    # Create child process
    pid = os.fork()

    # Child process executes shell_logger('build.log');
    if pid == 0:
        shell_logger(const.LOG_FILE)
        sys.exit(0)

    # Parent process waits for child process with expected timeout.
    pid, status = os.waitpid(pid, 0)
    assert os.WIFEXITED(status)
    assert os.WEXITSTATUS(status) == 0

    assert os.path.isfile(const.LOG_FILE)
    assert len(open(const.LOG_FILE).read()) > 0



# Generated at 2022-06-14 09:13:20.202574
# Unit test for function shell_logger
def test_shell_logger():
    f = open('./test_shell_logger.txt', 'w')
    old_stdout = sys.stdout
    sys.stdout = f
    return_code = shell_logger('./test_shell_logger.txt')
    f.close()
    sys.stdout = old_stdout
    os.remove('./test_shell_logger.txt')
    if return_code == 0:
        return True
    else:
        return False


# Generated at 2022-06-14 09:13:30.103173
# Unit test for function shell_logger
def test_shell_logger():
    # Prepares backup for `shutil.move` function
    import builtins
    backup = builtins.move

# Generated at 2022-06-14 09:13:33.143637
# Unit test for function shell_logger
def test_shell_logger():
    with open('output', 'w') as f_output:
        f_output.truncate(0)
    import subprocess
    subprocess.call(["python", "shell_logger.py"])

# Generated at 2022-06-14 09:13:45.244458
# Unit test for function shell_logger
def test_shell_logger():
    from . import _test_data
    import subprocess

    echo = subprocess.check_output(['which', 'echo']).strip()
    script = '{} -c "echo -n hello; sleep 2; echo -n world" | ./shell_logger {}'
    out = 'script.log'
    try:
        file_size = os.path.getsize(out)
        if file_size >= 10:
            os.remove(out)
            subprocess.call(script.format(echo, out).split())
            assert os.path.getsize(out) == const.LOG_SIZE_IN_BYTES
    finally:
        if os.path.exists(out):
            os.remove(out)

# Generated at 2022-06-14 09:13:54.914589
# Unit test for function shell_logger
def test_shell_logger():
    import shutil
    from . import helper

    helper.init_root_logger()

    f = open('log1.txt', 'w')
    f.close()
    shell_logger('log1.txt')
    f = open('log1.txt', 'r')
    text = f.readline()
    f.close()
    print(text)
    os.remove('log1.txt')

    f = open('log2.txt', 'w')
    f.write('test')
    f.close()
    shell_logger('log2.txt')
    f = open('log2.txt', 'r')
    text = f.readline()
    f.close()
    print(text)
    os.remove('log2.txt')

    f = open('log3.txt', 'w')