

# Generated at 2022-06-13 21:30:00.994947
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    default_config_dir = get_default_config_dir()
    default_config_file = default_config_dir / 'config.json'
    test_config_file = default_config_dir.parent / 'test.json' 
    dir_config = BaseConfigDict(test_config_file)
    dir_config.ensure_directory()
    assert os.path.exists(default_config_dir.parent)
    assert os.path.exists(default_config_dir.parent / 'test.json')
    os.remove(test_config_file)

if __name__ == "__main__":
    test_BaseConfigDict_ensure_directory()

# Generated at 2022-06-13 21:30:09.355337
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    os.environ.pop(ENV_XDG_CONFIG_HOME, None)
    assert get_default_config_dir() == Path.home() / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME
    os.environ[ENV_XDG_CONFIG_HOME] = '/tmp/xdg'
    assert get_default_config_dir() == Path('/tmp/xdg') / DEFAULT_CONFIG_DIRNAME
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/tmp/httpie'
    assert get_default_config_dir() == Path('/tmp/httpie')


# Generated at 2022-06-13 21:30:10.623239
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config_dict = BaseConfigDict()
    config_dict.save()


# Generated at 2022-06-13 21:30:15.873647
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/foo/bar'
    assert get_default_config_dir() == '/foo/bar'

    os.environ.pop(ENV_HTTPIE_CONFIG_DIR)
    os.environ[ENV_XDG_CONFIG_HOME] = '/foo/bar'
    assert get_default_config_dir() == '/foo/bar/httpie'

    os.environ.pop(ENV_XDG_CONFIG_HOME)
    assert get_default_config_dir() == '~/.config/httpie'

if __name__ == '__main__':
   test_get_default_config_dir()

# Generated at 2022-06-13 21:30:22.049345
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    # parameter path is a directory
    path = Path("config")
    BaseConfigDict(path).load()
    path.rmdir()
    # parameter path is a file
    path = Path("config.json").touch()
    BaseConfigDict(path).load()
    path.unlink()


# Generated at 2022-06-13 21:30:32.076175
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    def _get_home(env_name: str, default_value: str) -> str:
        try:
            return os.environ[env_name]
        except KeyError:
            return default_value
    def _get_xdg_home(xdg_env_name: str, default_relative: Path) -> Path:
        return Path(_get_home(xdg_env_name, str(Path.home()) + str(default_relative)))
    # 1. explicitly set through env
    try:
        del os.environ[ENV_HTTPIE_CONFIG_DIR]
    except KeyError:
        pass
    assert get_default_config_dir() == _get_xdg_home(ENV_XDG_CONFIG_HOME, DEFAULT_RELATIVE_XDG_CONFIG_HOME) / DEFAULT

# Generated at 2022-06-13 21:30:44.647960
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # No HTTPIE_CONFIG_DIR, no XDG_CONFIG_HOME, not Windows
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    os.environ.pop(ENV_XDG_CONFIG_HOME, None)

    # The default config dir is the legacy default.
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

    # HTTPIE_CONFIG_DIR overrides everything.
    with_httpie_dir = Path('/dummy') / DEFAULT_CONFIG_DIRNAME
    os.environ[ENV_HTTPIE_CONFIG_DIR] = with_httpie_dir
    assert get_default_config_dir() == with_httpie_dir

    # XDG_CONFIG_HOME overrides ... nothing.
    os.en

# Generated at 2022-06-13 21:30:50.581142
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    from httpie.config import BaseConfigDict
    from tempfile import mkstemp
    temp_fd, temp_path = mkstemp()
    with open(temp_path, 'w') as temp_file:
        temp_file.write('{}')

    try:
        cdict = BaseConfigDict(Path(temp_path))
        cdict.load()
    except IOError as e:
        if e.errno != errno.ENOENT:
            raise


# Generated at 2022-06-13 21:30:52.043741
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    base_config_dict = BaseConfigDict()
    assert base_config_dict.path == None
    base_config_dict.ensure_directory()
    assert base_config_dict.path == None


# Generated at 2022-06-13 21:30:57.701752
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    temp_file='temp_config.json'
    with open(temp_file,'w',encoding='utf-8') as f:
        f.write('{}')
    f.close()
    config = BaseConfigDict(path=temp_file)
    config.load()
    os.remove(temp_file)


# Generated at 2022-06-13 21:31:12.478671
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    pre_test_env = os.environ.copy()

# Generated at 2022-06-13 21:31:21.712665
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config_dir = Path(__file__).parent / '../tests/fixtures/config'
    path_file_exists = Path(config_dir / 'config.json')
    path_file_not_exists = Path(config_dir / 'not_exists.json')
    path_invalid_json = Path(config_dir / 'invalid.json')

    config = BaseConfigDict(path_file_exists)
    # Test load config file exists
    config.load()
    assert config['__meta__']['httpie'] == '0.0.0'
    assert config['default_options'] == ['--form']

    config = BaseConfigDict(path_file_not_exists)
    # Test load config file not exists
    config.load()
    assert dict(config) == dict()

   

# Generated at 2022-06-13 21:31:31.377665
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    tmp_path = Path('/tmp')
    test_file = tmp_path / 'test_BaseConfigDict.json'
    if test_file.exists():
        test_file.unlink()

    try:
        with test_file.open('wt') as f:
            f.write('{')

        d = BaseConfigDict(test_file)
        d.load()
    except ConfigFileError:
        pass
    else:
        raise AssertionError('ConfigFileError not raised')
    finally:
        if test_file.exists():
            test_file.unlink()


# Generated at 2022-06-13 21:31:40.280883
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class test_config(BaseConfigDict):
        name = 'test'
        helpurl = 'https://www.httpie.org/docs'
        about = 'https://www.httpie.org/getting-started'

    config = test_config(path = Path.home() / "test.json")
    config.save()



# Generated at 2022-06-13 21:31:48.280900
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    class TestConfigDict(BaseConfigDict):
        name = 'TestConfig'
        helpurl = 'TestConfig-Help'
        about = 'TestConfig-About'

    base_config_dict = TestConfigDict(Path('./test_config.json'))
    # test invaild json format
    base_config_dict['test_key'] = 'test_value'
    with base_config_dict.path.open('w') as f:
        f.write('test_config')
    with base_config_dict.path.open('r') as f:
        text = f.read()
    assert text == 'test_config'
    base_config_dict.load()
    assert base_config_dict['__meta__']['httpie'] == __version__

# Generated at 2022-06-13 21:31:55.658977
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config_dir = Path('./.httpie')
    config = BaseConfigDict(path=config_dir)
    config['Key'] = 'Value'
    config.save()
    config['Key'] = 'Value1'
    config.load()
    assert config['Key'] == 'Value'
    assert 'Value' == config['Key']
    config.delete()

# Generated at 2022-06-13 21:31:56.809495
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    raise NotImplementedError


# Generated at 2022-06-13 21:31:59.312034
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config = BaseConfigDict(path=Path('config.json'))
    config.load()
    print(config)



# Generated at 2022-06-13 21:32:03.608049
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config =  BaseConfigDict("/tmp/file.txt")
    config.ensure_directory()
    assert Path("/tmp/file.txt").exists()


# Generated at 2022-06-13 21:32:05.573440
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    b = BaseConfigDict(Path("test/test.json"))
    assert b.path.exists()

# Generated at 2022-06-13 21:32:13.485008
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() / '.config' / 'httpie'

# Generated at 2022-06-13 21:32:25.145465
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import tempfile
    import shutil
    import stat


# Generated at 2022-06-13 21:32:38.729724
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # If config directory exists we set env variable
    def set_env(path):
        return os.environ.update({ENV_HTTPIE_CONFIG_DIR: str(path)})

    # Make new config directory in temp dir
    with TemporaryDirectory() as d:
        config_dir = Path(d) / 'httpie'
        config_dir.mkdir(mode=0o700, parents=True)

        # Test that we can set HTTPIE_CONFIG_DIR
        set_env(config_dir)
        assert config_dir == get_default_config_dir()

        # Test that plain HTTPIE_CONFIG_DIR is set even if it doesn't exist
        set_env(Path(d) / 'httpie2')
        assert get_default_config_dir() == Path(d) / 'httpie2'




# Generated at 2022-06-13 21:32:40.873952
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() / '.config' / 'httpie'

# Generated at 2022-06-13 21:32:47.147868
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR
    os.environ[ENV_XDG_CONFIG_HOME] = '/foo'
    assert get_default_config_dir() == Path('/foo') / DEFAULT_CONFIG_DIRNAME
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/boo'
    assert get_default_config_dir() == Path('/boo')

# Generated at 2022-06-13 21:32:56.213467
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    class testDict(BaseConfigDict):
        def __init__(self, path: Path):
            super().__init__(path=path)

    file_path = Path("test.json")

    testDict(file_path)
    file_path.write_text("{}")
    testDict(file_path).load()
    assert file_path.read_text() == "{}"


if __name__ == "__main__":
    test_BaseConfigDict_load()
    print("Everything passed")

# Generated at 2022-06-13 21:32:59.037733
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert(get_default_config_dir().to_string() == join(expanduser("~"), '.config', 'httpie', 'config.json'))



# Generated at 2022-06-13 21:33:06.901108
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # $HTTPIE_CONFIG_DIR explicitly set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = 'foo'
    assert get_default_config_dir() == 'foo'
    # Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
    # Legacy ~/.httpie
    home_dir = Path.home()
    legacy_config_dir = home_dir / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(mode=0o700, parents=True)
    assert get_default_config_dir() == legacy_config_dir
    # $XDG_CONFIG_HOME explicitly set
    os.environ[ENV_XDG_CONFIG_HOME] = 'bar'

# Generated at 2022-06-13 21:33:16.142289
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():

    # Path where file is created
    test_path = Path('./test/')
    
    # Create config file (dictionary) 
    config = BaseConfigDict(test_path/'config2.json')
    config['test'] = 'test'
    
    # Test to save file
    config.save()

    # Test if file was created
    assert config.path.is_file()

    # Test if file can be read
    with open(config.path,'r') as f: 
        assert f.read()
    
    # Test if file can be deleted
    os.remove(config.path)

# Generated at 2022-06-13 21:33:22.444236
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class Config_test(BaseConfigDict):
        name = 'test'
    config_test=Config_test(Path('~/.httpie/test.json'))
    config_test['a'] = 1
    config_test['b'] = 2
    config_test.save()
    with open('~/.httpie/test.json', "r") as infile:
        config_test_content = json.load(infile)
        assert config_test_content['a'] == 1
        assert config_test_content['b'] == 2
# Test for method load of class BaseConfigDict

# Generated at 2022-06-13 21:33:39.996274
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # raise ConfigFileError if cannot create
    dir_path = Path('/tmp/httpie/test_oh_no/')
    dir_path.mkdir(parents=True)
    dir_path.chmod(0o500)
    baseconfigdict = BaseConfigDict(dir_path)
    with pytest.raises(ConfigFileError):
        baseconfigdict.ensure_directory()

    # no raise if already exist
    dir_path = Path('/tmp/httpie/test_oh_no_but_ok/')
    dir_path.mkdir(parents=True)
    baseconfigdict = BaseConfigDict(dir_path)
    baseconfigdict.ensure_directory()

    # no raise if successful
    dir_path = Path('/tmp/httpie/test_oh_yes/')
    baseconfig

# Generated at 2022-06-13 21:33:49.585774
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config_file_dict = BaseConfigDict(Path('/tmp/testconfigdict.json'))
    config_file_dict.ensure_directory()
    config_file_path = config_file_dict.path
    assert config_file_path.parent.is_dir()
    if config_file_path.parent.exists():
        config_file_path.parent.rmdir()
        assert config_file_path.parent.exists() is not True



# Generated at 2022-06-13 21:34:01.202080
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class DummyConfigDict(BaseConfigDict):
        def __init__(self, directory: Union[str, Path] = DEFAULT_CONFIG_DIR):
            self.directory = Path(directory)
            super().__init__(path=self.directory / self.FILENAME)

    def test_save(dicc):
        dicc.save()
        with open(dicc.path, "r") as file:
            assert dicc == json.load(file)

    Path.mkdir(DEFAULT_CONFIG_DIR, mode=0o700, parents=True)
    dicc = DummyConfigDict()
    dicc['test'] = list(range(10))
    dicc['test_str'] = "test string"
    test_save(dicc)


# Generated at 2022-06-13 21:34:03.834664
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    # Test case: load a valid config file
    path = Path.cwd() / 'config.json'
    config = BaseConfigDict(path)
    config.load()
    # Test case: load an invalid config file
    path = Path.cwd() / 'config_invalid.json'
    config = BaseConfigDict(path)
    try:
        config.load()
    except ConfigFileError as e:
        return "Passed"



# Generated at 2022-06-13 21:34:05.547853
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    path = get_default_config_dir()
    assert path == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:34:17.928449
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    """
    Test the function get_default_config_dir()
    """
    # 1. explicitly set through env
    os.environ[ENV_HTTPIE_CONFIG_DIR] = 'customconfig'
    assert get_default_config_dir() == 'customconfig'

    # 2. Windows
    if is_windows:
        expected_path = Path(os.path.expandvars('%APPDATA%')) / DEFAULT_CONFIG_DIRNAME
        assert get_default_config_dir() == expected_path

    # 3. legacy ~/.httpie
    home_dir = Path.home()
    legacy_config_dir = home_dir / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    if legacy_config_dir.exists():
        assert get_default_config_dir() == legacy_config

# Generated at 2022-06-13 21:34:25.056440
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    test_directory = Path('test_directory')
    test_directory.mkdir()

    test_file = test_directory / 'test_file'
    test_file.touch()
    test_file.chmod(420)
    
    # Open file and write test string
    test_file.open('w') and test_file.write('Testing')

    # Create object
    config_dict_object = BaseConfigDict(test_file)

    # Change file's access mode
    config_dict_object.ensure_directory()
    assert test_file.stat().st_mode & 777 == 420
    
    # Cleanup
    test_file.unlink()
    test_directory.rmdir()
    

# Generated at 2022-06-13 21:34:35.737976
# Unit test for function get_default_config_dir
def test_get_default_config_dir():

    # 1. PATH/ENV explicitly set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/my/config/dir'

    assert get_default_config_dir() == Path('/my/config/dir')

    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # 2. Windows
    if is_windows:

        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # 3. Legacy ~/.httpie

    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR

    legacy_config_dir.mkdir(mode=0o700, parents=True)

    assert get_default_config_dir() == legacy_config_dir

    legacy_config_dir.rmdir()

    #

# Generated at 2022-06-13 21:34:38.421686
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    test_path = Path('/test/test_config.json')
    test_dict = BaseConfigDict(test_path)
    try:
        test_dict.ensure_directory()
        assert(os.path.exists("/test"))
        assert(os.access("/test", os.W_OK))
    finally:
        if os.path.exists("/test"):
            os.removedirs("/test")

# Generated at 2022-06-13 21:34:47.447730
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # 1. explicitly set through env
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/foo/.httpie'
    assert get_default_config_dir() == Path('/foo/.httpie')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # 2. Windows
    assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # 3. legacy ~/.httpie
    try:
        os.mkdir(Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR)
        assert get_default_config_dir == Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
   

# Generated at 2022-06-13 21:35:10.121384
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '~/foo/bar'
    assert str(get_default_config_dir()) == '~/foo/bar'
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    os.environ[ENV_XDG_CONFIG_HOME] = '~/foo/bar'
    assert str(get_default_config_dir()) == '~/foo/bar/httpie'
    del os.environ[ENV_XDG_CONFIG_HOME]

    assert str(get_default_config_dir()) == '~/.config/httpie'

# Generated at 2022-06-13 21:35:16.350036
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Even when HOME is not set we can get the directory
    if os.environ.get('HOME'):
        del os.environ['HOME']
    default_config_dir = get_default_config_dir()
    assert default_config_dir == Path(r'C:\Users') / DEFAULT_CONFIG_DIRNAME

# Generated at 2022-06-13 21:35:25.788072
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    """Test method ensure_directory of BaseConfigDict."""
    from tempfile import TemporaryDirectory
    from pathlib import Path
    from shutil import rmtree

    with TemporaryDirectory() as d:
        path = Path(d)
        config = BaseConfigDict(path=path / 'config.json')

        # empty directory
        config.ensure_directory() # no exception?

        # deep directory
        deep_path = path / 'a/b/c/d/e'
        config.path = deep_path / 'config.json'
        config.ensure_directory() # no exception?
        assert deep_path.exists()

        # directory with a file
        file_path = path / 'file'
        file_path.touch()
        config.path = file_path / 'config.json'

# Generated at 2022-06-13 21:35:34.844164
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    from pathlib import Path
    import json

    import pytest

    def helper_load(path: Path, config: BaseConfigDict):
        try:
            with path.open('rt') as f:
                try:
                    data = json.load(f)
                except ValueError as e:
                    raise ConfigFileError(
                        f'invalid {config} file: {e} [{path}]'
                    )
                config.update(data)
        except IOError as e:
            if e.errno != errno.ENOENT:
                raise ConfigFileError(f'cannot read {config} file: {e}')



# Generated at 2022-06-13 21:35:36.046873
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config = BaseConfigDict(path='/home/user/test/test.json')
    config.load()
    assert config['__meta__']['httpie'] == __version__


# Generated at 2022-06-13 21:35:37.140984
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    print(get_default_config_dir())


# Generated at 2022-06-13 21:35:43.344418
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    cfg = BaseConfigDict(Path("test.json"))
    cfg["a"] = "b"
    cfg.save()
    with open("test.json") as f:
        assert f.readline() == "{'__meta__': {'httpie': '3.3.0'}, 'a': 'b'}\n"
        f.close()

if __name__ == "__main__":
    test_BaseConfigDict_save()

# Generated at 2022-06-13 21:35:52.356689
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class TestConfig(BaseConfigDict):
        FILENAME = 'config.json'
        DEFAULTS = {
            'default_options': []
        }

        def __init__(self, directory: Union[str, Path] = DEFAULT_CONFIG_DIR):
            self.directory = Path(directory)
            super().__init__(path=self.directory / self.FILENAME)
            self.update(self.DEFAULTS)

        @property
        def default_options(self) -> list:
            return self['default_options']

    test_config = TestConfig()
    print(test_config.save())
    test_config.save()
    # pytest.main()

test_BaseConfigDict_save()


# Generated at 2022-06-13 21:35:59.399609
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # set a default config dict to a random path
    path = '/tmp/{}'.format(random.random())
    baseConfigDict = BaseConfigDict(path)
    # ensure that this path does not exist
    assert not os.path.exists(path)
    # call ensure_directory method
    baseConfigDict.ensure_directory()
    # assert that path does now exist
    assert os.path.exists(path)

# Generated at 2022-06-13 21:36:02.838183
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() /'.config/httpie'
    assert get_default_config_dir(ENV_XDG_CONFIG_HOME) == \
        Path('/home/xdg_config_home') / 'httpie'

# Generated at 2022-06-13 21:36:36.115158
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    '''
    Checks that ensure_directory() on an existing directory does not raise an error and
    that on a non-existent directory it creates the directory.
    '''
    directory = Path('/tmp/').resolve()
    x = BaseConfigDict(directory.joinpath('file'))
    x.ensure_directory()

    if not directory.exists():
        raise Exception('Directory could not be created')

    try:
        x.ensure_directory()
    except:
        raise Exception('Directory could not be created')



# Generated at 2022-06-13 21:36:41.728882
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    # 任意目录
    cur = os.path.dirname(os.path.realpath(__file__))
    cur = os.path.dirname(cur)
    cur = os.path.dirname(cur)
    cur = os.path.dirname(cur)
    cur = os.path.dirname(cur)
    cur = os.path.dirname(cur)
    cur = os.path.dirname(cur)
    cur = os.path.dirname(cur)
    cur = os.path.dirname(cur)
    cur = os.path.dirname(cur)
    cur = os.path.dirname(cur)
    cur = os.path.dirname(cur)
    cur = os.path.dirname(cur)
    cur = os.path.dirname

# Generated at 2022-06-13 21:36:46.552022
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    dic = BaseConfigDict(Path.home() / 'test.txt')
    dic['user'] = 'root'
    dic['password'] = '123'
    dic.save()
    dic['password'] = '456'
    dic.save()


# Generated at 2022-06-13 21:36:52.194730
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import os
    assert os.path.expanduser('~') in get_default_config_dir().__str__()
    assert DEFAULT_CONFIG_DIRNAME in get_default_config_dir().__str__()

    assert os.path.expandvars('%APPDATA%') in get_default_config_dir().__str__()


# Generated at 2022-06-13 21:36:56.217938
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    # test config load when the file is not exist
    config = Config()
    config["test"] = "test"
    config.save()
    config.delete()
    config.load()
    assert config == {}



# Generated at 2022-06-13 21:37:04.037288
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    if is_windows:
        dir = get_default_config_dir()
        assert dir == DEFAULT_WINDOWS_CONFIG_DIR
    else:
        del os.environ[ENV_XDG_CONFIG_HOME]
        dir = get_default_config_dir()
        assert dir == os.path.expanduser('~/.config/httpie')

        os.environ[ENV_XDG_CONFIG_HOME] = 'XDG_CONFIG_HOME'
        dir = get_default_config_dir()
        assert dir == 'XDG_CONFIG_HOME/httpie'

# Generated at 2022-06-13 21:37:14.582547
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    from unittest import mock
    from httpie.context import Environment
    from httpie.config import DEFAULT_CONFIG_DIRNAME
    from pathlib import Path
    import os

    env = Environment()
    env.stdout = mock.MagicMock()
    env.stderr = mock.MagicMock()
    env.config = mock.MagicMock()

    home_dir = Path.home()
    default_xdg_config_dir = home_dir / '.config' / DEFAULT_CONFIG_DIRNAME

    with mock.patch('os.environ.get') as os_environ_get:
        # environment is explicitly set
        env.config_dir = (
            Path('/path/to/explicit/config/dir')
        )

# Generated at 2022-06-13 21:37:25.504254
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # 1. explicitly set through env
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/test/config'
    assert get_default_config_dir() == Path('/test/config')

    # 2. Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # 3. legacy ~/.httpie
    home_dir = Path.home()
    legacy_config_dir = home_dir / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir()
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()

    # 4. XDG
    # 4.1. explicit

# Generated at 2022-06-13 21:37:32.703226
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import tempfile
    test_dir = Path(tempfile.gettempdir())
    class CustomConfigDict(BaseConfigDict):
        name = "CustomConfigDict"
    config_file_path = test_dir / 'test_config.json'
    config = CustomConfigDict(config_file_path)
    config.save()
    assert config_file_path.exists()
    config.delete()


# Generated at 2022-06-13 21:37:36.043189
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    import pytest
    c = BaseConfigDict(Path('C:\\Users\\test\\test.json'))
    #test for exception
    with pytest.raises(ConfigFileError):
        c.ensure_directory()

# Generated at 2022-06-13 21:38:14.886421
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    from tempfile import TemporaryDirectory
    from shutil import copytree
    from os import environ, makedirs
    
    with TemporaryDirectory() as td:
        environ['HOME'] = td
        # 1. httpie explicitly set through env
        environ[ENV_HTTPIE_CONFIG_DIR] = '/foo/bar'
        assert get_default_config_dir() == Path('/foo/bar')
        environ.pop(ENV_HTTPIE_CONFIG_DIR)

        # 2. Windows
        if is_windows:
            assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

        # 3. legacy ~/.httpie
        legacy_config_dir = Path(td)/ DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
        legacy_config_dir.mkdir()

# Generated at 2022-06-13 21:38:31.043259
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import os
    # First, set the environment variables
    env_httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    env_xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

# Generated at 2022-06-13 21:38:42.248556
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    """
    Test if the default configuration directory is returned
    with and without other environment variables set
    """
    assert get_default_config_dir() == (Path.home() / '.config' / 'httpie')
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '~/.foo'
    assert get_default_config_dir() == '~/.foo'
    del os.environ[ENV_HTTPIE_CONFIG_DIR]
    os.environ[ENV_XDG_CONFIG_HOME] = '~/.bar'
    assert get_default_config_dir() == (Path.home() / '.bar' / 'httpie')
    del os.environ[ENV_XDG_CONFIG_HOME]

# Generated at 2022-06-13 21:38:53.417389
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    def assert_path(key, value, path):
        os.environ[key] = value
        assert get_default_config_dir() == path

    # test_get_default_config_dir case 1
    assert_path(ENV_HTTPIE_CONFIG_DIR, '/foo/bar', Path('/foo/bar'))

    # test_get_default_config_dir case 2
    assert_path(ENV_XDG_CONFIG_HOME, '/foo/bar', Path('/foo/bar/httpie'))

    # test_get_default_config_dir case 3
    assert_path(ENV_XDG_CONFIG_HOME, '', Path(Path.home() / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME))

# Generated at 2022-06-13 21:38:56.022866
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config = BaseConfigDict('test.json')
    # If the config file doesn't exist, the function will return
    try:
        config.load()
    except Exception:
        return

# Generated at 2022-06-13 21:39:00.580800
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
    os.environ[ENV_XDG_CONFIG_HOME] = '/home/user/.other_config'
    assert get_default_config_dir() == Path('/home/user/.other_config/httpie')
    del os.environ[ENV_XDG_CONFIG_HOME]
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/home/user/.other_config/httpie'
    assert get_default_config_dir() == Path('/home/user/.other_config/httpie')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]
    assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

# Generated at 2022-06-13 21:39:12.398429
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    def get_expected_xdg_config_dir():
        # 1. explicitly set through env
        env_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
        if env_config_dir:
            return Path(env_config_dir)

        # 2. Windows
        if is_windows:
            return DEFAULT_WINDOWS_CONFIG_DIR

        home_dir = Path.home()

        # 3. legacy ~/.httpie
        legacy_config_dir = home_dir / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
        if legacy_config_dir.exists():
            return legacy_config_dir

        # 4. XDG

# Generated at 2022-06-13 21:39:20.375988
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config_dir = Path('/xpto/config/dir')
    config_path = config_dir / Config.FILENAME

    config = Config(directory='/xpto/config/dir')
    config['a'] = 1
    config['b'] = 'a'
    config['c'] = True

    if not config_dir.is_dir():
        os.makedirs(config_dir)

    config.save()

    config = None
    config = Config(directory='/xpto/config/dir')
    config.load()

    assert config['a'] == 1
    assert config['b'] == 'a'
    assert config['c'] == True
    assert config['__meta__']['httpie'] == __version__

    if config_path.is_file():
        config_path.unlink()

# Generated at 2022-06-13 21:39:24.217575
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config = BaseConfigDict('test.json')
    config.load()
    assert config == {'__meta__' : {'httpie' : '0.9.9'}}


# Generated at 2022-06-13 21:39:25.830930
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR