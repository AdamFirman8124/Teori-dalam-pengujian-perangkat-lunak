

# Generated at 2022-06-13 21:40:27.032491
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert isinstance(env, Environment)
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty
    assert os.isatty(sys.stdin.fileno())
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.is_windows == is_windows
    assert env.program_name == 'http'
    assert env.colors == 256

# Generated at 2022-06-13 21:40:36.343195
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment() # default value
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.stdin_encoding == 'utf8'
    assert env.stdout_encoding == 'utf8'
    assert env.program_name == 'http'
    assert env.config_dir == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:40:48.795733
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull = sys.stdin,
                      is_windows = True,
                      config_dir = DEFAULT_CONFIG_DIR,
                      stdin = sys.stdin,
                      stdin_isatty = True,
                      stdin_encoding = 'utf-8',
                      stdout = sys.stdout,
                      stdout_isatty = True,
                      stdout_encoding = 'utf-8',
                      stderr = sys.stderr,
                      stderr_isatty = True,
                      colors = 15,
                      program_name = 'http')
    assert env.devnull == sys.stdin
    assert env.is_windows == True
    assert env.config_dir == Path.home() / '.config/httpie'
    assert env.stdin == sys.stdin

# Generated at 2022-06-13 21:41:00.112943
# Unit test for constructor of class Environment
def test_Environment():
    # create the instance
    env = Environment()

    # test the program_name attribute
    assert env.program_name == 'http'

    # test the stderr attribute
    assert env.stderr == sys.stderr

    # test the stderr_isatty attribute
    assert env.stderr_isatty == sys.stderr.isatty()

    # test the stderr_encoding attribute
    _stderrEncoding = getattr(sys.stderr, 'encoding', None)
    _stderrEncoding = 'utf8' if _stderrEncoding is None else _stderrEncoding
    assert env.stderr_encoding == _stderrEncoding

    # test the stdout attribute
    assert env.stdout == sys.stdout

    # test the

# Generated at 2022-06-13 21:41:06.971452
# Unit test for constructor of class Environment
def test_Environment():
    envdict = vars(Environment())
    # Colors not available when curses not available
    if curses:
        assert envdict['colors'] == 256
    else:
        assert envdict['colors'] == 0
    assert envdict['program_name'] == 'http'
    assert envdict['stdout_encoding'] == 'UTF-8'


# Generated at 2022-06-13 21:41:15.784151
# Unit test for constructor of class Environment
def test_Environment():
    import io
    import tempfile

    # Test initilizing with unicode
    env = Environment(program_name=u'\u2713')
    assert env.program_name == u'\u2713'

    # Test clearing
    env.stderr = io.StringIO()
    env.log_error('foo')
    assert env.stderr.getvalue() == 'foo\n'
    env.devnull = None
    env.stderr.seek(0)
    env.log_error('foo', level='warning')
    assert env.stderr.getvalue() == 'foo\n'
    env.devnull = None

    # Test initilizing with bytes
    env = Environment(program_name=b'\xe2\x9c\x93')
    assert env.program_name == u

# Generated at 2022-06-13 21:41:28.688569
# Unit test for constructor of class Environment
def test_Environment():
    env=Environment()
    print(env.program_name)
    env=Environment(program_name='abc')
    print(env.program_name)
    env=Environment(stdout_encoding='utf8')
    print(env.stdout_encoding)
    print(env.stdin_encoding)
    env=Environment(stdin=open('README.md'), stdin_encoding='utf8')
    print(env.stdin_encoding)
    print(env.stdout_encoding)
    env=Environment(stdin=open('README.md', encoding='utf8'))
    print(env.stdin_encoding)
    print(env.stdout_encoding)

if __name__ == "__main__":
    test_Environment()

# Generated at 2022-06-13 21:41:36.401557
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        program_name='http1',
        is_windows=False,
        config_dir='/usr/local/bin/',
        stdin_isatty=True,
        stdin_encoding='ascii',
        stdout_isatty=True,
        stdout_encoding='ascii',
        stderr_isatty=True,
        colors=256,
        program_name='http1',
        devnull='/usr/local/bin/'
    )
    assert env.program_name == 'http1'
    assert env.is_windows == False
    assert env.config_dir == Path('/usr/local/bin/')
    assert env.stdin_isatty == True
    assert env.stdin_encoding == 'ascii'

# Generated at 2022-06-13 21:41:42.825043
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    # print(env.config)
    print(env.devnull)
    # env.devnull.write('test_devnull_write')
    # env.devnull.write('test_devnull_write')

if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:41:44.739728
# Unit test for constructor of class Environment
def test_Environment():
    from httpie.environment import Environment
    env = Environment()
    print(env)
    print(env.config)

# Generated at 2022-06-13 21:41:55.762328
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name='curl', config_dir='~/.curl')
    assert env.config_dir == '~/.curl'
    assert env.colors == 0
    assert env.program_name == 'curl'
    assert env.stderr is sys.stderr
    assert env.stdin is sys.stdin
    assert env.stdin_isatty is False
    assert env.stdout is sys.stdout
    assert env.stdout_isatty is False
    assert env._orig_stderr is sys.stderr
    assert env._devnull is None


if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:41:58.241926
# Unit test for constructor of class Environment
def test_Environment():
    Environment()


# Generated at 2022-06-13 21:42:02.284968
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull = '1.txt')
    assert env.devnull == '1.txt'
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout


# Generated at 2022-06-13 21:42:12.549708
# Unit test for constructor of class Environment
def test_Environment():
    #raise AssertionError
    #raise Exception
    #sys.exit(1)
    env = Environment()
    print(env)
    #env = Environment(devnull=None, is_windows=True, config_dir=DEFAULT_CONFIG_DIR, stdin=sys.stdin, stdin_isatty=True, stdin_encoding=None, stdout=sys.stdout, stdout_isatty=True, stdout_encoding=None, stderr=sys.stderr, stderr_isatty=True, colors=256, program_name="http")
    print(env)


# Generated at 2022-06-13 21:42:21.440139
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(is_windows=True)
    assert env.is_windows == True
    assert env.config_dir == Path(os.path.expanduser("~/.config/httpie/"))
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr_isatty == sys.stderr.isatty()


# Generated at 2022-06-13 21:42:31.179660
# Unit test for constructor of class Environment
def test_Environment():
    assert (is_windows == False)
    assert (sys.stdin  == sys.stdin)
    assert (sys.stdin.isatty() == sys.stdin.isatty())
    assert (sys.stdout == sys.stdout)
    assert (sys.stdout.isatty() == sys.stdout.isatty())
    assert (sys.stderr == sys.stderr)
    assert (sys.stderr.isatty() == sys.stderr.isatty())
    assert (curses == None)
    assert (curses != None)

test_Environment()

# Generated at 2022-06-13 21:42:45.740588
# Unit test for constructor of class Environment
def test_Environment():
    # Tests for each of the arguments
    devnull = open(os.devnull, 'w+')
    stdin = open(os.devnull, 'w+')
    stdout = open(os.devnull, 'w+')
    stderr = open(os.devnull, 'w+')
    config_dir = DEFAULT_CONFIG_DIR
    stdin_encoding = 'ascii'
    stdout_encoding = 'ascii'

    e = Environment(devnull=devnull, stdin=stdin, stdout=stdout, stderr=stderr, config_dir=config_dir, stdin_encoding=stdin_encoding, stdout_encoding=stdout_encoding)

    assert isinstance(e, Environment)

# Generated at 2022-06-13 21:43:00.535296
# Unit test for constructor of class Environment
def test_Environment():
    # Test for constructor with no parameters
    env = Environment()
    assert env.is_windows
    assert env.colors == 256
    assert env.program_name == 'http'
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()

    # Test for constructor with parameters
    env = Environment(is_windows=False)
    assert not env.is_windows
    assert env.colors == 256
    assert env.program_name == 'http'

# Generated at 2022-06-13 21:43:08.345536
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
    assert env.colors == 256
    assert env.program_name == 'http'


if __name__ == "__main__":
    test_Environment()

# Generated at 2022-06-13 21:43:09.069493
# Unit test for constructor of class Environment
def test_Environment():
    pass

# Generated at 2022-06-13 21:43:25.044768
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert isinstance(env.config, Config)
    config = env.config
    assert isinstance(config.verify_ssl, bool)
    assert isinstance(config.max_redirects, int)
    assert isinstance(config.timeout, int)
    assert isinstance(config.style, str)
    assert isinstance(config.colors, str)
    assert isinstance(config.history_file, str)
    assert isinstance(config.default_options, dict)
    assert isinstance(config.shortcuts, dict)
    assert config.get_config_path() == 'C:\\Users\\youqi\\.httpie'

    assert env.is_windows is True
    assert isinstance(env.config_dir, Path)
    assert env.stdin_encoding == 'utf8'
   

# Generated at 2022-06-13 21:43:26.799662
# Unit test for constructor of class Environment
def test_Environment():
    class Env(Environment):
        pass
    Env()



# Generated at 2022-06-13 21:43:30.661195
# Unit test for constructor of class Environment
def test_Environment():
    try:
        e = Environment(devnull = "hello")
        assert e.devnull == "hello"
    except:
        pass



# Generated at 2022-06-13 21:43:40.064189
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(devnull=None)
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == env.stdin.isatty()
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == env.stdout.isatty()
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == env.stderr.isatty()
    assert isinstance(env.colors, int)
    assert env.program_name == 'http'

if __name__ == '__main__':
    test_Environment()

# Generated at 2022-06-13 21:43:46.756810
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stderr_isatty == sys.stderr.isatty()

    assert env.stdin_encoding == getattr(sys.stdin, 'encoding', 'utf8')
    assert env.stdout_encoding == getattr(sys.stdout, 'encoding', 'utf8')

# Generated at 2022-06-13 21:43:54.491384
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()

    assert isinstance(env, Environment)
    assert env.__dict__ == Environment.__dict__
    assert isinstance(env.stdin, file)
    assert isinstance(env.stdout, file)
    assert isinstance(env.stderr, file)

    env = Environment(stdin=sys.stdin, stdout=sys.stdout,
                      stderr=sys.stderr, program_name='http', devnull=os.devnull, is_windows=False)

    assert isinstance(env, Environment)

# Generated at 2022-06-13 21:43:56.750142
# Unit test for constructor of class Environment
def test_Environment():
    Environment(stdout_isatty=True)


# Generated at 2022-06-13 21:43:57.401578
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment()

# Generated at 2022-06-13 21:44:04.707578
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin_isatty=True,
                      stdout_isatty=False,
                      stderr_isatty=True,
                      program_name='xxx')

    assert env.stdin_isatty == True
    assert env.stderr_isatty == True
    assert env.stdin_encoding == 'utf8'
    assert env.stdout_encoding == 'utf8'
    assert env.program_name == 'xxx'

# Generated at 2022-06-13 21:44:16.836561
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        is_windows=False,
        config_dir=DEFAULT_CONFIG_DIR,
        stdin=False,
        stdin_isatty=False,
        stdin_encoding=None,
        stdout=False,
        stdout_isatty=False,
        stdout_encoding=None,
        stderr=False,
        stderr_isatty=False,
        colors=256,
        program_name='http'
    )
    assert env.is_windows is False
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin is False
    assert env.stdin_isatty is False
    assert env.stdin_encoding is None
    assert env.stdout is False
    assert env.stdout_isat

# Generated at 2022-06-13 21:44:35.123023
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert isinstance(env, Environment)
    assert env.stdin is sys.stdin
    assert env.stdout is sys.stdout
    assert env.stderr is sys.stderr
    assert env.config_dir == DEFAULT_CONFIG_DIR
    # env.config.cache_dir = '~/.httpie'
    # assert env.config.cache_dir == '~/.httpie'
    # assert env.config.config_dir == '~/.httpie'
    # assert env.config_dir == '~/.httpie'
    env = Environment(stdin=None, stdout=sys.stderr)
    assert env.stdin is None
    assert env.stdout is sys.stderr
    assert env.config_dir == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:44:39.135517
# Unit test for constructor of class Environment
def test_Environment():
    e=Environment(is_windows=True)
    print(e)
    print(e.is_windows)
    print(type(e.is_windows))
    return e

# Generated at 2022-06-13 21:44:51.408518
# Unit test for constructor of class Environment

# Generated at 2022-06-13 21:44:54.504690
# Unit test for constructor of class Environment
def test_Environment():
    assert sys.stdin.isatty()
    assert sys.stdout.isatty()
    assert sys.stderr.isatty()
    assert Environment().colors == 256


# Generated at 2022-06-13 21:45:05.505619
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert isinstance(env, Environment)
    assert env._config is None
    assert isinstance(env.config_dir, Path)
    assert env.stdin == sys.stdin
    assert isinstance(env.stdin, IO)
    assert env.stdin_isatty
    assert env.stdin_encoding == 'utf8'
    assert env.stdout == sys.stdout
    assert isinstance(env.stdout, IO)
    assert env.stdout_isatty
    assert env.stdout_encoding == 'utf8'
    assert env.stderr == sys.stderr
    assert isinstance(env.stderr, IO)
    assert env.stderr_isatty
    assert env.program_name == 'http'


global_env = Environment()

# Generated at 2022-06-13 21:45:08.036988
# Unit test for constructor of class Environment
def test_Environment():
    args = {'stdin': None, 'stdout': 1, 'stderr': 2}
    obj = Environment(**args)
    for key, value in args.items():
        assert obj.__dict__[key] == value

# Generated at 2022-06-13 21:45:18.469822
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert is_windows == env.is_windows
    assert DEFAULT_CONFIG_DIR == env.config_dir
    assert sys == env.stdin
    assert env.stdin.isatty() == env.stdin_isatty
    if 'utf8' == env.stdin_encoding:
        assert 'utf8' == env.stdin_encoding
    assert sys.stdout == env.stdout
    assert env.stdout.isatty() == env.stdout_isatty
    if 'utf8' == env.stdout_encoding:
        assert 'utf8' == env.stdout_encoding
    assert sys.stderr == env.stderr
    assert env.stderr.isatty() == env.stderr_isatty
    assert env

# Generated at 2022-06-13 21:45:21.572376
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stderr == sys.stderr
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    if env.is_windows:
        env = Environment()
        assert env.stderr != sys.stderr
        assert env.stdin == sys.stdin
        assert env.stdout != sys.stdout

# Generated at 2022-06-13 21:45:25.293076
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(is_windows=True, config_dir='test', colors=256,
                      program_name='test')
    assert env.is_windows == True
    assert env.config_dir == 'test'
    assert env.colors == 256
    assert env.program_name == 'test'

# Generated at 2022-06-13 21:45:36.590694
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty() if sys.stdin else False
    assert env.stdin_encoding == None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding == None
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.colors == 256
    assert env.program_name == 'http'

# Generated at 2022-06-13 21:45:49.041263
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout=sys.stdout, stdin=sys.stdin)
    assert env.stdout == sys.stdout
    assert env.stdin == sys.stdin

# Generated at 2022-06-13 21:46:00.860346
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin_encoding = 'stdin', stdout_encoding = 'stdout')
    assert env.stdin_encoding == 'stdin'
    assert env.stdout_encoding == 'stdout'
    env.stdin_encoding = 'stdin2'
    assert env.stdin_encoding == 'stdin2'
    env.stdout_encoding = 'stdout2'
    assert env.stdout_encoding == 'stdout2'

# Generated at 2022-06-13 21:46:08.129480
# Unit test for constructor of class Environment
def test_Environment():
    import sys

    env = Environment()

    assert env.is_windows is sys.platform == 'win32'

    assert env.config_dir is DEFAULT_CONFIG_DIR
    assert env.stdin is sys.stdin
    assert env.stdout is sys.stdout
    assert env.stderr is sys.stderr
    assert env.stderr_isatty is sys.stderr.isatty()


# Generated at 2022-06-13 21:46:20.614284
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.is_windows == is_windows
    assert isinstance(env.config_dir, str)
    assert isinstance(env.program_name, str)
    assert isinstance(env.stdin_isatty, bool)
    assert isinstance(env.stdout_isatty, bool)
    assert isinstance(env.stderr_isatty, bool)
    assert isinstance(env.stdin_encoding, str)
    assert isinstance(env.stdout_encoding, str)
    assert isinstance(env.colors, int)
    assert isinstance(env.config, Config)

# Generated at 2022-06-13 21:46:26.717546
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdout=sys.stdout)
    print('Path:', env.stdout)
    env = Environment(stdout=sys.stdout, stderr=sys.stderr)
    print('Path:', env.stdout)
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    print('End.')


# Generated at 2022-06-13 21:46:36.853845
# Unit test for constructor of class Environment
def test_Environment():
    x = Environment()
    assert x.is_windows == True
    assert str(x.config_dir) == '\\Users\\sharangp\\AppData\\Roaming\\httpie\\'
    assert x.stdin == sys.stdin
    assert x.stdin_isatty == True
    assert x.stdin_encoding == None
    assert x.stdout == sys.stdout
    assert x.stdout_isatty == True
    assert x.stdout_encoding == None
    assert x.stderr == sys.stderr
    assert x.stderr_isatty == True
    assert x.colors == 256
    assert x.program_name == 'http'
    #assert x.tb_frame == None
    #assert x.tb_lineno == None
    z = Environment()


# Generated at 2022-06-13 21:46:39.911688
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.program_name == 'http'
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout

# Generated at 2022-06-13 21:46:52.687918
# Unit test for constructor of class Environment
def test_Environment():
    sysEnv = Environment()

    assert sysEnv.is_windows == False
    assert sysEnv.config_dir == '~/.httpie'
    assert sysEnv.stdin == '<_io.TextIOWrapper name=<stdin> mode=<stdin> encoding=UTF-8>'
    assert sysEnv.stdin_isatty == False
    assert sysEnv.stdin_encoding == 'UTF-8'
    assert sysEnv.stdout ==  '<_io.TextIOWrapper name=<stdout> mode=<stdout> encoding=UTF-8>'
    assert sysEnv.stdout_isatty == False
    assert sysEnv.stdout_encoding == 'UTF-8'

# Generated at 2022-06-13 21:47:03.909371
# Unit test for constructor of class Environment

# Generated at 2022-06-13 21:47:12.128290
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(stdin=None, stdin_isatty=False, stdin_encoding=None,
                      stdout=sys.stdout, stdout_isatty=True, stdout_encoding='utf8',
                      stderr=sys.stderr, stderr_isatty=True, colors=256, program_name='http',
                      devnull=None)
    print(env)
# test_Environment()

# Generated at 2022-06-13 21:47:26.336701
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(
        stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr,
        program_name='Program', config_dir='config_dir',
        devnull='devnull'
    )
    assert env.program_name == 'Program'
    assert env.config_dir == 'config_dir'

# Generated at 2022-06-13 21:47:27.602210
# Unit test for constructor of class Environment
def test_Environment():
    assert Environment().stdout
    assert Environment(stdout=None)
    assert Environment()

# Generated at 2022-06-13 21:47:38.277619
# Unit test for constructor of class Environment
def test_Environment():
    print('test_Environment(): begin')
    env = Environment()
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
    print(env.colors)
    print(env.program_name)
    print(type(env.config))
    print(env.devnull)
    print('test_Environment(): end')



# Generated at 2022-06-13 21:47:44.627451
# Unit test for constructor of class Environment
def test_Environment():

    env = Environment(stdin_encoding=None)
    assert env.stdin_encoding == 'utf8'

    env = Environment(stdin_encoding='utf8')
    assert env.stdin_encoding == 'utf8'

# Generated at 2022-06-13 21:47:50.802052
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment()
    e.config
    assert e.stdin_isatty is False
    assert e.stdout_isatty is True
    assert e.stderr_isatty is True
    assert e.is_windows is True
    assert e.stdin_encoding is 'utf8'
    assert e.stdout_encoding is 'utf8'

test_Environment()

# Generated at 2022-06-13 21:48:01.882215
# Unit test for constructor of class Environment
def test_Environment():
    class TempEnv(Environment):
        def __init__(self, devnull=None, **kwargs):
            super().__init__(devnull=devnull, **kwargs)
            self.stdin_encoding = None
            self.stdout_encoding = None
            self.stderr_encoding = None


# Generated at 2022-06-13 21:48:12.159617
# Unit test for constructor of class Environment
def test_Environment():

    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir == DEFAULT_CONFIG_DIR
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == sys.stdin.isatty()
    assert env.stdin_encoding == None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == sys.stdout.isatty()
    assert env.stdout_encoding == None
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()
    assert env.colors == 256
    assert env.program_name == 'http'

# Generated at 2022-06-13 21:48:20.034979
# Unit test for constructor of class Environment
def test_Environment():
    from httpie.core import main
    _env = Environment(program_name='Foo Bar')

    assert _env.program_name == 'http'

    assert _env.stdin
    assert _env.stdin_isatty == True
    assert _env.stdin_encoding == 'cp950'

    assert _env.stdout
    assert _env.stdout_isatty == True
    assert _env.stdout_encoding == 'cp950'

    assert _env.stderr
    assert _env.stderr_isatty == True

    # devnull == no output
    _env = Environment(devnull=True)
    main(argv=['Foo Bar'], env=_env)

    assert _env.config_dir == DEFAULT_CONFIG_DIR

    assert _env.program_

# Generated at 2022-06-13 21:48:22.519938
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert isinstance(env, Environment)

# Generated at 2022-06-13 21:48:27.220751
# Unit test for constructor of class Environment
def test_Environment():
    print("[INFO] Begin unit test for constructor of class Environment")
    env = Environment()
    print(env)



# Generated at 2022-06-13 21:48:38.208916
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment()
    assert env.stdin == sys.stdin
    assert env.stdout == sys.stdout
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == sys.stderr.isatty()


# Generated at 2022-06-13 21:48:40.324728
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name='http')
    assert env.program_name == 'http'


# Generated at 2022-06-13 21:48:46.358188
# Unit test for constructor of class Environment
def test_Environment():
    e = Environment()
    assert e.config_dir == DEFAULT_CONFIG_DIR
    assert e.stdin == sys.stdin


# Sanity unit tests

# Generated at 2022-06-13 21:48:57.825545
# Unit test for constructor of class Environment
def test_Environment():
    from httpie.core import main
    from httpie.cli import argparser, parse_args
    from httpie.compat import is_windows
    from httpie.output.streams import BINARY_SUPPRESSED_NOTICE
    import os
    import os.path
    import sys
    import unittest

    class TestEnvironment(unittest.TestCase):
        def setUp(self):
            self.env = Environment()

        def test_Environment_str(self):
            env = Environment()

# Generated at 2022-06-13 21:49:08.812055
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(a=1, b=2, c=3)
    import httpie.plugins
    httpie.plugins.__path__[0] = '/'
    httpie.plugins.__file__ = '/'
    # env.stdout = sys.stdout
    if env.stdout_isatty:
        env.stdout_isatty = True
    else:
        env.stdout_isatty = False
    if env.stderr_isatty:
        env.stderr_isatty = True
    else:
        env.stderr_isatty = False
    env.use_colors = True
    env.is_windows = True
    env.colors = env.colors
    env.program_name = 'http'
    env.stdin = sys.std

# Generated at 2022-06-13 21:49:19.823908
# Unit test for constructor of class Environment
def test_Environment():
    from httpie.config import default_options
    env=Environment()
    assert not isinstance(env.is_windows, bool)
    config_dir = default_options['config_dir']
    assert env.config_dir == config_dir
    config = env.config
    assert not isinstance(config, str)
    assert isinstance(config.config_dir, Path)
    assert isinstance(config.config_path, Path)
    assert isinstance(config.options, dict)
    assert isinstance(config.file, str)
    assert isinstance(config.is_valid, bool)
    assert isinstance(config.is_new, bool)
    assert not isinstance(env.stdin, str)
    assert isinstance(env.stdin_isatty, bool)

# Generated at 2022-06-13 21:49:22.202411
# Unit test for constructor of class Environment
def test_Environment():
    env = Environment(program_name='httpie')
    assert env.program_name == 'httpie'

# Generated at 2022-06-13 21:49:32.920442
# Unit test for constructor of class Environment
def test_Environment():
    # initial attributes should match defaults
    env = Environment()
    assert env.is_windows == is_windows
    assert env.config_dir.as_posix() == DEFAULT_CONFIG_DIR.as_posix()
    assert env.stdin == sys.stdin
    assert env.stdin_isatty == bool(sys.stdin)  # or None
    assert env.stdin_encoding is None
    assert env.stdout == sys.stdout
    assert env.stdout_isatty == bool(sys.stdout)  # or None
    assert env.stdout_encoding is None
    assert env.stderr == sys.stderr
    assert env.stderr_isatty == bool(sys.stderr)  # or None
    assert env.colors == 256
    assert env

# Generated at 2022-06-13 21:49:40.770557
# Unit test for constructor of class Environment
def test_Environment():
    import sys
    import os
    def __init__(self):
        pass

    class C:
        pass
    # i define a class C
    instance1 = C()
    # build an instance of C
    instance2 = C()
    # build another instance
    assert instance1 != instance2
    # instance1 and instance2 are not equal
    instance1.x = 1
    instance2.x = 2
    # Two instances of C, each of which has a different attribute x
    assert instance1.x != instance2.x
    # Now the two instances are not equal
    c_attr_names = dir(instance1)
    # get the two instances' attributes
    assert dir(C) == c_attr_names
    # the same attribute names
    instance1.__init__ = __init__

# Generated at 2022-06-13 21:49:51.443374
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
    assert env.program_name == 'http'
    if not is_windows:
        if curses:
            try:
                curses.setupterm()
                colors = curses.tigetnum('colors')
            except curses.error:
                pass

# Generated at 2022-06-13 21:50:19.724372
# Unit test for constructor of class Environment
def test_Environment():
    from httpie.core import main
    from httpie.streams import open_raw_streams
    from httpie.utils import Version

    #
    # Test Environment class constructor
    #
    # set stdin,stdout,stderr
    streams = open_raw_streams(
        stdin=sys.stdin,stdout=sys.stdout,stderr=sys.stderr,
    )
    env = Environment(
        stdin=streams.stdin,stdout=streams.stdout,stderr=streams.stderr,
        devnull=open(os.devnull, 'w+'),
    )
    assert not env.stdin_isatty
    assert env.stdout.isatty()
    assert env.stderr.isatty()

    # set env.