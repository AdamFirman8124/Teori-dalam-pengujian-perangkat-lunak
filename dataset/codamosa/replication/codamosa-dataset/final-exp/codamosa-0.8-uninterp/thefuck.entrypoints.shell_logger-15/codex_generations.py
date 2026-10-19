

# Generated at 2022-06-14 09:04:05.756542
# Unit test for function shell_logger
def test_shell_logger():
    import os
    import tempfile
    import subprocess
    import shutil

    class _test(object):
        def __init__(self):
            self._old_shell = os.environ.get('SHELL')
            self.tmpdir = tempfile.mkdtemp()
            self.filename = os.path.join(self.tmpdir, 'log.txt')

        def __enter__(self):
            os.environ['SHELL'] = '/bin/sh'
            os.mkfifo(self.filename)
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            os.remove(self.filename)
            shutil.rmtree(self.tmpdir)
            os.environ['SHELL'] = self._old_shell
            return False


# Generated at 2022-06-14 09:04:07.341536
# Unit test for function shell_logger
def test_shell_logger():
    assert shell_logger("output") == 0


# Generated at 2022-06-14 09:04:10.949289
# Unit test for function shell_logger
def test_shell_logger():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        shell_logger(f.name)
    with open(f.name, 'r') as f:
        logs.assert_true(f.read())

# Generated at 2022-06-14 09:04:19.485402
# Unit test for function shell_logger
def test_shell_logger():
    if os.name != 'posix':
        raise Exception('This test for Unix systems only')

    import time
    import atexit

    output = b'/tmp/shell_logger.test'
    time.sleep(1)
    if not os.path.exists(output):
        raise Exception('File not exists')

    file_size = os.stat(output).st_size
    if file_size != const.LOG_SIZE_IN_BYTES:
        raise Exception('Wrong file size')

    shell_logger(output)



# Generated at 2022-06-14 09:04:29.019259
# Unit test for function shell_logger
def test_shell_logger():
    """
    Test to check if the file was created and has the same content.
    """
    # Create dummy file
    fd = open("test_file.txt", "w+")
    fd.write("Blah Blah");
    fd.close()
    # Call the funtion we want to test
    shell_logger("test_file.txt")
    # Open file and check the content
    fd = open("test_file.txt", "r")
    data = fd.read().splitlines()
    assert(data == ['Blah Blah'])
    # Delete dummy file
    os.unlink("test_file.txt")


if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:04:31.757903
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('shell.log')

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:04:37.082368
# Unit test for function shell_logger
def test_shell_logger():
    pid, master_fd = pty.fork()

    if pid == pty.CHILD:
        shell_logger(output='/tmp/logger')

    pid, _ = os.waitpid(pid, 0)
    # TODO: implement
    assert pid == 0

# Generated at 2022-06-14 09:04:38.909558
# Unit test for function shell_logger
def test_shell_logger():
    assert shell_logger('test_shell_logger.log') == 0

# Generated at 2022-06-14 09:04:47.405581
# Unit test for function shell_logger
def test_shell_logger():
    import io
    import os
    import stat
    from contextlib import contextmanager

    from .. import handler

    @contextmanager
    def _create_file():
        _, path = tempfile.mkstemp(prefix='test_', suffix='.log')
        try:
            yield path
        finally:
            os.remove(path)

    def _test_size():
        with _create_file() as path:
            shell_logger(path)
            size = os.stat(path).st_size
            assert size == const.LOG_SIZE_IN_BYTES

    def test_size():
        with handler.suppress():
            _test_size()

    def _test_content():
        with _create_file() as path:
            shell_logger(path)

# Generated at 2022-06-14 09:04:48.464984
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('./output')

# Generated at 2022-06-14 09:04:59.141292
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('test_file')

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:05:02.526438
# Unit test for function shell_logger
def test_shell_logger():
    assert(0 == shell_logger("out"))

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:05:09.130008
# Unit test for function shell_logger
def test_shell_logger():
    def _check(output):
        assert os.path.exists(output)
        with open(output, 'rb') as f:
            assert f.read() == b'\x00' * const.LOG_SIZE_IN_BYTES

    output = 'shell.log'
    shell_logger(output)
    _check(output)
    os.remove(output)

# Generated at 2022-06-14 09:05:21.529069
# Unit test for function shell_logger
def test_shell_logger():
    """Logs shell output to the `output`.

    Works like unix script command with `-f` flag.

    """
    if not os.environ.get('SHELL'):
        logs.warn("Shell logger doesn't support your platform.")
        sys.exit(1)

    fd = os.open("shell_logger.log", os.O_CREAT | os.O_TRUNC | os.O_RDWR)
    os.write(fd, b'\x00' * 100)
    buffer = mmap.mmap(fd, 100, mmap.MAP_SHARED, mmap.PROT_WRITE)
    return_code = _spawn(os.environ['SHELL'], partial(_read, buffer))

    sys.exit(return_code)


# Generated at 2022-06-14 09:05:22.391230
# Unit test for function shell_logger
def test_shell_logger():
    pass



# Generated at 2022-06-14 09:05:35.366169
# Unit test for function shell_logger
def test_shell_logger():
    import os
    import sys
    import time
    import subprocess
    import shutil

    from utils import this_dir

    TEST_DIR = os.path.join(this_dir(), 'tmp')
    TEST_LOG = os.path.join(TEST_DIR, 'tmp.log')

    if not os.path.exists(TEST_DIR):
        os.mkdir(TEST_DIR)

    F = open(TEST_LOG, 'a+')
    F.seek(const.LOG_SIZE_IN_BYTES - 1)
    F.write('\0')
    F.close()

    sys.argv = [TEST_LOG]
    shell_logger(TEST_LOG)

    time.sleep(1)

# Generated at 2022-06-14 09:05:45.005911
# Unit test for function shell_logger
def test_shell_logger():
    import os
    import shutil
    import subprocess
    import tempfile

    logs.set_up_logging()
    temp_dir = tempfile.mkdtemp()

    test_file = os.path.join(temp_dir, 'test_shell_logger')

    def get_result():
        with open(test_file) as f:
            return f.read()

    def test_func(cmd, expected, need_cleanup=True):
        start_result = get_result()
        subprocess.check_call(['python', '-c', 'from shelllogger import shell_logger\nshell_logger("%s")' % test_file, '-c', cmd])
        end_result = get_result()

# Generated at 2022-06-14 09:05:50.196674
# Unit test for function shell_logger
def test_shell_logger():
    """Test for shell_logger function."""
    import tempfile

    path = tempfile.mkstemp(suffix='-log')[1]
    shell_logger(path)

    print("Log is written to", path)

# Generated at 2022-06-14 09:05:57.281654
# Unit test for function shell_logger
def test_shell_logger():
    import os
    import shutil
    import tempfile

    fd, temp_file = tempfile.mkstemp(prefix='le-shell-')
    os.close(fd)

    with open(temp_file, 'wb') as buffer:
        _spawn('ls', partial(_read, buffer))

    with open(temp_file, 'rb') as buffer:
        assert b'le-shell' in buffer.read()

    os.unlink(temp_file)
    shutil.rmtree(tempfile.gettempdir())

# Generated at 2022-06-14 09:06:10.764261
# Unit test for function shell_logger
def test_shell_logger():
    """ Test for shell_logger """
    from .test_render import output_test
    from .test_shell import is_windows
    from .test_logs import output_test_log
    import subprocess
    import filecmp

    logs.info("Testing shell_logger")

    if is_windows():
        logs.warn("Shell logger doesn't support your platform.")
        return

    shell_logger_test = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), "shell_logger_test.sh")

    shell_test = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), "shell_logger_test.log")


# Generated at 2022-06-14 09:06:29.259402
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile
    with tempfile.TemporaryFile() as f:
        buffer = mmap.mmap(f.fileno(), const.LOG_SIZE_IN_BYTES)
        assert buffer.read() == b'\x00' * const.LOG_SIZE_IN_BYTES

        buffer.seek(0)
        buffer.write(b'a' * const.LOG_SIZE_IN_BYTES)
        for char in buffer:
            assert char == ord('a')

        buffer.seek(0)
        buffer.write(b'\x00' * const.LOG_SIZE_IN_BYTES)
        for char in buffer:
            assert char == 0

# Generated at 2022-06-14 09:06:39.837144
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile
    import time

    with tempfile.NamedTemporaryFile() as tmp_file:
        pid = os.fork()
        if pid == 0:
            shell_logger(tmp_file.name)
        else:
            time.sleep(1)
            os.kill(pid, signal.SIGTERM)
            os.waitpid(pid, 0)
            tmp_file.seek(0)
            with open(tmp_file.name, 'rb') as f:
                assert b'\x00' * const.LOG_SIZE_IN_BYTES not in f.read()

# Generated at 2022-06-14 09:06:43.641342
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile
    output = tempfile.mktemp()
    shell_logger(output)
    with open(output) as f:
        assert f.read() == 'exit'
    os.remove(output)

# Generated at 2022-06-14 09:06:52.601950
# Unit test for function shell_logger
def test_shell_logger():
    import shutil
    import tempfile
    import time

    temp_dir = tempfile.mkdtemp()

    # Make directory with enough space to avoid race condition
    if not os.getcwd().endswith('tests'):
        os.chdir(os.path.dirname(os.path.dirname(__file__)))
        temp_dir = os.path.join(os.getcwd(), temp_dir)
        os.makedirs(temp_dir)

    output = os.path.join(temp_dir, 'test.log')
    shell_logger(output)

    time.sleep(1)
    log = open(output, 'r')
    try:
        assert os.stat(output).st_size != 0
        assert log.read() != ''
    except AssertionError:
        logs

# Generated at 2022-06-14 09:06:58.643126
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile
    import shutil
    tmpdir = tempfile.mkdtemp()

    # Create a temporary file and invoke shell_logger
    with tempfile.NamedTemporaryFile(dir=tmpdir) as f:
        shell_logger(f.name)

    shutil.rmtree(tmpdir)




# Generated at 2022-06-14 09:07:06.424875
# Unit test for function shell_logger
def test_shell_logger():
    fd, path = mkstemp()
    unlink(path)

    child = Popen(['python', '-u', '-m', 'rtl.shlog', path])
    try:
        child.communicate(b'Hello, world!')
    except KeyboardInterrupt:
        child.terminate()
        child.wait()
    else:
        assert child.returncode == 0

    with open(path, 'rb') as f:
        content = f.read()
    unlink(path)

    assert content == b'Hello, world!'

if __name__ == '__main__':
    shell_logger(*sys.argv[1:])

# Generated at 2022-06-14 09:07:13.187187
# Unit test for function shell_logger
def test_shell_logger():
    import io
    from . import const
    from . import logs
    f = io.StringIO()
    logs.set_logging(f)
    shell_logger('/tmp/script')
    assert open('/tmp/script').read().count('\x00') == const.LOG_SIZE_IN_BYTES // 2

# Generated at 2022-06-14 09:07:21.834255
# Unit test for function shell_logger
def test_shell_logger():
    """
    Runs tests on the shell_logger function, including testing
    if the logger is run successfully and if the logger writes to
    the log file.
    """
    from . import shell_logger
    from . import logs
    from . import const

    # Test if function runs successfully
    logger = shell_logger("test.txt")
    assert logger is not None

    # Test that the logger writes output to the log file
    data = b'\x00' * const.LOG_SIZE_IN_BYTES
    fd = os.open("test.txt", os.O_CREAT | os.O_TRUNC | os.O_RDWR)
    os.write(fd, data)

# Generated at 2022-06-14 09:07:23.367134
# Unit test for function shell_logger
def test_shell_logger():
    assert shell_logger("shell_logger.txt")==0

# Generated at 2022-06-14 09:07:28.063701
# Unit test for function shell_logger
def test_shell_logger():
    logfile = '/tmp/pyte-shell-logger-test'
    shell_logger(logfile)

    with open(logfile, 'rb') as f:
        f.seek(-2, 2)
        assert f.read() == b'\r\n'
    os.remove(logfile)

# Generated at 2022-06-14 09:07:48.904257
# Unit test for function shell_logger
def test_shell_logger():
    # Configure logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # Create logger console output
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.DEBUG)

    # Create logger file output
    fh = logging.handlers.RotatingFileHandler(
        filename='shell_logger.log',
        maxBytes=const.LOG_SIZE_TO_CLEAN,
        backupCount=1
        )
    fh.setLevel(logging.WARNING)

    # Create formatter
    formatter = logging.Formatter('%(message)s')

    # Add formatter to console
    console.setFormatter(formatter)

    # Add formatter to fh
    fh.setFormatter(formatter)

# Generated at 2022-06-14 09:07:51.926359
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('test_shell_logger.txt')

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:07:53.786558
# Unit test for function shell_logger
def test_shell_logger():
    """Unit test for shell_logger"""
    shell_logger(output='/tmp/test.log')


# Generated at 2022-06-14 09:07:57.586720
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('test_shell_logger.txt')

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:08:01.325195
# Unit test for function shell_logger
def test_shell_logger():
    assert shell_logger

if __name__ == '__main__':
    shell_logger(sys.argv[1])

# Generated at 2022-06-14 09:08:05.387960
# Unit test for function shell_logger
def test_shell_logger():
    os.environ['SHELL'] = 'sh'
    shell_logger('/tmp/test')
    with open('/tmp/test') as f:
        assert f.read() == 'exit\n'

# Generated at 2022-06-14 09:08:15.074283
# Unit test for function shell_logger
def test_shell_logger():
    import time
    import subprocess
    from .. import logs
    from ..const import LOG_SIZE_IN_BYTES
    TEMP_OUTPUT = '/tmp/shell_logger'


# Generated at 2022-06-14 09:08:28.015006
# Unit test for function shell_logger
def test_shell_logger():
    import random
    import tempfile
    import time
    import unittest

    CLEAN_TEXT = 'Hello. This is a test\n'

    class TestShellLogger(unittest.TestCase):

        def test_shell_logger(self):
            output = tempfile.mktemp(prefix='log_')
            cmd = ['python', __file__, 'shell_logger', output]
            self.assertEqual(0, subprocess.Popen(cmd).wait())

            with open(output, 'rb') as f:
                self.assertEqual(f.read(len(CLEAN_TEXT)).decode('utf-8'),
                                 CLEAN_TEXT)


# Generated at 2022-06-14 09:08:32.222054
# Unit test for function shell_logger
def test_shell_logger():
    output = "./test_shell_logger_output.log"
    assert system("./tests/test_shell_logger.sh > " + output) == 0
    assert system("diff " + output + " tests/test_shell_logger_output.log") == 0
    system("rm " + output)

if __name__ == '__main__':
    shell_logger(sys.argv[1])

# Generated at 2022-06-14 09:08:36.900526
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile
    with tempfile.NamedTemporaryFile() as f:
        shell_logger(f.name)
    with tempfile.NamedTemporaryFile() as f:
        for i in range(10000):
            f.write(b'test')

# Generated at 2022-06-14 09:08:54.681025
# Unit test for function shell_logger
def test_shell_logger():
    tests = [
        ['shell_logger_test', 'exit 0', 0, '', 'exit code is 0'],
        ['shell_logger_test', 'exit 1', 1, '', 'exit code is 1'],
        ['shell_logger_test', 'echo 1', 0, '1\n', 'echo command is called'],
    ]
    for file, cmd, code, output, msg in tests:
        with open(file, 'w') as f:
            f.write(cmd)
        fd = os.open(file, os.O_CREAT | os.O_TRUNC | os.O_RDWR)
        os.write(fd, b'\x00' * const.LOG_SIZE_IN_BYTES)

# Generated at 2022-06-14 09:09:07.617527
# Unit test for function shell_logger
def test_shell_logger():
    def test_spawn(shell, master_read):
        master_read("test", 1)
        return 0

    sys.exit = lambda x: None
    logs.warn = lambda x: None
    fd = open("/dev/null", "r")
    os.open = lambda *args: fd
    mmap.mmap = lambda fd, *args: fd
    mmap.PROT_WRITE = 0
    mmap.MAP_SHARED = 0
    os.write = lambda *args: None
    os.close = lambda *args: None
    os.waitpid = lambda pid, err: (0, 0)
    os.environ['SHELL'] = '/bin/bash'
    pty.fork = lambda: (0, 1)
    os.execlp = lambda *args: None
    t

# Generated at 2022-06-14 09:09:16.726478
# Unit test for function shell_logger
def test_shell_logger():
    output_file = 'shell_output.log'
    output_file_copy = 'shell_output_copy.log'

    sys.argv = ['pyhistorian']
    command = shell_logger(output_file)
    
    # Run shell commands to modify output_file
    command('pwd')
    command('cd /')
    command('ls -al')
    
    # Open the file
    with open(output_file, 'rb') as f:
        data = f.read()
    os.remove(output_file)

    # Versions of Python before 3.2 don't have assertWarns
    if not hasattr(unittest.TestCase, "assertWarns"):
        unittest.TestCase.assertWarns = lambda self, warning, callable, *args, **kwds: self

# Generated at 2022-06-14 09:09:24.550144
# Unit test for function shell_logger
def test_shell_logger():
    sys.argv.append('-test.test_shell_logger')

    if os.path.isfile('test_shell_logger.log'):
        os.remove('test_shell_logger.log')

    shell_logger('test_shell_logger.log')

    assert os.path.isfile('test_shell_logger.log')

    os.remove('test_shell_logger.log')

# Generated at 2022-06-14 09:09:25.467754
# Unit test for function shell_logger
def test_shell_logger():
    from . import shell_logger
#    shell_logger(const.SHELL_OUTPUT)

# Generated at 2022-06-14 09:09:28.065363
# Unit test for function shell_logger
def test_shell_logger():
    assert shell_logger("shell.log") is None, "shell_logger() don't work properly."
test_shell_logger()

# Generated at 2022-06-14 09:09:31.409194
# Unit test for function shell_logger
def test_shell_logger():
    from tempfile import mkstemp
    from os import remove
    fd, name = mkstemp()
    shell_logger(name)
    close(fd)
    remove(name)

# Generated at 2022-06-14 09:09:35.725234
# Unit test for function shell_logger
def test_shell_logger():
    with TempFile() as output:
        shell_logger(output)
        with open(output, "r") as f:
            assert f.read() != ""

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:09:45.515071
# Unit test for function shell_logger
def test_shell_logger():
    from io import StringIO
    from contextlib import suppress
    import pytest

    # Read from stdout
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    # Create test files
    with StringIO() as f, open('test_shell_logger_test', 'w') as f2:
        f.write('Hello world!')
        f.seek(0)

        f2.write('Hello world!')
        f2.write(os.linesep)

        shell_logger('test_shell_logger_test')

        # Verify test
        assert f.read() == sys.stdout.getvalue()
        with suppress(FileNotFoundError):
            os.remove('test_shell_logger_test')

    # Restore stdout
    sys.stdout = old_stdout

# Generated at 2022-06-14 09:09:58.967286
# Unit test for function shell_logger
def test_shell_logger():
    import unittest
    import tempfile
    import contextlib
    import subprocess

    class ShellLoggerTestCase(unittest.TestCase):
        @contextlib.contextmanager
        def get_tmp_file(self):
            with tempfile.TemporaryFile(mode='w+') as tmp_file:
                yield tmp_file

        def _get_spawned_shell_output(self, spawn_shell_func, shell_command):
            tmp_file = tempfile.TemporaryFile()

            pid = os.fork()
            if pid == 0:
                spawn_shell_func(tmp_file.name)
                sys.exit(0)
            else:
                os.waitpid(pid, 0)

            tmp_file.seek(0)
            return tmp_file.read()


# Generated at 2022-06-14 09:10:22.146562
# Unit test for function shell_logger
def test_shell_logger():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    output = os.path.join(test_dir, 'test_shell.log')
    shell_logger(output)
    if not os.path.isfile(output):
        logs.warn("There was problem with unit test for shell logger.")
        assert False
    os.remove(output)

# Generated at 2022-06-14 09:10:33.938291
# Unit test for function shell_logger
def test_shell_logger():
    import os
    import random
    import shutil
    import sys
    import tempfile
    
    from . import common
    from . import logs

    def _test_content(content):
        logs.prepare_for_tests()
        
        tmp_dir = tempfile.mkdtemp(prefix="pwncat_test_")
        tmp_filename = os.path.join(tmp_dir, "test_output")
        with open(tmp_filename, "wb") as f:
            f.write(content)

        sys.stdin = common.FilelikeStringIO(content)
        shell_logger(tmp_filename)
        sys.stdin = sys.__stdin__

        with open(tmp_filename, "rb") as f:
            actual = f.read()

# Generated at 2022-06-14 09:10:40.687277
# Unit test for function shell_logger
def test_shell_logger():
    filename = 'test_shell_logger.txt'
    try:
        shell_logger(filename)
        with open(filename, 'r') as f:
            assert f.read()
    finally:
        os.remove(filename)

# Generated at 2022-06-14 09:10:49.267193
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile
    import time
    from os.path import join
    from ..const import LOG_SIZE_IN_BYTES

    with tempfile.TemporaryDirectory() as folder:
        with tempfile.NamedTemporaryFile(dir=folder) as fd:
            shell_logger(join(folder, 'log.txt'))


if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:11:00.339837
# Unit test for function shell_logger
def test_shell_logger():
    import random
    import string

    random_string = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
    test_file = '/tmp/' + random_string + '.log'

    import subprocess

    subprocess.call(['python', '-m', 'shell_logger', test_file])

    with open(test_file, 'r') as f:
        content = f.read()

    assert 'python' in content
    assert 'shell_logger' in content

    subprocess.call(['sh', '-c', 'rm ' + test_file])

# Generated at 2022-06-14 09:11:07.093761
# Unit test for function shell_logger
def test_shell_logger():
    from ..cli import main
    import tempfile
    import subprocess
    tmp = os.path.join(tempfile.gettempdir(), "test_logger.log")
    subprocess.run("echo 123 > {0}".format(tmp), shell=True, check=True)
    sys.argv = ["mycli", "--log", tmp, "-e", "ls"]
    main()



# Generated at 2022-06-14 09:11:17.794411
# Unit test for function shell_logger
def test_shell_logger():
    import unittest
    class ShellLoggerTest(unittest.TestCase):
        def test_shell_logger_normal(self):
            test_path = "testpath"
            output = "output.txt"
            f = open(output, "w")
            f.truncate(0)
            f.close()
            with self.assertRaises(SystemExit) as cm:
                shell_logger(output)
            self.assertEqual(cm.exception.code, os.EX_OK)
            self.assertEqual(os.path.getsize(output), const.LOG_SIZE_IN_BYTES)
            f = open(output, "r")
            self.assertEqual(f.readline(), "")
            f.close()

# Generated at 2022-06-14 09:11:20.019132
# Unit test for function shell_logger
def test_shell_logger():
    import doctest
    doctest.testmod(sys.modules[__name__])

# vim:ts=4:sw=4:noexpandtab:tw=80:ft=python:norl:

# Generated at 2022-06-14 09:11:20.752141
# Unit test for function shell_logger
def test_shell_logger():
    pass

# Generated at 2022-06-14 09:11:24.775503
# Unit test for function shell_logger
def test_shell_logger():
    pass

# Generated at 2022-06-14 09:11:47.186466
# Unit test for function shell_logger
def test_shell_logger():
    import subprocess
    import time
    try:
        pty.openpty()
    except OSError:
        raise unittest.SkipTest("pty module is not available")

    output = os.path.join(const.TEST_TMPDIR, "test_shell_logger")

    def check_test_output(test_output_path, expected):
        with open(test_output_path) as f:
            assert len(f.read()) == expected

    child = subprocess.Popen([sys.executable, __file__, output])

    while not os.path.exists(output):
        time.sleep(0.1)

    os.kill(child.pid, signal.SIGWINCH)
    time.sleep(0.1)


# Generated at 2022-06-14 09:11:58.844940
# Unit test for function shell_logger
def test_shell_logger():
    """Tests shell_logger by running it and then looking at the file it

    The function shouldn't return anything, just create a file with a bunch
    of stuff in it"""

    # Get the cwd and create a file, shell_logger will write to this file
    cwd = os.getcwd()
    fname = os.path.join(cwd, 'test_output.txt')

    # Call the function
    shell_logger(fname)

    # Open the file and read the data
    with open(fname, 'r') as f:
        data = f.read()

    # Delete the file
    os.remove(fname)

    return data


if __name__ == "__main__":
    logs.warn(test_shell_logger())

# Generated at 2022-06-14 09:12:07.551508
# Unit test for function shell_logger
def test_shell_logger():
    """
    >>> test_shell_logger.__name__
    'test_shell_logger'
    >>> if os.system("python -c 'from rtmbot.loggers import shell_logger' >>results.txt"):
    ...     1/0
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 09:12:10.198163
# Unit test for function shell_logger
def test_shell_logger():
    logger = shell_logger("test_shell_logger")

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:12:11.418759
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('tests/sample_shell.log')

# Generated at 2022-06-14 09:12:23.712456
# Unit test for function shell_logger
def test_shell_logger():
    """
    > ls
    file1
    file2
    > exit

    """
    pid = os.fork()
    if pid == 0:
        # Child process
        output = 'output_for_unittest_function_shell_logger'
        shell_logger(output)
    else:
        # Parent process
        try:
            os.close(0)
        except OSError:
            pass
        os.open('/dev/null', os.O_RDONLY)
        os.set_blocking(0, False)
        os.write(1, b'ls\nexit\n')
        os.waitpid(pid, 0)

# Generated at 2022-06-14 09:12:34.825553
# Unit test for function shell_logger
def test_shell_logger():
    """Executes shell_logger on the fly."""
    # Redirect the output to a file
    output_path = 'shell_logger_test.txt'
    fd = os.open(output_path, os.O_CREAT | os.O_TRUNC | os.O_RDWR)
    os.write(fd, b'\x00' * const.LOG_SIZE_IN_BYTES)
    buffer = mmap.mmap(fd, const.LOG_SIZE_IN_BYTES, mmap.MAP_SHARED, mmap.PROT_WRITE)
    return_code = _spawn(os.environ['SHELL'], partial(_read, buffer))

    # Check the output file
    f = open(output_path)

# Generated at 2022-06-14 09:12:36.345455
# Unit test for function shell_logger
def test_shell_logger():
    assert shell_logger('shell_logger_test.log') == 0

# Generated at 2022-06-14 09:12:43.961164
# Unit test for function shell_logger
def test_shell_logger():

    path = os.getcwd() + '/test.out'
    if os.path.exists(path):
        os.remove(path)

    shell_logger(path)

    assert os.path.exists(path)

    with open(path) as f:
        lines = f.readlines()

    assert len(lines) > 0

    os.remove(path)

# Generated at 2022-06-14 09:12:53.632107
# Unit test for function shell_logger
def test_shell_logger():
    import os
    import sys
    import subprocess as sp

    on_posix = 'posix' in sys.builtin_module_names

    # Create a new process and execute shell
    shell_file = "log_file.txt"
    proc = sp.Popen([sys.executable, __file__, shell_file],
                    stdin=sp.PIPE, stdout=sp.PIPE,
                    bufsize=0, shell=False, preexec_fn=os.setsid)

    # Write shell commands and end with `exit`
    commands = "ls; clear; exit\n"
    for command in commands:
        proc.stdin.write(command)
        proc.stdin.flush()

    # Should use appropriate process group
    assert proc.pid == proc.stdout.fileno()

    #

# Generated at 2022-06-14 09:13:21.160986
# Unit test for function shell_logger
def test_shell_logger():
    import sys
    import copy
    import fcntl
    import threading
    import subprocess
    import pipes

    logs_changed = "Press Enter to continue..."

    def setUpModule():
        current_logs = sys.stdout
        sys.stdout = open('/dev/null', 'w')

    def tearDownModule():
        sys.stdout = current_logs

    def check_logs(output):
        f = open(output, 'rb')
        for i in range(0, len(logs_changed)):
            try:
                assert logs_changed[i] == chr(f.read_byte())
            except AssertionError:
                return False
        return True


# Generated at 2022-06-14 09:13:33.435632
# Unit test for function shell_logger
def test_shell_logger():
    import os
    import shutil
    import tempfile
    fp = tempfile.NamedTemporaryFile(prefix='pytest-logs-', suffix='.log')
    os.environ["SHELL"] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test-shell.sh")
    exit_code = shell_logger(fp.name)
    assert exit_code == 0
    assert os.stat(fp.name).st_size > 0
    assert "This should be logged" in fp.read()
    fp.close()
    os.unlink(fp.name)

if __name__ == "__main__":
    test_shell_logger()

# Generated at 2022-06-14 09:13:46.720204
# Unit test for function shell_logger
def test_shell_logger():

    import io
    import unittest
    import unittest.mock as mock

    import pty

    def mock_fork():
        if os.environ.get('SHELL'):
            return 1, 1
        return 0, 1

    class TestShellLogger(unittest.TestCase):

        @mock.patch('sys.exit')
        @mock.patch('os.environ.get')
        def test_shell_logger_no_shell_environment_variable(self, os_environ_mock, sys_exit_mock):
            os_environ_mock.return_value = None
            shell_logger('/tmp/test')
            self.assertTrue(os_environ_mock.called)
            self.assertTrue(sys_exit_mock.called)
