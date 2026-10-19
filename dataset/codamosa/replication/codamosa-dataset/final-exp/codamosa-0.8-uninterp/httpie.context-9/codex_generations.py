

# Generated at 2022-06-13 21:40:27.725022
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull='', stdin='', stdout='', stderr='')
    assert env.devnull == ''
    assert env.stdin == ''
    assert env.stdout == ''
    assert env.stderr == ''
    assert env.colors == 0
    assert not env.is_windows
    assert env.program_name == 'http'

    if is_windows:
        # noinspection PyUnresolvedReferences
        import colorama.initialise
        env = Environment(stdout=colorama.initialise._Wrapper(None))
        assert env.stdout == ''


# Generated at 2022-06-13 21:40:30.950654
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=2, config_dir=3)
    assert isinstance(env, Environment)
    assert env.devnull == 2
    assert env.config_dir == 3

# Generated at 2022-06-13 21:40:36.383078
# Unit test for constructor of class Environment
def test_Environment():
    cwd = os.getcwd()
    e = Environment(config_dir=cwd, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
    assert isinstance(e, Environment)
    assert e.config_dir == cwd
    assert e.stdin == sys.stdin
    assert e.stdout == sys.stdout
    assert e.stderr == sys.stderr

# Generated at 2022-06-13 21:40:39.689762
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout = sys.stdout)
    assert(env.stdout == sys.stdout)

# Generated at 2022-06-13 21:40:48.469198
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(is_windows=True,
                      config_dir='/home/unittest/httpie',
                      stdin = None,
                      stdin_isatty=True,
                      stdin_encoding=None,
                      stdout=sys.stdout,
                      stdout_isatty=True,
                      stdout_encoding=None,
                      stderr=sys.stderr,
                      stderr_isatty=True,
                      colors=256,
                      program_name='http')

    print(env)
    print(env._orig_stderr)


# Generated at 2022-06-13 21:40:59.984486
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name='httpie',config_dir='/home/junru')
    assert str(env) == "{'config': <httpie.config.Config {}>, 'config_dir': '/home/junru', 'colors': 256, 'is_windows': False, 'program_name': 'http', 'stderr': <httpie.output.streams.StdErrStdOut object>, 'stderr_encoding': None, 'stderr_isatty': True, 'stdin': <httpie.output.streams.StdIn object>, 'stdin_encoding': None, 'stdin_isatty': False, 'stdout': <httpie.output.streams.StdErrStdOut object>, 'stdout_encoding': None, 'stdout_isatty': True}"
   

# Generated at 2022-06-13 21:41:02.076827
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    print(env.__dict__)

# Run the unit test
test_Environment()

# Generated at 2022-06-13 21:41:11.407826
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.program_name == 'http'

ENV = Environment()

# Generated at 2022-06-13 21:41:24.685834
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    print(env)
    # Get httpie config file path
    print(env.config_dir)
    # Read config file
    print(env.config)
    # Change config file name
    env.config_dir = os.path.join(env.config_dir, "test")
    print(env.config_dir)
    # Read config file
    print(env.config)
    # Change stdout to /dev/null
    env.stdout = open(os.devnull, 'w')
    print(env.stdout)
    # Add log_error function
    env.log_error("Test log method")
    print(env)

if __name__ == "__main__":
    test_Environment()

# Generated at 2022-06-13 21:41:35.576712
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        is_windows=True,
        config_dir=Path('/home/user/.config/httpie'),
        stdin=sys.stdin,
        stdin_isatty=True,
        stdin_encoding=None,
        stdout=sys.stdout,
        stdout_isatty=True,
        stdout_encoding=None,
        stderr=sys.stderr,
        stderr_isatty=True,
        colors=256,
        program_name='http',
        _devnull=None,
        _config=None
    )
    env.devnull = open(os.devnull, 'w+')
    assert env._orig_stderr == env.stderr
    assert env._devnull is not None

# Generated at 2022-06-13 21:41:52.531961
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert type(env.stdin_isatty) == bool
    assert type(env.stdout_isatty) == bool
    assert type(env.stderr_isatty) == bool
    assert type(env.stdin_encoding) == str
    assert type(env.stdout_encoding) == str
    assert type(env.stderr_encoding) == str
    assert type(env.colors) == int

# Generated at 2022-06-13 21:42:02.822556
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()

    test_val = "string"
    env = Environment(program_name=test_val)
    assert env.program_name == test_val


# Generated at 2022-06-13 21:42:13.367189
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment()
    assert Environment(is_windows=False)
    assert Environment(config_dir='.')
    assert Environment(stdin=open('/dev/null', 'r'))
    assert Environment(stdout=open('/dev/null', 'w+'))
    assert Environment(stderr=open('/dev/null', 'w+'))

    e = Environment(stdin_encoding='ascii')
    assert 'stdin_encoding' in str(e)

    e = Environment(stdout_encoding='utf8')
    assert 'stdout_encoding' in str(e)
    assert 'stdout_encoding' not in repr(e)

    assert Environment(program_name='httpie')

# Generated at 2022-06-13 21:42:19.782320
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    print(env)
    print(env.config)
    env.log_error('hello, world')
    env.devnull = 'hello'
    assert env.devnull == 'hello'
    assert not env.is_windows
    env2 = Environment(is_windows=True)
    assert env2.is_windows

# Generated at 2022-06-13 21:42:26.398369
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment()
    assert environment.config_dir == DEFAULT_CONFIG_DIR
    assert environment.stdin == sys.stdin
    assert environment.stdout == sys.stdout
    assert environment.stderr == sys.stderr
    assert environment.colors == 256
    assert environment.program_name == 'http'

# Generated at 2022-06-13 21:42:34.625528
# Unit test for constructor of class Environment
def test_Environment():
    # Unit test for constructor of class Environment
    env = Environment(devnull='/dev/null')
    assert env.devnull == '/dev/null'
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.program_name == 'http'



# Generated at 2022-06-13 21:42:48.723637
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == True
    assert str(env.config_dir) == '~/httpie'
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
    assert env.config == Config(directory=env.config_dir)


# Generated at 2022-06-13 21:42:50.444282
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(test = True)
    assert env.test == True

test_Environment()

# Generated at 2022-06-13 21:43:02.000639
# Unit test for constructor of class Environment
def test_Environment():
    import os
    from pathlib import Path
    from httpie.compat import is_windows
    from httpie.config import DEFAULT_CONFIG_DIR, Config, ConfigFileError
    from httpie.utils import repr_dict
    
    
    try:
        import curses
    except ImportError:
        curses = None # Compiled w/o curses
    import sys

    _orig_stdin = sys.stdin
    _orig_stdout = sys.stdout
    _orig_stderr = sys.stderr
    class Environment():
        is_windows: bool = is_windows
        config_dir: Path = DEFAULT_CONFIG_DIR
        stdin: Optional[IO] = sys.stdin  # `None` when closed fd (#791)
        stdin_encoding: Optional[str] = None


# Generated at 2022-06-13 21:43:04.269940
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout=None, stderr=None)
    assert env.stdout_isatty == False

#test_Environment()

# Generated at 2022-06-13 21:43:33.185222
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout=open("stdout.txt", "w+"),stderr=open("stderr.txt", "w+"),stdin = open("stdin.txt", "r+"), colors=100, program_name="http", devnull=open("devnull.txt", "w+"))
    env.config_dir = "D:\PycharmProjects\httpie"
    assert env.config_dir == "D:\PycharmProjects\httpie"

# Generated at 2022-06-13 21:43:34.751305
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment().program_name == 'http'


# Generated at 2022-06-13 21:43:38.696930
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert(env.is_windows)
    assert(env.stdin)
    assert(env.stdout)
    assert(env.stderr)
    if(env.is_windows):
        assert(env.colors == 0)
    else:
        assert(env.colors == 256)

# Generated at 2022-06-13 21:43:48.794248
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(is_windows=False,
                      config_dir='/Users/yuyu/.config/httpie',
                      stdin=None,
                      stdin_isatty=False,
                      stdin_encoding='utf8',
                      stdout=sys.stdout,
                      stdout_isatty=True,
                      stdout_encoding='utf8',
                      stderr=sys.stderr,
                      stderr_isatty=True,
                      colors=256,
                      program_name='http',
                      devnull=None)
    assert env.is_windows == False
    assert str(env.config_dir) == '/Users/yuyu/.config/httpie'
    assert env.stdin is None
    assert env.stdin_isatty == False
    assert env.stdin_

# Generated at 2022-06-13 21:43:53.487904
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout='<stdout>', stderr='<stderr>')
    assert env.stdout == '<stdout>'
    assert env.stderr == '<stderr>'

# Generated at 2022-06-13 21:43:57.720131
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name="test")
    assert env.program_name == "test"
    env2 = Environment(program_name="test2", config_dir="test")
    assert env2.program_name == "test2"
    assert env2.config_dir == "test"

# Generated at 2022-06-13 21:43:59.272046
# Unit test for constructor of class Environment
def test_Environment():
    assert isinstance(Environment(), Environment)


# Generated at 2022-06-13 21:44:08.532623
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment(
        config_dir = 'config_dir',
        devnull = 'devnull',
        is_windows = True,
        program_name = 'program_name',
        stderr = 'stderr',
        stderr_isatty = True,
        stdin = 'stdin',
        stdin_isatty = True,
        stdout = 'stdout',
        stdout_isatty = True
    )

    assert environment.config_dir == 'config_dir'
    assert environment.devnull == 'devnull'
    assert environment.is_windows == True
    assert environment.program_name == 'program_name'
    assert environment.stderr == 'stderr'
    assert environment.stderr_isatty == True
    assert environment.stdin == 'stdin'

# Generated at 2022-06-13 21:44:19.001350
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.colors == 256
    assert env.program_name == 'http'

    if not is_windows:
        if curses:
            try:
                curses.setupterm()
                colors = curses.tigetnum('colors')
                assert env.colors == colors
            except curses.error:
                pass
    else:
        import colorama.initialise
        assert env.stdout.convert == colorama.initialise.Convert
        assert env.stdout.strip == colorama.initialise.Strip


# Generated at 2022-06-13 21:44:33.749248
# Unit test for constructor of class Environment
def test_Environment():
    # Check if it is in a set of accepted values
    assert is_windows in (True, False)

    # Check if all keywords are in the class attributes
    keys = ['is_windows', 'config_dir', 'stdin', 'stdin_isatty', 'stdin_encoding', 'stdout', 'stdout_isatty', 'stdout_encoding', 'stderr', 'stderr_isatty', 'colors', 'program_name']
    assert keys == list(Environment.__dict__.keys())

    # Check if the type of all class attributes are correct
    assert isinstance(Environment().is_windows, bool)
    assert isinstance(Environment().config_dir, Path)
    assert isinstance(Environment().stdin, IO)
    assert isinstance(Environment().stdin_isatty, bool)
   

# Generated at 2022-06-13 21:45:18.274121
# Unit test for constructor of class Environment
def test_Environment():
    # Create a new Environment instance
    newEnv = Environment()

    # Check whether env is an instance of class Environment
    assert isinstance(newEnv, Environment)

    # Check whether env is an instance of class object
    assert isinstance(newEnv, object)

    # Check whether env is not None
    assert newEnv is not None

# Generated at 2022-06-13 21:45:20.025943
# Unit test for constructor of class Environment
def test_Environment():
    env=Environment()
    print(env)

# Generated at 2022-06-13 21:45:27.005201
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin_isatty=True,
                      stdout_isatty=True,
                      stderr_isatty=True,
                      config_dir=True,
                      stdin_encoding=True,
                      stdout_encoding=True)
    assert env.stdin_isatty == True
    assert env.stdout_isatty == True
    assert env.stderr_isatty == True
    assert env.config_dir == True
    assert env.stdin_encoding == True
    assert env.stdout_encoding == True

# Generated at 2022-06-13 21:45:37.675035
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()

    assert env.is_windows == is_windows
    assert env.config_dir == Path(DEFAULT_CONFIG_DIR)
    assert env.stdin == sys.stdin  # `None` when closed fd (#791)
    assert env.stdin_isatty == env.stdin.isatty() if env.stdin else False
    assert env.stdin_encoding == None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == env.stdout.isatty()
    assert env.stdout_encoding == None
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == env.stderr.isatty()
    assert env.colors == 256
    assert env.program_

# Generated at 2022-06-13 21:45:51.355485
# Unit test for constructor of class Environment
def test_Environment():
    # Prepare
    config_dir = '/a/b/c/d'

    # Execute
    environment = Environment(config_dir=config_dir)

    # Verify

# Generated at 2022-06-13 21:46:06.000684
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment()
    assert environment.is_windows == is_windows
    assert environment.config_dir == DEFAULT_CONFIG_DIR
    assert environment.stdin == sys.stdin
    assert environment.stdin_isatty == (sys.stdin.isatty() if sys.stdin else False)
    assert environment.stdin_encoding == getattr(
        sys.stdin, 'encoding', None) or 'utf8'
    assert environment.stdout == sys.stdout
    assert environment.stdout_isatty == sys.stdout.isatty()
    assert environment.stdout_encoding == getattr(
        sys.stdout, 'encoding', None) or 'utf8'
    assert environment.stderr == sys.stderr

# Generated at 2022-06-13 21:46:11.887203
# Unit test for constructor of class Environment
def test_Environment():
    try:
        sys.stdin.close()
    except:
        pass
    env = Environment(stdin=None, stdout=None, stderr=None)
    assert env.stdin is None
    assert env.stdout is None
    assert env.stderr is None
    env = Environment(stdin=1)
    assert env.stdin == 1
    env = Environment(stdout=2)
    assert env.stdout == 2
    env = Environment(stderr=3)
    assert env.stderr == 3
    env = Environment(devnull='devnull')
    assert env.devnull == 'devnull'
    try:
        sys.stdin.close()
    except:
        pass



# Generated at 2022-06-13 21:46:16.949443
# Unit test for constructor of class Environment
def test_Environment():
    env_windows = Environment(stdin_isatty=True, stdout_isatty=True, stderr_isatty=True)
    assert env_windows.is_windows == True
    assert env_windows.config_dir == Path(DEFAULT_CONFIG_DIR)
    assert env_windows.stdin_isatty == True
    assert env_windows.stdout_isatty == True
    assert env_windows.stderr_isatty == True
    assert env_windows.stdin_encoding == None
    assert env_windows.stdout_encoding == None
    assert env_windows.stderr_encoding == None
    assert env_windows.colors == 256
    assert env_windows.program_name == 'http'


# Generated at 2022-06-13 21:46:28.506012
# Unit test for constructor of class Environment
def test_Environment():
    # Unit test for constructor of class Environment
    env = Environment()
    assert env.__dict__.get("_config") is None
    assert env.__dict__.get("_devnull") is None
    assert env.__dict__.get("_orig_stderr") is None

    assert env.is_windows == env.program_name == "http"
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty() if sys.stdin else False
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding == sys.stdout.encoding
    assert env.stderr == sys.stderr
    assert env

# Generated at 2022-06-13 21:46:35.566169
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull='notNone')
    assert env._devnull == 'notNone'

    env = Environment(devnull='notNone', config_dir="./")
    assert env.config_dir == "./"

    assert Environment().config.directory == DEFAULT_CONFIG_DIR
    env = Environment(config_dir="./")
    assert env.config.directory == "./"

    env = Environment(config_dir="test_data/dir/")
    assert env.config.directory == "test_data/dir/"

# Generated at 2022-06-13 21:48:00.438734
# Unit test for constructor of class Environment
def test_Environment():
    from io import StringIO
    env = Environment(
        stdin=StringIO('{a: 1}'),
        stdin_encoding='utf8',
        stdin_isatty=True,
        stdout=StringIO(),
        stdout_encoding='utf8',
        stdout_isatty=True,
        stderr=StringIO(),
        stderr_isatty=True,
        config_dir='~/.config',
        program_name='http'
    )
    assert env.stdin_isatty == True
    assert env.stdout_isatty == True
    assert env.stderr_isatty == True
    assert env.stdin_encoding == 'utf8'
    assert env.stdout_encoding == 'utf8'
    assert env.stderr_

# Generated at 2022-06-13 21:48:09.367916
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    if env.stdin:
        assert type(env.stdin) == io.TextIOWrapper
        assert type(env.stdin.buffer) == io.FileIO
    assert type(env.stdout) == io.TextIOWrapper
    assert type(env.stdout.buffer) == io.FileIO
    assert type(env.stderr) == io.TextIOWrapper
    assert type(env.stderr.buffer) == io.FileIO

# Generated at 2022-06-13 21:48:12.916420
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(colors=None, stdout_isatty=True)
    assert env.colors is None
    assert env.stdout_isatty is True
    pass

# Generated at 2022-06-13 21:48:25.706442
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdin_isatty == sys.stdin.isatty()

    if is_windows:
        import colorama.initialise

        # noinspection PyUnresolvedReferences
        wrapped_stdout = colorama.initialise.wrap_stream(sys.stdout, convert=None, strip=None, autoreset=True, wrap=True)
        assert env.stdout == wrapped_stdout
        assert env.stderr == wrapped_stdout

# Generated at 2022-06-13 21:48:35.931466
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=open('/dev/null', 'w+'),
                      config_dir='/tmp/',
                      is_windows=True,
                      stdin=open('/dev/stdin', 'rb'),
                      stdin_isatty=True,
                      stdin_encoding='utf8',
                      stdout=open('/dev/stdout', 'wb'),
                      stdout_isatty=True,
                      stdout_encoding='utf8',
                      stderr=open('/dev/stderr', 'wb'),
                      stderr_isatty=True,
                      colors=256,
                      program_name='http')
    print(env)
    print(env.__dict__)
    # Open standard stream
    _orig_stderr = env._orig_stderr
    _dev

# Generated at 2022-06-13 21:48:40.175924
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(is_windows=False ,stdin='stdin', stdout='stdout',stderr='stderr')
    assert env.stdin == 'stdin'
    assert env.stdout == 'stdout'
    assert env.stderr == 'stderr'



# Generated at 2022-06-13 21:48:47.755335
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout_encoding='utf8')
    print(str(env))
    self.assertIsNotNone(env.stdout)

if __name__ == '__main__':
    import unittest
    unittest.main()

# Generated at 2022-06-13 21:48:50.192374
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    print(env)



# Generated at 2022-06-13 21:49:00.047598
# Unit test for constructor of class Environment
def test_Environment():
    """
    In this test, we test the constructor of class Environment.
    """
    # test with all defaults  
    env = Environment()
    assert env.is_windows == is_windows
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.program_name == 'http'
    
    # test with is_windows, stdin, stdout, stderr, devnull all set to None

# Generated at 2022-06-13 21:49:01.983881
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    print(env)

test_Environment()