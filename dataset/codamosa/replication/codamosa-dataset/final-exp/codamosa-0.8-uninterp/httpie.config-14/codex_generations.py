

# Generated at 2022-06-13 21:30:04.270473
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # the environment variable HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/tmp/'
    assert get_default_config_dir() == Path('/tmp/')

    # clear the environment variable HTTPIE_CONFIG_DIR, then on Windows
    del os.environ[ENV_HTTPIE_CONFIG_DIR]
    assert get_default_config_dir() == Path(DEFAULT_WINDOWS_CONFIG_DIR)

    # the directory XDG_CONFIG_HOME is set
    os.environ[ENV_XDG_CONFIG_HOME] = '/tmp/'
    assert get_default_config_dir() == Path('/tmp/') + DEFAULT_CONFIG_DIRNAME

    # the file ~/.httpie is there

# Generated at 2022-06-13 21:30:12.494285
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    class TestConfigDict(BaseConfigDict):
        def __init__(self, path: Path):
            super().__init__(path)

    path_test1 = Path('path_test1')
    path_test2 = Path('path_test2')
    dict_test1 = TestConfigDict(path_test1)
    dict_test2 = TestConfigDict(path_test2)
    try:
        dict_test1.ensure_directory()
        dict_test2.ensure_directory()
    except OSError:
        assert False
    else:
        assert path_test1.parent.exists()
        assert path_test2.parent.exists()
        path_test1.parent.rmdir()
        path_test2.parent.rmdir()



# Generated at 2022-06-13 21:30:16.653353
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    file = Path("test/test.json")
    BaseConfigDict(file).ensure_directory()
    assert file.exists()


# Generated at 2022-06-13 21:30:27.789005
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    os.environ.pop(ENV_XDG_CONFIG_HOME, None)


# Generated at 2022-06-13 21:30:35.943327
# Unit test for function get_default_config_dir
def test_get_default_config_dir():

    # For a typical user, the directory must be ~/.config/httpie
    assert get_default_config_dir() == Path.home() / ".config" / "httpie"

    # For a user with an XDG_CONFIG_HOME, the directory must be $XDG_CONFIG_HOME/httpie
    XDG_CONFIG_HOME = Path("/xdg/home")
    os.environ[ENV_XDG_CONFIG_HOME] = str(XDG_CONFIG_HOME)
    assert get_default_config_dir() == XDG_CONFIG_HOME / "httpie"

    # For a user with an HTTPIE_CONFIG_DIR, the directory must be $HTTPIE_CONFIG_DIR
    HTTPIE_CONFIG_DIR = Path("/httpie/home")

# Generated at 2022-06-13 21:30:47.072934
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path(
        os.environ['HOME'] + '/.config/httpie'
    ) or get_default_config_dir() == Path(
        os.environ['HOME'] + '/.httpie'
    )

    # XDG
    os.environ['XDG_CONFIG_HOME'] = '/foo/bar/xdg'
    assert get_default_config_dir() == Path('/foo/bar/xdg/httpie')

    # Windows
    os.environ['APPDATA'] = '/foo/bar/appdata'
    assert get_default_config_dir() == Path(
        '/foo/bar/appdata/httpie'
    )

    # Explicit
    os.environ['HTTPIE_CONFIG_DIR'] = '/foo/bar/config'

# Generated at 2022-06-13 21:30:48.968052
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    pass



# Generated at 2022-06-13 21:30:55.566734
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config = BaseConfigDict('test_data.json')
    config.save()
    config['test'] = 'TEST'
    config.save()
    config['test'] = 'TEST1'
    config.save()
    os.remove('test_data.json')

if __name__ == '__main__':
    test_BaseConfigDict_save()

# Generated at 2022-06-13 21:31:05.910491
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    try:
        del os.environ[ENV_HTTPIE_CONFIG_DIR]
    except KeyError:
        pass

    try:
        del os.environ[ENV_XDG_CONFIG_HOME]
    except KeyError:
        pass

    home_dir = Path.home()

    # Windows
    assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Legacy
    legacy_path = home_dir / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_path.mkdir()
    assert get_default_config_dir() == legacy_path
    legacy_path.rmdir()

    # XDG
    assert get_default_config_dir() == home_dir / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT

# Generated at 2022-06-13 21:31:15.729228
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    from pathlib import Path
    from shutil import rmtree

    from httpie.config import DEFAULT_CONFIG_DIR, Config, BaseConfigDict

    config_dir = Path(DEFAULT_CONFIG_DIR).parent / 'test-httpie'

    try:
        config_dir.mkdir(mode=0o700, parents=True)
        config = Config(config_dir)
        config.save()
        assert config_dir.exists()

        assert config['__meta__']['httpie'] == __version__

    finally:
        if config_dir.exists():
            rmtree(str(config_dir))



# Generated at 2022-06-13 21:31:30.985502
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    default_config_dir = get_default_config_dir()
    print('BaseConfigDict_ensure_directory:', default_config_dir)

    def test(name, obj):
        print('Test', name)
        print('=====')
        print('path:', obj.path)
        print('parent:', obj.path.parent)
        print('exists:', obj.path.parent.exists())
        print('is_dir:', obj.path.parent.is_dir())
        obj.ensure_directory()
        print('exists:', obj.path.parent.exists())
        print('is_dir:', obj.path.parent.is_dir())
        print()

    test('httpie', Config())

# Generated at 2022-06-13 21:31:39.738061
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config = BaseConfigDict(path=Path('test_BaseConfigDict_ensure_directory.json'))
    assert config.path.exists() == False
    config.ensure_directory()
    assert config.path.exists() == True
    config.path.unlink()
    config.path.parent.rmdir()


# Generated at 2022-06-13 21:31:48.258181
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Scenario 1: OS is Windows
    assert DEFAULT_WINDOWS_CONFIG_DIR == Path(
        r'C:\Users\user\AppData\Roaming\httpie')

    #-------------------------------#
    #-----Scenario 2: OS is UNIX-----#
    #-------------------------------#

    # Scenario 2.1: $XDG_CONFIG_HOME is set
    os.environ[ENV_XDG_CONFIG_HOME] = '/tmp/xdg_config'
    assert Path('/tmp/xdg_config/httpie') == get_default_config_dir()

    # Scenario 2.2: $XDG_CONFIG_HOME is not set
    os.environ.pop(ENV_XDG_CONFIG_HOME)
    assert (Path.home() / '.config/httpie') == get

# Generated at 2022-06-13 21:31:50.545486
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:31:52.879946
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    from httpie.config import BaseConfigDict
    bcd = BaseConfigDict('path')


# Generated at 2022-06-13 21:32:02.995716
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    from pathlib import Path

    from httpie.config import BaseConfigDict

    import httpie.input.utils as iu
    import httpie.output.utils as ou
    import httpie.cli.constants as cli_constants
    import httpie.cli.argtypes as argtypes
    
    # This code block creates a temporary directory to store the config file.
    temp_dir = Path('/tmp')
    temp_dir_name = temp_dir / f'test-httpie-{iu.get_random_string(5)}'
    temp_dir_name.mkdir(mode=0o700, parents=True)

    # This code block creates a new file to store the config.
    temp_file = temp_dir_name / 'config.json'
    
    # This code creates a new config object.
   

# Generated at 2022-06-13 21:32:12.021921
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert os.environ.get('HTTPIE_CONFIG_DIR') is None
    assert is_windows is False

    home_dir = Path.home()
    # 1. explicitly set through env
    os.environ['HTTPIE_CONFIG_DIR'] = str(Path(home_dir))
    assert get_default_config_dir() == home_dir
    del os.environ['HTTPIE_CONFIG_DIR']

    # 2. Windows
    # Windows will always be False
    # assert is_windows

    # 3. legacy ~/.httpie
    assert not (Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR).exists()
    assert get_default_config_dir() == home_dir / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR

    # 4. XDG
    os

# Generated at 2022-06-13 21:32:19.562551
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    for os_name, expected_path in [
        ('posix', Path(Path.home(), '.config', 'httpie')),
        ('nt', Path(os.path.expandvars('%APPDATA%'), 'httpie'))
    ]:
        with mock.patch('httpie.config.os.name', os_name):
            assert get_default_config_dir() == expected_path

# Generated at 2022-06-13 21:32:23.013871
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import os
    config_dir = os.getcwd() + '/test/'
    path = Path(config_dir) / 'config.json'
    config = BaseConfigDict(path)
    config.save()



# Generated at 2022-06-13 21:32:27.538565
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import os
    os.environ['XDG_CONFIG_HOME'] = ""
    config_dir = get_default_config_dir()
    assert config_dir == Path.home() / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME

    os.environ['XDG_CONFIG_HOME'] = "/Users/admin/.config1"
    config_dir = get_default_config_dir()
    assert config_dir == Path('/Users/admin/.config1') / DEFAULT_CONFIG_DIRNAME


# Generated at 2022-06-13 21:32:46.192884
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():

    def mock_mkdir(mode=0o700, parents=True):
        assert mode is 0o700
        assert parents is True
        raise OSError(errno.EEXIST, os.strerror(errno.EEXIST))

    class BaseConfigDict(object):
        def __init__(self, path: Path):
            self.path = path

        def ensure_directory(self):
            self.path.parent.mkdir(mode=0o700, parents=True)

    config_dict = BaseConfigDict(Path(os.path.join(tempfile.gettempdir(), 'httpie/config.json')))
    config_dict.path.parent.mkdir = mock_mkdir
    config_dict.ensure_directory()

# Generated at 2022-06-13 21:32:50.649660
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    configdir = DEFAULT_CONFIG_DIR
    configdir.mkdir(mode=0o700, parents=True)
    configfilepath = configdir / 'config.json'
    config = BaseConfigDict(configfilepath)
    config.ensure_directory()


# Generated at 2022-06-13 21:32:57.613209
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    if is_windows:
        expected = DEFAULT_WINDOWS_CONFIG_DIR
    else:
        expected = Path.home() / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME

    assert get_default_config_dir() == expected



# Generated at 2022-06-13 21:33:02.568803
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    base_config_dict_obj = BaseConfigDict(Path('/xxxx'))
    _is_error_happened = 0
    try:
        base_config_dict_obj.ensure_directory()
    except:
        _is_error_happened = 1
    finally:
        assert _is_error_happened == 0


# Generated at 2022-06-13 21:33:14.938234
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    """
    Test https://github.com/jakubroztocil/httpie/issues/1739
    """

    # create temporary directory
    tmp_dir = Path(tempfile.mkdtemp())
    tmp_dir.joinpath('config.json').touch()
    tmp_dir.joinpath('.httpie').mkdir()
    tmp_dir.joinpath('.httpie', 'config.json').touch()
    tmp_dir.joinpath('.config').mkdir()
    tmp_dir.joinpath('.config', 'httpie').mkdir()
    tmp_dir.joinpath('.config', 'httpie', 'config.json').touch()

    os.environ[ENV_HTTPIE_CONFIG_DIR] = str(tmp_dir / '.httpie')

    # test BaseConfigDict.save with non

# Generated at 2022-06-13 21:33:17.255148
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    assert BaseConfigDict.ensure_directory.__doc__ is not None

# Generated at 2022-06-13 21:33:21.469394
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config = BaseConfigDict('BaseConfigDict_test.json')
    config['aaa'] = 'test'
    config.save()
    config.load()
    assert config['aaa'] == 'test'


# Generated at 2022-06-13 21:33:35.162767
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    # test xdg with no XDG_CONFIG_HOME
    assert get_default_config_dir() == Path.home() / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME
    # test xdg with XDG_CONFIG_HOME
    os.environ[ENV_XDG_CONFIG_HOME] = 'testhome'
    assert get_default_config_dir() == Path('testhome') / DEFAULT_CONFIG_DIRNAME
    os.environ.pop(ENV_XDG_CONFIG_HOME, None)

    # test legacy with no legacy config dir
    assert get_default_config_dir() == Path.home() / DEFAULT_RELATIVE_X

# Generated at 2022-06-13 21:33:37.711000
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR


# Generated at 2022-06-13 21:33:52.317631
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    tmpdir = Path(os.environ['TEMP'])
    if not tmpdir.exists():
        raise RuntimeError(f'Environment variable TEMP not a valid path')

    # Non-existent directory, parent does not exist
    config_dir = tmpdir / 'this-dir-does-not-exist' / 'config'
    bc = BaseConfigDict(config_dir)

    bc.ensure_directory()
    assert os.path.isdir(os.fspath(config_dir.parent))

    # Non-existent directory, parent does exist
    config_dir = tmpdir / 'config'
    bc = BaseConfigDict(config_dir)
    bc.ensure_directory()
    assert os.path.isdir(os.fspath(config_dir))

# Generated at 2022-06-13 21:34:03.248585
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    class Tester(BaseConfigDict):
        name = 'tester'
        helpurl = 'http://example.com/help'
        about = 'about the tester'

    t = Tester('/tmp/test')
    assert(t.is_new())
    t.load()
    assert(t.is_new())
    t = Tester('/tmp/test')
    with open('/tmp/test', 'w') as f:
        f.write('{}')
    t.load()

# Generated at 2022-06-13 21:34:05.170260
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path('~/.config/httpie')

# Generated at 2022-06-13 21:34:11.242132
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    config_dir = get_default_config_dir()
    print(config_dir)
    print(DEFAULT_CONFIG_DIR)
    assert config_dir == DEFAULT_CONFIG_DIR

if __name__ == "__main__":
    test_get_default_config_dir()

# Generated at 2022-06-13 21:34:22.159756
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config_dir = Path('./test_BaseConfigDict_load')
    config_dir.mkdir(parents=True)
    config_file_path = config_dir / 'config.json'
    # Test for empty config file
    config_fd = open(config_file_path, 'w')
    config_fd.close()
    config = Config(config_dir)
    config.load()
    assert(config.DEFAULTS == config)

    # Test for invalid json file
    config_fd = open(config_file_path, 'w')
    config_fd.write('{}\n')
    config_fd.close()
    try:
        config.load()
        assert False
    except ConfigFileError:
        assert True

    # Test for normal file

# Generated at 2022-06-13 21:34:29.828261
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # Create class object
    config = Config("test_config_dir")
    # Ensure that the directory does not exist
    config.path.parent.rmdir()
    # Run test
    config.ensure_directory()
    # Check whether parent directory is created
    assert config.path.parent.exists()
    # Clean up
    config.path.parent.rmdir()


# Generated at 2022-06-13 21:34:32.243726
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    baseConfigDict = BaseConfigDict(os.getcwd())
    baseConfigDict.load()
    assert True



# Generated at 2022-06-13 21:34:44.881818
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    print(
        "Testing the function: get_default_config_dir()")

    def get_default_config_dir_from_env():
        print(
            "\n\tget_default_config_dir_from_env():")
        print(
            "\t\ttest 1.1:")
        os.environ[ENV_HTTPIE_CONFIG_DIR] = "test_config_dir"
        return get_default_config_dir()

    def get_default_config_dir_from_windows():
        print(
            "\n\tget_default_config_dir_from_windows()")
        print(
            "\t\ttest 1.2.1:")
        assert is_windows is True
        print(
            "\t\ttest 1.2.2:")
        assert DEFAULT_WINDOWS

# Generated at 2022-06-13 21:34:53.196182
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config_dir = Path("/tmp/httpie/")
    config_dir.mkdir(mode=0o700, parents=True, exist_ok=True)

    class TestConfig(BaseConfigDict):
        pass

    test_config = TestConfig(Path("/tmp/httpie/config.json"))
    test_config.ensure_directory()
    assert Path("/tmp/httpie/config.json").exists()
    
    config_dir.rmdir()

# Generated at 2022-06-13 21:34:57.906327
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # 测试文件夹存在情况
    B = BaseConfigDict('.')
    assert B.path.exists()
    # 测试文件夹不存在
    B1 = BaseConfigDict('../')
    B1.ensure_directory()
    assert B1.path.exists()


# Generated at 2022-06-13 21:35:05.547418
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    configdir = Path('test.dir')
    try:
        configdir.mkdir()
        (configdir / 'test_load.json').write_text(u'{}')
        c = BaseConfigDict(path=(configdir / 'test_load.json'))
        c.load()
        assert c == {}
    finally:
        configdir.rmdir()



# Generated at 2022-06-13 21:35:18.654723
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/abc'
    assert get_default_config_dir() == Path('/abc')
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
    else:
        os.environ[ENV_XDG_CONFIG_HOME] = '/xyz'
        assert get_default_config_dir() == Path('/xyz/httpie')

test_get_default_config_dir()

# Generated at 2022-06-13 21:35:27.047525
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    HOME = Path('/home/').expanduser()
    test_path = HOME / 'test_directory'
    try:
        config_dict = BaseConfigDict(test_path)
        config_dict.ensure_directory()
        assert test_path.is_dir()
    except Exception as e:
        raise e
    finally:
        test_path.rmdir()



# Generated at 2022-06-13 21:35:34.975394
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import json
    import os
    config_dir = get_default_config_dir()
    if not config_dir.exists():
        config_dir.mkdir()
    config_file = config_dir / "config.json"

    # Default config file should be empty
    assert len(json.loads(config_file.read_text())) == 0


    os.environ[ENV_HTTPIE_CONFIG_DIR] = "test_dir"
    config_dir2 = get_default_config_dir()
    assert config_dir2.parent == Path("test_dir")

# Generated at 2022-06-13 21:35:42.143917
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    with mock.patch('os.path.expanduser') as mocked_expanduser:
        mocked_expanduser.return_value = '/home/user'
        assert get_default_config_dir() == Path('/home/user/.config/httpie')

    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/env/config/dir'
    assert get_default_config_dir() == Path('/env/config/dir')

    os.environ[ENV_HTTPIE_CONFIG_DIR] = '~/env/config/dir'
    assert get_default_config_dir() == Path('/home/user/env/config/dir')

    os.environ[ENV_HTTPIE_CONFIG_DIR] = '../env/config/dir'
    assert get_default_config_dir

# Generated at 2022-06-13 21:35:52.181153
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    def get_default_config_dir_impl():
        return str(get_default_config_dir())

    # noob case
    try:
        del os.environ[ENV_HTTPIE_CONFIG_DIR]
    except KeyError:
        pass

    try:
        del os.environ[ENV_XDG_CONFIG_HOME]
    except KeyError:
        pass

    # case 1.1 - explicitly set through env
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/some/dir'
    assert get_default_config_dir_impl() == '/some/dir'
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # case 2. Windows
    if is_windows:
        assert get_default_config_dir_impl() == str

# Generated at 2022-06-13 21:36:02.245150
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Test XDG from XDG_CONFIG_HOME
    xdg_config_dir = Path('/dir/foo/config')
    os.environ[ENV_XDG_CONFIG_HOME] = str(xdg_config_dir)
    assert get_default_config_dir() == xdg_config_dir / DEFAULT_CONFIG_DIRNAME

    # Test Linux path from home
    assert get_default_config_dir() == Path.home() / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME

    # Test Windows path
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

# Generated at 2022-06-13 21:36:07.842524
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class Test(BaseConfigDict):
        name = "test"
        helpurl = "localhost"
        about = "httpie"

    path = Path('test.json')
    config = Test(path)
    config.save()
    assert path.read_text()

# Generated at 2022-06-13 21:36:09.311303
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config = Config()
    config.save()



# Generated at 2022-06-13 21:36:21.680538
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config = Config()

    # create folder .httpie in user's home folder
    config.ensure_directory()
    assert config.directory.exists()
    assert config.directory.is_dir()

    # Check for existence of file config.json in .httpie folder
    assert (config.directory / config.FILENAME).exists()
    assert (config.directory / config.FILENAME).is_file()

    # cleanup
    config.directory.rmdir()


# Generated at 2022-06-13 21:36:33.568942
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    from pytest import approx

    from httpie import __version__

    def is_httpie_installed(to: Path):
        for file in ['http', 'https', 'httpie', 'httpsie']:
            path = to / file
            if path.exists():
                return True
        return False

    def is_windows_exe_installed(to: Path):
        for file in ['http.exe', 'https.exe', 'httpie.exe', 'httpsie.exe']:
            path = to / file
            if path.exists():
                return True
        return False

    def is_legacy_httpie_installed(to: Path):
        if to.name == 'httpie' and to.is_dir():
            return True
        else:
            return False

    # Ensure the main test subject doesn't exist

# Generated at 2022-06-13 21:36:47.031571
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import pytest
    import tempfile
    import os
    import stat
    import errno

    def makedir(*path):
        '''
        A function to make a temporary directory relative to the tmpdir
        `path` is a series of strings that will be joined together onto the
        temporary directory path
        '''
        path = os.path.join(str(tmpdir), *path)
        try:
            os.makedirs(path)
        except OSError as error:
            if error.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise error
        return path

    tmpdir = tempfile.TemporaryDirectory().name
    for fail in [False, True]:
        yield check_default_config_dir, tmpdir, None, None, fail


# Generated at 2022-06-13 21:37:00.046667
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    original_env = dict(os.environ)


# Generated at 2022-06-13 21:37:02.979902
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    file = open('test', 'w+')
    file.write('''default_options = {}''')
    file.close()


# Generated at 2022-06-13 21:37:07.125750
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config = BaseConfigDict("test")
    config.save()
    assert config["__meta__"]["httpie"] == __version__
    assert config["__meta__"]["help"] == config.helpurl
    assert config["__meta__"]["about"] == config.about



# Generated at 2022-06-13 21:37:20.767446
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    environ = os.environ.copy()
    environ[ENV_XDG_CONFIG_HOME] = '/foo/.config'
    environ[ENV_HTTPIE_CONFIG_DIR] = '/bar'

# Generated at 2022-06-13 21:37:25.451806
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    directory = Path(os.tempnam())
    assert not directory.exists()

    config = BaseConfigDict(Path(directory, 'config.json'))
    config.ensure_directory()
    assert directory.exists()



# Generated at 2022-06-13 21:37:31.912101
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config_dir = Path('')
    config = BaseConfigDict(config_dir)
    with pytest.raises(ConfigFileError) as excinfo:
        config.load()
    assert 'invalid basedict file' in str(excinfo.value)
    assert 'json.decoder.JSONDecodeError: Expecting value:' in str(excinfo.value)

# Generated at 2022-06-13 21:37:33.659436
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config = Config()
    config.ensure_directory()
    assert config.path.parent.exists()

# Generated at 2022-06-13 21:37:45.892329
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Set HTTPIE_CONFIG_DIR variable
    os.environ[ENV_HTTPIE_CONFIG_DIR] = DEFAULT_WINDOWS_CONFIG_DIR
    assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # If HTTPIE_CONFIG_DIR variable is not set,
    # and if the platform is Windows then return DEFAULT_WINDOWS_CONFIG_DIR
    del os.environ[ENV_HTTPIE_CONFIG_DIR]
    assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # If HTTPIE_CONFIG_DIR variable is not set,
    # and if the platform is not Windows then return DEFAULT_WINDOWS_CONFIG_DIR
    is_windows = False
    assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG

# Generated at 2022-06-13 21:37:50.129528
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    t = BaseConfigDict(Path('test.json'))
    t['hello'] = 'world'
    t.save()
    f = Path('test.json')
    f.read_text() == '''{
    "hello": "world"
}
'''

test_BaseConfigDict_save()

# Generated at 2022-06-13 21:38:00.694108
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    class BaseConfigDict2(BaseConfigDict):
        def __init__(self, path: Path):
            super().__init__(path)
            self['__meta__'] = {
                'httpie': __version__
            }
    config = BaseConfigDict2(Path('./config.jsonx'))
    config.ensure_directory()
    config.load()

# Generated at 2022-06-13 21:38:11.436598
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    old_home = str(Path.home())
    old_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # 1. explicitly set through env
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/tmp/config_dir'
    assert get_default_config_dir() == Path('/tmp/config_dir')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # 2. Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
        return

    # 3. legacy ~/.httpie
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir

# Generated at 2022-06-13 21:38:11.983554
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    assert False

# Generated at 2022-06-13 21:38:20.116753
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    home_dir = Path.home()
    legacy_config_dir = home_dir / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.parent.mkdir(mode=0o700, parents=True)
    legacy_config_dir.touch()
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.unlink()
    xdg_config_home = home_dir / 'xdg_config_home/'
    xdg_config_home.mkdir(mode=0o700, parents=True)
    assert get_default_config_dir() == xdg_config_home / DEFAULT_CONFIG_DIRNAME

# Generated at 2022-06-13 21:38:25.554553
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    path = Path('./abc.json')
    dic = BaseConfigDict(path)
    dic.save()
    assert path.exists()
    path.unlink()


# Generated at 2022-06-13 21:38:31.633242
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    path = Path('/data/httpie/config/0')
    config = BaseConfigDict(path)
    config['__meta__'] = {
        'httpie': __version__
    }
    config.about = "The HTTPie config file"
    config.helpurl = "https://httpie.org/docs/config"
    config.save()
    print(f'Done... with test_BaseConfigDict_save()')



# Generated at 2022-06-13 21:38:33.317221
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    assert BaseConfigDict.load()


# Generated at 2022-06-13 21:38:46.515814
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import os
    import stat
    from pathlib import Path

    file = './test_BaseConfigDict_save.json'
    f = Path(file)
    if f.exists():
        os.unlink(file)
    config = BaseConfigDict(f)
    config['key1'] = 1
    config['key2'] = '2'
    config.save()

    assert f.exists()
    assert stat.S_IMODE(f.stat().st_mode) == (stat.S_IREAD | stat.S_IWRITE)

    config = BaseConfigDict(f)
    config.load()
    assert config['key1'] == 1
    assert config['key2'] == '2'

    config.delete()
    assert not f.exists()

test_BaseConfigDict_

# Generated at 2022-06-13 21:38:55.710489
# Unit test for method save of class BaseConfigDict

# Generated at 2022-06-13 21:39:03.201560
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config_dir = get_default_config_dir()
    config_dir.mkdir(mode=0o700)
    config = Config(config_dir)
    config.ensure_directory()

    if config.path.parent.exists():
        config.path.parent.rmdir()
        config_dir.rmdir()


GLOBAL_CONFIG = Config()



# Generated at 2022-06-13 21:39:26.241366
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import json
    from pathlib import Path
    from httpie.config import BaseConfigDict
    import os
    import shutil
    # test default save
    test_save_path = Path('./test_config')
    test_save_path.mkdir()
    test_save_file_path = test_save_path / "test.json"
    test_config = BaseConfigDict(test_save_file_path)
    test_config.save()
    f = open(test_save_file_path, 'r')
    data = json.loads(f.read())
    assert data == {}
    # test update and save
    test_config['xxx'] = 'yyy'
    test_config.save()
    f = open(test_save_file_path, 'r')
    data = json.loads

# Generated at 2022-06-13 21:39:38.869399
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    """Unit test for ``get_default_config_dir``."""
    import pytest

    # no env vars, legacy ~/.httpie
    if DEFAULT_CONFIG_DIR == DEFAULT_RELATIVE_LEGACY_CONFIG_DIR:

        # $XDG_CONFIG_HOME without parent dir
        with pytest.raises(ConfigFileError) as excinfo:
            assert (
                get_default_config_dir() ==
                Path(os.environ[ENV_XDG_CONFIG_HOME]) /
                DEFAULT_CONFIG_DIRNAME
            )
        assert 'cannot read config file' in str(excinfo.value)

        # $XDG_CONFIG_HOME with parent dir; should be ok because the
        # config file is not touched

# Generated at 2022-06-13 21:39:42.913736
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    test_config = BaseConfigDict(Path('/home/test/.httpie/config.json'))
    test_config.ensure_directory()
    assert test_config.path.parent.absolute() == Path('/home/test/.httpie').absolute()

