

# Generated at 2022-06-13 21:29:51.852328
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    import doctest
    doctest.testmod()


# Generated at 2022-06-13 21:30:03.970954
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import unittest
    import tempfile

    class TestGetDefaultConfigDir(unittest.TestCase):
        def setUp(self):
            self.old_env = os.environ.copy()
            self.old_platform = platform.system()
            self.old_cwd = os.getcwd()

        def tearDown(self):
            os.environ = self.old_env
            os.chdir(self.old_cwd)

        def test_get_default_config_dir_windows(self):
            platform.system = lambda: 'Windows'
            os.environ = {}

            with tempfile.TemporaryDirectory() as tmpdir:
                os.chdir(tmpdir)
                actual = get_default_config_dir()

# Generated at 2022-06-13 21:30:12.299461
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    # TODO: load should raise ConfigFileError if json.load raises ValueError
    from tempfile import NamedTemporaryFile
    from shutil import make_archive, rmtree

    # create an archive with a file with invalid JSON data
    # compress into a zip archive with type 0x1f8b
    with NamedTemporaryFile('wb', suffix='.zip') as tmp:
        tmp.write(b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\xff')
        tmp.flush()
        dirpath = tmp.name[:-4]

# Generated at 2022-06-13 21:30:17.963917
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    path = Path('./config.json')
    config = BaseConfigDict(path)
    from pathlib import Path
    config.path = Path("./config.json")
    config.load()


# Generated at 2022-06-13 21:30:20.157631
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # given
    _dir = os.path.join(os.getcwd(), 'BaseConfigDict_test')

    if not os.path.isdir(_dir):
        os.mkdir(_dir)

    config = BaseConfigDict(path=os.path.join(_dir, 'test.json'))

    # when
    config.ensure_directory()

    # then
    assert os.path.isdir(_dir)

# Generated at 2022-06-13 21:30:20.620110
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    assert True



# Generated at 2022-06-13 21:30:27.546164
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    class C(BaseConfigDict):
        def __init__(self, path: Path):
            super().__init__(path)
    path = Path('/tmp/abc') 
    c = C(path)
    try:
        c.ensure_directory()
        assert not path.exists()
        assert path.parent.exists()
        assert path.parent.is_dir()
    finally:
        path.parent.rmdir()



# Generated at 2022-06-13 21:30:35.731024
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    class SubDict(BaseConfigDict):
        name = "sub"
        helpurl = "http://example.com"
        about = "sub description"

    # test_load_success
    config = SubDict(Path("test.json"))
    with Path("test.json").open('w') as f:
        json.dump({
            "a": "b"
        }, f)
    config.load()
    assert config["a"] == "b"
    assert config["__meta__"]["httpie"] == __version__
    assert config["__meta__"]["help"] == SubDict.helpurl
    assert config["__meta__"]["about"] == SubDict.about
    os.remove("test.json")

    # test_load_failed

# Generated at 2022-06-13 21:30:38.541909
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    c = BaseConfigDict('path_to_config')
    try:
        c.load()
    except ConfigFileError as e:
        print(e)



# Generated at 2022-06-13 21:30:48.074730
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config_file = Config(directory='/tmp')
    config_file.ensure_directory()

    with open('/tmp/config.json', 'w') as fp:
        fp.write('{"a": 1}')
    config_file.load()
    assert config_file == {"a": 1}

    with open('/tmp/config.json', 'w') as fp:
        fp.write('{invalid')

# Generated at 2022-06-13 21:30:53.784406
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config_dict = BaseConfigDict(path='httpie/config.json')
    config_dict.save()
    assert config_dict.path.exists()


# Generated at 2022-06-13 21:30:57.865370
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config_dir = tempfile.TemporaryDirectory()
    path = Path(f"{config_dir.name}/config.json")
    config = BaseConfigDict(path)
    assert not config.is_new()


# Generated at 2022-06-13 21:31:05.744914
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    from tempfile import TemporaryDirectory
    from pathlib import Path
    from _pytest.monkeypatch import MonkeyPatch
    from httpie.config import BaseConfigDict

    with MonkeyPatch().context() as m:
        with TemporaryDirectory() as d:
            m.setattr(BaseConfigDict, 'ensure_directory', lambda x: None)
            m.setattr(BaseConfigDict, 'delete', lambda x: None)
            m.setattr(Path, 'write_text', lambda x, y: None)
            bcd = BaseConfigDict(Path(d).joinpath('test.json'))
            bcd.save()



# Generated at 2022-06-13 21:31:13.176270
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    tempdir = Path('/tmp/httpietest')
    tempdir.mkdir(parents=True, exist_ok=True)
    test_file = tempdir / 'config.json'
    data = {'a': 1}
    cfg = BaseConfigDict(test_file)
    cfg.update(data)
    cfg.save()
    assert cfg.is_new() is False
    test_file.unlink()
    tempdir.rmdir()

# Generated at 2022-06-13 21:31:19.528272
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    class MyConfigDict(BaseConfigDict):
        DEFAULTS = {
            'my_value': 1
        }

    config_path = Path('~/config').expanduser() / 'myconfig.json'
    my_config = MyConfigDict(config_path)
    my_config.load()
    assert 'my_value' in my_config
    assert my_config['my_value'] == 1

test_BaseConfigDict_load()


# Generated at 2022-06-13 21:31:22.051660
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config_dict = BaseConfigDict(DEFAULT_CONFIG_DIR)
    try:
        config_dict.save()
    except IOError:
        assert False

# Generated at 2022-06-13 21:31:33.847756
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/tmp/httpie'
    del os.environ[ENV_XDG_CONFIG_HOME]
    assert get_default_config_dir() == Path('/tmp/httpie')

    del os.environ[ENV_HTTPIE_CONFIG_DIR]
    os.environ[ENV_XDG_CONFIG_HOME] = '/tmp'
    assert get_default_config_dir() == Path('/tmp/httpie')

    if is_windows:
        del os.environ[ENV_XDG_CONFIG_HOME]
        assert get_default_config_dir() == Path(
            os.path.expandvars('%APPDATA%')) / DEFAULT_CONFIG_DIRNAME


# Generated at 2022-06-13 21:31:39.455554
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config_dict = BaseConfigDict(DEFAULT_CONFIG_DIR)
    config_dict.save()
    path = DEFAULT_CONFIG_DIR
    file_path = path.joinpath('.httpie')
    file = file_path.joinpath('config.json')
    assert file.exists()
    assert file.is_file()
    # clean up
    file.unlink()



# Generated at 2022-06-13 21:31:46.329779
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    from httpie.context import Environment
    from tests.test_config import test_config
    from tests import test_utils

    # Value as specified in file
    desired_config_homedir = test_utils.get_config_homedir()

    env = Environment()
    env.config = test_config

    # Manually call function to bypass context's env.config requirement
    actual_config_homedir = get_default_config_dir()

    # Check if values are the same
    assert actual_config_homedir == desired_config_homedir



# Generated at 2022-06-13 21:31:53.413166
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    import os

    os.environ[ENV_HTTPIE_CONFIG_DIR] = 'test_config_dir'
    assert get_default_config_dir() == 'test_config_dir'
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    config = Config()

    assert config['default_options'] == []

    config['default_options'].append('--help')
    config.save()

    config = Config()

    assert config['default_options'] == ['--help']

# Generated at 2022-06-13 21:32:02.593609
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    from tempfile import TemporaryDirectory
    from contextlib import ExitStack
    with ExitStack() as stack:
        output = stack.enter_context(TemporaryDirectory())
        cfg = BaseConfigDict(Path(output, 'config.json'))
        cfg['aa'] = 'dd'
        cfg.save()
        with open(Path(output, 'config.json'), 'r') as f:
            content = f.read()
        assert 'aa' in content, 'save method failed'
        assert 'dd' in content, 'save method failed'


# Generated at 2022-06-13 21:32:09.879824
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import tempfile
    test_dir = Path(tempfile.gettempdir())
    class TestDict(BaseConfigDict):
        name = None
        helpurl = None
        about = None

    test_dict = TestDict(path=test_dir/'test.json')
    test_dict.save()
    with open(test_dir/'test.json') as f:
        data = f.read()
    assert '"__meta__": {"httpie": "1.0.3"}' in data
    assert '"__meta__": {"about": null}' in data
    assert '"__meta__": {"help": null}' in data

# Generated at 2022-06-13 21:32:13.486892
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    class X(BaseConfigDict):
        path = Path('/tmp/x.json')
    x = X(Path('/tmp/x.json'))
    x.save()
    x.load()
    print(x)


# Generated at 2022-06-13 21:32:25.144593
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # No environment variable
    assert get_default_config_dir() == Path.home() / '.config' / 'httpie'

    # HTTPIE_CONFIG_DIR environment variable
    os.environ[ENV_HTTPIE_CONFIG_DIR] = 'httpied'
    assert get_default_config_dir() == Path('httpied')

    # Legacy ~/.httpie
    os.environ[ENV_HTTPIE_CONFIG_DIR] = ''
    os.environ[ENV_XDG_CONFIG_HOME] = ''
    assert get_default_config_dir() == Path.home() / '.httpie'

    # XDG_CONFIG_HOME environment variable
    os.environ[ENV_XDG_CONFIG_HOME] = 'xdg'

# Generated at 2022-06-13 21:32:34.704529
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config = Config()
    config.load()
    assert config.default_options == []
    assert config.name == 'config'
    assert config.helpurl is None
    assert config.about is None
# Prints the directory of config file
#     print(config.path)
#     print(config.directory)
# Prints the cache file path of current config
#     print(config.path.parent)

# Generated at 2022-06-13 21:32:47.148238
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config_dir = Path('tests/temp')
    config_path = config_dir / 'config.json'
    config = BaseConfigDict(path=config_path)

    # Case 1: fail silently when input file does not exist
    config.load()

    # Case 2: raise ConfigFileError when input file is invalid
    with open(config_path, 'wt') as f:
        f.write('invalid file')

    print(config_path.is_file())
    with pytest.raises(ConfigFileError):
        config.load()

    # Case 3: load valid input file
    with open(config_path, 'wt') as f:
        json.dump({'key': 'value'}, f)

    config.load()
    assert config['key'] == 'value'



# Generated at 2022-06-13 21:32:59.634381
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # TODO: drop default ".config" after releasing 0.10.0, use only XDG_CONFIG_HOME
    # 1. explicitly set through env
    assert get_default_config_dir() == \
        Path(os.environ[ENV_HTTPIE_CONFIG_DIR])

    # 2. Windows
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    assert get_default_config_dir().as_posix() == \
        DEFAULT_WINDOWS_CONFIG_DIR.as_posix()
    assert get_default_config_dir() == \
        Path(r'C:\Users\whoever\AppData\Roaming\httpie')
    assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # 3. legacy ~/.httpie

# Generated at 2022-06-13 21:33:03.899872
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import tempfile
    p = tempfile.TemporaryDirectory()
    l = BaseConfigDict(path = p.name)
    l.save()

    with open(l.path, 'r') as f:
        s = f.read()
    assert s == '{"__meta__": {"httpie": "2.1.0"}}\n'


# Generated at 2022-06-13 21:33:08.244382
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config = Config()
    config.directory.mkdir(parents=True)
    config.ensure_directory()
    config.directory.rmdir()


# Generated at 2022-06-13 21:33:13.642651
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    mock_path = Path("./mock_config_dir")
    mock_path.mkdir(parents=True)
    test_file_path = mock_path / 'test.json'
    config = BaseConfigDict(path=test_file_path)
    config.ensure_directory()
    assert test_file_path.parent.exists()


# Generated at 2022-06-13 21:33:23.842524
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    # Case 1 - Save the file with only default content
    config = BaseConfigDict(os.path.join('tests', 'unit', 'user_config', 'config.json'))
    config.save()
    with open(os.path.join('tests', 'unit', 'user_config', 'config.json'), 'r') as f:
        data = json.load(f)
    assert data['__meta__']['httpie'] == __version__

    # Case 2 - Save the file with only default content and fail silently
    config = BaseConfigDict(os.path.join('tests', 'unit', 'user_config', 'config.json'))
    config.save(fail_silently=True)

# Generated at 2022-06-13 21:33:29.844518
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() / '.config' / 'httpie'
    os.environ[ENV_XDG_CONFIG_HOME] = '/tmp'
    assert get_default_config_dir() == Path('/tmp') / 'httpie'

# Generated at 2022-06-13 21:33:33.206060
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import os
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/foo/bar'
    assert get_default_config_dir() == Path('/foo/bar')

# Generated at 2022-06-13 21:33:41.862205
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    class TestConfigDict(BaseConfigDict):
        def __init__(self, path: Path):
            super().__init__(path)
        def test_local_func(self):
            print("inside BaseConfigDict")

    class TestConfig(BaseConfigDict):
        FILENAME = 'config.json'
        DEFAULTS = {
            'default_options': []
        }
        def __init__(self, directory: Union[str, Path] = DEFAULT_CONFIG_DIR):
            self.directory = Path(directory)
            super().__init__(path=self.directory / self.FILENAME)
            self.update(self.DEFAULTS)
        def test_local_func(self):
            print("inside Config")

    # invalid json

# Generated at 2022-06-13 21:33:55.131201
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    from pathlib import Path

    # This is a configuration directory
    config_dir = Path("../../testdir/")

    # Create the configuration directory for testing
    config_dir.mkdir(parents=True, exist_ok=True)

    # Create a file under the configuration directory
    (config_dir / 'config_file').touch(exist_ok=True)

    # Test if the ensure_directory method works
    # The result is a directory named 'config_dir'
    BaseConfigDict(config_dir).ensure_directory()

    # Test if an exception is raised if 'config_dir' is a file
    # The result is an exception
    BaseConfigDict(config_dir / 'config_file').ensure_directory()


# Generated at 2022-06-13 21:33:58.914500
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config = Config()
    BaseConfigDict.load(config)
    assert config.is_new() is True
    assert BaseConfigDict.name is None
    assert BaseConfigDict.helpurl is None
    assert BaseConfigDict.about is None


# Generated at 2022-06-13 21:34:03.263561
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    path = Path.home() / Path("config.json")
    conf = BaseConfigDict(path)
    if conf.ensure_directory() == None:
        print("error")
    print("ok")

# Generated at 2022-06-13 21:34:14.753690
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import os
    from pathlib import Path
    from tempfile import gettempdir
    from unittest.mock import patch

    # Patch os.environ so that the tests can run without root privileges
    with patch.dict(os.environ, {'XDG_CONFIG_HOME': gettempdir()}):
        # Test all of the conditions
        with patch.object(os, 'name', 'nt'):
            assert get_default_config_dir() == Path(os.environ.get('APPDATA')) / 'httpie'

        with patch.dict(os.environ, {'HTTPIE_CONFIG_DIR': gettempdir()}):
            assert get_default_config_dir() == Path(os.environ.get('HTTPIE_CONFIG_DIR'))

            # Test the fallback of XDG

# Generated at 2022-06-13 21:34:17.200256
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() / '.config' / 'httpie'


# Generated at 2022-06-13 21:34:23.740961
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    # Assuming that there is a file named config.json under DEFAULT_CONFIG_DIR,
    # it should load the dictionary from config.json, otherwise
    # it should create an empty dictionary.
    config_file_path = DEFAULT_CONFIG_DIR / Config.FILENAME
    if config_file_path.exists():
        with config_file_path.open('rt') as f:
            data = json.load(f)
        assert data
    else:
        data = {}
    assert not data
    config = Config()
    assert data == config
    assert config.default_options == []



# Generated at 2022-06-13 21:34:32.347172
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    path = Path(__file__).parent / 'test_config_dir' / 'test_config_file.json'
    config = BaseConfigDict(path)
    return config.load()



# Generated at 2022-06-13 21:34:36.096575
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    d = BaseConfigDict(Path('config.json'))
    d.load()



# Generated at 2022-06-13 21:34:46.221209
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Test with HTTPIE_CONFIG_DIR
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '~/config'
    assert (get_default_config_dir()
            == Path(os.path.expanduser('~/config/httpie')))
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test with XDG_CONFIG_HOME
    os.environ[ENV_XDG_CONFIG_HOME] = '~/xdg_config'
    assert (get_default_config_dir()
            == Path(os.path.expanduser('~/xdg_config/httpie')))
    del os.environ[ENV_XDG_CONFIG_HOME]

    # Test for Windows
    assert is_windows

# Generated at 2022-06-13 21:34:57.599133
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    from io import StringIO
    from unittest.mock import patch

    class FakeConfig(BaseConfigDict):
        def __init__(self, path: Path) -> None:
            super().__init__(path)
            self.path = path

    fake_config_path = "test/test_config/test_config"
    fake_config = FakeConfig(fake_config_path)

    # Case where the parent directory name exists
    with patch('builtins.open', create=True) as mock_open:
        mock_open.return_value = StringIO()
        fake_config.ensure_directory()

    # Case where the parent directory name exists
    with patch('builtins.open', create=True) as mock_open:
        mock_open.side_effect = IOError(2, 'No such file or directory')

# Generated at 2022-06-13 21:35:06.694630
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    dir_path = tempfile.mkdtemp()
    print(dir_path)
    filename = 'httpie.json'
    filepath = os.path.join(dir_path, filename)
    config = BaseConfigDict(filepath)
    assert config.is_new() == True
    config.save()
    assert config.is_new() == False
    os.remove(filepath)
    os.rmdir(dir_path)


# Generated at 2022-06-13 21:35:19.137475
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    from unittest.mock import call

    def mock_makedirs(mode, parents=False):
        assert mode == 0o700
        assert parents, 'The ensure_directory method should work recursively'
        if not os.path.exists('/tmp'):
            raise OSError(errno.ENOENT, 'No such directory', '/tmp')

    class MockConfigDict(BaseConfigDict):
        pass

    with mock.patch.object(Path, 'mkdir', mock_makedirs):
        # test when directory already exists
        config_dict = MockConfigDict(path='/tmp/config.json')
        config_dict.ensure_directory()

        # test when directory doesn't exist
        with pytest.raises(OSError) as excinfo:
            config_dict.ensure_directory

# Generated at 2022-06-13 21:35:32.976470
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Case 1.1
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/foo/bar'
    assert get_default_config_dir() == Path('/foo/bar')

    # Case 1.2
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/tmp'
    assert get_default_config_dir() == Path('/tmp/httpie')

    # Case 1.3
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '~/foo'
    assert get_default_config_dir() == Path('~/foo/httpie')

    # Case 2.1
    assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Case 3.1

# Generated at 2022-06-13 21:35:39.050605
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config = BaseConfigDict(path=DEFAULT_CONFIG_DIR / 'config_for_test.json')
    config.update({'foo': 'bar'})
    config.save()
    assert config.get('foo') == 'bar'

    config_data = config.get('__meta__')
    assert config_data['httpie'] == __version__


# Generated at 2022-06-13 21:35:48.130781
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    test_file = Path('testfile.json')
    dict_ = BaseConfigDict(test_file)
    dict_['key'] = 'value'
    dict_.save(fail_silently=True)
    assert (test_file.read_text() ==
            '{\n    "key": "value",\n    "__meta__": {\n        '
            '"httpie": "1.0.3"\n    }\n}')
    test_file.unlink()


# Generated at 2022-06-13 21:36:00.997680
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    def xdg_config_home_override(expected: Path):
        def get_config_dir() -> Path:
            with patch.dict(
                'os.environ',
                {ENV_XDG_CONFIG_HOME: expected.as_posix()},
                clear=True
            ):
                return get_default_config_dir()
        return get_config_dir

    def httpie_config_dir_override(expected: Path):
        def get_config_dir() -> Path:
            return get_default_config_dir(expected)
        return get_config_dir

    def windows_override(expected: Path):
        def get_config_dir() -> Path:
            with patch('platform.system') as mock_platform_system:
                mock_platform_system.return_value = 'Windows'

# Generated at 2022-06-13 21:36:27.676473
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    class TestConfigDict(BaseConfigDict):
        pass
    try:
        TestConfigDict(Path("123.json")).load()
    except ConfigFileError:
        assert True
    temp = {"this.is":{"a":"test"}}
    TestConfigDict(Path("123.json")).save(temp)
    try:
        TestConfigDict(Path("123.json")).load()
    except ConfigFileError:
        assert False
    try:
        TestConfigDict(Path("123.json")).delete()
    except OSError:
        assert False

if __name__ == '__main__':
    test_BaseConfigDict_load()

# Generated at 2022-06-13 21:36:33.633727
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    # Arrange
    input = "{\"a\":\"abc\"}"
    expected = {
        "a": "abc",
        "__meta__": {
            "httpie": __version__
        }
    }

    # Act
    path = Path("test.json")
    path.write_bytes(input.encode())

    cfd = BaseConfigDict(path)
    cfd.load()

    # Assert
    assert cfd == expected



# Generated at 2022-06-13 21:36:38.932601
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    path = Path(os.path.join('test_files', 'test_write.json'))
    BaseConfigDict.save(self, path)

    f = open(path, 'r')
    list = f.readlines()
    f.close()
    assert list[0] == '{\n'
    assert list[1] == '    "__meta__": {\n'
    assert list[2] == '        "httpie": "httpie' + __version__[0] + '.' + __version__[1] + '"\n'
    assert list[3] == '    }\n'
    assert list[4] == '}\n'

    os.remove(path)

# Generated at 2022-06-13 21:36:43.791954
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
    else:
        assert get_default_config_dir() == Path.home() / \
            DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME


# Generated at 2022-06-13 21:36:54.838302
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    """
    httpie/config.py::test_get_default_config_dir
    """
    # These test assume a clean environment,
    # so we must unset the HTTPIE_CONFIG_DIR environment variable
    os.environ.pop('HTTPIE_CONFIG_DIR', None)

    home = Path.home()
    legacy = home / '.httpie'
    legacy_env = Path('/tmp/httpie-legacy-env')
    legacy.mkdir(mode=0o700, parents=True)
    legacy_env.mkdir(mode=0o700, parents=True)
    os.environ['HTTPIE_CONFIG_DIR'] = str(legacy_env)

    xdg_base = home / '.config'
    xdg_app = xdg_base / 'httpie'
   

# Generated at 2022-06-13 21:37:07.166349
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    global DEFAULT_CONFIG_DIR
    global DEFAULT_WINDOWS_CONFIG_DIR

    # the current default config dir is $HOME/.config/httpie
    assert DEFAULT_CONFIG_DIR == Path.home() / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME

    # override the default config dir
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/tmp/httpie-config'
    DEFAULT_CONFIG_DIR = get_default_config_dir()
    assert DEFAULT_CONFIG_DIR == Path('/tmp/httpie-config')

    # the config dir is $HOME/.config/httpie if previous override was deleted
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR)

# Generated at 2022-06-13 21:37:11.418959
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    import os
    config = BaseConfigDict(os.path.join(os.path.dirname(__file__),
                                         'resources/config.json'))
    assert isinstance(config, BaseConfigDict)

# Generated at 2022-06-13 21:37:15.800646
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import httpie.config
    httpie.config.DEFAULT_CONFIG_DIR = './tests/testdatas/'
    config = httpie.config.Config()
    config.save()
    assert config.is_new() == False

# Generated at 2022-06-13 21:37:20.301810
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    bcd = BaseConfigDict(path=Path('./aa/a.txt'))
    bcd.ensure_directory()
    assert os.path.exists('./aa')
    os.rmdir('./aa')

# Generated at 2022-06-13 21:37:22.452714
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:37:44.954389
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config_dir = Path('/tmp/httpie')
    assert not config_dir.exists()

    config_file = config_dir / 'config.json'
    assert not config_file.exists()

    # Make sure config directory exists.
    config = Config(config_dir)
    config.ensure_directory()
    assert config_dir.exists()

    # Make sure config file exists.
    config.save()
    assert config_file.exists()

    # Cleanup config file.
    config.delete()
    assert not config_file.exists()

    # Cleanup config directory.
    config_dir.rmdir()
    assert not config_dir.exists()


# Generated at 2022-06-13 21:37:53.073140
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    # This method is for testing BaseConfigDict.load
    test_config_filename = 'test_config.json'
    test_config_file_content = '{"name":"test"}'
    test_directory = Path.home() / 'test_config_dir'
    test_config_file = test_directory / test_config_filename

    if test_config_file.exists():
        test_config_file.unlink()

# Generated at 2022-06-13 21:37:56.116063
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config_dir = Path('/tmp')
    config = BaseConfigDict(path=config_dir / 'test')


# Generated at 2022-06-13 21:38:02.538200
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    d = {'a': 1, 'b': 2}
    c = BaseConfigDict(Path('./test.json'))
    c.update(d)
    c.save()
    c = BaseConfigDict(Path('./test.json'))
    e = {'a': 1, 'b': 2, '__meta__': {'httpie': __version__}}
    assert c == e
    os.remove('./test.json')



# Generated at 2022-06-13 21:38:12.553570
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config_dir = '/tmp/test_httpie/'
    config_dir_path = Path(config_dir)
    config_dir_path.mkdir(mode=0o700, parents=True)
    if config_dir_path.exists():
        config_dir_path.rmdir()
    config_file_path = config_dir_path / 'config.json'
    config = Config(directory=config_dir_path)
    config.ensure_directory()
    assert(config_file_path.parent.exists() == True)
    config_file_path.parent.rmdir()

# Generated at 2022-06-13 21:38:18.103827
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    try:
        from httpie.config import BaseConfigDict
        path = Path('./test/testdir')
        test_dir = BaseConfigDict(path)
        test_dir.ensure_directory()
        test_dir.path.parent.rmdir()
        print('Success.')
    except Exception as err:
        print('Error: '+ str(err))


# Generated at 2022-06-13 21:38:26.391006
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    from tempfile import TemporaryDirectory
    from unittest import TestCase

    class TestBaseConfigDict(BaseConfigDict):
        name = 'test.json'
        helpurl = 'helpurl'
        about = 'about'

    with TemporaryDirectory() as d:
        d = Path(d)
        config = TestBaseConfigDict(path=d / TestBaseConfigDict.name)
        config['key1'] = 'value1'
        config['key2'] = 'value2'
        config.save()
        with (d / TestBaseConfigDict.name).open('r') as f:
            jdata = json.load(f)
            assert jdata['key1'] == 'value1'
            assert jdata['key2'] == 'value2'

# Generated at 2022-06-13 21:38:29.893873
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    path = Path('~/.httpie/config.json')
    config = BaseConfigDict(path)
    try:
        config.load()
    except:
        raise Exception


# Generated at 2022-06-13 21:38:45.166264
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # Try to create a non existing directory
    directory = Path('/tmp/this/folder/does/not/exist')
    config = BaseConfigDict(path=directory / 'config.json')
    config.ensure_directory()
    assert(os.path.exists(str(config.path.parent)))
    # Cleanup
    os.removedirs(str(config.path.parent))
    assert(not os.path.exists(str(config.path.parent)))

    # Try to create an existing directory (should fail as is_directory)
    directory = Path(tempfile.gettempdir())
    config = BaseConfigDict(path=directory / 'config.json')
    with pytest.raises(OSError):
        config.ensure_directory()

    # Try to create an existing file (should fail as is not

# Generated at 2022-06-13 21:38:55.039550
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    from contextlib import redirect_stdout
    from io import StringIO
    from pathlib import Path
    from unittest.mock import patch

    class MockConfigDict(BaseConfigDict):
        pass

    with patch('httpie.config.get_default_config_dir', return_value=Path('/foo/bar')):
        # create a new config
        config = MockConfigDict(Path('/foo/bar/config.json'))
        assert config.is_new() is True
        assert config.path.exists() is False

        # try to save it, which will trigger directory creation
        # and redirect print output to a in-memory text stream
        with redirect_stdout(StringIO()) as out, patch('os.mkdir') as mock_mkdir:
            config.save()

        # os.mkdir should