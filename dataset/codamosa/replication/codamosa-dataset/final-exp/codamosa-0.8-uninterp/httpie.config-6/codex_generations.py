

# Generated at 2022-06-13 21:29:50.286808
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config = BaseConfigDict(path=Path('/tmp/config.json'))
    config.save()

# Generated at 2022-06-13 21:30:03.284907
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    from unittest import mock
    from httpie import config
    import pathlib
    PATH_MOCK_VALUE = 'mock_value'
    pathlib.Path = mock.MagicMock(return_value=PATH_MOCK_VALUE)

    DEFAULT_CONFIG_DIR_MOCK_VALUE = 'mock_value'
    config.DEFAULT_CONFIG_DIR = DEFAULT_CONFIG_DIR_MOCK_VALUE
    assert config.get_default_config_dir() is DEFAULT_CONFIG_DIR_MOCK_VALUE

    HOME_DIR_MOCK_VALUE = 'mock_value'
    config.DEFAULT_CONFIG_DIR = None
    os.environ.pop(config.ENV_HTTPIE_CONFIG_DIR, None)

# Generated at 2022-06-13 21:30:06.184877
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    try:
        DEFAULT_CONFIG_DIR.unlink()
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise


# Generated at 2022-06-13 21:30:07.286772
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    pass

# Generated at 2022-06-13 21:30:18.722432
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    pass
    # # case-1: dir exists
    # def ensure_directory(self):
    #     try:
    #         self.path.parent.mkdir(mode=0o700, parents=True)
    #     except OSError as e:
    #         if e.errno != errno.EEXIST:
    #             raise



# Generated at 2022-06-13 21:30:24.222421
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    test_config_dir = (Path(os.getcwd()) / "tests/unit_tests/config")
    test_config = BaseConfigDict(test_config_dir / Config.FILENAME)
    test_config.ensure_directory()

    assert test_config_dir.exists()
    test_config_dir.rmdir()
    assert not test_config_dir.exists()

# Generated at 2022-06-13 21:30:26.862865
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    try:
        Config("test_config").save(fail_silently=True)
    except:
        raise Exception("save failed!")

# Generated at 2022-06-13 21:30:35.191172
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    test_env_xdg_home = os.path.expanduser('~/xyz')
    test_env_httpie_config_dir = os.path.expanduser('~/abc')
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

    os.environ[ENV_XDG_CONFIG_HOME] = test_env_xdg_home
    assert get_default_config_dir() == Path(
        test_env_xdg_home) / DEFAULT_CONFIG_DIRNAME
    assert get_default_config_dir() == Path(
        test_env_xdg_home) / DEFAULT_CONFIG_DIRNAME

# Generated at 2022-06-13 21:30:46.501010
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    # To test for invalid json format
    try:
        os.chdir(os.path.expanduser('~'))
        test_config = Config()
        test_config['default_options'] = ['-v', 'httpbin.org/get']
        test_config.save()

        with open('config.json', 'w') as f:
            f.write('{')

        test_config2 = Config()
        test_config2.load()
    except ConfigFileError:
        # if the test case fails, clean the directory
        os.remove('config.json')
    else:
        raise AssertionError('The test case fails')
    
    # To test for invalid directory

# Generated at 2022-06-13 21:30:54.636084
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    from httpie.config import BaseConfigDict
    from pathlib import Path
    import os

    config = BaseConfigDict(Path(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../docs/config.json')))
    config.load()

    assert config['__meta__'] == {'httpie': '0.9.9'}

# Generated at 2022-06-13 21:31:07.122811
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    # Create a class
    class TestBaseConfigDict(BaseConfigDict):
        pass

    # Create the directory for the file
    test_dir_path = Path('./test-dir')
    test_dir_path.mkdir(mode=0o700, parents=True)

    # Create an instance of the test class
    test_config = TestBaseConfigDict(path=test_dir_path / 'test.json')

    # Put some data into the instance
    test_config['key1'] = 'value'
    test_config['key2'] = 123

    # Save the instance
    test_config.save()

    # Create a new instance and load the file
    new_test_config = TestBaseConfigDict(path=test_dir_path / 'test.json')
    new_test_config.load()



# Generated at 2022-06-13 21:31:09.558900
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:31:11.968764
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    config_dir = get_default_config_dir()
    print(config_dir)

# Generated at 2022-06-13 21:31:19.564970
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import shutil
    import os
    import httpie.config
    import tempfile
    print("Testing class BaseConfigDict, method save ....")
    tmpdirpath = tempfile.mkdtemp()
    try:
        c = httpie.config.BaseConfigDict(tmpdirpath)
        c['default_options'] = ['--json']
        c.save()
        assert os.path.isfile(os.path.join(tmpdirpath, 'config.json'))
    finally:
        shutil.rmtree(tmpdirpath)

# Generated at 2022-06-13 21:31:31.490051
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    # https://github.com/jakubroztocil/httpie/blob/fd41e01b7c1b8280619c030f6b29d6caa2991294/httpie/config.py#L150
    import datetime

    # test saving configuration with write_text
    def test_write_text():
        # initialize the test with hardcoded values
        # write values to file
        # check with assert if the file has been actually created
        pass

    # test saving configuration with json serialization
    def test_json_serialization():
        # initialize the test with hardcoded values
        # serialize values with json and write to file
        # check with assert if the file has been actually created
        pass

    # test saving configuration with json serialization and ensure_ascii=True

# Generated at 2022-06-13 21:31:45.494088
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    test_xdg_config_home = '/tmp'
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    config_dir = get_default_config_dir()
    assert config_dir == DEFAULT_WINDOWS_CONFIG_DIR

    config_dir = get_default_config_dir()
    assert config_dir == DEFAULT_WINDOWS_CONFIG_DIR

    os.environ[ENV_HTTPIE_CONFIG_DIR] = str(Path('/tmp'))
    config_dir = get_default_config_dir()
    assert config_dir == Path('/tmp')

    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    home_dir = Path.home()
    legacy_config_dir = home_dir / DEFAULT_RELATIVE_LE

# Generated at 2022-06-13 21:31:50.074686
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    config = BaseConfigDict(path=Path(BASE_DIR) / Path("test/config.json"))
    config.ensure_directory()
    assert os.path.exists(os.path.join(BASE_DIR,"test"))


# Generated at 2022-06-13 21:32:01.564079
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import os
    from pathlib import Path

    ENV_HOME = 'HOME'
    ENV_XDG_CONFIG_HOME = 'XDG_CONFIG_HOME'
    ENV_HTTPIE_CONFIG_DIR = 'HTTPIE_CONFIG_DIR'
    DEFAULT_CONFIG_DIRNAME = 'httpie'
    DEFAULT_RELATIVE_XDG_CONFIG_HOME = Path('.config')
    DEFAULT_RELATIVE_LEGACY_CONFIG_DIR = Path('.httpie')
    HOME = str(Path.home())
    WINDOWS_APPDATA = str(Path('%APPDATA%'))
    DEFAULT_XDG_CONFIG_HOME = HOME + '/.config'


# Generated at 2022-06-13 21:32:04.612493
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    configDict = BaseConfigDict('config.json')
    configDict.ensure_directory() 


# Generated at 2022-06-13 21:32:09.345456
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save(): 
    path = os.path.join(os.getcwd(), 'config.json')
    config = BaseConfigDict(path = path)
    config.save()
    assert os.path.exists(path) and os.path.isfile(path)
    os.remove(path)


# Generated at 2022-06-13 21:32:24.239857
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config_dir = Path('C:\\Users\\tengmingj\\.httpie')
    config_file_name = 'config.json'
    test_output = {
        'default_options': [
            '--json',
            '--verbose',
            '--style', 'solarized'
        ]
    }
    c = Config(config_dir)
    #test config_dict and c
    assert c['default_options'] == []
    #test initialize
    assert c.FILENAME == 'config.json'
    assert c.DEFAULTS == {'default_options': []}
    #test method load
    c.directory = config_dir
    assert c.path == 'C:\\Users\\tengmingj\\.httpie\\config.json'
    c.load()
    assert c.default_

# Generated at 2022-06-13 21:32:28.177850
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:32:35.506049
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import unittest

    class TestConfigDir(unittest.TestCase):
        def test_get_default_config_dir(self):
            from httpie.config import get_default_config_dir
            print(get_default_config_dir())
            self.assertTrue(get_default_config_dir())
            self.assertIsInstance(get_default_config_dir(), Path)

    unittest.main()

# Generated at 2022-06-13 21:32:44.977902
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    path = Path("/tmp/config-file.json")
    new_obj = {"name": "Python"}

    base_config_dict = BaseConfigDict(path)
    base_config_dict.update(new_obj)
    base_config_dict.save()

    assert path.exists()
    # Load object from file
    with path.open("rt") as config_file:
        loaded_obj = json.load(config_file)
        # Checked that loaded object is same as created
        assert loaded_obj == new_obj
    # Cleanup
    path.unlink()


# Generated at 2022-06-13 21:32:52.589139
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    from tempfile import TemporaryDirectory
    from os import path

    with TemporaryDirectory() as tmpdir:
        class Test(BaseConfigDict):
            def __init__(self):
                super().__init__(path)

        path = path.join(tmpdir, 'test.json')
        t = Test()
        assert t.ensure_directory() == None
        assert path.startswith(tmpdir)


# Generated at 2022-06-13 21:32:58.045570
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # in a regular directory
    class TestConfigDict(BaseConfigDict):
        pass
    path = Path('/tmp/test')
    test = TestConfigDict(path)
    test.ensure_directory()
    assert os.access(path.parent, os.R_OK)
    assert os.access(path.parent, os.W_OK)
    assert os.access(path.parent, os.X_OK)

    # in a directory that requires root
    class TestConfigDict(BaseConfigDict):
        pass
    path = Path('/var/log/test')
    test = TestConfigDict(path)
    try:
        test.ensure_directory()
        assert False
    except OSError:
        pass


# Generated at 2022-06-13 21:33:05.933897
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    # If there is no specification of abspath, then abspath is set to \.config\httpie\config.json.
    baseconfigdict = BaseConfigDict('config.json')
    # Ensure_directory is used to create directory.
    # If the directory already exists, it will not affect the subsequent test case.
    baseconfigdict.ensure_directory()
    # Save the file, write to the specified path \.config\httpie\config.json.
    # If the directory does not exist, it will be created.
    baseconfigdict.save()
    # Check if the file exists.
    # If the file exists, it means that the data is successfully written.
    assert os.path.exists('config.json') == True


# Generated at 2022-06-13 21:33:13.464983
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    path = Path(DEFAULT_CONFIG_DIR)
    config = BaseConfigDict(path)
    path.mkdir(mode=0o700, parents=True)
    try:
        path = path / 'test.json'
        assert config.load() is None
        assert path.write_text('{"a":1}') is None
        assert config.load() is None
        assert config['a'] == 1
    finally:
        path.unlink()
        path.parent.rmdir()


# Generated at 2022-06-13 21:33:21.124142
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import os.path
    from tempfile import mkdtemp
    from shutil import rmtree
    from httpie.config import BaseConfigDict

    config_file = 'test.json'
    config_info = {'test': 'test'}
    temp_dir = mkdtemp()
    config_path = os.path.join(temp_dir, config_file)


# Generated at 2022-06-13 21:33:23.396069
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() / '.config' / 'httpie'



# Generated at 2022-06-13 21:33:30.793838
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:33:35.718032
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class MyConfigDict(BaseConfigDict):
        def __init__(self, path):
            self.path= path

    my_config = MyConfigDict('/tmp/config.json')
    # since path.parent is not None, the helper
    # method 'ensure_directory' will execute
    my_config.save()

# Generated at 2022-06-13 21:33:48.575807
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import json
    import os
    import shutil
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as tmpdir:
        # make sure the temporary directory is readable and writable
        tmpdir = os.path.join(tmpdir, '1')
        os.mkdir(tmpdir)
        config_path = os.path.join(tmpdir, 'config.json')
        config = BaseConfigDict(path=config_path)
        config['foo'] = 'bar'
        config.save()
        assert config_path in os.listdir(tmpdir)
        with open(config_path) as f:
            data = json.load(f)
            assert data['foo'] == 'bar'
            assert data['__meta__']['httpie'] == __version__

# Generated at 2022-06-13 21:33:59.435386
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    from httpie.config import BaseConfigDict
    from os import path
    test_dict = BaseConfigDict("test.json")
    # ensure_directory()
    test_dict.ensure_directory()
    assert path.exists("test.json")
    # save()
    test_dict.update({"name": "Ben", "age": "18"})
    json_string = json.dumps({"name": "Ben", "age": "18"})
    with open("test.json","r") as f:
        assert json_string in f.read()
    # delete()
    test_dict.delete()
    assert not path.exists("test.json")

# Generated at 2022-06-13 21:34:02.823175
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    BCD = BaseConfigDict(path=Path('config_2.json'))
    BCD.ensure_directory()

# Generated at 2022-06-13 21:34:04.105987
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    c = Config()
    c.save()



# Generated at 2022-06-13 21:34:16.398051
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    os.environ.pop(ENV_XDG_CONFIG_HOME, None)

    with mock.patch('httpie.config.Path') as Path_mock:
        Path_mock.home.return_value = 'HOME_DIR'
        Path_mock.return_value.exists.return_value = False

        if is_windows:
            default_config_dir = DEFAULT_WINDOWS_CONFIG_DIR
        else:
            default_config_dir = Path('HOME_DIR', '.config', DEFAULT_CONFIG_DIRNAME)

        assert get_default_config_dir() == default_config_dir
        Path_mock.assert_called_with(default_config_dir)
        Path_mock().ex

# Generated at 2022-06-13 21:34:23.504853
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class Conf(BaseConfigDict):
        name = 'config'
        helpurl = 'https://httpie.org'
        about = 'HTTPie config file'
        DEFAULTS = {
            'default_options': ['--form']
        }

    conf1 = Conf('test.json')

    conf1['default_options'] = ['--json']
    conf1['__meta__'] = {}
    conf1.save()
    conf2 = Conf('test.json')
    assert '--json' in conf2['default_options']

    conf2.delete()
    assert not os.path.exists('test.json')

# Generated at 2022-06-13 21:34:33.063792
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    # Path("./data/").mkdir(parents=True, exist_ok=True)
    d = BaseConfigDict(path=Path("./data/config.txt"))
    try:
        d['url'] = 'www.example.com/example'
        d['body'] = 'body'
        d['option'] = '--pretty=all'
        d.save()
    finally:
        os.remove(str(d.path))
    # d.save()


if __name__ == '__main__':
    test_BaseConfigDict_save()

# Generated at 2022-06-13 21:34:35.845029
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:34:53.753969
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    dir_path = Path('./test/data/config')
    path = dir_path / 'config'
    config = BaseConfigDict(path)
    config.load()
    assert config == {
        '__meta__': {
            'httpie': '0.2.0',
            'help': 'https://github.com/jkbrzt/httpie#configuration',
        },
    }



# Generated at 2022-06-13 21:35:02.372033
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # ensure nothing is set
    for variable_name in [ENV_HTTPIE_CONFIG_DIR, ENV_XDG_CONFIG_HOME]:
        try:
            del os.environ[variable_name]
        except KeyError:
            pass

    # test default httpie config directory
    # -------------------------------------------------------------------------
    # |  env-xdg-config    | env-httpie-config   | default-httpie-config      |
    # |--------------------|---------------------|----------------------------|
    # | n/a                | n/a                 | ~/.config/httpie           |
    # | /config            | n/a                 | /config/httpie             |
    # | n/a                | $HOME/httpie-config | $HOME/httpie-config        |
    # -------------------------------------------------------------------------

    # httpie config directory does not exist


# Generated at 2022-06-13 21:35:05.290005
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config = BaseConfigDict("./data/test.json")
    config.update({"test":"test"})
    assert dict(config) == {"test":"test"}


# Generated at 2022-06-13 21:35:10.236578
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR
    os.environ[ENV_HTTPIE_CONFIG_DIR] = str(Path.home() / 'foo')
    assert get_default_config_dir() == Path.home() / 'foo'



# Generated at 2022-06-13 21:35:12.591101
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    BaseConfigDict.save()

# Generated at 2022-06-13 21:35:13.545730
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    get_default_config_dir()



# Generated at 2022-06-13 21:35:21.530807
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    class TestConfigDict(BaseConfigDict):
        def __init__(self, directory: Union[str, Path]):
            super().__init__(path=directory)
            self['force_colors'] = False
            self['history_file'] = str(Path.home() / '.httpie/history.json')

    # Test for function 'ensure_directory' of class 'BaseConfigDict'
    dir_to_be_ensured = Path('path/to/config/dir')

    assert dir_to_be_ensured.exists() is False

    # initialize an obj of class TestConfigDict
    test_config_dict = TestConfigDict(directory=dir_to_be_ensured)

    test_config_dict.ensure_directory()   # call function 'ensure_directory' of class 'BaseConfig

# Generated at 2022-06-13 21:35:29.328126
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import os
    import json
    import shutil
    from pathlib import Path
    from itertools import product
    from httpie import __version__
    from httpie.context import Environment
    from httpie.config import EnvironmentDefaults

    environment = Environment(
        default_options=EnvironmentDefaults(),
        config_dir=Path('PATH'),
    )
    env_path = environment.config_dir.parent
    env_path.mkdir(mode=0o700, parents=True)

    for fail_silently, env_config_dir in product([True, False], [None, 'PATH']):
        # update env for each loop
        os.environ.update(HTTPIE_CONFIG_DIR=env_config_dir)

        # save config
        environment.config.save(fail_silently=fail_silently)


# Generated at 2022-06-13 21:35:35.190858
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    from httpie.config import BaseConfigDict

    cfg = BaseConfigDict(Path('/home/user/.config/httpie/config.json'))
    cfg.load()
    cfg.get('__meta__')
    assert cfg['__meta__']['httpie'] == __version__, "config.__meta__['httpie'] doesn't match httpie.__version__"


# Generated at 2022-06-13 21:35:43.973824
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path(os.path.expanduser('~/.config/httpie'))

    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/foo/bar'
    assert get_default_config_dir() == Path(os.environ[ENV_HTTPIE_CONFIG_DIR])

    os.environ[ENV_XDG_CONFIG_HOME] = '/xdg/config'
    assert get_default_config_dir() == Path(os.environ[ENV_XDG_CONFIG_HOME]) / DEFAULT_CONFIG_DIRNAME

    os.environ.pop(ENV_XDG_CONFIG_HOME)

# Generated at 2022-06-13 21:36:16.255359
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Windows
    if is_windows:
        assert get_default_config_dir() == Path(
            os.path.expandvars('%APPDATA%')) / DEFAULT_CONFIG_DIRNAME
    # Legacy
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    os.environ.pop(ENV_XDG_CONFIG_HOME, None)
    assert get_default_config_dir() == (
        Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR)
    # XDG
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    os.environ.pop(ENV_XDG_CONFIG_HOME, None)

# Generated at 2022-06-13 21:36:21.258806
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # test to see if the method can raise error when parent directory cannot be created
    config_file_1=BaseConfigDict(Path('/root/config.json'))
    try:
        config_file_1.ensure_directory()
    except Exception as e:
        assert True
    else:
        assert False

    # test to see if the method can create the parent directory
    config_file_2 = BaseConfigDict(Path('./config.json'))
    try:
        config_file_2.ensure_directory()
    except Exception:
        assert False
    else:
        assert True


# Generated at 2022-06-13 21:36:33.086572
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    temp_dir = tempfile.TemporaryDirectory()
    temp_path = Path(temp_dir.name) / 'httpie'
    path = temp_path / 'config.json'
    test_dict = {'log-format': '1'}
    config = BaseConfigDict(path)
    config.ensure_directory = mock.Mock()
    with mock.patch('httpie.config.json.dumps') as mock_json_dumps:
        mock_json_dumps.return_value = json.dumps(obj=test_dict)
        config.save(fail_silently=False)
    config.ensure_directory.assert_called_once()
    assert path.is_file()
    assert config['__meta__']['httpie'] == __version__



# Generated at 2022-06-13 21:36:34.571029
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
        config_dict = Config()
        config_dict.save()
        assert config_dict['default_options']

# Generated at 2022-06-13 21:36:42.223340
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config_path = Path(__file__).parent / "test_load.json"
    bd = BaseConfigDict(config_path)
    bd.load()
    print(bd)
    bd["__meta__"] = {"httpie": "not empty"}
    print(bd)
    bd["not_empty"] = "not_empty"
    bd.save()



# Generated at 2022-06-13 21:36:50.796024
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    my_tmp_dir = Path.home() / 'tmp'
    my_tmp_dir.mkdir(parents=True, exist_ok=True)
    my_tmp_file = my_tmp_dir/'tmp_file.json'
    my_tmp_file.write_text("{'1': 2, '3': 4, '5': 6}")
    my_dict = BaseConfigDict(path=my_tmp_file)
    my_dict.load()
    assert '1' in my_dict
    assert my_dict['1'] == 2


# Generated at 2022-06-13 21:37:04.620713
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    os.environ[ENV_HTTPIE_CONFIG_DIR] = str(Path.home() / 'my-config-dir')
    assert get_default_config_dir() == Path(os.environ[ENV_HTTPIE_CONFIG_DIR])

    os.environ.pop(ENV_HTTPIE_CONFIG_DIR)
    assert get_default_config_dir() == Path(
        '~/.config/httpie'
    ).expanduser()

    os.environ[ENV_XDG_CONFIG_HOME] = '/some/abs/path'
    assert get_default_config_dir() == Path('/some/abs/path/httpie')

    os.environ[ENV_XDG_CONFIG_HOME] = 'some/rel/path'
    assert get_default_config

# Generated at 2022-06-13 21:37:15.299711
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # To run: pytest test_config.py::test_get_default_config_dir

    # https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch.dict
    with patch.dict('os.environ', {}, clear=True):
        assert get_default_config_dir() == Path.home() / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME

    with patch.dict('os.environ', {ENV_XDG_CONFIG_HOME: '/tmp'}, clear=True):
        assert get_default_config_dir() == Path('/tmp') / DEFAULT_CONFIG_DIRNAME


# Generated at 2022-06-13 21:37:24.338278
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    test_directory = './test_directory'
    if os.path.exists(test_directory):
        os.system(f'rm -rf {test_directory}')
    os.mkdir(test_directory)
    config = Config(f'./{test_directory}')
    config.load()
    if config.is_new():
        config.save()

    test_config = BaseConfigDict('./test_directory/config.json')
    test_config.ensure_directory()
    test_config.save()


if __name__ == "__main__":
    test_BaseConfigDict_save()

# Generated at 2022-06-13 21:37:32.524788
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    file_ = tempfile.NamedTemporaryFile()
    path = Path(file_.name)
    config_dict = BaseConfigDict(path)
    def_opt = config_dict['default_options'] = ['--json']
    config_dict.save()
    with file_.file:
        assert json.load(file_.file) == {'__meta__': {'httpie': __version__},
                                         'default_options': def_opt}
    file_.close()

# Generated at 2022-06-13 21:38:33.692487
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    home_dir = Path.home()
    test_dir = Path('.httpietest')

    # Check that XDG_CONFIG_HOME defaults to ~/.config/
    assert get_default_config_dir() == home_dir / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME

    # Check that XDG_CONFIG_HOME is overridable via env
    os.environ[ENV_XDG_CONFIG_HOME] = str(home_dir / test_dir)
    assert get_default_config_dir() == home_dir / test_dir / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]

    # Check that HTTPIE_CONFIG_DIR is overridable via env

# Generated at 2022-06-13 21:38:46.620346
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # pylint: disable=W0612
    saved_env = dict(os.environ)

# Generated at 2022-06-13 21:38:53.222159
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    with TempFile('{ "one": 1 }') as fp:
        config = BaseConfigDict(fp)
        config.load()
        assert config == {"one": 1}
    with TempFile('') as fp:
        config = BaseConfigDict(fp)
        config.load()
        assert config == {}
    with TempFile('invalid') as fp:
        config = BaseConfigDict(fp)
        with pytest.raises(ConfigFileError):
            config.load()


# Generated at 2022-06-13 21:38:55.927437
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    this_config = Config()
    this_config['default_options'] = ['--form']
    this_config.save(fail_silently=True)
    


# Generated at 2022-06-13 21:39:08.391210
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    import json
    import os
    import tempfile
    from pathlib import Path

    class CustomConfig(BaseConfigDict):
        FILENAME = 'config.json'
        DEFAULTS = {
            'default_options': []
        }

    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir) / 'config.json'
        os.chdir(tmpdir)
        with path.open('w') as f:
            json.dump({'greeting': 'hi'}, f)

        customobj = CustomConfig(path)
        assert customobj['greeting'] == 'hi'
        customobj.save()
        customobj.load()
        assert customobj['greeting'] == 'hi'
        customobj.delete()



# Generated at 2022-06-13 21:39:12.746108
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config = Config()
    config.save()
    assert config.path.exists()

    config_json = config.path.read_text()
    assert '"default_options": []' in config_json

    config.path.unlink()



# Generated at 2022-06-13 21:39:20.349466
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    _test_path = Path('./test_files/test_config.json')
    _test_config_dict = BaseConfigDict(_test_path)
    _test_config_dict['test_key'] = "test_value"
    try:
        _test_path.unlink()
    except OSError:
        pass
    assert _test_config_dict.is_new()
    _test_config_dict.save()
    assert _test_path.exists()
    with _test_path.open('rt') as f:
        _test_json = json.load(f)
    assert "test_key" in _test_json
    assert _test_json["test_key"] == "test_value"
    

# Generated at 2022-06-13 21:39:30.648099
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    def is_valid_directory(path: Path) -> bool:
        return (str(path).endswith(DEFAULT_CONFIG_DIRNAME) and
                path.parent == Path.home())

    def set_xdg_variable(directory_name: str) -> None:
        os.environ[ENV_XDG_CONFIG_HOME] = str(
            Path.home() / Path(directory_name)
        )

    # No value is set for HTTPIE_CONFIG_DIR.
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)

    # On Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
        return

    # The legacy configuration directory exists.
    legacy_config_dir = Path.home()

# Generated at 2022-06-13 21:39:38.163888
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdirname:
        config = Config(directory=tmpdirname)

        new_config = {'default_options': ['--json', '--verbose']}
        config.update(new_config)

        config.save()

        config_loaded = Config(directory=tmpdirname)
        config_loaded.load()

        assert config_loaded['default_options'] == new_config['default_options']

# Generated at 2022-06-13 21:39:46.984708
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # set xdg config home
    os.environ[ENV_XDG_CONFIG_HOME] = '/data/config'
    assert get_default_config_dir() == Path('/data/config/httpie')

    # set HTTPIE_CONFIG_DIR
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/data/config'
    assert get_default_config_dir() == Path('/data/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Windows
    class _Windows:
        @staticmethod
        def is_windows():
            return True
        @staticmethod
        def getenv(name):
            return os.environ.get(name)

    # set xdg config home