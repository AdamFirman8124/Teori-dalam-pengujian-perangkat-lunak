

# Generated at 2022-06-13 21:30:03.678550
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    def _get_expected_dir(env_xdg_config_home, env_httpie_config_dir,
                          is_windows, home_dir):
        if env_httpie_config_dir:
            return Path(env_httpie_config_dir)
        elif is_windows:
            return DEFAULT_WINDOWS_CONFIG_DIR
        elif (home_dir / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR).exists():
            return home_dir / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
        else:
            return (
                Path(env_xdg_config_home)
                if env_xdg_config_home
                else (home_dir / DEFAULT_RELATIVE_XDG_CONFIG_HOME)
            ) / DEFAULT_CONFIG_DIRNAME

# Generated at 2022-06-13 21:30:07.226403
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    b = BaseConfigDict(path=DEFAULT_CONFIG_DIR / 'test')
    b.ensure_directory()
    assert os.path.exists(DEFAULT_CONFIG_DIR / 'test')
    os.rmdir(DEFAULT_CONFIG_DIR / 'test')

# Generated at 2022-06-13 21:30:19.455577
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    import shutil
    import tempfile
    temp_path = tempfile.mkdtemp()
    try:
        config_dict = BaseConfigDict(Path(temp_path) / 'test_config.json')
        config_dict.ensure_directory()
        assert os.path.isdir(temp_path)
    finally:
        shutil.rmtree(temp_path)



# Generated at 2022-06-13 21:30:24.221543
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config_dir = Path('/tmp/test-config')
    
    if config_dir.exists():
        config_dir.rmdir()
    config = BaseConfigDict(path=config_dir)
    
    config.ensure_directory()
    assert config_dir.exists()
    config_dir.rmdir()


# Generated at 2022-06-13 21:30:28.391486
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    p = Path('/tmp/test_httpie_config_ensure_directory')
    p.mkdir(parents=True, mode=0o700)
    config = BaseConfigDict(p / 'config.json')
    config.ensure_directory()
    assert p.exists()

# Generated at 2022-06-13 21:30:40.768501
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    env = {}
    unset = object()
    with mock.patch.dict('os.environ', env, clear=True):
        assert get_default_config_dir() == Path.home() / '.config/httpie'
        env[ENV_HTTPIE_CONFIG_DIR] = '/foo/bar'
        assert get_default_config_dir() == Path('/foo/bar')

    env[ENV_XDG_CONFIG_HOME] = '/xdg/config/home'
    with mock.patch.dict('os.environ', env, clear=True):
        assert get_default_config_dir() == Path('/xdg/config/home/httpie')
        assert os.environ[ENV_HTTPIE_CONFIG_DIR] == '/foo/bar'  # untouched



# Generated at 2022-06-13 21:30:50.720935
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    # BaseConfigDict.save() is a function that saves the configuration to a file
    # When given a specific configuration, it should write the same configuration to the file
    # For this test we will use a test configuration given the path /tmp/config.json
    # The configuration is equivalent to
    # {
    #     "name": "nouserconfig",
    #     "default_options": []
    # }
    # We expect BaseConfigDict.save() to write the following to /tmp/config.json
    # {
    #     "__meta__": {
    #         "httpie": "1.0.3"
    #     },
    #     "name": "nouserconfig",
    #     "default_options": []
    # }

    # We will create a BaseConfigDict with the given configuration
    test

# Generated at 2022-06-13 21:31:02.774941
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # Test case 1: directory already exists
    home_directory = Path.home()
    config_directory_test_case1 = home_directory / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    if config_directory_test_case1.exists():
        config_directory_test_case1.rmdir()
    config_directory_test_case1.mkdir()

    base_config_dict_test_case1 = BaseConfigDict(path = config_directory_test_case1/ 'config.json')
    base_config_dict_test_case1.ensure_directory()

    assert config_directory_test_case1.exists()

    # Test case 2: directory does not exist
    config_directory_test_case2 = home_directory / 'config_directory'
    config_directory_test_case

# Generated at 2022-06-13 21:31:14.220744
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    try:
        config = Config('/tmp')
        config.ensure_directory()
        # assert config.directory.parent.exists()
        directory_exists = config.directory.parent.exists()
        assert directory_exists == True
    except:
        print ('test_BaseConfigDict_ensure_directory FAILED')
        raise
    print ('test_BaseConfigDict_ensure_directory PASSED')


# Generated at 2022-06-13 21:31:22.255166
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    from mock import patch
    from tempfile import NamedTemporaryFile

    cfg = BaseConfigDict(
        path=Path(NamedTemporaryFile().name)
    )

    with patch("httpie.config.Path.parent.mkdir") as mkdir:
        with patch("httpie.config.Path.parent.exists") as exists:
            exists.return_value = False
            cfg.ensure_directory()
            mkdir.assert_called_once_with(mode=0o700, parents=True)

            exists.return_value = True
            mkdir.reset_mock()
            cfg.ensure_directory()
            mkdir.assert_not_called()

    with patch("httpie.config.Path.parent.mkdir") as mkdir:
        mkdir.side_effect = OSError

# Generated at 2022-06-13 21:31:33.527540
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config_dict = Config()
    config_dict.save()
    with config_dict.path.open('rt') as f:
        assert f.read() == '{\n    "default_options": []\n}'
# Test for method delete of class BaseConfigDict

# Generated at 2022-06-13 21:31:36.508571
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    path = "tests/temporary_test_file.json"
    base = BaseConfigDict(path)
    base.save()
    if base.is_new():
        assert os.path.exists(path)
    else:
        assert True



# Generated at 2022-06-13 21:31:48.256852
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    home_dir = Path.home()

    # 1. explicitly set through env
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/'
    assert get_default_config_dir() == Path('/')

    # 2. Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # 3. legacy ~/.httpie
    legacy_config_dir = home_dir / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    with open(legacy_config_dir, 'a'):
        os.utime(legacy_config_dir)
    assert get_default_config_dir() == legacy_config_dir
    os.unlink(legacy_config_dir)

    # 4. XDG
    xdg_config

# Generated at 2022-06-13 21:31:57.471205
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    import yaml
    from pathlib import Path
    from httpie.config import BaseConfigDict

    class TestConfigDict(BaseConfigDict):
        pass

    tc = TestConfigDict(Path('/tmp/test_BaseConfigDict_ensure_directory/a/b/c/config.json'))
    tc.ensure_directory()
    if (tc.path.parent.exists()):
        print(yaml.dump(tc))
    else:
        print("No directory created")

# Generated at 2022-06-13 21:32:04.699562
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import tempfile
    class Test_BaseConfigDict(BaseConfigDict):
        name = 'test_name'
        helpurl = 'test_helpurl'
        about = 'test_about'
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmpdir = Path(tmpdirname)
        config = Test_BaseConfigDict(tmpdir/'test_file.json')
        config.save()
        with open(tmpdir/'test_file.json', 'rt') as f:
            data = json.load(f)
        assert data['__meta__']['httpie'] == __version__
        assert data['__meta__']['help'] == config.helpurl
        assert data['__meta__']['about'] == config.about
    # delete method error handling

# Generated at 2022-06-13 21:32:06.569636
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config = Config()
    config.load()
    assert config.get('default_options') == []



# Generated at 2022-06-13 21:32:19.611716
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    def _run_test(params):
        config_dict, mkdir_exception, expected_exception = params
        if mkdir_exception is not None:
            with patch('pathlib.Path.mkdir', mock_mkdir_raises(mkdir_exception)):
                if expected_exception is not None:
                    with pytest.raises(expected_exception):
                        config_dict.ensure_directory()
                else:
                    config_dict.ensure_directory()
        else:
            with patch('pathlib.Path.mkdir') as mkdir_mock:
                config_dict.ensure_directory()
                assert mkdir_mock.called

    def mock_mkdir_raises(e):
        def f(mode, parents):
            raise e

        return f


# Generated at 2022-06-13 21:32:23.587953
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    import os
    import tempfile
    filepath = os.path.join(tempfile.gettempdir(), 'test.json')
    if os.path.exists(filepath):
        os.remove(filepath)
    config = BaseConfigDict(filepath)
    assert not config.is_new()

    config.load()
    config.save()
    config.load()

    os.remove(filepath)



# Generated at 2022-06-13 21:32:27.686310
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    assert type(BaseConfigDict.ensure_directory) == types.MethodType

# Generated at 2022-06-13 21:32:30.230302
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:32:46.461055
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # Prepare
    test_path1 = DEFAULT_CONFIG_DIR / 'test/testfile'
    test_path2 = Path('/tmp/test/testfile')

    # Execute
    try:
        test_path1.parent.rmdir()
        test_path1.parent.parent.rmdir()
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise

    try:
        test_path2.parent.rmdir()
        test_path2.parent.parent.rmdir()
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise

    # Verify
    # Ensure that the test paths do not exist
    assert not test_path1.exists()
    assert not test_

# Generated at 2022-06-13 21:32:59.039669
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import platform
    import sys
    import unittest

    class TestGetDefaultConfigDir(unittest.TestCase):
        def setUp(self):
            self.environ = {}
            self.environ_patch = unittest.mock.patch(
                'os.environ', self.environ)
            self.environ_patch.start()

        def tearDown(self):
            self.environ_patch.stop()

        def test_get_default_config_dir(self):
            windows = platform.system() == 'Windows'
            python_version = sys.version_info.major

# Generated at 2022-06-13 21:33:03.145168
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/foo/bar'
    assert get_default_config_dir() == Path('/foo/bar')

# Generated at 2022-06-13 21:33:15.101535
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    test_dir = Path('test_dir')
    test_dir.mkdir()
    test_dir.joinpath('dir1').mkdir()
    test_dir.joinpath('dir1').joinpath('dir2').mkdir()
    test_dir.joinpath('dir3').mkdir()
    test_dir.joinpath('dir3').joinpath('dir4').mkdir()
    config_dir_path = test_dir.joinpath('dir1').joinpath('dir2').joinpath('config.json')

    base_config_dict = BaseConfigDict(config_dir_path)
    base_config_dict.ensure_directory()
    assert config_dir_path.parent.exists()
    test_dir.rmdir()



# Generated at 2022-06-13 21:33:21.963286
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    class TestConfigDict(BaseConfigDict):
        name = None
        helpurl = None
        about = None

        def __init__(self, path: Path):
            super().__init__(path)
            self.path = path
    test_config = TestConfigDict(Path("") / "test.json")
    my_dict = {1: 'hello', 2: 'world'}
    test_config.path.write_text(json.dumps(my_dict))
    test_config.load()
    assert(test_config == my_dict)
# Test passed


# Generated at 2022-06-13 21:33:32.450410
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import os
    import tempfile

    config_dir = os.path.join(tempfile.gettempdir(), 'httpie')
    old_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR, '')
    try:
        os.environ[ENV_HTTPIE_CONFIG_DIR] = config_dir
        assert get_default_config_dir() == Path(config_dir)
    finally:
        os.environ[ENV_HTTPIE_CONFIG_DIR] = old_httpie_config_dir

# Generated at 2022-06-13 21:33:41.478371
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    from tempfile import TemporaryDirectory
    import pytest

    with TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / 'config.json'
        assert not path.exists()

        x = BaseConfigDict(path)
        assert x.ensure_directory() is None
        assert path.parent.exists()

        path.parent.chmod(0o600)
        with pytest.raises(ConfigFileError) as e:
            x.ensure_directory()
        assert str(e.value).startswith('cannot create config dir')



# Generated at 2022-06-13 21:33:55.654024
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    assert get_default_config_dir() == Path(DEFAULT_RELATIVE_XDG_CONFIG_HOME) / DEFAULT_CONFIG_DIRNAME

    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/path/to/explicit'
    assert get_default_config_dir() == Path('/path/to/explicit')

    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    os.environ[ENV_XDG_CONFIG_HOME] = '/path/to/xdg/home'
    assert get_default_config_dir() == Path('/path/to/xdg/home') / DEFAULT_CONFIG_DIRNAME

# Generated at 2022-06-13 21:34:10.206751
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    env = os.environ.copy()
    del env[ENV_HTTPIE_CONFIG_DIR]

    # Case 1: Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Case 2: Legacy config dir set
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir()
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()

    # Case 3: Explicit
    env[ENV_HTTPIE_CONFIG_DIR] = '/foo'
    assert get_default_config_dir() == Path('/foo')

    # Case 4: Default

# Generated at 2022-06-13 21:34:21.259149
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    file_name = 'test_BaseConfigDict_save.json'
    config_path = './' + file_name

    class test_class(BaseConfigDict):
        def __init__(self, path):
            super().__init__(path)
            self['foo'] = 'bar'
            self['baz'] = ['qux']

    test_obj = test_class(config_path)
    test_obj.save()

    assert Path(config_path).exists()

    with open(config_path) as file:
        data = json.load(file)
        assert data['foo'] == 'bar'
        assert data['baz'] == ['qux']
        assert data['__meta__']['httpie'] == __version__

    os.remove(config_path)



# Generated at 2022-06-13 21:34:35.378485
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # If there's an explicitly set HTTPIE_CONFIG_DIR use that.
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/tmp/my_httpie_config'
    assert get_default_config_dir() == Path(os.environ[ENV_HTTPIE_CONFIG_DIR])
    # Windows: ~/.config/httpie
    # Linux: $XDG_CONFIG_HOME/httpie (defaults to ~/.config/httpie)
    del os.environ[ENV_HTTPIE_CONFIG_DIR]
    if is_windows:
        assert get_default_config_dir() == Path(r'C:\Users\{username}\AppData\Roaming\httpie')
    else:
        assert get_default_config_dir() == Path.home() / '.config' / 'httpie'

# Generated at 2022-06-13 21:34:43.569271
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    dir = tempfile.mkdtemp()
    config_file_path = Path(dir+'config.json')
    cd = BaseConfigDict(config_file_path)
    cd.ensure_directory()

    # tempfile.mkdtemp() creates a temporary directory.
    # Trying to create the directory again will raise OSError
    with pytest.raises(OSError):
        cd.ensure_directory()

    # remove the config.json and its parent directory
    os.remove(dir+'config.json')
    os.rmdir(dir)


# Generated at 2022-06-13 21:34:53.799362
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    class TestDict(BaseConfigDict):
        def __init__(self):
            super().__init__(Path('/tmp/test.txt'))

    d = TestDict()
    try:
        d.ensure_directory()
        assert not d.is_new()
        assert d.path.parent.is_dir()
        assert is_windows or os.stat(d.path.parent.__str__()).st_mode == 33152
    except FileExistsError:
        pass
    finally:
        d.path.parent.rmdir()

# Generated at 2022-06-13 21:35:01.109681
# Unit test for function get_default_config_dir
def test_get_default_config_dir():

    def mock_get_home_dir(s):
        return Path([s])

    def mock_get_xdg_config_home(s):
        return Path([s])

    home_dir = Path.home()
    xdg_config_home_dir = get_default_config_dir()

    # test when env var HTTPIE_CONFIG_DIR is explicitly set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/home/user/dev'
    assert get_default_config_dir() == Path('/home/user/dev')

    # test when os is windows
    sys.platform = 'win32'
    assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # test when legacy config dir exists

# Generated at 2022-06-13 21:35:10.557563
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    if is_windows:
        assert DEFAULT_WINDOWS_CONFIG_DIR == get_default_config_dir()
    else:
        if os.environ.get(ENV_HTTPIE_CONFIG_DIR):
            assert Path(os.environ[ENV_HTTPIE_CONFIG_DIR]) == get_default_config_dir()
        elif Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR:
            assert Path(os.environ[ENV_HTTPIE_CONFIG_DIR]) == get_default_config_dir()
        else:
            assert DEFAULT_WINDOWS_CONFIG_DIR == get_default_config_dir()

# Generated at 2022-06-13 21:35:19.243933
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class test_BaseConfigDict_save(BaseConfigDict):
        def __init__(self, path: Path):
            super().__init__(path)
            self['test_key'] = 'test_value'
            self['test_key2'] = 'test_value2'

    path = Path('test_BaseConfigDict_save')
    test_BaseConfigDict_save(path).save()

    with path.open('rt') as f:
        assert json.load(f) == {"test_key": "test_value", "test_key2": "test_value2"}

    path.unlink()

# Generated at 2022-06-13 21:35:27.662051
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config = BaseConfigDict("./abc.json")
    config['abc'] = '123'
    config.save()

    config1 = BaseConfigDict("./abc.json")
    config1.load()
    config1['def'] = '456'

    config2 = BaseConfigDict('./abc.json')
    config2.load()
    assert config2['def'] == '456'



# Generated at 2022-06-13 21:35:29.823769
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == '/home/xhx/.config/httpie'


# Generated at 2022-06-13 21:35:37.632535
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    # os.chdir(DEFAULT_CONFIG_DIR)
    config_dir = Path.home() / ".httpie"
    config_dir.mkdir()
    config_file = config_dir / 'config.json'
    config_file.touch()
    config_file.write_text("{'__meta__': {'httpie': '1.0.0'}}")

    config = Config(config_dir)
    assert config.load() == {"__meta__": {"httpie": "1.0.0"}}

    # os.chdir("..")
    config_file.unlink()
    config_dir.rmdir()

# Generated at 2022-06-13 21:35:44.938339
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    '''
    test load() method of class BaseConfigDict
    '''
    fpath = Path('./test')
    if not os.path.exists(fpath):
        os.mkdir(fpath)
# test for normal case
    fpath = fpath + '/BaseConfigDict_load.json'
    if os.path.exists(fpath):
        os.remove(fpath)
    testObj = BaseConfigDict(fpath)
    file=open(fpath,'w')
    file.write('{"key": "value"}')
    file.close()
    testObj.load()
    assert testObj['key']=='value', 'test case1: test_BaseConfigDict_load()ok'
# test for abnormal case
    file=open(fpath,'w')

# Generated at 2022-06-13 21:36:01.928101
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Case1: Check returned value in Case of un-set $XDG_CONFIG_HOME,
    # un-set $HTTPIE_CONFIG_DIR and ~/.httpie not exists.
    #
    # In this case, the directory will be set by XDG Base Directory
    # Specification.

    # Prepare for test
    home_dir = Path.home()
    xdg_config_home_dir = home_dir / DEFAULT_RELATIVE_XDG_CONFIG_HOME
    xdg_default_config_dir = xdg_config_home_dir / DEFAULT_CONFIG_DIRNAME
    legacy_config_dir = home_dir / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR

    legacy_config_dir.unlink(missing_ok=True)

    # Test
    config_dir

# Generated at 2022-06-13 21:36:14.420074
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # check directory not there and it was created
    path = '/home/user/directory'
    new_config_file = BaseConfigDict(path)
    mock_path = path + '/mock_file.json'
    ret = new_config_file.ensure_directory()
    assert not os.path.exists(mock_path)
    assert not ret

    # check directory is there
    path = 'httpie'
    new_config_file = BaseConfigDict(path)
    mock_path = path + '/mock_file.json'
    ret = new_config_file.ensure_directory()
    assert not os.path.exists(mock_path)
    assert ret == 0

    # check directory not there and not created
    path = '/home/user/directory'
    new_config_file

# Generated at 2022-06-13 21:36:21.282055
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    temp_dir = tempfile.TemporaryDirectory()
    temp_dir_path = Path(temp_dir.name)
    temp_config_dict_file = temp_dir_path / 'config.json'
    temp_config_dict_file.write_text('')

    base_config_dict = BaseConfigDict(path=temp_config_dict_file)
    base_config_dict.save()
    with open(temp_config_dict_file) as f:
        json_string = f.read()
    # status of is_new was changed from True to False
    assert json_string == '{\n    "__meta__": {\n        "httpie": "' + __version__ + '"\n    }\n}\n'
    temp_dir.cleanup()


test_BaseConfigDict_save()

# Generated at 2022-06-13 21:36:27.610703
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # Test 1: test that the directory doesn't exist
    test_dir = Path('./test_dir')
    cd = BaseConfigDict(path=test_dir)
    cd.ensure_directory()
    assert(test_dir.parent.exists() and test_dir.parent.is_dir())


# Generated at 2022-06-13 21:36:36.115162
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    save_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    save_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)


# Generated at 2022-06-13 21:36:37.606875
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    _test_BaseConfigDict_load()


# Generated at 2022-06-13 21:36:45.247924
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    directory = Path('/tmp/test_BaseConfigDict_ensure_directory')
    if not directory.exists():
        directory.mkdir(mode=0o700, parents=True)
    path = directory / 'Path_does_not_exist'
    class MyConfig(BaseConfigDict):
        pass
    config = MyConfig(path)
    config.ensure_directory()
    assert directory.exists()
    assert not path.exists()
    directory.rmdir()

if __name__ == '__main__':
    test_BaseConfigDict_ensure_directory()

# Generated at 2022-06-13 21:36:52.319166
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    tmp_dir = mkdtemp()
    test_dir = Path(tmp_dir) / "test_dir"
    assert not test_dir.is_dir()

    test = BaseConfigDict(test_dir)
    test.ensure_directory()

    assert test_dir.is_dir()

    rmtree(tmp_dir)
# end Unit test for method ensure_directory of class BaseConfigDict


# Generated at 2022-06-13 21:37:02.308462
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    test_dir = Path('test_dir')
    try:
        test_dir.mkdir()
        test_file = test_dir / 'config.json'
        test_file.write_text('{}')
        test_config = Config(test_dir)
        with test_file.open('rt') as f:
            assert json.load(f) == test_config
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    finally:
        shutil.rmtree(test_dir)



# Generated at 2022-06-13 21:37:12.594855
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import tempfile
    import shutil
    import os
    import json
    import httpie

    # Create directory tmp
    tmp_path = tempfile.mkdtemp()

    # Create directory to save file
    dir_to_save = os.path.join(tmp_path, 'config.json')
    dir_to_save = Path(dir_to_save)
    dir_to_save.touch()

    # Create class under test
    config = BaseConfigDict(dir_to_save)

    # Generate and save config
    config.save()

    # Check if file exists
    assert os.path.exists(dir_to_save) == True

    # Load from file and assert existence of key in file
    loaded_config = json.load(open(dir_to_save))

# Generated at 2022-06-13 21:37:29.352596
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    xdg_config_home_dir = Path.home() / DEFAULT_RELATIVE_XDG_CONFIG_HOME
    assert get_default_config_dir() == xdg_config_home_dir / DEFAULT_CONFIG_DIRNAME
    os.environ[ENV_XDG_CONFIG_HOME] = str(Path.home())
    assert get_default_config_dir() == Path.home() / DEFAULT_CONFIG_DIRNAME


# Generated at 2022-06-13 21:37:31.635756
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert isinstance(get_default_config_dir(), Path)

# Generated at 2022-06-13 21:37:40.529697
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    class Dict(BaseConfigDict):
        pass
    d = Dict(Path('/tmp/dir/file.json'))
    if d.path.parent.exists():
        shutil.rmtree(d.path.parent)
    assert not d.path.parent.exists()
    assert not d.path.exists()
    try:
        d.load()
    except ConfigFileError:
        assert True
    else:
        assert False
    assert not d.path.parent.exists()
    assert not d.path.exists()
    d.ensure_directory()
    assert d.path.parent.exists()
    assert not d.path.exists()
    d.update({'a': 'b'})
    d.save()
    del d['a']

# Generated at 2022-06-13 21:37:50.753316
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    windows = is_windows
    pathlib = Path

    class Path(pathlib):
        def __new__(cls, *args, **kwargs):
            return pathlib(*args, **kwargs)

    Path.home = lambda: Path('/home/httpie')
    Path.exists = lambda self: True

    config_dir_xdg = get_default_config_dir()
    assert str(config_dir_xdg) == '/home/httpie/.config/httpie'

    Path.exists = lambda self: False

    config_dir_legacy = get_default_config_dir()
    assert str(config_dir_legacy) == '/home/httpie/.httpie'

    is_windows = True
    config_dir_windows = get_default_config_dir()

# Generated at 2022-06-13 21:38:02.443592
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR
    # Relative config dir
    os.environ[ENV_XDG_CONFIG_HOME] = './test-config'
    assert get_default_config_dir() == Path('./test-config') / DEFAULT_CONFIG_DIRNAME
    # Absolute config dir
    os.environ[ENV_XDG_CONFIG_HOME] = Path(os.path.expanduser('~')) / DEFAULT_RELATIVE_XDG_CONFIG_HOME
    assert get_default_config_dir() == (Path(os.path.expanduser('~')) / DEFAULT_RELATIVE_XDG_CONFIG_HOME) / DEFAULT_CONFIG_DIRNAME
    # Windows config dir

# Generated at 2022-06-13 21:38:14.777742
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    def get_random_string():
        import random  
        str = [chr(random.randint(65, 65 + 25)) for i in range(10)]
        return ''.join(str)

    temp_dir = Path('/tmp')
    config = BaseConfigDict(path=temp_dir/'test.json')
    config['key'] = get_random_string()
    try:
        config.save()
    except Exception as e:
        from pytest import fail
        fail(str(e))
    try:
        for _ in range(10):
            config['key'] = get_random_string()
            config.save()
            config['key'] = get_random_string()
            config.save(fail_silently=True)
    except Exception as e:
        from pytest import fail
        fail

# Generated at 2022-06-13 21:38:23.677225
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config = BaseConfigDict(path=Path(''))
    with mock.patch('pathlib.Path') as mock_Path:
        mock_Path.mkdir.return_value = None
        config.ensure_directory()
        mock_Path.mkdir.return_value = True


# Generated at 2022-06-13 21:38:33.971908
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # directory for test
    tempdir = Path(tempfile.mkdtemp(dir=os.getcwd()))
    # create a test config dict, the config file will be the file
    # path.join(tempdir, "config.json")
    config_dict = BaseConfigDict(path=tempdir / 'config.json')

    # test that file does not exist
    test_file = tempdir / 'config.json'
    assert not test_file.exists()

    # test ensure_directory, ensure that the directory exists
    config_dict.ensure_directory()
    assert tempdir.exists()

    # test that the file still does not exist
    assert not test_file.exists()

    # remove the temp directory and its contents
    # tempfile.TemporaryDirectory() does not work here, because we
    #

# Generated at 2022-06-13 21:38:46.710611
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Default dir is .config/httpie
    os.environ.clear()
    assert get_default_config_dir() == Path('~/.config/httpie').expanduser()

    # Default dir is ~/.config/httpie
    os.environ.clear()
    os.environ[ENV_XDG_CONFIG_HOME] = '/my/config/home'
    assert get_default_config_dir() == Path('/my/config/home/httpie')

    # Explicitly set
    os.environ.clear()
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/my/config/dir'
    assert get_default_config_dir() == Path('/my/config/dir')

    # Windows defaults to %APPDATA%\httpie
    os.environ.clear

# Generated at 2022-06-13 21:38:53.222972
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    home_dir = Path.home()
    config_dir = home_dir / DEFAULT_CONFIG_DIRNAME
    if not config_dir.is_dir():
        os.mkdir(config_dir, mode=0o700)
    config_file = config_dir / 'config.json'
    config_json = config_file.read_text()
    config_json_obj = json.loads(config_json)
    assert type(config_json_obj).__name__ == 'dict'



# Generated at 2022-06-13 21:39:21.421406
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    with mock.patch('httpie.config.Path.home',
                    return_value='/home/user'):
        assert get_default_config_dir() == Path('/home/user/.config/httpie')
    with mock.patch('httpie.config.Path.home',
                    return_value='/home/user'),\
            mock.patch.dict('os.environ', {}):
        assert get_default_config_dir() == Path('/home/user/.config/httpie')
    with mock.patch.dict('os.environ', {
        'HTTPIE_CONFIG_DIR': '/path/to/httpie'
    }):
        assert get_default_config_dir() == Path('/path/to/httpie')

# Generated at 2022-06-13 21:39:25.274878
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config = BaseConfigDict(DEFAULT_CONFIG_DIR)
    config_str = '{ "key": "value" }'
    with open(DEFAULT_CONFIG_DIR, 'w+') as f:
        f.write(config_str)
    config.load()
    assert config['key'] == 'value'



# Generated at 2022-06-13 21:39:38.385579
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    path = Path("/tmp/test_config.json")
    config_dict = BaseConfigDict(path)
    config_dict.delete()
    config_dict.load()
    assert(config_dict == {})

    path = Path("/tmp/test_config_new.json")
    config_dict = BaseConfigDict(path)
    assert(config_dict.is_new())

    config_dict.load()
    assert(config_dict == {})
    assert(not config_dict.is_new())

    with path.open("w") as f:
        f.write('{"a":1}')
    config_dict = BaseConfigDict(path)
    config_dict.load()
    assert(config_dict == {"a": 1})

    with path.open("w") as f:
        f

# Generated at 2022-06-13 21:39:47.139052
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    def assert_dir_is(dirname, path):
        assert path, f'{dirname} is empty'
        assert path.exists(), f'{dirname} {path} does not exist'
        assert path.is_dir(), f'{dirname} {path} is not a directory'
    def assert_empty_dir_is(dirname, path):
        assert path == '', f'{dirname} is not empty'
        assert not path.exists(), f'{dirname} {path} exists'
    def assert_dir_is_not(dirname, path):
        assert path == '', f'{dirname} is not empty'
        assert not path.exists(), f'{dirname} {path} exists'

    def get_dir():
        config_dir = get_default_config_dir()
