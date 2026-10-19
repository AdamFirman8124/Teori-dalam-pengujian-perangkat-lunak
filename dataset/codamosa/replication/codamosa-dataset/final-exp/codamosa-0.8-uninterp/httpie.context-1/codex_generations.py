

# Generated at 2022-06-13 21:40:20.968125
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    print(env)
    print(repr(env))

    env = Environment(devnull='/dev/null', colors=16)
    print(repr(env))

# Generated at 2022-06-13 21:40:23.966010
# Unit test for constructor of class Environment
def test_Environment():
    print("TESTING OF ENVIRONMENT CLASS")
    env = Environment(devnull="devnull")
    print("ENVIRONMENT: ", env)

# Generated at 2022-06-13 21:40:25.849312
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert isinstance(env, Environment)
    env = Environment(stdin=sys.stdin)
    print(env)

# Generated at 2022-06-13 21:40:35.144281
# Unit test for constructor of class Environment
def test_Environment():
    import io
    import tempfile
    stdin = io.StringIO('content')
    stdout = io.StringIO()
    stderr = io.StringIO()
    devnull = tempfile.TemporaryFile()
    environment = Environment(stdin=stdin, stdout=stdout, stderr=stderr, devnull=devnull)
    assert environment.stdin == stdin
    assert environment.stdout == stdout
    assert environment.stderr == stderr
    assert environment.devnull == devnull

# To get code coverage for 'Environment' class,
# run 'nosetests -s --with-coverage --cover-erase --cover-package=httpie'
# in tests/ folder.

# Generated at 2022-06-13 21:40:41.269702
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR



# Generated at 2022-06-13 21:40:47.636745
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    config = env.config
    print(config.__dict__)
    if env.is_windows:
        print(env.stdout)
    print(env.stdout_isatty)
    if env.is_windows:
        print(env.stderr)
    print(env.stderr_isatty)

test_Environment()

# Generated at 2022-06-13 21:40:51.646801
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=None, stdout=sys.stdout, stderr=sys.stderr, stdin=sys.stdin)

# Generated at 2022-06-13 21:41:02.037514
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull='/dev/null',
                      is_windows=True,
                      config_dir='/home/user/.config/httpie',
                      stdin='devnull',
                      stdin_isatty=True,
                      stdin_encoding='utf8',
                      stdout='stdout',
                      stdout_isatty=True,
                      stdout_encoding='utf8',
                      stderr='stderr',
                      stderr_isatty=True,
                      colors=256,
                      program_name='http')
    assert env.is_windows == True
    assert env.config_dir == '/home/user/.config/httpie'
    assert env.devnull == 'devnull'
    assert env.stdin == 'devnull'
    assert env.stdin_isatty == True

# Generated at 2022-06-13 21:41:03.981855
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(colors=1024)
    env.config_dir = Path('/tmp')
    print(env)

# Generated at 2022-06-13 21:41:10.436466
# Unit test for constructor of class Environment
def test_Environment():
    '''
    Test the constructor of class Environment.
    '''
    from httpie.config import Config

    env = Environment(config_dir=Config().directory, devnull='hello')
    assert env.devnull == 'hello'
    assert env.config_dir == Config().directory



# Generated at 2022-06-13 21:41:28.322832
# Unit test for constructor of class Environment
def test_Environment():

    env = Environment()

    assert env.is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR

    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.stdin_isatty
    assert env.stdout_isatty
    assert env.stderr_isatty

    assert env.stdin_encoding == 'utf8'
    assert env.stdout_encoding == 'utf8'
    assert env.stderr_encoding == 'utf8'

    assert env.colors == 256

    assert env.program_name == 'http'

# Generated at 2022-06-13 21:41:40.923689
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        colors=256,
        config_dir=DEFAULT_CONFIG_DIR,
        is_windows=False,
        program_name='http',
        stderr=sys.stderr,
        stdin=sys.stdin,
        stdout=sys.stdout,
        colors = 256,
        program_name = 'http'
    )
    env = Environment(
        colors=256,
        config_dir=DEFAULT_CONFIG_DIR,
        is_windows=True,
        program_name='http',
        stderr=sys.stderr,
        stdin=sys.stdin,
        stdout=sys.stdout,
        colors=256,
        program_name='http'
    )
    print(type(env))


# Generated at 2022-06-13 21:41:51.671703
# Unit test for constructor of class Environment
def test_Environment():
    class temp(Environment):
        pass
    e = temp()
    e.stdin = temp.stdin
    assert e.stdin
    assert e.stdin.isatty()
    e.stdout = temp.stdout
    assert e.stdout_isatty
    assert e.stderr_isatty
    e.devnull = temp.devnull
    assert e.devnull
    e = temp(devnull=1)
    e = temp(devnull=1, a=2)
    assert e.a == 2
    assert e.devnull == 1

# Generated at 2022-06-13 21:42:04.920134
# Unit test for constructor of class Environment
def test_Environment():
    environ = Environment(stdin_isatty=True, stdin_encoding='a', stdout_isatty=True, stdout_encoding='b', colors=256, program_name='http',is_windows=True)
    ( actual, expected ) = ( environ.stdin_isatty, True )
    assert actual == expected
    ( actual, expected ) = ( environ.stdin_encoding, 'a' )
    assert actual == expected
    ( actual, expected ) = ( environ.stdout_isatty, True )
    assert actual == expected
    ( actual, expected ) = ( environ.stdout_encoding, 'b' )
    assert actual == expected
    ( actual, expected ) = ( environ.colors, 256 )
    assert actual == expected

# Generated at 2022-06-13 21:42:11.379609
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull='1234567', stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stdout)
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stdout
    assert env.devnull == '1234567'


# Generated at 2022-06-13 21:42:14.156203
# Unit test for constructor of class Environment
def test_Environment():
    import warnings
    warnings.filterwarnings("ignore")
    env = Environment(program_name='httpie')
    print(env)

test_Environment()

# Generated at 2022-06-13 21:42:24.639788
# Unit test for constructor of class Environment
def test_Environment():
    # Instantiate the class using default arguments
    actual = str(Environment())

# Generated at 2022-06-13 21:42:28.620904
# Unit test for constructor of class Environment
def test_Environment():
    passed = True
    try:
        assert isinstance(str(Environment()), str)
        assert isinstance(repr(Environment()), str)
    except AssertionError:
        passed = False
    assert passed

# Generated at 2022-06-13 21:42:32.291824
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=None, **{'__dict__': {'x': 1, 'y': 2}})
    assert env.__dict__ == {'__dict__': {'x': 1, 'y': 2}}
    assert env.x == 1
    assert env.y == 2

# Generated at 2022-06-13 21:42:45.681315
# Unit test for constructor of class Environment
def test_Environment():
    # unit test: test constructor of class Environment
    env = Environment()
    assert env is not None
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


# Generated at 2022-06-13 21:43:01.919034
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    import pathlib
    env = Environment(config_dir=pathlib.Path('./test_config'), stdin=sys.stdin,
    stdout=sys.stdout, stderr=sys.stderr)

# Generated at 2022-06-13 21:43:07.692154
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment()
    assert environment.is_windows == is_windows
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        assert getattr(environment, stream.name) is stream
    assert environment.stdin_isatty is sys.stdin.isatty()
    assert environment.stdin_encoding == 'utf8'
    assert environment.stdout_encoding == 'utf8'
    assert environment.stderr_encoding == 'utf8'
    assert environment.program_name == 'http'

# Generated at 2022-06-13 21:43:17.560750
# Unit test for constructor of class Environment
def test_Environment():
    # test if Environment is defined by the class with correct attributes
    assert isinstance(Environment(),Environment)
    assert hasattr(Environment(),'colors')
    assert hasattr(Environment(),'program_name')
    assert hasattr(Environment(),'_orig_stderr')
    assert hasattr(Environment(),'stdin')
    assert hasattr(Environment(),'stdout')
    assert hasattr(Environment(),'stderr')
    assert hasattr(Environment(),'stdout_encoding')
    assert hasattr(Environment(),'colors')
    assert hasattr(Environment(),'_devnull')
    assert hasattr(Environment(),'_config')
    assert hasattr(Environment(),'stdin_encoding')
    assert hasattr(Environment(),'stdin_isatty')

# Generated at 2022-06-13 21:43:18.500377
# Unit test for constructor of class Environment
def test_Environment():
    Environment()

# Generated at 2022-06-13 21:43:24.937445
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin = sys.stdin, stdout = sys.stdout, stderr = sys.stderr)
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr

# Generated at 2022-06-13 21:43:30.603033
# Unit test for constructor of class Environment
def test_Environment():
    """
    Test Environment
    :return:
    """
    env = Environment()
    assert isinstance(env, Environment)
    test = Environment(is_windows=True)
    assert  isinstance(test, Environment)
    assert test.is_windows is True
    assert env.is_windows is False
    test_config = Environment(config_dir=DEFAULT_CONFIG_DIR)
    assert isinstance(test_config, Environment)
    assert test_config.config_dir == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:43:40.294079
# Unit test for constructor of class Environment
def test_Environment():
    environ = Environment()
    assert isinstance(environ, Environment)
    assert not isinstance(environ, type(Environment))
    assert environ.is_windows == is_windows
    assert environ.config_dir == Path(DEFAULT_CONFIG_DIR)
    assert environ.stdin == sys.stdin
    assert environ.stdin_isatty == sys.stdin.isatty() if sys.stdin is not None else False
    assert environ.stdin_encoding == 'utf8'
    assert environ.stdout == sys.stdout
    assert environ.stdout_isatty == sys.stdout.isatty()
    assert environ.stdout_encoding == 'utf8'
    assert environ.stderr == sys.stderr
    assert environ.stder

# Generated at 2022-06-13 21:43:46.849291
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(is_windows=True, devnull=True, config_dir='.')
    assert isinstance(env, Environment)
    assert env.is_windows == True
    assert env.config_dir == Path('.')
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == True
    assert env.stdin_encoding == None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == True
    assert env.stdout_encoding == None
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == True
    assert env.stderr_encoding == None
    assert env.colors == 256
    assert env.program_name == 'http'

    assert env._config == None

# Generated at 2022-06-13 21:43:49.998794
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment(devnull=1234).devnull == 1234
    assert Environment(stdin=1234).stdin == 1234
    assert str(Environment(stdin=1234)) == 'stdin=1234'

# Generated at 2022-06-13 21:43:55.999967
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    print(env)
    print(env.program_name)
    print(env.config_dir)
    new_env = Environment(program_name='new_http',config_dir='new_dir')
    print(new_env)
    print(new_env.program_name)
    print(new_env.config_dir)
test_Environment()

# Generated at 2022-06-13 21:44:08.756171
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    if sys.stdin is not None:
        assert env.stdin_isatty == sys.stdin.isatty()
        assert env.stdin_encoding == sys.stdin.encoding
    else:
        assert env.stdin_isatty == False
        assert env.stdin_encoding is None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding == sys.stdout.encoding
    assert env.stderr == sys.stderr
    assert env.stderr_is

# Generated at 2022-06-13 21:44:09.417607
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()

# Generated at 2022-06-13 21:44:12.124191
# Unit test for constructor of class Environment
def test_Environment():
    base = Environment()
    base.config_dir = 'data/config'
    print(base.config)
    assert 'data/config' in base.config_dir



# Generated at 2022-06-13 21:44:20.632322
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    if is_windows:
        assert env.stderr_isatty
        assert env.stdout_isatty
    else:
        assert env.is_windows is False
    assert env.stdin_isatty
    assert env.stderr == sys.stderr
    assert env.stdout == sys.stdout
    assert env.stdin == sys.stdin
    assert env.config_dir == Path(__file__).parent
    assert env.program_name == 'http'
    assert env.colors == 256

# Generated at 2022-06-13 21:44:34.271096
# Unit test for constructor of class Environment
def test_Environment():
    # test initializing the environment
    env = Environment()
    assert type(env).is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdin_encoding == getattr(sys.stdin, 'encoding', 'utf8')
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding == getattr(sys.stdout, 'encoding', 'utf8')
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty

# Generated at 2022-06-13 21:44:39.254674
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    with open(os.devnull, 'r+') as devnull:
        env_with_devnull_stream = Environment(devnull=devnull)

if __name__ == "__main__":
    test_Environment()

# Generated at 2022-06-13 21:44:51.528726
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        is_windows=True,
        config_dir=Path("/dev/null"),
        stdin=sys.stdin,
        stdin_encoding="utf8",
        stdin_isatty=False,
        stdout=sys.stdout,
        stdout_encoding="utf8",
        stdout_isatty=True,
        stderr=sys.stderr,
        stderr_isatty=True,
        colors=256,
        program_name="http",
    )
    assert env.color_support

    assert env.program_name == "http"
    assert env.is_windows
    assert not env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin

# Generated at 2022-06-13 21:44:54.548365
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    env.stdout.write("test is ok\n")
    env = Environment(stdout=env.devnull, print = "print")
    env.stdout.write("test is not ok")

# Generated at 2022-06-13 21:44:55.537304
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment()


# Generated at 2022-06-13 21:45:02.507917
# Unit test for constructor of class Environment
def test_Environment():
    defaultEnv = Environment()
    assert defaultEnv.is_windows == is_windows
    assert defaultEnv.config_dir == Path(DEFAULT_CONFIG_DIR)
    assert defaultEnv.stdout == sys.stdout
    assert defaultEnv.stdout_isatty == sys.stdout.isatty()
    assert defaultEnv.stderr == sys.stderr
    assert defaultEnv.stderr_isatty == sys.stderr.isatty()
    assert defaultEnv.program_name == 'http'

# Generated at 2022-06-13 21:45:11.772748
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull='123')
    env.log_error('123')
    env.config.update()
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.is_windows == is_windows
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.colors == 256
    assert env.program_name == 'http'
    assert env._orig_stderr == sys.stderr

# Generated at 2022-06-13 21:45:20.425040
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()

    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.colors == 256

    if not is_windows:
        if curses:
            assert env.colors == curses.tigetnum('colors')

    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr_isatty == sys.stderr.isatty()


# Generated at 2022-06-13 21:45:30.203559
# Unit test for constructor of class Environment
def test_Environment():
    env=Environment(devnull=None, is_windows=True, config_dir='./config/')
    env.config_dir = 'httpie'
    assert env.config_dir == 'httpie'
    env.stdin = sys.stdin  # `None` when closed fd (#791)
    env.stdin_isatty = env.stdin.isatty() if env.stdin else False
    env.stdin_encoding = None
    env.stdout = sys.stdout
    env.stdout_isatty = env.stdout.isatty()
    env.stdout_encoding = None
    env.stderr = sys.stderr
    env.stderr_isatty = env.stderr.isatty()

# Generated at 2022-06-13 21:45:39.310011
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdin_encoding == sys.stdin.encoding or 'utf8'
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding == sys.stdout.encoding or 'utf8'
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.program_name == 'http'

# Generated at 2022-06-13 21:45:42.551555
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert isinstance(env,Environment)
    assert env.is_windows == is_windows
    assert env._config == None

# Generated at 2022-06-13 21:45:48.622479
# Unit test for constructor of class Environment
def test_Environment():
    assert isinstance(Environment().config, Config)

    assert Environment(devnull='/dev/null').devnull == '/dev/null'
    assert Environment().devnull == open(os.devnull, 'w+')

    Environment(devnull=None)
    assert Environment().devnull is None

    Environment().log_error('error')
    Environment().log_error('warning')

# Generated at 2022-06-13 21:45:53.602910
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment() is not Environment()
    assert Environment() is not Environment(config_dir='test')

# Generated at 2022-06-13 21:46:07.149667
# Unit test for constructor of class Environment
def test_Environment():
    envir = Environment(is_windows=False, config_dir=DEFAULT_CONFIG_DIR, stdin=sys.stdin,
                        stdin_isatty=sys.stdin.isatty(), stdin_encoding = None, stdout=sys.stdout,
                        stdout_isatty=sys.stdout.isatty(), stdout_encoding=None, stderr=sys.stderr,
                        stderr_isatty=sys.stderr.isatty(), colors=256, program_name='http')

    # If a class has _config and devnull attribute, the methods related to them should be in Environment class
    assert hasattr(envir, '_config')
    assert hasattr(envir, 'devnull')

    # If a class has _config and devnull attribute, the method get

# Generated at 2022-06-13 21:46:11.634421
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert isinstance(env.devnull, type(sys.stderr))

    env = Environment(devnull=None)
    assert env.devnull is None

    env = Environment(stdin=None)
    assert env.stdin is None
    assert env.stdin_isatty is False
    assert env.stdin_encoding == 'utf8'

    env = Environment(stdout=None)
    assert env.stdout is None
    assert env.stdout_isatty is False
    assert env.stdout_encoding == 'utf8'

# Generated at 2022-06-13 21:46:19.137260
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        stdin=sys.stdin,
        stdout=sys.stdout,
        stderr=sys.stderr,
        is_windows=False,
        config_dir='',
    )
    assert sys.stdin == env.stdin
    assert sys.stdout == env.stdout
    assert sys.stderr == env.stderr
    assert is_windows == env.is_windows
    assert '' == env.config_dir

# Generated at 2022-06-13 21:46:26.966156
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=1)
    assert env.devnull == 1
    assert env.stderr_isatty

test_Environment()

# Generated at 2022-06-13 21:46:33.979409
# Unit test for constructor of class Environment

# Generated at 2022-06-13 21:46:38.240115
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment()
    e.program_name = 'http'
    if e.is_windows:
        e.stdout = e.stdout
        e.stderr = e.stderr
    assert e.program_name == 'http'
    e.stdout = e.stdout
   

# Generated at 2022-06-13 21:46:50.352915
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin is sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdin_encoding == sys.stdin.encoding
    assert env.stdout is sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding == sys.stdout.encoding
    assert env.stderr is sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.program_name == 'http'

# Generated at 2022-06-13 21:46:59.647016
# Unit test for constructor of class Environment
def test_Environment():
    import io
    import pathlib
    env = Environment(
        is_windows=False,
        config_dir=pathlib.Path('.'),
        stdin=io.BytesIO(),
        stdin_isatty=False,
        stdin_encoding='utf8',
        stdout=io.BytesIO(),
        stdout_isatty=False,
        stdout_encoding='utf8',
        stderr=io.BytesIO(),
        stderr_isatty=False
    )

    assert env.is_windows is False
    assert str(env.config_dir) == '.'
    assert isinstance(env.stdin, io.BytesIO)
    assert env.stdin_isatty is False
    assert env.stdin_encoding == 'utf8'

# Generated at 2022-06-13 21:47:13.816800
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(foo=1)
    assert env.foo == 1
    #incorrect keyword argument
    try:
        env = Environment(meow=None)
        raise AssertionError('There should have been an error here')
    except AssertionError:
        pass
    #incorrect keyword argument
    try:
        env = Environment(program_name='httpie', meow=None)
        raise AssertionError('There should have been an error here')
    except AssertionError:
        pass
    #correct keyword arguments
    env = Environment(is_windows=True, program_name='httpie')
    assert env.program_name == 'httpie'
    assert env.is_windows == True

# Generated at 2022-06-13 21:47:26.382044
# Unit test for constructor of class Environment
def test_Environment():
    import io
    import sys
    print(sys.stdin.encoding)
    stdin1 = type('stdin', (io.BytesIO,), {})()
    stdout1 = type('stdout', (io.BytesIO,), {})()
    default_env = Environment()

    print(default_env)
    print(default_env.stdin_encoding)
    assert default_env.stdin_encoding == 'utf8'
    print(default_env.stdout_encoding)
    assert default_env.stdout_encoding == 'utf8'

    print(default_env)
    env = Environment(stdin=stdin1, stdout=stdout1)
    print(env)
    # print(env.stdin.encoding)
    assert env.stdin_encoding == None


# Generated at 2022-06-13 21:47:28.731908
# Unit test for constructor of class Environment
def test_Environment():
    env_class=Environment
    print(env_class.__dict__.items())
    envinstance=Environment()
    print(envinstance.__dict__.items())

# Generated at 2022-06-13 21:47:38.296760
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.program_name == 'http'
    assert env.colors == 256
    assert not env.stdin_encoding
    assert not env.stdout_encoding
    assert not env._devnull
    assert env == Environment()

# Generated at 2022-06-13 21:47:45.228429
# Unit test for constructor of class Environment
def test_Environment():
    print("test_Environment()")
    env = Environment(is_windows=False,config_dir=DEFAULT_CONFIG_DIR)
    print(env)

if __name__ == "__main__":
    print("httpie.env")
    #test_Environment()

# Generated at 2022-06-13 21:48:06.322131
# Unit test for constructor of class Environment
def test_Environment():
    import io
    import json
    import unittest
    from httpie.utils import Environment

    stdin = io.StringIO()
    stdin.write('{"a": 1, "b": 2, "c": 3}')
    stdin.seek(0)
    stdin_isatty = stdin.isatty()
    stdin_encoding = getattr(stdin, 'encoding', None)

    stdout = io.StringIO()
    stdout_isatty = stdout.isatty()
    stdout_encoding = getattr(stdout, 'encoding', None)

    stderr = io.StringIO()
    stderr_isatty = stderr.isatty()

    devnull = io.StringIO()

# Generated at 2022-06-13 21:48:14.504318
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.colors == 256
    assert env.program_name == "http"

# Generated at 2022-06-13 21:48:22.243383
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(is_windows=True, stdin_encoding=None, stdout_encoding='GBK', stderr_encoding='GBK')
    assert env.is_windows == True
    assert env.stdin_encoding == None
    assert env.stdout_encoding == 'GBK'
    assert env.stderr_encoding == 'GBK'
    assert env.config.isinstance(Config)
    assert env.devnull == None

# Generated at 2022-06-13 21:48:34.490991
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.config_dir == DEFAULT_CONFIG_DIR

    # overwrite the default value of stdout
    env = Environment(stdout = sys.stderr)
    assert env.stdout == sys.stderr

    # use config_dir value
    env = Environment(config_dir='~')
    assert env.config_dir == Path('~')

    # Overwrite the default value of config_dir
    env = Environment(config_dir = Path('~/.config/hi'))
    assert env.config_dir == Path('~/.config/hi')

    # Default value of devnull = None
    env = Environment(devnull = None)
    assert env.devnull == None

    # overwrite the default value of devnull
    env = Environment(devnull = sys.stderr)
    assert env

# Generated at 2022-06-13 21:48:40.467366
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment(devnull = 'hi')
    assert environment.devnull == 'hi'
    environment = Environment()
    assert environment.config.is_new() == False
    assert environment.stdin == sys.stdin
    assert environment.stderr == sys.stderr
    assert environment.stdout == sys.stdout
    assert environment.config.directory == DEFAULT_CONFIG_DIR
    assert environment.devnull == None


# Generated at 2022-06-13 21:48:54.645429
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    if env.is_windows:
        assert (env.stdout_encoding == 'utf-8')
        assert (env.stdout_isatty == True)
        assert (env.stderr_isatty == False)
        assert (env.stderr_encoding == 'utf-8')
    else:
        assert (env.stdout_encoding == 'utf-8')
        assert (env.stdout_isatty == True)
        assert (env.stderr_isatty == True)
        assert (env.stderr_encoding == 'utf-8')


# Generated at 2022-06-13 21:49:06.696850
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    import os
    import tempfile
    config_directory = tempfile.mkdtemp()
    os.chdir(config_directory)
    env = Environment(config_dir = config_directory, program_name = 'http')
    #test is_windows
    assert(env.is_windows == is_windows)
    #test config_dir
    assert(env.config_dir == config_directory)
    #test program_name
    assert(env.program_name == 'http')
    #test stdin, stdout, stderr
    assert(env.stdin == sys.stdin)
    assert(env.stdout == sys.stdout)
    assert(env.stderr == sys.stderr)
    #test stdin_isatty, stdout_isatty, stderr_is

# Generated at 2022-06-13 21:49:15.366041
# Unit test for constructor of class Environment
def test_Environment():
    default_env_config_dir = DEFAULT_CONFIG_DIR
    default_env_is_windows = is_windows
    default_env_stdin = sys.stdin
    default_env_stdin_isatty = sys.stdin.isatty()
    default_env_stdin_encoding = getattr(sys.stdin, 'encoding', None) or 'utf8'
    default_env_stdout = sys.stdout
    default_env_stdout_isatty = sys.stdout.isatty()
    default_env_stdout_encoding = getattr(sys.stdout, 'encoding', None) or 'utf8'
    default_env_stderr = sys.stderr
    default_env_stderr_isatty = sys.stderr.isatty

# Generated at 2022-06-13 21:49:20.579050
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert isinstance(env.config_dir, Path)
    assert env.stdin is not None
    assert env.stdout is not None
    assert env.stderr is not None


# Generated at 2022-06-13 21:49:25.403197
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert is_windows == env.is_windows
    assert DEFAULT_CONFIG_DIR == env.config_dir
    assert sys.stdin == env.stdin
    assert sys.stdout == env.stdout
    assert sys.stderr == env.stderr


# Generated at 2022-06-13 21:50:04.317837
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        is_windows=True,
        stdin=None,
        stdin_isatty=True,
        stdin_encoding="utf8",
        stdout=None,
        stdout_isatty=True,
        stdout_encoding="utf8",
        stderr=None,
        stderr_isatty=True,
        colors=256,
        program_name="http",
        config_dir=None,
        devnull="test"
    )
    print(env.config)
    print(env._devnull)
    assert env.is_windows == True
    assert env.stdin == None
    assert env.stdin_isatty == True
    assert env.stdin_encoding == "utf8"
    assert env.stdout == None

# Generated at 2022-06-13 21:50:14.402650
# Unit test for constructor of class Environment
def test_Environment():
    from io import StringIO
    from tempfile import TemporaryDirectory
    from httpie.clients import JSONClient
    from httpie.config import BaseConfig

    args = ['--json']
    env = Environment()
    assert env.program_name == 'http'
    assert env.stderr_isatty == True
    assert env.stdin.isatty()
    assert env.stdin.readable()

    # Change directory
    env.config_dir = Path('/')
    assert env.config_dir == Path('/')
    assert env.stdin.isatty()

    # Change standard in
    env.stdin = StringIO("Testing")
    assert env.stdin.read() == "Testing"

    # Change standard out
    env.stdout = StringIO("Testing")
    assert env.stdout.getvalue