

# Generated at 2022-06-13 21:29:54.056769
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:30:05.160868
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import tempfile
    from unittest.mock import patch

    # Without XDG_CONFIG_HOME
    with patch.dict('os.environ', {}, clear=True):
        assert get_default_config_dir() == \
            Path.home() / Path('.config/httpie')

    # With XDG_CONFIG_HOME
    with tempfile.TemporaryDirectory() as td:
        with patch.dict('os.environ', {'XDG_CONFIG_HOME': td}, clear=True):
            assert get_default_config_dir() == Path(td) / 'httpie'


# Generated at 2022-06-13 21:30:06.786245
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Test for system default value
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR



# Generated at 2022-06-13 21:30:23.875317
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # 1. explicitly set through env
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/'
    assert get_default_config_dir() == Path('/')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # 2. Windows
    if not is_windows:
        # unset XDG variables
        if ENV_XDG_CONFIG_HOME in os.environ:
            del os.environ[ENV_XDG_CONFIG_HOME]

        # 2.1 legacy ~/.httpie
        legacy_config_dir = DEFAULT_WINDOWS_CONFIG_DIR / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
        legacy_config_dir.mkdir(parents=True, exist_ok=True)
        assert get_default_config_dir

# Generated at 2022-06-13 21:30:26.725912
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config = BaseConfigDict('config.json')
    config.load()
    assert config['default_options'] == []


# Generated at 2022-06-13 21:30:33.992292
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import httpie.config as config
    import json
    my_path = config.DEFAULT_CONFIG_DIR / config.Config.FILENAME
    my_path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    myconfig = config.Config(config.DEFAULT_CONFIG_DIR)
    myconfig['key'] = 'value'
    myconfig.save()

    with open(my_path, "r") as cf:
        mydata = json.load(cf)
    # Now I want to delete the file config.json
    my_path.unlink()
    assert mydata['key'] == 'value'

# Generated at 2022-06-13 21:30:39.895417
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # check whether the directory of the file is existed or not
    if not DEFAULT_CONFIG_DIR.exists():
        # if the directory is not existed, then we create the directory and its parents
        DEFAULT_CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        # if we cannot create the directory then it will raise an error
        assert DEFAULT_CONFIG_DIR.exists(), "Cannot create the directory"
    else:
        # if the directory is existed, then we do nothing
        pass



# Generated at 2022-06-13 21:30:50.157730
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    import shutil
    import tempfile
    temp_dir = tempfile.mkdtemp()
    config_file = os.path.join(temp_dir, 'config_file')
    config_dir = os.path.join(temp_dir, 'config_dir')
    config_dir_file = os.path.join(config_dir, 'config_file')

    config = BaseConfigDict(config_dir_file)
    config.ensure_directory()

    print("Check if {0} exists: {1}".format(config_dir, os.path.exists(config_dir)))
    print("Check if {0} exists: {1}".format(config_dir_file, os.path.exists(config_dir_file)))

    assert os.path.exists(config_dir)

    shutil.r

# Generated at 2022-06-13 21:30:54.360599
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    d = BaseConfigDict(Path('test.json'))
    d.ensure_directory()
    assert os.path.isdir('test.json')
    os.rmdir('test.json')


# Generated at 2022-06-13 21:31:00.547746
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    configDir = 'test'
    path = Path(configDir)
    if path.exists():     # remove the directory if it already exists
        shutil.rmtree(configDir)
    self = BaseConfigDict(path)
    self.ensure_directory()
    assert path.exists()
    shutil.rmtree(configDir)


# Generated at 2022-06-13 21:31:11.800921
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    path = Path('test.json')
    d = BaseConfigDict(path)
    d.ensure_directory()
    res = d.path.parent.exists()
    os.removedirs(path.parent)
    if res:
        return True
    else:
        return False


# Generated at 2022-06-13 21:31:20.364568
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    # In order to test, you need to delete the folder
    # ~/.local/share/httpie, or set environment variable
    # HTTPIE_CONFIG_DIR to a folder that can be deleted.
    #
    # After setting the environment variable, execute the
    # following command before running the unit test:
    #
    # $ rm -r $HTTPIE_CONFIG_DIR
    import json

    # Test saving a file
    c = Config()
    if os.path.isfile(c.path):
        raise AssertionError('cannot run test')

    c.save()
    assert os.path.isfile(c.path)

    # Test saving a file is idempotent
    c.save()
    assert os.path.isfile(c.path)

# Generated at 2022-06-13 21:31:31.489829
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    test_path = Path('test_config.json')
    test_dict = {'test_string': 'a string',
                 'test_number': 123,
                 'test_list': [1, 2, 3],
                 'test_dict': {'key1': 1, 'key2': 2}}
    json_string = json.dumps(obj=test_dict, indent=4, sort_keys=True, ensure_ascii=True)
    try:
        test_path.write_text(json_string + '\n')
        test_config = BaseConfigDict(path=test_path)
        test_config.load()
        assert test_config == test_dict
    finally:
        test_path.unlink()



# Generated at 2022-06-13 21:31:37.858564
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    expected = Path.home() / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME
    assert expected == get_default_config_dir()



# Generated at 2022-06-13 21:31:48.757466
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '~/custom'
    assert get_default_config_dir() == Path('~/custom')

    del os.environ[ENV_HTTPIE_CONFIG_DIR]
    os.environ[ENV_XDG_CONFIG_HOME] = '~/.custom_config'
    assert get_default_config_dir() ==\
        Path('~/.custom_config') / DEFAULT_CONFIG_DIRNAME

    del os.environ[ENV_XDG_CONFIG_HOME]
    assert get_default_config_dir() ==\
        Path.home() / '.config' / DEFAULT_CONFIG_DIRNAME


if __name__ == '__main__':
    test_get_default_config_dir()

# Generated at 2022-06-13 21:31:50.852746
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config = BaseConfigDict('testfile.txt')
    config.ensure_directory()

# Generated at 2022-06-13 21:31:57.166833
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    class DummyConfig(BaseConfigDict):
        # Dummy path for passing to test
        path = Path('/foo/bar.json')

    c = DummyConfig(path = c.path)

    # Directory of given path does not exist
    c.ensure_directory()

    # Directory of path exists
    c.ensure_directory()

# Generated at 2022-06-13 21:31:59.565590
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == \
        (Path.home() / '.config' / 'httpie')

# Generated at 2022-06-13 21:32:02.145434
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    session = BaseConfigDict(path=DEFAULT_CONFIG_DIR / 'config.json')
    session.ensure_directory()
    assert os.path.exists(str(DEFAULT_CONFIG_DIR))



# Generated at 2022-06-13 21:32:05.937242
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config = BaseConfigDict(Path('/tmp/httpie'))
    config.ensure_directory()
    assert os.path.exists(config.path.parent), "Directory has not been created"


# Generated at 2022-06-13 21:32:16.628225
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    if is_windows:
        assert(get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR)
        os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
        assert(get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR)
    else:
        assert(get_default_config_dir() == DEFAULT_CONFIG_DIR)
        os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
        assert(get_default_config_dir() == DEFAULT_CONFIG_DIR)
        os.environ[ENV_HTTPIE_CONFIG_DIR] = 'whatever'
        assert(get_default_config_dir() == 'whatever')

# Generated at 2022-06-13 21:32:26.087682
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    def _test_path(path, expected):
        actual = get_default_config_dir()
        assert actual == expected, f'{path} != {expected}'
    _test_path(None, Path.home() / 'httpie')
    _test_path('/tmp', Path('/tmp'))
    _test_path('C:/tmp', Path('C:/tmp'))
    _test_path('~', Path.home())
    _test_path('.', Path.cwd())
    _test_path('..', Path.cwd().parent)
    _test_path('/tmp~', Path('/tmp~'))
    _test_path('/tmp/..', Path('/'))
    _test_path('/tmp/./abc', Path('/tmp/abc'))

# Generated at 2022-06-13 21:32:29.753551
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    try:
        config = Config()
        config.load()
    except ConfigFileError:
        print("TEST CASE FAILED: Corrupted configuration file found!")
    except:
        print("TEST CASE FAILED: An unexpected error.")
        raise


# Generated at 2022-06-13 21:32:34.874546
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config = BaseConfigDict(Path('~/config_dir/config.json'))
    config.ensure_directory()
    assert (Path('~/config_dir').exists())
    assert (Path('~/config_dir').is_dir())


# Generated at 2022-06-13 21:32:42.690863
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # test without parent directory
    config = BaseConfigDict(path=Path('./test/test_file.json'))
    assert not (Path('./test')).exists()
    assert not (Path('./test/test_file.json')).exists()

    config.ensure_directory()
    assert (Path('./test')).exists()
    assert (Path('./test/test_file.json')).exists()
    (Path('./test/test_file.json')).unlink()
    os.rmdir('./test')
    assert not (Path('./test')).exists()
    assert not (Path('./test/test_file.json')).exists()

    # test with parent directory
    (Path('./test')).mkdir()
    config

# Generated at 2022-06-13 21:32:53.900037
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # test that ensure_directory creates a directory ordinary directory
    new_dir_name = 'hello'
    new_config_path = Path(new_dir_name) / Config().FILENAME
    try:
        new_config = Config(new_dir_name)
        new_config.ensure_directory()

        # if the above method call is successful, the following should be true
        assert new_config_path.parent.exists()
    finally:
        try:
            Path(new_dir_name).rmdir()
        except OSError as e:
            print("Unable to remove directory {}".format(new_dir_name), e)

# Generated at 2022-06-13 21:33:04.071376
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Test with XDG environment variables set
    os.environ[ENV_XDG_CONFIG_HOME] = '/explicit/xdg'
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/explicit/httpie'

    assert get_default_config_dir() == Path('/explicit/httpie')

    del os.environ[ENV_HTTPIE_CONFIG_DIR]
    assert get_default_config_dir() == Path('/explicit/xdg/httpie')

    del os.environ[ENV_XDG_CONFIG_HOME]
    assert get_default_config_dir() == Path.home() / '.config/httpie'

    # Test on Windows
    import sys
    orig_platform = sys.platform
    sys.platform = 'win32'



# Generated at 2022-06-13 21:33:16.445089
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    os.environ[ENV_XDG_CONFIG_HOME] = '/test/.config'
    # for linux
    assert get_default_config_dir() == Path('/test/.config/httpie')
    os.environ[ENV_XDG_CONFIG_HOME] = '~/test/.config'
    assert get_default_config_dir() == Path(Path.home() / 'test/.config/httpie')
    # for windows
    os.environ[ENV_HTTPIE_CONFIG_DIR] = Path(os.path.expandvars('%APPDATA%')) / 'test/httpie'
    assert get_default_config_dir() == Path(os.path.expandvars('%APPDATA%')) / 'test/httpie'

# Generated at 2022-06-13 21:33:19.606556
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    from tempfile import TemporaryDirectory
    
    with TemporaryDirectory() as tmp_dir:
        config = BaseConfigDict(Path(tmp_dir) / 'config.json')
        config.ensure_directory()
        assert Path(tmp_dir).exists()


# Generated at 2022-06-13 21:33:21.783326
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    a = BaseConfigDict(path = Path("test.json"))
    a.ensure_directory()

# Generated at 2022-06-13 21:33:35.053281
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    ConfigFileError.__str__ = lambda self: self.args[0]
    import shutil
    import os
    import subprocess
    import tempfile

    temp_dir = tempfile.mkdtemp()
    print(temp_dir)
    dirpath = Path(temp_dir)
    path = dirpath / 'config.json'
    try:
        os.chmod(str(dirpath), 0o755)
        print(path)
        config = Config(directory=dirpath)
        config.load()
        config.save()

    finally:
        subprocess.call(['rm', '-rf', temp_dir])

# Generated at 2022-06-13 21:33:36.762380
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    t = BaseConfigDict(path = '/home/zhang/.httpie/config.json')
    t.load()

# Generated at 2022-06-13 21:33:38.470639
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    r = BaseConfigDict(Path('./'))
    r.save()

# Generated at 2022-06-13 21:33:49.585881
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    try:
        os.mkdir("testdir")
        testdir = Path("testdir")
        cdir = BaseConfigDict(testdir/'test')
        cdir.save()
        json_string = cdir.path.read_text()
        assert json_string == '{\n    "__meta__": {\n        "httpie": "1.0.3"\n    }\n}\n'
    except:
        assert False
    finally:
        os.remove("testdir/test")
        os.removedirs("testdir")


# Generated at 2022-06-13 21:33:56.433927
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    directory = "config/"
    path = f"{directory}config.json"
    obj = BaseConfigDict(Path(path))
    obj.ensure_directory()
    obj.save()
    assert os.path.isfile(path)
    assert os.path.isdir(directory)
    os.remove(path)
    os.rmdir(directory)

# Generated at 2022-06-13 21:33:59.550974
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    c = Config()
    c.ensure_directory()
    assert c.path.parent.exists()

# Unit tests for class Config

# Generated at 2022-06-13 21:34:12.576427
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    import tempfile

    temp_dir = Path(tempfile.gettempdir())
    random_dirname = ''.join(random.choice('0123456789ABCDEF') for i in range(16))
    config_dir = temp_dir / random_dirname
    test_config_dict = BaseConfigDict(config_dir)

    # directory with random_dirname should not exist
    assert config_dir.exists() is False

    # directory with random_dirname should now exist
    test_config_dict.ensure_directory()
    assert config_dir.exists() is True

    # deleting directory with random_dirname
    config_dir.rmdir()
    assert config_dir.exists() is False

# Generated at 2022-06-13 21:34:23.074073
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():

    class BaseConfigDict_Mock(BaseConfigDict):
        #Mock the method os.makedirs
        def makedirs(self, mode=0o700, parents=True):
            pass

    #Test the method ensure_directory of class BaseConfigDict
    #with a valid path
    base_config_dict = BaseConfigDict_Mock(Path('config.json'))
    base_config_dict.ensure_directory()

    #Test the method ensure_directory of class BaseConfigDict
    #with an error
    base_config_dict = BaseConfigDict_Mock(Path('config.json'))
    base_config_dict.makedirs = Mock()
    base_config_dict.makedirs.side_effect = OSError(13, 'Permission denied')

# Generated at 2022-06-13 21:34:32.885028
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    from pathlib import Path
    from shutil import rmtree
    from tempfile import mkdtemp
    from httpie.config.path import Config
    import json
    import os
    config_dir = mkdtemp()
    config_file = Path(config_dir, "config.json")
    config = Config(config_dir)
    config.save()
    assert os.path.exists(config_file)
    assert os.path.getsize(config_file) == 0
    config.delete()
    rmtree(config_dir)


# Generated at 2022-06-13 21:34:44.954747
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    Path.home = lambda: Path('/home/user')

    # Test case 1: HTTPIE_CONFIG_DIR explicitly set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/my/config/dir'
    assert get_default_config_dir() == Path('/my/config/dir')
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR)

    # Test case 2: Windows
    is_windows = lambda: True
    assert get_default_config_dir() == (
        Path(os.path.expandvars('%APPDATA%')) / 'httpie')
    is_windows = lambda: False

    # Test case 3: legacy ~/.httpie
    Path.exists = lambda self: str(self) == '/home/user/.httpie'
    assert get

# Generated at 2022-06-13 21:34:55.821606
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    user_dir = Path('./test_data/user_dir')
    not_exist_dir = Path('./test_data/user_dir/_not_exist_dir')
    path = Path('./test_data/user_dir/_not_exist_dir/case_insensitive_config.json')
    BaseConfigDict(path=path).ensure_directory()
    assert not_exist_dir.exists()
    shutil.rmtree(user_dir)


# Generated at 2022-06-13 21:35:00.576929
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    try:
        os.mkdir(os.getcwd()+'\\test')
    except FileExistsError:
        pass
    config = BaseConfigDict(os.path.join(os.getcwd(), 'test'))
    config.ensure_directory()
    try:
        os.remove(os.path.join(os.getcwd(), 'test'))
    except OSError:
        pass
    os.rmdir(os.getcwd()+'\\test')


# Generated at 2022-06-13 21:35:10.523346
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == \
            Path.home() / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME
    os.environ[ENV_XDG_CONFIG_HOME] = '/tmp/test'
    assert get_default_config_dir() == Path('/tmp/test') / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/tmp/test1'
    assert get_default_config_dir() == Path('/tmp/test1')

# Generated at 2022-06-13 21:35:20.693072
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    dir_path = '../test/test_config'
    config_type = 'test'
    pass_f = 0
    fail_f = 0
    try:
        config = BaseConfigDict(dir_path)
        config.ensure_directory()
        assert os.path.exists(dir_path)
        pass_f = pass_f + 1
    except:
        fail_f = fail_f + 1

    try:
        config = BaseConfigDict(dir_path)
        config.ensure_directory()
        assert os.path.exists(dir_path)
        pass_f = pass_f + 1
    except:
        fail_f = fail_f + 1


# Generated at 2022-06-13 21:35:33.856368
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    def check(got, expected):
        assert str(got).replace('\\', '/') == str(expected).replace('\\', '/')

    check(get_default_config_dir(), Path('~/.config/httpie'))

    os.environ[ENV_XDG_CONFIG_HOME] = '/tmp/xdg/config'
    check(get_default_config_dir(), Path('/tmp/xdg/config/httpie'))

    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/tmp'
    check(get_default_config_dir(), Path('/tmp'))

    os.environ.pop(ENV_HTTPIE_CONFIG_DIR)
    os.environ.pop(ENV_XDG_CONFIG_HOME)

    if is_windows:
        os

# Generated at 2022-06-13 21:35:43.592124
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Test default case
    get_default_config_dir()

    # Test xdg config home case
    os.environ[ENV_XDG_CONFIG_HOME] = '/tmp'
    path = get_default_config_dir()
    assert path == Path('/tmp/httpie')

    # Test windows case
    os.environ['APPDATA'] = '/AppData/Roaming'
    path = get_default_config_dir()
    assert path == Path('/AppData/Roaming/httpie')

    # Test windows case with APPDATA='C:\\Users\\user\\AppData\\Roaming'
    os.environ['APPDATA'] = 'C:\\Users\\user\\AppData\\Roaming'
    path = get_default_config_dir()

# Generated at 2022-06-13 21:35:47.349710
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
        path = Path("/tmp")
        config_dict = BaseConfigDict(path)
        result = config_dict.ensure_directory()
        assert result == None

# Generated at 2022-06-13 21:35:52.889590
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() / Path('.config') / DEFAULT_CONFIG_DIRNAME
    assert get_default_config_dir().exists()
    assert get_default_config_dir() == Config().directory

# Generated at 2022-06-13 21:35:59.593229
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config_dir = Path('.test_httpie')
    try:
        class TestConfig(BaseConfigDict):
            pass
        instance = TestConfig(config_dir)
        instance.ensure_directory()
        assert config_dir.parent.exists() 
    finally:
        if config_dir.parent.exists():
            config_dir.parent.rmdir()


# Generated at 2022-06-13 21:36:06.327248
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    home = Path('~')
    home = Path(os.path.expanduser('~'))
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
    else:
        if os.environ.get(ENV_HTTPIE_CONFIG_DIR):
            assert get_default_config_dir() == Path(os.environ.get(ENV_HTTPIE_CONFIG_DIR))
        elif (home / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR).exists():
            assert get_default_config_dir() == home / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR

# Generated at 2022-06-13 21:36:10.658656
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:36:28.240388
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # 1. explicitly set through env
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/httpie'
    assert get_default_config_dir() == Path('/httpie')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # 2. Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # 3. legacy ~/.httpie
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(mode=0o700, exist_ok=True)
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()

    # 4. XDG
   

# Generated at 2022-06-13 21:36:30.281756
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR


# Generated at 2022-06-13 21:36:45.200516
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    env = os.environ.copy()

    def expect(expected_dir, **kwargs):
        env.update(kwargs)
        assert get_default_config_dir() == expected_dir

    home = Path.home()
    legacy_config_dir = home / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    xdg_config_home_dir = home / DEFAULT_RELATIVE_XDG_CONFIG_HOME
    xdg_config_dir = xdg_config_home_dir / DEFAULT_CONFIG_DIRNAME
    default_config_dir = DEFAULT_WINDOWS_CONFIG_DIR
    if is_windows:
        assert get_default_config_dir() == default_config_dir

# Generated at 2022-06-13 21:36:47.956629
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path(os.path.expanduser('~/.config/httpie'))

# Generated at 2022-06-13 21:36:53.118952
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    test_file = Path('test/test_save_file.json')
    if os.path.exists(test_file):
        os.remove(test_file)
    config = Config(test_file)
    config.save()
    if os.path.exists(test_file):
        os.remove(test_file)


# Generated at 2022-06-13 21:36:56.441225
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import pytest

    with pytest.raises(ConfigFileError):
        cfg = BaseConfigDict(Path('/'))
        cfg.save()

# Generated at 2022-06-13 21:37:04.419454
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    class MyConfigDict(BaseConfigDict):
        def __init__(self, path):
            super().__init__(path=path)

    base_path = Path.cwd()/'testDir'
    config_file = base_path/'testConfig'
    myConfigDict = MyConfigDict(config_file)

    myConfigDict.ensure_directory()

    assert base_path.exists()

# Generated at 2022-06-13 21:37:15.068691
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import os
    from pathlib import Path

    from xdg import BaseDirectory

    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)

    # 1. explicitly set through env
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/foo/bar/baz'
    assert get_default_config_dir() == '/foo/bar/baz'

    os.environ.pop(ENV_HTTPIE_CONFIG_DIR)

    # 2. Windows
    if is_windows:
        assert get_default_config_dir() == Path(os.path.expandvars('%APPDATA%')) / 'httpie'
        return

    # 3. legacy ~/.httpie
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY

# Generated at 2022-06-13 21:37:26.594354
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    def ensure_envvars_cleared():
        if envvar_httpie_config_dir in os.environ:
            del os.environ[envvar_httpie_config_dir]
        if envvar_xdg_config_home in os.environ:
            del os.environ[envvar_xdg_config_home]

    envvar_httpie_config_dir = ENV_HTTPIE_CONFIG_DIR
    envvar_xdg_config_home = ENV_XDG_CONFIG_HOME
    home = Path.home()

    # case 1: explicitly set through env
    os.environ[envvar_httpie_config_dir] = '/foo/bar'
    assert get_default_config_dir() == Path('/foo/bar')
    ensure_envvars_cleared()

# Generated at 2022-06-13 21:37:39.414847
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    from httpie_tempfile import NamedTemporaryJSONFile
    tmp_file = NamedTemporaryJSONFile.create()
    class TestDict(BaseConfigDict):
        name = None
        helpurl = None
        about = None
    the_dict = TestDict(path=Path(tmp_file.name))
    the_dict['o'] = 'p'
    the_dict.save()
    from httpie.output.exception import ParseError
    parsed_dict = None
    try:
        parsed_dict = json.load(open(tmp_file.name))
    except Exception as e:
        if isinstance(e, ParseError):
            print('Config file {} parse failed.'.format(tmp_file.name))
    assert parsed_dict is not None
    assert parsed_dict == the_dict
    tmp_

# Generated at 2022-06-13 21:37:48.759980
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class TestBaseConfigDict(BaseConfigDict):
        pass

    import tempfile
    tmp_dir = tempfile.TemporaryDirectory()
    path = Path(tmp_dir.name + '/tmp.json')
    tmp_dir.cleanup()  # delete the directory that contains the file
    d = TestBaseConfigDict(path=path)
    d['foo'] = 'bar'
    d.save()
    with open(path, 'r') as f:
        assert f.read() == '{\n    "__meta__": {\n        "httpie": "' \
                           + __version__ + '"\n    }, \n    "foo": "bar"\n}\n'



# Generated at 2022-06-13 21:37:56.711400
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    test_path = Path.home() / 'test_save.txt'
    try:
        test_path.unlink()
    except:
        pass
    test_config = BaseConfigDict(test_path)
    test_config.save()
    assert test_path.exists()
    assert test_path.is_file()
    try:
        test_path.unlink()
    except:
        pass



# Generated at 2022-06-13 21:38:00.735565
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    home_dir = Path.home()

# Generated at 2022-06-13 21:38:09.847399
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class test_BaseConfigDict(BaseConfigDict):
        name = 'b'
        helpurl = '1'
        about = '2'
    e = test_BaseConfigDict(Path('./config/config.json'))
    e['a'] = 'A'
    e.save()
    # Assert the function save is correct
    with open('./config/config.json') as f:
        assert json.load(f) == {'__meta__': {'httpie': __version__, 'help': '1', 'about': '2'}, 'a': 'A'}

# Generated at 2022-06-13 21:38:19.641746
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    class Dummy(BaseConfigDict):
        def __init__(self, path: Path):
            super().__init__(path)
            self.path = path
            self.mkdir_called = 0
            self.mkdir_exc = None

        def mkdir(self, **kwargs):
            self.mkdir_called += 1
            if self.mkdir_exc:
                raise OSError(self.mkdir_exc)

    dummy = Dummy(Path('/some/path'))

    # 1. exists
    dummy['__meta__'] = {'httpie': __version__}
    assert dummy.ensure_directory() is None

    # 2. error creating
    dummy.mkdir_exc = errno.EIO
    with pytest.raises(ConfigFileError):
        dummy.ensure_

# Generated at 2022-06-13 21:38:27.309942
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    home_dir = Path.home()
    test_dir_1 = home_dir / Path('test_dir')
    test_dir_2 = home_dir / Path('.config') / Path('test_dir')
    test_obj_1 = BaseConfigDict(test_dir_1 / Path('test_file'))
    test_obj_2 = BaseConfigDict(test_dir_2 / Path('test_file'))
    try:
        test_obj_1.ensure_directory()
        test_obj_2.ensure_directory()
    finally:
        try:
            test_dir_1.rmdir()
        except OSError as e:
            if e.errno != errno.ENOENT:
                raise

# Generated at 2022-06-13 21:38:35.048577
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # test macos
    if sys.platform == 'darwin':
        assert get_default_config_dir() == Path.home() / 'Library' / 'Application Support' / 'httpie'
    # test unix
    elif sys.platform.startswith('linux'):
        old_env = os.environ.get(ENV_XDG_CONFIG_HOME)
        old_home = os.environ.get(ENV_HTTPIE_CONFIG_DIR)

        os.environ[ENV_XDG_CONFIG_HOME] = '/tmp'
        assert get_default_config_dir() == Path('/tmp') / DEFAULT_CONFIG_DIRNAME

        del os.environ[ENV_XDG_CONFIG_HOME]

# Generated at 2022-06-13 21:38:43.537967
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    cfg = BaseConfigDict(path=Path('my_path/config'))
    cfg.ensure_directory()
    assert Path('my_path/config').exists()
    with open(Path('my_path/config')) as f:
        cfg1 = json.load(f)
    assert cfg1 == {}


# Generated at 2022-06-13 21:38:44.644505
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert DEFAULT_CONFIG_DIR == Path.home() / DEFAULT_RELATIVE_XDG_CONFIG_HOME / 'httpie'

# Generated at 2022-06-13 21:38:53.531097
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    class TestBaseConfigDict(BaseConfigDict):
        pass

    test_file = Path('./test_base_config_dict')
    
    test_data = TestBaseConfigDict(path=test_file)
    test_data['name'] = 'tianyin'
    test_data.save()
    
    test_data.load()
    
    assert test_data['name'] == 'tianyin'

    test_data.delete()


# Generated at 2022-06-13 21:39:04.897579
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import shutil
    import tempfile

    dirpath = Path(tempfile.mkdtemp())
    cfg = Config(dirpath)
    assert not cfg.path.exists()

    cfg.save()

    # Check that the directory for the config file was created.
    assert dirpath.exists()
    assert dirpath.is_dir()

    # Check that the config file was created.
    assert cfg.path.exists()
    assert cfg.path.is_file()

    # Delete the directory recursively.
    shutil.rmtree(dirpath)

    # Check that the whole directory is gone.
    assert not dirpath.exists()



# Generated at 2022-06-13 21:39:15.317664
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    from tempfile import TemporaryDirectory
    with TemporaryDirectory() as tempdir:
        test_dict = BaseConfigDict(Path(tempdir))
        test_dict.update({'a': 2})
        test_dict.save()
        test_dict.update({'b': 4})
        test_dict.save()
        with open(os.path.join(tempdir, 'config.json'), 'r') as f:
            config_dump = json.load(f)
            expected_config_dump = {'a': 2, 'b': 4, '__meta__': {'httpie': __version__}}
            assert config_dump == expected_config_dump
            test_dict.delete()
        assert os.listdir(tempdir) == []



# Generated at 2022-06-13 21:39:24.095391
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    bcd = BaseConfigDict('config.json')
    bcd['user'] = 'root'
    bcd['password'] = '123'
    bcd['url'] = 'http://127.0.0.1'
    with open('config.json','w') as f_w:
        json.dump(bcd, f_w)
    # Test if the write is successful
    with open('config.json','r') as f_r:
        json.load(f_r)



# Generated at 2022-06-13 21:39:28.752651
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR
    assert get_default_config_dir() == get_default_config_dir()
    assert get_default_config_dir() == Config().directory



# Generated at 2022-06-13 21:39:40.322137
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # Create a temporary directory for testing
    tmp_dir = Path(tempfile.mkdtemp())
    # Create a directory that would have an one-level-deeper directory
    # along with a config.json file (which would be read and written by code
    # in this module)
    bad_dir = tmp_dir / 'bad/dir'
    bad_dir.mkdir(mode=0o700, parents=True)
    bad_dir_config = bad_dir / 'config.json'
    with bad_dir_config.open('w') as f:
        f.write('{}\n')
    # Create a non-exist directory
    empty_dir = Path(tempfile.mkdtemp(dir=tmp_dir))
    # Test method ensure_directory with a bad path

# Generated at 2022-06-13 21:39:42.448137
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    f = open('tmp', 'w')
    f.close()
    config_dict = BaseConfigDict(Path('tmp'))
    config_dict.save(fail_silently=True)
    os.remove('tmp')
