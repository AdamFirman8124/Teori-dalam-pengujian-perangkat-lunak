

# Generated at 2022-06-13 21:40:19.955147
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows


# Generated at 2022-06-13 21:40:30.471814
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert type(env)==Environment
    assert env.stderr == sys.stderr
    assert env.stdout == sys.stdout
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.stdin_encoding is None
    assert env.stdout_encoding is None
    assert env.stderr_encoding is None
    assert env.colors == 256
    assert env.devnull is None
    assert env._devnull is None
    assert env._orig_stderr == sys.stderr
   

# Generated at 2022-06-13 21:40:37.471282
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment()
    assert e.config_dir == DEFAULT_CONFIG_DIR
    assert e.stdin == sys.stdin
    assert e.stdout_isatty == sys.stdout.isatty()
    assert e.stderr_isatty == sys.stderr.isatty()
    assert e.stdout_encoding == sys.stdout.encoding
    assert e.stderr_isatty == sys.stderr.isatty()
    assert e.is_windows == is_windows
    assert e.program_name == 'http'



# Generated at 2022-06-13 21:40:41.310300
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=10, is_windows=True, program_name='httpie')
    assert env.devnull == 10
    assert env.is_windows == True
    assert env.program_name == 'httpie'

# Generated at 2022-06-13 21:40:51.779907
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin=sys.stdin, 
                      stdout=sys.stdout, 
                      stderr=sys.stderr, 
                      config_dir=DEFAULT_CONFIG_DIR,
                      program_name='http',
                      colors=256,
                      is_windows=is_windows)


# Generated at 2022-06-13 21:41:02.117623
# Unit test for constructor of class Environment
def test_Environment():
    """
    Unit test for constructor of class Environment
    """
    env = Environment(devnull="test", is_windows=False,
                      config_dir="./test", stdin="stdin", stdin_isatty=True,
                      stdin_encoding="utf8", stdout="stdout", stdout_isatty=True,
                      stdout_encoding="utf8", stderr="stderr", stderr_isatty=True,
                      colors=256, program_name="http2", _orig_stderr="stderr",
                      _devnull="test", _config=Config())
    assert env.stdin == "stdin"
    assert env.config_dir == Path("./test")
    assert env.is_windows == False
    assert env.stdin_isatty == True


# Generated at 2022-06-13 21:41:12.720666
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin=object())
    assert env.stdin == object()
    assert env.is_windows == is_windows
    assert env.stdin_isatty == False
    assert env.stdin_encoding == 'utf8'
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == True
    assert env.stdout_encoding == 'utf8'
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == True
    assert env.program_name == 'http'
    assert env.colors == 256
    assert env.config_dir == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:41:18.944665
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    env = Environment(stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
    print(env)
    assert env


if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:41:29.637743
# Unit test for constructor of class Environment
def test_Environment():
    # Normal test
    e = Environment()
    assert e.is_windows==is_windows
    assert e.config_dir==DEFAULT_CONFIG_DIR
    assert e.stdin==sys.stdin
    assert e.stdin_isatty==(sys.stdin.isatty() if sys.stdin else False)
    assert e.stdin_encoding==''
    assert e.stdout==sys.stdout
    assert e.stdout_isatty==sys.stdout.isatty()
    assert e.stdout_encoding==''
    assert e.stderr==sys.stderr
    assert e.stderr_isatty==sys.stderr.isatty()
    assert e.colors==256
    assert e.program_name=='http'

    # Test

# Generated at 2022-06-13 21:41:34.647463
# Unit test for constructor of class Environment
def test_Environment():
    """
    Test function
    """
    env = Environment(devnull=None)
    assert env.devnull == None
    env = Environment(stdout = sys.stdout)
    assert env.stdout == sys.stdout

# Generated at 2022-06-13 21:41:43.485809
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert isinstance(env, Environment)
    env.config.load()
    assert isinstance(env.config.items(), list)
    env.config.save()



# Generated at 2022-06-13 21:41:54.696159
# Unit test for constructor of class Environment
def test_Environment():
    try:
        env = Environment()
        assert isinstance(env, Environment)
        assert env.stderr != None
        assert env.stdin != None
        assert env.stdout != None
        assert env.stdin_isatty == True
        assert env.stdin_encoding == 'utf8'
        assert env.stdout_isatty == True
        assert env.stdout_encoding == 'utf8'
        assert env.stderr_isatty == True
        assert env.colors == 256
        assert env.program_name == 'http'
        assert env.is_windows == False
        assert env.config_dir != None
        assert env.devnull == None
    except:
        assert False

# Generated at 2022-06-13 21:42:11.692014
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    import os
    from httpie.config import DEFAULT_CONFIG_DIR, Config, ConfigFileError
    from httpie.utils import repr_dict

    from httpie.compat import is_windows
    from httpie.config import DEFAULT_CONFIG_DIR
    from httpie.utils import repr_dict

    from httpie.compat import is_windows

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
        stdin: Optional[IO] = sys.stdin  # `None

# Generated at 2022-06-13 21:42:23.265129
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin='stdin', stdout='stdout', stderr='stderr')
    assert env.stdin == 'stdin'
    assert env.stdout == 'stdout'
    assert env.stderr == 'stderr'

    # stdin
    env.stdin = 'stdin'
    assert env.stdin == 'stdin'
    env.stdin = None
    assert env.stdin is None
    env.stdin = stdin
    assert env.stdin == stdin

    # stdout
    env.stdout = 'stdout'
    assert env.stdout == 'stdout'
    env.stdout = stdout
    assert env.stdout == stdout

    # stderr
    env.stderr = 'stderr'
    assert env.st

# Generated at 2022-06-13 21:42:28.204562
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment()
    assert e.is_windows == is_windows
    assert e.config_dir == DEFAULT_CONFIG_DIR
    assert e.stdin == sys.stdin
    assert e.stdin_isatty == sys.stdin.isatty()
    assert e.stdout == sys.stdout
    assert e.stdout_isatty == sys.stdout.isatty()
    assert e.stderr == sys.stderr
    assert e.stderr_isatty == sys.stderr.isatty()
    assert e.program_name == 'http'

# Generated at 2022-06-13 21:42:29.810763
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin=None)
    assert env
    print(repr(env))
    print(env)

# Generated at 2022-06-13 21:42:36.578238
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()

    env.__dict__.update(is_windows=True, config_dir=DEFAULT_CONFIG_DIR, stdin=sys.stdin, stdin_isatty=True, stdin_encoding='utf-8', stdout=sys.stdout, stdout_isatty=True, stdout_encoding=None, stderr=sys.stderr, stderr_isatty=True, colors=256, program_name='http')

    assert env.__dict__['colors'] == 256

    default_stream = sys.stdout
    def set_default_stream():
        env.__dict__['stdin'] = sys.stdin
        env.__dict__['stdout'] = default_stream
        env.__dict__['stderr'] = default_stream

    set_

# Generated at 2022-06-13 21:42:49.323470
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin_isatty=False,
                      stdin_encoding='utf8',
                      stdout_isatty=True,
                      stdout_encoding='utf8',
                      stderr_isatty=True,
                      devnull=None,
                      config_dir='config_dir',
                      program_name='program_name',
                      color=256,
                      is_windows=False,
                      stdin='stdin',
                      stdout='stdout',
                      stderr='stderr')
    assert env.is_windows is False
    assert env.config_dir == 'config_dir'
    assert env.stdin == 'stdin'
    assert env.stdin_isatty is False
    assert env.stdin_encoding == 'utf8'

# Generated at 2022-06-13 21:42:55.255496
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name = 'http', stdin = sys.stdin, stdout = sys.stdout, stderr = sys.stderr, devnull = None, config_dir = DEFAULT_CONFIG_DIR)
    assert sys.stdin == env.stdin
    assert sys.stdout == env.stdout
    assert sys.stderr == env.stderr
    assert DEFAULT_CONFIG_DIR == env.config_dir
    assert 'http' == env.program_name


# Generated at 2022-06-13 21:43:10.371810
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name='test', stdout_encoding='test')
    assert env.stdout_encoding == 'test'


# TODO: move this to a separate module.

new_httpie_colors = {
    'scheme': {'https': ('bold', 'brightgreen')},
    'host': ('bold', 'brightmagenta'),
    'header': ('dim', 'green'),
    'index': ('dim', 'magenta'),
    'item': ('dim', 'cyan'),
    'verbose_header': ('bold', 'green'),
    'verbose_value': ('dim', 'cyan'),
    'error': ('bold', 'red'),
    'body': ('reset', None),
    'kv': ('reset', None),
}



# Generated at 2022-06-13 21:43:26.759142
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == False
    assert str(env.config_dir)[-16:] == "httpie/httpie"
    assert str(env.stdin)[:12] == "<_io.TextIOWrapper"
    assert env.stdin_isatty == True
    assert env.stdin_encoding == "UTF-8"
    assert str(env.stdout)[:12] == "<_io.TextIOWrapper"
    assert env.stdout_isatty == True
    assert env.stdout_encoding == "UTF-8"
    assert str(env.stderr)[:12] == "<_io.TextIOWrapper"
    assert env.stderr_isatty == True
    assert env.colors == 256
    assert env.program_name

# Generated at 2022-06-13 21:43:38.723600
# Unit test for constructor of class Environment
def test_Environment():

    # Creating an instance of the class Environment
    # with adapted parameters for additional tests.
    # This has to be done in order to
    # set the actual values of instance attributes "devnull" and "config".
    environment = Environment(
        program_name='http',
        devnull=None,
        config=None,
        stdin=None,
        stdin_isatty=False,
        stdin_encoding='utf8',
        stdout=None,
        stdout_isatty=False,
        stdout_encoding='utf8',
        stderr=None,
        stderr_isatty=False,
        _orig_stderr=None,
        colors=256,
        is_windows=False,
        config_dir=Path(''))

    # Test if the parameter list of constructor


# Generated at 2022-06-13 21:43:47.261728
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(config_dir="config_dir", stdin="stdin",
                      stdin_isatty=True, stdin_encoding="utf8", stdout="stdout",
                      stdout_isatty=True, stdout_encoding="utf8", stderr="stderr",
                      stderr_isatty=True, colors=256, program_name="http")
    assert env.config_dir == "config_dir"
    assert env.stdin_isatty == True
    assert env.stdin_encoding == "utf8"
    assert env.stdout_isatty == True
    assert env.stdout_encoding == "utf8"

# Generated at 2022-06-13 21:43:54.662179
# Unit test for constructor of class Environment
def test_Environment():

    env = Environment(is_windows=True, config_dir='/a/b',
        stdin=None, stdin_isatty=False, stdin_encoding=None,
        stdout=None, stdout_isatty=False, stdout_encoding=None,
        stderr=None, stderr_isatty=False, colors=256, program_name='http')
    assert env.is_windows
    assert env.config_dir == Path('/a/b')
    assert env.stdin is None
    assert env.stdin_encoding is None
    assert env.stdout is None
    assert env.stdout_encoding is None
    assert env.stderr is None
    assert env.stderr_isatty is False
    assert env.colors == 256
    assert env

# Generated at 2022-06-13 21:43:58.779248
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout=sys.stderr, config_dir=Path('/some/where'))
    assert env.stdout == sys.stderr
    assert env.config_dir == Path('/some/where')

# Generated at 2022-06-13 21:44:07.632612
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == True
    assert env.config_dir == '.config/httpie'
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == True
    assert env.stdin_encoding == 'utf-8'
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == True
    assert env.stdout_encoding == 'utf-8'
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == True
    assert env.colors == 256
    assert env.program_name == 'http'
    
    
    

# Generated at 2022-06-13 21:44:18.835269
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        config_dir='/foo',
        stdin=None,
        stdin_isatty=False,
        stdin_encoding='ascii',
        stdout=sys.__stdout__,
        stdout_isatty=True,
        stdout_encoding='utf8',
        stderr=sys.__stderr__,
        stderr_isatty=True,
        colors=0,
        colors_256=False,
        colors_16m=False,
        colors_true_color=False,
        program_name='httpie',
    )
    assert env.config_dir == '/foo'
    assert env.stdin is None
    assert env.stdin_isatty is False
    assert env.stdin_encoding == 'ascii'

# Generated at 2022-06-13 21:44:26.076127
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin='a', stdout='b', stderr='c')
    assert env.stdin == 'a'
    assert env.stdout == 'b'
    assert env.stderr == 'c'


# Generated at 2022-06-13 21:44:36.113753
# Unit test for constructor of class Environment
def test_Environment():
    # Non-default options to pass to the constructor of class Environment
    stderr = sys.stdout
    devnull = open(os.devnull, 'w+')
    is_windows = True
    config_dir = '/tmp/Httpie'
    program_name = 'http'
    # Default options
    stdin = sys.stdin
    stdout = sys.stdout
    stdin_isatty = stdin.isatty() if stdin else False
    stdin_encoding = None
    stdout_isatty = stdout.isatty()
    stdout_encoding = None
    stderr_isatty = stderr.isatty()
    colors = 256
    # Constructor
    env = Environment(stderr, devnull, is_windows, config_dir, program_name)

# Generated at 2022-06-13 21:44:48.652892
# Unit test for constructor of class Environment

# Generated at 2022-06-13 21:45:01.942660
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin_isatty=True, stdout_isatty=True, stderr_isatty=True)
    env = Environment(config_dir="test", stdin_encoding=None)

# Generated at 2022-06-13 21:45:08.659890
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        is_windows=True,
        stdin=sys.stdin,
        stdout=sys.stdout,
        stderr=sys.stderr
    )
    assert env.is_windows
    assert env.stdin is sys.stdin
    assert env.stdout is sys.stdout
    assert env.stderr is sys.stderr
    assert isinstance(env.config, Config)

# Generated at 2022-06-13 21:45:16.155095
# Unit test for constructor of class Environment
def test_Environment():
    from httpie.config import DEFAULT_CONFIG_DIR
    print(Environment(stdin_encoding='2', stdout_encoding='3'))
    print(Environment(stdout=None))
    print(Environment(is_windows=False))
    print(Environment(config_dir=DEFAULT_CONFIG_DIR))
    print(Environment(program_name='http'))
    print(Environment(colors=256))
    print(Environment())

if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:45:17.545584
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment()
    print(environment)



# Generated at 2022-06-13 21:45:27.778351
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(colors = 256,
                      stdin = sys.stdin,
                      stdin_isatty = True,
                      stdin_encoding = None,
                      stdout = sys.stdout,
                      stdout_isatty = True,
                      stdout_encoding = None,
                      stderr = sys.stderr,
                      stderr_isatty = True,
                      colors = 256,
                      program_name = 'http')
    assert(env.colors == 256)
    assert(env.stdin == sys.stdin)
    assert(env.stdin_isatty == True)
    assert(env.stdin_encoding == None)
    assert(env.stdout == sys.stdout)
    assert(env.stdout_isatty == True)

# Generated at 2022-06-13 21:45:29.400478
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    env.stderr.write('\nHello\n')

# Generated at 2022-06-13 21:45:37.032206
# Unit test for constructor of class Environment
def test_Environment():
    import os
    from pathlib import Path
    from typing import IO, Optional

    e = Environment()
    assert e.is_windows == is_windows
    assert e.config_dir == DEFAULT_CONFIG_DIR
    assert e.stdin == sys.stdin
    assert e.stdin_isatty == sys.stdin.isatty()
    assert e.stdin_encoding == None
    assert e.stdout == sys.stdout
    assert e.stdout_isatty == sys.stdout.isatty()
    assert e.stdout_encoding == None
    assert e.stderr == sys.stderr
    assert e.stderr_isatty == sys.stderr.isatty()
    assert e.colors == 256

# Generated at 2022-06-13 21:45:41.022843
# Unit test for constructor of class Environment
def test_Environment():
    # print("\nChecking whether default values of object of class Environment were set successfully or not!\n")
    assert Environment()



# Generated at 2022-06-13 21:45:43.762983
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout_encoding = 'utf8')
    assert isinstance(env.stdout_encoding, str)


# Generated at 2022-06-13 21:45:44.487587
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment()

# Generated at 2022-06-13 21:45:58.971439
# Unit test for constructor of class Environment
def test_Environment():
    """
    import httpie
    e=httpie.Environment()
    assert e.stdout_encoding.lower() == 'utf8'
    """
    print('Pass')


if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:46:00.988967
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin=None)
    assert env.stdin == None

# Generated at 2022-06-13 21:46:10.818398
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert type(env) == Environment
    assert env.is_windows == is_windows
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.config_dir == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:46:22.828806
# Unit test for constructor of class Environment
def test_Environment():
    stdout = open("str.txt","w")
    stderr = open("str.txt","w")
    env = Environment(stdout, stderr)
    print("is_windows: ",env.is_windows)
    print("config_dir: ",env.config_dir)
    print("stdin: ",env.stdin)
    print("stdin_isatty: ",env.stdin_isatty)
    print("stdout_isatty: ",env.stdout_isatty)
    print("stdout_encoding: ",env.stdout_encoding)
    print("stderr_isatty: ",env.stderr_isatty)
    print("colors: ",env.colors)
    print("program_name: ",env.program_name)
    #config:

# Generated at 2022-06-13 21:46:31.595786
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment(program_name="httpie123")
    assert environment.program_name == "httpie123"
    assert environment.is_windows == is_windows
    assert environment.config_dir == DEFAULT_CONFIG_DIR
    assert environment.stdin == sys.stdin
    assert environment.stdout == sys.stdout
    assert environment.stderr == sys.stderr
    assert environment.stdin_isatty == True
    assert environment.stdout_isatty == True
    assert environment.stderr_isatty == True
    assert environment.stdin_encoding == "utf-8"
    assert environment.stdout_encoding == "utf-8"

# Generated at 2022-06-13 21:46:35.419243
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull="bla", program_name='bla', config_dir=None)
    assert env.devnull == 'bla'
    assert env.program_name == 'bla'
    assert env.config_dir is None
    # https://docs.python.org/3/library/unittest.mock.html
    # https://docs.python.org/3/library/unittest.mock.html#quick-guide

# Generated at 2022-06-13 21:46:37.775959
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name='httpie')
    assert env.program_name == 'httpie'


# Generated at 2022-06-13 21:46:41.825147
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(is_windows=False)
    assert(env.is_windows == False)
    assert(env.stdin == sys.stdin)
    assert(env.stdout == sys.stdout)
    assert(env.stderr == sys.stderr)
    assert(env.config_dir == DEFAULT_CONFIG_DIR)
    assert(env.colors == 256)

# Generated at 2022-06-13 21:46:47.795737
# Unit test for constructor of class Environment
def test_Environment():                         
    e = Environment(**{"devnull":None, "is_windows":is_windows, "config_dir": DEFAULT_CONFIG_DIR, "stdin": sys.stdin, "stdin_isatty": sys.stdin.isatty(), "stdin_encoding":None, "stdout":sys.stdout, "stdout_isatty":sys.stdout.isatty(), "stdout_encoding":None, "stderr":sys.stderr, "stderr_isatty":sys.stderr.isatty(), "colors":256, "program_name":"http"})
    e._orig_stderr = e.stderr
    e._devnull = None

# Generated at 2022-06-13 21:46:50.418867
# Unit test for constructor of class Environment
def test_Environment():
     env = Environment()
     assert type(env) is Environment
    

# Generated at 2022-06-13 21:47:23.638101
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        config_dir = "H:/httpie",
        stdin = sys.stdin, 
        stdout = sys.stdout, 
        stderr = sys.stderr,
        devnull = "nothing",
        stdin_isatty = False,
        stdout_isatty = False, 
        stderr_isatty = False,
        stdin_encoding = "utf8",
        stdout_encoding = "utf8",
        colors = 256,
        program_name = "http",
        )
    assert env.config_dir == "H:/httpie"
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr

# Generated at 2022-06-13 21:47:37.092161
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()

    assert env.is_windows is is_windows
    assert is_windows is False
    assert env.config_dir is DEFAULT_CONFIG_DIR
    assert env.stdin is sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdin_encoding is None
    assert env.stdout is sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding is None
    assert env.stderr is sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.colors == 256
    assert env.program_name is 'http'
    assert env._orig_stderr

# Generated at 2022-06-13 21:47:40.237399
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment(devnull='devnull')
    assert e._devnull == 'devnull'
    e.devnull = 'test'
    assert e._devnull == 'test'

# Generated at 2022-06-13 21:47:42.315492
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()

test_Environment()

# Generated at 2022-06-13 21:47:55.115529
# Unit test for constructor of class Environment
def test_Environment():
    import io
    import os
    from pathlib import Path
    from httpie.config import DEFAULT_CONFIG_DIR
    from httpie.context import Environment
    from httpie.utils import repr_dict
    stdin = io.StringIO("Dummy String")
    stdout = io.StringIO("Dummy String")
    stderr = io.StringIO("Dummy String")
    config_dir = Path("Dummy String")

# Generated at 2022-06-13 21:47:59.574494
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment(stdout=sys.stdout, stderr=sys.stderr)
    assert environment.stdout == sys.stdout
    assert environment.stderr == sys.stderr
    assert environment.devnull is None

environment = Environment()

# Generated at 2022-06-13 21:48:04.948488
# Unit test for constructor of class Environment
def test_Environment():
    actual = Environment(
        is_windows=True,
        config_dir=Path('./config'),
        stdin=open('./config'),
        stdin_isatty=True,
        stdin_encoding='utf-8',
        stdout=open('./stdout'),
        stdout_isatty=False,
        stdout_encoding='ascii',
        stderr=open('./stderr'),
        stderr_isatty=True,
        colors=16,
        program_name='test'
    )
    assert actual.is_windows
    assert actual.config_dir == Path('./config')
    assert actual.stdin == open('./config')
    assert actual.stdin_isatty

# Generated at 2022-06-13 21:48:15.931882
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.config == Config()

    env = Environment(devnull=100, stdout_encoding='ascii')
    assert env.devnull == 100
    assert env.stdout_encoding == 'ascii'
    env.devnull = 300
    assert env.devnull == 300
    assert env.stdout_encoding == 'ascii'

    env = Environment(devnull=100, stdin='ass')
    assert env.devnull == 100
    assert env.stdin == 'ass'
    assert env.stdin_encoding is None
    assert env.stdin_isatty is False

# Generated at 2022-06-13 21:48:19.858016
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    print("测试结果：", env.stderr.encoding)

if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:48:28.477865
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(is_windows=True,
                      config_dir=DEFAULT_CONFIG_DIR,
                      stdin=sys.stdin,
                      stdin_isatty=sys.stdin.isatty(),
                      stdin_encoding=sys.stdin.encoding,
                      stdout=sys.stdout,
                      stdout_isatty=sys.stdout.isatty(),
                      stdout_encoding=sys.stdout.encoding,
                      stderr=sys.stderr)
    if env.colors != 256:
        assert curses is None
    if not env.is_windows:
        if curses:
            assert env.colors == curses.tigetnum('colors')
    print(env)
    print(env.config)
    env.log_error('test')


# Generated at 2022-06-13 21:49:04.242700
# Unit test for constructor of class Environment
def test_Environment():
    invoke_str = 'err_str'
    try:
        raise Exception(invoke_str)
    except Exception as e:
        error_str = str(e)
    env = Environment(stderr=StringIO())
    env.log_error(invoke_str)
    assert error_str == env.stderr.getvalue().strip()


# Generated at 2022-06-13 21:49:18.230164
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    if not is_windows:
        assert env.is_windows is False
    else:
        assert env.is_windows is True
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty is env.stdin.isatty()
    assert env.stdout == sys.stdout
    assert env.stdout_isatty is env.stdout.isatty()
    assert env.stderr == sys.stderr
    assert env.stderr_isatty is env.stderr.isatty()
    assert env.colors == 256
    assert env.program_name == 'http'


# Generated at 2022-06-13 21:49:25.055318
# Unit test for constructor of class Environment
def test_Environment():
    import json

    env = Environment(program_name='http')
    assert env.program_name == 'http'

    env = Environment(program_name='http', colors=64)
    assert env.colors == 64

    env = Environment(program_name='http', colors=128)
    assert env.colors == 128

    env = Environment(program_name='http', colors=255)
    assert env.colors == 255


# Generated at 2022-06-13 21:49:35.136146
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name="test_http", stdin=None, stdin_isatty=False, stdin_encoding="test_utf8",
                      stdout=None, stdout_isatty=False, stdout_encoding="test_utf8",
                      stderr=None, stderr_isatty=False, colors=256, is_windows=False,
                      config_dir = "/home/user/", devnull=None)
    for key, value in env.__dict__.items():
        if key == "program_name":
            assert value == "test_http"
        elif key == "stdin":
            assert value is None
        elif key == "stdin_isatty":
            assert value is False

# Generated at 2022-06-13 21:49:39.920429
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        config_dir='~',
        stdin=None,
        stdout=None,
        stderr=None,
        is_windows=False,
        program_name='HTTPI')
    assert env.config_dir.name == '~'
    assert env.stdin == None
    assert env.stdout == None
    assert env.stderr == None
    assert env.is_windows == False
    assert env.program_name == 'HTTPI'

# Generated at 2022-06-13 21:49:49.985105
# Unit test for constructor of class Environment
def test_Environment():
    assert str(Environment()) == '''\
{'colors': 256,
 'config_dir': '/Users//.config/httpie',
 'is_windows': False,
 'program_name': 'http',
 'stderr': <_io.TextIOWrapper name='<stderr>' encoding='UTF-8'>,
 'stderr_isatty': True,
 'stdin': <_io.TextIOWrapper name='<stdin>' encoding='UTF-8'>,
 'stdin_encoding': 'UTF-8',
 'stdin_isatty': True,
 'stdout': <_io.TextIOWrapper name='<stdout>' encoding='UTF-8'>,
 'stdout_encoding': 'UTF-8',
 'stdout_isatty': True}'''

# Generated at 2022-06-13 21:49:59.827877
# Unit test for constructor of class Environment
def test_Environment():
    # Initialise the class
    env = Environment()
    assert isinstance(env, Environment)

    # Check if the class variables are valid
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.program_name == 'http'

    # Overwrite class variables

# Generated at 2022-06-13 21:50:11.484653
# Unit test for constructor of class Environment
def test_Environment():
    import io
    import os
    from pathlib import Path

    stdin = io.StringIO()
    stdin.close()
    devnull = open(os.devnull, 'w+')

    env = Environment(
        is_windows=True,
        config_dir='/foo',
        stdin=stdin,
        stdout=io.StringIO(),
        stderr=io.StringIO(),
        program_name='test',
        devnull=devnull,
    )
    assert env.is_windows is True
    assert env.config_dir == Path('/foo')
    assert env.stdin is stdin
    assert env.stdout.buffer is not None
    assert env.stderr.buffer is not None
    assert env.program_name == 'test'
    assert env.devnull is devnull