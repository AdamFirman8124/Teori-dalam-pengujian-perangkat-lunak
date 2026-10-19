

# Generated at 2022-06-13 21:40:28.303324
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(colors=7)
    assert env.colors == 7
    env = Environment(config_dir = DEFAULT_CONFIG_DIR, colors = 7)
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.colors == 7
    env = Environment(is_windows = True)
    assert env.is_windows == True
    env = Environment(stdin = sys.stdin)
    assert env.stdin == sys.stdin
    env = Environment(stdin_isatty = False)
    assert env.stdin_isatty == False
    env = Environment(stdin_encoding = None)
    assert env.stdin_encoding == None
    env = Environment(stdout = sys.stdout)
    assert env.stdout == sys.stdout
    env = Environment

# Generated at 2022-06-13 21:40:34.081830
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(asdf=1, qwer='123')
    assert env.asdf == 1
    assert env.qwer == '123'
    assert not hasattr(env, 'is_windows')
    assert not hasattr(env, 'config_dir')
    assert not hasattr(env, 'program_name')
    assert not hasattr(env, 'stdin')


# Generated at 2022-06-13 21:40:41.348056
# Unit test for constructor of class Environment
def test_Environment():
        import os
        import sys
        from httpie.compat import is_windows
        from httpie.config import DEFAULT_CONFIG_DIR, Config, ConfigFileError
        from httpie.config import ConfigFileError
        from httpie.utils import repr_dict
        from httpie import __version__ as httpie_version
        from collections import OrderedDict
        from httpie import output

        environ = Environment()
        # print(environ.is_windows)
        # print(environ.stdin)
        # print(environ.stdin_isatty)
        # print(environ.stdin_encoding)
        # print(environ.stdout)
        # print(environ.stdout_isatty)
        # print(environ.stdout_encoding)
        # print(environ.

# Generated at 2022-06-13 21:40:54.670922
# Unit test for constructor of class Environment
def test_Environment():
    import tempfile
    import shutil
    from httpie.config import DEFAULT_CONFIG_DIR as default_config_dir
    from httpie.compat import is_windows as is_windows

    # save the original value of is_windows
    original_is_windows = is_windows

    # start the test
    tempdir = tempfile.mkdtemp()

# Generated at 2022-06-13 21:40:56.955628
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment(devnull = '123')
    assert environment.devnull == '123'

if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:41:08.743605
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(colors=2)

# Generated at 2022-06-13 21:41:15.356506
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    print(env)
    assert env.is_windows == True
    assert env.config_dir == '/home/travis/.config/httpie'
    assert env.stdin.readable() == True
    assert env.stdin_isatty == True
    assert env.stdin_encoding == 'utf-8'
    assert env.stdout_isatty == True
    assert env.stdout_encoding == 'utf-8'
    assert env.stderr_isatty == True
    assert env.colors == 256
    assert env.program_name == 'http'
    assert env.config is not None

# Generated at 2022-06-13 21:41:28.061988
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    import httpie

    env = Environment(stdout=sys.stdout, program_name="http", config_dir="./")
    assert env.stdout == sys.stdout
    assert env.program_name == "http"
    assert env.config_dir == "./"
    assert env.stdin_isatty == False
    assert env.stdout_isatty == True
    assert env.stderr_isatty == True
    assert env.config_dir == "./"
    assert env.config._dir == "./"
    assert env.config.config_dir == "./"

if __name__ == "__main__":
    test_Environment()

# Generated at 2022-06-13 21:41:30.178710
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    print(env)

test_Environment()

# Generated at 2022-06-13 21:41:32.638548
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment().is_windows == sys.platform == 'win32'

# Generated at 2022-06-13 21:41:48.224502
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == env.stdin.isatty() if env.stdin else False
    assert env.stdin_encoding is None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == env.stdout.isatty()
    assert env.stdout_encoding is None
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == env.stderr.isatty()
    assert env.program_name == 'http'
    assert env.colors == 256

# Generated at 2022-06-13 21:41:50.895585
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin_encoding='', stdin=None)
    print(env)
    assert env.stdin_encoding == ''
    assert not env.stdin_isatty

# Generated at 2022-06-13 21:42:00.590922
# Unit test for constructor of class Environment
def test_Environment():
    # Function to test Environment class
    e = Environment(devnull=None, stdin=sys.stdin, stdin_isatty=True, stdout=sys.stdout, stdout_isatty=True, stderr=sys.stderr, stderr_isatty=True, colors=256, program_name='http')

# Generated at 2022-06-13 21:42:02.278692
# Unit test for constructor of class Environment
def test_Environment():
    print(Environment())

# Generated at 2022-06-13 21:42:06.239697
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout=object(), stderr=object())
    assert env.__dict__ != Environment().__dict__
    assert isinstance(env.config, Config)
    assert env.stdout != sys.stdout
    assert env.stderr != sys.stderr
    assert '<Environment ' in repr(env)
    assert str(env).startswith('{')

if __name__ == "__main__":
    test_Environment()

# Generated at 2022-06-13 21:42:14.318493
# Unit test for constructor of class Environment
def test_Environment():
    temp = Environment()
    e = Environment(temp.config_dir,
                    temp.stdin,
                    temp.stdin_isatty,
                    temp.stdin_encoding,
                    temp.stderr,
                    temp.stderr_isatty,
                    temp.stdout,
                    temp.stdout_isatty,
                    temp.stdout_encoding,
                    temp.program_name,
                    temp.is_windows,
                    temp.colors)

# Generated at 2022-06-13 21:42:15.842108
# Unit test for constructor of class Environment
def test_Environment():
    Environment(program_name='http', colors=256)

# Generated at 2022-06-13 21:42:20.448816
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=None, **{'stdin': sys.stdin, 'stdout': sys.stdout, 'stderr': sys.stderr})
    print(env)

if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:42:25.145518
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr_isatty == sys.stderr.isatty()
    print()



# Generated at 2022-06-13 21:42:27.730131
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stderr=None)
    assert env.stderr is None


# Generated at 2022-06-13 21:42:48.986868
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert type(env.is_windows) == bool
    assert type(env.config_dir) == PosixPath
    assert type(env.stdin) == TextIOWrapper
    assert type(env.stdin_isatty) == bool
    assert type(env.stdin_encoding) == str
    assert type(env.stdout) == TextIOWrapper
    assert type(env.stdout_isatty) == bool
    assert type(env.stdout_encoding) == str
    assert type(env.stderr) == TextIOWrapper
    assert type(env.stderr_isatty) == bool
    assert type(env.colors) == int
    assert type(env.program_name) == str
    assert type(env) == Environment
    assert type

# Generated at 2022-06-13 21:42:51.139477
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment().stdout == sys.stdout

# Generated at 2022-06-13 21:43:02.527540
# Unit test for constructor of class Environment

# Generated at 2022-06-13 21:43:13.148998
# Unit test for constructor of class Environment
def test_Environment():
    import mock
    e = Environment(devnull=True, stdout=False, stderr=False,
                    stdin=False, stdout_isatty=False, stdout_encoding=False,
                    stderr_isatty=False, stderr_encoding=False,
                    colors=False, program_name=False)
    assert e.devnull == True
    assert e.stdout == False
    assert e.stderr == False
    assert e.stdin == False
    assert e.stdout_isatty == False
    assert e.stdout_encoding == False
    assert e.stderr_isatty == False
    assert e.stderr_encoding == False
    assert e.colors == False
    assert e.program_name == False



# Generated at 2022-06-13 21:43:25.683958
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        config_dir=Path('some/dir'),
        stdin=None,
        stdin_isatty=True,
        stdin_encoding='iso-8859',
        stdout=None,
        stdout_isatty=True,
        stdout_encoding='ascii',
        stderr=None,
        stderr_isatty=True
    )
    assert env.config_dir == Path('some/dir')
    assert env.stdin is None
    assert env.stdin_isatty is True
    assert env.stdin_encoding == 'iso-8859'
    assert env.stdout is None
    assert env.stdout_isatty is True
    assert env.stdout_encoding == 'ascii'
    assert env.stder

# Generated at 2022-06-13 21:43:32.833769
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name='test')
    assert env._orig_stderr == sys.stderr
    assert env._devnull is None
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

# Generated at 2022-06-13 21:43:41.316092
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    summary = {'is_windows': env.is_windows, 'config_dir': env.config_dir, 'stdin': env.stdin, 'stdin_isatty': env.stdin_isatty,
               'stdin_encoding': env.stdin_encoding, 'stdout': env.stdout, 'stdout_isatty': env.stdout_isatty, 'stdout_encoding': env.stdout_encoding,
               'stderr': env.stderr, 'stderr_isatty': env.stderr, 'stderr_encoding': env.stderr_encoding, 'colors': env.colors, 'program_name': env.program_name}

# Generated at 2022-06-13 21:43:52.724310
# Unit test for constructor of class Environment
def test_Environment():
    """
    Unit test for constructor of class Environment.
    """

    # Test for constructor of class Environment
    env1 = Environment()
    assert str(env1) == '<Environment {\'config_dir\': Path(~/.config/httpie), \'stdin_isatty\': True, \'stdout_isatty\': True, \'stderr_isatty\': True, \'colors\': 256, \'program_name\': \'http\'}>'


# Generated at 2022-06-13 21:44:03.790795
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment.devnull is None
    assert Environment.config_dir == DEFAULT_CONFIG_DIR
    assert Environment.stdin == sys.stdin
    assert Environment.stdin_isatty == sys.stdin.isatty()
    assert Environment.stdin_encoding == None
    assert Environment.stdout == sys.stdout
    assert Environment.stdout_isatty == sys.stdout.isatty()
    assert Environment.stdout_encoding == None
    assert Environment.stderr == sys.stderr
    assert Environment.stderr_isatty == sys.stderr.isatty()
    assert Environment.program_name == 'http'

# Generated at 2022-06-13 21:44:08.515244
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    # 打印类属性
    print(env)
    # colors, config_dir, is_windows, program_name, stderr, stderr_isatty, stderr_encoding, stdout, stdout_isatty, stdout_encoding, stdin, stdin_isatty, stdin_encoding


if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:44:27.643425
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    env.STDIN_ISATTY = False
    env.CONFIG_DIR = Path('/test')
    assert env.STDIN_ISATTY == False
    assert env.CONFIG_DIR == Path('/test')


# Generated at 2022-06-13 21:44:33.239572
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        colors=2,
        stdin_encoding=None,
        stdout_encoding='stdout_encoding',
        stderr_encoding=None,
    )
    assert env.colors == 2
    assert env.stdin_encoding is None
    assert env.stdout_encoding == 'stdout_encoding'
    assert env.stderr_encoding is None

# Generated at 2022-06-13 21:44:42.363362
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == Path(DEFAULT_CONFIG_DIR)
    assert env.stdin is sys.stdin
    assert env.stdin_isatty == env.stdin.isatty()
    assert env.stdin_encoding == getattr(env.stdin, 'encoding', None)
    assert env.stdout is sys.stdout
    assert env.stdout_isatty == env.stdout.isatty()
    assert env.stdout_encoding == getattr(env.stdout, 'encoding', None)
    assert env.stderr is sys.stderr
    assert env.stderr_isatty == env.stderr.isatty()

# Generated at 2022-06-13 21:44:54.064979
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    import os
    from pathlib import Path
    from typing import IO, Optional

    try:
        import curses
    except ImportError:
        curses = None  # Compiled w/o curses
    
    from httpie.compat import is_windows
    from httpie.config import DEFAULT_CONFIG_DIR
    from httpie.utils import repr_dict
    
    class Environment:
        """
        Information about the execution context
        (standard streams, config directory, etc).

        By default, it represents the actual environment.
        All of the attributes can be overwritten though, which
        is used by the test suite to simulate various scenarios.

        """
        
        is_windows: bool = is_windows
        config_dir: Path = DEFAULT_CONFIG_DIR
        stdin: Optional[IO] = sys.stdin

# Generated at 2022-06-13 21:44:58.753473
# Unit test for constructor of class Environment
def test_Environment():
    stdin = sys.stdin
    stdout = sys.stdout
    stderr = sys.stderr
    env = Environment(stdin, stdout, stderr)
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr

# Generated at 2022-06-13 21:45:03.703288
# Unit test for constructor of class Environment
def test_Environment():
    en = Environment()
    assert en.stdout_isatty
    assert en.stdin_isatty
    assert en.stderr_isatty

    en = Environment(stdout=None, stdin=None, stderr=None)
    assert en.stdout_isatty == False
    assert en.stdin_isatty == False
    assert en.stderr_isatty == False


if __name__ == "__main__":
    test_Environment()

# Generated at 2022-06-13 21:45:06.206390
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout_isatty=None)
    assert isinstance(env.stderr, sys.stderr.__class__)
    assert isinstance(env.stdout, sys.stdout.__class__)
    assert isinstance(env.stdin, sys.stdin.__class__)



# Generated at 2022-06-13 21:45:11.051367
# Unit test for constructor of class Environment
def test_Environment():

    # True
    (Environment().is_windows)
    (Environment().config_dir)
    (Environment().stdin)
    (Environment().stdin_isatty)
    (Environment().stdin_encoding)
    (Environment().stdout)
    (Environment().stdout_isatty)
    (Environment().stdout_encoding)
    (Environment().stderr)
    (Environment().stderr_isatty)
    (Environment().colors)
    (Environment().program_name)

    # False
    not Environment().config
    not Environment().devnull
    not Environment()._orig_stderr
    not Environment()._devnull

# Generated at 2022-06-13 21:45:17.788472
# Unit test for constructor of class Environment
def test_Environment():
    en = Environment(program_name='http')
    assert (en.program_name == 'http')
    assert (en.devnull == None)
    assert (en._orig_stderr == sys.stderr)
    assert (en._config == None)
    en.config_dir = 'test_dir'
    assert (en.config_dir == 'test_dir')
    assert (en.config != None)
    assert (en.config.directory != None)


# Generated at 2022-06-13 21:45:19.620791
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    print(env)

# Generated at 2022-06-13 21:45:43.535699
# Unit test for constructor of class Environment
def test_Environment():
    # Unit test for constructor of class Environment
    env = Environment(stdin=None, stdin_isatty=False, stdin_encoding='utf8',
                      stdout=sys.stdout, stdout_isatty=True, stdout_encoding='utf8',
                      stderr=sys.stderr, stderr_isatty=True, colors=256, program_name='http')
    assert hasattr(env, 'is_windows')
    assert hasattr(env, 'config_dir')
    assert hasattr(env, 'stdin')
    assert hasattr(env, 'stdin_isatty')
    assert hasattr(env, 'stdin_encoding')
    assert hasattr(env, 'stdout')
    assert hasattr(env, 'stdout_isatty')
    assert has

# Generated at 2022-06-13 21:45:55.554319
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment(colors=256, program_name="http")
    if e.stdout.encoding is not None:
       e.stdout_encoding = e.stdout.encoding
    assert e.is_windows == is_windows
    assert e.config_dir == DEFAULT_CONFIG_DIR
    assert e.stdin == sys.stdin
    assert e.stdin_isatty == sys.stdin.isatty()
    assert e.stdin_encoding == e.stdout_encoding
    assert e.stdout == sys.stdout
    assert e.stdout_isatty == sys.stdout.isatty()
    assert e.stdout_encoding == e.stdout_encoding
    assert e.stderr == sys.stderr
    assert e.stderr

# Generated at 2022-06-13 21:45:57.235293
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=True)
    assert '{' in str(env)

# Generated at 2022-06-13 21:46:02.856613
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin_encoding='changed')
    assert env.stdin_encoding == 'changed'
    # If the keyword argument is not in __init__'s argument list
    try:
        env = Environment(djd='jfjdfdf')
    except AssertionError:
        pass

# Generated at 2022-06-13 21:46:14.308023
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment()
    assert environment.stdin.isatty()
    # assert environment.encoding is not None
    # assert environment.stdout.isatty()
    # assert environment.stderr.isatty()
    # assert environment.colors == 256
    # assert environment.program_name is not None
    # assert environment.devnull is not None
    assert environment.config_dir is not None
    assert environment._config is None
    assert environment.config is not None
    assert environment._config is not None
    environment.log_error('This is my log')
    assert environment._orig_stderr is not None
    environment.devnull = open(os.devnull, 'w+')
    assert environment.devnull is not None


# Generated at 2022-06-13 21:46:16.057054
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert type(env) == Environment


# Generated at 2022-06-13 21:46:18.730628
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name='http', devnull=True)
    assert env.program_name == 'http'
    assert env.devnull == True

# Generated at 2022-06-13 21:46:28.917692
# Unit test for constructor of class Environment
def test_Environment():
    E = Environment
    try:
        os.name
    except Exception:
        pass
    try:
        sys.stdout
    except Exception:
        pass
    try:
        sys.stdin
    except Exception:
        pass
    env = Environment()
    assert env.is_windows == E.is_windows
    assert env.config_dir == E.config_dir
    assert env.stdout_isatty == E.stdout_isatty
    assert env.stdout_encoding == E.stdout_encoding
    assert env.stdout == E.stdout
    assert env.stderr == E.stderr
    assert env.stderr_isatty == E.stderr_isatty
    assert env.stderr_encoding == E.stderr_encoding
   

# Generated at 2022-06-13 21:46:38.803093
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment(
        config_dir=Path('~/.httpie'),
        stdin=None,
        stdout=sys.stdout,
        stderr=sys.stderr,
    )
    assert environment.config_dir == Path('~/.httpie')
    assert environment.stdin is None
    assert environment.stdout == sys.stdout
    assert environment.stderr == sys.stderr
    assert environment.config.directory == Path('~/.httpie')
    assert environment.config.is_new()

# Generated at 2022-06-13 21:46:51.362130
# Unit test for constructor of class Environment
def test_Environment():
    # testing for method __init__
    env = Environment()

# Generated at 2022-06-13 21:47:17.409478
# Unit test for constructor of class Environment
def test_Environment():
    # Env is the actual environment
    Env = Environment()
    # Env2 is a simulation we use in the tests
    Env2 = Environment(program_name='myprog')
    import io
    import sys
    # Set the actual stdin, stdout and stderr of our simulation
    Env2.stdout = io.StringIO()
    Env2.stderr = io.StringIO()
    Env2.stdin = sys.stdin
    # Check if our simulation returned different results than the actual environment
    assert str(Env) != str(Env2)
    assert repr(Env) != repr(Env2)


# Generated at 2022-06-13 21:47:34.022105
# Unit test for constructor of class Environment
def test_Environment():
    assert not Environment().is_windows
    env = Environment(is_windows=True)
    assert env.is_windows
    assert env.stdin_isatty
    assert not env.stdout_isatty
    assert not env.stderr_isatty
    assert env.stdout_encoding
    assert env.stderr_encoding
    env = Environment(stdin=None)
    assert not env.stdin_isatty
    env = Environment(stdout=None)
    assert not env.stdout_isatty
    env = Environment(stderr=None)
    assert not env.stderr_isatty
    env = Environment(stdout_encoding='utf8')
    assert env.stdout_encoding == 'utf8'

# Generated at 2022-06-13 21:47:42.991743
# Unit test for constructor of class Environment

# Generated at 2022-06-13 21:47:47.586339
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment(config_dir=Path('.'))
    print(e.config_dir)

if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:47:58.929388
# Unit test for constructor of class Environment
def test_Environment():
    env=Environment(**{"stdin":sys.stdin,"stdin_isatty":True,"stdin_encoding":"abc","stdout":sys.stdout,"stdout_isatty":True,"stdout_encoding":"efg","stderr":sys.stderr,"stderr_isatty":True,"program_name":"test"})
    assert env.stdin==sys.stdin
    assert env.stdin_isatty==True
    assert env.stdin_encoding=="abc"
    assert env.stdout==sys.stdout
    assert env.stdout_isatty==True
    assert env.stdout_encoding=="efg"
    assert env.stderr==sys.stderr
    assert env.stderr_isatty==True
    assert env.program_

# Generated at 2022-06-13 21:47:59.918085
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    print(env)



# Generated at 2022-06-13 21:48:03.220598
# Unit test for constructor of class Environment
def test_Environment():
    # type: () -> None
    env = Environment()
    assert str(env) == '{' \
                       'colors=256, ' \
                       'config_dir=<config dir>, ' \
                       'program_name=http, ' \
                       'stderr=<stderr>, ' \
                       'stdin=<stdin>, ' \
                       'stdout=<stdout>}'


env = Environment()

# Generated at 2022-06-13 21:48:13.215735
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin is sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdin_encoding is None
    assert env.stdout is sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding is None
    assert env.stderr is sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.program_name == 'http'

    assert env.stdin_encoding == sys.stdin.encoding
    assert env.stdout_enc

# Generated at 2022-06-13 21:48:20.600386
# Unit test for constructor of class Environment
def test_Environment():
    stdin = sys.stdin
    stdout = sys.stdout
    stderr = sys.stderr

    environ = Environment()

    assert environ.is_windows == is_windows
    assert environ.config_dir == DEFAULT_CONFIG_DIR
    assert environ.stdin == stdin
    assert environ.stdin_isatty == stdin.isatty() if stdin else False
    assert environ.stdin_encoding == None
    assert environ.stdout == stdout
    assert environ.stdout_isatty == stdout.isatty()
    assert environ.stdout_encoding == None
    assert environ.stderr == stderr
    assert environ.stderr_isatty == stderr.isatty()

    # Close stdin

# Generated at 2022-06-13 21:48:27.480279
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull = 'hi', stderr_isatty = False, is_windows = False)
    assert env.devnull is 'hi'
    assert env.stderr_isatty is False
    assert env.is_windows is False

# Generated at 2022-06-13 21:48:55.741712
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout=None)
    assert env.stdout == None


# eof

# Generated at 2022-06-13 21:49:10.856447
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert not (env.is_windows)
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty
    assert env.stdin_encoding == None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty
    assert env.stdout_encoding == None
    assert env.stderr == sys.stderr
    assert env.stderr_isatty
    assert env.colors == 256
    assert env.program_name == 'http'
    # test __str__

# Generated at 2022-06-13 21:49:13.837597
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    print(env)


if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:49:26.885164
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull = 'Hello', is_windows = 'I am windows')
    print(env.devnull)
    print(env.is_windows)
    print(env.config_dir)
    print(env.stdin)
    print(env.stdin_isatty)
    print(env.stdin_encoding)
    print(env.stdout)
    print(env.stdout_isatty)
    print(env.stdout_encoding)
    print(env.stderr)
    print(env.stderr_isatty)
    print(env._orig_stderr)
    print(env.colors)
    print(env.program_name)
    print(env._config)
    print(env._devnull)
    # Test the __str__ and __

# Generated at 2022-06-13 21:49:36.554670
# Unit test for constructor of class Environment
def test_Environment():
    # Test Environment attributes
    my_env = Environment(devnull=None)
    assert my_env.is_windows == is_windows
    assert str(my_env.config_dir) == str(DEFAULT_CONFIG_DIR)
    assert my_env.stdin == sys.stdin
    assert my_env.stdin_isatty == (sys.stdin.isatty() if sys.stdin else False)
    assert my_env.stdin_encoding == None
    assert my_env.stdout == sys.stdout
    assert my_env.stdout_isatty == sys.stdout.isatty()
    assert my_env.stdout_encoding == None
    assert my_env.stderr == sys.stderr
    assert my_env.stderr_isatty == sys

# Generated at 2022-06-13 21:49:39.415354
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        config_dir = '/test',
        stderr = 'stderr',
        is_windows = False
    )
    assert env.__str__() == '{}'
    assert env.__repr__() == '<Environment {}>'

# Generated at 2022-06-13 21:49:49.693255
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    import os
    env = Environment()
    assert env.is_windows==sys.platform.startswith("win"), 'The environment is not windows'
    assert env.devnull==os.devnull, 'The environment is not os.devnull'
    assert env.config_dir==Path("/httpie"), 'The environment is not default config dir'
    assert env.stdin==sys.stdin, 'The environment is not standard sys.stdin'
    assert env.stdin_isatty==sys.stdin.isatty(), 'The environment is not the same stdin_isatty'
    assert env.stdin_encoding==sys.stdin.encoding, 'The environment is not the same stdin_encoding'

# Generated at 2022-06-13 21:49:55.137727
# Unit test for constructor of class Environment
def test_Environment():
    defaults = dict(Environment.__dict__)
    env = Environment(stdin=None)
    assert env.stdin is None
    assert env.stdin_isatty is False
    assert env.stdin_encoding is None
    assert defaults.items() <= env.__dict__.items()



# Generated at 2022-06-13 21:49:57.688327
# Unit test for constructor of class Environment
def test_Environment():
    sys.stdout = open('environment-test.txt', 'a')
    env = Environment()
    print(env)
    sys.stdout.close()

if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:50:04.872499
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull="xx", stdin=None, stdin_encoding=None,
                      stdout=sys.stdout, stdout_encoding=None)
    assert env.devnull == "xx"
    assert env.stdin == None
    assert env.stdin_encoding == None
    assert env.stdout == sys.stdout
    assert env.stdout_encoding == None