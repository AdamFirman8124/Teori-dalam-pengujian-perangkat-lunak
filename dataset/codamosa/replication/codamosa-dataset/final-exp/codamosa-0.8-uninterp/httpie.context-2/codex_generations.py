

# Generated at 2022-06-13 21:40:29.614278
# Unit test for constructor of class Environment
def test_Environment():
    # use mock object
    from unittest.mock import MagicMock
    environment = Environment(
        config_dir='/user/.config/httpie',
        is_windows=True,
        stdin=MagicMock(),
        stdin_isatty=False,
        stdin_encoding='utf8',
        stdout=MagicMock(),
        stdout_isatty=False,
        stdout_encoding='utf8',
        stderr=MagicMock(),
        stderr_isatty=False,
        colors=256,
        program_name='http'
    )

    # get atribute from instance
    assert environment.config_dir == '/user/.config/httpie'


# Generated at 2022-06-13 21:40:38.535327
# Unit test for constructor of class Environment
def test_Environment():
    import io
    import os

    # 构造类的对象
    env = Environment()

    # pylint: disable=bad-whitespace
    assert env.is_windows                == is_windows
    assert env.config_dir                == DEFAULT_CONFIG_DIR
    assert env.stdin                     == sys.stdin
    assert env.stdin_isatty              == sys.stdin.isatty() if sys.stdin else False
    assert env.stdin_encoding            == None
    assert env.stdout                    == sys.stdout
    assert env.stdout_isatty             == sys.stdout.isatty()
    # assert env.stdout_encoding           == None
    assert env.stderr                    == sys.stderr
    assert env.st

# Generated at 2022-06-13 21:40:50.948512
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stdout_isatty
    assert env.stderr_isatty
    assert env.stdin_isatty
    assert env.stdout_encoding == 'utf8'
    assert env.stderr_encoding == 'utf8'
    assert env.stdin_encoding == 'utf8'
    assert env.stderr is not env.stdout
    assert env.stdout is not env.stdin

    env = Environment(devnull='a', stdin='a', stdout='b', stderr='c')
    assert env.stdout_isatty is False
    assert env.stderr_isatty is False
    assert env.stdin_isatty is False
    assert env.stdout_encoding == 'a'
    assert env.st

# Generated at 2022-06-13 21:41:00.944045
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name='http', stdin=None, stdin_encoding='utf8', stdin_isatty=True,
                      stdout=sys.stdout, stdout_encoding='utf8', stdout_isatty=True,
                      stderr=sys.stderr, stderr_isatty=True, colors=256, config_dir=DEFAULT_CONFIG_DIR)

    assert env.program_name == 'http'
    assert env.stdin is None
    assert env.stdin_encoding == 'utf8'
    assert env.stdin_isatty is True
    assert env.stdout == sys.stdout
    assert env.stdout_encoding == 'utf8'
    assert env.stdout_isatty is True
    assert env.stderr == sys

# Generated at 2022-06-13 21:41:13.249799
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    import os
    from httpie.utils import get_netrc_path
    from pathlib import Path
    import tempfile
    env = Environment()
    print(env)
    devnull = open(os.devnull, 'w+')
    assert isinstance(env, Environment)
    assert env.is_windows == sys.platform == "win32"
    assert os.path.isdir(env.config_dir)
    assert env.config_dir == os.path.dirname(get_netrc_path())
    assert (not isinstance(env.stdin, str)) and env.stdin == sys.stdin
    assert isinstance(env.stdin_isatty, bool)
    assert isinstance(env.stdin_encoding, str)

# Generated at 2022-06-13 21:41:25.511821
# Unit test for constructor of class Environment
def test_Environment():
    stdin = sys.stdin
    stdout = sys.stdout
    stderr = sys.stderr
    env = Environment(stdin=stdin, stdout=stdout, stderr=stderr)
    assert env.stdin_isatty
    assert env.stdout_isatty
    assert env.stderr_isatty

    env = Environment(stdout=stdout, stderr=stderr)
    assert env.stdout_isatty
    assert env.stderr_isatty
    assert env.devnull.name == os.devnull

    env = Environment(stderr=stderr)
    assert env.stderr_isatty
    assert env.devnull.name == os.devnull

# Generated at 2022-06-13 21:41:35.633951
# Unit test for constructor of class Environment

# Generated at 2022-06-13 21:41:47.986339
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    import os
    from pathlib import Path
    from typing import IO, Optional

    from httpie.compat import is_windows
    from httpie.config import DEFAULT_CONFIG_DIR, Config, ConfigFileError

    from httpie.utils import repr_dict


    env = Environment()
    #print(env)

    #print(env)
    #print(env.stdin)
    #print(env.stdin.isatty())
    #print(env.stdin_isatty)
    #print(env.stdin_encoding)
    #print(env.stdout)
    #print(env.stdout.isatty())
    #print(env.stdout_isatty)
    #print(env.stdout_encoding)
    #print(env.stderr

# Generated at 2022-06-13 21:41:49.435300
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert isinstance(env, Environment)



# Generated at 2022-06-13 21:42:03.084051
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    # Check infomation a instance of class environment
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
    assert env.colors == 256

# Generated at 2022-06-13 21:42:11.655347
# Unit test for constructor of class Environment
def test_Environment():
    import StringIO
    env = Environment(
        stdin=StringIO.StringIO(),
        stdout=StringIO.StringIO(),
        stderr=StringIO.StringIO(),
    )
    print(env)

if __name__ == "__main__":
    test_Environment()

# Generated at 2022-06-13 21:42:23.263941
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin is not None
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdin_encoding == getattr(sys.stdin, 'encoding', None) or 'utf8'
    assert env.stdout is not None
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding == getattr(sys.stdout, 'encoding', None) or 'utf8'
    assert env.stderr is not None
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.colors == 256


# Generated at 2022-06-13 21:42:28.396577
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(hello='world')
    assert env.hello == 'world'
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr_isatty == sys.stderr.isatty()

    import io
    stream = io.StringIO()
    stream.encoding = 'utf8'
    env = Environment(stderr=stream)
    assert env.stderr == stream
    assert env.stderr_isatty is False
    assert env.stderr_encoding == 'utf8'



# Generated at 2022-06-13 21:42:35.876988
# Unit test for constructor of class Environment
def test_Environment():
    environment_1=Environment()
    assert(environment_1.is_windows == is_windows)
    assert(environment_1.config_dir == DEFAULT_CONFIG_DIR)
    assert(environment_1.stdin == sys.stdin)
    assert(environment_1.stdin_isatty == environment_1.stdin.isatty())
    assert(environment_1.stdout == sys.stdout)
    assert(environment_1.stderr == sys.stderr)
    assert(environment_1.stdout_isatty == environment_1.stdout.isatty())
    assert(environment_1.stderr_isatty == environment_1.stderr.isatty())
    assert(environment_1.stdin_encoding == None)

# Generated at 2022-06-13 21:42:48.996240
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(is_windows = True)
    assert env.is_windows == True
    env = Environment(config_dir = Path('test'))
    assert env.config_dir == Path('test')
    env = Environment(stdin = sys.stdin)
    assert env.stdin == sys.stdin
    env = Environment(stdout = sys.stdout)
    assert env.stdout == sys.stdout
    env = Environment(stderr = sys.stderr)
    assert env.stderr == sys.stderr
    env = Environment(colors = 256)
    assert env.colors == 256
    env = Environment(program_name = 'http')
    assert env.program_name == 'http'
    assert env.is_windows == False
    assert env.colors == 256
    assert env

# Generated at 2022-06-13 21:42:56.917913
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    env = Environment(stdin=None, stdout_encoding='abc', abc=123)
    assert env.stdin is None
    assert env.stdin_encoding == 'abc'
    assert env.abc == 123
    assert not hasattr(env, 'stdout_encoding')

# Generated at 2022-06-13 21:43:11.237351
# Unit test for constructor of class Environment
def test_Environment():
    print("\nRunning function test_Environment")
    env = Environment(is_windows = True, stdin = sys.stdin, stdout = sys.stdout, stderr = sys.stderr)
    print("env.is_windows = "+str(env.is_windows))
    print("env.config_dir = "+str(env.config_dir))
    print("env.stdin = "+str(env.stdin))
    print("env.stdin_isatty = "+str(env.stdin_isatty))
    print("env.stdin_encoding = "+str(env.stdin_encoding))
    print("env.stdout = "+str(env.stdout))
    print("env.stdout_isatty = "+str(env.stdout_isatty))

# Generated at 2022-06-13 21:43:24.318137
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(colors = 256,stdin = sys.stdin,stdout = sys.stdout,stderr = sys.stderr)
    assert env.is_windows == is_windows
    assert env.stdin == sys.stdin
    assert env.stderr == sys.stderr
    assert env.stdout == sys.stdout
    assert env.stdin_isatty == stdin.isatty() if stdin else False
    assert env.stdin_encoding == None
    assert env.stdout_isatty == stdout.isatty()
    assert env.stdout_encoding == None
    assert env.stderr_isatty == stderr.isatty()
    assert env.colors == 256
    assert env.program_name == 'http'
    #assert

# Generated at 2022-06-13 21:43:31.487800
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty
    assert env.stdin_encoding == 'utf8'
    assert env.stdout == sys.stdout
    assert env.stdout_isatty
    assert env.stdout_encoding == 'utf8'
    assert env.stderr == sys.stderr
    assert env.stderr_isatty
    assert env.colors == 256
    assert env.program_name == 'http'

if __name__ == "__main__":
    test_Environment()

# Generated at 2022-06-13 21:43:37.804989
# Unit test for constructor of class Environment
def test_Environment():
    d = dict(is_windows=True, config_dir='./testconfig_dir/')
    env = Environment(**d)
    assert env.is_windows == True
    assert env.config_dir == Path('./testconfig_dir/')
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.colors == 256
    assert env.program_name == 'http'

# Generated at 2022-06-13 21:43:47.135200
# Unit test for constructor of class Environment
def test_Environment():
    env=Environment()
    print(str(env))
    # print(env.config)
    print(env.is_windows)
    env.log_error('this is a error')


# Generated at 2022-06-13 21:43:49.553046
# Unit test for constructor of class Environment
def test_Environment():
    # Arrange
    global environment_object

    # Act
    environment_object = Environment()

    # Assert
    assert environment_object.is_windows == is_windows

# Generated at 2022-06-13 21:43:57.233937
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.program_name == 'http'
    assert env.stdin_encoding == 'utf8'
    assert env.stdout_encoding == 'utf8'

# Generated at 2022-06-13 21:44:06.540983
# Unit test for constructor of class Environment
def test_Environment():

    # Test case: is_windows, stdin and stdout in python3 is
    # OK
    e = Environment()
    assert e.is_windows == False
    assert e.stdin == sys.stdin
    assert e.stdout == sys.stdout
    assert e.stderr == sys.stderr
    assert e.color == 256

    # Test case: No config dir if not a valid path
    with pytest.raises(AssertionError):
        e = Environment(config_dir = "")

    # Test case: No stdin if it is not ok
    with pytest.raises(AssertionError):
        e = Environment(stdin = "")

    # Test case: stderr is sys.stderr

# Generated at 2022-06-13 21:44:11.287140
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment()
    assert isinstance(environment, Environment)
    assert environment.stdin_encoding == 'utf8'
    assert environment.stderr == sys.stderr
    assert environment.stderr_isatty == sys.stderr.isatty()

# Generated at 2022-06-13 21:44:16.038243
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull="devnull")
    assert env._devnull == "devnull"
    assert env.__str__() != None

# Generated at 2022-06-13 21:44:22.383165
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr

# Generated at 2022-06-13 21:44:34.233271
# Unit test for constructor of class Environment
def test_Environment():
    # Test case 1:
    env1 = Environment()
    assert env1.is_windows == is_windows
    assert env1.stdin == sys.stdin
    assert env1.stdout == sys.stdout
    assert env1.stderr == sys.stderr
    assert env1.config.directory == DEFAULT_CONFIG_DIR
    # Test case 2:
    env2 = Environment(config_dir='D:/PythonTest/httpie-1.0.2')
    assert env2.config.directory == 'D:/PythonTest/httpie-1.0.2'
    # Test case 3:
    env3 = Environment(program_name='name3')
    assert env3.program_name == 'name3'

# Generated at 2022-06-13 21:44:47.192713
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment(devnull='a', program_name='b', config_dir='c', stdin='d', stdin_isatty='e', stdin_encoding='f', stdout='g', stdout_isatty='h', stdout_encoding='i', stderr='j')
    assert e.devnull == 'a'
    assert e.program_name == 'b'
    assert e.config_dir == 'c'
    assert e.stdin == 'd'
    assert e.stdin_isatty == 'e'
    assert e.stdin_encoding == 'f'
    assert e.stdout == 'g'
    assert e.stdout_isatty == 'h'
    assert e.stdout_encoding == 'i'
    assert e.stderr == 'j'

# Generated at 2022-06-13 21:44:57.559151
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert isinstance(env, Environment)
    assert isinstance(env.config_dir, Path)
    assert isinstance(env.stdin, IO)
    assert isinstance(env.stdin_isatty, bool)
    assert isinstance(env.stdin_encoding, str)
    assert isinstance(env.stdin_encoding, str)
    assert isinstance(env.stdout, IO)
    assert isinstance(env.stdout_isatty, bool)
    assert isinstance(env.stdout_encoding, str)
    assert isinstance(env.stderr, IO)
    assert isinstance(env.stderr_isatty, bool)
    assert isinstance(env.colors, int)
    assert isinstance(env.program_name, str)

# Generated at 2022-06-13 21:45:07.725968
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(**{'program_name':'test_program_name'})
    assert env.program_name == 'test_program_name'
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr


# Generated at 2022-06-13 21:45:16.717893
# Unit test for constructor of class Environment
def test_Environment():
    environ = Environment()
    assert environ.is_windows == is_windows
    assert os.path.exists(str(environ.config_dir))
    assert environ.stdin == sys.stdin
    assert environ.stdin_isatty == sys.stdin.isatty()
    assert environ.stdout == sys.stdout
    assert environ.stdout_isatty == sys.stdout.isatty()
    assert environ.stderr == sys.stderr
    assert environ.stderr_isatty == sys.stderr.isatty()


# Generated at 2022-06-13 21:45:27.257840
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin = sys.stdin, stdout = sys.stdout, stderr = sys.stderr, is_windows = True, config_dir = DEFAULT_CONFIG_DIR, stdin_isatty = True, stdout_isatty = True, stderr_isatty = True, program_name = "http")
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.is_windows == True
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin_isatty == True
    assert env.stdout_isatty == True
    assert env.stderr_isatty == True

# Generated at 2022-06-13 21:45:37.861266
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    import os
    import pathlib
    env = Environment()
    assert env.is_windows == True
    assert env.config_dir == pathlib.Path(os.path.expanduser('~')) / '.config' / 'httpie'
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == True
    assert env.stdin_encoding == 'utf8'
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == True
    assert env.stdout_encoding == 'cp936'
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == True
    assert env.program_name == 'http'
    assert env.colors == 256

# Generated at 2022-06-13 21:45:51.572622
# Unit test for constructor of class Environment
def test_Environment():
    import tempfile
    import io
    import os
    import os.path
    import sys

    env = Environment()


# Generated at 2022-06-13 21:45:59.587936
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout_encoding='gbk')
    print(env.stdout_encoding)
    env.stderr_isatty = False
    print(env.stderr_isatty, env.stdout_encoding)

if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:46:04.320535
# Unit test for constructor of class Environment
def test_Environment():
    if not curses:
        return
    assert curses

    env = Environment()
    out = str(env)
    assert isinstance(out, str)
    assert out.startswith('<Environment ')
    assert out.endswith('>')


default_env = Environment()

# Generated at 2022-06-13 21:46:12.142767
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.config_dir
    assert env.stdin
    assert env.stdin_isatty
    assert env.stdin_encoding
    assert env.stdout
    assert env.stdout_isatty
    assert env.stdout_encoding
    assert env.stderr
    assert env.stderr_isatty
    assert env.colors
    assert env.program_name
    assert env.is_windows

# Generated at 2022-06-13 21:46:15.554456
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    str(env)
    repr(env)
    env.log_error("Error")
# end

if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:46:28.108621
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=1, is_windows=False, config_dir=2,
                      stdin=3, stdin_isatty=True, stdin_encoding='utf8',
                      stdout=4, stdout_isatty=True, stdout_encoding='utf8',
                      stderr=5, stderr_isatty=True, colors=256,
                      program_name='http')
    assert isinstance(env, Environment)
    assert env.devnull == 1
    assert env.is_windows == False
    assert env.config_dir == 2
    assert env.stdin == 3
    assert env.stdin_isatty == True
    assert env.stdin_encoding == 'utf8'
    assert env.stdout == 4

# Generated at 2022-06-13 21:46:37.527279
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin=None, stdout=None, stderr=None, config_dir=None, program_name=None)
    assert env.stdin is None
    assert env.stdout is None
    assert env.stderr is None
    assert env.config_dir is None
    assert env.program_name == 'http'

# Generated at 2022-06-13 21:46:44.909661
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdin_encoding == sys.stdin.encoding or 'utf8'
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding == sys.stdout.encoding or 'utf8'
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()

if __name__ == '__main__':
    test_Environment

# Generated at 2022-06-13 21:46:55.743187
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()

    assert type(env) == Environment
    assert hasattr(env, 'is_windows')
    assert hasattr(env, 'config_dir')
    assert hasattr(env, 'stdout_encoding')
    assert hasattr(env, 'stdout_isatty')
    assert hasattr(env, 'stdin_isatty')
    assert hasattr(env, 'stdin_encoding')
    assert hasattr(env, 'stderr_isatty')
    assert hasattr(env, 'program_name')
    assert hasattr(env, 'config')
    assert hasattr(env, 'devnull')
    assert env.stdin_isatty == env.stdin.isatty() if env.stdin else False
    assert env.stdout_isatty == env.stdout

# Generated at 2022-06-13 21:47:03.264154
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment(stdin_isatty=False, stdin_encoding=None, stdout_isatty=False, stdout_encoding=None, stderr_isatty=True)
    assert e.stdin_isatty == False
    assert e.stdin_encoding == None
    assert e.stdout_isatty == False
    assert e.stdout_encoding == None
    assert e.stderr_isatty == True

# Generated at 2022-06-13 21:47:16.590572
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    import os
    from httpie.config import DEFAULT_CONFIG_DIR
    from httpie.utils import repr_dict
    from pathlib import Path
    from io import StringIO, BytesIO

    class DummyStream:
        encoding = 'latin1'
        isatty = False

    sys.stdin = StringIO('Foobar')
    sys.stdout = StringIO()
    sys.stderr = StringIO()
    os.environ['LANG'] = 'de_DE.UTF-8'
    os.environ['LC_ALL'] = 'de_DE.UTF-8'
    os.environ['LC_MESSAGES'] = 'de_DE.UTF-8'

    environment = Environment()

    assert environment.is_windows is False

# Generated at 2022-06-13 21:47:27.778206
# Unit test for constructor of class Environment
def test_Environment():
    import requests
    env = Environment(**requests.__dict__)
    assert hasattr(env, '_requests')

    import io
    f = io.StringIO()
    # f is file-like object
    env = Environment(stdout=f, stdin_encoding="utf-8", stderr_encoding="gbk")
    assert env.stdout == f
    assert env.stdout_encoding == "utf-8"
    assert env.stderr_encoding == "gbk"
    # f = open(os.devnull, 'w')
    # env = Environment(stdout=f, stderr_encoding="gbk")
    # assert env.stdout_encoding == ""
    # assert env.stderr_encoding == "gbk"



# Generated at 2022-06-13 21:47:30.860315
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment(foo=42).foo == 42
    # Test to see if it accepts non-existent attributes
    Environment(x=42) 
    # Test to see if it accepts invalid type of values
    Environment(foo="42")

# Generated at 2022-06-13 21:47:32.921084
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull='something')
    assert env.devnull == 'something'



# Generated at 2022-06-13 21:47:39.459557
# Unit test for constructor of class Environment
def test_Environment():
    class MyEnv(Environment):
        def __init__(self, **kwargs):
            self.foo = kwargs.get('foo')
            self.bar = kwargs.get('bar')
            assert all(hasattr(type(self), attr) for attr in kwargs.keys())

    env = MyEnv(foo='baz', bar=42)
    assert env.foo == 'baz'
    assert env.bar == 42


env = Environment()

# Generated at 2022-06-13 21:47:52.616575
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull = '/dev/null', is_windows = False, 
        config_dir = '~/.config/httpie',
        stdin = sys.stdin, stdin_isatty = True, 
        stdin_encoding = 'utf8',      
        stdout = sys.stdout, stdout_isatty = True, stdout_encoding = 'utf8',
        stderr = sys.stderr, stderr_isatty = True,
        colors = 256, program_name = 'http',
        )
    print(env)
    print(env.devnull)
    env.devnull = None
    print(env.devnull)

# test main
if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:48:06.443140
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

# Generated at 2022-06-13 21:48:14.557034
# Unit test for constructor of class Environment
def test_Environment():
    args = [
            '--ignore-stdin',
            '--output',
            'output',
            '--verbose',
            '--print',
            'bBH'
            ]
    env = Environment(*(args))
    assert env.__str__() == """{'is_windows': False, 'config_dir': '/home/httpie/.config/httpie', 'stdin': <_io.TextIOWrapper encoding='UTF-8'>}"""

# Generated at 2022-06-13 21:48:17.696535
# Unit test for constructor of class Environment
def test_Environment():
    # Create an instance of environment class
    env = Environment()

    # Check whether the class has been initialized properly
    assert env != None


# Generated at 2022-06-13 21:48:25.482644
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=True, is_windows=False, program_name='http')
    assert env.devnull == True
    assert env.is_windows == False
    assert env.program_name == 'http'

# Generated at 2022-06-13 21:48:33.697161
# Unit test for constructor of class Environment
def test_Environment():
    conf = 'some_config_file'
    enc = 'utf8'
    stdin = sys.stdin
    stdout = sys.stdout
    stderr = sys.stderr
    env = Environment(config_dir=conf, stdin_encoding=enc, stdin=stdin,
                      stdout=stdout, stderr=stderr)
    assert env.config_dir == conf
    assert env.stdin_encoding == enc
    assert env.stdin == stdin
    assert env.stdout == stdout
    assert env.stderr == stderr

# Generated at 2022-06-13 21:48:42.364327
# Unit test for constructor of class Environment
def test_Environment():
    try:
        env = Environment(
            devnull="/dev/null",
            stderr=sys.stderr,
            stderr_isatty=True,
            stderr_encoding="utf-8",
            stdin=None,
            stdout=sys.stderr,
            stdout_isatty=True,
            stdout_encoding="utf-8",
            program_name='http',
            is_windows=False
        )
        assert env.stdin is None
        assert env.stdout_isatty
        assert env.program_name == 'http'
    except Exception as e:
        print(e)


env: Environment = Environment()
config_dir = env.config_dir

# Generated at 2022-06-13 21:48:56.475029
# Unit test for constructor of class Environment
def test_Environment():
    import io
    env = Environment()
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin is sys.stdin
    assert env.stdout is sys.stdout
    assert env.stderr is sys.stderr
    assert env.colors == 256
    assert env.program_name == 'http'
    env = Environment(
        devnull=io.BytesIO(),
        config_dir='/custom/config/dir',
        stdin=io.BytesIO(),
        stdout=io.BytesIO(),
        stderr=io.BytesIO(),
        colors=16,
        program_name='my_program'
    )
    assert env.config_dir == Path('/custom/config/dir')
    assert env.stdin is not sys.stdin

# Generated at 2022-06-13 21:49:11.627251
# Unit test for constructor of class Environment
def test_Environment():
    # 实例化对象
    env = Environment(**{
        'config_dir': Path('/root'),
        'stdin': sys.stdin,  # `None` when closed fd (#791)
        'stdin_isatty': sys.stdin.isatty() if sys.stdin else False,
        'stdin_encoding': None,
        'stdout': sys.stdout,
        'stdout_isatty': sys.stdout.isatty(),
        'stdout_encoding': None,
        'stderr': sys.stderr,
        'stderr_isatty': sys.stderr.isatty(),
        'colors': 256,
    })

    # 使用实例化对

# Generated at 2022-06-13 21:49:16.104527
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=1, colors=2, stdin=3)
    assert env.devnull == 1
    assert env.colors == 2
    assert env.stdin == 3


# Generated at 2022-06-13 21:49:25.176423
# Unit test for constructor of class Environment
def test_Environment():
	env = Environment(is_windows=True, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, devnull=os.devnull, config_dir=Path("/home/config"))
	assert env.is_windows is True
	assert env.stdin is sys.stdin
	assert env.stdout is sys.stdout
	assert env.stderr is sys.stderr
	assert env.devnull == os.devnull
	assert env.config_dir == Path("/home/config")

# Generated at 2022-06-13 21:49:43.580463
# Unit test for constructor of class Environment
def test_Environment():
    # noinspection PyUnusedLocal
    env = Environment(stdin=None, stdout=None, stderr=None)
    # Should not raise any exception

# Generated at 2022-06-13 21:49:56.360218
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    # Test that all attributes of class "Environment" have a value
    assert bool(env.is_windows)
    assert bool(env.config_dir)
    assert bool(env.stdin)
    assert bool(env.stdin_isatty)
    assert bool(env.stdin_encoding)
    assert bool(env.stdout)
    assert bool(env.stdout_isatty)
    assert bool(env.stdout_encoding)
    assert bool(env.stderr)
    assert bool(env.stderr_isatty)
    assert bool(env.program_name)

# Generated at 2022-06-13 21:50:06.902058
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=None, is_windows=None, config_dir=None, stdin=None, stdin_isatty=None, stdin_encoding=None, stdout=None, stdout_isatty=None, stdout_encoding=None, stderr=None, stderr_isatty=None, colors=None, program_name=None)
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty() if sys.stdin else False
    assert env.stdin_encoding == None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.std

# Generated at 2022-06-13 21:50:10.136784
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.config is not None