

# Generated at 2022-06-13 21:40:30.682773
# Unit test for constructor of class Environment
def test_Environment():
    from httpie.config import DEFAULT_CONFIG_DIR
    from httpie.constants import DEFAULT_CONFIG_PATH
    env = Environment(
        stdin=sys.stdin,
        stdin_isatty=sys.stdin.isatty(),
        stdin_encoding=sys.stdin.encoding,
        stdout=sys.stdout,
        stdout_isatty=sys.stdout.isatty(),
        stdout_encoding=sys.stdout.encoding,
        stderr=sys.stderr,
        stderr_isatty=sys.stderr.isatty(),
        colors = 256,
        program_name='http',
        config_dir=DEFAULT_CONFIG_DIR,
        devnull=None,
    )

# Generated at 2022-06-13 21:40:38.218986
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == env.stdin.isatty
    #assert env.stdout == sys.stdin
    #assert env.stdout_isatty == env.stdout.isatty
    #assert env.stderr == sys.stderr
    #assert env.stderr_isatty == env.stderr.isatty
    assert env.colors == 256
    assert env.program_name == 'http'

# Generated at 2022-06-13 21:40:45.282731
# Unit test for constructor of class Environment
def test_Environment():
    env=Environment()
    assert env.stderr_isatty == True
    # assert env.stdout_isatty == True
    assert env.stdin_isatty == True

# def test_log_error():
#     env=Environment(program_name='pippo')
#     env.log_error('Pippo test')
#     assert env.stderr_isatty == True

# Generated at 2022-06-13 21:40:55.282463
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout = None, stdin = None, stderr = None)
    assert env.stdout is None
    assert env.stdin is None
    assert env.stderr is None

    env = Environment(devnull = None)
    assert env.devnull is None

    env = Environment(config_dir = "config_dir_name", program_name = "httpie_name")
    assert env.config_dir == "config_dir_name"
    assert env.program_name == "httpie_name"

    env = Environment(program_name = "httpie_name")
    assert env.program_name == "httpie_name"

# Generated at 2022-06-13 21:40:59.420565
# Unit test for constructor of class Environment
def test_Environment():
    def open():
        return open(os.devnull)
    environment = Environment(stdin = stdin, stdout = stdout, stderr = stderr, devnull = open())
    assert environment.stdin == stdin
    assert environment.stdout == stdout
    assert environment.stderr == stderr
    assert environment._devnull == open()


# Generated at 2022-06-13 21:41:02.541638
# Unit test for constructor of class Environment
def test_Environment():
    import io
    env = Environment(stdin=io.StringIO(), stdout=io.StringIO(), stderr=io.StringIO())
    assert env.stdin.readable()
    assert env.stdout.writable()
    assert env.stderr.writable()

# Generated at 2022-06-13 21:41:14.181554
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == (sys.stdin.isatty() if sys.stdin else False)
    assert env.stdin_encoding == None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding == None
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.colors == 256
    assert env.program_name == 'http'


# Generated at 2022-06-13 21:41:25.771353
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull ='abc')
    env.__dict__['config'] = 'xyz'
    env.__dict__['devnull'] = 'xyz'
    env.__dict__['_orig_stderr'] = 'xyz'
    env.program_name = 'xyz'
    env.stdin = 'xyz'
    env.stdin_encoding = 'xyz'
    env.stdout = 'xyz'
    env.stdout_encoding = 'xyz'
    env.stderr = 'xyz'
    del env.__dict__['_config']
    assert env.is_windows is False
    assert env.config_dir =='/root/.config/httpie'
    assert env.stdin is 'xyz'

# Generated at 2022-06-13 21:41:35.687424
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(sboo=42)
    assert env.sboo == 42


# Generated at 2022-06-13 21:41:48.019424
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()

    # test is_windows
    assert env.is_windows == is_windows

    # test program_name
    assert env.program_name == 'http'

    # test config_dir
    assert env.config_dir == DEFAULT_CONFIG_DIR

    # test stdin and stdin_isatty
    assert env.stdin == sys.stdin
    assert stdin.isatty() == env.stdin_isatty

    # test stdout and stdout_isatty
    assert env.stdout == sys.stdout
    assert stdout.isatty() == env.stdout_isatty

    # test stderr and stderr_isatty
    assert env.stderr == sys.stderr
    assert stderr.isatty() == env.stder

# Generated at 2022-06-13 21:42:05.395637
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        is_windows=True,
        config_dir='~/.httpie',
        stdin=Object(),
        stdin_isatty=True,
        stdin_encoding='utf-8',
        stdout=Object(),
        stdout_isatty=True,
        stdout_encoding='utf-8',
        stderr=Object(),
        stderr_isatty=True,
        colors=256,
        program_name='httpie',
    )
    assert env
    assert env.is_windows is True
    assert env.config_dir == '~/.httpie'
    assert env.stdin is Object()
    assert env.stdin_isatty is True
    assert env.stdin_encoding == 'utf-8'
    assert env.stdout is Object

# Generated at 2022-06-13 21:42:10.239048
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin=1)
    assert env.stdin == 1
    env2 = Environment(stdin=2, stdout=3)
    assert env2.stdin == 2
    assert env2.stdout == 3

# Generated at 2022-06-13 21:42:22.751086
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment().is_windows == is_windows
    assert Environment(is_windows=False).is_windows == False
    assert Environment().config_dir == DEFAULT_CONFIG_DIR
    assert Environment(config_dir="\path").config_dir == "\path"
    assert Environment().stdin == sys.stdin
    assert Environment(stdin = None).stdin == None
    assert Environment().stdin_isatty == sys.stdin.isatty()
    assert Environment(stdin_isatty=False).stdin_isatty == False
    assert Environment().stdin_encoding == None
    assert Environment(stdin_encoding="utf8").stdin_encoding == "utf8"
    assert Environment().stdout == sys.stdout 
    assert Environment(stdout = sys.stdin).stdout == sys.std

# Generated at 2022-06-13 21:42:27.055222
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.__dict__ is not None
    assert env.devnull is None
    assert isinstance(env, Environment)


# Generated at 2022-06-13 21:42:34.257866
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment()
    assert e.is_windows == True
    assert e.config_dir == DEFAULT_CONFIG_DIR
    assert e.stdin == sys.stdin
    assert e.stdin_isatty == True
    assert e.stdin_encoding == 'utf8'
    assert e.stdout == sys.stdout
    assert e.stdout_isatty == True
    assert e.stdout_encoding == 'utf8'
    assert e.stderr == sys.stderr
    assert e.stderr_isatty == True
    assert e.colors == 256
    assert e.program_name == 'http'


# Generated at 2022-06-13 21:42:48.666797
# Unit test for constructor of class Environment
def test_Environment():
    import io
    import sys

    class DummyStream(io.StringIO):
        def __init__(self):
            pass

        @property
        def encoding(self):
            return 'utf-8'

    stream = DummyStream()
    env = Environment(stdin = None, stdin_encoding = 'utf-8', stdout = stream, stdout_encoding = 'utf-8',
                      stderr = stream, stderr_isatty = True, colors = 256, program_name = 'http')
    assert env.stdin == sys.stdin
    assert env.stdin_encoding == 'utf-8'
    assert env.stdout_encoding == 'utf-8'
    assert env.stderr_isatty == True
    assert env.colors == 256
    assert env.program_

# Generated at 2022-06-13 21:43:00.018587
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(is_windows=False)

    assert not env.is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty
    assert env.stdin_encoding is None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty
    assert env.stdout_encoding is None
    assert env.stderr == sys.stderr
    assert env.stderr_isatty
    assert env.colors == 256
    assert env.program_name == 'http'



# Generated at 2022-06-13 21:43:04.435551
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment.stdin_encoding == None
    assert Environment.stdout_encoding == None
    Environment(stdin_encoding = 'utf8', stdout_encoding = 'ascii')
    assert Environment.stdin_encoding == 'utf8'
    assert Environment.stdout_encoding == 'ascii'

# Generated at 2022-06-13 21:43:13.355793
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.__str__() == '<Environment>'
    assert env.__repr__() == '<Environment {colors=256, colors256=False, \
is_windows=False, stdin=/dev/pts/3, stdin_isatty=True, stdin_encoding=utf-8, \
stdout=/dev/pts/3, stdout_isatty=True, stdout_encoding=utf-8, \
stderr=/dev/pts/3, stderr_isatty=True, stderr_encoding=utf-8, colors16m=True, \
program_name=http}>'


# Generated at 2022-06-13 21:43:20.259442
# Unit test for constructor of class Environment
def test_Environment():

    import pytest

    env = Environment()
    env = Environment(colors=128)
    env.stdin_encoding = 'utf8'
    env.stdin=sys.stdin
    env.stdout=sys.stdout
    env.stdout_encoding = 'utf8'
    env.stderr = sys.stderr
    with pytest.raises(ConfigFileError):
        env.config

# Generated at 2022-06-13 21:43:39.639244
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.config_dir == Path(DEFAULT_CONFIG_DIR)
    assert env.stderr is sys.stderr
    assert env.stderr_isatty is sys.stderr.isatty()
    assert env.stderr_encoding is None
    assert env.stdout is sys.stdout
    assert env.stdout_isatty is sys.stdout.isatty()
    assert env.stdout_encoding is None
    assert env.stdin is sys.stdin
    assert env.stdin_isatty is sys.stdin.isatty()
    assert env.stdin_encoding is None
    # Another test
    env = Environment(stdout_encoding='utf-8', stdin_encoding='gb2312')
    assert env

# Generated at 2022-06-13 21:43:46.630539
# Unit test for constructor of class Environment
def test_Environment():

    is_windows = Environment.is_windows
    config_dir = Environment.config_dir
    stdin = Environment.stdin
    stdin_isatty = Environment.stdin_isatty
    stdin_encoding = Environment.stdin_encoding
    stdout = Environment.stdout
    stdout_isatty = Environment.stdout_isatty
    stdout_encoding = Environment.stdout_encoding
    stderr = Environment.stderr
    stderr_isatty = Environment.stderr_isatty
    colors = Environment.colors
    program_name = Environment.program_name


# Generated at 2022-06-13 21:43:54.449514
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == bool(sys.stdin and sys.stdin.isatty())
    assert env.stdin_encoding == getattr(sys.stdin, 'encoding', None) or 'utf-8'
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding == getattr(sys.stdout, 'encoding', None) or 'utf-8'
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stder

# Generated at 2022-06-13 21:43:56.394761
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    print(env)

# Generated at 2022-06-13 21:44:06.037388
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    import os
    from httpie.compat import is_windows
    from httpie.config import DEFAULT_CONFIG_DIR
    from httpie.utils import repr_dict
    from httpie.core import Environment
    env = Environment()
    print("\nstart")
    print("is_windows:" + str(env.is_windows))
    print("config_dir:" + str(env.config_dir))
    print("stdin:" + str(env.stdin))
    print("stdin_isatty:" + str(env.stdin_isatty))
    print("stdin_encoding:" + str(env.stdin_encoding))
    print("stdout:" + str(env.stdout))
    print("stdout_isatty:" + str(env.stdout_isatty))

# Generated at 2022-06-13 21:44:10.466349
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name='httpie', colors = 256)
    assert env.program_name == 'httpie', "The program name is wrong"
    assert env.colors == 256, "The colors is wrong"



# Generated at 2022-06-13 21:44:22.231420
# Unit test for constructor of class Environment
def test_Environment():
	env = Environment()
	if is_windows:
		assert env.colors == 0
	else:
		assert env.colors == 256
	assert env.stderr == sys.stderr
	assert env.stdout == sys.stdout
	assert env.stdin == sys.stdin
	assert env.program_name == 'http'
	assert env.stdout_isatty == sys.stdout.isatty()
	assert env.stdin_isatty == sys.stdin.isatty()
	assert env.stderr_isatty == sys.stderr.isatty()
	assert env.config_dir == DEFAULT_CONFIG_DIR
	assert env.is_windows == is_windows
	#assert env.config == Config(directory=DEFAULT_CONFIG_DIR)

# Generated at 2022-06-13 21:44:26.168257
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin='a', stdout='b', stderr='c', program_name='d')
    assert env.stdin == 'a'
    assert env.stdout == 'b'
    assert env.stderr == 'c'
    assert env.program_name == 'd'


# Generated at 2022-06-13 21:44:32.582231
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(is_windows=True, stdin=sys.stdin, stdout=sys.stdout,
                      stderr=sys.stderr, devnull=sys.devnull, config_dir=DEFAULT_CONFIG_DIR,
                      program_name='http')
    print(env.__dict__)


if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:44:35.698522
# Unit test for constructor of class Environment
def test_Environment():
    """
    >>> env = Environment(program_name='http')
    >>> env.program_name
    'http'
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 21:44:50.709166
# Unit test for constructor of class Environment
def test_Environment():
    en = Environment()
    assert hasattr(en, 'config_dir')
    assert hasattr(en, 'stdin')
    assert hasattr(en, 'stdout')
    assert hasattr(en, 'stderr')
    assert hasattr(en, 'program_name')
    assert hasattr(en, 'colors')
    assert hasattr(en, 'is_windows')


# Generated at 2022-06-13 21:45:01.907045
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment(
        devnull=1,
        is_windows=False,
        config_dir=DEFAULT_CONFIG_DIR,
        stdin=sys.stdin,
        stdin_isatty=sys.stdin.isatty(),
        stdin_encoding=None,
        stdout=sys.stdout,
        stdout_isatty=sys.stdout.isatty(),
        stdout_encoding=None,
        stderr=sys.stderr,
        stderr_isatty=sys.stderr.isatty(),
        colors=256,
        program_name='http'
    )
    print(environment)
    print(environment.config_dir)
    print(environment.stdin)
    print(environment.stdin_isatty)
   

# Generated at 2022-06-13 21:45:13.438409
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.__dict__ == dict(type(env).__dict__)

    devnull = open(os.devnull, 'w+')
    env = Environment(devnull=devnull,
                      is_windows=True,
                      config_dir='./test',
                      stdin=sys.stdin,
                      stdin_isatty=True,
                      stdin_encoding="utf8",
                      stdout=sys.stdout,
                      stdout_isatty=True,
                      stdout_encoding="utf8",
                      stderr=sys.stderr,
                      stderr_isatty=True,
                      colors=240,
                      program_name="http12345")
    assert env.devnull == devnull
    assert env.is_windows == True

# Generated at 2022-06-13 21:45:16.236995
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert isinstance(env, Environment)

if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:45:27.169184
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    import io
    buf1 = io.BytesIO()
    buf2 = io.BytesIO()
    buf3 = io.BytesIO()
    env = Environment(
        colors=256,
        stdin=buf1,
        stdin_encoding='utf8',
        stdout=buf2,
        stdout_encoding='utf8',
        stdout_isatty=True,
        stderr=buf3,
        stderr_isatty=True,
        program_name='http',
    )
    env.__dict__.update(
        is_windows=sys.platform.startswith("win32"),
        config_dir=DEFAULT_CONFIG_DIR,
    )
    # Test __str__() and __repr__()
    print(env)

# Generated at 2022-06-13 21:45:37.481288
# Unit test for constructor of class Environment
def test_Environment():
    '''
    parameter: None
    return: none
    '''
    env = Environment(config_dir=True,
                      stderr=True,
                      stderr_isatty=True,
                      stdin=True,
                      stdin_isatty=True,
                      stdout=True,
                      stdout_isatty=True,
                      stdout_encoding=True)
    assert env.config_dir is True
    assert env.stderr is True
    assert env.stderr_isatty is True
    assert env.stdin is True
    assert env.stdin_isatty is True
    assert env.stdout_isatty is True
    assert env.stdout is True
    assert env.stdout_encoding is True

# Generated at 2022-06-13 21:45:41.086259
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stderr_encoding == sys.stderr.encoding

# Generated at 2022-06-13 21:45:47.720525
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull='devnull', stderr=sys.stdout)
    assert env.devnull == 'devnull'
    assert env.stderr == sys.stdout
    env = Environment(stdout=sys.stderr)
    assert env.stdout == sys.stderr
    env = Environment(devnull='random')
    assert env.devnull == 'devnull'


# Generated at 2022-06-13 21:46:03.722727
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull = 'devnull', program_name = 'http')
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.colors == 256
    assert env.is_windows == is_windows
    assert env.program_name == 'http'
    assert env.devnull == 'devnull'
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.config_dir == DEFAULT_CONFIG_DIR

test_Environment()


globalenv = Environment()

# Generated at 2022-06-13 21:46:16.163028
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        is_windows=False,
        config_dir='/path/to/config/dir',
        stdin=None,
        stdin_isatty=False,
        stdin_encoding='utf-8',
        stdout=None,
        stdout_isatty=False,
        stdout_encoding=None,
        stderr=None,
        stderr_isatty=False,
        colors=True,
        program_name='httpie',
    )
    assert env.is_windows is False
    assert env.config_dir == Path('/path/to/config/dir')
    assert env.stdin is None
    assert env.stdin_isatty is False
    assert env.stdin_encoding == 'utf-8'
    assert env.stdout

# Generated at 2022-06-13 21:46:30.884865
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment()
    assert environment.is_windows == is_windows
    assert environment.config_dir == DEFAULT_CONFIG_DIR
    assert environment.stdin == sys.stdin
    assert environment.stdout == sys.stdout
    assert environment.stderr == sys.stderr
    assert environment.colors == 256
    assert environment.program_name == 'http'
    assert environment._orig_stderr == sys.stderr
    assert environment.config is not None

# Generated at 2022-06-13 21:46:31.881182
# Unit test for constructor of class Environment
def test_Environment():
    assert isinstance(Environment(), (Environment))

# Generated at 2022-06-13 21:46:40.245986
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout=sys.stderr)
    assert env.stdout is sys.stderr
    assert not env.stdout_isatty
    assert env.stdout_encoding
    env = Environment(stdout=sys.stdout, stdout_isatty=True)
    assert env.stdout is sys.stdout
    assert env.stdout_isatty
    assert env.stdout_encoding
    # devnull
    env = Environment(devnull=sys.stderr)
    assert env.devnull is sys.stderr
    assert env.devnull is sys.stderr
    devnull = sys.stdout
    env = Environment(devnull=devnull)
    assert env.devnull is sys.stdout


# Generated at 2022-06-13 21:46:45.638019
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert repr(env) == "<Environment {'__dict__': {}, '_config': None, ...}"
    env = Environment(devnull=True)
    assert repr(env) == "<Environment {'__dict__': {}, '_config': None, ...}"

# Generated at 2022-06-13 21:46:52.686829
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        is_windows=False,
        config_dir="/dir/path",
        stdin=sys.stdin,
        stdin_encoding="utf8",
        stdout=sys.stdout,
        stdout_encoding="utf8",
        stderr=sys.stderr,
        stderr_isatty=False,
        colors=True,
        program_name="http"
    )
    assert isinstance(env, Environment)

# Generated at 2022-06-13 21:46:56.151182
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment(stdout_isatty=True, stdin_isatty=False)
    assert e.stdout_isatty is True
    assert e.stdin_isatty is False

# Generated at 2022-06-13 21:47:05.963193
# Unit test for constructor of class Environment
def test_Environment():

    env = Environment(
        is_windows=True,
        config_dir=DEFAULT_CONFIG_DIR,
        stdin=sys.stdin,
        stdin_isatty=True,
        stdin_encoding=None,
        stdout=sys.stdout,
        stdout_isatty=True,
        stdout_encoding=None,
        stderr=sys.stderr,
        stderr_isatty=True,
        stderr_encoding=None,
        program_name='http'
        )
    print(env)
#Unit test for the colorama.initialise part
#def test_colorama():
#    from colorama import initialise

# Generated at 2022-06-13 21:47:17.327258
# Unit test for constructor of class Environment
def test_Environment():
    test_env = Environment(devnull = 'test_devnull')
    assert test_env.devnull == 'test_devnull'
    assert not test_env.stdin
    assert test_env.stdin_isatty == False
    assert test_env.stdin_encoding == None
    assert test_env.stdout == sys.stdout
    assert test_env.stdout_isatty == True
    assert test_env.stdout_encoding == 'utf8'
    assert test_env.stderr == sys.stderr
    assert test_env.stderr_isatty == True
    assert test_env.colors == 256
    assert test_env.program_name == 'http'


# Generated at 2022-06-13 21:47:20.559413
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment(devnull=os.devnull, stdin=sys.stdin, stdout=sys.stdout)
    assert environment.devnull.name == '/dev/null'

# Generated at 2022-06-13 21:47:24.151094
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(a=1, b=2)
    assert env.a == 1
    assert env.b == 2



# Generated at 2022-06-13 21:47:51.949478
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == True
    assert env.config_dir == Path('~\\.config\\httpie')
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == False
    assert env.stdin_encoding == 'cp950'
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == True
    assert env.stdout_encoding == 'cp950'
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == True
    assert env.colors == 16
    assert env.program_name == 'http'

# Generated at 2022-06-13 21:47:53.889493
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment()
    assert environment

# Generated at 2022-06-13 21:48:02.499095
# Unit test for constructor of class Environment
def test_Environment():
    config_dir = DEFAULT_CONFIG_DIR
    stdin = sys.stdin  # `None` when closed fd (#791)
    stdin_isatty = stdin.isatty() if stdin else False
    # noinspection PyCompatibility
    stdin_encoding = getattr(stdin, 'encoding', None) or 'utf8'
    stdout = sys.stdout
    stdout_isatty = stdout.isatty()
    # noinspection PyCompatibility
    stdout_encoding = getattr(stdout, 'encoding', None) or 'utf8'
    stderr = sys.stderr
    stderr_isatty = stderr.isatty()
    colors = 256
    is_windows = is_windows

# Generated at 2022-06-13 21:48:05.195878
# Unit test for constructor of class Environment
def test_Environment():
    a = Environment()
    print(a)

if __name__ == "__main__":
    test_Environment()

# Generated at 2022-06-13 21:48:12.157870
# Unit test for constructor of class Environment
def test_Environment():
    import io
    fp = io.BytesIO()
    env = Environment(
        devnull = fp,
        program_name = 'http',
        colors = 256,
        stdout = fp,
        stderr = fp,
        is_windows = True,
        stdin_isatty = True,
        stdin = fp,
        stdout_isatty = False,
        stderr_isatty = True,
    )
    print(env)

if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:48:16.012899
# Unit test for constructor of class Environment
def test_Environment():
    env=Environment()
    print(env)

if __name__ == '__main__':
    print(test_Environment())

# Generated at 2022-06-13 21:48:27.081162
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment.__new__(Environment)
    assert env.is_windows is is_windows
    assert env.stdin is sys.stdin
    assert env.stdin_isatty is sys.stdin.isatty()
    assert env.stdin_encoding is None
    assert env.stdout is sys.stdout
    assert env.stdout_isatty is sys.stdout.isatty()
    assert env.stdout_encoding is None
    assert env.stderr is sys.stderr
    assert env.stderr_isatty is sys.stderr.isatty()
    assert env.colors == 256
    assert env.program_name == 'http'
    assert env._orig_stderr is sys.stderr
    assert env._devnull is None


# Generated at 2022-06-13 21:48:28.806533
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    print(env)

# Generated at 2022-06-13 21:48:31.772531
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env._orig_stderr == sys.stderr

# Generated at 2022-06-13 21:48:38.365480
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name='http')
    print(env)

# Generated at 2022-06-13 21:49:20.462745
# Unit test for constructor of class Environment
def test_Environment():
        env = Environment()
        assert env.is_windows == True
        assert env.config_dir == DEFAULT_CONFIG_DIR
        assert env.stdin == sys.stdin
        assert env.stdin_isatty == sys.stdin.isatty()
        assert env.stdin_encoding == None
        assert env.stdout == sys.stdout
        assert env.stdout_isatty == True
        assert env.stdout_encoding == None
        assert env.stderr == sys.stderr
        assert env.stderr_isatty == False
        assert env.program_name == 'http'
        
        assert env.__str__() == 'http'
        assert env.__repr__() == '<Environment {}>'

# Generated at 2022-06-13 21:49:23.845469
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout = sys.stdout)
    if env.stdout_isatty and env.is_windows:
        print("stdout is tty and os is windows")

# Generated at 2022-06-13 21:49:34.195219
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(is_windows=True, config_dir='myconfig.json')
    assert env.is_windows == True
    assert env.config_dir == 'myconfig.json'
    assert env.stdin == '<_io.TextIOWrapper name=sys.stdin mode=r encoding=utf-8>'
    assert env.stdin_isatty == True
    assert env.stdin_encoding == 'utf8'
    assert env.stdout == '<_io.TextIOWrapper name=sys.stdout mode=w encoding=utf-8>'
    assert env.stdout_isatty == True
    assert env.stdout_encoding == 'utf8'

# Generated at 2022-06-13 21:49:41.450535
# Unit test for constructor of class Environment
def test_Environment():
    env_one = Environment(is_windows=True)
    assert env_one.is_windows is True
    assert env_one.config_dir == DEFAULT_CONFIG_DIR
    assert env_one.stdin is None
    assert env_one.stdin_isatty == False
    assert env_one.stdin_encoding is None
    assert env_one.stdout is sys.stdout
    assert env_one.stdout_isatty == True
    assert env_one.stdout_encoding is None
    assert env_one.stderr is sys.stderr
    assert env_one.stderr_isatty == True
    assert env_one.colors == 256
    assert env_one.program_name == 'http'
    assert env_one._devnull is None
    assert env_

# Generated at 2022-06-13 21:49:53.061739
# Unit test for constructor of class Environment
def test_Environment():
    program_name = 'http'
    config_dir = DEFAULT_CONFIG_DIR
    stdin = sys.stdin
    stdin_isatty = stdin.isatty()
    stdin_encoding = 'utf8'
    stdout = sys.stdout
    stdout_isatty = stdout.isatty()
    stdout_encoding = 'utf8'
    stderr = sys.stderr
    stderr_isatty = stderr.isatty()
    colors = 256
    if not is_windows:
        if curses:
            try:
                curses.setupterm()
                colors = curses.tigetnum('colors')
            except curses.error:
                pass
    # Default environment
    env = Environment()
    assert env.program_name == program_

# Generated at 2022-06-13 21:50:00.821441
# Unit test for constructor of class Environment
def test_Environment():
    stdin = sys.stdin
    stdout = sys.stdout
    stderr = sys.stderr
    config_dir = DEFAULT_CONFIG_DIR 
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == config_dir
    assert env.stdin == stdin
    assert env.stdin_isatty == stdin.isatty()
    assert env.stdout == stdout
    assert env.stdout_isatty == stdout.isatty()
    assert env.stderr == stderr
    assert env.stderr_isatty == stderr.isatty()
    assert env.program_name == "http"
    assert env.config == env.config
    assert env.devnull == env.devnull
   

# Generated at 2022-06-13 21:50:07.684426
# Unit test for constructor of class Environment
def test_Environment():
    import io
    import tempfile
    import unittest

    class EnvironmentTest(unittest.TestCase):

        def test_default(self):
            env = Environment()
            self.assertTrue(isinstance(env.stderr, io.TextIOWrapper))
            self.assertTrue(isinstance(env.stdout, io.TextIOWrapper))
            self.assertTrue(isinstance(env.stdin, io.TextIOWrapper))
            self.assertEqual(env.program_name, 'http')
            self.assertTrue(isinstance(env.config_dir, Path))
            self.assertTrue(isinstance(env._orig_stderr, io.TextIOWrapper))

        def test_overwrite_stderr(self):
            fd = tempfile.TemporaryFile()

# Generated at 2022-06-13 21:50:12.117328
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin = None, stdout = None, stderr = None)
    env.stdin = sys.stdin
    env.stdout = sys.stdout
    env.stderr = sys.stderr
    env._config = Config