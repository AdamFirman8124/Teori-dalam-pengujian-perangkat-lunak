

# Generated at 2022-06-14 09:03:58.111299
# Unit test for function shell_logger
def test_shell_logger():
    from io import StringIO
    from contextlib import redirect_stderr
    from unittest.mock import patch, mock_open

    files = """\
    print('test')""".split('\n')

    with patch('builtins.open', mock_open(read_data='\n'.join(files))) as mock_file, \
        patch('sys.argv', ['shell_logger', 'test.log']):

        with redirect_stderr(StringIO()) as result:
            shell_logger('test.log')

        assert True

test_shell_logger()

# Generated at 2022-06-14 09:04:09.059849
# Unit test for function shell_logger
def test_shell_logger():
    input_ = b'ls -l\n'
    output = '/tmp/shell_logger_test.txt'


# Generated at 2022-06-14 09:04:12.865978
# Unit test for function shell_logger
def test_shell_logger():
    """
    This test is too complex to create.
    """
    pass


if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:04:17.508385
# Unit test for function shell_logger
def test_shell_logger():
    from . import testing
    from .testing import dummy

    stdout = dummy.DummyStdout()

    with testing.temp_file('./test.vttrace') as output:
        shell_logger(output)

    stdout.close()



# Generated at 2022-06-14 09:04:21.561799
# Unit test for function shell_logger
def test_shell_logger():
    log = './shell.log'
    cmd = './shell.log'

    if not sys.platform.startswith('win32'):
        cmd += ' && ls'

    shell_logger(log)

    if not sys.platform.startswith('win32'):
        assert '__init__.py' in open(log, 'r').read()
        assert 'shell.log' in open(log, 'r').read()

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:04:27.564159
# Unit test for function shell_logger
def test_shell_logger():
    # FIXME: should be replaced with the proper unittest
    input = open('input.txt', 'w')
    input.write('ls -l')
    input.close()
    shell_logger('output.txt')
    output = open('output.txt', 'rb')
    print(output.read())
    output.close()
    
if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:04:31.757115
# Unit test for function shell_logger
def test_shell_logger():
    os.environ['SHELL'] = '/bin/bash'
    try:
        shell_logger('unit_test.log')
    except SystemExit:
        return
    raise Exception("Waited exit.")

__all__ = ['shell_logger']

# Generated at 2022-06-14 09:04:32.778385
# Unit test for function shell_logger
def test_shell_logger():
    pass

# Generated at 2022-06-14 09:04:45.043908
# Unit test for function shell_logger
def test_shell_logger():
    def _get_log(output):
        with io.open(output, 'rb', buffering=0) as f:
            data = f.read(const.LOG_SIZE_IN_BYTES)
            return data

    def _test(shell, command, fd):
        tty.setraw(fd)
        shell.write(command)
        shell.flush()
        time.sleep(0.25)
        tty.setcbreak(fd)
        tty.setcbreak(pty.STDIN_FILENO)
        try:
            while True:
                char = shell.read(1).decode('utf-8')
                os.write(fd, char.encode('utf-8'))
        except KeyboardInterrupt:
            pass
        except EOFError:
            pass


# Generated at 2022-06-14 09:04:58.910016
# Unit test for function shell_logger
def test_shell_logger():
    import os
    import shutil
    import tempfile
    import unittest
    import unittest.mock
    import subprocess

    class TestShellLogger(unittest.TestCase):
        def test_logger(self):
            with unittest.mock.patch.object(logs, 'warn'):
                with tempfile.TemporaryDirectory() as tdir:
                    os.environ['SHELL'] = 'test_shell'
                    shell_logger(os.path.join(tdir, 'output.log'))
                    self.assertEqual(1, logs.warn.call_count)

            with tempfile.TemporaryDirectory() as tdir:
                mock_write = unittest.mock.Mock()

# Generated at 2022-06-14 09:05:11.865305
# Unit test for function shell_logger
def test_shell_logger():
    output = 'shell_logger_test_output'

    # remove default output if exist
    if os.path.exists(output):
        os.remove(output)

    return_code = shell_logger(output)
    assert return_code == 0

    assert os.path.exists(output)


if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:05:23.348154
# Unit test for function shell_logger
def test_shell_logger():
    import subprocess
    import re
    import shutil
    import tempfile
    import os
    import sys

    from . import tests
    
    log_filename = tests.tmp_file('shell.log')
    child = subprocess.Popen([sys.executable, __file__, log_filename],
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
    child.stdin.write(b'ls\n')
    child.stdin.flush()
    
    out, err = child.communicate('exit\n')

    assert err == b''

    with open(log_filename) as f:
        content = f.read()
    

# Generated at 2022-06-14 09:05:29.889576
# Unit test for function shell_logger
def test_shell_logger():
    output = 'test.txt'
    # Delete log file
    try:
        os.remove(output)
    except OSError:
        pass
    # Check that function saves log file
    shell_logger(output)
    assert os.path.isfile(output)
    # Delete log file
    try:
        os.remove(output)
    except OSError:
        pass

# Generated at 2022-06-14 09:05:41.282490
# Unit test for function shell_logger
def test_shell_logger():
    with tempfile.NamedTemporaryFile() as f:
        logger = shell_logger(f.name)
        try:
            logger()
        except SystemExit:
            pass

        assert os.path.isfile(f.name)
        assert os.path.getsize(f.name) > 0

        buffer = mmap.mmap(f.fileno(), const.LOG_SIZE_IN_BYTES, mmap.MAP_SHARED, mmap.PROT_READ)
        buffer.seek(0, os.SEEK_END)
        assert buffer.tell() > 0


if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:05:55.501869
# Unit test for function shell_logger
def test_shell_logger():
    import io
    import StringIO
    import textwrap
    import unittest

    class test_shell_logger(unittest.TestCase):

        shell = "sh"
        python = sys.executable

        @staticmethod
        def _spawn(shell, master_read):
            pid, master_fd = pty.fork()

            if pid == pty.CHILD:
                os.execlp(shell, shell)

            _set_pty_size(master_fd)
            signal.signal(signal.SIGWINCH, lambda *_: _set_pty_size(master_fd))

            try:
                pty._copy(master_fd, master_read, pty._read)
            except OSError:
                pass

            os.close(master_fd)
            return os.waitpid

# Generated at 2022-06-14 09:06:01.785746
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'log')
        shell_logger(path)
        with open(path) as f:
            print(f.read())

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:06:13.486757
# Unit test for function shell_logger
def test_shell_logger():
    import os
    import StringIO
    from .. import logs
    from ..const import LOG_SIZE_IN_BYTES, LOG_SIZE_TO_CLEAN
    from ..tests.support import TestCase

    class TestShellLogger(TestCase):
        def setUp(self):
            TestCase.setUp(self)
            self.addCleanup(logs.stop_logging)
            logs.setup_logging(StringIO.StringIO())

        def test_log_str_in_log(self):
            shell_logger(self.log_file)
            content = self.get_log_content()
            self.assertIn('\n', content)


# Generated at 2022-06-14 09:06:17.643637
# Unit test for function shell_logger
def test_shell_logger():
    """shell_logger unit test

    runs in a subprocess, exits with code 0 on success, 1 on failure
    """
    import os
    import sys
    import time
    import subprocess

    filename = '/tmp/oslogger_shell_logger_test'
    if os.path.exists(filename):
        os.unlink(filename)

    def test_log(text):
        """Test log with given length.

        If the text size is larger than the log size, then it will split it by half.
        """
        log_size = const.LOG_SIZE_IN_BYTES
        if len(text) > log_size:
            test_log(text[:len(text)//2])
            test_log(text[len(text)//2:])

# Generated at 2022-06-14 09:06:20.947529
# Unit test for function shell_logger
def test_shell_logger():
    from .__init__ import shell_logger
    devnull = open(os.devnull, 'w')
    sys.stdout.write = devnull.write
    shell_logger('/tmp/shell.log')
    devnull.close()

# Generated at 2022-06-14 09:06:24.861930
# Unit test for function shell_logger
def test_shell_logger():
    import os
    try:
        os.remove('test_shell_logger.txt')
    except OSError:
        pass
    shell_logger('test_shell_logger.txt')

# Generated at 2022-06-14 09:06:36.834114
# Unit test for function shell_logger
def test_shell_logger():
    def _test():
        buffer = bytearray(b'\x00' * const.LOG_SIZE_IN_BYTES)
        fd = os.open(os.devnull, os.O_WRONLY)
        return _spawn(os.environ['SHELL'], partial(_read, buffer, fd))

    return_code = _test()
    assert return_code == 0, 'Return code should be 0 and is %s.' % return_code


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    path = sys.argv[1]
    shell_logger(path)

# Generated at 2022-06-14 09:06:39.138936
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger(os.path.join(os.path.dirname(__file__), 'test.log'))

# Generated at 2022-06-14 09:06:46.469594
# Unit test for function shell_logger
def test_shell_logger():
    from test.test_files import temp_file
    with temp_file() as output:
        shell_logger(output)
        assert os.path.exists(output)
        assert os.path.getsize(output) == const.LOG_SIZE_IN_BYTES
        with open(output, 'r') as f:
            content = f.read()
        assert content.find('SHELL_LOGGER_UNIT_TEST') != -1

# Generated at 2022-06-14 09:06:47.898238
# Unit test for function shell_logger
def test_shell_logger():
    test_logger = shell_logger('test_shell_logger.log')

# Generated at 2022-06-14 09:07:00.456998
# Unit test for function shell_logger
def test_shell_logger():
    import filecmp
    import tempfile
    import shutil
    tmp_dir = tempfile.mkdtemp()

    # Test command with input
    logs.debug('test_script_capture: test command with input')
    command = 'echo abc 123 | tee %s/test_shell_logger.txt' % tmp_dir
    shell_logger('%s/test_shell_logger_1.txt' % tmp_dir)

    # Test command without input
    logs.debug('test_script_capture: test command without input')
    command = 'echo abc 123 | tee %s/test_shell_logger.txt' % tmp_dir
    shell_logger('%s/test_shell_logger_2.txt' % tmp_dir)

    # Test command with input and clean flag

# Generated at 2022-06-14 09:07:09.839538
# Unit test for function shell_logger
def test_shell_logger():
    fd = os.open('testlog.txt', os.O_CREAT | os.O_TRUNC | os.O_RDWR)
    os.write(fd, b'\x00' * const.LOG_SIZE_IN_BYTES)
    buffer = mmap.mmap(fd, const.LOG_SIZE_IN_BYTES, mmap.MAP_SHARED, mmap.PROT_WRITE)

    return_code = _spawn('/bin/bash', partial(_read, buffer))

    os.close(fd)
    sys.exit(return_code)


if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:07:10.557303
# Unit test for function shell_logger
def test_shell_logger():
    pass

# Generated at 2022-06-14 09:07:15.360388
# Unit test for function shell_logger
def test_shell_logger():
    import time
    from . import utils

    logger = shell_logger('/tmp/shell_logger')

    time.sleep(5)
    logger.kill()

    output_path = '/tmp/shell_logger'
    utils.rm_file(output_path)

# Generated at 2022-06-14 09:07:17.071306
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('/tmp/test.log')


# Generated at 2022-06-14 09:07:26.965124
# Unit test for function shell_logger
def test_shell_logger():
    if not os.environ.get('SHELL'):
        logs.warn("Shell logger doesn't support your platform.")
        return False

    fd = os.open('shell_logger.log', os.O_CREAT | os.O_TRUNC | os.O_RDWR)
    os.write(fd, b'\x00' * const.LOG_SIZE_IN_BYTES)
    buffer = mmap.mmap(fd, const.LOG_SIZE_IN_BYTES, mmap.MAP_SHARED, mmap.PROT_WRITE)
    return_code = _spawn(os.environ['SHELL'], partial(_read, buffer))

    return return_code == 0

# Generated at 2022-06-14 09:07:36.772516
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile
    import subprocess
    temp_file = tempfile.NamedTemporaryFile()
    buff = open(temp_file.name, "r+b")
    shell_logger(temp_file.name)
    buff.close()
    temp_file.close()

if __name__ == "__main__":
    test_shell_logger()

# Generated at 2022-06-14 09:07:42.460727
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile
    import subprocess
    subprocess.call(['touch', '1.txt'])
    with tempfile.TemporaryFile(mode='w') as f:
        shell_logger(f)
    subprocess.call(['rm', '1.txt'])

# Generated at 2022-06-14 09:07:51.305765
# Unit test for function shell_logger
def test_shell_logger():
    import os
    import shutil


    os.environ['SHELL'] = '/bin/zsh'
    if os.path.exists('/tmp/test_log'):
        shutil.rmtree('/tmp/test_log')
    os.mkdir('/tmp/test_log')


    shell_logger('/tmp/test_log/test_log_file')
    text = open('/tmp/test_log/test_log_file', 'r').read()

    assert len(text) > 0
    assert text[:10].find('/bin/zsh') != -1

# Generated at 2022-06-14 09:07:55.138783
# Unit test for function shell_logger
def test_shell_logger():
    # check that we can write to a file
    shell_logger("test_script_logger.txt")

if __name__ == "__main__":
    test_shell_logger()

# Generated at 2022-06-14 09:07:56.546628
# Unit test for function shell_logger
def test_shell_logger():
    ____ = shell_logger(output="/tmp/test_logger.txt")

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:08:01.008095
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile
    with open(tempfile.gettempdir() + "/shell.log", "w") as output:
        print(shell_logger(output))
    print("done")

# Generated at 2022-06-14 09:08:02.879805
# Unit test for function shell_logger

# Generated at 2022-06-14 09:08:05.780335
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger("./shell_log.txt")


if __name__ == "__main__":
    test_shell_logger()

# Generated at 2022-06-14 09:08:15.017871
# Unit test for function shell_logger
def test_shell_logger():
    try:
        os.environ['SHELL'] = '/bin/bash'
        p = multiprocessing.Process(target=shell_logger, args=('test_shell_logger.log', ))
        p.start()
        p.terminate()
        p.join()
        assert os.path.exists('test_shell_logger.log')
        with open('test_shell_logger.log', 'rb') as f:
            f.seek(const.LOG_SIZE_IN_BYTES - const.LOG_SIZE_TO_CLEAN)
            assert f.read().strip()
    finally:
        if os.path.exists('test_shell_logger.log'):
            os.unlink('test_shell_logger.log')

# Generated at 2022-06-14 09:08:16.580473
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('test_shell_logger_file')

# Generated at 2022-06-14 09:08:36.173560
# Unit test for function shell_logger
def test_shell_logger():
    """Test for function shell_logger"""
    import pipes
    import shutil
    import tempfile
    import unittest

    class ShellLoggerTest(unittest.TestCase):
        """Test class for function shell_logger"""
        def setUp(self):
            self.path = tempfile.mkdtemp()
            self.output = os.path.join(self.path, 'output')

        def tearDown(self):
            shutil.rmtree(self.path)

        def test_empty(self):
            """Test for empty shell input"""
            shell_logger(self.output)
            self.assertEqual(open(self.output).readlines(), [])

        def test_non_empty(self):
            """Test for non empty shell input"""
            cmd = pipes.quote('echo hello')


# Generated at 2022-06-14 09:08:45.308402
# Unit test for function shell_logger
def test_shell_logger():
    output = '/tmp/shell.log'

    try:
        os.remove(output)
    except Exception:
        pass

    if os.path.exists(output):
        os.remove(output)

    shell_logger(output)
    assert os.path.exists(output) is True

# Generated at 2022-06-14 09:08:51.074571
# Unit test for function shell_logger
def test_shell_logger():
    """ """
    f = tempfile.NamedTemporaryFile(delete=False)
    f.close()
    f = open(f.name, "w")
    sys.stdout = f
    shell_logger(f.name)
    f.close()
    os.remove(f.name)

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:08:55.641786
# Unit test for function shell_logger
def test_shell_logger():
    # TODO: test with mocking os.open, os.write, mmap
    try:
        shell_logger('/tmp/_t2s_shell_logger_test.txt')
    except OSError:
        pass
    except:
        raise AssertionError("Unexpected exception")

# Generated at 2022-06-14 09:09:00.345188
# Unit test for function shell_logger
def test_shell_logger():
    output = 'test_shell.log'
    shell_logger(output)
    log_data = open(output).read().replace('\x00', '').replace('\n', '')
    assert log_data == 'Test Shell Logger'

# Generated at 2022-06-14 09:09:05.418414
# Unit test for function shell_logger
def test_shell_logger():
    """
    Runs script shell_logger.py
    :return:
    """
    from subprocess import call
    call("python shell_logger.py 'output.txt'", shell=True)
    return 0

# Generated at 2022-06-14 09:09:15.624351
# Unit test for function shell_logger
def test_shell_logger():
    import os.path
    import shutil
    import tempfile

    tempdir = tempfile.mkdtemp()
    tempfile = os.path.join(tempdir, "test.log")
    temp_txt = os.path.join(tempdir, "test.txt")

    with open(temp_txt, "w") as f:
        f.write('test')
    with open(tempfile, "wb") as f:
        f.write(b'\x00' * const.LOG_SIZE_IN_BYTES)

    try:
        shell_logger(tempfile)
    finally:
        shutil.rmtree(tempdir)

    with open(tempfile, "rb") as f:
        assert f.read().find(b'test') != -1

# Generated at 2022-06-14 09:09:19.623042
# Unit test for function shell_logger
def test_shell_logger():
    return_code = shell_logger('.shell_logger.log')
    sys.exit(return_code)


if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:09:20.897691
# Unit test for function shell_logger
def test_shell_logger():
    pass

# Generated at 2022-06-14 09:09:22.249125
# Unit test for function shell_logger
def test_shell_logger():
    pass

# Generated at 2022-06-14 09:09:32.201770
# Unit test for function shell_logger
def test_shell_logger():
    def test_f():
        pass
    shell_logger(test_f)
    pass

# Generated at 2022-06-14 09:09:44.939155
# Unit test for function shell_logger
def test_shell_logger():
    with tempfile.NamedTemporaryFile() as f:
        with mock.patch('sys.exit') as mock_exit:
            with mock.patch('os.environ.get') as mock_environ:
                with mock.patch('__builtin__.open') as mock_open:
                    with mock.patch('pty.fork') as mock_fork:
                        with mock.patch('pty._read') as mock_read:
                            with mock.patch('pty.waitpid') as mock_waitpid:
                                with mock.patch('os.close') as mock_close:
                                    with mock.patch('logs.warn') as mock_warn:
                                        with mock.patch('pty._copy') as mock_copy:
                                            mock_environ.return_value = None

# Generated at 2022-06-14 09:09:57.718374
# Unit test for function shell_logger
def test_shell_logger():
    import time
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdirname:
        fileout = os.path.join(tmpdirname, 'out.log')
        filein = os.path.join(tmpdirname, 'in.log')
        with open(filein, 'w') as f:
            f.write('Test')
        newpid = os.fork()
        if newpid == 0:
            shell_logger(fileout)
        else:
            os.waitpid(newpid, 0)
            time.sleep(0.3)
            with open(fileout, 'r') as f:
                result = f.read()
                assert result == 'Test'


# vim: set ft=python:

# Generated at 2022-06-14 09:10:08.543603
# Unit test for function shell_logger
def test_shell_logger():
    def test():
        import os
        from .. import logs
        from ..core import main
        from . import shell_logger

        logs.set_stream_handler(debug=True, verbose=False)
        work_dir = utils.get_test_dir(__file__)
        tests.create_files(work_dir, ['1.txt', '2.txt'])
        cfg = config.Config(
            work_dir=work_dir,
            tasks=[
                {
                    'name': 'shell_logger',
                    'verbosity': 2,
                    'shell_logger': {
                        'output': os.path.join(work_dir, 'log.txt'),
                    },
                },
            ],
        )
        main.main(cfg)


# Generated at 2022-06-14 09:10:11.572813
# Unit test for function shell_logger
def test_shell_logger():
    output = 'output'
    try:
        shell_logger(output)
    except OSError:
        pass
    with open(output, 'r') as f:
        string = f.read()
        assert string[:4] == 'exit'

    os.remove(output)

# Generated at 2022-06-14 09:10:14.323944
# Unit test for function shell_logger
def test_shell_logger():
    """Test function shell_logger."""
    import mock
    import tempfile

    with mock.patch('pty.spawn') as spawn_mock:
        with tempfile.NamedTemporaryFile() as f:
            shell_logger(f.name)
            assert spawn_mock.call_count == 1

# Generated at 2022-06-14 09:10:18.424715
# Unit test for function shell_logger
def test_shell_logger():
    output = const.TEST_PATH + '/test_shell_logger.txt'
    try:
        shell_logger(output)
    except KeyboardInterrupt as e:
        logs.warn(e)
    finally:
        if os.path.exists(output):
            os.remove(output)
            logs.info('Remove test file: %s' % output)


if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:10:24.423975
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile
    temp_fd, temp_path = tempfile.mkstemp()
    shell_logger(temp_path)
    assert os.path.getsize(temp_path) == const.LOG_SIZE_IN_BYTES

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:10:34.913626
# Unit test for function shell_logger
def test_shell_logger():
    """Unit test for function shell_logger"""

    from subprocess import Popen, PIPE
    from time import sleep
    from os.path import isfile

    output = 'test.log'

    # Run shell_logger as a subprocess
    p1 = Popen(['python', '-c', 'from pyscripts import shell_logger; shell_logger("test.log")'], stdin = PIPE, stdout = PIPE)

    # Wait for shell_logger to start
    sleep(1)

    # Kill shell_logger
    p1.terminate()

    # Compare the results
    with open("test.log", 'r') as f:
        if f.read().strip() == 'exit':
            print("test_shell_logger: pass")

# Generated at 2022-06-14 09:10:40.367372
# Unit test for function shell_logger
def test_shell_logger():
    def _test_output(output):
        assert output == os.environ['SHELL']
    _orig_spawn = pty.spawn
    pty.spawn = _test_output
    shell_logger('')
    pty.spawn = _orig_spawn

# Generated at 2022-06-14 09:10:55.412706
# Unit test for function shell_logger
def test_shell_logger():
    from . import tmpdir
    from . import assert_raises

    with tmpdir() as tmp:
        shell_logger(str(tmp))
        assert os.path.isfile(str(tmp))
        with open(str(tmp)) as f:
            assert f.read() == '\x00' * const.LOG_SIZE_IN_BYTES


# Generated at 2022-06-14 09:10:58.944069
# Unit test for function shell_logger
def test_shell_logger():
    return_code = shell_logger('test_shell_logger.txt')
    assert return_code == 0
    assert os.path.exists('test_shell_logger.txt')

# Generated at 2022-06-14 09:11:04.061051
# Unit test for function shell_logger
def test_shell_logger():
    """Check for executing bash with shell_logger when SHELL is set."""
    os.environ['SHELL'] = '/usr/bin/bash'
    assert shell_logger("/tmp/test") == 0
    assert os.stat("/tmp/test").st_size == 536870912

# Generated at 2022-06-14 09:11:12.457560
# Unit test for function shell_logger

# Generated at 2022-06-14 09:11:15.274178
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('./screen-ut.log')

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:11:21.118584
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger(os.path.join(os.path.dirname(__file__), 'shell_logger.test'))

# Generated at 2022-06-14 09:11:25.434272
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger("tmp_file")

# Generated at 2022-06-14 09:11:38.113227
# Unit test for function shell_logger
def test_shell_logger():

    import io
    import tempfile
    import subprocess

    # Test without SHELL variable
    logs.set_logger(io.StringIO())
    logs.set_verbosity(logs.ERROR)
    old_environ = os.environ.copy()
    os.environ.pop('SHELL')
    shell_logger(tempfile.mktemp())
    logs.set_verbosity()
    os.environ.update(old_environ)

    # Test with SHELL variable
    stdout = io.StringIO()
    logs.add_logger(stdout)
    logs.set_verbosity(logs.ERROR)

# Generated at 2022-06-14 09:11:44.347673
# Unit test for function shell_logger
def test_shell_logger():
    import argparse
    import subprocess
    import tempfile

    parser = argparse.ArgumentParser(description='Run shell logger')
    parser.add_argument(
        '-o',
        dest='output',
        metavar='OUTPUT',
        default='/tmp/logger',
        help='output log file location')
    args = parser.parse_args()
    shell_logger(args.output)


if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:11:46.469420
# Unit test for function shell_logger
def test_shell_logger():
    """Test function shell_logger"""
    shell_logger('/tmp/test')

# Generated at 2022-06-14 09:12:01.047508
# Unit test for function shell_logger
def test_shell_logger():
    import subprocess
    import time
    import uuid

    output = '/tmp/{}.log'.format(uuid.uuid4().hex)
    pid = subprocess.Popen(['python', '-m', 'pytest', output], shell=True)
    time.sleep(1)
    pid.kill()
    pid.wait()

    with open(output, 'r') as f:
        assert f.name.endswith('.log')
        assert f.read()


if __name__ == '__main__':
    shell_logger(sys.argv[1])

# Generated at 2022-06-14 09:12:03.626853
# Unit test for function shell_logger
def test_shell_logger():
    """Run doctest on shell_logger"""
    import doctest
    return doctest.testmod(verbose=False)

# Generated at 2022-06-14 09:12:07.732337
# Unit test for function shell_logger
def test_shell_logger():
    shell_logger('test.log')

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:12:09.906732
# Unit test for function shell_logger
def test_shell_logger():
    pass


if __name__ == "__main__":
    fire.Fire(shell_logger)

# Generated at 2022-06-14 09:12:22.439908
# Unit test for function shell_logger
def test_shell_logger():
    sys.argv.append(__file__)
    result_process = subprocess.run([sys.executable, '-m', 'deploy_shell', 'shell_logger'],
                                    input=b'Hello', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert result_process.returncode == 0
    assert result_process.stdout == b''
    assert os.path.exists(os.path.join(const.DEPLOY_HOME_DIR, 'shell_logger.txt'))
    with open(os.path.join(const.DEPLOY_HOME_DIR, 'shell_logger.txt'), 'rb') as f:
        data = f.read()

# Generated at 2022-06-14 09:12:24.160453
# Unit test for function shell_logger
def test_shell_logger():
    assert shell_logger('no_such_file') == 1

# Generated at 2022-06-14 09:12:26.772474
# Unit test for function shell_logger
def test_shell_logger():
    if os.path.exists('/tmp/example'):
        os.remove('/tmp/example')
    shell_logger('/tmp/example')

# Generated at 2022-06-14 09:12:33.326076
# Unit test for function shell_logger
def test_shell_logger():
    logs.log_level(logs.LEVEL.DEBUG)
    const.LOG_SIZE_IN_BYTES = 1000
    const.LOG_SIZE_TO_CLEAN = 50
    if os.path.isfile('shell_output'):
        os.remove('shell_output')
    import threading
    from time import sleep

# Generated at 2022-06-14 09:12:41.444032
# Unit test for function shell_logger
def test_shell_logger():
    import os
    import subprocess
    import time
    import shutil
    import tempfile
    import unittest    
    
    def is_file_empty(filename):
        return os.stat(filename).st_size == 0

    class MyTestCase(unittest.TestCase):
        """ Unit tests for shell logger.
            Test case requires bash shell to be installed.
            May be broken on some platforms in the future.
        """
        def setUp(self):
            self.temp_dir = tempfile.mkdtemp()
            self.output = os.path.join(self.temp_dir, "out.txt")

        def tearDown(self):
            shutil.rmtree(self.temp_dir)


# Generated at 2022-06-14 09:12:44.175365
# Unit test for function shell_logger
def test_shell_logger():
    assert shell_logger('/dev/null') == 0

if __name__ == '__main__':
    shell_logger('/dev/null')

# Generated at 2022-06-14 09:13:05.224874
# Unit test for function shell_logger
def test_shell_logger():
    import filecmp
    import random
    import tempfile
    import time
    import unittest

    class ShellLoggerTests(unittest.TestCase):
        def setUp(self):
            self.tmpdir = tempfile.TemporaryDirectory()
            self.output = os.path.join(self.tmpdir.name, 'output.log')
            self.expected = os.path.join(self.tmpdir.name, 'expected.log')
            self.expected_full = os.path.join(self.tmpdir.name, 'expected_full.log')
            self.slave = random.randint(0,101)
            self.master = random.randint(0,101)

        def tearDown(self):
            self.tmpdir.cleanup()


# Generated at 2022-06-14 09:13:08.363221
# Unit test for function shell_logger
def test_shell_logger():
    # Test init
    # We don't have logger test yet, thus this test is not very complete.
    try:
        shell_logger('test.log')
        assert(False)
    except SystemExit:
        pass

# Generated at 2022-06-14 09:13:14.048718
# Unit test for function shell_logger
def test_shell_logger():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    shell_logger(os.path.join(current_dir, '..', '..', '..', '..', 'tmp.out'))

if __name__ == '__main__':
    test_shell_logger()

# Generated at 2022-06-14 09:13:15.427246
# Unit test for function shell_logger
def test_shell_logger():
    assert shell_logger('/tmp/test_shell_logger.log') == 1

# Generated at 2022-06-14 09:13:24.237718
# Unit test for function shell_logger
def test_shell_logger():
    import pexpect
    import shutil
    import time
    import tempfile

    logs.info("Testing shell_logger...")

    logs.info("Create a temporary directory")
    tmp_dir = tempfile.mkdtemp()

    # TODO: Add a case with a directory without write permission
    # TODO: Check if it logs background commands like in `script -f`

    logs.info("Make a note of current directory")
    p = pexpect.spawn("pwd")
    p.expect("\n")
    cwd = bytes(p.before)
    p.close()

    logs.info("Navigate to temporary directory")
    os.chdir(tmp_dir)

    logs.info("Launch shell logger in a background process")

# Generated at 2022-06-14 09:13:25.380037
# Unit test for function shell_logger
def test_shell_logger():
    logger = shell_logger("")
    assert logger

# Generated at 2022-06-14 09:13:38.236071
# Unit test for function shell_logger
def test_shell_logger():
    from .. import utils

    if utils.is_windows() or utils.is_mac():
        raise AssertionError('Function shell_logger() doesn\'t seem to be supported for Windows and Mac.')

    import subprocess
    import time

    with open('test.log', 'w') as out:
        proc = subprocess.Popen([sys.executable, __file__, 'test.log'], stderr=subprocess.PIPE)
        time.sleep(1)
        print('Hello', file=out)

    assert proc.poll() is None
    proc.terminate()
    proc.wait()
    os.remove('test.log')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        log = sys.argv[-1]


# Generated at 2022-06-14 09:13:46.447952
# Unit test for function shell_logger
def test_shell_logger():
    import tempfile, datetime, os
    timestr = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    filepath = timestr+ "shell_logger_unit_test.log"
    shell_logger(filepath)

if __name__ == "__main__":
    test_shell_logger()