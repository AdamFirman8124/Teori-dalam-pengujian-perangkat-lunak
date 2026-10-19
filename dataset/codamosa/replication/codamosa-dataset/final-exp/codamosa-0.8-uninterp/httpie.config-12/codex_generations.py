

# Generated at 2022-06-13 21:29:44.568318
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    tempdir = tempfile.mkdtemp(prefix='httpie-')

    try:
        config_dir = Path(tempdir) / 'config'
        os.makedirs(str(config_dir))

        auth_file = config_dir / 'auth'
        auth_file.unlink()

        auth_data = Auth(config_dir)
        auth_data.update({'user': 'test', 'password': 'test123'})
        auth_data.save(fail_silently=True)

        assert auth_file.exists()
        assert auth_file.stat().st_mode == 0o600
        assert auth_file.stat().st_uid == 0
    finally:
        shutil.rmtree(tempdir)

# Generated at 2022-06-13 21:29:50.564247
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    d = BaseConfigDict(path=Path('/tmp/test.json'))
    d.save()


# Generated at 2022-06-13 21:29:58.527965
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    test_dict = BaseConfigDict(get_default_config_dir() / Config.FILENAME)
    test_dict['answer'] = 42
    test_dict.save()
    new_test_dict = BaseConfigDict(get_default_config_dir() / Config.FILENAME)
    new_test_dict.load()
    assert new_test_dict['answer'] == test_dict['answer']

# Generated at 2022-06-13 21:30:08.197880
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import pytest

    @pytest.fixture
    def mock_ensure_directory(mocker):
        return mocker.patch.object(BaseConfigDict, 'ensure_directory')

    def test_writes_json(table, config_dir, mock_ensure_directory):
        mocked_table = dict(table)
        mocked_table.update({
            '__meta__': {
                'httpie': __version__
            }
        })
        config = BaseConfigDict(path=config_dir.joinpath('foo'))
        config.update(table)
        with config_dir.as_cwd():
            config.save()
        mock_ensure_directory.assert_called_once()
        with config_dir.joinpath('foo').open('rt') as f:
            contents = f.read()

# Generated at 2022-06-13 21:30:13.761684
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() / '.config' / 'httpie'


# Generated at 2022-06-13 21:30:26.338312
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    # The configurarion file is not existed
    config_dir = BaseConfigDict("./config_dir") # 创建一个不存在的配置文件
    config_dir.save() # 保存配置文件
    assert config_dir.path.exists() == True
    # The configurarion file is existed
    config_dir_1 = BaseConfigDict("./config_dir")
    config_dir_1.save()
    assert config_dir_1.path.exists() == True
    config_dir_1.delete()
    # Handle exception
    config_dir_2 = BaseConfigDict("/")

# Generated at 2022-06-13 21:30:38.280668
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Ensure that the legacy dir is used when it exists
    base = Path('/home/nobody')
    os.environ.pop(ENV_XDG_CONFIG_HOME, None)
    (base / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR).mkdir(mode=0o700, parents=True)
    assert get_default_config_dir() == base / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR

    # Ensure that the XDG dir is used when the legacy dir doesn't exist
    (base / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR).rmdir()
    assert get_default_config_dir() == \
        base / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME

    # Ensure that the XDG dir

# Generated at 2022-06-13 21:30:48.811855
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    from pathlib import Path
    import json
    import os
    import tempfile
    from httpie.config import BaseConfigDict
    tmp_dir = tempfile.gettempdir()
    config_test = BaseConfigDict(Path(tmp_dir+'/httpie_test.json'))
    config_test.load()
    assert [] == config_test
    data = {'content': 'test'}
    f = open(tmp_dir+'/httpie_test.json','w')
    json.dump(data,f)
    f.close()
    config_test.load()
    assert data == config_test
    data = {'content': 'test', 'meta': {'httpie': 'httpie-test'}}
    f = open(tmp_dir+'/httpie_test.json','w')
    json

# Generated at 2022-06-13 21:30:59.787446
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    from pathlib import Path
    
    config_dir = Path('~').expanduser() / '.httpie'
    config_dir.mkdir(exist_ok=True)
    config_file = config_dir / 'config.json'
    config_file.touch()

    config = Config(directory=config_dir)

    content = b'{"abc":"abc"}'
    config_file.write_bytes(content)

    try:
        config.load()
    except ConfigFileError as e:
        if isinstance(e, ValueError):
            pass
    else:
        raise Exception('should raise ValueError')



# Generated at 2022-06-13 21:31:00.850832
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    assert False



# Generated at 2022-06-13 21:31:06.662104
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    c = BaseConfigDict('httpie/test_run')
    c['hello'] = 'world'
    c.save()
    print(c['hello'])

# Generated at 2022-06-13 21:31:09.770510
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    test = BaseConfigDict("/Users/sundayy/httpie/httpie/config.json")
    test.load()



# Generated at 2022-06-13 21:31:14.136700
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    #For testing coverage we need to create some object
    config = ConfigFileError()
    #This method doesn't return anything
    config.save()


# Generated at 2022-06-13 21:31:16.033574
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert str(get_default_config_dir()) == str(Path.home() / '.config/httpie')



# Generated at 2022-06-13 21:31:17.940615
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    path = Path('test_file_path')
    dict = BaseConfigDict(path)
    dict.ensure_directory()

# Generated at 2022-06-13 21:31:26.773532
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    """
    test method save of class BaseConfigDict
    
    """
    class TestClass(BaseConfigDict):
        pass
    
    test_dir = Path('test_save')
    test_dir.mkdir(parents=True)
    filepath = test_dir / 'testfile'
    test_instance = TestClass(filepath)
    test_instance['a'] = 1

    test_instance.save()
    assert filepath.exists()

    test_dir.rmdir()



# Generated at 2022-06-13 21:31:41.760499
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config = BaseConfigDict(Path('config.json'))
    config.update({
        'first_name': 'Eric',
        'last_name': 'Idle',
        'language': 'English',
        'born': 1934,
    })

    config.save()
    config_str = Path('config.json').read_text()
    config_dict = json.loads(config_str)

    assert config_dict == {
        'first_name': 'Eric',
        'last_name': 'Idle',
        'language': 'English',
        'born': 1934,
    }


# Generated at 2022-06-13 21:31:45.632269
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    # create a new file and delete it
    test = BaseConfigDict('test.json')
    test.ensure_directory()
    test.save(fail_silently=True)
    test.delete()
    # test if load() works well with a non-exist file
    test.load()
    test.delete()

# Generated at 2022-06-13 21:31:55.724618
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    """
    Tests the function get_default_config_dir.

    """
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/config/dir'
    assert get_default_config_dir() == '/config/dir'
    os.environ[ENV_HTTPIE_CONFIG_DIR] = ''

    if is_windows:
        assert get_default_config_dir() == Path('%APPDATA%\\httpie')

    os.environ[ENV_XDG_CONFIG_HOME] = 'XDG_CONFIG_HOME'
    assert (get_default_config_dir() ==
            Path.home() / 'XDG_CONFIG_HOME/httpie')
    os.environ[ENV_XDG_CONFIG_HOME] = ''


# Generated at 2022-06-13 21:32:04.067003
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    CONFIG_DIR = Path(__file__).parent / 'test_dir'
    testdir = CONFIG_DIR / 'testdir'
    testdir.mkdir(mode=0o700, parents=True, exist_ok=True)
    testdir_file = CONFIG_DIR / 'testdir_file'
    testdir_file.write_text('test')
    testdir_file.chmod(0o777)
    try:
        base_config_dict = BaseConfigDict(testdir_file)
        base_config_dict.ensure_directory()
        assert testdir_file.parent.exists()
        assert testdir_file.is_file()
        assert testdir.is_dir()
        assert testdir.stat().st_mode & 0o700 == 0o700
    finally:
        testdir.rmd

# Generated at 2022-06-13 21:32:19.057741
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    class TestConfigDict(BaseConfigDict):
        pass

    import tempfile

    path = Path(tempfile.mkdtemp()) / 'test.json'
    path.parent.mkdir(parents=True)
    path.write_text('{"a": 1}')

    config_dict = TestConfigDict(path=path)
    config_dict.load()

    assert config_dict['a'] == 1
    path.unlink()
    path.parent.rmdir()

# Generated at 2022-06-13 21:32:27.027747
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() / Path('.config') / DEFAULT_CONFIG_DIRNAME

    original_env_xdg_config_home_value = os.environ.get(ENV_XDG_CONFIG_HOME)
    os.environ[ENV_XDG_CONFIG_HOME] = '/tmp'
    assert get_default_config_dir() == Path('/tmp') / DEFAULT_CONFIG_DIRNAME
    os.environ[ENV_XDG_CONFIG_HOME] = original_env_xdg_config_home_value

    original_env_httpie_config_dir_value = os.environ.get(ENV_HTTPIE_CONFIG_DIR)

# Generated at 2022-06-13 21:32:33.370670
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    class testBaseConfigDict(BaseConfigDict):
        name = None
        helpurl = None
        about = None
        
    path = Path('./test.json')
    
    Config = testBaseConfigDict(path)
    try:
        Config.load()
        assert True
    except:
        assert False
    #Delete the current test file
    try:
        path.unlink()
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise


# Generated at 2022-06-13 21:32:47.302813
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import unittest
    import os
    import shutil
    from pathlib import Path

    class GetDefaultConfigDirTest(unittest.TestCase):
        """Tests for get_default_config_dir()."""

        def setUp(self):
            self.home = os.environ['HOME'] = os.path.abspath('.home')
            self.root = os.path.abspath('root')
            self.subdir = os.path.join(self.home, '.config/subdir')
            for d in (self.root, self.subdir):
                os.mkdir(d)

        def tearDown(self):
            shutil.rmtree(self.home)


# Generated at 2022-06-13 21:32:50.852424
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    path = os.environ.get(ENV_HTTPIE_CONFIG_DIR, get_default_config_dir() / 'test' / 'test.json')
    baseConfigDict = BaseConfigDict(path)

# Generated at 2022-06-13 21:32:56.572362
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # Check that ensure directory work on path that exist and have mode 700
    path = Path('/tmp/.config/httpie')
    path.mkdir(mode=0o700, parents=True)
    test_config = BaseConfigDict(path=path)
    test_config.ensure_directory()

# Generated at 2022-06-13 21:33:03.829644
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config_dir = Path('/tmp/test_httpie')
    path = config_dir / Config.FILENAME
    if path.exists():
        path.unlink()

    class TestConfig(BaseConfigDict):
        name = 'test'

    config = TestConfig(path)
    config['test'] = 'test'
    config.save()

    assert (path.read_text().strip() == '''{
        "__meta__": {
            "httpie": "1.0dev"
        },
        "test": "test"
    }'''.strip())


# Generated at 2022-06-13 21:33:14.409453
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    global DEFAULT_CONFIG_DIR
    DEFAULT_CONFIG_DIR = Path('/tmp/httpie')

    global DEFAULT_CONFIG_DIRNAME
    DEFAULT_CONFIG_DIRNAME = 'httpie'

    if DEFAULT_CONFIG_DIR.exists():
        DEFAULT_CONFIG_DIR.unlink()

    c = Config()
    assert(c.is_new())

    c.save()
    assert(c.path.exists())

    with open(c.path, 'wt') as f:
        f.write('invalid json')

    with pytest.raises(ConfigFileError):
        c.load()



# Generated at 2022-06-13 21:33:21.631973
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # with $XDG_CONFIG_HOME
    input_ = {
        'XDG_CONFIG_HOME': '/a/b/c'
    }
    expected_output = '/a/b/c/httpie'
    with patch.dict('os.environ', input_, clear=True):
        output = get_default_config_dir()
    assert output == expected_output

    # with $XDG_CONFIG_HOME and $HTTPIE_CONFIG_DIR
    input_ = {
        'XDG_CONFIG_HOME': '/a/b/c',
        'HTTPIE_CONFIG_DIR': '/a/b/c/d'
    }
    expected_output = '/a/b/c/d'

# Generated at 2022-06-13 21:33:35.225433
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    def make_xdg_config_home(val):
        return {ENV_XDG_CONFIG_HOME: val}

    def make_httpie_config_dir(val):
        return {ENV_HTTPIE_CONFIG_DIR: val}

    def check(expected, *args, **kwargs):
        assert get_default_config_dir() == Path(expected), \
            (expected, args, kwargs)

    def check_xdg(expected, *args, **kwargs):
        check(expected, *args, **kwargs, **make_xdg_config_home('/xdg'))

    check_xdg('/xdg/httpie')

    if is_windows:
        check(DEFAULT_WINDOWS_CONFIG_DIR)

# Generated at 2022-06-13 21:33:52.492938
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config = get_default_config_dir()
    path = config / "config.json"

    f = open(str(path), 'w+')
    f.write("{'f': 'test'}")
    f.close()

    c = Config(get_default_config_dir())
    c.load()
    assert c['f'] == "test"
    os.remove(str(path))

# Generated at 2022-06-13 21:33:57.130491
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    class TestConfig(BaseConfigDict):
        def __init__(self):
            super().__init__(os.path.expanduser('~/test_config_dir'))
    t = TestConfig()
    t.ensure_directory()
    assert os.path.exists(t.path.parent)

# Generated at 2022-06-13 21:34:01.130792
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    class DemoConfigDict(BaseConfigDict):
        pass
    c = DemoConfigDict(
        path = Path.cwd() / 'temp.json'
    )
    c.ensure_directory()
    with open("temp.json", "w") as f:
        f.write("{}")


# Generated at 2022-06-13 21:34:03.949011
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert DEFAULT_CONFIG_DIR.expanduser().as_posix() == os.path.join(Path.home(), '.config/httpie')

# Generated at 2022-06-13 21:34:16.229388
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    def get_config_dict(filename):
        class ConfigDict(BaseConfigDict):
            pass
        return ConfigDict(filename)

    c = get_config_dict(Path('testdata/c.json'))
    c.load()
    assert c == {'a': 1, 'b': 'c'}

    c = get_config_dict(Path('testdata/nonexistent_c.json'))
    c.load()
    assert c == {}

    c = get_config_dict(Path('testdata/invalid_c.json'))
    try:
        c.load()
    except ConfigFileError as e:
        assert str(e) == 'invalid configdict file: Expecting value: line 1 column 1 (char 0) [testdata/invalid_c.json]'


# Unit test

# Generated at 2022-06-13 21:34:19.571825
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config = BaseConfigDict(Path('./httpie/test.json'))
    config.ensure_directory()
    assert os.path.exists('./httpie')
    os.rmdir('./httpie')

# Generated at 2022-06-13 21:34:24.088476
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    func = get_default_config_dir
    if is_windows:
        assert func() == Path('C:\\Users\\nullbyte\\AppData\\Roaming\\httpie')
    elif os.environ.get(ENV_XDG_CONFIG_HOME):
        assert (func()
                == Path('/home/nullbyte/.config/httpie'))
    else:
        assert func() == Path('/home/nullbyte/.config/httpie')

# Generated at 2022-06-13 21:34:35.515755
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    if os.path.isdir("c:\\Users\\mahui\\.httpie"):
        # there is a folder ".httpie" in "c:\Users\mahui"
        filename = "c:\\Users\\mahui\\.httpie\\config.json"
        # load the file
        config = Config(filename)
        config.load()
        assert config['__meta__']['httpie'] == "1.0.3"
        assert config['__meta__']['help'] == "https://httpie.org/"
        assert config['__meta__']['about'] == "HTTPie %(version)s, a cURL-like, " \
                                             "user-friendly command line HTTP client."
        assert config['default_options'] == []


# Generated at 2022-06-13 21:34:40.927154
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() / Path('.config/httpie')
    assert os.environ['XDG_CONFIG_HOME'] == '/home/httpie/.config'
    assert get_default_config_dir() == Path('/home/httpie/.config/httpie')

# Generated at 2022-06-13 21:34:46.809843
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    test_dict = {'a':1}
    tmp_path = Path('/tmp')
    with open(tmp_path / 'config', 'w') as f:
        json.dump(test_dict, f)
    base_config_dict = BaseConfigDict(tmp_path / 'config')
    base_config_dict.load()
    assert base_config_dict == test_dict

# Generated at 2022-06-13 21:35:06.649369
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    from tempfile import TemporaryDirectory
    from pathlib import Path
    with TemporaryDirectory() as td:
        p = Path(td) / '777' / '888' / '999'
        c = BaseConfigDict(p)
        c.ensure_directory()
        assert p.parent.exists()
        assert p.parent.is_dir()
        assert p.parent == Path(td) / '777' / '888'


# Generated at 2022-06-13 21:35:08.914087
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config = BaseConfigDict(Path(DEFAULT_CONFIG_DIR))
    config.ensure_directory()
    assert config.path.parent.exists()



# Generated at 2022-06-13 21:35:20.077883
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():

    def test_create_dir(dirpath):
        try:
            os.mkdir(dirpath)
        except OSError:
            pass
        assert os.path.isdir(dirpath)

    def test_remove_dir(dirpath):
        os.chmod(dirpath, 0o700)
        try:
            os.rmdir(dirpath)
        except OSError:
            pass
        assert not os.path.exists(dirpath)

    config_dict = BaseConfigDict(Path('~/.config/not_exist_directory/config.json'))
    config_dict.ensure_directory()
    assert os.path.isdir(config_dict.path.parent)

    test_create_dir(Path('~/ensure_directory_test/'))

# Generated at 2022-06-13 21:35:28.362300
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    test_config_dir = Path('/tmp/httpie/test_config')
    config_file_name = 'config.json'
    config_file_path = test_config_dir / config_file_name

    if not os.path.exists(test_config_dir):
        os.makedirs(test_config_dir)

    if config_file_path.exists():
        os.remove(config_file_path)

    cfg = BaseConfigDict(config_file_path)
    cfg.save()

    assert config_file_path.exists()

    os.remove(config_file_path)

    if os.path.exists(test_config_dir):
        os.removedirs(test_config_dir)


# Generated at 2022-06-13 21:35:36.257376
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    try:
        os.mkdir('./config-test')
    except:
        pass

    config = BaseConfigDict(path='./config-test/test-config.json')
    config.save(fail_silently=True) # save
    config.load()
    config.save(fail_silently=True) # save
    config.save(fail_silently=True) # save

    config.load()
    config['a'] = 2
    config.save(fail_silently=True)

    config.delete()
    config.delete()

# Generated at 2022-06-13 21:35:44.025292
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config = Config()
    config['new_option'] = 'value'
    config.save()
    print(config.path)
    with config.path.open() as file:
        file_content = file.read()
        assert '"new_option": "value"' in file_content
        assert '"httpie": "0.9.9"' in file_content
        assert '"help": "https://httpie.org/doc#config"' in file_content
        assert '"about": "https://httpie.org/about"' in file_content


if __name__ == '__main__':
    test_BaseConfigDict_save()

# Generated at 2022-06-13 21:35:45.008918
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() is not None

# Generated at 2022-06-13 21:35:53.546367
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # with regard to legacy ~/.httpie
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    os.environ.pop(ENV_XDG_CONFIG_HOME, None)

    Path(Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR).mkdir()
    try:
        assert get_default_config_dir() == Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    finally:
        Path(Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR).rmdir()

    # with regard to $XDG_CONFIG_HOME
    os.environ[ENV_XDG_CONFIG_HOME] = '/foo/xdg/config/home'

# Generated at 2022-06-13 21:35:57.319118
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    default_config_dir = get_default_config_dir().absolute()
    assert (default_config_dir == DEFAULT_CONFIG_DIR)



# Generated at 2022-06-13 21:35:59.146719
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    d = Path('~/.config/httpie_test_ensure_directory')
    t = BaseConfigDict(d)
    t.ensure_directory()
    assert d.parent.exists()
    d.parent.rmdir()



# Generated at 2022-06-13 21:36:31.120045
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() / '.config' / 'httpie'

    assert os.environ.get(ENV_HTTPIE_CONFIG_DIR) is None
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/usr/share/httpie'
    assert get_default_config_dir() == Path('/usr/share/httpie')



# Generated at 2022-06-13 21:36:35.297577
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    try:
        (DEFAULT_CONFIG_DIR / 'config.json').unlink(missing_ok=True)
    except OSError as e:
        if e.errno != errno.ENOENT:
            raise

    config = Config()

    # Unload config file
    assert config.is_new()

    # Load config file
    config.save()

    assert not config.is_new()

# Generated at 2022-06-13 21:36:46.024289
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Test when $XDG_CONFIG_HOME is set
    class Env:
        pass
    env = Env()
    env.old = os.environ.get(ENV_XDG_CONFIG_HOME, '')
    os.environ[ENV_XDG_CONFIG_HOME] = '/tmp'
    assert get_default_config_dir() == Path('/tmp') / DEFAULT_CONFIG_DIRNAME
    os.environ[ENV_XDG_CONFIG_HOME] = env.old
    assert get_default_config_dir() != Path('/tmp') / DEFAULT_CONFIG_DIRNAME

    # Test when OS is Windows
    class OS:
        pass
    os = OS()
    os.name = 'nt'

# Generated at 2022-06-13 21:36:51.417224
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    if os.path.exists('test.json'):
        os.remove('test.json')
    config = BaseConfigDict('test.json')
    config['hello'] = 'world'
    config.save()
    assert os.path.exists('test.json')
    if os.path.exists('test.json'):
        os.remove('test.json')

# Generated at 2022-06-13 21:37:05.101299
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # When running the httpie command, both of these are empty
    assert os.getenv('HTTPIE_CONFIG_DIR') is None
    assert os.getenv('XDG_CONFIG_HOME') is None

    # TODO: test on a POSIX-compliant system
    if is_windows:
        # Windows should always fall-back to the default location
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # When performing a unit-test, the CWD is changed to the httpie
    # package directory. This means that the default directories
    # (and everything under it) will be considered to be under the
    # project's root directory (which is a useless location for
    # configurations)
    assert get_default_config_dir() == Path.cwd() / DEFAULT_CONFIG_DIRNAME

# Generated at 2022-06-13 21:37:18.029138
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    from mock import patch
    from httpie.config import DEFAULT_CONFIG_DIRNAME, DEFAULT_WINDOWS_CONFIG_DIR
    from httpie.config import ENV_HTTPIE_CONFIG_DIR, ENV_XDG_CONFIG_HOME
    from httpie.config import DEFAULT_RELATIVE_XDG_CONFIG_HOME
    from httpie.config import DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    from httpie.compat import is_windows

    # 1. explicitly set through env
    with patch.dict('os.environ', {}, clear=True):
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR


# Generated at 2022-06-13 21:37:23.450736
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config = BaseConfigDict(Path('./test_config.json'))
    config.load()
    assert config['test_key'] == 'test_value'
    assert config['test_key1'] == 'test_value1'


# Generated at 2022-06-13 21:37:32.809623
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    conf = BaseConfigDict(path=DEFAULT_CONFIG_DIR)
    conf['content'] = [1,2,3]
    conf.save()
    with open(DEFAULT_CONFIG_DIR.parent / "test_bc.json", "r") as read_file:
        data = json.load(read_file)
        #assert data == {'content': [1, 2, 3], '__meta__': {'httpie': __version__}}
        assert data['content'] == [1, 2, 3]


# Unit testing for method delete of class BaseConfigDict

# Generated at 2022-06-13 21:37:40.032814
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    # Create a configuration directory
    test_directory = Path('.tmp/test/')
    test_directory.mkdir(parents=True, exist_ok=True)

    # Create a BaseConfigDict object
    test_config_dict = BaseConfigDict(test_directory / 'config.json')
    # Save the BaseConfigDict object to the configuration directory
    test_config_dict.save()
    # Check if the saved file contains the information
    assert "httpie" in test_config_dict.path.read_text()
    # Delete the created file
    test_config_dict.path.unlink()
    test_directory.rmdir()

# Generated at 2022-06-13 21:37:50.458247
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # basic functionality
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR
    # xdg is ignored on windows
    with httpie.environment.Environment(**{ENV_XDG_CONFIG_HOME: '/xdg'}):
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
    # xdg is configured
    with httpie.environment.Environment(**{ENV_XDG_CONFIG_HOME: '/xdg'}):
        assert get_default_config_dir() == Path('/xdg') / DEFAULT_CONFIG_DIRNAME
    # xdg is configured, but empty

# Generated at 2022-06-13 21:38:36.189667
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME


if __name__ == '__main__':
    test_get_default_config_dir()

# Generated at 2022-06-13 21:38:39.979920
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    assert BaseConfigDict(Path('test')).path == Path('test')

# test for method save of class BaseConfigDict

# Generated at 2022-06-13 21:38:42.869277
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert DEFAULT_CONFIG_DIRNAME in get_default_config_dir().as_posix()

# Generated at 2022-06-13 21:38:53.684563
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    from httpie.config import get_default_config_dir
    from os import unsetenv, mkdir
    from os.path import expanduser
    from shutil import rmtree
    from tempfile import TemporaryDirectory
    with TemporaryDirectory() as tmp:
        tests = [
            (None, tmp),
            ("", tmp),
            ("/var/tmp", Path('/var/tmp')),
            (Path(tmp, 'test'), Path(tmp, 'test')),
            ]
        for env, exp in tests:
            try:
                unsetenv('HTTPIE_CONFIG_DIR')
            except ValueError:
                pass
            if env:
                os.environ['HTTPIE_CONFIG_DIR'] = env

# Generated at 2022-06-13 21:38:56.553396
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    BaseConfigDict_test = BaseConfigDict('path')
    BaseConfigDict_test.save(fail_silently=True)
    pass


# Generated at 2022-06-13 21:39:04.848722
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config = BaseConfigDict(Path('/a/b/c'))
    config.path=Path('/a/b/c/config.json')
    config.update({"key":"Test"})
    config.save()
    with open('/a/b/c/config.json') as json_file:
        data = json.load(json_file)
        assert data['key'] == "Test"
        os.remove('/a/b/c/config.json')

# Generated at 2022-06-13 21:39:16.025348
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    try:
        pwd = os.getcwd()
        # Case 1: Set config directory through env
        os.environ[ENV_HTTPIE_CONFIG_DIR] = os.getcwd()
        assert DEFAULT_CONFIG_DIR == pwd
    finally:
        del os.environ[ENV_HTTPIE_CONFIG_DIR]

    try:
        # Case 2: Run on Windows
        is_windows_previous = is_windows
        is_windows = True
        assert DEFAULT_CONFIG_DIR == DEFAULT_WINDOWS_CONFIG_DIR
    finally:
        is_windows = is_windows_previous

    if is_windows:
        return


# Generated at 2022-06-13 21:39:17.184746
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:39:18.547595
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    c = Config()
    assert c.load() == None

# Generated at 2022-06-13 21:39:19.239610
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    assert 1