

# Generated at 2022-06-13 21:40:30.333374
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name='http')
    assert env.program_name == 'http'
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin  # `None` when closed fd (#791)
    assert env.stdin_isatty == (sys.stdin.isatty() if sys.stdin else False)
    assert env.stdin_encoding == (getattr(sys.stdin, 'encoding', None) or 'utf8')
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()

# Generated at 2022-06-13 21:40:37.696394
# Unit test for constructor of class Environment
def test_Environment():
    # Check if init takes correct parameters
    env = Environment(is_windows=True, config_dir="httpie", stdin="1", stdout="2", stderr="3")
    assert env.is_windows == True
    assert env.config_dir == Path("httpie")
    assert env.stdin == "1"
    assert env.stdout == "2"
    assert env.stderr == "3"

    # Check if it throws exception when given wrong parameters
    try:
        env = Environment(is_windows=1)
    except:
        pass
    else:
        assert False, "Environment init should have thrown exception"


# Generated at 2022-06-13 21:40:49.039615
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    env = Environment(program_name='http',
                      config_dir=DEFAULT_CONFIG_DIR,
                      stdin=sys.stdin,
                      stdin_encoding=sys.stdin.encoding,
                      stdout=sys.stdout,
                      stdout_encoding=sys.stdout.encoding,
                      stderr=sys.stderr,
                      stderr_isatty=sys.stderr.isatty(),
                      colors=256,
                      is_windows=is_windows)
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_encoding == sys.stdin.encoding
    assert env.stdout == sys.stdout

# Generated at 2022-06-13 21:41:02.821075
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        config_dir='~',
        stdin=None,
        stdin_isatty=False,
        stdin_encoding='utf8',
        stdout=sys.stdout,
        stdout_isatty=False,
        stdout_encoding='utf8',
        stderr=sys.stderr,
        stderr_isatty=False,
        colors=256,
        program_name='http',
    )
    assert env.config_dir == '~'
    assert env.stdin_isatty is False
    assert env.stdin_encoding == 'utf8'
    assert env.stdout == sys.stdout
    assert env.stdout_isatty is False
    assert env.stdout_encoding == 'utf8'
    assert env

# Generated at 2022-06-13 21:41:08.904016
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin=None, stdout=None, stderr=None, is_windows=False)
    assert not env.stdout_isatty
    assert not env.stderr_isatty
    assert not env.stdin_isatty



# Generated at 2022-06-13 21:41:10.945453
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert not env.__dict__ == Environment.__dict__


# Generated at 2022-06-13 21:41:17.972847
# Unit test for constructor of class Environment
def test_Environment():
    env=Environment()
    print(env)
    print(env.stdin_encoding)
    print(env.stdout_encoding)
    print(env._orig_stderr)
    print(env.config)
    print(env.devnull)


# Generated at 2022-06-13 21:41:29.372983
# Unit test for constructor of class Environment
def test_Environment():
    cwd = os.getcwd()
    stdin_encoding = 'utf8'
    stdout_encoding = 'utf8'
    stderr = sys.stderr
    stderr_isatty = True
    stdin = sys.stdin
    stdin_isatty = True
    stdout = sys.stdout
    stdout_isatty = True
    config_dir = os.path.join(cwd, '.httpie')
    program_name = 'http'

# Generated at 2022-06-13 21:41:30.373520
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    print(env)



# Generated at 2022-06-13 21:41:35.606162
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    import sys
    import os
    assert env.is_windows == is_windows()
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.devnull

# Generated at 2022-06-13 21:41:42.869287
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin=open(os.devnull, 'r'), stdout=sys.__stdout__, stderr=sys.__stderr__, config_file=None)
    print(env)

# Generated at 2022-06-13 21:41:54.465020
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=1)
    assert(env.is_windows == False), "Default is_windows is not correct"
    assert(str(env.config_dir) == "~/.config/httpie"), "Default config_dir is not correct"
    assert(str(env.stdin) == "<_io.TextIOWrapper name='<stdin>' mode='r' encoding='UTF-8'>"
           ), "Default stdin is not correct"
    assert(env.stdin_isatty == False), "Default stdin_isatty is not correct"
    assert(env.stdin_encoding == "UTF-8"), "Default stdin_encoding is not correct"

# Generated at 2022-06-13 21:42:11.693104
# Unit test for constructor of class Environment
def test_Environment():
    # 断言所有构造函数传入的关键字参数必须在类中存在
    # 断言一个类的所有属性必须在该类中存在
    # assert all(hasattr(type(self), attr) for attr in kwargs.keys())
    environ = Environment()
    assert environ.is_windows == True
    assert environ.config_dir == Path('/home/linjie/.config/httpie')
    assert environ.stdin == None
    assert environ.stdin_isatty == False
    assert environ.stdin_encoding == None

# Generated at 2022-06-13 21:42:23.265252
# Unit test for constructor of class Environment

# Generated at 2022-06-13 21:42:28.396470
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=None, **{'is_windows': True, 'config_dir': Path('D:\\Users\\xiaosong\\.httpie\\config.json'), 'stdin': os.fdopen(0, 'r'), 'stdin_isatty': False, 'stdin_encoding': 'utf8', 'stdout': sys.stdout, 'stdout_isatty': True, 'stdout_encoding': 'utf8', 'stderr': sys.stderr, 'stderr_isatty': True, 'colors': 256, 'program_name': 'http'})
    assert env.is_windows == True
    assert env.config_dir == Path('D:\\Users\\xiaosong\\.httpie\\config.json')

# Generated at 2022-06-13 21:42:31.380812
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout_isatty=True, config_dir='/home/config')
    assert env.stdout_isatty
    assert env.config_dir == '/home/config'


# Generated at 2022-06-13 21:42:45.425978
# Unit test for constructor of class Environment
def test_Environment():
    '''
    test for constructor of class Environment
    :return:
    '''
    env = Environment(stdout=sys.stderr, colors=8)
    assert env.stdout == sys.stderr
    assert env.colors == 8
    assert env.is_windows == sys.platform.startswith('win')
    assert not env.config_dir
    assert env.stdin_isatty is sys.stdin.isatty()
    assert env.stdout_isatty is sys.stderr.isatty()
    assert env.stderr_isatty is sys.stderr.isatty()
    assert 'stdin' in repr(env)


# Generated at 2022-06-13 21:43:00.500239
# Unit test for constructor of class Environment
def test_Environment():
    class TestEnv(Environment):
        def __init__(self,**kwargs):
            super().__init__(**kwargs)
            # assert all(hasattr(type(self), attr) for attr in kwargs.keys())

    env = TestEnv(is_windows=True,config_dir=Path(".config"),stdin=sys.stdin,stdin_isatty=True,stdin_encoding='utf-8',
                        stdout=sys.stdout,stdout_isatty=True,stdout_encoding='utf-8',stderr=sys.stderr,stderr_isatty=True,
                        colors=256,program_name='http')
    env = TestEnv(is_windows=True)
    # print(env.is_windows)
# Unit test

# Generated at 2022-06-13 21:43:04.585114
# Unit test for constructor of class Environment
def test_Environment():
    environment = Environment()
    assert environment.is_windows == False
    assert environment.config_dir == DEFAULT_CONFIG_DIR
    assert environment.stdin == sys.stdin
    assert environment.stdout == sys.stdout
    assert environment.stderr == sys.stderr

# Generated at 2022-06-13 21:43:14.377568
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout=object())
    assert env.stdout is not sys.stdout
    assert env.stdout_isatty is False
    assert env.stdout_encoding is None
    assert env.stderr is sys.stderr
    assert env.stderr_isatty is sys.stderr.isatty()
    assert env.stderr_encoding is None
    assert env.colors is None

    env = Environment(stdout=sys.stdout)
    assert env.stdout is sys.stdout
    assert env.stdout_isatty is sys.stdout.isatty()
    assert env.stdout_encoding == sys.stdout.encoding
    assert env.stderr is sys.stderr