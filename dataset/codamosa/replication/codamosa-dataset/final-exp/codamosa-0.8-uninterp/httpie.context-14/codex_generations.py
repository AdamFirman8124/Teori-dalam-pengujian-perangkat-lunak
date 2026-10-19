

# Generated at 2022-06-13 21:40:28.915607
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull='test', stdin_isatty='False')

# Generated at 2022-06-13 21:40:36.501543
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment()
    print(e.stdin)
    print(e.stdin_isatty)
    print(e.stdin_encoding)
    print(e.stdout)
    print(e.stdout_isatty)
    print(e.stdout_encoding)
    print(e.stderr)
    print(e.stderr_isatty)
    print(e.colors)
    print(e.program_name)
    print(e.is_windows)
    print(e.config_dir)
    print(repr(e))


# Generated at 2022-06-13 21:40:48.890950
# Unit test for constructor of class Environment
def test_Environment():
    # GIVEN
    env = Environment()

    # WHEN
    print("Environment: \n", env)

    # THEN
    assert env == Environment()

# Generated at 2022-06-13 21:41:00.119770
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(colors=256, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
    assert env.colors is 256
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr

# Generated at 2022-06-13 21:41:12.610171
# Unit test for constructor of class Environment
def test_Environment():
    import io
    import pytest
    from httpie.output.writers.stdout import StdoutWriter

    env = Environment()
    with pytest.raises(AssertionError):
        env.__init__(stdout='hello')
    with pytest.raises(AssertionError):
        env.__init__(stdout=StdoutWriter())
    with pytest.raises(AssertionError):
        env.__init__(fdsaf='stdout')

    orig_stdout = env.stdout
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.program_name == 'http'

# Generated at 2022-06-13 21:41:25.328470
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=None, is_windows=False,
                      config_dir=DEFAULT_CONFIG_DIR,
                      stdin=sys.stdin, stdin_isatty=sys.stdin.isatty(),
                      stdin_encoding="utf8",
                      stdout=sys.stdout, stdout_isatty=sys.stdout.isatty(),
                      stdout_encoding="utf8",
                      stderr=sys.stderr, stderr_isatty=sys.stderr.isatty(),
                      colors=256, program_name="http")
    assert env.is_windows==False
    assert env.config_dir==DEFAULT_CONFIG_DIR
    assert env.stdin==sys.stdin
    assert env.stdin_isatty==sys.std

# Generated at 2022-06-13 21:41:35.638842
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdin_encoding == None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding == None
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.colors == 256
    assert env.program_name == 'http'


if __name__ == "__main__":
    test_Environment()

# Generated at 2022-06-13 21:41:39.620640
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name='http', colors=24)

    assert env.is_windows is False
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.colors == 24
    assert env.program_name == 'http'

# Generated at 2022-06-13 21:41:41.378167
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    # print(env)
    pass


environment = Environment()

# Generated at 2022-06-13 21:41:49.881365
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stderr_isatty
    assert env.stderr == sys.stderr
    assert env.is_windows == is_windows
    assert env.stdin_isatty
    assert env.stdin.encoding == 'utf8'
    assert env.stdout_isatty
    assert env.stdout.encoding == 'utf8'
    assert env.colors == 256

# Generated at 2022-06-13 21:42:11.378848
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr

    assert env.stdin is not None
    assert env.stdout is not None
    assert env.stderr is not None

    assert env.stdin_isatty is True
    assert env.stdout_isatty is True
    assert env.stderr_isatty is True

    assert type(env.stdin_encoding) is str
    assert type(env.stdout_encoding) is str
    assert env.stdin_encoding == 'utf8'
    assert env.stdout_encoding == 'utf8'

# Generated at 2022-06-13 21:42:23.231067
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    actual = env.__dict__
    assert actual['config_dir'] == DEFAULT_CONFIG_DIR
    assert actual['stdin'] == sys.stdin
    assert actual['stdin_isatty'] == (sys.stdin.isatty() if sys.stdin else False)
    assert actual['stdin_encoding'] is None
    assert actual['stdout'] == sys.stdout
    assert actual['stdout_isatty'] == sys.stdout.isatty()
    assert actual['stdout_encoding'] is None
    assert actual['stderr'] == sys.stderr
    assert actual['stderr_isatty'] == sys.stderr.isatty()
    assert actual['program_name'] == 'http'
    print(env)


test_Environment

# Generated at 2022-06-13 21:42:24.669104
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(foo=123, bar='hello')
    assert env.foo == 123
    assert env.bar == 'hello'


# Generated at 2022-06-13 21:42:26.451122
# Unit test for constructor of class Environment
def test_Environment():
    pass


# Generated at 2022-06-13 21:42:29.140825
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin_isatty=False,  stdout=None)
    assert env.stdin_isatty == False
    assert env.stdout == None

# Generated at 2022-06-13 21:42:36.292378
# Unit test for constructor of class Environment
def test_Environment():
    import pytest
    env = Environment()
    # Test of property _orig_stderr
    env._orig_stderr = sys.stdout
    assert env._orig_stderr == sys.stdout
    # Test of the variable _devnull
    devnull = open(os.devnull, 'w+')
    env._devnull = devnull
    assert env._devnull is devnull
    # Test of function log_error
    # Can not get the exception information of httpie 
    # without modifying the source code of httpie, so only test the normal situation
    with pytest.raises(AssertionError):
        env.log_error('error')
    sys.stdout = sys.stderr
    # env.log_error('warning', level='warning')
    sys.stdout = sys.__stdout

# Generated at 2022-06-13 21:42:48.161591
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment()
    assert e.is_windows == is_windows
    assert e.config_dir == DEFAULT_CONFIG_DIR
    assert e.stdin is sys.stdin
    assert e.stdout is sys.stdout
    assert e.stderr is sys.stderr
    assert e.program_name == 'http'
    assert e.stdin_isatty is sys.stdin.isatty()
    assert e.stdout_encoding is e.stdout.encoding
    assert e.stderr_isatty is sys.stderr.isatty()
    assert e.stderr_encoding is e.stderr.encoding
    assert not e._devnull

# Generated at 2022-06-13 21:42:55.350486
# Unit test for constructor of class Environment
def test_Environment():
    env=Environment()
    print(env)

    curEnv=dict(type(env).__dict__)
    curEnv['config']=env.config
    print(curEnv)

if __name__=='__main__':
    test_Environment()

# Generated at 2022-06-13 21:43:10.732822
# Unit test for constructor of class Environment
def test_Environment():
    import tempfile
    import platform
    import locale
    import argparse

    httpie = Environment()

    # Test class attribute
    assert httpie.is_windows == platform.system() == "Windows"

    # Test keyword arguments
    test_env = Environment(stdout_isatty=True,
                           stdin_encoding=locale.getpreferredencoding())
    assert test_env.stdout_isatty == True
    assert test_env.stdin_encoding == locale.getpreferredencoding()
    assert test_env.stderr_encoding == locale.getpreferredencoding()
    test_env.stdout = tempfile.TemporaryFile(mode='w+', encoding=locale.getpreferredencoding())
    assert test_env.stdout_encoding == locale.getpreferredencoding

# Generated at 2022-06-13 21:43:16.141605
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(a=1, b='2', c=3.0)
    print(str(env))
    print(repr(env))
    assert env.a == 1
    assert env.b == '2'
    assert env.c == 3.0



# Generated at 2022-06-13 21:43:21.998242
# Unit test for constructor of class Environment
def test_Environment():
    print(Environment())



# Generated at 2022-06-13 21:43:28.549158
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name='http')
    assert env.program_name == 'http'

    env = Environment(program_name='http', config_dir=DEFAULT_CONFIG_DIR)
    assert env.program_name == 'http'
    assert env.config_dir == DEFAULT_CONFIG_DIR

    # env = Environment(_devnull='some_string')
    # assert env._devnull == 'some_string'

# Generated at 2022-06-13 21:43:30.358992
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(foo='bar')
    assert env.foo == 'bar'

# Generated at 2022-06-13 21:43:35.957845
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        devnull='/dev/null',
        stdin='stdin',
        stdout='stdout',
        stderr='stderr')
    assert env.devnull == '/dev/null'
    assert env.stdin == 'stdin'
    assert env.stdout == 'stdout'
    assert env.stderr == 'stderr'

# Generated at 2022-06-13 21:43:45.763515
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    env = Environment(stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr,
    )
    assert env.stdin == sys.stdin and env.stdout == sys.stdout and env.stderr == sys.stderr

# Generated at 2022-06-13 21:43:47.669246
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env is not None

# Test to check if the config file is loaded correctly

# Generated at 2022-06-13 21:43:59.405912
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    import os
    env = Environment()
    assert isinstance(env, Environment)
    assert env.stderr == sys.stderr
    assert env.stdout == sys.stdout
    assert env.stdin == sys.stdin
    assert env.stdout_isatty == True
    #assert env.stdout_encoding == 'utf-8'
    assert env.config_dir == os.path.expanduser('~/.httpie')
    assert env.colors == '256'
    assert env.program_name == 'http'
    assert env.stderr_isatty == True
    assert env.stdin_isatty == True



# Generated at 2022-06-13 21:44:06.949806
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout='default')
    assert env.stdout == 'default'
    assert env.stdin == sys.stdin
    assert env.stdin_encoding == 'utf8'
    assert env.stdout_encoding == 'utf8'
    assert env.stderr == sys.stderr
    assert env.colors == 256
    assert env.program_name == 'http'
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.config is None
    assert env._orig_stderr == sys.stderr
    assert env._devnull is None



# Generated at 2022-06-13 21:44:18.368176
# Unit test for constructor of class Environment
def test_Environment():
    class TestEnv(Environment):
        def __init__(self, test=None):
            self.test = test
            super(TestEnv, self).__init__()

        def __str__(self):
            return f'test={self.test}'

    env = Environment()
    print(env)
    print(type(env))
    print(type(env.stdout))
    print(type(env.stdin))
    print(env.__dict__)

    test_env = TestEnv(test=123)
    print(test_env)
    print(type(test_env))
    print(type(test_env.stdout))
    print(type(test_env.stdin))
    print(test_env.__dict__)

# def main():
#     test_Environment()



# Generated at 2022-06-13 21:44:33.036952
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdin_encoding is None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding is None
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.colors == 256
    assert env.program_name == 'http'

# Generated at 2022-06-13 21:44:49.293838
# Unit test for constructor of class Environment
def test_Environment():
    import io
    import os
    import contextlib
    # mock stdin
    stdin_obj = io.StringIO()

# Generated at 2022-06-13 21:44:53.501217
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(config_dir='foo', colors=1)
    print(env)

if __name__ == '__main__':
    env = Environment(config_dir='foo', colors=1)
    print(env)

# Generated at 2022-06-13 21:44:57.679457
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment(config_dir = Path('.'))
    assert environment.config_dir == Path('.')
    assert environment.stdin == sys.stdin
    assert environment.stdout == sys.stdout
    assert environment.stderr == sys.stderr

# Generated at 2022-06-13 21:45:05.920028
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()

    assert env.is_windows is False
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin is sys.stdin
    assert env.stdin_isatty is True
    assert env.stdin_encoding is not None
    assert env.stdout is sys.stdout
    assert env.stdout_isatty
    assert env.stdout_encoding is not None
    assert env.stderr is sys.stderr
    assert env.stderr_isatty
    assert env.program_name == 'http'

    assert env.config is not None
    assert env.devnull is not None
    assert env.log_error('Error',level='warning') is None

# Generated at 2022-06-13 21:45:11.154763
# Unit test for constructor of class Environment
def test_Environment():
    """
    >>> import sys
    >>> env = Environment(config_dir='/foo/bar')
    >>> env.config_dir
    PosixPath('/foo/bar')
    >>> env.stdin = None
    >>> env.stdin_isatty
    False
    >>> env.stdin_encoding = 'ascii'
    >>> env.stdout = sys.stdout
    >>> env.stdout_isatty
    True
    >>> env.stderr = sys.stderr
    >>> env.stderr_isatty
    True
    >>> env.colors = 16
    >>> env.program_name = 'httpie_test'
    """



# Generated at 2022-06-13 21:45:20.286142
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdin_encoding == None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding == None
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    if is_windows:
        assert env.colors == 256
    else:
        if curses:
            assert env.colors == 16

# Generated at 2022-06-13 21:45:26.594513
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        colors=8,
        stdin_encoding='ascii',
        stdout_encoding='cp1251',
        colors=2,
        devnull='something',
        # Unsupported attribute
        foo=123
    )
    assert str(env) == \
        "{'colors': 2, 'devnull': 'something', 'program_name': 'http', " \
        "'stdin_encoding': 'ascii', 'stdout_encoding': 'cp1251'}"

# Generated at 2022-06-13 21:45:37.440259
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment(stdin=None, is_windows=False,
                    config_dir="~/.http/", stdin_isatty=False, stdin_encoding='utf8',
                    stdout=sys.stdout, stdout_isatty=True, stdout_encoding='utf8',
                    stderr=sys.stderr, stderr_isatty=True, colors=256,
                    program_name='http', _orig_stderr=sys.stderr, _devnull=None)
    assert e.stdin is None
    assert e.is_windows is False
    assert e.config_dir == "~/.http/"
    assert e.stdin_isatty is False
    assert e.stdin_encoding == 'utf8'
    assert e.stdout is sys.stdout

# Generated at 2022-06-13 21:45:50.657409
# Unit test for constructor of class Environment
def test_Environment():
    print("Environment中属性的测试")
    import sys
    import curses
    env = {
        'is_windows': True,
        'config_dir': '.ie',
        'stdin': sys.stdin,
        'stdin_isatty': True,
        'stdin_encoding': 'utf8',
        'stdout': sys.stdout,
        'stdout_isatty': True,
        'stdout_encoding': 'utf8',
        'stderr': sys.stderr,
        'stderr_isatty': True,
        'colors': 256,
        'program_name': 'httpie',
    }
    my_env = Environment(**env)
    print(my_env)

# Generated at 2022-06-13 21:46:02.067852
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin=None, stdout=sys.stdout, stderr=sys.stderr)
    assert not env.stdin_isatty
    assert env.stdout_isatty
    assert env.stderr_isatty
    assert env.stdin_encoding is None
    assert env.stdout_encoding == 'utf8'
    assert env.stderr_encoding == 'utf8'
    assert env.colors == 256
    assert env.program_name == 'http'



# Generated at 2022-06-13 21:46:16.528677
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == False
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == True
    assert env.stdin_encoding == 'UTF-8'
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == True
    assert env.stdout_encoding == 'UTF-8'
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == True
    assert env.colors == 256
    assert env.program_name == 'http'

# Unit tests for method `__str__()` of class Environment

# Generated at 2022-06-13 21:46:28.243419
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == False
    assert env.config_dir == Path(os.path.expanduser("~/.httpie"))
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdin_encoding == None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding == None
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.colors == 256
    assert env.program_name == 'http'

# Generated at 2022-06-13 21:46:38.404030
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty() if sys.stdin else False
    assert env.stdin_encoding is None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding is None
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env._orig_stderr == sys.stderr
    assert env._devnull is None
    assert env.colors

# Generated at 2022-06-13 21:46:45.751979
# Unit test for constructor of class Environment
def test_Environment():
    import io
    env = Environment(
        stdin = io.StringIO("stdin"),
        stdout = io.StringIO("stdout"),
        stderr = io.StringIO("stderr"),
    )
    assert env.stdin == io.StringIO("stdin")
    assert env.stdout == io.StringIO("stdout")
    assert env.stderr == io.StringIO("stderr")


# Generated at 2022-06-13 21:46:54.013149
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=False,
                      is_windows=False,
                      config_dir=DEFAULT_CONFIG_DIR,
                      stdin=sys.stdin,
                      stdout=sys.stdout,
                      stderr=sys.stderr)
    assert env.devnull is False
    assert env.is_windows is False
    assert env.config_dir is DEFAULT_CONFIG_DIR
    assert env.stdin is sys.stdin
    assert env.stdout is sys.stdout
    assert env.stderr is sys.stderr

# Generated at 2022-06-13 21:47:00.793545
# Unit test for constructor of class Environment
def test_Environment():
    """
    Target: Environment

    Purpose:
        Verify that the Environment class contains default values that are expected.

    Procedure:
        1. Create an instance of the target class.
        2. Compare the values in the instance to the default values for the class.
        3. If the values are not the same, then the test has failed. Otherwise, the test passed.

    Pass Criteria:
        The constructor returns an instance whose values match those of the values in the template.

    Test Necessity:
        High. None of the tests in the suite can complete without this.

    Last modified: 2020.06.06
    By: Nick
    """
    env = Environment()
    assert env.stdin is sys.stdin
    assert env.stdin_encoding is None
    assert env.stdout is sys.stdout
    assert env.stdout_is

# Generated at 2022-06-13 21:47:13.124345
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        config_dir='/foo/bar',
        stdout=object(),
        colors=None,
        program_name='http',
        stderr=object()
    )
    assert env.config_dir == '/foo/bar'
    assert env.stdout == object()
    assert env.stderr == object()
    assert env.colors is None
    assert env.program_name == 'http'
    assert env.stderr_isatty == False
    
## Unit test for the method Environment.log_error()
## It writes to stderr with the format:
## '<env.program_name>: <level of error>: <msg>\n\n'

# Generated at 2022-06-13 21:47:25.219631
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(is_windows=False)
    assert (env.is_windows == False)
    assert (env.stdin.buffer.raw.isatty() == False)
    assert (env.stdout.isatty() == True)
    assert (env.stderr.isatty() == True)
    assert (env.colors == 256)
    assert (env.program_name == 'http')
    assert (env.stdin_encoding == 'utf8')
    assert (env.stdout_encoding == 'utf8')
    #assert (env.devnull.isatty() == False)


from httpie.downloads import Downloader
from httpie.output.streams import STREAM_FORMATS



# Generated at 2022-06-13 21:47:26.533114
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=True)
    print('%s' % env)

# Generated at 2022-06-13 21:47:37.451299
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=1)
    assert env._devnull == 1
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout_isatty == sys.stdout.isatty()
    env = Environment(devnull=1, stdin_isatty=False)
    assert env._devnull == 1
    assert env.stdin_isatty == False
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.stdout_isatty == sys.stdout.isatty()
    env = Environment(stdin=sys.stdout, devnull=1)

# Generated at 2022-06-13 21:48:23.172151
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    print(type(env))
    print(env.config_dir)
    print(env.stdin)
    print(env.stdin_isatty)
    print(env.stdin_encoding)
    print(env.stdout)
    print(env.stdout_isatty)
    print(env.stdout_encoding)
    print(env.stderr)
    print(env.stderr_isatty)
    print(env.colors)
    print(env.program_name)


if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:48:29.559502
# Unit test for constructor of class Environment
def test_Environment():
    # dict to Environment for test
    env_var = dict(
        config_dir='/root',
        stdin='stdin',
        stdin_isatty=False,
        stdin_encoding='stdin_encoding',
        stdout='stdout',
        stdout_isatty=False,
        stdout_encoding='stdout_encoding',
        stderr='stderr',
        stderr_isatty=False,
        colors = False,
        program_name = 'program_name',
    )

    env = Environment(**env_var)

    actual = dict(env.__dict__)
    del actual['_orig_stderr']
    del actual['_devnull']

    assert actual == env_var

# test Environment.__str__()

# Generated at 2022-06-13 21:48:37.160081
# Unit test for constructor of class Environment
def test_Environment():
    from io import BytesIO
    from httpie.config import Config

    # devnull是一个空白文件，用来丢弃写到它里面的内容
    # 实际上devnull是一个特殊的文件，写入它的内容都会被丢弃，即读取时会返回EOF
    # 它的路径为 /dev/null，默认为空文件。可以用来当作空管道，命令的输

# Generated at 2022-06-13 21:48:45.447612
# Unit test for constructor of class Environment
def test_Environment():

    a = Environment()
    print(a)

    b = Environment(is_windows=False, config_dir='/config/httpie/', stdin='sys.stdin',
                    stdin_isatty=True, stdin_encoding='utf8', stdout='sys.stdout',
                    stdout_isatty=True, stdout_encoding='utf8', stderr='sys.stderr',
                    stderr_isatty=True, colors=256, program_name='http')
    print(b)

    #assert all(hasattr(type(self), attr) for attr in kwargs.keys())

    # Use keyword arguments to overwrite
    # print(type(self).__dict__)

    #print(kwargs.keys())
    #print(kwargs.values())
    #print

# Generated at 2022-06-13 21:48:48.026180
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows



# Generated at 2022-06-13 21:48:52.570858
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=1, colors=123) 
    assert(env.devnull == 1)
    assert(env.colors == 123)



# Generated at 2022-06-13 21:49:01.292404
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir.__repr__() == f'{Path.home()}/.httpie'
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == True
    assert env.stdin_encoding == 'utf8'
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == True
    assert env.stdout_encoding == 'utf8'
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == True
    assert env.program_name == 'http'

    env = Environment()
    assert env.is_windows == is_windows

# Generated at 2022-06-13 21:49:04.686852
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=None)
    print(env)
    print(repr(env))
    env = Environment(devnull=None)

# Generated at 2022-06-13 21:49:14.404643
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    if (env.is_windows):
        assert(env.colors == -1)
        assert(env.program_name == 'http')
        assert(env.stdin == sys.stdin)
        assert(env.stdout == sys.stdout)
        assert(env.stderr == sys.stderr)
        assert(env.stdin_isatty)
        assert(env.stdout_isatty)
        assert(env.stderr_isatty)
        assert(env.stdin_encoding == 'utf-8')
        assert(env.stdout_encoding == 'utf-8')
        assert(env.colors == -1)
    else:
        assert(env.colors == 256)
        assert(env.program_name == 'http')


# Generated at 2022-06-13 21:49:21.059203
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.config_dir
    assert env.stdin
    assert env.stdin_encoding
    assert env.stdout_encoding
    assert env.stderr_isatty
    assert env.stderr_encoding
    assert env.colors
    assert env.program_name


# Generated at 2022-06-13 21:49:41.596559
# Unit test for constructor of class Environment
def test_Environment():
	env = Environment(is_windows=False, config_dir='/')
	print(env.__init__())
	print(env.__str__())
	print(env.__repr__())
	print(env.devnull)

if __name__ == '__main__':
	env = Environment(is_windows=False, config_dir='/')
	env.devnull = "override value"
	print(env.devnull)

	env = Environment(is_windows=False, config_dir='/')
	print(env.devnull)

	test_Environment()

# Generated at 2022-06-13 21:49:53.228620
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()

# Generated at 2022-06-13 21:50:00.901240
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()

# Generated at 2022-06-13 21:50:08.289124
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin=None, stdin_isatty=False, stdin_encoding='utf8', stdout=sys.stdout,stdout_isatty=True, 
                        stdout_encoding='utf8', stderr=sys.stderr, stderr_isatty=True, colors=256, program_name='http')
    print(env)
    
if __name__ == "__main__":
    test_Environment()

# Generated at 2022-06-13 21:50:24.450637
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment()
    assert e.config_dir == DEFAULT_CONFIG_DIR
    assert e.stdin == sys.stdin
    assert e.stdin_isatty == sys.stdin.isatty()
    assert e.stdin_encoding == sys.stdin.encoding
    assert e.stdout == sys.stdout
    assert e.stdout_isatty == sys.stdout.isatty()
    assert e.stdout_encoding == sys.stdout.encoding
    assert e.stdout_isatty == sys.stdout.isatty()
