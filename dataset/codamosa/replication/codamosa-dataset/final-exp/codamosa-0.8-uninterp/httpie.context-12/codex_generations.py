

# Generated at 2022-06-13 21:40:19.087734
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stdin_isatty is True
    assert env.stdout_isatty is True
    assert env.stderr_isatty is True
    assert env.colors > 0

# Generated at 2022-06-13 21:40:29.157805
# Unit test for constructor of class Environment
def test_Environment():
    def assert_attr(attr, default):
        value = getattr(env, attr)
        assert value is not default, \
            f'{value!r} is the default for {attr!r}'
    env = Environment()
    assert_attr('config_dir', DEFAULT_CONFIG_DIR)
    assert_attr('stdin', sys.stdin)
    assert_attr('stdin_isatty', sys.stdin.isatty())
    assert_attr('stdin_encoding', None)
    assert_attr('stdout', sys.stdout)
    assert_attr('stdout_isatty', sys.stdout.isatty())
    assert_attr('stdout_encoding', None)
    assert_attr('stderr', sys.stderr)

# Generated at 2022-06-13 21:40:35.437566
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stdin is not None
    assert env.stdin_isatty is True
    assert env.stdin_encoding is not None
    assert env.stdout_isatty is True
    assert env.stdout_encoding is not None
    assert env.stderr_isatty is True
    assert env._orig_stderr is not None
    assert env._devnull is None
    assert env.config_dir.exists()

# Generated at 2022-06-13 21:40:42.302218
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    e = Environment()
    assert e.is_windows == sys.platform.startswith('win')
    assert e.config_dir == DEFAULT_CONFIG_DIR
    assert e.stdin == sys.stdin
    assert e.stdin_isatty == sys.stdin.isatty()
    assert e.stdout == sys.stdout
    assert e.stdout_isatty == sys.stdout.isatty()
    assert e.stderr == sys.stderr
    assert e.stderr_isatty == sys.stderr.isatty()
    assert e.program_name == 'http'

    # Test for overwrite arguments

# Generated at 2022-06-13 21:40:56.038444
# Unit test for constructor of class Environment
def test_Environment():
    stdin = sys.stdin
    stdin_isatty = stdin.isatty() if stdin else False
    stdin_encoding = getattr(stdin, 'encoding', None) or 'utf8'
    stdout = sys.stdout
    stdout_isatty = stdout.isatty()
    stdout_encoding = getattr(stdout, 'encoding', None) or 'utf8'
    stderr = sys.stderr
    stderr_isatty = stderr.isatty()


# Generated at 2022-06-13 21:41:00.487378
# Unit test for constructor of class Environment
def test_Environment():
    import io
    import platform
    if platform.system() == 'Darwin':
        devnull = io.open(os.devnull, 'w+', buffering=0)
    else:
        devnull = os.devnull
    env = Environment(devnull=devnull, program_name='httpie-test')
    assert env.devnull == devnull
    assert env.program_name == 'httpie-test'

# Generated at 2022-06-13 21:41:07.026256
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=1)
    assert env.devnull == 1
    assert env.stdin_encoding=='utf8'
    assert env.stdout_encoding=='utf8'
    assert env.stderr_isatty

    
if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:41:15.798060
# Unit test for constructor of class Environment
def test_Environment():

    stdin = open(os.devnull, 'r')
    stdin.encoding = 'utf-16'
    env = Environment(
        stdin=stdin,
        stdin_encoding=None,
        stdout=open(os.devnull, 'w'),
        stdout_encoding=None,
        stderr=open(os.devnull, 'w'),
        stderr_encoding=None,
        colors=None,
        program_name='httpie',
        config_dir=None,
        is_windows=False
    )
    act_stdout = env.stdout
    act_stderr = env.stderr

    assert env.stdin_isatty is False
    assert env.stdout_isatty is False

# Generated at 2022-06-13 21:41:24.612665
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        devnull = open(os.devnull, 'w+'),
        is_windows = True,
        program_name = 'http',
        stderr = sys.stderr
    )
    print(env.stderr)

if __name__ == "__main__":
    test_Environment()

# Generated at 2022-06-13 21:41:35.546757
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    import os
    import pathlib
    env = Environment(**{'is_windows': is_windows, 'config_dir':DEFAULT_CONFIG_DIR, 'stdin':sys.stdin, 'stdin_isatty':env.stdin.isatty() if env.stdin else False, 'stdin_encoding': getattr(env.stdin, 'encoding', None) or 'utf8', 'stdout':sys.stdout, 'stdout_isatty':env.stdout.isatty(), 'stdout_encoding': getattr(env.stdout, 'encoding', None) or 'utf8', 'stderr':sys.stderr, 'stderr_isatty':env.stderr.isatty(), 'colors':256, 'program_name':'http'})

# Generated at 2022-06-13 21:41:54.873995
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=1, username='test', password='test', 
                      verify = True, cert = 'test', 
                      proxy = 'test', headers = 'test', body = 'test',
                      output_file = True, output_options = 'test',
                      stdin = True, form = True, json = True, stream = True, verbose = True, pretty = True,
                      colors = 256, is_windows = True, config_dir = 'test', stdin_isatty = True, stdin_encoding = 'test',
                      stdout = True, stdout_isatty = True, stdout_encoding = 'test', stderr = True, stderr_isatty = True,
                      program_name = 'test', _config = 'test')
    assert env.username == 'test'

# Generated at 2022-06-13 21:42:11.762849
# Unit test for constructor of class Environment
def test_Environment():
    environ = Environment(
            is_windows=False,
            config_dir=DEFAULT_CONFIG_DIR,
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
    )
    assert environ.is_windows == False
    assert environ.config_dir == DEFAULT_CONFIG_DIR
    assert environ.stdin == None
    assert environ.stdin_isatty == False
    assert environ.stdin_encoding == 'utf8'


# Generated at 2022-06-13 21:42:16.130329
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(is_windows=True, config_dir=Path("/test/test/test"))
    assert env.is_windows is True
    assert env.config_dir == Path("/test/test/test")



# Generated at 2022-06-13 21:42:20.292617
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=sys.stdin, program_name='http', colors=256)
    assert env._devnull is sys.stdin
    assert env.program_name == 'http'
    assert env.colors == 256

# Generated at 2022-06-13 21:42:22.497171
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment()
    assert e.stdin_encoding is not None
    assert e.stdout_encoding is not None

# Generated at 2022-06-13 21:42:33.186328
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    import os
    from pathlib import Path

    env = Environment()
    assert env.is_windows == os.name == 'nt'

    # stdin
    assert isinstance(env.stdin, sys.stdin.__class__)
    assert env.stdin_isatty == sys.stdin.isatty()

    # stdout
    assert isinstance(env.stdout, sys.stdout.__class__)
    assert env.stdout_isatty == sys.stdout.isatty()

    # stderr
    assert isinstance(env.stderr, sys.stderr.__class__)
    assert env.stderr_isatty == sys.stderr.isatty()



# Generated at 2022-06-13 21:42:47.041090
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

# Generated at 2022-06-13 21:42:51.038214
# Unit test for constructor of class Environment
def test_Environment():
    import io

    env = Environment(config_dir='/some/dir',
                      stdin=io.StringIO(),
                      stdout=io.StringIO(),
                      stderr=io.StringIO())
    assert env.config_dir == '/some/dir'

# Generated at 2022-06-13 21:43:02.432992
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin = sys.stderr, stdin_isatty = False,
                      stdin_encoding = '', stdout = sys.stdin,
                      stdout_isatty = True, stdout_encoding = '',
                      stderr = sys.stdout, stderr_isatty = False,
                      colors = 0, program_name = 'echo', devnull = os.null)
    res = env.__str__()

# Generated at 2022-06-13 21:43:11.236059
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stdout_encoding is not None
    stdin, stdout, stderr = sys.stdin, sys.stdout, sys.stderr
    # Clear sys.stderr to a temporary "devnull" stdout stream
    sys.stderr = sys.stdout
    try:
        # Throw exception to see if log_error() works
        env.log_error('my_message')
        # Add parenthesis for print() function to work, hence "my_message" gets printed to the console
        assert env.stderr.getvalue() == '\nhttp: error: my_message\n\n'
    finally:
        # Restore stderr back
        sys.stderr = stderr
        sys.stdin, sys.stdout, sys.stderr = std

# Generated at 2022-06-13 21:43:25.001039
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=None, stdout=sys.stdout)
    assert isinstance(env, Environment)
    from pprint import pprint
    pprint(env)


if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:43:30.128353
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        config_dir='/config_dir',
        stdin='stdin',
        stdout='stdout',
        stderr='stderr',
    )
    assert env.config_dir == '/config_dir'
    assert env.stdin == 'stdin'
    assert env.stdout == 'stdout'
    assert env.stderr == 'stderr'
    assert env.config

# Generated at 2022-06-13 21:43:39.888937
# Unit test for constructor of class Environment

# Generated at 2022-06-13 21:43:46.736958
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull='devnull', is_windows=False, config_dir='/home')
    env.devnull = None
    assert env.devnull is None
    assert env.is_windows == False
    assert env.config_dir == '/home'
    # Test if the private member _config can be accessed
    assert env._config == None
    # Test if the private member devnull can be accessed
    assert env._devnull == None
    assert env.stdin != None
    assert env.stdin_isatty == False
    assert env.stdin_encoding == 'utf8'
    assert env.stdout != None
    assert env.stdout_isatty == False
    assert env.stdout_encoding == 'utf8'
    assert env.stderr != None
    assert env.stderr_

# Generated at 2022-06-13 21:43:53.419922
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        stdin=True,
        stdin_isatty=True,
        stdin_encoding='utf8',
        stdout=True,
        stdout_isatty=True,
        stdout_encoding='utf8',
        stderr=True,
        stderr_isatty=True,
        colors=256,
        program_name='http',
    )
    print(env)
    assert Environment().__dict__ == env.__dict__
    assert 'config_dir' not in env.__dict__.keys()

if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:44:04.273644
# Unit test for constructor of class Environment

# Generated at 2022-06-13 21:44:16.787582
# Unit test for constructor of class Environment
def test_Environment():
    from httpie.client import Environment
    from httpie.config import Config

# Generated at 2022-06-13 21:44:33.170651
# Unit test for constructor of class Environment
def test_Environment():
    # construct an `Environment` instance with these keyword arguments.
    env = Environment(is_windows=False, stdin=None)

    # it is an instance of class `Environment`.
    assert isinstance(env, Environment)
    # and it has all the class attributes.
    assert hasattr(env, 'is_windows')
    assert hasattr(env, 'config_dir')
    assert hasattr(env, 'stdin')
    assert hasattr(env, 'stdin_isatty')
    assert hasattr(env, 'stdin_encoding')
    assert hasattr(env, 'stdout')
    assert hasattr(env, 'stdout_isatty')
    assert hasattr(env, 'stdout_encoding')
    assert hasattr(env, 'stderr')

# Generated at 2022-06-13 21:44:39.138160
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=None, **{'stdin_encoding': 'stdin_encoding'})
    assert env.devnull == None
    assert env.stdin_encoding == 'stdin_encoding'
    assert env.stderr == sys.stderr
    env = Environment(**{'devnull': 1, 'stderr': 2},)
    assert env.devnull == 1
    assert env.stderr == 2

# Generated at 2022-06-13 21:44:49.982350
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        devnull='/dev/null',
        stdin=None,
        stdout=sys.stdout,
        stderr=sys.stderr
    )
    def check(attr, value):
        assert getattr(env, attr) == value
    check('devnull', '/dev/null')
    check('stdin', None)
    check('stdin_isatty', False)
    check('stdout', sys.stdout)
    check('stdout_isatty', sys.stdout.isatty())
    check('stdin_encoding', None)
    check('stderr', sys.stderr)
    check('stderr_isatty', sys.stderr.isatty())

# Generated at 2022-06-13 21:45:01.720681
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    import sys
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.stdin == sys.stdin

# Generated at 2022-06-13 21:45:07.379326
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name='httpie')
    assert env.program_name == 'httpie'
    assert env.stdout_encoding == 'utf8'
    assert env.stderr == sys.stderr
    assert env.stdin == sys.stdin
    assert env.stdin_encoding == 'utf8'

# Generated at 2022-06-13 21:45:15.779008
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.program_name == 'http'
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr

    new_env = Environment(program_name='haha', stdin='hehe')
    assert new_env.program_name == 'haha'
    assert new_env.stdin == 'hehe'
    assert new_env.stdout == sys.stdout
    assert new_env.stderr == sys.stderr

# Generated at 2022-06-13 21:45:18.706968
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout=None, stdin=None)
    assert env.stdout == None
    assert env.stdin == None

# Generated at 2022-06-13 21:45:26.701604
# Unit test for constructor of class Environment
def test_Environment():
    env1 = Environment()
    assert env1.config_dir == DEFAULT_CONFIG_DIR
    assert env1.stdin == sys.stdin
    assert env1.stdin_isatty == True
    assert env1.stdin_encoding == 'utf8'
    assert env1.stdout == sys.stdout
    assert env1.stdout_isatty == True
    assert env1.stdout_encoding == 'utf8'
    assert env1.stderr == sys.stderr
    assert env1.stderr_isatty == True
    assert env1.colors == 256

# Generated at 2022-06-13 21:45:37.482246
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdin_encoding == sys.stdin.encoding or None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding == sys.stdout.encoding or None
    if is_windows:
        assert env.colors == curses.tigetnum('colors')
    assert env.program_name == 'http'
    assert env.log_error(msg='hello world', level='error') == None

# Generated at 2022-06-13 21:45:51.871230
# Unit test for constructor of class Environment
def test_Environment():
    def assert_environment(env, **expected):
        assert env.__dict__ == expected

    env = Environment()

    assert_environment(env,
        is_windows=is_windows,
        config_dir=DEFAULT_CONFIG_DIR,
        stdin=sys.stdin,
        stdin_isatty=sys.stdin.isatty(),
        stdin_encoding=sys.stdin.encoding,
        stdout=sys.stdout,
        stdout_isatty=sys.stdout.isatty(),
        stdout_encoding=sys.stdout.encoding,
        stderr=sys.stderr,
        stderr_isatty=sys.stderr.isatty(),
        colors=256,
        program_name='http'
    )

    #

# Generated at 2022-06-13 21:45:57.315306
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment().stdout_isatty
    assert Environment(stdout_isatty=True).stdout_isatty
    assert not Environment(stdout_isatty=False).stdout_isatty

# Generated at 2022-06-13 21:46:10.493657
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=None,
                      is_windows=True,
                      config_dir='~/.httpie/',
                      stdin=None,
                      stdin_isatty=False,
                      stdin_encoding=None,
                      stdout=None,
                      stdout_isatty=False,
                      stdout_encoding=None,
                      stderr=None,
                      stderr_isatty=False,
                      colors=256,
                      program_name='http')

# Generated at 2022-06-13 21:46:13.151019
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment.stdin.read() == sys.stdin.read()


env = Environment()

# Generated at 2022-06-13 21:46:39.248658
# Unit test for constructor of class Environment
def test_Environment():
    try:
        import colorama
        colorama.initialise.wrap_stream(
                sys.stdout, convert=None, strip=None,
                autoreset=True, wrap=True
        )
        del colorama
    except:
        pass
    env = Environment()
    assert env.is_windows == is_windows
    assert env.stdin_isatty == env.stdin.isatty()
    assert env.stdout_isatty == env.stdout.isatty()
    assert env.stderr_isatty == env.stderr.isatty()
    assert env.stdin_encoding is not None
    assert env.stdout_encoding is not None
    assert env.program_name == 'http'
    assert env.stdin == sys.stdin

# Generated at 2022-06-13 21:46:51.988314
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        program_name = "http",
        stdin = sys.stdin,
        stdin_isatty = sys.stdin.isatty(),
        stdout = sys.stdout,
        stdout_isatty = sys.stdout.isatty(),
        stderr = sys.stderr,
        stderr_isatty = sys.stderr.isatty()
    )
    assert env.program_name == 'http'
    assert env.stdin is sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout is sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr is sys.stderr
   

# Generated at 2022-06-13 21:47:00.206001
# Unit test for constructor of class Environment
def test_Environment():
    stdout, stderr, stdin = sys.stdout, sys.stderr, sys.stdin
    if not is_windows:
        if curses:
            try:
                curses.setupterm()
                colors = curses.tigetnum('colors')
            except curses.error:
                pass
    else:
        # noinspection PyUnresolvedReferences
        import colorama.initialise
        stdout = colorama.initialise.wrap_stream(
            stdout, convert=None, strip=None,
            autoreset=True, wrap=True
        )
        stderr = colorama.initialise.wrap_stream(
            stderr, convert=None, strip=None,
            autoreset=True, wrap=True
        )
        del colorama
        print(stderr,stdout)

# Generated at 2022-06-13 21:47:05.267764
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(foo=1, baz='2')
    print(env)
    assert env.foo == 1
    assert env.baz == '2'
    assert not hasattr(env, 'bar')

# Generated at 2022-06-13 21:47:17.489410
# Unit test for constructor of class Environment
def test_Environment():
    # 这个主要是看能不能把sys.stdin赋值给self.stdin，能就返回
    assert Environment().stdin == sys.stdin
    for attr in ('stdout', 'stderr'):
        assert getattr(Environment(), attr) == getattr(sys, attr)
    # 如果不是就返回None
    assert Environment(stdin=None).stdin is None
    # 如果不等于则赋值并且返回
    env = Environment(stdin=object(), stdout=object(), stderr=object())
    assert env.stdin is not sys.stdin

# Generated at 2022-06-13 21:47:25.934931
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=None, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, program_name="http")
    assert env.is_windows == False
    assert env.config_dir == Path("~/.httpie").expanduser()
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.program_name == "http"
    assert env.devnull == None


# Generated at 2022-06-13 21:47:36.448423
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert isinstance(env.is_windows, bool)
    assert env.is_windows == is_windows
    assert isinstance(env.config_dir, Path)
    assert env.config_dir == Path(DEFAULT_CONFIG_DIR)
    assert isinstance(env.stdin, IO)
    assert env.stdin == sys.stdin
    assert isinstance(env.stdin_isatty, bool)
    assert env.stdin_isatty == env.stdin.isatty()
    assert isinstance(env.stdin_encoding, str)
    assert env.stdin_encoding == 'utf8'
    assert isinstance(env.stdout, IO)
    assert env.stdout == sys.stdout

# Generated at 2022-06-13 21:47:46.723617
# Unit test for constructor of class Environment
def test_Environment():
    environ = Environment()
    assert environ.is_windows == is_windows
    assert environ.config_dir == DEFAULT_CONFIG_DIR
    assert environ.stdin == sys.stdin
    assert environ.stdin_isatty == environ.stdin.isatty()
    assert environ.stdout_isatty == environ.stdout.isatty()
    assert environ.stderr_isatty == environ.stderr.isatty()
    assert environ.program_name == 'http'

    # Test constructor with devnull argument
    environ = Environment(devnull=sys.stdout)
    assert environ.devnull == sys.stdout

# Generated at 2022-06-13 21:47:55.470574
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment()
    assert type(e) == Environment
    assert e.is_windows == is_windows
    assert e.config_dir == DEFAULT_CONFIG_DIR
    assert e.stdin == sys.stdin
    assert e.stdin_isatty == sys.stdin.isatty() 
    assert e.stdout == sys.stdout
    assert e.stdout_isatty == sys.stdout.isatty()
    assert e.stderr == sys.stderr
    assert e.stderr_isatty == sys.stderr.isatty()
    assert e.colors == 256
    assert e.program_name == 'http'
    assert e.config == Config(directory=DEFAULT_CONFIG_DIR)
    # assert e.devnull == e.devnull

# Generated at 2022-06-13 21:47:58.150835
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull = '', colors = 256)
    assert env.devnull == ''

# Generated at 2022-06-13 21:48:55.968294
# Unit test for constructor of class Environment
def test_Environment():
    # normal case
    ENV = Environment()
    assert ENV.is_windows == is_windows
    assert ENV.stdin == sys.stdin
    assert ENV.stdout == sys.stdout
    assert ENV.stderr == sys.stderr
    assert ENV.config_dir == DEFAULT_CONFIG_DIR
    assert ENV.stdin_isatty == sys.stdin.isatty() if sys.stdin else False
    assert ENV.stdout_isatty == sys.stdout.isatty()
    assert ENV.stderr_isatty == sys.stderr.isatty()
    assert ENV.colors == 256
    assert ENV.program_name == 'http'
    assert ENV.stdin_encoding == None

# Generated at 2022-06-13 21:49:00.724561
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout_encoding='utf8')
    assert env.stdout_encoding == 'utf8'
    assert env.stdin_encoding == 'utf8'
    assert env.stderr_isatty == True

# Generated at 2022-06-13 21:49:13.331436
# Unit test for constructor of class Environment
def test_Environment():
    print("Testing Environment...")
    import httpie.utils
    env = Environment()
    assert env._orig_stderr == sys.stderr
    assert env._devnull is None
    assert env.stderr == sys.stderr
    assert env.stdout == sys.stdout
    assert env.stdin == sys.stdin
    assert env.is_windows == httpie.utils.is_windows
    assert env.config_dir == httpie.compat.DEFAULT_CONFIG_DIR
    assert env.program_name == 'http'
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.stdout_isatty == sys.stdout.isat

# Generated at 2022-06-13 21:49:20.652314
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout_isatty=False, stdout_encoding='latin1',
                      stderr_isatty=False, stderr_encoding='latin1',
                      program_name='http', config_dir=DEFAULT_CONFIG_DIR)
    assert env.stdout_isatty == False
    assert env.stdout_encoding == 'latin1'
    assert env.stderr_isatty == False
    assert env.stderr_encoding == 'latin1'
    assert env.program_name == 'http'
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env._orig_stderr == sys.stderr
    assert env._devnull == None


# Generated at 2022-06-13 21:49:23.997796
# Unit test for constructor of class Environment
def test_Environment():
    out = Environment(stdout=None)
    assert out.stdout is None

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 21:49:28.886129
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=True, config_dir = '/', stdout_isatty=True)
    assert env.devnull
    assert env.stdin
    assert env.stdout
    assert env.stderr
    assert env.config_dir == '/'
    assert env.stdout_isatty

# Generated at 2022-06-13 21:49:38.271908
# Unit test for constructor of class Environment
def test_Environment():
    # If this unit test fails,
    # then the class Environment has changed in a way that makes it
    # incompatible with the `with` statement.

    import contextlib
    from tempfile import TemporaryFile

    with TemporaryFile('w', encoding='utf8') as temp_stdin:
        with TemporaryFile('w', encoding='utf8') as temp_stdout:
            with TemporaryFile('w', encoding='utf8') as temp_stderr:
                class CustomEnvironment(Environment):
                    pass


# Generated at 2022-06-13 21:49:43.244844
# Unit test for constructor of class Environment
def test_Environment():
    is_windows: bool = True
    config_dir: str = '0'
    stdin: str = '1'
    stdin_isatty: bool = True
    stdin_encoding: str = 'utf8'
    stdout: str = '2'
    stdout_isatty: bool = True
    stdout_encoding: str = 'utf8'
    stderr: str = '3'
    stderr_isatty: bool = True
    colors = 256
    program_name: str = 'http'


# Generated at 2022-06-13 21:49:48.349016
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        config_dir='config_dir',
        stdin='stdin',
        stdout='stdout',
        stderr='stderr'
    )
    assert env.config_dir == 'config_dir'
    assert env.stdin == 'stdin'
    assert env.stdout == 'stdout'
    assert env.stderr == 'stderr'


# Generated at 2022-06-13 21:50:04.450885
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment()
    assert e.is_windows == is_windows
    assert e.config_dir == DEFAULT_CONFIG_DIR
    assert e.stdin == sys.stdin
    assert e.stdin_isatty == sys.stdin.isatty()
    assert e.stdin_encoding == sys.stdin.encoding
    assert e.stdout == sys.stdout
    assert e.stdout_isatty == sys.stdout.isatty()
    assert e.stdout_encoding == sys.stdout.encoding
    assert e.stderr == sys.stderr
    assert e.stderr_isatty == sys.stderr.isatty()
    assert e.colors == 256
    assert e.program_name == 'http'
