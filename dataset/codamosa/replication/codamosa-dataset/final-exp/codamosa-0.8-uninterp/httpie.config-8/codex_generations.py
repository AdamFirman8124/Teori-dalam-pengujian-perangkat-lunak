

# Generated at 2022-06-13 21:29:58.263255
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    bcd_path = Path('~/.httpie/config.json')
    bcd = BaseConfigDict(bcd_path)
    assert bcd.is_new()
    bcd.load()
    with bcd.path.open('w') as f:
        f.write('This is not json')
    bcd.load()

# Generated at 2022-06-13 21:30:05.286110
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    data = {}
    with open('config.json', 'w') as file:
        json.dump(data, file)
    c = Config()
    assert c['default_options'] == []
    with open('config.json', 'w') as file:
        json.dump({"default_options": ["-b", "-u", "user", "-p", "pwd"]}, file)
    c = Config()
    assert c['default_options'] == ["-b", "-u", "user", "-p", "pwd"]


# Generated at 2022-06-13 21:30:09.453287
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    directory = Path('.httpie')
    if not directory.exists():
        directory.mkdir(mode=0o700)
    filename = directory / 'config.json'
    filename.touch(mode=0o600)
    config = ConfigFile(directory='.httpie')
    config.save(fail_silently=False)
    assert filename.open(mode='rt').read() == '{}\n'

# Generated at 2022-06-13 21:30:14.064383
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import os, sys, tempfile
    config_dir = tempfile.mkdtemp()
    os.environ[ENV_HTTPIE_CONFIG_DIR] = config_dir
    test_config = Config()
    test_config['test'] = 'test'
    test_config.save()
    assert test_config.path.exists()
    test_config.delete()
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR)
    os.rmdir(config_dir)

# Generated at 2022-06-13 21:30:17.998049
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    from tempfile import TemporaryDirectory
    import shutil
    from httpie.config import get_default_config_dir
    from httpie.compat import is_windows, is_py37

    # Only run this if we're running on a Unix-like system
    if is_windows or is_py37:
        return

    # create an empty config file in a temporary directory
    dirname = os.path.realpath(os.path.dirname(__file__))
    working_dir = os.path.join(dirname, '..')
    with TemporaryDirectory() as temp_dir:
        # Create a fake home directory in our temporary directory
        fake_home_dir = os.path.join(temp_dir, 'home')
        fake_config_dir = os.path.join(fake_home_dir, '.config', 'httpie')

# Generated at 2022-06-13 21:30:21.714061
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    # test_BaseConfigDict_load_normal
    # Test load normal when config file exist and valid
    with open(DEFAULT_CONFIG_DIR / Config.FILENAME, 'w') as cf:
        cf.write('{"default_options": []}')
    config = Config(DEFAULT_CONFIG_DIR)
    config.load()
    assert config == {'__meta__': {'httpie': __version__}, 'default_options': []}

    # test_BaseConfigDict_load_raise_ConfigFileError
    # Test load raise ConfigFileError when config file valid
    with open(DEFAULT_CONFIG_DIR / Config.FILENAME, 'w') as cf:
        cf.write('{"default_options": [}')


# Generated at 2022-06-13 21:30:26.776448
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME

    os.environ[ENV_HTTPIE_CONFIG_DIR] = "/foo/bar"
    assert get_default_config_dir() == Path("/foo/bar")
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    os.environ[ENV_XDG_CONFIG_HOME] = "/foo/bar"
    assert get_default_config_dir() == Path("/foo/bar") / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]

# Generated at 2022-06-13 21:30:38.645020
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import platform
    import shutil
    from pathlib import Path

    from httpie.config import (
        DEFAULT_CONFIG_DIR,
        DEFAULT_RELATIVE_LEGACY_CONFIG_DIR,
        DEFAULT_WINDOWS_CONFIG_DIR,
        get_default_config_dir,
    )

    def _platform_is_unsupported(platform_, httpie_version):
        return (
            (platform_ == 'darwin' and httpie_version < '0.9.9') or
            (platform_ == 'win32' and httpie_version < '0.9.5')
        )

    httpie_version = __version__


# Generated at 2022-06-13 21:30:43.002677
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    from pathlib import Path
    from httpie.config.json_config import BaseConfigDict
    c = BaseConfigDict('httpie/config/httpie_test.json')
    c.load()
    assert c == {'key': 'value'}



# Generated at 2022-06-13 21:30:46.317020
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    dirname = 'mock'
    filename = 'mock.json'
    content = {}
    config = BaseConfigDict(dirname / filename)
    
    assert config.load() == content


# Generated at 2022-06-13 21:31:02.206840
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():

    class TempConfig(BaseConfigDict):
        FILENAME = 'config.json'

    directory = Path('/tmp/httpie_config')
    TempConfig(directory).save()
    assert os.path.exists(directory / 'config.json')
    assert os.path.exists(directory)

    try:
        TempConfig(Path('/root/httpie_config')).save()
        assert False
    except ConfigFileError:
        pass

    try:
        TempConfig(Path('/root/')).save()
        assert False
    except ConfigFileError:
        pass

    try:
        TempConfig(Path('/root')).save()
        assert False
    except ConfigFileError:
        pass


# Generated at 2022-06-13 21:31:11.756615
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    path = 'test/config.json'
    d = BaseConfigDict(path)
    d.save()
    with open(path, 'r') as f:
        assert f.read() == """{
    "__meta__": {
        "httpie": "2.2.0"
    }
}
"""
    d['test'] = 'test'
    d.save()
    with open(path, 'r') as f:
        assert f.read() == """{
    "__meta__": {
        "httpie": "2.2.0"
    },
    "test": "test"
}
"""
    os.remove(path)


# Generated at 2022-06-13 21:31:19.940077
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():

    # Test whether the method can handle properly well-formed JSON.
    # Test not expecting an exception.
    class TestConfig1(BaseConfigDict):
        pass
    test_config = TestConfig1('tests/config/empty.json')
    assert test_config.load() is None

    # Test whether the method can detect malformed JSON.
    # Test expecting the ConfigFileError exception with 'invalid config file'
    # in the message.
    class TestConfig2(BaseConfigDict):
        pass
    test_config = TestConfig2('tests/config/malformed.json')
    with pytest.raises(ConfigFileError) as e:
        test_config.load()
        assert 'invalid config file' in str(e)


# Generated at 2022-06-13 21:31:26.669096
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import tempfile
    config_test = BaseConfigDict(path = Path(tempfile.mkstemp()[1]))
    config_test.save(fail_silently=True)
    assert config_test.is_new() is False
    assert config_test.path.exists() is True
    config_test.delete()
    assert config_test.path.exists() is False


# Generated at 2022-06-13 21:31:43.246780
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    # Create a temporary 'httpie' folder
    os.mkdir('httpie', mode=0o700)
    
    temp_path = Path('httpie/config.json')
    
    # Create a temp Config object
    temp_config = Config(directory=Path('httpie'))
    temp_config['key1'] = 'value1'
    
    # Save the temp config
    temp_config.save()
    
    # Check if config file is written by verifying the content
    # of the file
    with open(temp_path) as f:
        read = f.read()
        assert 'key1' in read and 'value1' in read

    # Remove httpie folder after testing
    shutil.rmtree('httpie')

# Generated at 2022-06-13 21:31:46.363546
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    a = BaseConfigDict("/path/to/file")
    a.load()



# Generated at 2022-06-13 21:31:47.563505
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    path = 'test.json'
    config = BaseConfigDict(path)
    config.load()

# Generated at 2022-06-13 21:31:57.045365
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    """
    GIVEN a sample config file (as JSON string)
    WHEN it is loaded and converted to a Python dictionary
    THEN the dictionary should be equal to the expected value.
    """
    test_filename = 'test_load.json'
    test_config_dir = Path(__file__).parent.parent / 'tests' / 'config'
    base_config_dict = BaseConfigDict(path=test_config_dir / test_filename)
    # Sample content of config file
    expected_value = {
        'foo': {
            'bar': 'baz',
            'nested': {'unicode': '\u20ac', 'list': [1, 2, 3]}
        }
    }

    base_config_dict.load()
    assert base_config_dict == expected_value

# Generated at 2022-06-13 21:31:58.453274
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    pass


# Generated at 2022-06-13 21:32:11.454167
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    tmpdir = Path(tempfile.gettempdir())

    class TestConfig(BaseConfigDict):
        def __init__(self, path):
            super().__init__(path)

    def test_path(path: str, expected_exception: Exception):
        try:
            TestConfig(path).load()
        except Exception as e:
            assert type(e) == type(expected_exception)
            assert e.args == expected_exception.args
        else:
            assert False

    test_path(str(tmpdir / 'non_existent'), IOError)
    test_path(str(tmpdir / 'non_json'), ConfigFileError)

    # test a path that exists, but has invalid json
    content = 'not json'
    tmpfile = tmpdir / 'that_exists'
    tmpfile.write

# Generated at 2022-06-13 21:32:16.934006
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config = Config()
    config.load()
    assert config.path

# Generated at 2022-06-13 21:32:22.000721
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        config = Config(directory=tmpdir)
        config.directory.mkdir(parents=True)
        config.save()
        config.load()
        assert config.get('__meta__') is not None


# Generated at 2022-06-13 21:32:37.618455
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config_dir = Path('/tmp/httpie_test_save')
    dir_path = config_dir / DEFAULT_CONFIG_DIRNAME
    config_path = dir_path / Config.FILENAME

    class TestConfig(BaseConfigDict):
        name = None
        helpurl = None
        about = None
    test_config = TestConfig(config_path)

    # Test initial creation
    if dir_path.exists():
        print(f'Deleting {dir_path}')
        shutil.rmtree(dir_path)
    assert test_config.is_new()
    test_config['test_key'] = 'test value'
    test_config.save()
    assert test_config.path.exists()

    # Test overwriting file

# Generated at 2022-06-13 21:32:48.060323
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import httpie.output.config

    env = {
        ENV_HTTPIE_CONFIG_DIR: 'test_env_httpie_config_dir',
        ENV_XDG_CONFIG_HOME: 'test_xdg_config_home'
    }

    def run():
        return httpie.output.config.get_default_config_dir()

    # Test default if env is not set
    with mock.patch('os.environ', {}):
        assert run() == Path.home() / Path('.config') / DEFAULT_CONFIG_DIRNAME

    # Test windows
    with mock.patch('httpie.output.config.is_windows', True):
        assert run() == Path(os.path.expandvars('%APPDATA%')) / DEFAULT_CONFIG_DIRNAME

    # Test

# Generated at 2022-06-13 21:33:00.690269
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Test 1: Windows
    import sys
    if sys.platform == 'win32':
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
    else:
        # Test 2: Legacy
        legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
        legacy_config_dir.mkdir()
        assert get_default_config_dir() == legacy_config_dir

        # Test 3: xdg
        home_dir = Path.home()
        xdg_config_home_dir = home_dir / DEFAULT_RELATIVE_XDG_CONFIG_HOME
        xdg_config_home_dir.mkdir()
        assert get_default_config_dir() == xdg_config_home_dir / DEFAULT_CONFIG

# Generated at 2022-06-13 21:33:14.202216
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # 1. explicitly set through env
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/foo/bar'
    assert get_default_config_dir() == Path('/foo/bar')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # 2. Windows
    orig_is_windows = is_windows
    is_windows = True
    assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
    is_windows = orig_is_windows

    # 3. legacy ~/.httpie
    path = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    path.touch()
    assert get_default_config_dir() == path

    # 4. XDG

# Generated at 2022-06-13 21:33:21.483673
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import io
    import os
    import pytest
    import tempfile
    from httpie.config import BaseConfigDict

    @pytest.fixture(scope='function')
    def workdir():
        name = None
        try:
            fd, name = tempfile.mkstemp(prefix='httpie-test-', suffix='.json')
            os.close(fd)
            os.remove(name)
            yield Path(name).parent

        finally:
            if name and os.path.exists(name):
                os.remove(name)

    def test_save(self, workdir):
        class Config(BaseConfigDict):
            name = 'test'

        config = Config(path=workdir / 'test.json')
        config.save()
        assert config.path.exists()
        assert config

# Generated at 2022-06-13 21:33:35.161440
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Should use legacy dir if it exists
    mock_legacy_path = '/home/httpie/.httpie'
    mock_xdg_path = '/home/httpie/.config/httpie'
    mock_env_path = '/home/httpie/.httpie'
    os.environ[ENV_HTTPIE_CONFIG_DIR] = mock_env_path
    mock_xdg_env_path = '/home/httpie/.config'
    os.environ[ENV_XDG_CONFIG_HOME] = mock_xdg_env_path
    with mock.patch('httpie.config.DEFAULT_CONFIG_DIR.exists', side_effect=[False, True]):
        path = get_default_config_dir()
        assert path.as_posix() == mock_legacy_path
    #

# Generated at 2022-06-13 21:33:37.468238
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    """
    The test case covers save method of class BaseConfigDict
    """
    config_obj = BaseConfigDict(Path())
    config_obj.save()

# Generated at 2022-06-13 21:33:38.649231
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    print(get_default_config_dir())

# Generated at 2022-06-13 21:33:49.409808
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    test_config = BaseConfigDict(Path("test.json"))
    try:
        test_config.load()
    except ConfigFileError as e:
        print(e)

# Generated at 2022-06-13 21:34:00.504005
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    import os
    import os.path

    import pytest
    from httpie.config import BaseConfigDict

    class ConfigDict(BaseConfigDict):
        name = 'test_config'
        helpurl = 'http://help.me'
        about = 'about info'

    tmpdir = pytest.ensuretemp(ConfigDict.name)
    path = os.path.join(tmpdir, 'config.json')
    c = ConfigDict(path=path)

    c['foo'] = 'bar'
    c.save()

    c2 = ConfigDict(path=path)
    assert c2['foo'] == 'bar'

    c2.delete()
    assert not os.path.exists(path)

# Generated at 2022-06-13 21:34:12.746084
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import os
    import shutil

    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/foo/bar'
    assert get_default_config_dir() == Path('/foo/bar')

    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
    else:
        assert get_default_config_dir() == Path.home() / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME

        # XDG disabled
        os.environ[ENV_XDG_CONFIG_HOME] = ''
        assert get_default_config_dir() == Path.home() / DEFAULT_CONFIG_DIRNAME

        # Legacy ~/.

# Generated at 2022-06-13 21:34:23.189388
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config_dict = BaseConfigDict('test_config.json')

    try:
        config_dict.save()
    except ConfigFileError as e:
        assert "cannot read config file: [Errno 2] No such file or directory: 'test_config.json'" in str(e)
    else:
        # should not get here
        pass

    config_dict.load()
    assert config_dict['default_options'] == config.default_options

    try:
        config_dict.update({'default_options': ['--json', '--form']})
        config_dict.save()
    except ConfigFileError:
        assert False

    config_dict.load()
    config_dict['default_options'] = ['--verbose', '--all']
    config_dict.save()

# Generated at 2022-06-13 21:34:34.002566
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    p = Path(__file__).parent
    config_path = p / 'test_BaseConfigDict_save.json'
    config_path.unlink(missing_ok=True)
    bc = BaseConfigDict(config_path)
    bc.save(fail_silently=True)
    bc.save()
    bc.save()
    bc['a'] = '1'
    bc.save()
    b = json.load(config_path.open('rt'))
    assert b.get('a') == '1'
    bc['b'] = '2'
    bc.save()
    bc.delete()

# Test for inheritance from dict

# Generated at 2022-06-13 21:34:39.610542
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config_dict = BaseConfigDict(path='/home/config.json')
    config_dict['key'] = 'value'
    config_dict.save()
    saved_config_dict = BaseConfigDict(path='/home/config.json')
    saved_config_dict.load()
    assert saved_config_dict['key'] == 'value'

# Generated at 2022-06-13 21:34:41.857073
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config_dict = BaseConfigDict("test")
    config_dict.load()



# Generated at 2022-06-13 21:34:48.840200
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    class ConfigFile(BaseConfigDict):
        name = "config"
        helpurl = "https://httpie.org/help"
        about = "https://httpie.org/about"

        def __init__(self, path: Path):
            super().__init__(path)

    dirname = tempfile.mkdtemp()
    path = Path(dirname) / "config.json"
    json_string = '{"b": ["a", "b"], "__meta__": {"about": "https://httpie.org/about", "httpie": "0.9.9", "help": "https://httpie.org/help"}}'
    path.write_text(json_string + '\n')
    config = ConfigFile(path)
    config.load()

# Generated at 2022-06-13 21:34:51.517634
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    p = Path(r"C:\Users\Administrator\.httpie\config.json")
    base = BaseConfigDict(p)
    base.load()
    print(base)



# Generated at 2022-06-13 21:34:59.927851
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    if os.path.exists('/tmp/test_BaseConfigDict_save.json'):
        os.remove('/tmp/test_BaseConfigDict_save.json')
    bcd = BaseConfigDict('/tmp/test_BaseConfigDict_save.json')
    bcd.save()
    assert os.path.exists('/tmp/test_BaseConfigDict_save.json')
    with open('/tmp/test_BaseConfigDict_save.json') as f:
        string = f.read()
        assert string == '{\n}' or string == '{\n    "__meta__": {\n        "httpie": ' + __version__.__version__ + '\n    }\n}'
    os.remove('/tmp/test_BaseConfigDict_save.json')



# Generated at 2022-06-13 21:35:25.756344
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class Config(BaseConfigDict):
        name = 'config'
        helpurl = 'http://example.org/help_config'
        about = 'example configuration file'

    json_string = json.dumps(
        obj={'__meta__': {'httpie': __version__, 'help': 'http://example.org/help_config', 'about': 'example configuration file'}},
        indent=4,
        sort_keys=True,
        ensure_ascii=True,
    )
    path = Path('/tmp/test.json').resolve()

    config = Config(path)
    config.save()

    with open(path, 'r') as f:
        assert f.read() == json_string + '\n'

    config.save()


# Generated at 2022-06-13 21:35:36.559324
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import os
    import os.path
    import shutil
    import tempfile

    def _mkdir(dir, parents=False):
        if not os.path.isdir(dir):
            if parents:
                _mkdir(os.path.dirname(dir), parents=parents)
            os.mkdir(dir)

    def _touch(file):
        if not os.path.isfile(file):
            with open(file, 'wt'):
                pass

    def _rm(path):
        if os.path.exists(path):
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path, ignore_errors=True)

    config_dir = get_default_config_dir()
   

# Generated at 2022-06-13 21:35:47.658729
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    from pathlib import Path
    from httpie.config import BaseConfigDict
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        test1 = BaseConfigDict(Path(tmpdir).joinpath("test.json"))
        with open(test1.path, 'w') as fp:
            fp.write("adfasd")
        try:
            test1.load()
        except ConfigFileError as e:
            assert str(e) == 'invalid basedict file: Expecting value: line 1 column 1 (char 0) [%s]' % test1.path
        else:
            raise Exception("ConfigFileError should be raised")

        with open(test1.path, 'w') as fp:
            fp.write("{'a': 1}")

# Generated at 2022-06-13 21:36:00.917337
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # 1. explicitly set through env
    env_config_dir = '/foo'
    os.environ[ENV_HTTPIE_CONFIG_DIR] = env_config_dir
    default_config_dir1 = get_default_config_dir()
    assert default_config_dir1 == Path(env_config_dir)

    # 2. Windows
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR)
    os.environ.pop(ENV_XDG_CONFIG_HOME)
    if is_windows:
        default_config_dir2 = get_default_config_dir()
        assert default_config_dir2 == DEFAULT_WINDOWS_CONFIG_DIR

    # 3. legacy ~/.httpie
    default_config_dir3 = get_default_config_dir()
    assert default_

# Generated at 2022-06-13 21:36:14.215970
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    from tempfile import TemporaryDirectory
    from json import loads
    from contextlib import contextmanager
    from unittest.mock import patch

    with TemporaryDirectory() as temp_dir:
        # create the config file
        config_path = Path(temp_dir) / 'config.json'
        config_data = {'name': 'test', 'path': config_path}
        config_string = json.dumps(config_data)
        config_path.write_text(config_string)

        # test the method load
        config_dict = BaseConfigDict(config_path)
        assert('name' not in config_dict)
        assert('path' not in config_dict)
        config_dict.load()
        assert(config_dict['name'] == 'test')

# Generated at 2022-06-13 21:36:17.557344
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    # test1: test for fail_silently=True
    configDict = BaseConfigDict("")
    configDict.save(fail_silently=True)
    # test2: test for fail_silently=False
    configDict.save()



# Generated at 2022-06-13 21:36:29.806748
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    from pytest import raises
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as tmp_dir:
        config = BaseConfigDict(path=Path(tmp_dir) / 'test.json')
        config.save()
        assert os.path.exists(config.path)
        assert config.path.read_text() == (
            '{\n'
            '    "__meta__": {\n'
            '        "httpie": "' + __version__ + '"'
            '\n'
            '    }\n'
            '}'
        )
        config = BaseConfigDict(path=Path(tmp_dir) / 'test.json')
        config.load()
        assert config['__meta__']['httpie'] == __version__


# Generated at 2022-06-13 21:36:40.088853
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    import json

    class A(BaseConfigDict):
        def __init__(self, path: Path):
            super().__init__(path)

    mydict = A(path="config.json")
    assert len(mydict) == 0

    mydict["a"] = "b"
    mydict.save()

    mydict = A(path="config.json")
    assert len(mydict) == 0

    mydict.load()
    assert len(mydict) == 2
    assert mydict["a"] == "b"



# Generated at 2022-06-13 21:36:52.840477
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    XDG_CONFIG_HOME = os.environ.get('XDG_CONFIG_HOME')
    XDG_CONFIG_DIRS = os.environ.get('XDG_CONFIG_DIRS')


# Generated at 2022-06-13 21:37:05.943518
# Unit test for function get_default_config_dir

# Generated at 2022-06-13 21:37:21.721053
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config = Config()
    config['abc'] = 'abc'
    config['helpurl'] = 'bcd'
    config['about'] = 'cba'
    config.save()



# Generated at 2022-06-13 21:37:34.237964
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import pytest
    from pathlib import Path
    from shutil import rmtree

    # 1. explicitly set through env
    _old_env_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR, None)
    _new_env_config_dir = '/foo/bar'
    os.environ[ENV_HTTPIE_CONFIG_DIR] = _new_env_config_dir
    p = get_default_config_dir()
    assert p == Path(_new_env_config_dir)

    os.environ[ENV_HTTPIE_CONFIG_DIR] = _old_env_config_dir
    if _old_env_config_dir is None:
        del os.environ[ENV_HTTPIE_CONFIG_DIR]  # type: ignore

    # 2

# Generated at 2022-06-13 21:37:43.077959
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import json
    import tempfile
    temp_dir = tempfile.TemporaryDirectory()
    try:
        test_class = BaseConfigDict(Path(temp_dir.name) / 'config.json')
        test_class.save()
        with (Path(temp_dir.name) / 'config.json').open('r') as f:
            data = json.load(f)
            assert len(data) == 1 and data['__meta__']
    finally:
        temp_dir.cleanup()



# Generated at 2022-06-13 21:37:47.883257
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    print('-'*10, 'test_BaseConfigDict_save', '-'*10)
    conf = BaseConfigDict(Path('/home/httpie/config.json'))
    conf['__meta__'] = {
        'httpie': __version__
    }
    conf.save()
    print('='*10)



# Generated at 2022-06-13 21:38:00.319828
# Unit test for function get_default_config_dir
def test_get_default_config_dir():

    import sys
    import os
    from io import StringIO
    from unittest.mock import patch

    stderr = StringIO()
    with patch.object(sys, 'stderr', stderr):
        def test(env_xdg_config_home, expected_output, expected_xdg_home):
            os.environ[ENV_XDG_CONFIG_HOME] = env_xdg_config_home
            os.environ[ENV_HTTPIE_CONFIG_DIR] = None
            assert get_default_config_dir() == Path(expected_output)
            assert os.environ[ENV_XDG_CONFIG_HOME] == expected_xdg_home


# Generated at 2022-06-13 21:38:03.657902
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() / '.config' / 'httpie'

# Generated at 2022-06-13 21:38:10.516324
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    class Test(BaseConfigDict):
        def __init__(self):
            self.path = Path(r'c:\test.json')
            self.helpurl = "https://github.com"
            self.about = "This is a test"
    a = Test()
    assert(a.load() == None)
    assert(a.update({'a':'b'}) == None)
    assert(a.update({'b':'c'}) == None)
    assert(a.save() == None)
    assert(a.load() == None)


# Generated at 2022-06-13 21:38:16.458447
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    configDir = '../tests/.httpie'
    configFile = 'config.json'
    configPath = os.path.join(configDir, configFile)

    try:
        test_BaseConfigDict_load.configDict = BaseConfigDict(Path(configPath))
        test_BaseConfigDict_load.configDict.load()
    except ConfigFileError:
        return False
    return True



# Generated at 2022-06-13 21:38:25.481259
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Windows
    assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Legacy
    os.environ[ENV_HTTPIE_CONFIG_DIR] = str(Path('~/.httpie').expanduser())
    assert get_default_config_dir() == Path(
        '~/.httpie').expanduser()
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)

    # Explicit
    os.environ[ENV_XDG_CONFIG_HOME] = str(Path('~/config').expanduser())

# Generated at 2022-06-13 21:38:34.605556
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    # Given
    directory_name = 'test_BaseConfigDict_save'
    file_name = 'config.json'
    metadata = {
        'httpie': '1.0'
    }
    content = {
        '__meta__': metadata,
        'key': 'value'
    }

    # When
    config = BaseConfigDict(directory=directory_name / file_name)
    config.save()
    file_content = json.loads(Path(directory_name / file_name).read_text())

    # Then
    assert json.loads(json.dumps(file_content)) == json.loads(json.dumps(content))

    # When
    metadata['httpie'] = '1.1'
    content['__meta__'] = metadata
    content['key'] = 'value2'
   

# Generated at 2022-06-13 21:39:11.369474
# Unit test for function get_default_config_dir

# Generated at 2022-06-13 21:39:16.882766
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    """
    Test whether BaseConfigDict can save into file successfully.
    """
    class TestBaseConfigDict(BaseConfigDict):
        name = 'test'

    test_config = TestBaseConfigDict(Path('test.json'))
    test_config.save()
    assert Path('test.json').exists()
    assert test_config.path.exists()

# Generated at 2022-06-13 21:39:28.626909
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert str(get_default_config_dir()).endswith('httpie')
    test_dir = '/tmp/this_dir_does_not_exist'
    os.environ[ENV_HTTPIE_CONFIG_DIR] = test_dir
    assert get_default_config_dir() == test_dir
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/etc/this/dir/does/not/exist'
    assert get_default_config_dir() == Path('/etc/this/dir/does/not/exist')
    os.environ[ENV_HTTPIE_CONFIG_DIR] = ''
    home = str(Path.home())

# Generated at 2022-06-13 21:39:30.853055
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
  config_dir = get_default_config_dir()
  assert config_dir.is_dir()

# Generated at 2022-06-13 21:39:35.643057
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    path = '/Users/lazetutida/Desktop/git/httpie-demo/httpie/demo.json'
    config_dict = BaseConfigDict(path)
    config_dict.load()
    config_dict.save()
    assert True

# Generated at 2022-06-13 21:39:38.901602
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() / Path('.config') / Path('httpie')