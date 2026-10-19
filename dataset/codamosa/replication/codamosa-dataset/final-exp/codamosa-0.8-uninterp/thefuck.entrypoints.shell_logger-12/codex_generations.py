

# Generated at 2022-06-14 09:04:00.120078
# Unit test for function shell_logger
def test_shell_logger():
    with tempfile.NamedTemporaryFile('rb+') as f:
        shell_logger(f.name)
    # TODO: Check the file size and read first bytes

# Generated at 2022-06-14 09:04:02.970299
# Unit test for function shell_logger
def test_shell_logger():
    try:
        shell_logger("temp.log")
    except:
        assert False
    os.remove("temp.log")

# Generated at 2022-06-14 09:04:04.145148
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('/tmp/test.log')

# Generated at 2022-06-14 09:04:07.794922
# Unit test for function shell_logger
def test_shell_logger():
    logs.set_log_level(logs.NOTSET)  # actual logs are not needed in test
    assert shell_logger('/tmp/test.log') == 0

# Generated at 2022-06-14 09:04:10.033238
# Unit test for function shell_logger
def test_shell_logger():
    with open('/tmp/test_shell_logger.log', 'w') as f:
        shell_logger(f)

# Generated at 2022-06-14 09:04:13.094570
# Unit test for function shell_logger
def test_shell_logger():
    result = shell_logger('/tmp/test.log')
    sys.exit(result)


# Generated at 2022-06-14 09:04:25.215038
# Unit test for function shell_logger
def test_shell_logger():
    from . import const
    import os
    import random
    import string
    import sys
    import tempfile
    import time

    def random_test_string():
        return ''.join(
            random.choice(string.ascii_uppercase + string.digits)
            for _ in range(random.randint(1, 80))
        ).encode('utf-8')

    def random_test_session():
        length = random.randint(1, 64)
        time_interval = random.randint(1, 10)
        return [random_test_string() for _ in range(length)], time_interval

    _, output = tempfile.mkstemp()
    # File must be closed before using the 'script' command
    os.close(_)
    child = os.fork()


# Generated at 2022-06-14 09:04:37.129294
# Unit test for function shell_logger
def test_shell_logger():
    # Source: http://stackoverflow.com/questions/7358118/mmap-memory-access-in-python
    block_size = 1024
    mapped_size = 0
    with open('test_shell_logger.txt', 'w') as test_file:
        test_file.write('\x00' * (block_size * 5))
    # Open our test file
    fd = os.open('test_shell_logger.txt', os.O_RDWR)
    # Create our memory mapped object
    m = mmap.mmap(fd, 0, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE)
    # Start at the beginning
    pos = 0
    # Read and print a block

# Generated at 2022-06-14 09:04:39.016140
# Unit test for function shell_logger
def test_shell_logger():
    # Check that the whole file is filled with zeros
    zeros = b'\x00' * const.LOG_SIZE_IN_BYTES

    output = 'shell_logger.tmp'
    shell_logger(output)
    with open(output) as f:
        assert f.read() == zeros



# Generated at 2022-06-14 09:04:51.422930
# Unit test for function shell_logger
def test_shell_logger():
    import logging
    import unittest
    import tempfile

    class TestShellLogger(unittest.TestCase):
        def test_shell_logger(self):
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_path = temp_dir + '/shell.log'
                shell_logger(temp_path)

                fd = os.open(temp_path, os.O_RDONLY)
                buffer = mmap.mmap(fd, const.LOG_SIZE_IN_BYTES, mmap.MAP_SHARED, mmap.PROT_READ)
                logs.debug(buffer[:].decode())
                self.assertGreaterEqual(len(buffer[:]), const.LOG_SIZE_IN_BYTES)
                os.close(fd)


# Generated at 2022-06-14 09:04:59.706878
# Unit test for function shell_logger
def test_shell_logger():
    return_code = shell_logger('shell_logger.log')
    assert return_code == 0

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:05:12.282882
# Unit test for function shell_logger
def test_shell_logger():
    import pty
    import pexpect
    import os
    import os.path

    cmd = ['/bin/bash']
    prompt = '$'

    # Start the process
    p = pexpect.spawn(cmd)
    fd = p.fileno()
    mode = tty.tcgetattr(fd)
    tty.setraw(fd)

    # Start logging
    output = 'shell.log'
    fd = os.open(output, os.O_CREAT | os.O_TRUNC | os.O_RDWR)
    os.write(fd, b'\x00' * const.LOG_SIZE_IN_BYTES)

# Generated at 2022-06-14 09:05:16.673584
# Unit test for function shell_logger
def test_shell_logger():
    try:
        shell_logger('/tmp/test_shell_logger')
    except:
        assert False

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:05:25.388641
# Unit test for function shell_logger
def test_shell_logger():
    os.chdir(os.path.dirname(__file__))

    import subprocess

    subprocess.check_call(['rm', '-f', '/tmp/term_logs'])
    p = subprocess.Popen([sys.executable, 'shell_logger.py', '/tmp/term_logs'])
    sleep(1)
    subprocess.check_call(['kill', '-s', 'SIGTERM', str(p.pid)])
    sleep(1)

    with open('/tmp/term_logs', 'r') as f:
        assert 'first' in f.read()
        assert 'second' in f.read()

    subprocess.check_call(['rm', '-f', '/tmp/term_logs'])



# Generated at 2022-06-14 09:05:29.669857
# Unit test for function shell_logger
def test_shell_logger():
    """ Test shell_logger function.
    Test that we can run the script without problem.
    """
    shell_logger("./shell.log")


if __name__ == "__main__":
    test_shell_logger()

# Generated at 2022-06-14 09:05:41.445858
# Unit test for function shell_logger
def test_shell_logger():
    import shutil
    import tempfile

    tempdir = tempfile.mkdtemp()
    output_path = os.path.join(tempdir, "shell.log")

    assert not os.path.exists(output_path)
    shell_logger(output_path)
    assert os.path.exists(output_path)

    with open(output_path, "rb") as output:
        assert output.read(1) == b"\x00"
        assert output.read(const.LOG_SIZE_IN_BYTES - 1) == b"\x00" * (const.LOG_SIZE_IN_BYTES - 1)

    shutil.rmtree(tempdir)

# Generated at 2022-06-14 09:05:54.379062
# Unit test for function shell_logger

# Generated at 2022-06-14 09:05:58.382146
# Unit test for function shell_logger
def test_shell_logger():
    """
    test_shell_logger: the test for shell_logger
    """
    try:
        shell_logger('./test.txt')
    except:
        logs.warn("Shell logger doesn't support your platform.")
    return

# Generated at 2022-06-14 09:06:06.409513
# Unit test for function shell_logger
def test_shell_logger():
    import time
    import tempfile
    import os

    def _read_log_file(filename):
        with open(filename, 'r') as f:
            return f.read()

    with tempfile.NamedTemporaryFile() as f:
        shell_logger(f.name)
        time.sleep(1)
        result = _read_log_file(f.name)
        assert result == '/bin/bash'
        os.remove(f.name)

# Generated at 2022-06-14 09:06:13.750061
# Unit test for function shell_logger
def test_shell_logger():
    # Test to see if the function can be run with no argument at all
    try:
        shell_logger()
    except TypeError:
        pass
    else:
        assert False
    # Test to see if the function can be run without an argument
    try:
        shell_logger('test_file1')
    except TypeError:
        assert False
    else:
        # There is no good way to test the output of this function to an output file
        pass
    # Test to see if the function can be run with a non string argument
    try:
        shell_logger(True)
    except TypeError:
        assert False
    else:
        # There is no good way to test the output of this function to an output file
        pass
    # Test to see if the function can be run with two arguments

# Generated at 2022-06-14 09:06:44.157573
# Unit test for function shell_logger
def test_shell_logger():
    sys.argv = [sys.argv[0], 'shell_logger', '/tmp/shell_logger.out']
    shell_logger.main()

if __name__ == '__main__':
    # test_shell_logger()
    shell_logger.main()

# Generated at 2022-06-14 09:06:47.941973
# Unit test for function shell_logger
def test_shell_logger():
    import pytest
    with pytest.raises(SystemExit) as err:
        shell_logger('shell.log')
    assert err.value.code == 0

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:07:00.461993
# Unit test for function shell_logger
def test_shell_logger():
    from . import test_util
    from .. import logs

    filename = 'test_shell_logger.txt'
    if os.path.isfile(filename):
        os.remove(filename)

    assert test_util.shell_command('pikaur echo "shell" > ' + filename,
                                   expected_retcode=0) is None
    assert test_util.shell_command('pikaur cat ' + filename,
                                   expected_retcode=0) == b'shell\n'
    os.remove(filename)

    assert test_util.shell_command('pikaur echo "logger"',
                                   expected_retcode=0) is None
    log_content = logs.read_log(filename)
    assert b'logger' in log_content
    os.remove(filename)

# Generated at 2022-06-14 09:07:07.512614
# Unit test for function shell_logger
def test_shell_logger():
    logs.set_logger('test_shell_logger')
    output = 'test_shell_logger.log'
    shell_logger(output)
    with open(output, 'rb') as f:
        assert f.read(100) == b'\x00' * 100
    os.remove(output)
    logs.set_logger('default')

# Generated at 2022-06-14 09:07:09.908738
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('/tmp/log.txt')



# Generated at 2022-06-14 09:07:20.781073
# Unit test for function shell_logger
def test_shell_logger():
    import os
    import tempfile
    import shutil

    current_cwd = os.getcwd()
    tempdir = tempfile.mkdtemp()
    os.chdir(tempdir)

    # Create file for input
    with open('input.txt', 'w') as f:
        for text in ["ls -l /", "date", "uname -a", "exit"]:
            f.write(text + os.linesep)

    # Create file for output
    output = os.path.join(tempdir, 'output')
    with open(output, 'w'):
        pass

    # Create pseudo-terminal
    master_fd, slave_fd = pty.openpty()

    # Create shell process
    pid = os.fork()
    if pid == 0:
        os.close(master_fd)

# Generated at 2022-06-14 09:07:23.936138
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger("/tmp/shell_logger_test.log")

# To run unit tests
if __name__ == "__main__":
    test_shell_logger()

# Generated at 2022-06-14 09:07:33.029455
# Unit test for function shell_logger
def test_shell_logger():
    """Test the shell_logger function."""
    import subprocess
    import tempfile
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.close()
    try:
        proc = subprocess.Popen([
            sys.executable,
            '-c',
            "import sys; from als.shell import shell_logger; sys.exit(shell_logger('{}'))".format(temp_file.name),
        ], stdin=subprocess.PIPE)
        proc.communicate(b'script\n')
        if proc.returncode:
            raise AssertionError("Function shell_logger failed")
    finally:
        os.remove(temp_file.name)

# Generated at 2022-06-14 09:07:36.874329
# Unit test for function shell_logger
def test_shell_logger():
    filename = 'test_shell_logger'
    shell_logger(filename)
    try:
        lines = open(filename).readlines()
    except:
        assert False
    # Remove trailing whitespace
    lines = [line.rstrip() for line in lines]
    assert lines[-3:] == ['exit', 'end', '']
    os.remove(filename)
    assert True

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:07:39.716436
# Unit test for function shell_logger
def test_shell_logger():
    import tests.unit.const as const
    shell_logger(const.TEST_OUTPUT)

# Generated at 2022-06-14 09:07:47.618695
# Unit test for function shell_logger
def test_shell_logger():
    assert hasattr(shell_logger, '__call__')

# Generated at 2022-06-14 09:07:58.135731
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile
    import random
    import string

    output = None

# Generated at 2022-06-14 09:08:11.022981
# Unit test for function shell_logger
def test_shell_logger():
    from .. import config
    from .. import logger
    logs_path = './test_logs'
    config.Config.set_logs_path(logs_path)
    logger.Logger.set_log_file_name('test_shell_logger')
    shell_logger(os.path.join(logs_path, logger.Logger.get_log_file_name()))
    print('\n')
    print("Please type some text in the shell and then press Enter.")
    print("Press Ctrl-C to stop the script.")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:08:12.119265
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('shell.log')

# Generated at 2022-06-14 09:08:20.032330
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile
    import subprocess
    with tempfile.NamedTemporaryFile(prefix='mr-logger-test-') as f:
        subprocess.call('echo test_shell_logger', env={
            'SHELL': '/bin/bash',
            'PYTHONPATH': '.',
            'PATH': os.environ['PATH'],
        }, shell=True, executable='/bin/bash', cwd=os.path.dirname(__file__),
            stdout=f, stderr=subprocess.STDOUT)
        with open(f.name) as f:
            assert 'test_shell_logger\n' in f.read()

# Generated at 2022-06-14 09:08:26.843114
# Unit test for function shell_logger
def test_shell_logger():
    from subprocess import Popen, PIPE

    output = f'/tmp/{__name__}'
    shell = os.environ['SHELL']

    # Launch script logger
    process = Popen(['python', os.path.abspath(__file__), 'shell_logger', output], stdin=PIPE)

    # Check it's pid is not child
    with open('/proc/1/task/{}/children'.format(process.pid), 'r') as f:
        children = f.read()
        assert process.pid != int(children)

    # Write some data to parent
    os.write(process.stdin.fileno(), b'Test')

    # Send EOF
    os.close(process.stdin.fileno())

    # Get return code
    return_code = process.wait

# Generated at 2022-06-14 09:08:37.551636
# Unit test for function shell_logger
def test_shell_logger():
    import shutil
    test_output = 'test_shell_logger_output'
    if os.path.isfile(test_output):
        os.remove(test_output)
    assert not os.path.isfile(test_output)

    shell_logger(test_output)
    assert os.path.isfile(test_output)

    size = os.path.getsize(test_output)
    assert size <= const.LOG_SIZE_IN_BYTES

    with open(test_output, 'rb') as f:
        data = f.read(size)
    assert data
    assert not data.endswith(b'\x00')

    os.remove(test_output)
    assert not os.path.isfile(test_output)

# Generated at 2022-06-14 09:08:47.375369
# Unit test for function shell_logger
def test_shell_logger():
    """Unit test for shell_logger, which writes to current directory"""
    import tempfile

    temp_path = tempfile.mkdtemp()
    shell_logger(temp_path + "/shell_logger")
    print(temp_path)


if __name__ == "__main__":
    test_shell_logger()

# Generated at 2022-06-14 09:08:53.115805
# Unit test for function shell_logger
def test_shell_logger():
    mode = tty.tcgetattr(pty.STDIN_FILENO)
    tty.setraw(pty.STDIN_FILENO)
    def restore():
        tty.tcsetattr(pty.STDIN_FILENO, tty.TCSAFLUSH, mode)
    restore()

if __name__ == '__main__':
    print('Testing shell_logger...')
    test_shell_logger()

# Generated at 2022-06-14 09:09:05.986619
# Unit test for function shell_logger
def test_shell_logger():
    from mock import patch

    class Mmap(object):
        @staticmethod
        def mmap(fd, size, flags, prot):
            return '<mmap>'

    mmap_patch = patch.object(mmap, 'mmap', Mmap.mmap)

    original_pty_fork = pty.fork
    def mock_pty_fork():
        return (1, '<master_fd>')
    pty_fork_patch = patch.object(pty, 'fork', mock_pty_fork)

    original_pty_copy = pty._copy
    def mock_pty_copy(master_fd, master_read, f):
        return
    pty_copy_patch = patch.object(pty, '_copy', mock_pty_copy)

    original_pty_read = pty._read

# Generated at 2022-06-14 09:09:14.551491
# Unit test for function shell_logger
def test_shell_logger():
    """Unit test for function shell_logger"""
    # todo write unit test
    pass

# Generated at 2022-06-14 09:09:27.306985
# Unit test for function shell_logger
def test_shell_logger():
    import io
    import os
    import select

    def test_fd():
        r, w = os.pipe()
        os.set_blocking(r, False)
        os.set_blocking(w, False)
        return os.fdopen(r, 'rb'), os.fdopen(w, 'wb')

    master_in, master_out = test_fd()
    master_out.write(b'$')
    master_out.flush()

    old_stdin, old_stdout = sys.stdin, sys.stdout

# Generated at 2022-06-14 09:09:29.010867
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('/tmp/lol.log')

# Generated at 2022-06-14 09:09:30.395635
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('/tmp/test.log')

# Generated at 2022-06-14 09:09:34.282792
# Unit test for function shell_logger
def test_shell_logger():
    with open('test.txt', 'w') as f:
        pass
    import platform
    os.environ['SHELL'] = platform.system().lower() + '_shell'
    shell_logger('test.txt')

# Generated at 2022-06-14 09:09:45.022079
# Unit test for function shell_logger
def test_shell_logger():
    import os
    import shutil
    import subprocess
    import tempfile

    size = 1024

    def test():
        fd, fname = tempfile.mkstemp(suffix='.test.log')
        logfile = os.fdopen(fd, 'w+')
        logfile.seek(size + 1)
        logfile.write('\0')
        logfile.flush()
        logfile.close()
        os.chmod(fname, 0o777)
        os.unlink(fname)

        # Execute shell_logger function
        shell_logger(fname)

        # Ensure that there is no errors in the log file
        with open(fname, 'r') as f:
            logs = f.readlines()


# Generated at 2022-06-14 09:09:52.155082
# Unit test for function shell_logger
def test_shell_logger():
    """
    >>> import tempfile
    >>> fd, f = tempfile.mkstemp()
    >>> shell_logger(f)  # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    00000: Shell logger doesn't support your platform.
    + [warn] Shell logger doesn't support your platform.
    """
    pass

# Generated at 2022-06-14 09:10:04.929240
# Unit test for function shell_logger
def test_shell_logger():
    """Test for function shell_logger."""
    from ptyshell import shell_logger
    from tempfile import NamedTemporaryFile
    from subprocess import Popen
    from threading import Thread

    def expected(*data):
        b'\x00' * const.LOG_SIZE_IN_BYTES + data

    with NamedTemporaryFile() as f:
        for i in range(10):
            p = Popen([sys.executable, "-m", "ptyshell.commands.logs", f.name])
            Thread(target=p.wait).start()
            assert p.wait() == 0

            with open(f.name, "rb") as ff:
                assert ff.read() == expected(b'\n', b'> ', b'exit\n')


# Generated at 2022-06-14 09:10:16.193484
# Unit test for function shell_logger
def test_shell_logger():
    import shutil
    from .common import delete_file
    from .cout import cout

    try:
        shell_logger(const.TEST_LOG_FILE)
    except Exception as e:
        delete_file(const.TEST_LOG_FILE)
        logs.warn("Shell logger doesn't support your platform.")
        return

    shutil.move(const.TEST_LOG_FILE, const.TEST_LOG_FILE + '.1')
    with open(const.TEST_LOG_FILE, 'w') as f:
        f.write("test" + os.linesep)

    shell_logger(const.TEST_LOG_FILE)

    with open(const.TEST_LOG_FILE + '.1') as f:
        log_1 = f.read()


# Generated at 2022-06-14 09:10:22.900974
# Unit test for function shell_logger
def test_shell_logger():
    """Test that the function shell_logger(output) is working correctly."""
    # A file that contains the output of shell when this test is run
    output = './test_shell_logger.txt'
    shell_logger(output)
    os.system('rm ' + output)

if __name__ == "__main__":
    test_shell_logger()

# Generated at 2022-06-14 09:10:37.002340
# Unit test for function shell_logger
def test_shell_logger():
    buffer = bytes([0] * const.LOG_SIZE_IN_BYTES)
    f = open('test', 'wb')
    f.write(buffer)
    f.close()
    logger = shell_logger('test')
    logger
    f = open('test', 'rb')
    buffer = f.read()
    assert buffer == bytes([0] * const.LOG_SIZE_IN_BYTES)
    f.close()
    os.unlink('test')

# Generated at 2022-06-14 09:10:49.326203
# Unit test for function shell_logger
def test_shell_logger():
    """Unit test for `shell_logger` function.
    """
    from platform import system
    from shutil import rmtree
    import os.path as path
    import subprocess

    def run_logger(command, tmp_dir):
        """Run logger and return output.
        """
        proc = subprocess.Popen([path.join(path.dirname(__file__), '..', '..', 'shell_logger.py'),
                                 tmp_dir, 'run'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        proc.stdin.write(command.strip().encode('utf-8'))
        proc.stdin.write(b'\n')
        proc.stdin.flush()
        proc.stdin.close()

# Generated at 2022-06-14 09:10:55.090199
# Unit test for function shell_logger
def test_shell_logger():
    from tests.helpers import get_random_string
    import tempfile

    fd, temp_filename = tempfile.mkstemp(suffix='.txt')
    os.close(fd)

    shell_logger(temp_filename)

    with open(temp_filename) as f:
        result = f.read()

    assert result.startswith(b'Script started on')
    assert get_random_string().encode() in result
    assert result.endswith(b'Script done on')

    os.remove(temp_filename)

# Generated at 2022-06-14 09:10:56.559253
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('test.log')

# Generated at 2022-06-14 09:11:00.338932
# Unit test for function shell_logger
def test_shell_logger():
    try:
        shell_logger('/tmp/shell_logger.test')
    except SystemExit:
        pass

if __name__ == "__main__":
    test_shell_logger()

# Generated at 2022-06-14 09:11:08.477228
# Unit test for function shell_logger
def test_shell_logger():
    import time
    shell_logger("/tmp/test_shell_logger")
    f = open("/tmp/test_shell_logger")
    time.sleep(0.5)
    data = f.read()

    assert data.startswith("#!/bin/sh")
    data = data.split("\n")
    # On Linux ps aux prints '-'. On OS X it prints '?'
    assert any("ps aux" in line for line in data)

    os.remove("/tmp/test_shell_logger")


# Generated at 2022-06-14 09:11:23.531765
# Unit test for function shell_logger
def test_shell_logger():
    """Unit test for shell_logger"""
    import subprocess

    # Run shell_logger in subprocess, enter some text and check
    # if logger save the data to the log file.
    proc = subprocess.Popen([
        'python3',
        '-c',
        'import sys; sys.path.insert(0, ".."); from tools import shell_logger; shell_logger("_test.log")',
    ], stdin=subprocess.PIPE)
    proc.stdin.write(b'foo\n')
    proc.communicate()
    assert subprocess.call(['diff', '-q', '_test.log', 'tools/test.log']) == 0
    os.remove('_test.log')

# Generated at 2022-06-14 09:11:37.185478
# Unit test for function shell_logger
def test_shell_logger():
    """Functional test"""
    import os
    import subprocess
    import time

    # Create log file
    log_file = '.__log.test'
    with open(log_file, 'wb') as f:
        f.write(b'\x00' * const.LOG_SIZE_IN_BYTES)

    # Spawn shell
    p = subprocess.Popen([sys.executable, '-m', __package__ + '.logs', 'test', log_file])

    # Wait for shell to start
    time.sleep(0.1)

    # Send commands to spawned shell
    p.stdin.write(b'pwd\n')  # 1
    p.stdin.write(b'ls /\n')  # 2

# Generated at 2022-06-14 09:11:44.387352
# Unit test for function shell_logger
def test_shell_logger():
    output = 'test_shell_logger_output'
    if os.path.exists(output):
        os.remove(output)

    try:
        shell_logger(output)
        assert os.path.exists(output)
        f = open(output, 'r')
        data = f.read()
        assert data == '\x00' * const.LOG_SIZE_IN_BYTES
        f.close()
    finally:
        if os.path.exists(output):
            os.remove(output)


if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:11:50.706755
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('/tmp/test.log')
    for line in open('/tmp/test.log'):
        print(line.rstrip())


if __name__ == "__main__":
    test_shell_logger()

# vim: ts=4:sw=4:et:fdm=indent:ff=unix

# Generated at 2022-06-14 09:12:04.849346
# Unit test for function shell_logger
def test_shell_logger():
    with open('/tmp/idlerun_test.log', 'w') as f:
        f.write('test\n')
        f.flush()
    shell_logger('/tmp/idlerun_test.log')



# Generated at 2022-06-14 09:12:08.459688
# Unit test for function shell_logger
def test_shell_logger():
    pass

# Generate test for function shell_logger
from test import generate_test
test_shell_logger = partial(generate_test, shell_logger)

# Generated at 2022-06-14 09:12:16.972150
# Unit test for function shell_logger
def test_shell_logger():
    """
    Here we test that shell_logger() writes some text to the file specified
    in the first argument.

    Here is the example of what it should be:

    # from logfury import logs, const
    >>> import subprocess
    >>> import os

    # Create an empty file of size const.LOG_SIZE_IN_BYTES;
    >>> test_file = "test.log"
    >>> open(test_file, "w").close()
    >>> open(test_file, "ab").write(b"\x00" * const.LOG_SIZE_IN_BYTES)
    """
    def test():
        """
        This function is not a part of Unit test.
        It is a function which should be executed by shell_logger()
        and which do the "print" function.
        """

# Generated at 2022-06-14 09:12:32.845482
# Unit test for function shell_logger
def test_shell_logger():
    "hihi"
    import shlex, subprocess
    import time

    test_file = "test_shell_logger.log"
    test_command = "echo 'hello world' 1>&2 ; echo 'hell world 2' 1>&2 ; sleep 1"

    # start the test shell that runs the example command
    process = subprocess.Popen(shlex.split(test_command))
    # start the logger
    logger = subprocess.Popen(["python", "pipeshell.py", "shell_logger", test_file])

    # wait for logger to finish
    logger.wait()
    # read the log file
    log_file = open(test_file, "rb").read()
    # kill and wait for the example shell
    process.kill()
    process.wait()


# Generated at 2022-06-14 09:12:42.855088
# Unit test for function shell_logger
def test_shell_logger():
    if not os.environ.get('SHELL'):
        logs.warn("Shell logger doesn't support your platform.")
        sys.exit(1)

    def run(command):
        master_fd, slave_fd = pty.openpty()
        pid = os.fork()
        if pid == 0:
            os.execv(os.environ['SHELL'], [os.environ['SHELL'], '-c', command])
        os.close(slave_fd)
        os.waitpid(pid, 0)
        os.close(master_fd)

    import tempfile
    tmp_file = tempfile.NamedTemporaryFile()
    run('printf "1 2 3\n"')
    run('printf "4 5 6\n"')
    shell_logger(tmp_file.name)

# Generated at 2022-06-14 09:12:47.884367
# Unit test for function shell_logger
def test_shell_logger():
    from . import utils
    tmp = utils.temp_file()

    try:
        shell_logger(tmp)
    except utils.NoSuchFileError:
        pass
    finally:
        try:
            os.remove(tmp)
        except OSError:
            pass

# Generated at 2022-06-14 09:12:59.325867
# Unit test for function shell_logger
def test_shell_logger():
    """Unit test for shell_logger"""
    pass

    # from shell_logger import _read
    # import tempfile
    # import os
    # f = tempfile.NamedTemporaryFile()
    # master_fd = os.open(os.readlink("/proc/self/fd/0"), os.O_RDWR)
    # os.write(master_fd, b"a" * 1024)
    # _read(f, master_fd)
    # assert f.read() == b"a" * 1024

    # os.write(master_fd, b"a" * 1024)
    # _read(f, master_fd)
    # assert f.read() == b"a" * 2048
    # f.close()

# Generated at 2022-06-14 09:13:09.982054
# Unit test for function shell_logger
def test_shell_logger():
    buffer = logs.shell_logger('tests/test.log')

# Generated at 2022-06-14 09:13:12.261481
# Unit test for function shell_logger
def test_shell_logger():
    return_code = shell_logger('test_shell_logger')
    assert return_code == 0

# Generated at 2022-06-14 09:13:22.794860
# Unit test for function shell_logger
def test_shell_logger():
    """Unit test for function shell_logger"""
    import os
    import shutil
    import tempfile

    def _test():
        """Test logic for _test_shell_logger()"""
        import psutil

        child_test_file = os.path.join(test_dir, 'child.log')
        child_pid = os.fork()

        if child_pid == 0:
            with open(child_test_file, 'w') as f:
                with open(file_path, 'r') as parent_f:
                    while True:
                        data = parent_f.read(1024)
                        if len(data) == 0:
                            break
                        f.write(data)
            return

        os.system("sleep 1 && echo 'Hello there'")

# Generated at 2022-06-14 09:13:34.400787
# Unit test for function shell_logger
def test_shell_logger():
    """Test that the shell logger can log the shell output."""
    import filecmp
    import tempfile

    shell_logger(output="test_shell")
    assert(filecmp.cmp("test_shell", "test_shell_logger"))

# Generated at 2022-06-14 09:13:46.831429
# Unit test for function shell_logger
def test_shell_logger():
    def _test_shell_logger():
        logs.debug("Test starting...")
        import platform

        if platform.system() == 'Windows':
            logs.warn("Test doesn't support your platform.")
            return

        import os
        import sys

        file_name = 'test.log'
        shell_logger(file_name)

    def _check(log_size, output_size):
        with open("test.log", "rb") as f:
            output = f.read()
            assert len(output) == output_size
            assert output[log_size-output_size:log_size] == b'\x00'*(log_size-output_size)

    logs.set_debug(True)

    _test_shell_logger()

# Generated at 2022-06-14 09:13:47.898961
# Unit test for function shell_logger
def test_shell_logger():
    # TODO: write a unit test for this
    pass

# Generated at 2022-06-14 09:13:55.548754
# Unit test for function shell_logger
def test_shell_logger():
    import subprocess
    import tempfile

    tfile = tempfile.mktemp()
    rfile = tempfile.mktemp()
    subprocess.call(['python', '-c', 'import runcommands; runcommands.shell_logger("%s");' % tfile])
    with open(tfile, 'r') as f:
        with open(rfile, 'w') as o:
            o.write(f.read())
    os.remove(tfile)
    with open(rfile, 'r') as f:
        assert f.read().startswith('Script started')