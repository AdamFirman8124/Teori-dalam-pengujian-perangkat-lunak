

# Generated at 2022-06-13 21:40:20.575822
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin='DEVNULL', stdout='STDOUT', stderr='STDERR')
    assert env.stdin == 'DEVNULL'
    assert env.stdout == 'STDOUT'
    assert env.stderr == 'STDERR'
    assert env.program_name == 'http'

# Generated at 2022-06-13 21:40:22.198062
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()

    with env.stdin:
        pass

# Generated at 2022-06-13 21:40:25.530700
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert type(env) == Environment
    _test_Environment(env)

    env = Environment(program_name='test')
    assert type(env) == Environment
    _test_Environment(env)


# Generated at 2022-06-13 21:40:35.811324
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin=None, stdout=sys.stdout, stdin_isatty=True,
                      stdin_encoding='utf8', stdout_isatty=False, stdout_encoding='utf8',
                      stderr=sys.stderr, stderr_isatty=False, enable_unicode=True, enable_colors=True,
                      config_dir='C:/Users/zhiw_cao/AppData/Local/httpie/config')
    if env.stdin:
        stdin_isatty = env.stdin.isatty()
    else:
        stdin_isatty = False

    if env.stdout_isatty:
        stdout_encoding = sys.stdout.encoding

# Generated at 2022-06-13 21:40:48.580276
# Unit test for constructor of class Environment
def test_Environment():
    import io

    class DummyStdIO:
        encoding = 'UTF-8'
        isatty = True

    env = Environment(
        stdin=DummyStdIO(),
        stdout=DummyStdIO(),
        stderr=DummyStdIO(),
        devnull=io.StringIO(),
        program_name='http',
        config_dir=Path(__file__),
    )

# Generated at 2022-06-13 21:40:55.152090
# Unit test for constructor of class Environment
def test_Environment():
    print("\n\n***** test_Environment *****")

    # Unit test for constructor of class Environment
    env = Environment(stdout = sys.stderr)
    print("env: {0}".format(env.__dict__))


if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:40:56.369844
# Unit test for constructor of class Environment
def test_Environment():
    assert 'stdin_isatty' in str(Environment())


# Generated at 2022-06-13 21:41:07.627046
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin=None, stdout=None, stderr=None, devnull=None)
    assert env.is_windows == False
    assert env.stdin == None
    assert env.stdin_encoding == None
    assert env.stdin_isatty == None
    assert env.stdout == None
    assert env.stdout_encoding == None
    assert env.stdout_isatty == None
    assert env.stderr == None
    assert env.stderr_isatty == None
    assert env.colors == 256
    assert env.program_name == 'http'
    assert env._orig_stderr == None
    assert env._devnull == None
    assert env._config == None
    assert env.config == Config(directory='/httpie/')

# Generated at 2022-06-13 21:41:15.988128
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment().is_windows == is_windows, "Environment().is_windows is wrong"
    assert Environment().config_dir == DEFAULT_CONFIG_DIR, "Environment().config_dir is wrong"
    assert Environment().stdin == sys.stdin, "Environment().stdin is wrong"
    assert Environment().stdin_isatty == sys.stdin.isatty(), "Environment().stdin_isatty is wrong"
    assert Environment().stdin_encoding == None, "Environment().stdin_encoding is wrong"
    assert Environment().stdout == sys.stdout, "Environment().stdout is wrong"
    assert Environment().stdout_isatty == sys.stdout.isatty(), "Environment().stdout_isatty is wrong"

# Generated at 2022-06-13 21:41:26.252547
# Unit test for constructor of class Environment
def test_Environment():
    #Arrange
    #Act
    env = Environment(stdin_encoding = 'utf8', stdout_encoding = 'utf8', stderr_isatty = True, colors = 256)
    #Assert
    assert env is not None
    assert env.stdin_encoding == 'utf8'
    assert env.stdout_encoding == 'utf8'
    assert env.stderr_isatty is True
    assert env.colors == 256


# Generated at 2022-06-13 21:41:35.606296
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stderr.isatty()

    env = Environment(stderr=sys.stdout)
    assert env.stderr.isatty()

    env = Environment(stderr=sys.stderr)
    assert env.stderr.isatty()

# Generated at 2022-06-13 21:41:47.361708
# Unit test for constructor of class Environment
def test_Environment():
    stdin = io.StringIO()
    env = Environment(
        colors=0,
        stdin=stdin,
        stdin_encoding='utf-8',
        stdout_isatty=True,
        config_dir=Path('/tmp'),
        program_name="http"
    )
    assert env.is_windows is False
    assert env.stdin_isatty is True
    assert env.stdout_isatty is True
    assert env.colors == 0
    assert env.stdin_encoding == "utf-8"
    assert env.stdin is stdin
    assert env.config_dir == Path('/tmp')
    assert env.program_name == "http"



# Generated at 2022-06-13 21:41:56.835336
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(a=1, b=2)
    assert env.a == 1
    assert env.b == 2
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert type(env.config) == Config
    env = Environment()
    assert env.a is None
    assert env.b is None
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert type(env.config) == Config

# Generated at 2022-06-13 21:42:07.196374
# Unit test for constructor of class Environment
def test_Environment():
    assert not Environment().is_windows
    assert Environment().config_dir == DEFAULT_CONFIG_DIR
    assert Environment().stdin.isatty()
    assert Environment(is_windows=True).is_windows
    assert Environment(is_windows=True).config_dir == DEFAULT_CONFIG_DIR
    assert Environment(is_windows=True).stdin.isatty()
    assert Environment(config_dir=DEFAULT_CONFIG_DIR).config_dir == DEFAULT_CONFIG_DIR
    assert not Environment(config_dir=DEFAULT_CONFIG_DIR).is_windows
    assert Environment()._config == None
    assert Environment().stdin.isatty()
    assert Environment(config_dir=DEFAULT_CONFIG_DIR)._config == None
    assert Environment().config_dir == DEFAULT_CONFIG_DIR
   

# Generated at 2022-06-13 21:42:09.755244
# Unit test for constructor of class Environment
def test_Environment():
    if not isinstance(Environment(), Environment):
        raise Exception("Cannot create instance of class Environment")
    return True


# Generated at 2022-06-13 21:42:22.424148
# Unit test for constructor of class Environment

# Generated at 2022-06-13 21:42:27.601971
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    try:
        str(env)
    except Exception:
        print('str() fails')

    try:
        repr(env)
    except Exception:
        print('repr() fails')

test_Environment()

# Generated at 2022-06-13 21:42:32.217030
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment(config_dir="~/.httpie")
    assert e.config_dir == Path("~/.httpie")
    e = Environment(config_dir="~/.httpie", devnull="/dev/null")
    assert e.config_dir == Path("~/.httpie")
    assert e.devnull == "/dev/null"

test_Environment()

# Generated at 2022-06-13 21:42:46.518200
# Unit test for constructor of class Environment
def test_Environment():
    from httpie.compat import is_windows
    from httpie.config import DEFAULT_CONFIG_DIR
    from httpie.utils import get_requests_stream_kwargs
    from httpie import ExitStatus

    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin_isatty
    assert env.stdout_isatty
    assert env.stderr_isatty
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.stdin_encoding  # iso-8859-1
    assert env.stdout_encoding  # utf-8
    assert env.stderr

# Generated at 2022-06-13 21:43:00.744954
# Unit test for constructor of class Environment
def test_Environment():
    class TestEnv(Environment):
        def __init__(self):
            super().__init__()
    env = TestEnv()
    env.stdin = sys.stdin
    env.stdout = sys.stdout
    env.stderr = sys.stderr
    env.config_dir = DEFAULT_CONFIG_DIR
    env.program_name = 'http'

# Generated at 2022-06-13 21:43:18.033173
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    res = env.__str__()

# Generated at 2022-06-13 21:43:26.548701
# Unit test for constructor of class Environment
def test_Environment():
    print(Environment(devnull = 100))
    print(Environment(program_name = 'hello'))
    print(Environment(devnull = 100, program_name = 'hello'))
    print(Environment(devnull = '', program_name = 'hello'))
    print(Environment(devnull = '', program_name = 'hello', stdout_isatty = True))

# test_Environment()

# Generated at 2022-06-13 21:43:27.465091
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment()



# Generated at 2022-06-13 21:43:30.531993
# Unit test for constructor of class Environment
def test_Environment():
    if __name__ == "__main__":
        print(Environment())


test_Environment()

# Generated at 2022-06-13 21:43:34.350643
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(colors=1, stdin_encoding='stdin_encoding')
    assert env.colors == 1
    assert env.stdin_encoding == 'stdin_encoding'

# Generated at 2022-06-13 21:43:37.013746
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment(stdin=1, stdout=2, stderr=3)
    assert e.stdin == 1
    assert e.stdout == 2
    assert e.stderr == 3



# Generated at 2022-06-13 21:43:43.135508
# Unit test for constructor of class Environment
def test_Environment():
	new_env = Environment(devnull = sys.stdout)

	print(new_env.stderr)
	print(new_env.stdout)
	print(new_env.stdin)
	print(new_env)
	print(new_env._devnull)
	print(new_env.devnull)

	new_env.devnull = new_env.stdout
	print(new_env.devnull)

	new_env.stderr = new_env.stdout
	new_env.stdout = new_env.stdin

	print(new_env.stderr)
	print(new_env.stdout)
	print(new_env.stdin)
	print(new_env)
	print(new_env._devnull)

# Generated at 2022-06-13 21:43:46.050956
# Unit test for constructor of class Environment
def test_Environment():
    import inspect
    assert inspect.isclass(Environment)
    assert 'Environment' in str(Environment)

# Generated at 2022-06-13 21:43:54.181729
# Unit test for constructor of class Environment
def test_Environment():
    stdin = open('/dev/null', 'r')
    stdout = open('/dev/null', 'w')
    stderr = open('/dev/null', 'w')
    env = Environment(stdin = stdin,
                      stdout = stdout,
                      stderr = stderr)
    assert env.stdin == stdin
    assert env.stdout == stdout
    assert env.stderr == stderr
    assert env.stdin_isatty == stdin.isatty()
    assert env.stdout_isatty == stdout.isatty()
    assert env.stderr_isatty == stderr.isatty()
    assert env.stdin_encoding == stdin.encoding or 'utf8'
    assert env.stdout_encoding == std

# Generated at 2022-06-13 21:44:06.139425
# Unit test for constructor of class Environment
def test_Environment():
    import io
    import pytest
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as tmpdir:
        _orig_stdin = io.StringIO()
        _orig_stdout = io.StringIO()
        env = Environment(
            devnull=_orig_stdin,
            stdin=_orig_stdout,
            stdin_encoding='ascii',
            stdout=_orig_stdin,
            stdout_encoding='ascii',
            stderr=_orig_stdout,
            is_windows=True,
            config_dir=Path(tmpdir),
            program_name='test',
        )
        assert env.devnull is _orig_stdin
        assert env.stdin is _orig_stdout
        assert env.stdin_encoding == 'ascii'

# Generated at 2022-06-13 21:44:14.895312
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment()

# Generated at 2022-06-13 21:44:24.004554
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert(env.is_windows == is_windows)
    assert(env.config_dir == DEFAULT_CONFIG_DIR)
    assert(env.stdin == sys.stdin)
    assert(env.stdin_isatty == env.stdin.isatty())
    assert(env.stdout == sys.stdout)
    assert(env.stdout_isatty == env.stdout.isatty())
    assert(env.stderr == sys.stderr)
    assert(env.stderr_isatty == env.stderr.isatty())
    assert(env.program_name == 'http')
    assert(env.config == None)
    assert(env.devnull == None)

    from httpie.compat import is_windows

# Generated at 2022-06-13 21:44:35.286821
# Unit test for constructor of class Environment
def test_Environment():
    from tempfile import TemporaryDirectory
    import os

    with TemporaryDirectory() as config_dir:
        try:
            os.mkdir(os.path.join(config_dir, '.httpie'))
        except FileExistsError:
            pass
        env = Environment(config_dir=config_dir)

        assert env.config_dir == config_dir
        assert str(env.config_dir) == config_dir
        assert env.config_dir.name == '.httpie'
        assert env.config_dir.parent == config_dir

        assert env.is_windows == is_windows
        assert env.config_dir == DEFAULT_CONFIG_DIR
        assert env.stdin == sys.stdin
        assert env.stdin_isatty == sys.stdin.isatty()
        assert env.stdout == sys

# Generated at 2022-06-13 21:44:48.227679
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
    is_windows= True,
    config_dir = '/home/osboxes/.config/httpie',
    stdin = sys.stdin,
    stdin_isatty = sys.stdin.isatty(),
    stdin_encoding = getattr(sys.stdin, 'encoding', None) or 'utf8',
    stdout = sys.stdout,
    stdout_isatty = sys.stdout.isatty(),
    stdout_encoding = getattr(sys.stdout, 'encoding', None) or 'utf8',
    stderr = sys.stderr,
    stderr_isatty = sys.stderr.isatty(),
    colors = 256,
    program_name = 'http'
    )
    print(env)

# Generated at 2022-06-13 21:44:55.117755
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    print('stdout encodings:', env.stdin_encoding)
    print('stderr encodings:', env.stdout_encoding)
    print('config_dir:', env.config_dir)
    print('program_name:', env.program_name)
    print('devnull:', env.devnull)
    print('stdin:', env.stdin)
    print(env)

test_Environment()

# Generated at 2022-06-13 21:45:05.768754
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment(devnull = '/dev/null')
    assert isinstance(environment, Environment)
    assert environment.is_windows == False
    assert environment.config_dir == '/Users/user/.httpie'
    assert environment.stdin is sys.stdin
    assert environment.stdin_isatty == True
    assert environment.stdin_encoding == 'utf8'
    assert environment.stdout is sys.stdout
    assert environment.stdout_isatty == True
    assert environment.stdout_encoding == 'utf8'
    assert environment.stderr is sys.stderr
    assert environment.stderr_isatty == True
    assert environment.colors == 256
    assert environment.program_name == 'http'


# Generated at 2022-06-13 21:45:11.910509
# Unit test for constructor of class Environment
def test_Environment():
	import os
	from pathlib import Path
	enviroment = Environment()
	assert enviroment.is_windows == os.name == 'nt'
	assert enviroment.config_dir == Path.home() / '.config' / 'httpie'
	assert enviroment.stdin_isatty is True
	assert enviroment.stdin_encoding == 'utf8'
	assert enviroment.stdout_isatty is True
	assert enviroment.stdout_encoding == 'utf8'
	assert enviroment.stderr_isatty is True
	assert enviroment.colors == 256
	assert enviroment.program_name == 'http'
	assert enviroment._orig_stderr == enviroment.stderr
	

# Generated at 2022-06-13 21:45:17.534054
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert type(env).__name__ == 'Environment'
    assert env._orig_stderr == sys.stderr
    assert env._config is None
    assert env._devnull is None
    assert env.program_name == 'http'


import sys, os
from pytest import raises
from unittest.mock import Mock

from httpie.context import Environment


# Generated at 2022-06-13 21:45:24.290865
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name = "http", colors=256, stdout = "stdout", stderr = "stderr")
    assert env.__dict__['program_name'] == "http"
    assert env.__dict__['colors'] == 256
    assert env.__dict__['stdout'] == "stdout"
    assert env.__dict__['stderr'] == "stderr"

# Generated at 2022-06-13 21:45:36.679759
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()

    # Test if the constructor setting for attributes
    # is as per our expectation
    assert env.is_windows is not None, "is_windows not set"
    assert env.config_dir is not None, "config_dir not set"
    assert env.stdin is not None, "stdin not set"
    assert env.stdin_isatty is not None, "stdin_isatty not set"
    assert env.stdin_encoding is not None, "stdin_encoding not set"
    assert env.stdout is not None, "stdout not set"
    assert env.stdout_isatty is not None, "stdout_isatty not set"
    assert env.stdout_encoding is not None, "stdout_encoding not set"
    assert env.stderr

# Generated at 2022-06-13 21:45:50.102634
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.program_name == 'http'
    assert env.colors == 256

    env2 = Environment(program_name='new')
    assert env2.config_dir == DEFAULT_CONFIG_DIR
    assert env2.program_name == 'new'
    assert env2.colors == 256

# Generated at 2022-06-13 21:46:02.477000
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name='http')
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == True
    assert env.stdin_encoding == None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == True
    assert env.stdout_encoding == None
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == True
    assert env.program_name == 'http'
    assert env.config_dir == DEFAULT_CONFIG_DIR


# Generated at 2022-06-13 21:46:14.916486
# Unit test for constructor of class Environment

# Generated at 2022-06-13 21:46:18.016304
# Unit test for constructor of class Environment
def test_Environment():
    if (Environment().stdin_encoding == 'ANSI_X3.4-1968'):
        return False
    return True


# Generated at 2022-06-13 21:46:27.460376
# Unit test for constructor of class Environment
def test_Environment():
    orig_env = Environment()
    env = Environment(
        stdin=None,
        stdout=orig_env.stdout,
        stderr=orig_env.stderr,
    )
    assert env.stdin is None
    assert env.stdout is orig_env.stdout
    assert env.stderr is orig_env.stderr
    assert env.stdout_encoding == orig_env.stdout_encoding
    assert env.stderr_encoding == orig_env.stdout_encoding



# Generated at 2022-06-13 21:46:31.090187
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment(stdout=None, stderr=None, stdin=None)
    assert e.stdout == None, "stdout should be None"
    assert e.stderr == None, "stderr should be None"
    assert e.stdin == None, "stdin should be None"

    if __name__ == '__main__':
        test_Environment()

# Generated at 2022-06-13 21:46:40.048947
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment(**{'colors': 256, 'config_dir': DEFAULT_CONFIG_DIR, 'devnull': None, 'is_windows': False, 'program_name': 'http', 'stderr': sys.stderr, 'stderr_isatty': stderr.isatty(), 'stdin': stdin, 
    'stdin_isatty': stdin.isatty() if stdin else False, 'stdout': sys.stdout, 'stdout_isatty': stdout.isatty()})
    print(e)
    print(e.__dict__['config_dir'])
    print(type(e.__dict__['config_dir']))
    print(e.__dict__['program_name'])

# Generated at 2022-06-13 21:46:52.842362
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, program_name='http')
    print(env)
    test_data = {'stdin': sys.stdin, 'stdout': sys.stdout, 'stderr': sys.stderr, 'program_name': 'http', 'devnull': None, 'is_windows': False, 'config_dir': Path('~/.config/httpie'), 'stdin_isatty': True, 'stdin_encoding': 'utf8', 'stdout_isatty': True, 'stdout_encoding': 'utf8', 'stderr_isatty': True, 'colors': 256, 'config': Config(directory=Path('~/.config/httpie'))}

# Generated at 2022-06-13 21:47:00.441916
# Unit test for constructor of class Environment
def test_Environment():
    # create a Environment object
    env = Environment(stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, config_dir=DEFAULT_CONFIG_DIR)
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stderr == sys.stderr
    assert env.is_windows == is_windows
    if not is_windows:
        if curses:
            try:
                curses.setupterm()
                colors = curses.tigetnum('colors')
            except curses.error:
                pass
        else:
            colors = 256
    assert env.colors == colors

# Generated at 2022-06-13 21:47:08.812010
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin_isatty=False, stdout_isatty=False, stderr_isatty=False)
    print(env)
    assert not env.is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert not env.stdin_isatty
    assert not env.stdout_isatty
    assert not env.stderr_isatty

# Generated at 2022-06-13 21:47:29.180919
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        program_name="http",
        colors=256
    )
    assert env.program_name == "http"

# Generated at 2022-06-13 21:47:38.376038
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()

    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdin_encoding == getattr(
        sys.stdin, 'encoding', None) or 'utf8'
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding == getattr(
        sys.stdout, 'encoding', None) or 'utf8'
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.program_name == 'http'
    assert env.config_dir == DEFAULT_CONFIG_

# Generated at 2022-06-13 21:47:49.502952
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment.is_windows
    assert Environment.config_dir
    assert Environment.stdin
    assert Environment.stdin_isatty
    assert Environment.stdin_encoding
    assert Environment.stdout
    assert Environment.stdout_isatty
    assert Environment.stdout_encoding
    assert Environment.stderr
    assert Environment.stderr_isatty
    assert Environment.program_name
    assert not Environment._config
    assert not Environment._devnull
    assert Environment()


# Generated at 2022-06-13 21:47:51.143893
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.devnull



# Generated at 2022-06-13 21:47:57.423037
# Unit test for constructor of class Environment
def test_Environment():
    import sys, os
    assert isinstance(sys.stdin, Environment().stdin)
    assert isinstance(sys.stdout, Environment().stdout)
    assert isinstance(sys.stderr, Environment().stderr)
    assert isinstance(os.devnull, Environment().devnull)

if __name__ == '__main__' :
    print("Unit test for class Environment:")
    test_Environment()

# Generated at 2022-06-13 21:47:59.495705
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment(stdout_isatty=False)
    assert e.stdout_isatty == False


# Generated at 2022-06-13 21:48:00.431923
# Unit test for constructor of class Environment
def test_Environment():
    Environment(test=True)

# Generated at 2022-06-13 21:48:07.856452
# Unit test for constructor of class Environment
def test_Environment():
    # type: () -> None
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()


# unit test for property config of class Environment

# Generated at 2022-06-13 21:48:20.168828
# Unit test for constructor of class Environment
def test_Environment():

    try:
        import builtins
        input = getattr(builtins, 'raw_input', input)
    except (ImportError, NameError):
        pass
    env = Environment()
    # print(env)

# Generated at 2022-06-13 21:48:33.660540
# Unit test for constructor of class Environment
def test_Environment():
    """
    Unit test for Environment class
    """
    environment = Environment()
    assert environment.is_windows == is_windows
    assert isinstance(environment.config_dir, Path)
    assert environment.stdin == sys.stdin
    assert environment.stdin_isatty == sys.stdin.isatty()
    assert environment.stdin_encoding == 'utf8'
    assert environment.stdout == sys.stdout
    assert environment.stdout_isatty == sys.stdout.isatty()
    assert environment.stdout_encoding == 'utf8'
    assert environment.stderr == sys.stderr
    assert environment.stderr_isatty == sys.stderr.isatty()
    assert environment.program_name == 'http'
    assert environment.colors == 256


# Generated at 2022-06-13 21:49:14.294584
# Unit test for constructor of class Environment
def test_Environment():
    # https://docs.python.org/3/library/io.html#io.TextIOWrapper
    input_str = TextIOWrapper(
            open("/Users/troy/Projects/HTTPie/httpie/tests/fixtures/requests/README_with_unicode.md", "r"),
            encoding="utf8",
            line_buffering=True,
            write_through=True,
        )

    # print(input_str.encoding)
    # print(input_str.line_buffering)
    # print(input_str.write_through)
    # print(input_str.readable())
    # print(input_str.writable())
    # print(input_str.seekable())
    # print(input_str.buffer)

    # print(input_str.is

# Generated at 2022-06-13 21:49:19.501313
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment()
    print(environment)
    print(environment.config)
    print(environment.devnull)
    print(environment.log_error(msg='hello'))

if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:49:20.228991
# Unit test for constructor of class Environment
def test_Environment():
    pass

# Generated at 2022-06-13 21:49:24.983119
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert hasattr(env, "stdin")
    assert hasattr(env, "is_windows")
    assert hasattr(env, "config")
    assert hasattr(env, "devnull")
    assert isinstance(env.stdin, type(sys.stdin))



# Generated at 2022-06-13 21:49:29.368700
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    env.stdin = sys.stdin
    env.stdout = sys.stdout
    env.stderr = sys.stderr
    print(env)

if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:49:38.816139
# Unit test for constructor of class Environment
def test_Environment():
    # Create an environment object with stdout.
    env = Environment(stdout = sys.stdout)
    # Test the output of __repr__() of the object

# Generated at 2022-06-13 21:49:43.580281
# Unit test for constructor of class Environment
def test_Environment():
    from httpie.__main__ import main
    env = Environment()
    main()
    assert env.__class__.__name__ == 'Environment'
    assert env.stdout_isatty
    assert env.stdin_isatty


# Generated at 2022-06-13 21:49:48.909292
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout_isatty=1, stdout_encoding='ha')
    assert env.stdout_isatty == 1
    assert env.stdout_encoding == 'ha'

    env = Environment(stdout_isatty=0, stdout_encoding='ha')
    assert env.stdout_isatty == 0
    assert env.stdout_encoding == 'ha'


env = Environment()

# Generated at 2022-06-13 21:49:56.588802
# Unit test for constructor of class Environment
def test_Environment():
    env=Environment()
    print(env)
    print(env.__dict__)
    env2 = Environment(is_windows=True, stdin=None, stdout=sys.stdin,
                       stderr=sys.stdout, colors=256, program_name='http')
    print(env2)
    print(env2.__dict__)


# Generated at 2022-06-13 21:50:02.322819
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin = "stdin")
    assert env.stdin == "stdin"
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr