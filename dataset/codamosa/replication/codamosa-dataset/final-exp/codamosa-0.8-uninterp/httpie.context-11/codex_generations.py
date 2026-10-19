

# Generated at 2022-06-13 21:40:25.133292
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(is_windows = False)
    assert env.is_windows == False
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == False
    assert env.stdin_encoding is None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == True
    assert env.stdout_encoding is None
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == True
    assert env.colors == 256
    assert env.program_name == 'http'
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env._orig_stderr == sys.stderr
    assert env._devnull

# Generated at 2022-06-13 21:40:26.608139
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin_isatty=False, stdout_isatty=False)
    print(env)

# Generated at 2022-06-13 21:40:36.882289
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert isinstance(env, Environment)
    assert env.is_windows == os.name == "nt"
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.colors == 256
    assert env.program_name == "http"

    env = Environment(stdout=sys.stdin, devnull=sys.stdout)
    assert isinstance(env, Environment)
    assert env.is_windows == os.name

# Generated at 2022-06-13 21:40:38.936185
# Unit test for constructor of class Environment
def test_Environment():
    print(env)


# Generated at 2022-06-13 21:40:51.039143
# Unit test for constructor of class Environment
def test_Environment():                           # write your test code here
    _env = Environment(stdin=sys.stdin,
                       stdout=sys.stdout,
                       stderr=sys.stderr,
                       config_dir=DEFAULT_CONFIG_DIR,
                       is_windows = is_windows,
                       program_name = 'http',
                       devnull = None)

    print(_env)
    assert _env.stdin == sys.stdin
    assert _env.stdout == sys.stdout
    assert _env.stderr == sys.stderr
    assert _env.config_dir == DEFAULT_CONFIG_DIR
    assert _env.is_windows == is_windows
    assert _env.program_name == 'http'
    assert _env.devnull == None

    # log_error Test

# Generated at 2022-06-13 21:41:01.396468
# Unit test for constructor of class Environment
def test_Environment():
    """
    Test the constructor of class Environment
    :return:
    """
    # Test basic attributes
    env = Environment(config_dir='/Users/kashyap/PycharmProjects')
    assert env.config_dir == Path('/Users/kashyap/PycharmProjects')
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()

    # Test __str__()

# Generated at 2022-06-13 21:41:13.284212
# Unit test for constructor of class Environment
def test_Environment():
    def get_env(**kwargs): env = Environment()
    env.__dict__.update(**kwargs)
    return env
    env = get_env()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin is sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout is sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr is sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.program_name == 'http'

# Generated at 2022-06-13 21:41:22.937694
# Unit test for constructor of class Environment
def test_Environment():
     stdin = sys.stdin
     stdout = sys.stdout
     stderr = sys.stderr
     devnull = open(os.devnull, 'w+')
     #env = Environment(stdin=stdin)
     env = Environment(stdout=stdout,stderr=stderr,devnull=devnull)
     print(env)
     print(env.stdin)
     print(env.stdout)
     print(env.stderr)
     env.log_error("Hello World")


# Generated at 2022-06-13 21:41:32.413562
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    stdin_encoding = env.stdin_encoding
    stdout_encoding = env.stdout_encoding
    env2 = Environment(stdin_encoding='utf8', stdout_encoding='utf8')
    assert env.stdin_encoding == stdin_encoding and env2.stdin_encoding == 'utf8'
    assert env.stdout_encoding == stdout_encoding and env2.stdout_encoding == 'utf8'


# Generated at 2022-06-13 21:41:38.846581
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name='httpie')
    assert env.program_name == 'httpie'
    assert env.config_dir == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:42:02.267161
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    import curses

    def get_mock_stdin():
        class MockStdin:
            def isatty(self):
                return False
        return MockStdin()

    def get_mock_stdout():
        class MockStdout:
            def isatty(self):
                return False
        return MockStdout()

    env = Environment()
    assert env.is_windows == sys.platform.startswith('win')
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty() if sys.stdin else False
    assert env.stdin_encoding == sys.stdin.encoding if sys.stdin else None

# Generated at 2022-06-13 21:42:13.590704
# Unit test for constructor of class Environment
def test_Environment():
    from io import StringIO
    from tempfile import TemporaryDirectory
    from unittest import mock

    config_dir = TemporaryDirectory()
    env = Environment(
        program_name='custom_program_name',
        config_dir=config_dir.name,
        stdin=StringIO(),
        stdout=StringIO(),
        stderr=StringIO(),
    )
    assert env.program_name == 'custom_program_name'
    assert env.config_dir == Path(config_dir.name)
    assert isinstance(env.stdin, StringIO)
    assert isinstance(env.stdout, StringIO)
    assert isinstance(env.stderr, StringIO)

    parametrize = mock.MagicMock()
    parametrize.is_windows = is_windows

# Generated at 2022-06-13 21:42:18.967761
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert isinstance(env, Environment)
    assert isinstance(env.stdin, IO)
    assert isinstance(env.stdout, IO)
    assert isinstance(env.stderr, IO)


# Generated at 2022-06-13 21:42:31.179964
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment()
    assert type(e).__dict__['config_dir'] == DEFAULT_CONFIG_DIR
    assert type(e).__dict__['stdin'] == sys.stdin
    assert type(e).__dict__['stdin_isatty'] == sys.stdin.isatty()
    assert type(e).__dict__['stdout'] == sys.stdout
    assert type(e).__dict__['stdout_isatty'] == sys.stdout.isatty()
    assert type(e).__dict__['stderr'] == sys.stderr
    assert type(e).__dict__['stderr_isatty'] == sys.stderr.isatty()
    assert type(e).__dict__['colors'] == 256
    assert type(e).__dict__

# Generated at 2022-06-13 21:42:45.740571
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    env1 = Environment(program_name = 'http', stdin = sys.stdin)
    env2 = Environment(stdin = None)
    env3 = Environment(stdin = None, stdout = sys.stdout, stderr = sys.stderr)
    assert not env.stdin_isatty
    assert env.stdin_isatty == env1.stdin_isatty
    assert env.stdin_isatty != env2.stdin_isatty and not env2.stdin_isatty
    assert env1.stdin_isatty == env3.stdin_isatty
    assert env1.stdout == env3.stdout and env1.stderr == env3.stderr

# Generated at 2022-06-13 21:43:00.244271
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin = sys.stdin, stdout = sys.stdout, stderr = sys.stderr, config_dir = DEFAULT_CONFIG_DIR, is_windows = is_windows, colors = 256, program_name = 'http', stdin_isatty = sys.stdin.isatty(), stdin_encoding = 'utf8', stdout_isatty = sys.stdout.isatty(), stdout_encoding = 'utf8', stderr_isatty = sys.stderr.isatty(), _devnull = open(os.devnull, 'w+'))
    print(env)
    print(env._devnull)
    print(env._orig_stderr)
    print(env.config)

test_Environment()

# Generated at 2022-06-13 21:43:08.661909
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert repr(type(env)) == "<class 'httpie.environment.Environment'>"
    assert isinstance(env, Environment)

# Generated at 2022-06-13 21:43:17.364690
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdin_encoding == None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding == None
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.program_name == 'http'
    assert env.colors == 256
    assert env.config_dir == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:43:27.506381
# Unit test for constructor of class Environment
def test_Environment():
    # (1) Initialization
    env = Environment()
    # 1.1 For all attributes:
    #     1.1.1 Check if all attributes are identical to the ones in the default environment
    for attr in env.__dict__.keys():
        assert env.__dict__[attr] == Environment.__dict__[attr]
    
    # (2) Calling the constructor with keyword arguments 
    #     (which are then used to overwrite the class attributes)
    env1 = Environment(devnull='This is a devnull file', stdin='stdin file')
    # 1.1 For all attributes:
    #     1.1.1 Check if the keyword arguments are set properly
    assert env1.devnull == 'This is a devnull file'
    assert env1.stdin == 'stdin file'
    #     1.1.

# Generated at 2022-06-13 21:43:35.915401
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.colors == 256
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    config = env.config
    assert config.directory == DEFAULT_CONFIG_DIR
    assert env.stdin_encoding == config.config_file.encoding

# Generated at 2022-06-13 21:43:51.966512
# Unit test for constructor of class Environment
def test_Environment():
  env = Environment(config_dir="/home", stdin_isatty=True, stdout_isatty=False, stderr_isatty=False, devnull="/dev/null", colors=256)
  assert env.config_dir == "/home"
  assert env.stdin_isatty == True
  assert env.stdout_isatty == False
  assert env.stderr_isatty == False
  assert env.devnull == "/dev/null"
  assert env.colors == 256
  assert Environment().config_dir == "/home/.httpie"



# Generated at 2022-06-13 21:43:54.064296
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env is not None
    print(env)


# Unit tests for class Config

# Generated at 2022-06-13 21:44:06.101823
# Unit test for constructor of class Environment
def test_Environment():
    from tempfile import TemporaryDirectory
    from httpie.plugins import plugin_manager
    from httpie.config import Config
    import os

    with TemporaryDirectory() as tmpdir:
        env = Environment(stdin=None,
                          stdout=None,
                          stderr=None,
                          config_dir=Path(tmpdir),
                          program_name='test_program')

        assert env.stdin is None
        assert env.stdout is None
        assert env.stderr is None
        assert env.config_dir == Path(tmpdir)
        assert env.config == Config(directory=Path(tmpdir))
        assert env.program_name == 'test_program'

        # Test: check if the configuration file is created.
        config_file = Path(tmpdir) / 'config.json'
        assert config_

# Generated at 2022-06-13 21:44:17.806913
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.program_name == 'http'
    assert env.stderr == env._orig_stderr
    assert env.stderr == sys.stderr
    assert env.stderr_encoding == getattr(env.stderr, 'encoding', None) or 'utf8'
    assert env.stdin == sys.stdin
    assert env.stdin_encoding == getattr(env.stdin, 'encoding', None) or 'utf8'
    assert env.stdout == sys.stdout
    assert env.stdout_encoding == getattr(env.stdout, 'encoding', None) or 'utf8'
    assert env.is_windows == is_windows
    assert env.colors == 256
    assert env.config_dir == DEFAULT_CONFIG_

# Generated at 2022-06-13 21:44:33.598990
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(a=1, b=2)
    assert env.a == 1
    assert env.b == 2
    assert env.__dict__['a'] == 1
    assert env.__dict__['b'] == 2
    assert env.__dict__.get('c') == None
    assert env.__dict__.get('d') == None
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert isinstance(env.config, Config)
    # Set the value of env.config_dir and set a new Config
    env.config_dir = './'
    assert str(env.config_dir) == "PosixPath('./')"
    assert isinstance(env.config, Config)
    # We can't change the value of config_dir because it is read-only

# Generated at 2022-06-13 21:44:35.236151
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.config == Config(directory=DEFAULT_CONFIG_DIR)

# Generated at 2022-06-13 21:44:47.748021
# Unit test for constructor of class Environment
def test_Environment():
    # initialize environment
    env = Environment()
    # assert if attributes are set or not
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == stdin.isatty() if stdin else False
    assert env.stdin_encoding == None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == stdout.isatty()
    assert env.stdout_encoding == None
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == stderr.isatty()
    assert env.colors == 256

# Generated at 2022-06-13 21:44:57.910880
# Unit test for constructor of class Environment
def test_Environment():
    obj = Environment()
    assert not hasattr(obj, '_orig_stderr')
    assert not hasattr(obj, '_devnull')
    obj1 = Environment(devnull=None,is_windows=False,config_dir=Path('.'),stdin=sys.stdin,stdin_isatty=False,stdin_encoding='utf8',stdout=sys.stdout,stdout_isatty=True,stdout_encoding='utf8',stderr=sys.stderr,stderr_isatty=True,colors=256,program_name='http')
    assert obj1.is_windows == False
    assert obj1.config_dir == Path('.')
    assert obj1.stdin == sys.stdin
    assert obj1.stdin_isatty == False
   

# Generated at 2022-06-13 21:45:02.847288
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=True, config_dir=Path('.'), program_name='HTTPIE')
    assert env.devnull == True
    assert env.config_dir == Path('.')
    assert env.program_name == 'HTTPIE'
    assert env.colors == 256
    assert env.stderr == sys.stderr
    print(env)

# Generated at 2022-06-13 21:45:06.733322
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=1,stdout=1,config_dir=1)
    assert env.devnull == 1
    assert env.stdout == 1
    assert env.config_dir == 1

# Generated at 2022-06-13 21:45:22.790649
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment()
    assert environment.is_windows == is_windows
    assert environment.config_dir == DEFAULT_CONFIG_DIR
    assert environment.stdin == sys.stdin
    assert environment.stdout == sys.stdout
    assert environment.stderr == sys.stderr

# Generated at 2022-06-13 21:45:29.048608
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment(a=1, b='xyz')
    assert e.a == 1
    assert e.b == 'xyz'
    try:
        e.c
    except AttributeError:
        pass
    else:
        raise AssertionError



# Generated at 2022-06-13 21:45:37.032414
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    import os
    from pathlib import Path
    from typing import IO, Optional


    # test Environment()
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdin_encoding == str(sys.stdin.encoding)
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding == str(sys.stdout.encoding)
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys

# Generated at 2022-06-13 21:45:50.657462
# Unit test for constructor of class Environment
def test_Environment():
    # Default environment
    env = Environment()
    assert env.stdin_encoding is not None
    assert env.stdout_encoding is not None
    assert env.stderr_encoding is not None

    # Override the default standard streams
    env = Environment(
        stdin=None,
        stdin_encoding='foo',
        stdout=None,
        stdout_encoding='foo',
        stderr=None,
        stderr_encoding='foo',
    )
    assert env.stdin is None
    assert env.stdin_encoding == 'foo'
    assert env.stdout is None
    assert env.stdout_encoding == 'foo'
    assert env.stderr is None
    assert env.stderr_encoding == 'foo'


# Generated at 2022-06-13 21:45:53.075305
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.config_dir == DEFAULT_CONFIG_DIR


# Generated at 2022-06-13 21:46:06.148768
# Unit test for constructor of class Environment
def test_Environment():
    ass = Environment()
    assert ass.is_windows == False
    assert ass.config_dir == Path.home().joinpath('.httpie')
    assert ass.stdin == sys.stdin
    assert ass.stdin_isatty == False
    assert ass.stdin_encoding == 'utf-8'
    assert ass.stdout == sys.stdout
    assert ass.stdout_isatty == True
    assert ass.stdout_encoding == 'utf-8'
    assert ass.stderr == sys.stderr
    assert ass.stderr_isatty == True
    assert ass.colors == 256
    assert ass.program_name == 'http'


# Generated at 2022-06-13 21:46:07.909622
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name='http')
    assert env.program_name == 'http'
    assert env.colors == 256

# Generated at 2022-06-13 21:46:18.319765
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull='/dev/null', is_windows=True,
                      config_dir='/', stdin=sys.stdin,
                      stdin_encoding='utf8', stdin_isatty=sys.stdin.isatty(),
                      stdout=sys.stdout, stdout_encoding='utf8',
                      stdout_isatty=sys.stdout.isatty(), stderr=sys.stderr,
                      stderr_isatty=sys.stderr.isatty(), program_name='http',
                      colors=256)
    env.log_error('msg', level='error')
    env.devnull = 'dev'

# Generated at 2022-06-13 21:46:28.652579
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()

    assert env.is_windows is True
    assert env.config_dir == Path.home() / '.httpie'
    assert env.stdin is not None
    assert env.stdin_isatty is True
    assert env.stdin_encoding == 'utf8'
    assert env.stdout is not None
    assert env.stdout_isatty is True
    assert env.stdout_encoding == 'utf8'
    assert env.stderr is not None
    assert env.stderr_isatty is True
    assert env.colors is 256
    assert env.program_name == 'http'


# Generated at 2022-06-13 21:46:38.652740
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        is_windows = True,
        config_dir = '/home/httpie',
        stdin = None,
        stdin_isatty = False,
        stdin_encoding = 'utf8',
        stdout = sys.stdout,
        stdout_isatty = True,
        stdout_encoding = 'utf8',
        stderr = sys.stderr,
        stderr_isatty = True,
        colors = 256,
        program_name = 'httpi'
    )
    assert env.is_windows == True
    assert env.config_dir == Path('/home/httpie')
    assert env.stdin == None
    assert env.stdin_isatty == False
    assert env.stdin_encoding == 'utf8'
    assert env

# Generated at 2022-06-13 21:46:58.831506
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()

    # Check if the parameters passed during initialization are correct
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin # `None` wenn closed fd (#791)
    assert env.stdin_isatty == (env.stdin.isatty() if env.stdin else False)
    assert env.stdin_encoding == None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == env.stdout.isatty()
    assert env.stdout_encoding == None
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == env.stderr.isatty()

# Generated at 2022-06-13 21:47:13.069058
# Unit test for constructor of class Environment

# Generated at 2022-06-13 21:47:19.050955
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert is_windows == env.is_windows
    assert sys.stdin == env.stdin
    assert sys.stdout == env.stdout
    assert sys.stderr == env.stderr
    assert 256 == env.colors

# Generated at 2022-06-13 21:47:24.179476
# Unit test for constructor of class Environment
def test_Environment():
    class TmpClass(object):
        def __init__(self, devnull = None, **kwargs):
            assert all(hasattr(type(self), attr) for attr in kwargs.keys())
            self.__dict__.update(**kwargs)

    t = TmpClass(test = 'test')
    print(t.test)

# Generated at 2022-06-13 21:47:35.877279
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

# Generated at 2022-06-13 21:47:38.575825
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        
            stdin_encoding = 'abc'
        )
    print(env.stdin_encoding)
    return env


# Generated at 2022-06-13 21:47:44.059053
# Unit test for constructor of class Environment
def test_Environment():
    # print(Environment.config_dir)
    # print(Environment.stdin)
    # print(Environment.stdout)
    # print(Environment.stderr)
    print(Environment())



# Generated at 2022-06-13 21:47:54.339360
# Unit test for constructor of class Environment
def test_Environment():
    # Dummy data for testing
    env_data1 = {
        'is_windows': False,
        'config_dir': '/home/username/.httpie'
    }
    env_data2 = {
        'is_windows': False,
        'config_dir': '/home/username/'
    }
    # Unit test
    env1 = Environment(**env_data1)
    assert env1.config_dir == env_data1['config_dir']
    assert env1.is_windows == env_data1['is_windows']

    env2 = Environment(**env_data2)
    assert env2.config_dir == env_data2['config_dir']
    assert env2.is_windows == env_data2['is_windows']



# Generated at 2022-06-13 21:47:56.515527
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(is_windows=True)
    assert env.is_windows == True


# Generated at 2022-06-13 21:47:59.330859
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment(stdin = None, stdin_isatty = False, stdin_encoding = None)


# Generated at 2022-06-13 21:48:19.404766
# Unit test for constructor of class Environment
def test_Environment():
    stdin_encoding = 'utf-8'
    stdout_encoding = 'utf-8'
    env = Environment(stdin_encoding=stdin_encoding, stdout_encoding=stdout_encoding)
    assert env.stdin_encoding == stdin_encoding
    assert env.stdout_encoding == stdout_encoding

# Generated at 2022-06-13 21:48:21.238814
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert isinstance(env, Environment)

# Generated at 2022-06-13 21:48:34.076021
# Unit test for constructor of class Environment
def test_Environment():
    from io import StringIO
    from tempfile import mkdtemp
    from httpie.core import main
    from httpie.config import DEFAULT_CONFIG_DIR
    from httpie import ExitStatus

    # Test the default constructor first
    assert(Environment().stdin.name == '<stdin>')
    assert(Environment().stdout.name == '<stdout>')
    assert(Environment().stderr.name == '<stderr>')
    assert(Environment().config_dir == DEFAULT_CONFIG_DIR)

    # Test the custom constructor
    tempdir = mkdtemp()
    config_dir = Path(tempdir)
    stdin = StringIO("I am the content of stdin")
    stdout = StringIO("")
    stderr = StringIO("")
    devnull = StringIO("")
   

# Generated at 2022-06-13 21:48:43.174819
# Unit test for constructor of class Environment
def test_Environment():
    env1 = Environment()
    assert env1.stdin == sys.stdin
    assert env1.stdout == sys.stdout
    assert env1.stderr == sys.stderr
    assert env1.config_dir == DEFAULT_CONFIG_DIR
    assert env1.stdin_encoding == None
    assert env1.stdout_encoding == None

    env2 = Environment(stdin = sys.stdout, stdout = sys.stdin,
                       config_dir = Path('/'), stdin_encoding = 'ascii',
                       stdout_encoding = 'utf8', stderr_encoding = 'utf8')
    assert env2.stdin == sys.stdout
    assert env2.stdout == sys.stdin
    assert env2.stderr == sys.stderr


# Generated at 2022-06-13 21:48:56.714910
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment().__str__() == '<Environment {\'config\': None, \'colors\': 256, \'is_windows\': False, \'program_name\': \'http\', \'config_dir\': PosixPath(\'~/.config/httpie\'), \'stdin\': <_io.TextIOWrapper encoding=\'UTF-8\'>, \'stdin_isatty\': True, \'stdin_encoding\': \'UTF-8\', \'stdout\': <_io.TextIOWrapper encoding=\'UTF-8\'>, \'stdout_isatty\': True, \'stdout_encoding\': \'UTF-8\', \'stderr\': <_io.TextIOWrapper encoding=\'UTF-8\'>, \'stderr_isatty\': True}>'
    
test_

# Generated at 2022-06-13 21:48:58.633972
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin=None)
    print(env)


# Generated at 2022-06-13 21:49:11.702141
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows is False
    assert env.stdin is sys.stdin
    assert env.stdin.isatty() is False
    assert env.stdin_isatty is False
    assert env.stdin_encoding == 'UTF-8'
    assert env.stdout is sys.stdout
    assert env.stdout.isatty() is True
    assert env.stdout_isatty is True
    assert env.stdout_encoding == 'UTF-8'
    assert env.stdout.write('hello stdout') == 6
    print(env.stdout.write('hello stdout'))
    assert env.stderr is sys.stderr
    assert env.stderr.isatty() is True

# Generated at 2022-06-13 21:49:20.463623
# Unit test for constructor of class Environment
def test_Environment():
    from io import StringIO

    stdout = StringIO()
    env = Environment(
        stdout=stdout,
        stdin_encoding='utf-16',
        stdout_encoding='utf-8',
    )
    env.stderr = None
    assert env.stdout_isatty is False
    assert env.stdin_isatty is False
    assert env.stderr_isatty is False
    assert env.stdout == stdout
    assert env.stdin_encoding == 'utf-16'
    assert env.stdout_encoding == 'utf-8'
    assert env.stderr is None
    # assert env.stderr is not None
    assert env.stdin is not None

# Generated at 2022-06-13 21:49:28.881324
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stdin == sys.stdin
    assert env.stdin_encoding == "UTF-8"
    assert env.stdout == sys.stdout
    assert env.stdout_encoding == "UTF-8"
    assert env.stderr == sys.stderr
    assert env.stderr_encoding == "UTF-8"
    assert env.colors == 256
    assert env.program_name == 'http'

# Generated at 2022-06-13 21:49:38.271401
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull="devnull", is_windows=True,
                      config_dir="DEFAULT_CONFIG_DIR", stdin="sys.stdin",
                      stdin_isatty=False, stdin_encoding="None",
                      stdout="sys.stdout", stdout_isatty=False,
                      stdout_encoding="None", stderr="sys.stderr",
                      stderr_isatty=False, colors=256, program_name="http")
    assert env.devnull == "devnull"
    assert env.is_windows
    assert env.config_dir == "DEFAULT_CONFIG_DIR"
    assert env.stdin == "sys.stdin"
    assert not env.stdin_isatty
    assert env.stdin_encoding == "None"
   

# Generated at 2022-06-13 21:49:59.359478
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdin_encoding is None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding == sys.stdout.encoding
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.stderr_encoding is None


# Generated at 2022-06-13 21:50:07.367549
# Unit test for constructor of class Environment
def test_Environment():
    import io
    import os
    import sys
    from pathlib import Path
    e = Environment()
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