

# Generated at 2022-06-13 21:40:30.578320
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment(
        stdin=None,
        stdin_isatty=False,
        stdout=sys.stdout,
        stdout_isatty=False,
        stderr=sys.stderr,
        stderr_isatty=True,
        colors=256,
        program_name='http'
    )
    assert e.stdin is None
    assert e.stdin_isatty == False
    assert e.stdout == sys.stdout
    assert e.stdout_isatty == False
    assert e.stderr == sys.stderr
    assert e.stderr_isatty == True
    assert e.colors == 256
    assert e.program_name == 'http'
    print("Passed test_Environment()")


# Generated at 2022-06-13 21:40:39.113946
# Unit test for constructor of class Environment
def test_Environment():
	_key = 1
	for _key in range(1):
		env = Environment()
		__key = 1

# Generated at 2022-06-13 21:40:46.300999
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull = sys.stdin, stdin = sys.stdout, stdin_isatty = True,
                      stdout = sys.stderr, stdout_isatty = False, stdout_encoding = 'utf8',
                      stderr = sys.stdin, stderr_isatty = True, colors = 256, program_name = 'http')
    print(env)
    print(env.devnull)


# Generated at 2022-06-13 21:40:58.723360
# Unit test for constructor of class Environment
def test_Environment():
    # Initialize class environment with default values
    env = Environment()

    # Check default values
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()

    # test configuration
    assert isinstance(env.config, Config)
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert not env.config.is_new()

    # Overwrite class attributes and verify
    env.is_windows = False
    env.config_dir = 'config_dir'
    env.stdin = None

# Generated at 2022-06-13 21:41:04.936809
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.colors == 256
    assert env.program_name == "http"

# Test for property of class Environment

# Generated at 2022-06-13 21:41:15.300699
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin is sys.stdin  # `None` when closed fd (#791)
    assert env.stdin_isatty == env.stdin.isatty() if env.stdin else False
    assert env.stdin_encoding is None
    assert env.stdout is sys.stdout
    assert env.stdout_isatty == env.stdout.isatty()
    assert env.stdout_encoding is None
    assert env.stderr is sys.stderr
    assert env.stderr_isatty == env.stderr.isatty()
    assert env.colors == 256

# Generated at 2022-06-13 21:41:17.619114
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert type(env) == Environment

# Generated at 2022-06-13 21:41:29.287802
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name='testprogram')
    assert env.program_name == 'testprogram'
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
    assert env.program_name == 'testprogram'
    assert env._devnull is None

# Generated at 2022-06-13 21:41:36.586448
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == True
    if env.is_windows == True:
        assert env.colors == 256
    else:
        assert env.colors == 0
    assert env.stdin == sys.stdin
    assert env.stdin_encoding == 'UTF-8'
    assert env.stdout == sys.stdout
    assert env.stdout_encoding == 'UTF-8'
    assert env.stderr == sys.stderr
    assert env.stderr_encoding == 'UTF-8'

    if env.is_windows == False:
        assert env.program_name == 'http'
    else:
        assert env.program_name == 'http.exe'
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin

# Generated at 2022-06-13 21:41:48.257627
# Unit test for constructor of class Environment
def test_Environment():
    from httpie.client import ExitStatus
    from httpie.compat import is_windows
    from httpie import ExitStatus
    # devnull = open(os.devnull, 'w+')
    stderr = StringIO()
    stdin = StringIO()

    env = Environment(devnull=None, stderr=stderr, stdin_isatty=True)
    env.stdout.s = 0
    env.log_error('TEST ERROR')
    env.log_error('TEST WARNING', 'warning')

    # env.devnull = stdin
    # env.devnull = None
    # print('a', file=stdin, flush=True)
    # print(env.devnull)
    # verbose=True, stdin_isatty=True, stdout_isatty=True,

# Generated at 2022-06-13 21:42:05.513781
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.stdin_encoding is None
    assert env.stdout_encoding == sys.stdout.encoding
    assert env.program_name == "http"

# Generated at 2022-06-13 21:42:12.609788
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    """
    name = os.path.basename(sys.argv[0])
    if name == 'http':
        name = 'httpie'
    lookup = os.path.join(env.config_dir, 'lookup')
    lookup_default = os.path.join(env.config_dir, 'lookup.default')
    """
    print(env)
    print(env.config)


if __name__ == "__main__":
    test_Environment()

# Generated at 2022-06-13 21:42:23.790026
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        is_windows=False,
        config_dir='DOT_CONFIG_DIR',
        stdin='STDIN',
        stdin_isatty=False,
        stdin_encoding='STDIN_ENCODING',
        stdout='STDOUT',
        stdout_isatty=False,
        stdout_encoding='STDOUT_ENCODING',
        stderr='STDERR',
        stderr_isatty=False,
        colors=256,
        program_name='PROGRAM_NAME',
    )

    assert env.is_windows == False
    assert env.config_dir == 'DOT_CONFIG_DIR'
    assert env.stdin == 'STDIN'
    assert env.stdin_isatty == False

# Generated at 2022-06-13 21:42:27.728244
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin=False, stdout=False, stderr=False)
    assert env.stdin is False
    assert env.stdout is False
    assert env.stderr is False

# Generated at 2022-06-13 21:42:34.413125
# Unit test for constructor of class Environment
def test_Environment():
    x = Environment()
    assert x.is_windows == is_windows
    assert x.config_dir == DEFAULT_CONFIG_DIR
    assert x.stdin == sys.stdin
    assert x.stdin_isatty == sys.stdin.isatty()
    assert x.stdout == sys.stdout
    assert x.stdout_isatty == sys.stdout.isatty()
    assert x.stderr == sys.stderr
    assert x.stderr_isatty == sys.stderr.isatty()
    assert x.colors == 256
    assert x.program_name == 'http'

# Generated at 2022-06-13 21:42:47.921882
# Unit test for constructor of class Environment
def test_Environment():
    a = Environment()
    assert a.is_windows == Environment.is_windows
    assert a.config_dir == Environment.config_dir
    assert a.stdin == Environment.stdin
    assert a.stdin_isatty == Environment.stdin_isatty
    assert a.stdin_encoding == Environment.stdin_encoding
    assert a.stdout == Environment.stdout
    assert a.stdout_isatty == Environment.stdout_isatty
    assert a.stdout_encoding == Environment.stdout_encoding
    assert a.stderr == Environment.stderr
    assert a.stderr_isatty == Environment.stderr_isatty
    assert a.colors == Environment.colors
    assert a.program_name == Environment.program_name


# Generated at 2022-06-13 21:42:51.792604
# Unit test for constructor of class Environment
def test_Environment():
    new_env = Environment()
    assert new_env.stdin == sys.stdin
    assert new_env.config == Config(directory=DEFAULT_CONFIG_DIR)
    assert new_env.stdin_encoding == 'utf8'


environ = Environment()

# Generated at 2022-06-13 21:42:56.192126
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin=123)
    assert env.stdin == 123
    assert env.stdout_encoding is None
    assert hasattr(env, '_orig_stderr')
    assert hasattr(env, '_devnull')

# Generated at 2022-06-13 21:43:09.998003
# Unit test for constructor of class Environment
def test_Environment():
  env = Environment()
  assert env.is_windows == False
  assert env.config_dir == DEFAULT_CONFIG_DIR
  assert env.stdin == sys.stdin
  assert env.stdin_isatty == True
  assert env.stdin_encoding == "UTF-8"
  assert env.stdout == sys.stdout
  assert env.stdout_isatty == True
  assert env.stdout_encoding == "UTF-8"
  assert env.stderr == sys.stderr
  assert env.stderr_isatty == True
  assert env.colors == 256
  assert env.program_name == "http"


# Generated at 2022-06-13 21:43:15.423688
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin_isatty=False)
    assert env.stdin_isatty == False
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr


# Generated at 2022-06-13 21:43:31.800414
# Unit test for constructor of class Environment
def test_Environment():
    # case1: running with --traceback
    environment = Environment(program_name='httpie', stdin_isatty=False,
        stdout_isatty=False, stderr_isatty=False, colors=0)

# Generated at 2022-06-13 21:43:34.661235
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        stdin_encoding='utf8',
        stdout_encoding='utf8'
    )
    print(env)

test_Environment()

# Generated at 2022-06-13 21:43:42.071496
# Unit test for constructor of class Environment
def test_Environment():
    def p(arg, expected):
        actual = Environment(**arg)
        if actual != expected:
            print(f'input:       {arg}')
            print(f'expected:    {expected}')
            print(f'received:    {actual}')
    p({'stdin': 'a', 'stdout': 'b', 'stderr': 'c'},
      "<Environment {'stdin': 'a', 'stdout': 'b', 'stderr': 'c'}>")
    p({'stdin': 'a', 'stdout': 'b', 'stderr': 'c', 'is_windows': 'd'},
      "<Environment {'stdin': 'a', 'stdout': 'b', 'stderr': 'c', 'is_windows': 'd'}>")

# Generated at 2022-06-13 21:43:50.956820
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == True
    assert env.config_dir == '/home/baalajimaestro/.config/httpie'
    assert env.stdin_isatty == False
    assert env.stdin_encoding == 'UTF-8'
    assert env.stdout_isatty == True
    assert env.stdout_encoding == 'UTF-8'
    assert env.stderr_isatty == True
    assert env.colors == 256
    assert env.program_name == 'http'




# Generated at 2022-06-13 21:44:02.366716
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()

    if not is_windows:
        if curses:
            curses.setupterm()
            assert curses.tigetnum('colors') == env.colors
    else:
        from colorama.initialise import wrap_stream

# Generated at 2022-06-13 21:44:13.697331
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == (sys.stdin.isatty() if sys.stdin else False)
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.program_name == 'http'


# Generated at 2022-06-13 21:44:15.965759
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    assert Environment(stdout=sys.stderr).stdout == sys.stderr

# Generated at 2022-06-13 21:44:32.796738
# Unit test for constructor of class Environment
def test_Environment():
    def assert_env_equal(env1, env2):
        # Unit tests for environment class
        if env1.is_windows:
            assert env2.is_windows
        else:
            assert not env2.is_windows

        assert env1.config_dir == env2.config_dir
        assert env1.stdin == env2.stdin
        assert env1.stdin_isatty == env2.stdin_isatty
        assert env1.stdin_encoding == env2.stdin_encoding
        assert env1.stdout == env2.stdout
        assert env1.stdout_isatty == env2.stdout_isatty
        assert env1.stdout_encoding == env2.stdout_encoding
        assert env1.stderr == env2.stderr

# Generated at 2022-06-13 21:44:42.550009
# Unit test for constructor of class Environment
def test_Environment():
    print('\n')
    from httpie import exit_status

    env = Environment()
    print(env)
    assert env.is_windows == os.name == 'nt'
    assert env.config_dir == Path(
        os.getenv(
            'XDG_CONFIG_HOME',
            os.path.join(os.path.expanduser('~'), '.config')
        )
    ) / 'httpie'
    assert env.stdin is sys.stdin
    assert env.stdin.closed == False and env.stdin.isatty() == sys.stdin.isatty()
    assert env.stdout is sys.stdout
    assert env.stdout.closed == False and env.stdout.isatty() == sys.stdout.isatty()
    # noinspection PyProt

# Generated at 2022-06-13 21:44:54.252115
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=None)
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
    assert env._orig_stderr == sys.stderr
    assert env._devnull is None

# Generated at 2022-06-13 21:45:06.988193
# Unit test for constructor of class Environment
def test_Environment():
    try:
        sys.stdout.encoding
    except AttributeError:
        sys.stdin = mock.MagicMock()
        sys.stdout = mock.MagicMock()
        sys.stderr = mock.MagicMock()

    env = Environment(
        config_dir='/path/to/config',
        stdin=mock.MagicMock(),
        stdin_isatty=True,
        stdin_encoding='utf8',
        stdout=mock.MagicMock(),
        stdout_isatty=False,
        stdout_encoding='utf8',
        stderr=mock.MagicMock(),
        stderr_isatty=False,
        colors=256,
        program_name='http'
    )
    assert env.is_windows is False


# Generated at 2022-06-13 21:45:10.314218
# Unit test for constructor of class Environment
def test_Environment():
    # code
    e = Environment(devnull=None, **kwargs)
    assert all(hasattr(type(e), attr) for attr in kwargs.keys())
    assert isinstance(e, Environment)

# Generated at 2022-06-13 21:45:13.393210
# Unit test for constructor of class Environment
def test_Environment():
    environment_1 = Environment()
    environment_2 = Environment(program_name='hi')
    assert environment_1.program_name == 'http'
    assert environment_2.program_name == 'hi'

# Generated at 2022-06-13 21:45:21.274218
# Unit test for constructor of class Environment
def test_Environment():
    import io
    import os
    import sys
    import tempfile

    class MockStream:
        def __init__(self, name, encoding):
            self.name = name
            self.encoding = encoding
        def isatty(self):
            return False

    stdin = io.StringIO()
    stdout = io.StringIO()
    stderr = io.StringIO()

    directory = tempfile.TemporaryDirectory().name

# Generated at 2022-06-13 21:45:23.452013
# Unit test for constructor of class Environment
def test_Environment():
    assert isinstance(Environment(), Environment)

# Run unit tests
if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:45:30.341684
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin=None)
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin is None
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.colors == 256


# Generated at 2022-06-13 21:45:39.410770
# Unit test for constructor of class Environment
def test_Environment():
    class Mock:
        pass
    env = Environment(devnull=Mock, stdin=Mock, stdout=Mock, stderr=Mock)
    assert env.devnull == Mock
    assert env.stdin == Mock
    assert env.stdout == Mock
    assert env.stderr == Mock
    assert env._orig_stderr == Mock
    # test _config property is not None
    assert env.config is not None

# Generated at 2022-06-13 21:45:49.352246
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    env = Environment()
    assert env.is_windows == is_windows
    assert env.program_name == 'http'
    if not is_windows:
        assert env.colors == 256
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdin_encoding == None

# Generated at 2022-06-13 21:45:55.884288
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment().stderr == sys.stderr
    assert Environment()._orig_stderr == sys.stderr

    assert Environment(stderr=sys.stdout).stderr != sys.stderr

# Generated at 2022-06-13 21:46:02.554346
# Unit test for constructor of class Environment
def test_Environment():
    stdin = object()
    stdout = object()
    stderr = object()
    env = Environment(
        stdin=stdin,
        stdout=stdout,
        stderr=stderr
    )
    assert env.stdin is stdin
    assert env.stdout is stdout
    assert env.stderr is stderr

# Generated at 2022-06-13 21:46:16.917039
# Unit test for constructor of class Environment
def test_Environment():
    import io
    import os
    
    class TestStream(io.IOBase):
        def isatty(self): return False
        def fileno(self): return os.open(os.devnull, os.O_RDWR)
    
    env = Environment(stdin=TestStream(), stdout=sys.stdout, stderr=sys.stderr)
    assert env._stdin.isatty() == False
    assert env._stdin_isatty == False
    assert env._stdin_encoding is None
    assert env._stdout.isatty() == True
    assert env._stdout_isatty == True
    assert env._stdout_encoding == 'utf8'
    assert env._stderr.isatty() == True
    assert env._stderr_isatty == True


# Generated at 2022-06-13 21:46:25.293059
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.is_windows == is_windows
    assert env.colors == 256
    assert env.program_name == 'http'

    env = Environment(program_name='https')
    assert env.program_name == 'https'


# Generated at 2022-06-13 21:46:35.097883
# Unit test for constructor of class Environment
def test_Environment():
    assert repr(Environment()) == repr_dict({
        'is_windows': is_windows,
        'config_dir': str(DEFAULT_CONFIG_DIR),
        'stdin': '<stdin>',
        'stdin_isatty': sys.stdin.isatty(),
        'stdin_encoding': sys.stdin.encoding,
        'stdout': '<stdout>',
        'stdout_isatty': sys.stdout.isatty(),
        'stdout_encoding': sys.stdout.encoding,
        'stderr': '<stderr>',
        'stderr_isatty': sys.stderr.isatty(),
        'colors': 256,
        'program_name': 'http'
    })


# Main instance of the Environment

# Generated at 2022-06-13 21:46:37.380636
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin_isatty=False).stdin_isatty
    assert env == False


# Generated at 2022-06-13 21:46:44.801759
# Unit test for constructor of class Environment
def test_Environment():
    import io
    import json
    import sys
    import os
    from pathlib import Path
    import os.path
    import pytest
    import tempfile
    devnull = open(os.devnull, 'w+')

# Generated at 2022-06-13 21:46:55.696000
# Unit test for constructor of class Environment
def test_Environment():
    env=Environment(devnull=None, **kwargs)
    assert env
    assert not env.is_windows
    if curses:
        try:
            curses.setupterm()
            colors = curses.tigetnum('colors')
        except curses.error:
            assert env.colors == 256
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    if sys.stdin:
        assert env.stdin_isatty == env.stdin.isatty()
    else:
        assert not env.stdin_isatty
    assert env.stdout_isatty == env.stdout.isatty()
    assert env.stderr_isatty == env.stderr.isatty()

# Generated at 2022-06-13 21:47:06.980145
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stdin == sys.stdin
    assert env.stdin.isatty()
    assert env.stdin_isatty

    assert env.stdout == sys.stdout
    assert env.stdout.isatty()
    assert env.stdout_isatty

    assert env.stderr == sys.stderr
    assert env.stderr.isatty()
    assert env.stderr_isatty

    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert not env.is_windows
    assert env.colors == 256
    assert env.program_name == 'http'

    assert env.stdin.encoding is None
    assert env.stdout.encoding is None
    assert env.stderr.encoding is None

   

# Generated at 2022-06-13 21:47:18.094017
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert hasattr(env, 'is_windows')
    assert hasattr(env, 'config_dir')
    assert hasattr(env, 'stdin')
    assert hasattr(env, 'stdin_isatty')
    assert hasattr(env, 'stdin_encoding')
    assert hasattr(env, 'stdout')
    assert hasattr(env, 'stdout_isatty')
    assert hasattr(env, 'stdout_encoding')
    assert hasattr(env, 'stderr')
    assert hasattr(env, 'stderr_isatty')
    assert hasattr(env, 'colors')
    assert hasattr(env, 'program_name')
    assert hasattr(env, 'devnull')
    assert not hasattr(env, 'config')

# Generated at 2022-06-13 21:47:34.723828
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        is_windows=True,
        config_dir=Path('~/.config'),
        stdin=sys.stdin,
        stdin_encoding='utf8',
        stdout=sys.stdout,
        stdout_encoding='utf8',
        stderr=sys.stderr,
        colors=256,
        program_name='http',
        devnull=None
    )
    assert env.is_windows == True
    assert env.config_dir == Path('~/.config')
    assert env.stdin == sys.stdin
    assert env.stdin_encoding == 'utf8'
    assert env.stdout == sys.stdout
    assert env.stdout_encoding == 'utf8'
    assert env.stderr == sys.stderr
    assert env

# Generated at 2022-06-13 21:47:42.940821
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows is False
    assert env.config_dir is DEFAULT_CONFIG_DIR
    assert env.stdin is sys.stdin
    assert env.stdin_isatty is sys.stdin.isatty()
    assert env.stdin_encoding is None
    assert env.stdout is sys.stdout
    assert env.stdout_isatty is sys.stdout.isatty()
    assert env.stdout_encoding is None
    assert env.stderr is sys.stderr
    assert env.stderr_isatty is sys.stderr.isatty()
    assert env.colors is 256
    assert env.program_name is 'http'

# Generated at 2022-06-13 21:48:01.882484
# Unit test for constructor of class Environment
def test_Environment():
    try:
        from colorama import init as colorama_init
    except ImportError:
        colorama_init = None

    def patch_stream(stream):
        """Enable mocking of stream attributes for Windows."""
        if colorama_init and isinstance(stream, colorama_init.wrap_stream):
            return stream.wrapped
        return stream

    orig_stdin = patch_stream(sys.stdin)
    orig_stdout = patch_stream(sys.stdout)
    orig_stderr = patch_stream(sys.stderr)
    orig_stdin.encoding = 'mocked'
    orig_stdout.encoding = 'mocked'
    orig_stderr.encoding = 'mocked'

# Generated at 2022-06-13 21:48:12.793790
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    expected = {
        'config_dir': Path(DEFAULT_CONFIG_DIR),
        'colors': 256,
        'program_name': 'http',
        'stdin': sys.stdin,
        'stdin_isatty': sys.stdin.isatty(),
        'stdin_encoding': 'UTF-8',
        'stdout': sys.stdout,
        'stdout_isatty': sys.stdout.isatty(),
        'stdout_encoding': 'UTF-8',
        'stderr': sys.stderr,
        'stderr_isatty': sys.stderr.isatty(),
    }

    if sys.platform == 'win32':
        # noinspection PyUnresolvedReferences
        import colorama.initial

# Generated at 2022-06-13 21:48:25.623025
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        devnull='devnull',
        is_windows=False,
        stdin=sys.stdin,
        stdin_isatty=True,
        stdin_encoding='utf-8',
        stdout=sys.stdout,
        stdout_isatty=False,
        stdout_encoding=None,
        stderr=sys.stderr,
        stderr_isatty=True,
        program_name='http',
        config=None,
        config_dir='/opt/httpie',
    )

    assert env.devnull == "devnull"
    assert env.is_windows == False
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == True

# Generated at 2022-06-13 21:48:35.904677
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert isinstance(env, Environment)
    assert hasattr(env, '_orig_stderr')
    assert hasattr(env, '_devnull')
    assert hasattr(env, '_config')
    assert hasattr(env, 'is_windows')
    assert hasattr(env, 'config_dir')
    assert hasattr(env, 'stdin')
    assert hasattr(env, 'stdin_isatty')
    assert hasattr(env, 'stdin_encoding')
    assert hasattr(env, 'stdout')
    assert hasattr(env, 'stdout_isatty')
    assert hasattr(env, 'stdout_encoding')
    assert hasattr(env, 'stderr')
    assert hasattr(env, 'stderr_isatty')


# Generated at 2022-06-13 21:48:36.777801
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment()


# Generated at 2022-06-13 21:48:41.392177
# Unit test for constructor of class Environment
def test_Environment():
    """
    Test the constructor of Environment
    """
    env = Environment(stdin = "", stdout = "", stderr = "")
    env.config_dir = 'C:\httpie'

    assert env.stdin == ""
    assert env.stdout == ""
    assert env.stderr == ""
    assert env.config_dir == "C:\httpie"

# Generated at 2022-06-13 21:48:56.100694
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        devnull = os.devnull,
        is_windows = True,
        config_dir = Path(os.getcwd()) / "test_config.json",
        stdin = open(os.devnull, 'a'),
        stdin_isatty = False,
        stdin_encoding = "utf8",
        stdout = sys.stdout,
        stdout_isatty = True,
        stdout_encoding = "utf8",
        stderr = sys.stderr,
        stderr_isatty = True,
        colors = 256,
        program_name = "http")
    assert env.config_dir == Path(os.getcwd()) / "test_config.json"


# Generated at 2022-06-13 21:49:01.984171
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment(stdout_encoding='ascii').stdout_encoding == 'ascii'
    assert Environment(stdout_encoding='ascii').stdout_isatty == False
    assert Environment(stdout_encoding='ascii').stdout == sys.stdout



# Generated at 2022-06-13 21:49:13.615573
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == bool(sys.stdin.isatty())
    assert env.stdin_encoding is None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == bool(sys.stdout.isatty())
    assert env.stdout_encoding is None
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == bool(sys.stderr.isatty())
    assert env.colors == 256
    assert env.program_name == 'http'

# Generated at 2022-06-13 21:49:14.644875
# Unit test for constructor of class Environment
def test_Environment():
    Environment()
    assert Environment(devnull=True)

# Generated at 2022-06-13 21:49:33.990378
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=None, stdout=sys.stdout, config_dir=Path('C:\\'), stderr=sys.stderr, stdin=sys.stdin)
    print(env)

test_Environment()

# Generated at 2022-06-13 21:49:41.380226
# Unit test for constructor of class Environment
def test_Environment():
    """
    httpie.core.environment.Environment.__init__
    """
    env = Environment(
        devnull = open(os.devnull,'w+')
    )
    assert(env.is_windows == is_windows)
    assert(env.config_dir == DEFAULT_CONFIG_DIR)
    assert(env.stdin == sys.stdin)
    assert(env.stdin_isatty == (sys.stdin.isatty() if sys.stdin else False))
    assert(env.stdin_encoding is None)
    assert(env.stdout == sys.stdout)
    assert(env.stdout_isatty == sys.stdout.isatty())
    assert(env.stdout_encoding is None)
    #assert(env.stdout == 'utf8')


# Generated at 2022-06-13 21:49:52.860788
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin='in', stdout='out', stderr='err', config_dir='cDirectory', stdin_encoding='inEncoding', stdout_encoding='outEncoding', stderr_encoding='errEncoding', is_windows=True, devnull='devnull')

# Generated at 2022-06-13 21:49:54.949933
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.program_name == 'http'


# Generated at 2022-06-13 21:49:59.910408
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=None)
    assert "devnull=None" in str(env)

env = Environment()
"""
The active execution context.

"""

# Generated at 2022-06-13 21:50:11.486605
# Unit test for constructor of class Environment
def test_Environment():
    import io
    import sys
    import os
    from pathlib import Path
    from typing import IO, Optional

    config_dir = Path(r'C:\Users\Administrator\AppData\Local\httpie')

    # 模拟标准输入流 stdin
    # 默认是 sys.stdin , 也可以自定义
    in_ = sys.stdin if sys.stdin else 'stdin'
    in_isatty = sys.stdin.isatty() if sys.stdin else False
    in_encoding = getattr(in_, 'encoding', None) or 'utf8'

    # 模拟标准输出流 stdout
    # 默认