

# Generated at 2022-06-13 21:40:28.798320
# Unit test for constructor of class Environment
def test_Environment():
    # Test 1, empty inputs
    stdin = sys.stdin
    stdout = sys.stdout
    stderr = sys.stderr
    colors = 256
    if curses:
        try:
            curses.setupterm()
            colors = curses.tigetnum('colors')
        except curses.error:
            pass
    env1 = Environment()
    assert env1.stdin == stdin
    assert env1.stdout == stdout
    assert env1.stderr == stderr
    assert env1.colors == colors
    # Test 2, overwrite some of the attributes
    stdin = 'sys.stdin'
    stdout = 'sys.stdout'
    stderr = 'sys.stderr'
    colors = 'curses'

# Generated at 2022-06-13 21:40:32.688334
# Unit test for constructor of class Environment
def test_Environment():
    os.environ['HTTPIE_CONFIG_DIR'] = '/home/httpie/config'
    env = Environment()
    assert env.config_dir == '/home/httpie/config'
    os.environ.clear()

# Generated at 2022-06-13 21:40:36.260232
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    env = Environment(program_name = "http", stdout = sys.stdout, stderr = sys.stderr)
    assert env.program_name == 'http'
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr

# Generated at 2022-06-13 21:40:48.759456
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(k1='v1', k2='v2')
    assert env.is_windows == False, "is_windows is not False"
    assert env.config_dir.name == "config", "config_dir is not 'config'"
    assert env.stdin is None, "stdin is not None"
    assert env.stdin_isatty == False, "stdin_isatty is not False"
    assert env.stdin_encoding == None, "stdin_encoding is not None"
    assert env.stdout is not None, "stdout is None"
    assert env.stdout_isatty == False, "stdout_isatty is not False"
    assert env.stdout_encoding == "utf8", "stdout_encoding is not 'utf8'"
    assert env.st

# Generated at 2022-06-13 21:40:59.152652
# Unit test for constructor of class Environment
def test_Environment():
    if is_windows:
        # noinspection PyUnresolvedReferences
        del colorama
    env = Environment(stdin=None, stdout=sys.stdout, stderr=sys.stderr)
    assert env.stdin is None
    assert env.stdout is sys.stdout
    assert env.stderr is sys.stderr
    assert env.stdout_encoding == sys.stdout.encoding
    assert env.is_windows == is_windows
    assert env.program_name == 'http'
    assert env.stdin_isatty == False
    assert env.stdout_isatty == True
    assert env.stderr_isatty == True

# Generated at 2022-06-13 21:41:05.974121
# Unit test for constructor of class Environment
def test_Environment():
    # Unit test case for test constructor of class Environment
    # Scenario 1: All value are set to default.
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == env.stdin.isatty()
    assert env.stdin_encoding is None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == env.stdout.isatty()
    assert env.stdout_encoding is None
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == env.stderr.isatty()
    assert env.colors == 256
    assert env

# Generated at 2022-06-13 21:41:06.977519
# Unit test for constructor of class Environment
def test_Environment():
    assert (Environment(is_windows=False)
            == Environment(is_windows=False))


# Generated at 2022-06-13 21:41:15.782416
# Unit test for constructor of class Environment
def test_Environment():
    import platform
    env = Environment(
        program_name='http',
        colors=256,
        config_dir='/Users/apple/httpie',
        stderr_isatty=True,
        stdout_encoding=platform.system(),
        stderr='output',
        stdout_isatty=True,
        devnull=None,
        colors=256,
        stdin_isatty=True,
        stdout='output',
        stdin=None,
        stdin_encoding=platform.system(),
        is_windows=True,
        stderr_encoding=platform.system(),
    )
    assert env.program_name == 'http'
    assert env.colors == 256
    assert env.config_dir == Path('/Users/apple/httpie')

# Generated at 2022-06-13 21:41:21.802266
# Unit test for constructor of class Environment
def test_Environment():
    """ 测试类 Environment 初始化 """
    env = Environment()
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr

# Generated at 2022-06-13 21:41:30.343569
# Unit test for constructor of class Environment
def test_Environment():
    import sys, pathlib
    from httpie.compat import is_windows
    from httpie.config import DEFAULT_CONFIG_DIR

    DEBUG_ENV = Environment()
    assert DEBUG_ENV.is_windows == is_windows
    assert DEBUG_ENV.config_dir == DEFAULT_CONFIG_DIR
    assert DEBUG_ENV.stdin == sys.stdin
    assert DEBUG_ENV.stdin_encoding == None 
    assert DEBUG_ENV.stdout == sys.stdout
    assert DEBUG_ENV.stdout_encoding == None
    assert DEBUG_ENV.stderr == sys.stderr
    assert DEBUG_ENV.stderr_isatty == sys.stderr.isatty()
    assert DEBUG_ENV.colors == 256
    assert DEBUG_ENV

# Generated at 2022-06-13 21:41:47.833773
# Unit test for constructor of class Environment
def test_Environment():
    import io
    import tempfile

    fd, config_file_path = tempfile.mkstemp()
    with open(config_file_path, 'w+') as f:
        f.write("""
            [colors]
            request = cyan
            response = green
        """)

    env = Environment(
        program_name='example',
        config_dir=config_file_path,
        stdin=io.BytesIO(b'example'),
        stdin_encoding='utf8',
        stdout=io.BytesIO(),
        stderr=io.BytesIO(),
        is_windows=True,
    )
    assert env.program_name == 'example'
    assert env.config_dir == config_file_path
    assert env.stdin is not None
    assert env.stdin_enc

# Generated at 2022-06-13 21:41:54.471541
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr_isatty == sys.stderr.isatty()

    env = Environment(stdin=object())
    assert env.stdin != sys.stdin

# Generated at 2022-06-13 21:42:11.692795
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        config_dir = '/custom/config/dir',
        stdin = sys.stdin,
        stdin_isatty = sys.stdin.isatty(),
        stdin_encoding = sys.stdin.encoding,
        stdout = sys.stdout,
        stdout_isatty = sys.stdout.isatty(),
        stdout_encoding = sys.stdout.encoding,
        stderr = sys.stderr,
        stderr_isatty = sys.stderr.isatty(),
        colors = 256,
        program_name = 'http',
        devnull = os.devnull
    )
    env._config = Config(directory=env.config_dir)
    env._orig_stderr = sys.stderr

# Generated at 2022-06-13 21:42:13.235997
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert isinstance(env, Environment)


# Generated at 2022-06-13 21:42:17.475075
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout_encoding='FOO', debug=True)
    assert env.stdout_encoding == 'FOO'
    assert env.debug



# Generated at 2022-06-13 21:42:19.501589
# Unit test for constructor of class Environment
def test_Environment():
	env = Environment(stdout_encoding=None, stdout=sys.stdout)
	print(env)

# Generated at 2022-06-13 21:42:31.592402
# Unit test for constructor of class Environment
def test_Environment():
    from io import TextIOWrapper
    from unittest.mock import Mock
    from tempfile import TemporaryFile

    config_dir = Path('test_environment')
    stdin = TextIOWrapper(TemporaryFile('r+'), encoding='utf8')
    stdin.isatty = lambda: True
    stdout = Mock()
    stdout.isatty = lambda: True
    stderr = Mock()
    stderr.isatty = lambda: True
    devnull = None


# Generated at 2022-06-13 21:42:40.611788
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        config_dir = '/home/httpie/config'
    )
    assert env.config_dir == '/home/httpie/config'
    assert env.stderr == sys.stderr
    assert env.stderr.isatty() == True
    assert env.stderr_isatty == True
    assert env.stderr_encoding == 'utf8'


if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:42:51.825571
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()

    assert env.is_windows is is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin is sys.stdin
    assert env.stdin_isatty is bool(sys.stdin.isatty())
    assert env.stdin_encoding is None
    assert env.stdout is sys.stdout
    assert env.stdout_isatty is bool(sys.stdout.isatty())
    assert env.stdout_encoding is None
    assert env.stderr is sys.stderr
    assert env.stderr_isatty is bool(sys.stderr.isatty())
    assert env.colors == (
       256
       if not is_windows
       else None
    )
    assert env.program_

# Generated at 2022-06-13 21:43:03.188850
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=None,is_windows=False,config_dir=".config",stdin="Test",stdin_isatty=False,stdin_encoding="utf8",stdout="teststd1",stdout_isatty=False,stdout_encoding="utf8",stderr="teststderr",stderr_isatty=False,colors=10,program_name="test")
    assert env._devnull==None
    assert env._orig_stderr=="teststderr"

# Generated at 2022-06-13 21:43:13.487979
# Unit test for constructor of class Environment
def test_Environment():
    import os, sys
    import tempfile
    argv = sys.argv
    sys.argv = ['http']
    temp_dir = tempfile.TemporaryDirectory()
    env = Environment(config_dir = temp_dir.name)
    temp_dir.cleanup()
    sys.argv = argv
    return env

# Generated at 2022-06-13 21:43:22.667201
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == Path(DEFAULT_CONFIG_DIR)

    if not is_windows:
        assert env.stdin_isatty == True
        assert env.stdout_isatty == True
        assert env.stderr_isatty == True

    # All attributes can be overwritten using keyword arguments.
    env.test_test = True
    env.test_test2 = False
    assert env.test_test == True
    assert env.test_test2 == False

# Generated at 2022-06-13 21:43:31.771290
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=None, **{
        is_windows : True,
        config_dir : '/home/httpie/',
        stdin : sys.stdin,
        stdin_isatty : False,
        stdin_encoding : None,
        stdout : sys.stdout,
        stdout_isatty : True,
        stdout_encoding : None,
        stderr : sys.stderr,
        stderr_isatty : True,
        colors : 16,
        program_name : 'http',
    })

    assert env.is_windows
    assert env.config_dir == '/home/httpie/'
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == False
    assert not env.stdin_encoding
   

# Generated at 2022-06-13 21:43:35.740981
# Unit test for constructor of class Environment
def test_Environment():

    instance = Environment(
        stdout = open("test_output.txt", "w+"),
        program_name = "http"
    )
    assert instance.stdout is not None
    instance.stdout.close()
    assert instance.program_name == "http"

# Generated at 2022-06-13 21:43:45.734167
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        is_windows=True,
        config_dir='/var/config',
        stdin=None,
        stdin_isatty=False,
        stdin_encoding='utf12',
        stdout=None,
        stdout_isatty=False,
        stdout_encoding='utf12',
        stderr=None,
        stderr_isatty=False,
        colors=1000,
        program_name='http',
        devnull='/dev/null'
    )
    assert env.is_windows == True
    assert env.config_dir == '/var/config'
    assert env.stdin == None
    assert env.stdin_isatty == False
    assert env.stdin_encoding == 'utf12'
    assert env.stdout == None

# Generated at 2022-06-13 21:43:54.042697
# Unit test for constructor of class Environment
def test_Environment():
    # print(Environment(program_name = 'mock'))
    import sys
    import os
    import pathlib
    assert Environment().program_name == 'http'
    assert Environment().is_windows == False
    assert Environment().config_dir == pathlib.Path(DEFAULT_CONFIG_DIR)
    assert Environment().stdin == sys.stdin
    assert Environment().stdin_isatty == sys.stdin.isatty()
    assert Environment().stdin_encoding == None
    assert Environment().stdout == sys.stdout
    assert Environment().stdout_isatty == sys.stdout.isatty()
    assert Environment().stdout_encoding == None
    assert Environment().stderr == sys.stderr
    assert Environment().stderr_isatty == sys.stderr.isatty()

# Generated at 2022-06-13 21:44:06.102256
# Unit test for constructor of class Environment
def test_Environment():
    import io
    env = Environment(
        devnull=io.StringIO(),
        is_windows=False,
        config_dir=Path('./'),
        stdin=io.StringIO(),
        stdin_isatty=True,
        stdin_encoding='utf8',
        stdout=io.StringIO(),
        stdout_isatty=True,
        stdout_encoding='utf8',
        stderr=io.StringIO(),
        stderr_isatty=True,
        program_name='http',
    )
    assert env.devnull.name == "./namespace.devnull"
    assert env.is_windows == False
    assert env.config_dir == "./"
    assert env.stdin.name == "./namespace.stdin"

# Generated at 2022-06-13 21:44:17.806492
# Unit test for constructor of class Environment
def test_Environment():
    dict = {
            'is_windows': 0,
            'config_dir': '/home/.config/httpie',
            'stdin': None,
            'stdin_isatty': 0,
            'stdin_encoding': 'utf8',
            'stdout': 'httpie.stdout',
            'stdout_isatty': 1,
            'stdout_encoding': 'utf8',
            'stderr': 'httpie.stderr',
            'stderr_isatty': 1,
            'colors': 256,
            'program_name': 'http',
            '_orig_stderr': 'httpie.stderr',
            '_devnull': 'httpie.devnull',
            '_config': 'httpie.config'
            }

# Generated at 2022-06-13 21:44:33.597842
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
    assert env._orig_stderr == sys.stderr
    assert env._devnull == None
    assert env._

# Generated at 2022-06-13 21:44:39.159133
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows()
    assert env.config_dir == Path('C:/Users/ph/AppData/Roaming/httpie/')
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == env.stdin.isatty()
    x = env.stdin_encoding
    #assert env.stdin_encoding == env.stdin.encoding or 'utf8'
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == env.stdout.isatty()
    assert env.stdout_encoding == env.stdout.encoding
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == env.stderr.isatty()

# Generated at 2022-06-13 21:44:46.208988
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name = "test name")
    assert(env.program_name == "test name")

# Generated at 2022-06-13 21:44:49.508779
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    if env.is_windows:
        import colorama
        assert getattr(env.stdout, '_wrapped').__class__ == colorama.AnsiToWin32


# Generated at 2022-06-13 21:44:59.114045
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin=None, stdout=None, stderr=None, program_name="http", is_windows=False, config_dir=Path("/"), stdin_encoding="utf-8", stdout_encoding="utf-8", stderr_encoding="utf-8", colors=256)
    print("stdin value: " + str(env.stdin)) 
    print("stdout value: " + str(env.stdout))
    print("stderr value: " + str(env.stderr))
    print("program name: " + str(env.program_name))
    print("is windows: " + str(env.is_windows))
    print("config dir: " + str(env.config_dir))

# Generated at 2022-06-13 21:45:01.793718
# Unit test for constructor of class Environment
def test_Environment():
    setattr(sys, 'stdin', sys.stdout)
    setattr(sys, 'stdout', sys.stderr)
    setattr(sys, 'stderr', None)
    Environment()

# Generated at 2022-06-13 21:45:12.493535
# Unit test for constructor of class Environment
def test_Environment():
    # Testing code
    env = Environment(is_windows=False)
    print(env.config_dir)
    print(env.stdin.name)
    print(env.stdin_isatty)
    print(env.stdin_encoding)
    print(env.stdout.name)
    print(env.stdout_isatty)
    print(env.stdout_encoding)
    print(env.stderr.name)
    print(env.stderr_isatty)
    print(env._devnull)
    print(env._config)
    print(env.program_name)
    print(env)
    print(str(env))
    print(repr(env))


# Generated at 2022-06-13 21:45:19.029692
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin_encoding == 'utf8'
    assert env.stdout_encoding == 'utf8'
    assert env.stdin_isatty
    assert env.stdout_isatty
    assert env.stderr_isatty
    assert env.stderr == sys.stderr
    assert env.devnull is None
    assert env.config != {}

# Generated at 2022-06-13 21:45:28.215455
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
         stdin=None,
         stdin_isatty=False,
         stdout=None,
         stdout_isatty=False,
         stderr=None,
         stderr_isatty=False,
         colors=None,
         is_windows=False,
         program_name='http',
         config_dir=Path('./')
    )
    assert env.stdin is None
    assert env.stdin_isatty is False
    assert env.stdout is None
    assert env.stderr is None
    assert env.colors is None
    assert env.is_windows is False
    assert env.program_name == 'http'
    assert env.config_dir == Path('./')
    # Test the method __str__
    assert str(env)

# Generated at 2022-06-13 21:45:38.482519
# Unit test for constructor of class Environment
def test_Environment():
    # Test if an object e of class Environment is created
    e = Environment()
    assert type(e) == Environment
    # Test if the attributes of e are correctly set
    assert e.is_windows == is_windows
    assert e.config_dir == DEFAULT_CONFIG_DIR
    assert e.stdin == sys.stdin
    assert e.stdin_isatty == sys.stdin.isatty() if e.stdin else False
    assert e.stdout == sys.stdout
    assert e.stdout_isatty == sys.stdout.isatty()
    assert e.stderr == sys.stderr
    assert e.stderr_isatty == sys.stderr.isatty()

# Generated at 2022-06-13 21:45:43.282449
# Unit test for constructor of class Environment
def test_Environment():
    env=Environment()
    if env.stderr.isatty() is True:
        print("stderr is a tty")
    else:
        print("stderr is not a tty")

# Generated at 2022-06-13 21:45:54.406549
# Unit test for constructor of class Environment
def test_Environment():
    stdin_encoding = 'utf8'
    stdout_encoding = 'utf8'
    is_windows = True
    config_dir = 'config_dir'
    program_name = 'http'
    assert Environment(
        stdin_encoding=stdin_encoding,
        stdout_encoding=stdout_encoding,
        is_windows=is_windows,
        config_dir=config_dir,
        program_name=program_name
    ) == Environment(
        stdin_encoding=stdin_encoding,
        stdout_encoding=stdout_encoding,
        is_windows=is_windows,
        config_dir=config_dir,
        program_name=program_name
    )

# Generated at 2022-06-13 21:46:02.116939
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment()
    e.config_dir = DEFAULT_CONFIG_DIR
    assert e.config_di

# Generated at 2022-06-13 21:46:09.984423
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()

    assert env.is_windows
    assert env.config_dir
    assert env.stdin
    assert env.stdin_isatty
    assert env.stdin_encoding
    assert env.stdout
    assert env.stdout_isatty
    assert env.stdout_encoding
    assert env.stderr
    assert env.stderr_isatty
    assert env.program_name
    assert env.config
    assert env.devnull

# Generated at 2022-06-13 21:46:12.538822
# Unit test for constructor of class Environment
def test_Environment():
    assert not Environment().stdin_isatty
    assert Environment().stdout_isatty
    

# Generated at 2022-06-13 21:46:16.000628
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=1)
    assert env.devnull == 1
    assert type(env.config) == Config
    assert env.config.directory == DEFAULT_CONFIG_DIR


# Generated at 2022-06-13 21:46:24.266815
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(config_dir=None, stdin=None, stdout=None, stderr=None)
    assert env.config_dir == None
    assert env.stdin == None
    assert env.stdout == None
    assert env.stderr == None
    assert env.is_windows == is_windows
    assert env.stdin_isatty == False
    assert env.stdout_isatty == False
    assert env.stderr_isatty == False
    assert env.stdin_encoding == None
    assert env.stdout_encoding == None

# Generated at 2022-06-13 21:46:34.300912
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment()

    # test values
    assert e.is_windows == is_windows
    assert e.config_dir == DEFAULT_CONFIG_DIR
    assert e.stdin == sys.stdin
    assert e.stdin_isatty == sys.stdin.isatty()
    assert e.stdin_encoding is None
    assert e.stdout == sys.stdout
    assert e.stdout_isatty == sys.stdout.isatty()
    assert e.stdout_encoding is None
    assert e.stderr == sys.stderr
    assert e.stderr_isatty == sys.stderr.isatty()
    assert e.colors == 256

    # test __str__

# Generated at 2022-06-13 21:46:35.699632
# Unit test for constructor of class Environment
def test_Environment():
    print("Start test_Environment")
    env = Environment.__init__(Environment)
    print(env)

# Generated at 2022-06-13 21:46:44.193063
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin=None)
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin is None
    assert env.stdin_isatty is False
    assert env.stdin_encoding is None
    assert env.stdout is sys.stdout
    assert env.stdout_isatty is True
    assert env.stdout_encoding == 'utf8'
    assert env.stderr is sys.stderr
    assert env.stderr_isatty is True
    assert env.colors == 8
    assert env.program_name == 'http'

    env = Environment(colors=256, program_name='http123')
    assert env.colors == 256

# Generated at 2022-06-13 21:46:51.753383
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin is not None
    assert env.stdin_isatty is not None
    assert env.stdout is not None
    assert env.stdout_isatty is not None
    assert env.stderr is not None
    assert env.stderr_isatty is not None
    assert env.program_name == 'http'

# Generated at 2022-06-13 21:47:00.110001
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(colors=16)
    assert env.colors == 16
    assert env._devnull is None

    with open(os.devnull, 'w+') as devnull:
        env = Environment(devnull=devnull)
        assert env._devnull == devnull

    env = Environment(stdout=None)
    assert env.stdout is None

    env = Environment(stderr=None)
    assert env.stderr is None

    # We use `is not None` instead of `is None` to
    # avoid `AttributeError` on `stream.name` in
    # the default case.
    env = Environment(stdin=None)
    assert env.stdin is None

    env = Environment(stdin=sys.stdin)
    assert env.stdin is sys.stdin
    assert env

# Generated at 2022-06-13 21:47:19.007392
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        config_dir=Path('/config_dir'),
        stdin=None,
        stdin_isatty=False,
        stdin_encoding=None,
        stdout=sys.stderr,
        stdout_isatty=True,
        stdout_encoding='utf8',
        stderr=sys.stdout,
        stderr_isatty=True,
        colors=256,
        program_name='httpie',
    )
    assert env.config_dir == Path('/config_dir')
    assert env.stdin_isatty == False
    assert env.stdout == sys.stderr
    assert env.stdout_isatty == True
    assert env.stdout_encoding == 'utf8'

# Generated at 2022-06-13 21:47:25.279079
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(is_windows=True,
                      config_dir=DEFAULT_CONFIG_DIR,
                      stdin=sys.stdin,
                      stdin_isatty=sys.stdin.isatty(),
                      stdout=sys.stdout,
                      stdout_isatty=sys.stdout.isatty(),
                      stderr=sys.stderr,
                      stderr_isatty=sys.stderr_isatty,
                      program_name='http')
    assert env.is_windows == True
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout == sys.stdout
    assert env.stdout

# Generated at 2022-06-13 21:47:30.084128
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.config
    assert env.stdout
    assert env.stdout_isatty
    assert env.stderr
    assert env.stderr_isatty
    assert env.stdin
    assert env.stdin_isatty
    assert env.colors is 256
    assert env.program_name



# Generated at 2022-06-13 21:47:40.488387
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
    assert env.program_name == 'http'

# Generated at 2022-06-13 21:47:46.745978
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin="test", stdout="test", stderr="test")
    assert env.stdin == "test"
    assert env.stdout == "test"
    assert env.stderr == "test"

# Generated at 2022-06-13 21:47:54.328192
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()

    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin is sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout is sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()


# Generated at 2022-06-13 21:48:01.030036
# Unit test for constructor of class Environment
def test_Environment():
    import builtins
    env = Environment()
    assert env.is_windows is False
    assert env.config_dir == Path('/Users/xshen/.config/httpie')
    assert env.stdin == builtins.stdin
    assert env.stdin_isatty is True
    assert env.stdout is builtins.stdout
    assert env.stdout_isatty is True
    assert env.stderr is builtins.stderr
    assert env.stderr_isatty is True

# Generated at 2022-06-13 21:48:02.757381
# Unit test for constructor of class Environment
def test_Environment():
    assert repr_dict(dict(env.__dict__)) == repr_dict(ENV_ATTRS)


# Generated at 2022-06-13 21:48:13.104748
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment()
    # check if subclass of object
    assert isinstance(e, object)
    # check if instance of class Environment
    assert isinstance(e, Environment)
    # check if it has the correct attributes
    assert e.is_windows == is_windows
    assert e.config_dir == DEFAULT_CONFIG_DIR
    assert e.stdin == sys.stdin
    # check if stdin_isatty = true
    assert e.stdin_isatty == e.stdin.isatty() if e.stdin else False
    assert e.stdin_encoding == None
    assert e.stdout == sys.stdout
    assert e.stdout_isatty == e.stdout.isatty()
    assert e.stdout_encoding == None

# Generated at 2022-06-13 21:48:17.464711
# Unit test for constructor of class Environment
def test_Environment():
    sys.stderr.write("Testing Environment ... ")
    env = Environment()
    print("constructor default value are correctly set")
    sys.stderr.write("OK\n")

# Generated at 2022-06-13 21:48:46.165084
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stdin.__class__.__name__ == '_io.TextIOWrapper'
    assert env.stdout.__class__.__name__ == '_io.TextIOWrapper'
    assert env.stderr.__class__.__name__ == '_io.TextIOWrapper'
    assert env.stdin_isatty is True
    assert env.stdout_isatty is True
    assert env.stderr_isatty is True
    assert env.stdin_encoding == 'utf8'
    assert env.stdout_encoding == 'utf8'
    assert env.is_windows == False
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.program_name == 'http'
    assert env.colors

# Generated at 2022-06-13 21:48:53.716511
# Unit test for constructor of class Environment
def test_Environment():
    # Test for Environment class
    stdin = 'sys.stdin'
    is_atty = 'True'
    env = Environment(stdin=stdin, stdin_isatty=is_atty)
    assert stdin == env.stdin
    assert is_atty == env.stdin_isatty



# Generated at 2022-06-13 21:49:08.069598
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


if __name__ == '__main__':
    import pytest

# Generated at 2022-06-13 21:49:15.096868
# Unit test for constructor of class Environment
def test_Environment():
    import tempfile
    def test():
        # a little testing of Environment
        env = Environment()
        assert type(env.stdin) == file
        assert type(env.stdout) == file
        assert type(env.stderr) == file
        assert isinstance(env.stdout_encoding, str)
    test()
    temp = tempfile.TemporaryFile()
    env2 = Environment(stdin=temp)
    assert env2.stdin == temp
    assert isinstance(env2.stdout_encoding, str)
    assert type(env2.stdout) == file
    assert type(env2.stderr) == file
    temp.close()

# Generated at 2022-06-13 21:49:24.367628
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin=None, stdout=None, stderr=None,
                      colors=256, program_name='http', is_windows=True,
                      config_dir=DEFAULT_CONFIG_DIR)
    #assert env.stdin == None
    assert env.stdout == None
    assert env.stderr == None
    assert env.colors == 256
    assert env.program_name == 'http'
    assert env.is_windows == True
    assert env.config_dir == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:49:31.393349
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    print(env)
    # assert env.__dict__.keys() == __builtins__.__dict__.keys()
    env2 = Environment(devnull=5)
    print(env2)
    # assert env2.__dict__.keys() == __builtins__.__dict__.keys()
    env3 = Environment(is_windows=False)
    print(env3)
    # assert env3.__dict__.keys() == __builtins__.__dict__.keys()



# Generated at 2022-06-13 21:49:40.014223
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.__dict__['is_windows'] == is_windows
    assert env.__dict__['config_dir'] == Path(DEFAULT_CONFIG_DIR)
    assert env.__dict__['stdin'] == sys.stdin
    assert env.__dict__['stdin_isatty'] == sys.stdin.isatty()
    assert env.__dict__['stdin_encoding'] == None
    assert env.__dict__['stdout'] == sys.stdout
    assert env.__dict__['stdout_isatty'] == sys.stdout.isatty()
    assert env.__dict__['stdout_encoding'] == None
    assert env.__dict__['stderr'] == sys.stderr

# Generated at 2022-06-13 21:49:41.616219
# Unit test for constructor of class Environment
def test_Environment():
    os.chdir('./httpie')
    e = Environment()
    print(e)


# Generated at 2022-06-13 21:49:53.229574
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout_encoding='utf-16le')
    assert env.stdout_encoding == 'utf-16le'

    # Unit test for attribute stdout_isatty of class Environment
    assert env.stdout_isatty == 1

    # Unit test for attribute stderr_isatty of class Environment
    assert env.stderr_isatty == 1

    # Unit test for attribute colors of class Environment
    assert env.colors == 256

    # Unit test_dict for attribute program_name of class Environment
    assert env.program_name == 'http'

    # Unit test for property config of class Environment
    assert env.config is not None

    # Unit test for property devnull of class Environment
    assert env.devnull is not None

    # Unit test for function log_error of class Environment

# Generated at 2022-06-13 21:49:55.286608
# Unit test for constructor of class Environment
def test_Environment():
    assert not Environment(colors=16).is_windows
    assert Environment(colors=16).colors == 16
    if not is_windows:
        assert Environment(colors=16).__repr__() == "<Environment {'colors': 16, 'is_windows': False}>"
    else:
        assert Environment(colors=16).__repr__() == "<Environment {'colors': 16, 'is_windows': True}>"