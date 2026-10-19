

# Generated at 2022-06-13 21:40:25.558781
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
            is_windows = False,
            config_dir = 'path of config dir',
            stdin = None,
            stdin_isatty = False,
            stdin_encoding = 'abc',
            stdout = None,
            stdout_isatty = False,
            stdout_encoding = 'abc',
            stderr = None,
            stderr_isatty = False,
            colors = 256,
            program_name = 'http'
        )
    assert env.is_windows == False
    assert env.config_dir == 'path of config dir'
    assert env.stdin == None
    assert env.stdin_isatty == False
    assert env.stdin_encoding == 'abc'
    assert env.stdout == None
    assert env.stdout_

# Generated at 2022-06-13 21:40:35.908218
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment(devnull=None, stdin=sys.stdin, 
    stdin_isatty=True, stdin_encoding='utf8', stdout=sys.stdout, 
    stdout_isatty=True, stdout_encoding='ansi', stderr=sys.stdin, 
    stderr_isatty=False, colors=16, program_name='http')
    assert environment.devnull == None
    assert environment.stdin == sys.stdin
    assert environment.stdin_isatty == True
    assert environment.stdin_encoding == 'utf8'
    assert environment.stdout == sys.stdout
    assert environment.stdout_isatty == True
    assert environment.stdout_encoding == 'ansi'
    assert environment.stderr == sys

# Generated at 2022-06-13 21:40:37.564595
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment()

# Generated at 2022-06-13 21:40:48.979346
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(is_windows=False)
    assert env.is_windows is False
    assert env.colors == 256
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty is False
    assert env.stdin_encoding == 'utf8'
    assert env.stdout == sys.stdout
    assert env.stdout_isatty is False
    assert env.stdout_encoding == 'utf8'
    assert env.stderr == sys.stderr
    assert env.stderr_isatty is False
    assert env.program_name == 'http'
    assert env.config_dir == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:41:02.882404
# Unit test for constructor of class Environment
def test_Environment():
    os.environ['HTTPIE_CONFIG_DIR'] = 'test_dir'
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == 'test_dir'
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout_encoding == sys.stdout.encoding
    assert env.stderr_encoding == sys.stderr.encoding
    assert env.std

# Generated at 2022-06-13 21:41:04.492766
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    return env


# Generated at 2022-06-13 21:41:07.042870
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env
    assert isinstance(env, Environment)

# Generated at 2022-06-13 21:41:15.797932
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    env = Environment(
        stdin=sys.stdin, stdin_isatty=True, stdin_encoding=None,
        stdout=sys.stdout, stdout_isatty=True, stdout_encoding=None,
        stderr=sys.stderr, stderr_isatty=True,
        is_windows=is_windows, config_dir=DEFAULT_CONFIG_DIR,
        program_name='http', colors=256
    )
    print(env)
    # http: error: Keyword arguments {'config': None, 'colors': 256, 'stdin_encoding': 'utf-8', 'stdin_isatty': True, 'stdout': <ipykernel.iostream.OutStream object at 0x7f3b3e3af7

# Generated at 2022-06-13 21:41:28.914641
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(is_windows = False,
                      config_dir = Path('./config_dir'),
                      stdin = None,
                      stdin_isatty = False,
                      stdin_encoding = 'utf-8',
                      stdout = sys.stdout,
                      stdout_isatty = True,
                      stdout_encoding = 'utf-8',
                      stderr = sys.stderr,
                      stderr_isatty = True,
                      colors = 256,
                      program_name = 'http')
    assert env.is_windows == False, "test_Environment(): is_windows"
    assert env.config_dir ==  Path('./config_dir'), "test_Environment(): config_dir"
    assert env.stdin == None, "test_Environment(): stdin"

# Generated at 2022-06-13 21:41:32.740615
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(config_dir='/home/httpie/.config')
    assert not env.stdin_isatty
    assert not env.stdout_isatty
    assert env.stderr_isatty
    assert env.colors == 256
    assert env.program_name == 'http'

# Generated at 2022-06-13 21:41:48.446072
# Unit test for constructor of class Environment
def test_Environment():
    """
    The class Environment is defined to hold some config of the system.
    The only property of this class is the config property.
    When the property is called, a new config will be created.
    The create process is done by Config.__init__.
    But the test need to be done in the Constructor.
    Thus, the test of config can only be done in the constructor.
    """
    # Given
    path = mock.patch('httpie.core.main.os', spec=os)
    path.path.exists.return_value = False
    path.path.expanduser.return_value = False

    config_dir = os.path.join(os.path.expanduser('~'), '.httpie')

    # When
    environment = Environment(config_dir=config_dir)

    # Then

# Generated at 2022-06-13 21:41:56.870750
# Unit test for constructor of class Environment
def test_Environment():
    args = {
        'config_dir': DEFAULT_CONFIG_DIR,
        'stdin': sys.stdin,
        'stdin_isatty': sys.stdin.isatty(),
        'stdout': sys.stdout,
        'stdout_isatty': sys.stdout.isatty(),
        'stderr': sys.stderr,
        'stderr_isatty': sys.stderr.isatty(),
        'colors': 256,
        'program_name': 'http',
        'is_windows': sys.platform == 'win32',
        '_devnull': os.devnull,
        '_orig_stderr': sys.stderr,
        'config': Config(directory=DEFAULT_CONFIG_DIR)
    }
    test_case

# Generated at 2022-06-13 21:42:07.222733
# Unit test for constructor of class Environment

# Generated at 2022-06-13 21:42:08.108042
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    print(env)

test_Environment()

# Generated at 2022-06-13 21:42:14.717375
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=None,
                      program_name="http",
                      stdin=sys.stdin,
                      stdin_isatty=False,
                      stdin_encoding="utf8",
                      stdout=sys.stdout,
                      stdout_isatty=False,
                      stdout_encoding="utf8",
                      stderr=sys.stderr,
                      stderr_isatty=False,
                      colors=256,
                      is_windows=False,
                      config_dir=Path('/Users/george/Library/Application Support/httpie'
                                      ))
    assert env.is_windows == False
    assert env.config_dir == Path('/Users/george/Library/Application Support/httpie')
    assert env.stdin == sys.stdin
    assert env.std

# Generated at 2022-06-13 21:42:24.098193
# Unit test for constructor of class Environment
def test_Environment():
    import io
    stdin_key = 'stdin'
    stdout_key = 'stdout'
    stderr_key = 'stderr'
    stdin = io.StringIO()
    stdout = io.StringIO()
    stderr = io.StringIO()
    env = Environment(**{stdin_key: stdin, stdout_key: stdout, stderr_key: stderr})
    assert env.stdin is stdin
    assert env.stdout is stdout
    assert env.stderr is stderr
    assert env.stdout_encoding == 'utf8'

if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:42:33.973573
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=None,
                      is_windows=is_windows,
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
                      program_name='http')
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdout_isatty is True
   

# Generated at 2022-06-13 21:42:44.098728
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(is_windows=True, config_dir=Path('test'),
                      stdin=None, stdout=None, stderr=None, program_name='test')
    assert env.is_windows == True
    assert env.config_dir == Path('test')
    assert env.stdin is None
    assert env.stdout is None
    assert env.stderr is None
    assert env.program_name == 'test'


# Generated at 2022-06-13 21:43:00.243244
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert isinstance(env.stdin, IO), 'stdin should be isatty'
    assert isinstance(env.stdout, IO), 'stdout should be isatty'
    assert isinstance(env.stderr, IO), 'stderr should be isatty'
    assert env.stdin_isatty == sys.stdin.isatty(), 'stdin_isatty'
    assert env.stdout_isatty == sys.stdout.isatty(), 'stdout_isatty'
    assert env.stderr_isatty == sys.stderr.isatty(), 'stderr_isatty'
    assert isinstance(env.config_dir, Path), 'config_dir is Path'

# Generated at 2022-06-13 21:43:08.662091
# Unit test for constructor of class Environment
def test_Environment():
    """
    >>> test_Environment()
    <Environment is_windows=False stdin=<_io.TextIOWrapper
    name='<stdin>' mode='r' encoding='utf8'> stdin_isatty=True
    stdin_encoding='utf8' stdout=<_io.TextIOWrapper name='<stdout>'
    mode='w' encoding='utf8'> stdout_isatty=True stdout_encoding='utf8'
    stderr=<_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf8'>
    stderr_isatty=True colors=256 program_name='http' config=<httpie.config.
    Config>>
    """
    print(Environment())



# Generated at 2022-06-13 21:43:24.748084
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stdin.isatty()
    assert env.stdin_isatty
    assert env.stdout.isatty()
    assert env.stdout_isatty
    assert env.stderr.isatty()
    assert env.stderr_isatty
    assert env.is_windows

# Generated at 2022-06-13 21:43:32.513027
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin=None, stdin_isatty=None, stdin_encoding=None, stdout=None, stdout_isatty=None, stdout_encoding=None, stderr=None, stderr_isatty=None, stderr_encoding=None, config_dir="C:\\Users\\alish\\AppData\\Roaming\\httpie", program_name="http")

# Generated at 2022-06-13 21:43:41.180724
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull = 10, is_windows = True, stdin = sys.stdin, stdin_isatty = False,
                      stdout = sys.stdout, stdin_encoding = 'utf8', stdout_encoding = 'utf8', stderr = sys.stderr,
                      stderr_isatty = True, config_dir = DEFAULT_CONFIG_DIR)
    dict_env = env.__dict__
    assert dict_env['_devnull'] == 10
    assert dict_env['is_windows'] is True
    assert dict_env['stdin'] == sys.stdin
    assert dict_env['stdin_isatty'] is False
    assert dict_env['stdout'] == sys.stdout
    assert dict_env['stdin_encoding'] == 'utf8'


# Generated at 2022-06-13 21:43:52.651427
# Unit test for constructor of class Environment
def test_Environment():
    for kwargs in [
        {},
        {'stdin_isatty': False},
        {'stdout_isatty': False},
        {'stderr_isatty': False},
        {'stdin_isatty': False, 'stdout_isatty': False},
        {'stdin_isatty': False, 'stdout_isatty': False, 'stderr_isatty': False},
        {'stdout_isatty': False, 'stderr_isatty': False},
        {'stdin_isatty': False, 'stderr_isatty': False},
    ]:
        environment = Environment(**kwargs)
        repr(environment)
        assert str(environment) == repr(environment)


# Generated at 2022-06-13 21:44:02.198091
# Unit test for constructor of class Environment
def test_Environment():
    actual = Environment(
        devnull = open(os.devnull, 'w+'),
        stdin = sys.stdin,
        stdin_isatty = False,
        stdin_encoding = None,
        stdout = sys.stdout,
        stdout_isatty = False,
        stdout_encoding = None,
        stderr = sys.stderr,
        stderr_isatty = False,
        colors = 256,
        program_name = 'cmd test'
    )
    # test output
    print(actual)
    print(actual.devnull)
    print(actual.config)
    print(actual._orig_stderr)

# Generated at 2022-06-13 21:44:14.341953
# Unit test for constructor of class Environment
def test_Environment():
    import pprint
    env = Environment(stdin=1, stdout=2, stderr=3)
    env_text = pprint.pformat(env)
    expected_env_text = pprint.pformat(Environment())
    expected_env_text = expected_env_text.replace("'stdin':<_io.TextIOWrapper", "'stdin':1")
    expected_env_text = expected_env_text.replace("stdout':<_io.TextIOWrapper", "stdout':2")
    expected_env_text = expected_env_text.replace("stderr':<_io.TextIOWrapper", "stderr':3")
    assert env_text == expected_env_text


# Generated at 2022-06-13 21:44:15.376703
# Unit test for constructor of class Environment
def test_Environment():
    pass

# Generated at 2022-06-13 21:44:30.808709
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    env.config_dir = "/home/httpie"
    env.stdout = None
    env.stderr = None
    env.stdin = None
    env.stdin_isatty = False
    env.stdin_encoding = "gbk"
    env.stdout_isatty = False
    env.stdout_encoding = "utf-8"
    env.stderr_isatty = False
    env.program_name = "httpie"
    env.colors = 256
    env.is_windows = False
    env.devnull = None
    print(env)

# Generated at 2022-06-13 21:44:34.866986
# Unit test for constructor of class Environment
def test_Environment():
    class Env(Environment):
        x = 1
        y = 2

    env = Env(x=11, y=22)
    assert env.x == 11
    assert env.y == 22

# Generated at 2022-06-13 21:44:47.863811
# Unit test for constructor of class Environment
def test_Environment():
    # Test the constructor of class Environment
    env = Environment(devnull=None, is_windows=True,
                      config_dir=DEFAULT_CONFIG_DIR, stdin=None,
                      stdin_isatty=False, stdin_encoding=None, stdout=sys.stdout,
                      stdout_isatty=sys.stdout.isatty(), stdout_encoding=None,
                      stderr=sys.stderr, stderr_isatty=sys.stderr.isatty(),
                      colors=256, program_name='http')
    assert env.is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin is None
    assert not env.stdin_isatty
    assert env.stdin_encoding is None

# Generated at 2022-06-13 21:45:00.358451
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment()
    assert e.is_windows == is_windows
    assert e.config_dir == Path(DEFAULT_CONFIG_DIR)
    assert e.stderr == sys.stderr
    assert e.stdout_encoding == sys.stdout.encoding
    assert e.stderr_isatty == sys.stderr.isatty()
    assert e.stdout == sys.stdout
    assert e.stdout_isatty == sys.stdout.isatty()
    assert e.stderr_encoding == sys.stderr.encoding
    assert e.stdin == sys.stdin
    assert e.stdin_isatty == sys.stdin.isatty()
    assert e.stdin_encoding == sys.stdin.encoding


# Unit

# Generated at 2022-06-13 21:45:11.976257
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(unwanted_argument=True)
    assert env.unwanted_argument is None
    assert env.is_windows is is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin is sys.stdin
    assert env.stdin_isatty == env.stdin.isatty()
    assert env.stdin_encoding is None
    assert env.stdout is sys.stdout
    assert env.stdout_isatty == env.stdout.isatty()
    assert env.stdout_encoding is None
    assert env.stderr is sys.stderr
    assert env.stderr_isatty == env.stderr.isatty()
    assert env.program_name == 'http'
    assert env.colors

# Generated at 2022-06-13 21:45:20.558332
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.__dict__ == dict(Environment.__dict__)

    env = Environment(foo='bar')
    assert env.__dict__ == dict(Environment.__dict__, foo='bar')

    env = Environment(foo='bar', config_dir='/test/httpie')
    assert env.__dict__ == dict(Environment.__dict__, foo='bar', config_dir='/test/httpie')

    env = Environment(foo='bar', config_dir='/test/httpie', stdin=sys.stdin, stdin_isatty=sys.stdin.isatty())

# Generated at 2022-06-13 21:45:30.182208
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.program_name == 'http'
    if not env.is_windows:
        if curses:
            try:
                curses.setupterm()
                env.colors = curses.tigetnum('colors')
            except curses.error:
                env.colors = 256


# Generated at 2022-06-13 21:45:39.801895
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    import json
    import os
    stdin = sys.stdin
    stdout = sys.stdout
    stderr = sys.stderr
    sys.stdin = open(os.devnull, 'r')
    sys.stdout = open(os.devnull, 'w+')
    sys.stderr = open(os.devnull, 'w+')
    env_test = Environment(devnull=None)
    env_test2 = Environment(devnull=os.devnull,
                            stdout=stdout,
                            stdin=stdin,
                            stderr=stderr)

# Generated at 2022-06-13 21:45:50.263998
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment()

    assert(is_windows == environment.is_windows)
    assert(DEFAULT_CONFIG_DIR == environment.config_dir)
    assert(sys.stdin == environment.stdin)
    assert(False == environment.stdin_isatty)
    assert(env.stdin_encoding == environment.stdin_encoding)
    assert(sys.stdout == environment.stdout)
    assert(False == environment.stdout_isatty)
    assert(env.stdout_encoding == environment.stdout_encoding)
    assert(sys.stderr == environment.stderr)
    assert(False == environment.stderr_isatty)
    assert(256 == environment.colors)
    assert('http' == environment.program_name)

env = Environment()

# Generated at 2022-06-13 21:46:04.909168
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment(
        config_dir='/test/config/dir',
        stdin_isatty=True,
        stdin_encoding='stdin encoding',
        stdout_isatty=True,
        stdout_encoding='stdout encoding',
        stderr_isatty=True,
        program_name='programname',
        colors=256,
    )
    print('Testing the constructor of class Environment !')

# Generated at 2022-06-13 21:46:14.782366
# Unit test for constructor of class Environment
def test_Environment():
    import io
    from httpie.config import BaseConfig
    from pathlib import Path
    from unittest.mock import Mock
    from httpie.utils import JSON_ACCEPT, JSON_CONTENT_TYPE

    mystdin = io.StringIO(JSON_ACCEPT)
    mystdin.encoding = None
    mystdin.isatty = Mock()
    mystdout = io.StringIO('')
    mystdout.encoding = 'ascii'
    mystderr = io.StringIO('')
    mystderr.encoding = 'utf-8'
    myconfig = BaseConfig()


# Generated at 2022-06-13 21:46:23.097470
# Unit test for constructor of class Environment
def test_Environment():
    # this function consists of deliberately redundant code
    env = Environment()
    env2 = Environment(env.is_windows, env.config_dir, env.stdin, env.stdin_isatty, env.stdin_encoding,\
                       env.stdout, env.stdout_isatty, env.stdout_encoding, env.stderr, env.stderr_isatty, env.colors)

test_Environment()

# Generated at 2022-06-13 21:46:33.513445
# Unit test for constructor of class Environment
def test_Environment():
    # 1
    env = Environment()
    print(env.stderr)
    print(env.stderr_isatty)
    print(env.stderr_encoding)
    print(env.stdout)
    print(env.stdout_isatty)
    print(env.stdout_encoding)
    print(env.is_windows)
    print(env.config_dir)
    print(env.stdin)
    print(env.stdin_isatty)
    print(env.stdin_encoding)
    print(env.program_name)
    print(env.colors)
    print(env.devnull)

    # 2
    # env.stderr = 1
    # env.stderr_isatty = 1
    # env.stderr_

# Generated at 2022-06-13 21:46:50.869652
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin = sys.stdin, stdout = sys.stdout, stderr = sys.stderr,
                      config_dir='/tmp/httpie')
    print(env.stdin)
    print(env.stdout)
    print(env.stderr)
    print(env.config_dir)
    #print(env.config.default_options)
    #assert not env.config.default_options
    #print(env.config.dir)
    #assert env.config.dir == '/tmp/httpie'
    print(env.__str__())

# Generated at 2022-06-13 21:46:52.843133
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=1)
    assert 'devnull=1' in repr(env)

# Generated at 2022-06-13 21:46:54.662200
# Unit test for constructor of class Environment
def test_Environment():
    obj = Environment()
    assert isinstance(obj,Environment)

# Generated at 2022-06-13 21:47:06.189744
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment(stdin=None, stdin_isatty=False, stdin_encoding='utf8', stdout=sys.stdout, stdout_isatty=True, stdout_encoding='utf8', stderr=sys.stderr, stderr_isatty=True, colors=256)
    assert not environment.stdin
    assert not environment.stdin_isatty
    assert environment.stdin_encoding == 'utf8'
    assert environment.stdout == sys.stdout
    assert environment.stdout_isatty
    assert environment.stdout_encoding == 'utf8'
    assert environment.stderr == sys.stderr
    assert environment.stderr_isatty
    assert environment.colors == 256
    assert environment.program_name == 'http'


# Generated at 2022-06-13 21:47:08.551826
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env
    assert env.devnull

# Generated at 2022-06-13 21:47:23.829073
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment(
        # Overwrite default values
        config_dir='/config',
        stdin=sys.stdin,
        stdin_isatty=sys.stdin.isatty(),
        stdin_encoding='/stdin_encoding',
        stdout=sys.stdout,
        stdout_isatty=sys.stdout.isatty(),
        stdout_encoding='/stdout_encoding',
        stderr=sys.stderr,
        stderr_isatty=sys.stderr.isatty(),
        colors='/colors',
        program_name='/program_name',
        is_windows='/is_windows'
    )
    #print(Environment.__dict__)
    assert Environment.config_dir == '/config'

# Generated at 2022-06-13 21:47:37.124012
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stderr_isatty
    assert env.stdin_isatty == env.stdin.isatty()

    env.stdin_isatty = True
    assert env.stdin_isatty
    assert env.stderr_isatty == env.stderr.isatty()
    env.stderr_isatty = False
    assert not env.stderr_isatty
    assert env.stdout_isatty == env.stdout.isatty()
    env.stdout_isatty = True
    assert env.stdout_isatty
    assert env.is_windows == is_windows

    env.is_windows = True
    assert env.is_windows is True
    assert env.config_dir == DEFAULT_CONFIG

# Generated at 2022-06-13 21:47:48.792827
# Unit test for constructor of class Environment
def test_Environment():
    from httpie.cli import Environment as environment
    from httpie.config import Config as config
    from sys import stdin
    from sys import stdout
    from sys import stderr
    from os import devnull
    from pathlib import Path
    e = environment()
    assert isinstance(e, environment)
    assert isinstance(e.config, config)
    assert isinstance(e.stdin, stdin)
    assert isinstance(e.stdout, stdout)
    assert isinstance(e.stderr, stderr)
    assert isinstance(e.devnull, devnull)
    assert isinstance(e.config_dir, Path)
    assert e.stdin_isatty
    assert e.stdout_isatty
    assert e.stderr_isatty

# Generated at 2022-06-13 21:47:59.889413
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment(devnull='a')
    assert e.devnull == 'a', e.devnull
    assert e.stdin_encoding == getattr(sys.stdin, 'encoding', None) or 'utf8', e.stdin_encoding
    assert e.stdout_encoding == getattr(sys.stdout, 'encoding', None) or 'utf8', e.stdout_encoding
    assert e.stdin_isatty == sys.stdin.isatty(), e.stdin_isatty
    assert e.stdout_isatty == sys.stdout.isatty(), e.stdout_isatty
    assert e.stderr_isatty == sys.stderr.isatty(), e.stderr_isatty

# Generated at 2022-06-13 21:48:08.620817
# Unit test for constructor of class Environment
def test_Environment():
    import sys

    env = Environment(stdin=None, stdin_encoding="utf8", stdout=sys.stdout,
    stdout_encoding="utf8", stderr=sys.stderr, stderr_encoding=None,
    colors=8, program_name="http", devnull=None)

    assert env.stdin == None
    assert env.stdin_encoding == "utf8"
    assert env.stdout == sys.stdout
    assert env.stdout_encoding == "utf8"
    assert env.stderr == sys.stderr
    assert env.stderr_encoding == None
    assert env.colors == 8
    assert env.program_name == "http"
    assert env.devnull == None

# Generated at 2022-06-13 21:48:27.565861
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin_encoding='abc')
    assert env.stdin_encoding == 'abc'

# Generated at 2022-06-13 21:48:36.512135
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=True)
    assert env.devnull is True
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdin_encoding == 'utf8'
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding == 'utf8'
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.stderr_encoding == 'utf8'

# Generated at 2022-06-13 21:48:45.011481
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    from io import TextIOWrapper
    from httpie.compat import is_windows

    e = Environment()
    assert e.is_windows == is_windows
    assert e.config_dir == Path(DEFAULT_CONFIG_DIR)
    assert e.stdin == sys.stdin
    assert e.stdin_isatty == sys.stdin.isatty()
    if sys.stdin_encoding:
        assert e.stdin_encoding == sys.stdin_encoding
    assert e.stdout == sys.stdout
    assert e.stdout_isatty == sys.stdout.isatty()
    if sys.stdout_encoding:
        assert e.stdout_encoding == sys.stdout_encoding
    assert e.stderr == sys.stder

# Generated at 2022-06-13 21:48:57.361873
# Unit test for constructor of class Environment

# Generated at 2022-06-13 21:49:04.960668
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(is_windows=False, config_dir=DEFAULT_CONFIG_DIR, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
    assert env.is_windows == False and env.config_dir == DEFAULT_CONFIG_DIR and env.stdin == sys.stdin and env.stdout == sys.stdout and env.stderr == sys.stderr

# Generated at 2022-06-13 21:49:14.590680
# Unit test for constructor of class Environment
def test_Environment():    
    #making a mock instance of class Environment
    env1 = Environment(devnull=None)   
    #checking the attributes of the mock instance
    assert(env1.is_windows == is_windows)    
    assert(env1.stdin == sys.stdin)
    assert(env1.stdin_isatty == sys.stdin.isatty())
    assert(env1.stdout == sys.stdout)
    assert(env1.stdout_isatty == sys.stdout.isatty())
    assert(env1.stderr == sys.stderr)
    assert(env1.stderr_isatty == sys.stderr.isatty())
    assert(env1.stdin_encoding is None)
    assert(env1.stdout_encoding is None)
   

# Generated at 2022-06-13 21:49:22.173035
# Unit test for constructor of class Environment
def test_Environment():
    # test for assertion
    try:
        Environment(devnull=0)
        assert False
    except AssertionError:
        assert True
    # test for value of colors
    assert Environment().colors == 256
    # test for value of colors when curses is None
    # import httpie.environment
    # httpie.environment.curses = None
    # e = Environment()
    # assert e.colors == None

# Generated at 2022-06-13 21:49:29.215100
# Unit test for constructor of class Environment
def test_Environment():
    environment=Environment()
    assert environment.stdin == sys.stdin
    assert environment.stdin_encoding == None
    assert environment.stdout == sys.stdout
    assert environment.stdout_encoding == None
    assert environment.stderr == sys.stderr
    assert environment.stderr_isatty == True
    assert environment.program_name == 'http'
    assert environment.colors == 256
    assert environment.config_dir == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:49:37.016722
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment()
    assert isinstance(environment, Environment)
    assert environment.is_windows == False
    assert environment.config_dir == DEFAULT_CONFIG_DIR
    assert environment.stdin == sys.stdin
    assert environment.stdin_isatty == True
    assert environment.stdin_encoding == 'cp950'
    assert environment.stdout == sys.stdout
    assert environment.stdout_isatty == True
    assert environment.stdout_encoding == 'cp950'
    assert environment.stderr == sys.stderr
    assert environment.stderr_isatty == True
    assert environment.colors == 256
    assert environment.program_name == 'http'


# Generated at 2022-06-13 21:49:39.939161
# Unit test for constructor of class Environment
def test_Environment():
	a = Environment(stdout = sys.stdout)
	assert isinstance(a, Environment)
	assert a.stdin == sys.stdin
	assert a.stdin_encoding == 'UTF-8'
	assert a.stdout == sys.stdout
	assert a.stdout_encoding == 'UTF-8'
	assert a.stdout_isatty == True
	assert a.stderr == sys.stderr
	assert a.stderr_isatty == True


# Generated at 2022-06-13 21:50:25.265559
# Unit test for constructor of class Environment