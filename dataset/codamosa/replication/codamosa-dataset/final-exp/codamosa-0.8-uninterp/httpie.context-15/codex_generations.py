

# Generated at 2022-06-13 21:40:16.809930
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name="test")
    print(env)

# Generated at 2022-06-13 21:40:26.252915
# Unit test for constructor of class Environment
def test_Environment():
    # Test the constructor with no args
    try:
        Environment()
    except AssertionError as e:
        assert str(e) == 'AssertionError'

    # Test the constructor with valid args
    environment = Environment(is_windows=False, config_dir="/home/user/.config/httpie")
    assert environment.is_windows == False
    assert environment.config_dir == Path("/home/user/.config/httpie")

    # Test the constructor with invalid args

# Generated at 2022-06-13 21:40:36.544046
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(is_windows=True, devnull=None, program_name='HTT ')
    env.config_dir = '/config'
    env.stdin = None
    env.stdout = '/stdout'
    env.stderr = '/stderr'
    if is_windows:
        env.stdout = '/stdout'
        env.stderr = '/stderr'

# Generated at 2022-06-13 21:40:48.890761
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(a='1', b=2, c=None)
    # If the key is not in the class, it should be false
    assert not hasattr(env, 'd')
    # If the key is in the class, it should be true
    assert hasattr(env, 'a')
    # If change the value, the value should be changed
    assert env.a == '1'
    env.a = '2'
    assert env.a == '2'
    assert env.b == 2
    # If the value is None, it should be true
    assert env.c is None
    env.c = '3'
    assert env.c == '3'
    # Test the __str__

# Generated at 2022-06-13 21:40:54.292035
# Unit test for constructor of class Environment
def test_Environment():
    stdin: IO = sys.stdin
    stdout: IO = sys.stdout
    stderr: IO = sys.stderr

    env = Environment(
        is_windows=True,
        devnull=True,
        config_dir='/home/',
        stdin=stdin,
        stdin_isatty=True,
        stdin_encoding=None,
        stdout=stdout,
        stdout_isatty=True,
        stdout_encoding=None,
        stderr=stderr,
        stderr_isatty=True,
        colors=256,
        program_name='http'
    )

# Generated at 2022-06-13 21:41:00.293107
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stdin.isatty()
    assert env.stdout.isatty()
    assert env.stderr.isatty()
    assert env.colors == 256


# Generated at 2022-06-13 21:41:12.757701
# Unit test for constructor of class Environment
def test_Environment():

    env = Environment()
    assert env.stdin is sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout is sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr is sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.colors == 256

    # Overwrite stdin, stdout, stderr with mock objects
    stdin = MagicMock()
    stdout = MagicMock()
    stderr = MagicMock()

    mock_stdin_isatty = MagicMock(return_value=True)

# Generated at 2022-06-13 21:41:28.027127
# Unit test for constructor of class Environment
def test_Environment():
    testenv = Environment()
    assert testenv.is_windows is False
    assert str(testenv.config_dir) == 'C:\\Users\\tao\.config\\httpie'
    assert testenv.stdin_isatty is True
    assert testenv.stdin_encoding == 'cp936'
    assert testenv.stdout_isatty is True
    assert testenv.stdout_encoding == 'cp936'
    assert testenv.stderr_isatty is True
    assert testenv.program_name == 'http'
    assert testenv.colors == 256

# Generated at 2022-06-13 21:41:31.778518
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(key1='value1', key2='value2')
    assert env.__dict__ == {'key1': 'value1', 'key2': 'value2'}

# Generated at 2022-06-13 21:41:43.277730
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.__dict__['is_windows'] == is_windows
    assert env.__dict__['config_dir'].name == DEFAULT_CONFIG_DIR.name
    assert env.__dict__['stdin'] == sys.stdin
    assert env.__dict__['stdin_isatty'] == sys.stdin.isatty()
    assert env.__dict__['stdin_encoding'] == None
    assert env.__dict__['stdout'] == sys.stdout
    assert env.__dict__['stdout_isatty'] == sys.stdout.isatty()
    assert env.__dict__['stdout_encoding'] == None
    assert env.__dict__['stderr'] == sys.stderr

# Generated at 2022-06-13 21:41:56.743980
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(config_dir='config_dir')
    assert env.config_dir == Path('config_dir')
    assert env.config.directory == Path('config_dir')

# Generated at 2022-06-13 21:42:01.290688
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    # def __init__(self, devnull=None, **kwargs):
    '''
    assert all(hasattr(type(self), attr) for attr in kwargs.keys())
    '''
    assert hasattr(env, "devnull")
    assert hasattr(env, "kwargs")
    # def __str__(self) -> str:
    assert type(str(env)) is str
# test_Environment()

# Generated at 2022-06-13 21:42:13.314104
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment(**{'devnull': 'value'})
    assert environment.devnull == 'value'
    environment = Environment(**{'devnull': 'value', 'stdin': sys.stdin})
    assert environment.devnull == 'value'
    assert environment.stdin == sys.stdin
    assert environment.stdin_isatty == False
    assert environment.stdin_encoding == None
    assert environment.stdout == sys.stdout
    assert environment.stdout_isatty == False
    assert environment.stdout_encoding == None
    assert environment.stderr == sys.stderr
    assert environment.stderr_isatty == False
    assert environment.colors == 256
    assert environment.program_name == 'http'
    assert environment.stdin is not None

# Generated at 2022-06-13 21:42:18.029321
# Unit test for constructor of class Environment
def test_Environment():
    if __name__ == '__main__':
        env = Environment(stdout_encoding="utf-8")
        print(env)
        print(env.stdout_encoding)


# Generated at 2022-06-13 21:42:25.875781
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == os.name == 'nt'
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin is sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout is sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr is sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.colors == (
        256 if curses and not env.is_windows else 0
    )
    assert env.program_name == 'http'
    assert env._orig_stderr is sys.stderr

    # stdout

# Generated at 2022-06-13 21:42:34.623923
# Unit test for constructor of class Environment
def test_Environment():
    environment__str__ = {
        'is_windows': True,
        'config_dir': 'DEFAULT_CONFIG_DIR',
        'stdin': 'sys.stdin',
        'stdin_isatty': True,
        'stdin_encoding': None,
        'stdout': 'sys.stdout',
        'stdout_isatty': True,
        'stdout_encoding': None,
        'stderr': 'sys.stderr',
        'stderr_isatty': True,
        'colors': 256,
        'program_name': 'http',
        'config': 'Config({...})',
    }
    environment = Environment(config_dir='/test')
    assert environment.config_dir == '/test'

# Generated at 2022-06-13 21:42:48.121319
# Unit test for constructor of class Environment
def test_Environment():
    # default is_windows is False
    env = Environment()
    assert env.is_windows == False

    # default stdin is None
    assert env.stdin_isatty == False

    # default stdout is sys.stdout
    assert env.stdout == sys.stdout

    # default stderr is sys.stderr
    assert env.stderr == sys.stderr

    # default program_name is "http"
    assert env.program_name == "http"

    # ----

    # overwrite is_windows with True
    env = Environment(is_windows=True)
    assert env.is_windows == True

    # overwrite stdin with sys.stdin
    env = Environment(stdin=sys.stdin)
    assert env.stdin_isatty == True

    # overwrite stdout as None

# Generated at 2022-06-13 21:42:57.286504
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    config_dir = env.config_dir
    env = Environment(devnull=True)
    config_dir2 = env.config_dir
    assert config_dir == config_dir2
    assert isinstance(env.config, Config)
    assert env.config == {}

if __name__ == "__main__":
    test_Environment()

# Generated at 2022-06-13 21:43:10.809953
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name='http', config_dir='.',
                      stdin=open(os.devnull, 'w+'),
                      stdout=open(os.devnull, 'w+'),
                      stderr=open(os.devnull, 'w+'))
    assert env.program_name == 'http', 'Attribute program_name does not match'
    assert env.config_dir == Path('.'), 'Attribute config_dir does not match'
    assert isinstance(env.stdin, IO), 'Attribute stdin is not a stream'
    assert isinstance(env.stdout, IO), 'Attribute stdout is not a stream'
    assert isinstance(env.stderr, IO), 'Attribute stderr is not a stream'



# Generated at 2022-06-13 21:43:20.731682
# Unit test for constructor of class Environment
def test_Environment():
    actual = Environment(devnull = "test", is_windows = False, config_dir = Path('/home/username/.config/httpie/config.json'),
    stdin = None, stdin_isatty = False, stdin_encoding = None, stdout = sys.stdout, stdout_isatty = True, stdout_encoding = None,
    stderr = sys.stderr, stderr_isatty = True, colors = 256, program_name = 'http')
    print(actual)

test_Environment()

# Generated at 2022-06-13 21:43:39.797381
# Unit test for constructor of class Environment
def test_Environment():
    default_env = Environment()
    assert default_env.__dict__['is_windows'] == is_windows
    assert default_env.__dict__['config_dir'] == DEFAULT_CONFIG_DIR
    assert default_env.__dict__['stdin'] == sys.stdin
    assert default_env.__dict__['stdout'] == sys.stdout
    assert default_env.__dict__['stderr'] == sys.stderr

    new_env = Environment(
        is_windows=True,
        config_dir='/home/user/',
        stdin=stdin,
        stdout=stdout,
        stderr=stderr
    )
    assert new_env.__dict__['is_windows'] == True

# Generated at 2022-06-13 21:43:46.517562
# Unit test for constructor of class Environment
def test_Environment():
    env1 = Environment()
    env2 = Environment()
    # Test case of the correct execution
    assert env1.stderr == sys.stderr
    assert env1.stderr_isatty is True
    assert env1._orig_stderr == sys.stderr
    assert env2.stderr == sys.stderr
    assert env2.stderr_isatty is True
    assert env2._orig_stderr == sys.stderr
    assert env1.config == env2.config
    # Test case of the incorrect execution
    try:
        Environment(stderr = None, devnull = sys.stderr)
        Environment(stderr = None, devnull = sys.stderr)
    except Exception:
        assert True

# Generated at 2022-06-13 21:43:54.404701
# Unit test for constructor of class Environment
def test_Environment():
    def t(actual=None, defaults=None, **kwargs):
        defaults = defaults or dict(Environment.__dict__)
        if actual is None:
            actual = dict(defaults)
        actual.update(kwargs)
        env = Environment(**kwargs)
        for key, value in actual.items():
            assert getattr(env, key) == value
    t()

    t(is_windows=False)
    t(config_dir='foo')
    t(stdin=io.BytesIO(), stdin_isatty=False)
    t(stdin_encoding='utf8')
    t(stdout=io.BytesIO(), stdout_isatty=False)
    t(stdout_encoding='utf8')

# Generated at 2022-06-13 21:44:06.150632
# Unit test for constructor of class Environment
def test_Environment():
    import io
    import pathlib
    import random
    import string
    random_string = lambda: ''.join(random.sample(string.printable, 10))
    old_env = Environment(
        stdin=io.StringIO(),
        stdin_encoding=random_string(),
        stdout=io.StringIO(),
        stdout_encoding=random_string(),
        stderr=io.StringIO(),
        stderr_isatty=random.choice([True, False]),
        config_dir=str(random.randint(111111, 999999)),
        program_name=random_string()
    )

    # Create a new environment with random attributes

# Generated at 2022-06-13 21:44:17.859775
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin=None, stdin_isatty=False, stdin_encoding=None,
                      stdout=sys.stdout, stdout_isatty=sys.stdout.isatty(), stdout_encoding=sys.stdout.encoding,
                      stderr=sys.stderr, stderr_isatty=sys.stderr.isatty(),
                      colors=256, program_name='http')
    assert env.stdin is None
    assert env.stdin_isatty is False
    assert env.stdin_encoding is None
    assert env.stdout is sys.stdout
    assert env.stdout_isatty is True
    assert env.stdout_encoding is sys.stdout.encoding
    assert env.stderr is sys.stder

# Generated at 2022-06-13 21:44:33.636188
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name="http", config_dir=Path("/some/path/config"))
    assert env.program_name == "http"
    assert env.config_dir == Path("/some/path/config")
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdin_encoding == None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding == None
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.colors == 256
    assert env._devnull == None

# Generated at 2022-06-13 21:44:37.240355
# Unit test for constructor of class Environment
def test_Environment():
    print(Environment())
    print(Environment(stdin = sys.stdin, stdout = sys.stdout, stderr = sys.stderr, devnull = os.devnull, config_dir = DEFAULT_CONFIG_DIR))


# test call to the constructor of class Config
# within function config of Environment

# Generated at 2022-06-13 21:44:39.077497
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(booldevnull=False)
    assert env.stdout_isatty

# Generated at 2022-06-13 21:44:40.230982
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment().stdin == sys.stdin

# Generated at 2022-06-13 21:44:45.335961
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin = 1, stdout = 2, stderr = 3)
    if (env.stdin == 1 and env.stdout == 2 and env.stderr == 3):
        print('test environment passed')
    else:
        print('test environment failed')


# Generated at 2022-06-13 21:45:03.272181
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        config_dir = '~/.config/http',
        stdin = sys.stdin,
        stdin_isatty = sys.stdin.isatty(),
        stdin_encoding = sys.stdin.encoding,
        stdout = sys.stdout,
        stdout_isatty = sys.stdout.isatty(),
        stdout_encoding = sys.stdout.encoding,
        stderr = sys.stderr,
        stderr_isatty = sys.stderr.isatty(),
        colors = 256,
        program_name = 'http'
    )
    assert env.config_dir == '~/.config/http'
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.std

# Generated at 2022-06-13 21:45:13.393873
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == False
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == True
    assert env.stdin_encoding == 'utf8'
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == True
    assert env.stdout_encoding == 'utf8'
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == True
    assert env.program_name == 'http'


if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:45:16.836042
# Unit test for constructor of class Environment
def test_Environment():
	env = Environment()
	print(env)
	env = Environment(stdout = sys.stderr)
	print(env)

if __name__=='__main__':
	test_Environment()

# Generated at 2022-06-13 21:45:27.318166
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        stdin=1,
        stdin_encoding='stdin_encoding',
        stdout=2,
        stdout_encoding='stdout_encoding',
        stderr=3,
        stderr_encoding='stderr_encoding',
        colors=1,
        program_name='test',
        is_windows=True,
        config_dir='test',
        devnull=4,
        _config='config',
        _orig_stderr='orig_stderr',
    )
    assert repr(env) == "<Environment {'stdin': 1, 'stdin_encoding': 'stdin_encoding', " \
                        "'stdout': 2, 'stdout_encoding': 'stdout_encoding', 'stderr': 3, " \
                       

# Generated at 2022-06-13 21:45:29.300157
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    print(env)

if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:45:33.582197
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin_encoding = "utf8",
                      stdout_encoding = "utf8",
                      stderr_encoding = "utf8",
                      config_dir = "test_directory")
    assert env.stdin_encoding == "utf8"
    assert env.stdout_encoding == "utf8"
    assert env.stderr_encoding == "utf8"
    assert env.config_dir == "test_directory"


# Generated at 2022-06-13 21:45:38.905851
# Unit test for constructor of class Environment
def test_Environment():
    args = {'is_windows': False, 'program_name': 'test'}
    env = Environment(**args)
    assert env.is_windows is False
    assert env.colors == 256
    assert env.program_name == 'test'

# Generated at 2022-06-13 21:45:41.241904
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert repr(env.colors) == '256'

# Generated at 2022-06-13 21:45:51.480653
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin_encoding='utf8')
    assert env.stdin_encoding == 'utf8'
    assert env.stdout_encoding == 'utf8'
    assert env.stderr_encoding == 'utf8'

    env = Environment(stdin_encoding=None)
    assert env.stdin_encoding == 'utf8'
    assert env.stdout_encoding == 'utf8'
    assert env.stderr_encoding == 'utf8'

    env = Environment(stdout_encoding='utf8')
    assert env.stdin_encoding == 'utf8'
    assert env.stdout_encoding == 'utf8'
    assert env.stderr_encoding == 'utf8'

    env = Environment(stdout_encoding=None)
    assert env

# Generated at 2022-06-13 21:46:04.118152
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment().is_windows == is_windows
    assert Environment().config_dir == DEFAULT_CONFIG_DIR
    assert Environment().stdin == sys.stdin
    assert Environment().stdin_isatty == sys.stdin.isatty()
    assert Environment().stdout == sys.stdout
    assert Environment().stdout_isatty == sys.stdout.isatty()
    assert Environment().stderr == sys.stderr
    assert Environment().stderr_isatty == sys.stderr.isatty()
    assert Environment().program_name == 'http'
    if is_windows:
        assert Environment().stdout_encoding == getattr(Environment().stdout, 'encoding', None)

# Generated at 2022-06-13 21:46:21.140053
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin_encoding = 'utf-8')
    assert env.__dict__['stdin_encoding'] == 'utf-8'
    assert env.__dict__['stdout_encoding'] == 'utf8'


# Generated at 2022-06-13 21:46:24.550259
# Unit test for constructor of class Environment
def test_Environment():
    # Initialize the constructor of class Environment
    env = Environment()
    print(env)

if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:46:25.913401
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment().__str__().startswith("{'config': ")

# Generated at 2022-06-13 21:46:27.915283
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=None)
    print(env)
    print(repr(env))
    print(env.config)



# Generated at 2022-06-13 21:46:38.115403
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    env.stdin = None
    # 实例属性覆盖类属性
    env.stdin_isatty = False
    env.stdin_encoding = None
    env.stdout = sys.stdout
    env.stdout_isatty = True
    env.stdout_encoding = None
    env.stderr = sys.stderr
    env.stderr_isatty = True
    env.colors = 256
    env.program_name = 'http'
    env.is_windows = is_windows

    assert env.stdin == None
    print(env.stdin)
    assert env.stdin_isatty == False
    assert env.stdin_encoding == None
    assert env

# Generated at 2022-06-13 21:46:39.661006
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment().stdin is not None
    assert Environment(stdin=None).stdin is None

# Generated at 2022-06-13 21:46:52.399056
# Unit test for constructor of class Environment
def test_Environment():
    """Unit test for constructor of class Environment"""
    # The default
    env = Environment()
    print(repr(env))
    # if __name__ == 'main':
    #   env = Environment()
    #   print(repr(env))
    env2 = Environment(
        stdin=None,
        stdin_encoding='ascii',
        stdout=None,
        stdout_encoding='ascii',
        program_name='http'
    )

# Generated at 2022-06-13 21:46:59.728175
# Unit test for constructor of class Environment
def test_Environment():
    environ = Environment()
    assert environ.is_windows == is_windows
    assert environ.config_dir == DEFAULT_CONFIG_DIR
    assert environ.stdin == sys.stdin
    assert environ.stdin_encoding == None
    assert environ.stdout == sys.stdout
    assert environ.stdout_encoding == None
    assert environ.stderr == sys.stderr
    assert environ.colors == 256
    assert environ.program_name == 'http'
    assert environ._orig_stderr == sys.stderr
    #assert environ._devnull == None
    assert environ.config == None
    assert environ.devnull == None

# Generated at 2022-06-13 21:47:04.854516
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert type(env) == Environment
    assert env.config_dir == DEFAULT_CONFIG_DIR
if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:47:15.180638
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert type(env) == Environment
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

# Generated at 2022-06-13 21:47:55.013951
# Unit test for constructor of class Environment
def test_Environment():
    from io import StringIO
    import sys

    env = Environment()
    assert env.is_windows == sys.platform == 'win32'
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.stdin == sys.stdin
    #assert env.stdin_encoding == 'utf8'
    assert env.stdout_encoding == 'utf8'
    assert env.stderr_encoding == 'utf8'
    assert env.stdin_isatty == True
    assert env.stdout_isatty == True
    assert env.stderr_isatty == True

    stdin = StringIO()
    #stdout = sys.stdout
    stderr = StringIO()


# Generated at 2022-06-13 21:47:59.169533
# Unit test for constructor of class Environment
def test_Environment():
    tmp_env = Environment(is_windows=True)
    print(tmp_env)
    print(tmp_env.config)
    print(tmp_env.devnull)


if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:48:06.149019
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull = open(os.devnull, 'w+'),
                      program_name='http',
                      stdin=open(os.devnull, 'w+'),
                      stdout=open(os.devnull, 'w+'),
                      stderr=open(os.devnull, 'w+'),
                      config_dir=Path('.config'),
                      colors=0,
                      is_windows=True
                      )
    print(env)
    print(env.devnull)

if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:48:11.412315
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(foo=1)
    assert env.foo == 1
    env = Environment(foo=1, stdout_encoding='utf8')
    assert env.foo == 1
    assert env.stdout_encoding == 'utf8'


# Generated at 2022-06-13 21:48:23.097600
# Unit test for constructor of class Environment
def test_Environment():
    if not os.path.isfile('./temp;'):
        os.system('touch ./temp')
    # Create a class Environment object
    env = Environment()

    # Test the stdin attribute and the stdin_encoding attribute
    assert type(env.stdin) == io.TextIOWrapper
    assert env.stdin_encoding == 'UTF-8'

    # Test the stdout_encoding attribute
    assert env.stdout_encoding == 'UTF-8'

    # Test the program_name attribute
    assert env.program_name == 'http'

    # Test the colors attribute
    assert type(env.colors) == int

    # Test the __str__ method
    assert str(env).__contains__("<class 'httpie.Environment'")

    # Test the config property

# Generated at 2022-06-13 21:48:26.443808
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment(program_name='httpie_test')


# Generated at 2022-06-13 21:48:36.164288
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    environment = Environment(stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)
    assert sys.stdin == environment.stdin
    assert sys.stdout == environment.stdout
    assert sys.stderr == environment.stderr
    assert DEFAULT_CONFIG_DIR == environment.config_dir
    assert environment == environment
    assert environment.__repr__() == '<Environment {http://www.env.com}>'
    assert environment.__str__() == 'http://www.env.com'
    assert environment.is_windows is False
    assert environment._orig_stderr is None
    assert environment._devnull is None
    assert environment._config is None
    assert environment.program_name == 'http'
    assert environment.stdin_is

# Generated at 2022-06-13 21:48:44.787293
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

    from httpie.utils import open_file

    env = Environment()
    assert env
    assert env.is_windows == sys.platform == 'win32'
    assert env.config_dir == Path(os.environ.get(
        'XDG_CONFIG_HOME', '~/.config')) / 'httpie'
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty() if sys.stdin else False
    assert env.stdout == sys.stdout

# Generated at 2022-06-13 21:48:51.670072
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name='http', config_dir='/u/as/d')
    assert env.program_name == 'http'
    assert env.config_dir == '/u/as/d'
    assert not env.is_windows


# Generated at 2022-06-13 21:49:00.606313
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        is_windows=1,
        config_dir=Path('a'),
        stdin='a',
        stdin_isatty=0,
        stdin_encoding='a',
        stdout='a',
        stdout_isatty=0,
        stdout_encoding='a',
        stderr='a',
        stderr_isatty=0,
        colors=256,
        program_name='a',
        devnull='a',
    )
    assert env.is_windows == 1
    assert env.config_dir == Path('a')
    assert env.stdin == 'a'
    assert env.stdin_isatty == 0
    assert env.stdin_encoding == 'a'
    assert env.stdout == 'a'
    assert env

# Generated at 2022-06-13 21:50:06.358498
# Unit test for constructor of class Environment
def test_Environment():
    # Create an instance of Environment
    env = Environment()
    assert isinstance(env, Environment)

    # Create an instance of Environment and overwrite the standard
    # input, output and error stream
    env = Environment(stdin=sys.stdin, stdout=sys.stdout,\
        stderr=sys.stderr)

    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr

    # Assert that the attribute type is set to the default configuration
    assert isinstance(env.config, Config)
    assert isinstance(env.config_dir, Path)
    assert isinstance(env.stdin, IO)
    assert isinstance(env.stdin_isatty, bool)