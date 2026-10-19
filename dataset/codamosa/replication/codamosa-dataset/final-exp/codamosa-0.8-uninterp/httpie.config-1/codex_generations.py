

# Generated at 2022-06-13 21:29:57.004453
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    print("\nTest method save of class BaseConfigDict...")
    print("\t-Create a new BaseConfigDict instance:")
    test = BaseConfigDict(Path("test.txt"))
    print("\t-Ensure the directory of file:")
    test.ensure_directory()
    print("\t-Save method:")
    test.save()
    print("\t-Delete the file:")
    test.delete()

# Generated at 2022-06-13 21:30:06.908242
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/foo/bar'
    assert get_default_config_dir() == Path('/foo/bar')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Mock os.environ on Windows
    if is_windows:
        os.environ[ENV_HTTPIE_CONFIG_DIR] = '/foo/bar'
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
        del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Mock os.environ on Unix-like system
    os.environ[ENV_XDG_CONFIG_HOME] = '/foo'
    assert get_default_config_dir() == Path('/foo/httpie')


# Generated at 2022-06-13 21:30:11.328521
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:30:23.169940
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    cwd = os.getcwd()
    os.chdir(os.path.expanduser('~'))
    try:
        dir_name = 'test_hier_conf'
        test_dir = Path(dir_name + '/foo/bar/baz')
        test_instance = BaseConfigDict(path=Path('~/.httpie/{0}'.format(dir_name)))
        test_instance.ensure_directory()
        os.rmdir(os.path.expanduser(str(test_dir)))
    finally:
        os.chdir(cwd)

# Generated at 2022-06-13 21:30:32.950690
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    from . import utils
    from .utils import temp_dir
    from .utils import mock

    with temp_dir() as temp_dir_path:
        # test new config
        test_config_file_path = temp_dir_path / 'config.json'
        test_config = BaseConfigDict(test_config_file_path)
        test_config.save()

        with utils.mock.patch('httpie.__version__', '1.0.0'):
            test_config.helpurl = 'https://github.com/jakubroztocil/httpie'

            test_config.save()
            with open(test_config_file_path) as f:
                json_data = json.load(f)
                # verify default config

# Generated at 2022-06-13 21:30:42.568267
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    PATH = Path('no/such/dir/file')
    DICT = {'json': 'dict'}

    try:
        base_config_dict = BaseConfigDict(path=PATH)
        base_config_dict.update(DICT)
        base_config_dict.save()
    except Exception as e:
        assert False, f'unexpected exception: {e}'

    try:
        assert PATH.read_text() == json.dumps(obj=DICT, indent=4)
    except Exception as e:
        assert False, f'unexpected exception: {e}'


# Generated at 2022-06-13 21:30:51.651906
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    def assert_config_dir(expected, **kwargs):
        with tempfile.TemporaryDirectory(**kwargs) as tmp:
            os.chmod(tmp, 0o700)
            assert get_default_config_dir() == Path(tmp) / DEFAULT_CONFIG_DIRNAME

    # 1. explicitly set through env
    with tempfile.TemporaryDirectory() as tmp:
        os.environ[ENV_HTTPIE_CONFIG_DIR] = str(Path(tmp))
        assert get_default_config_dir() == Path(tmp)

        del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # === Not Windows ===

    # 2. legacy ~/.httpie
    with tempfile.TemporaryDirectory() as tmp:
        Path(tmp) / DEFAULT_RELATIVE_LEGACY_CONFIG

# Generated at 2022-06-13 21:30:57.756086
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    class Test(BaseConfigDict):
        def __init__(self, path):
            super().__init__(path)

    t = Test('/a/b/c/test.json')
    t.ensure_directory()
    assert os.path.isdir('/a/b/c') is True
    shutil.rmtree('/a/b')


# Generated at 2022-06-13 21:31:06.854846
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class Config(BaseConfigDict):
        FILENAME = 'test_save.json'
        DEFAULTS = {
            'default_options': []
        }

        def __init__(self, directory: Union[str, Path] = DEFAULT_CONFIG_DIR):
            self.directory = Path(directory)
            super().__init__(path=self.directory / self.FILENAME)
            self.update(self.DEFAULTS)
            self.update({'url': 'http://httpbin.org/get'})

    config = Config()
    config.save()

    with open(str(config.path), 'r') as f:
        data = f.read()
        data_dict = json.loads(data)

    assert 'url' in data_dict.keys()

# Generated at 2022-06-13 21:31:19.813319
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    os.environ.pop(ENV_XDG_CONFIG_HOME, None)
    xdg_config_home = Path.home() / DEFAULT_RELATIVE_XDG_CONFIG_HOME
    assert get_default_config_dir() == xdg_config_home / DEFAULT_CONFIG_DIRNAME
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/tmp'
    assert get_default_config_dir() == Path('/tmp')
    os.environ[ENV_XDG_CONFIG_HOME] = '/tmp'
    assert get_default_config_dir() == Path('/tmp') / DEFAULT_CONFIG_DIRNAME



# Generated at 2022-06-13 21:31:24.541907
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:31:34.795689
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    from tempfile import mkdtemp
    from shutil import rmtree
    from .config import BaseConfigDict
    from .exceptions import ConfigFileError
    from .compat import is_windows

    # Check Invalid File Name
    path_invalid_fn = Path('/tmp/httpie/~#&*|')
    invalid_config = BaseConfigDict(path_invalid_fn)

    try:
        invalid_config.save()
    except (ConfigFileError, UnicodeEncodeError):
        if not is_windows:
            rmtree('/tmp/httpie', ignore_errors=True)
    else:
        invalid_config.delete()
        if not is_windows:
            rmtree('/tmp/httpie', ignore_errors=True)
        assert False

    # Check Invalid File Path
    path_

# Generated at 2022-06-13 21:31:44.753735
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    test_config_dir = Path('test_config')
    test_config_file = test_config_dir / 'config.json'
    test_config = Config(test_config_dir)
    test_config.ensure_directory()
    test_config['test_option'] = 'test_option_value'
    test_config.save()
    test_config = Config(test_config_dir)
    test_config.load()
    assert test_config['test_option'] == 'test_option_value'
    test_config.delete()
    test_config_dir.rmdir()

# Generated at 2022-06-13 21:31:54.590677
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    class Config(BaseConfigDict):
        def __init__(self, path):
            super().__init__(path)

    def reset_dir():
        if os.path.exists('dirname') :
            shutil.rmtree('dirname')

    test_dir = 'dirname'
    test_file_name = 'test_file'
    reset_dir()
    config = Config(test_dir + '/' + test_file_name)
    config.ensure_directory()
    assert os.path.exists(test_dir), f"{test_dir} does not exists"

    f = open('dirname/test_file', 'w')
    f.close()
    reset_dir()



# Generated at 2022-06-13 21:31:59.465881
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    path = Path('/tmp/httpie/test')
    assert path.exists() == False
    dict = BaseConfigDict(path)
    dict.ensure_directory()
    assert path.parent.exists() == True
    assert path.parent.is_dir() == True


# Generated at 2022-06-13 21:32:04.019610
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    config_dir = get_default_config_dir()
    assert(config_dir.name == DEFAULT_CONFIG_DIRNAME)
    assert(DEFAULT_CONFIG_DIR == config_dir)

# Generated at 2022-06-13 21:32:16.483552
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    """Unit test for BaseConfigDict.load()"""
    class TestClass(BaseConfigDict): pass
    # TODO: unit test for file not found
    # Load an empty config file
    c = TestClass('./unit_test.json')
    try:
        os.remove('./unit_test.json')
    except FileNotFoundError as e:
        pass
    try:
        c.load()
    except ConfigFileError as e:
        print(f'{e.args}')
    c.save()
    c.load()

    os.remove('./unit_test.json')

    # Load a normal config file
    c = TestClass('./unit_test.json')

# Generated at 2022-06-13 21:32:21.600296
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    configFile = BaseConfigDict("/tmp/test_ensure_directory.json")
    configFile.ensure_directory()
    assert os.path.exists("/tmp/test_ensure_directory.json")
    os.remove("/tmp/test_ensure_directory.json")


# Generated at 2022-06-13 21:32:30.494186
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    if is_windows:
        assert (get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR)
    else:
        assert (get_default_config_dir() == Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR)

# Generated at 2022-06-13 21:32:37.064447
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    import os
    import tempfile

    with tempfile.TemporaryDirectory() as temp_dir:
        config_dir = Path(temp_dir) / "httpie"
        config_path = config_dir / "config.json"

        config_dict = BaseConfigDict(config_path)
        config_dict.ensure_directory()

        assert os.path.isdir(config_dir)

# Generated at 2022-06-13 21:32:46.901565
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class TestDict(BaseConfigDict):
        name = 'test'
        helpurl = None
        about = None
        path = Path('test.json')

    test_dict = TestDict(path=path)
    test_dict['test'] = 'test'
    test_dict.save()

    with open('test.json', 'r') as f:
        assert 'test' in f.read()


# Generated at 2022-06-13 21:32:51.988324
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    with TemporaryDirectory() as td:
        test_path = Path(td) / 'testfile'
        test_config = BaseConfigDict(test_path)
        assert not test_path.exists()
        test_config.ensure_directory()
        assert test_path.exists()

# Generated at 2022-06-13 21:32:59.183428
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class TestConfig(BaseConfigDict):
        name = None
        helpurl = None
        about = None
    config = TestConfig(path=Path('tests/config.json'))
    config.update({'a': '1'})
    config.save()
    with Path('tests/config.json').open() as f:
        assert '{"a": "1", "__meta__": {"httpie": "1"}}\n' == f.read()


# Generated at 2022-06-13 21:33:04.435614
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # test for existing directory - this should not raise an error
    path = Path("/tmp/")
    obj = BaseConfigDict(path) 
    assert obj.ensure_directory() == None
    # test for non-existing directory - this should raise an error
    path = Path("/tmp/123")
    obj = BaseConfigDict(path) 
    with pytest.raises(OSError):
        assert obj.ensure_directory()


# Generated at 2022-06-13 21:33:10.268219
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    from httpie.config import get_default_config_dir, DEFAULT_CONFIG_DIR
    from os import environ
    
    if 'XDG_CONFIG_HOME' in environ.keys():
        config_home = Path(environ['XDG_CONFIG_HOME'])
        if not os.path.isdir(config_home) or not os.access(config_home, os.W_OK):
            config_home = Path(os.path.join(Path.home(), '.config'))
    else:
        config_home = Path(os.path.join(Path.home(), '.config'))

    # On Windows the test fails
    if not is_windows():
        assert get_default_config_dir() == config_home / DEFAULT_CONFIG_DIRNAME


# Generated at 2022-06-13 21:33:14.379947
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    dict = BaseConfigDict(Path('../../'))
    dict['k']='v'
    dict.save()
    print(dict)

# Generated at 2022-06-13 21:33:19.774264
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import tempfile
    tmpdir = tempfile.TemporaryDirectory()
    try:
        path = Path(tmpdir.name + "/config.json")
        d = BaseConfigDict(path)
        d.ensure_directory()
        d.save()
        assert path.exists()
        d['key1'] = 'value1'
        d.save()
        with path.open() as f:
            data = json.load(f)
        assert data == d
    finally:
        tmpdir.cleanup()


# Generated at 2022-06-13 21:33:25.123080
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    directory_name = BaseConfigDict.__init__.__defaults__[0]
    BaseConfigDict(directory_name).ensure_directory()
    assert directory_name.exists()



# Generated at 2022-06-13 21:33:29.456113
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    tmp_path = Path('/tmp/BaseConfigDict_save')
    config = BaseConfigDict(tmp_path)
    tmp_path.unlink(missing_ok=True)
    config.save()



# Generated at 2022-06-13 21:33:37.702404
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    class TestConfig(BaseConfigDict):
        pass

    tmp_config_path = tempfile.TemporaryDirectory()
    config_path = Path(tmp_config_path.name)

    tmp_config_sub_path = tempfile.TemporaryDirectory()
    config_sub_path = Path(tmp_config_sub_path.name)

    TestConfig(path=config_path).ensure_directory()
    TestConfig(path=config_sub_path).ensure_directory()

    assert config_path.exists() and config_path.is_dir()
    assert config_sub_path.exists() and config_sub_path.is_dir()

    tmp_config_sub_path.cleanup()
    tmp_config_path.cleanup()


if __name__ == '__main__':
    test_BaseConfig

# Generated at 2022-06-13 21:33:43.266844
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    file_name = 'data/config.json'
    path = Path(file_name)
    config = BaseConfigDict(path=path)
    config.save()



# Generated at 2022-06-13 21:33:57.089904
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    import os
    import shutil
    import json
    config_test_file = Path('test.json')
    if config_test_file.exists():
        config_test_file.unlink()

# Generated at 2022-06-13 21:34:11.834192
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Test function behavior with httpie environment variables
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/tmp/test1'
    assert '/tmp/test1' == str(get_default_config_dir())

    os.environ.pop(ENV_HTTPIE_CONFIG_DIR)
    assert '/tmp/test1' == str(get_default_config_dir())

    # Test function behavior with no environment variables
    os.environ[ENV_XDG_CONFIG_HOME] = '/tmp/test2'
    assert '/tmp/test2/httpie' == str(get_default_config_dir())

    os.environ.pop(ENV_XDG_CONFIG_HOME)

# Generated at 2022-06-13 21:34:17.705159
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class testConfig(BaseConfigDict):
        pass
    config = testConfig(Path('testfile'))
    config.update({'key': 'value'})
    config.save()
    with open(config.path, 'rt') as f:
        assert json.load(f)['key'] == 'value'
    config.delete()



# Generated at 2022-06-13 21:34:24.303881
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    import os
    import shutil
    import tempfile

    dirpath = tempfile.mkdtemp()
    try:
        a_file = os.path.join(dirpath, 'a_file')
        with open(a_file, 'w') as f:
            f.write('content')
        os.chmod(dirpath, 0o400)

        path = os.path.join(dirpath, 'foo.txt')
        config = BaseConfigDict(path)
        config.ensure_directory()

        assert os.path.exists(path)

    finally:
        shutil.rmtree(dirpath)

# Generated at 2022-06-13 21:34:35.677016
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # 1. explicitly set through env
    os.environ[ENV_HTTPIE_CONFIG_DIR] = "foo/bar"
    assert get_default_config_dir() == Path("foo/bar")
    del os.environ[ENV_HTTPIE_CONFIG_DIR]
    # 2. Windows
    assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
    # 3. legacy ~/.httpie
    home_dir = Path.home()
    legacy_config_dir = home_dir / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    if os.path.exists(legacy_config_dir):
        assert get_default_config_dir() == legacy_config_dir
    # 4. XDG

# Generated at 2022-06-13 21:34:41.005740
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    """Unit test for method save of class BaseConfigDict"""
    class TestConfigDict(BaseConfigDict):
        pass
    config = TestConfigDict(Path())
    config['hello'] = 'world'
    config.save()
    assert config['hello'] == 'world'
    config.delete()

# Generated at 2022-06-13 21:34:47.239090
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    print("--- TEST FOR FUNCTION: test_get_default_config_dir")
    print("--- DEFAULT_CONFIG_DIR = ", DEFAULT_CONFIG_DIR)
    print("--- DEFAULT_CONFIG_DIR = ", get_default_config_dir())
    assert DEFAULT_CONFIG_DIR == get_default_config_dir()

test_get_default_config_dir()

# Generated at 2022-06-13 21:34:54.185076
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    from pathlib import Path
    from httpie.config import DEFAULT_CONFIG_DIR
    from httpie.plugins import plugin_manager
    configfile = BaseConfigDict(DEFAULT_CONFIG_DIR / 'plugins/enabled.json')
    plugin_manager.set_core_plugins()
    configfile.load()
    assert 'builtin' in configfile['installed']


# Generated at 2022-06-13 21:35:01.285338
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import httpie
    import httpie.config
    import json
    import os

    configfile = httpie.config.DEFAULT_CONFIG_DIR + '/test.json'
    if os.path.exists(configfile):
        os.remove(configfile)

    config = BaseConfigDict(configfile)
    config['testkey'] = "testvalue"
    config['testkeylist'] = ["testvaluelist1", "testvaluelist2"]
    config.save()
    with open(configfile) as f:
        newconfig = json.load(f)
        assert newconfig['__meta__']['httpie']
        assert newconfig['testkey'] == config['testkey']
        assert newconfig['testkeylist'] == config['testkeylist']

    os.remove(configfile)


# Unit

# Generated at 2022-06-13 21:35:07.024801
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config = BaseConfigDict(path='')
    config.save = save = mock.Mock()

    config.save()

    assert save.called



# Generated at 2022-06-13 21:35:12.346965
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config_dict = BaseConfigDict(path="test.json")
    config_dict.save()
    assert os.path.exists("test.json")
    os.remove("test.json")


# Generated at 2022-06-13 21:35:13.682997
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:35:20.602280
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    import tempfile
    tempdir = tempfile.mkdtemp()
    path = Path(tempdir) / 'test.json'
    BaseConfigDict(path=path).ensure_directory()
    assert path.parent.exists()
    assert path.parent.is_dir()
    path.parent.rmdir()

# Generated at 2022-06-13 21:35:26.775226
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    """
    Check import from A
    """
    configFile = BaseConfigDict(Path("./test/test1.json"))
    configFile.load()
    assert {'glossary': {'title': 'example glossary'}} == configFile


# Generated at 2022-06-13 21:35:28.970862
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    conf = BaseConfigDict(Path('dummy_path'))
    conf.ensure_directory()
    assert 1==1

# Generated at 2022-06-13 21:35:38.659089
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    from tempfile import TemporaryDirectory
    from pathlib import Path
    from shutil import rmtree

    def is_directory(path : Path) -> bool:
        return path.is_dir()

    def is_file(path : Path) -> bool:
        return path.is_file()

    with TemporaryDirectory() as tmp_dir:
        tmp_dir = Path(tmp_dir)
        tmp_file = tmp_dir / 'test_file.json'
        assert is_directory(tmp_dir)
        assert not is_file(tmp_file)

        test_BaseConfigDict = BaseConfigDict(path=tmp_file)
        test_BaseConfigDict.ensure_directory()

        assert is_directory(tmp_dir)
        assert not is_file(tmp_file)


# Generated at 2022-06-13 21:35:50.434294
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # 1. explicitly set through env
    os.environ['HTTPIE_CONFIG_DIR'] = 'mydir1'
    assert get_default_config_dir() == Path('mydir1')
    os.environ.clear()
    # 2. Windows
    platform = sys.platform
    sys.platform = 'Windows'
    assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
    sys.platform = platform
    home_dir = Path.home()

    # 3. legacy ~/.httpie
    os.environ['HTTPIE_CONFIG_DIR'] = ''
    legacy_config_dir = home_dir / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(mode=0o700, parents=True)
    assert get_default_config_dir

# Generated at 2022-06-13 21:36:02.436032
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    homedir = Path.home()
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR
    assert get_default_config_dir() == \
        homedir / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME

    os.environ[ENV_XDG_CONFIG_HOME] = str(homedir / 'foo')
    assert get_default_config_dir() == \
        homedir / 'foo' / DEFAULT_CONFIG_DIRNAME

    os.environ[ENV_HTTPIE_CONFIG_DIR] = str(homedir / 'bar')
    assert get_default_config_dir() == homedir / 'bar'
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

# Generated at 2022-06-13 21:36:14.765908
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    c1 = BaseConfigDict('/Users/junrong/Desktop/file.txt')
    c1.load()
    print(c1)
    print(c1.path)
    print(c1._BaseConfigDict__Init__keys)
    print(c1.__class__)
    print(c1.__class__.__dict__)
    print(c1.__class__.__dict__['_BaseConfigDict__Init__keys'])
    print(c1.__class__.__dict__['__module__'])
    print(c1.__class__.__dict__['__doc__'])
    print(c1.__class__.__dict__['__dict__'])
    print(c1.__class__.__dict__['__dict__']['__doc__'])

# Generated at 2022-06-13 21:36:25.183125
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    path = "tests/resources/json/config"
    directory = Path(path)
    config = BaseConfigDict(directory / BaseConfigDict.FILENAME)
    config['default_options'] = ["--form", "--json"]
    config.save(fail_silently=True)
    assert path == 'tests/resources/json/config'



# Generated at 2022-06-13 21:36:27.374624
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    c = BaseConfigDict("test_file.json")
    c.ensure_directory()



# Generated at 2022-06-13 21:36:32.278114
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    import random
    dir_name = str(random.randint(1, 100000))
    path = Path.home() / dir_name
    if path.exists():
        path.rmdir()
    instance = BaseConfigDict(path)
    instance.ensure_directory()
    assert path.exists()
    path.rmdir()

# Generated at 2022-06-13 21:36:37.040871
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class TestConfig(BaseConfigDict):
        name = 'test'
        helpurl = 'www.baidu.com'
        about = 'test'

    test_config = TestConfig(DEFAULT_CONFIG_DIR / 'test_config.json')
    test_config.save()
    assert test_config.path.read_text() == r'{"__meta__": {"about": "test", "help": "www.baidu.com", "httpie": "0.9.8"}}'
    test_config.delete()


# Generated at 2022-06-13 21:36:46.426862
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Clear environment variables
    os.environ.pop(ENV_XDG_CONFIG_HOME, None)
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # Case for windows
    os.environ[ENV_HTTPIE_CONFIG_DIR] = "/do_not_exist"
    assert get_default_config_dir() == Path("/do_not_exist")

    os.environ[ENV_HTTPIE_CONFIG_DIR] = "1"
    assert get_default_config_dir() == Path("1")

    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    # Case for linux/mac

# Generated at 2022-06-13 21:36:55.316288
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    from tempfile import TemporaryDirectory
    from os import path, mkdir
    from os import makedirs as os_makedirs
    from os.path import exists
    from os.path import isdir
    from contextlib import contextmanager

    from unittest import mock
    # mock the os.makedirs method
    @contextmanager
    def mock_makedirs(name):
        try:
            yield
        except:
            pass

    with mock.patch('httpie.config.BaseConfigDict.ensure_directory', lambda self: os_makedirs(self.path)) as ensure:
        with TemporaryDirectory() as tmp_dir:
            config_dir = path.join(tmp_dir, 'test_config_dir')
            os_makedirs(config_dir)

# Generated at 2022-06-13 21:37:07.470445
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    TEST_ENV = {
        # 'XDG_CONFIG_HOME': '/path/to/XDG_CONFIG_HOME',
        # 'HTTPIE_CONFIG_DIR': '/path/to/HTTPIE_CONFIG_DIR',
    }
    for key, value in TEST_ENV.items():
        os.environ[key] = value

    assert get_default_config_dir() == Path('/path/to/HTTPIE_CONFIG_DIR')

    del os.environ['HTTPIE_CONFIG_DIR']

    assert get_default_config_dir() == Path('/path/to/XDG_CONFIG_HOME') / DEFAULT_CONFIG_DIRNAME

    del os.environ['XDG_CONFIG_HOME']
    if is_windows:
        assert get_default_config

# Generated at 2022-06-13 21:37:10.093591
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert DEFAULT_CONFIG_DIR == Path.home() / '.config' / 'httpie'

# Generated at 2022-06-13 21:37:22.972608
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    import os
    import tempfile
    tempdir = tempfile.TemporaryDirectory()
    testdir = tempdir.name

    class config(BaseConfigDict):
        name = 'test'
        def __init__(self):
            testpath = os.path.join(testdir, 'test.json')
            super().__init__(path=Path(testpath))

    fake_config_path = os.path.join(testdir, 'test.json')
    fake_config_file = open(fake_config_path, 'w')
    fake_data = '{"foo": "bar"}'
    fake_config_file.write(fake_data)
    fake_config_file.close()

    fake_config = config()
    fake_config.load()
    assert fake_config['foo'] == 'bar'
   

# Generated at 2022-06-13 21:37:27.941077
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    with mock.patch('os.environ', {
        ENV_XDG_CONFIG_HOME: '/xdg/config/home'
    }):
        assert get_default_config_dir() == Path('/xdg/config/home/httpie')

# Generated at 2022-06-13 21:37:32.566479
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR


# Generated at 2022-06-13 21:37:41.520180
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # 1. Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
        return

    # 2. legacy ~/.httpie
    Path.home().joinpath(DEFAULT_RELATIVE_LEGACY_CONFIG_DIR).mkdir(mode=0o700, parents=True)
    assert get_default_config_dir().name == DEFAULT_RELATIVE_LEGACY_CONFIG_DIR.name

    Path.home().joinpath(DEFAULT_RELATIVE_LEGACY_CONFIG_DIR).rmdir()

    # 3. XDG
    Path.home().joinpath(DEFAULT_RELATIVE_XDG_CONFIG_HOME).mkdir(mode=0o700, parents=True)

# Generated at 2022-06-13 21:37:51.239682
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import json
    from copy import copy
    from pathlib import Path

    from httpie.config import BaseConfigDict

    config_dir = Path.cwd() / 'test_config_dir'

    class DummyConfig(BaseConfigDict):
        def __init__(self, config_dir):
            self.path = config_dir / 'dummy_config.json'
            super().__init__(path=self.path)

    config = DummyConfig(config_dir)
    config.save()

    # Check default content
    path = Path(config_dir / 'dummy_config.json')
    assert path.exists() and path.is_file()
    with path.open() as file:
        assert json.load(file) == {'__meta__': {'httpie': __version__}}

    #

# Generated at 2022-06-13 21:37:52.240210
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir().exists()

# Generated at 2022-06-13 21:38:01.147712
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    from pathlib import Path
    from tempfile import TemporaryDirectory
    from json import loads

    with TemporaryDirectory() as tmpdir:
        config_dir = Path(tmpdir)
    config = Config(config_dir)
    config.save()

    with open(config_dir / Config.FILENAME, 'r') as f:
        json_str = f.read()
    json_obj = loads(json_str)
    assert json_obj['__meta__']['httpie'] == __version__
    assert json_obj['default_options'] == config.DEFAULTS['default_options']



# Generated at 2022-06-13 21:38:04.045184
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:38:12.417333
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # create empty directory
    dir_path = Path('/tmp/directory1')
    if not dir_path.exists():
        dir_path.mkdir(mode=0o700, parents=True)

    # create 2 files in empty directory
    file_path = Path('/tmp/directory1/file1')
    if not file_path.exists():
        file_path.touch()

    file_path = Path('/tmp/directory1/file2')
    if not file_path.exists():
        file_path.touch()

    # create an object from class BaseConfigDict, the
    # directory /tmp/directory1 already exists, so the
    # method ensure_directory() won't be executed
    test_object = BaseConfigDict(file_path)

    assert not test_object.is_new()

   

# Generated at 2022-06-13 21:38:21.163592
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    import os, os.path
    import shutil
    import tempfile
    from pathlib import Path
    from httpie.config import BaseConfigDict

    temp_dir = tempfile.mkdtemp().replace('\\', '/')
    config_filename = 'config.json'
    # Have no existence directory
    temp_path = Path(temp_dir) / config_filename
    assert temp_path.exists() == False
    # Create directory
    c = BaseConfigDict(temp_path)
    c.ensure_directory()
    # Check existence
    assert temp_path.exists() == False
    # Clean up
    os.remove(temp_dir + '/' + config_filename)
    os.rmdir(temp_dir)


# Generated at 2022-06-13 21:38:29.852866
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    uncompleted_path = Path("/home/user")
    completed_path = Path("/home/user/Documents")
    uncompleted_path.parent.mkdir(mode=0o700, parents=True)
    uncompleted_path.ensure_directory()
    completed_path.ensure_directory()
    assert uncompleted_path == Path("/home/user")
    assert completed_path == Path("/home/user/Documents")


# Generated at 2022-06-13 21:38:43.313941
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/tmp'
    assert get_default_config_dir() == Path('/tmp')
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR)

    os.environ[ENV_XDG_CONFIG_HOME] = '/tmp'
    assert get_default_config_dir() == Path('/tmp/httpie')
    os.environ.pop(ENV_XDG_CONFIG_HOME)

    assert get_default_config_dir() == Path.home() / '.config/httpie'

# Generated at 2022-06-13 21:38:55.552770
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # 1. explicitly set through env
    env_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    if env_config_dir:
        print(Path(env_config_dir))

    # 2. Windows
    if is_windows:
        print(DEFAULT_WINDOWS_CONFIG_DIR)

    home_dir = Path.home()

    # 3. legacy ~/.httpie
    legacy_config_dir = home_dir / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    if legacy_config_dir.exists():
        print(legacy_config_dir)

    # 4. XDG

# Generated at 2022-06-13 21:39:05.705475
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    """
    if the base class of config file can not find the config file, it will throw IOError
    else, it will read the config file and store the data into the dict
    """
    try:
        dic = BaseConfigDict("/httpie2/not-exists.conf")
        dic.load()
    except IOError as e:
        raise IOError("Config file /httpie2/not-exists.conf does not exist")

    dic = BaseConfigDict("config.json")
    dic.load()
    assert len(dic) != 0



# Generated at 2022-06-13 21:39:07.298719
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() / '.config' / 'httpie'

# Generated at 2022-06-13 21:39:17.974130
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # XDG Base Directory Specification support:
    # See https://wiki.archlinux.org/index.php/XDG_Base_Directory

    # 1. explicitly set through env
    # Environment variable HTTPIE_CONFIG_DIR has priority
    test_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    if test_dir:
        assert get_default_config_dir() == Path(test_dir)
        return

    # 2. Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
        return

    home_dir = str(Path.home())

    # 3. legacy ~/.httpie
    legacy_config_dir = home_dir + DEFAULT_RELATIVE_LEGACY_CONFIG_DIR

# Generated at 2022-06-13 21:39:29.271740
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    class TestDict(BaseConfigDict):
        name = 'test'
        helpurl = 'http://www.github.com/httpie/httpie'
        about = 'test about'

    config_dict = TestDict(Path('/tmp/test.json'))
    config_dict['default_options'] = ['bbb']
    config_dict.save()

    config_dict2 = TestDict(Path('/tmp/test.json'))
    config_dict2.load()
    assert config_dict2['default_options'] == ['bbb']
    config_dict2['default_options'].append('aaa')
    config_dict2.save()

    config_dict3 = TestDict(Path('/tmp/test.json'))
    config_dict3.load()

# Generated at 2022-06-13 21:39:40.516735
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    home_dir = Path.home()
    default_xdg_config_dir = home_dir / DEFAULT_RELATIVE_XDG_CONFIG_HOME

    # 1. explicitly set through env
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/path/to/config/directory'
    assert get_default_config_dir() == Path('/path/to/config/directory')
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR)

    # 2. Windows
    if is_windows:
        expected_path = DEFAULT_WINDOWS_CONFIG_DIR
    # 3. legacy ~/.httpie
    elif (home_dir / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR).exists():
        expected_path = home_dir / DEFAULT_RELATIVE_LE