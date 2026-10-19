

# Generated at 2022-06-13 21:30:00.684693
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    # patch sys.platform to test Windows
    from unittest.mock import patch
    from contextlib import contextmanager

    @contextmanager
    def win_mock():
        with patch('httpie.config.is_windows', True):
            yield

    with win_mock():
        config = BaseConfigDict(path='a')
        path = config.path
        assert path == DEFAULT_WINDOWS_CONFIG_DIR / 'a'
        with patch('httpie.config.DEFAULT_WINDOWS_CONFIG_DIR', 'b'):
            config = BaseConfigDict(path='a')
            path = config.path
            assert path == Path('b') / 'a'


# Generated at 2022-06-13 21:30:09.453111
# Unit test for function get_default_config_dir
def test_get_default_config_dir():

    def get_default_config_dir_env_override(
            config_home: str,
            config_dirs: str,
            cwd: str) -> Path:
        saved_env = {
            'XDG_CONFIG_HOME': os.environ.get('XDG_CONFIG_HOME'),
            'XDG_CONFIG_DIRS': os.environ.get('XDG_CONFIG_DIRS'),
            'PWD': os.environ.get('PWD'),
        }

# Generated at 2022-06-13 21:30:15.634558
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

# Run this one by one.
# In function test_get_default_config_dir(),
# when one of the assert fails, the following ones won't run.
# Test the function get_default_config_dir()
# def test_get_default_config_dir():
#     assert get_default_config_dir() == DEFAULT_CONFIG_DIR
#
#     # Explicitly set through env
#     os.environ['HTTPIE_CONFIG_DIR'] = '/tmp/httpie'
#     assert get_default_config_dir() == Path('/tmp/httpie')
#     del os.environ['HTTPIE_CONFIG_DIR']
#
#     # Explicity set through env, but empty
#     os.environ['HTTPIE

# Generated at 2022-06-13 21:30:21.911961
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Windows
    if is_windows:
        assert str(get_default_config_dir()) == 'C:\\Users\\Administrator\\AppData\\Roaming\\httpie'

    # Linux
    else:
        assert str(get_default_config_dir()) == '/home/lee/.config/httpie'

# Generated at 2022-06-13 21:30:27.359629
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    # test loading from non existent file
    try:
        test_conf = BaseConfigDict(path=Path('/tmp/test_config'))
        test_conf.load()
        assert False
    except ConfigFileError as e:
        assert str(e) == 'cannot read baseconfigdict file: [Errno 2] No such file or directory: \'/tmp/test_config\''

    # create empty file
    with open('/tmp/test_config', 'a'):
        os.utime('/tmp/test_config', None)
    test_conf = BaseConfigDict(path=Path('/tmp/test_config'))

    # test loading from empty file

# Generated at 2022-06-13 21:30:35.598065
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import os
    import tempfile

    # Test for windows
    if os.name == 'nt':
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
    else:
        # Test for Linux, MacOS and others
        path = tempfile.mkdtemp()
        # Test for environment variable HTTPIE_CONFIG_DIR
        os.environ[ENV_HTTPIE_CONFIG_DIR] = path
        assert get_default_config_dir() == Path(path)

        # Test for legacy config file
        path = tempfile.mkdtemp()

        legacy_config_dir = Path(path) / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
        legacy_config_dir.mkdir()

        with legacy_config_dir.open(mode='w'):
            pass

       

# Generated at 2022-06-13 21:30:44.171977
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    directory = Path(Path.home(), '.config', 'httpie')
    filename = 'config.json'
    try:
        directory.mkdir(mode=0o700, parents=True)
    except OSError as e:
        if e.errno == errno.EEXIST and directory.exists():
            pass
        else:
            raise
    path = Path(directory, filename)
    config = Config(directory)
    assert 'default_options' in config
    assert not config.is_new() 
    assert path.exists()
    config['default_options'] = ['--start=test']
    config.save()
    config['default_options'] = ''
    config.load()
    assert 'default_options' in config
    assert config['default_options'] == ['--start=test']
    config

# Generated at 2022-06-13 21:30:47.585863
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # test for case that directory is not exist
    path = Path('./non-exist-directory/abc')
    config = BaseConfigDict(path)
    config.ensure_directory()
    assert path.parent.exists(), "should create parent directory"

# Generated at 2022-06-13 21:30:50.982974
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    config_dir = Path(get_default_config_dir())
    assert config_dir.exists()

# Generated at 2022-06-13 21:31:01.413620
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config_dir = Path.home() / Path('.test_httpie')
    config_dir.mkdir(mode=0o700, parents=True)
    test_f=config_dir / Path('test_file.txt')
    assert test_f.parent.is_dir() ==True
    assert test_f.exists() == False
    test_f.write_text('test')
    assert test_f.exists() == True
    test_f.unlink()
    test_f.parent.rmdir()
    assert test_f.exists() == False
    assert test_f.parent.is_dir() == False


# Generated at 2022-06-13 21:31:16.927245
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # 1. Using default config directory
    expected_default_config_dir = str(Path.home()) + '/.config/httpie'
    assert get_default_config_dir() == Path(expected_default_config_dir)

    # 2. Using Legacy config directory
    # Setting Env variable XDG_CONFIG_HOME
    home = str(Path.home())
    os.environ[ENV_XDG_CONFIG_HOME] = home
    assert get_default_config_dir() == Path(home + '/httpie')

    # 3. Remove Environment Variable XDG_CONFIG_HOME
    os.environ.pop(ENV_XDG_CONFIG_HOME)
    assert get_default_config_dir() == Path(expected_default_config_dir)

    # 4. Setting Environment Variable HTTPIE_CONFIG

# Generated at 2022-06-13 21:31:27.657962
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    """
    Testing the save method of BaseConfigDict
    """
    import tempfile
    temp_dir = tempfile.gettempdir()
    config = Config(directory = temp_dir)
    config.save()
    try:
        with open(config.path, 'r') as json_file:
            assert(json.loads(json_file.read()) == {'__meta__': {'httpie': __version__}, 'default_options': []})
    finally:
        os.unlink(config.path)

# Generated at 2022-06-13 21:31:41.024567
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # configuration file path
    test_config_path = 'test_config_path'

    # create a class instance, the file does not exist yet
    config_dict = BaseConfigDict(Path(test_config_path))

    # the file does not exist
    assert not os.path.exists(test_config_path)

    # call ensure_directory()
    config_dict.ensure_directory()

    # the file exists
    assert os.path.exists(test_config_path)


# Generated at 2022-06-13 21:31:48.543473
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # 1: explicitly set through env
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '~/.xyz'
    assert get_default_config_dir() == Path.home() / '.xyz'
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # 2: legacy ~/.httpie
    legacy = Path.home() / '.httpie'
    legacy.mkdir()
    assert get_default_config_dir() == legacy
    legacy.rmdir()

    # 3: XDG
    xdg_config_home = Path.home() / '.config'

# Generated at 2022-06-13 21:31:59.343059
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class FakeBaseConfigDict(BaseConfigDict):
        pass

    # case 1: normal case
    config_dict = FakeBaseConfigDict(Path('/dev/null'))
    config_dict.save(fail_silently=True)

    # case 2: fail to write to file
    config_dict = FakeBaseConfigDict(Path('/dev/full'))
    try:
        config_dict.save()
        assert False, 'Expected ConfigFileError exception'
    except ConfigFileError:
        pass
    except Exception as e:
        assert False, f'Expected ConfigFileError exception, not {type(e)}'



# Generated at 2022-06-13 21:32:05.756645
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    my_path = Path('/tmp/fake_httpie_dir/config.json')
    my_obj = BaseConfigDict(path = my_path)
    my_obj.ensure_directory()
    assert my_path.parent.is_dir()
    assert my_path.parent.exists()


# Generated at 2022-06-13 21:32:11.266326
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    path = Path('./test/test_config_dir/config.json')
    test_config_dict = BaseConfigDict(path)
    if os.path.exists(path.parent):
        shutil.rmtree(path.parent)
    test_config_dict.ensure_directory()
    assert os.path.exists(path.parent)


# Generated at 2022-06-13 21:32:23.638408
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    """
    test function
    """
    if not os.path.exists('test_dir'):
        os.makedirs('test_dir')
        test_file = open('test_dir/test.json', 'w')
        test_file.close()
    test_cfg = BaseConfigDict(path='test_dir/test.json')
    if not os.path.exists('test_dir/test_dir2'):
        os.makedirs('test_dir/test_dir2')
    test_cfg.path = Path('test_dir/test_dir2/test.json')
    test_cfg.ensure_directory()
    if not os.path.exists('test_dir/test_dir2'):
        print('test fail')
    else:
        print('test success')
    shut

# Generated at 2022-06-13 21:32:34.838619
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    tmp_dir = Path('/tmp/httpie/test_BaseConfigDict_ensure_directory')
    tmp_dir.mkdir(mode=0o700, parents=True, exist_ok=True)
    tmp_dir.chmod(0o700)
    config = BaseConfigDict(path=tmp_dir / 'test.json')
    config.ensure_directory()
    assert os.stat(str(tmp_dir)).st_mode == 0o700



# Generated at 2022-06-13 21:32:40.021582
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    path = Path('test-save')
    assert not path.exists()

    class TestClass(BaseConfigDict):
        def __init__(self):
            super().__init__(path=path)

    test = TestClass()
    test['key'] = 'value'
    test.save()

    assert path.exists()
    assert path.read_text() == '{\n    "key": "value"\n}\n'

    path.unlink()



# Generated at 2022-06-13 21:32:49.829771
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    try:
        base_config = BaseConfigDict('./test.json')
        base_config.save()
    except Exception as e:
        assert False
    assert os.path.exists('./test.json')
    

# Generated at 2022-06-13 21:32:52.134794
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:33:02.881773
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    xdg_config_home = Path('/foo/bar')
    home_dir = Path('/baz')
    legacy_config_dir = home_dir / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    os.environ[ENV_XDG_CONFIG_HOME] = str(xdg_config_home)
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/qux'
    assert get_default_config_dir() == Path('/qux')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]
    assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
    assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

# Generated at 2022-06-13 21:33:06.193265
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() / '.config' / 'httpie'

# Generated at 2022-06-13 21:33:10.788229
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    file_path = Path(__file__).parent.joinpath('.env.production')
    env_config = BaseConfigDict(file_path)
    env_config.load()
    assert type(env_config) == dict
    return True


# Generated at 2022-06-13 21:33:20.161818
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    from httpie.config import DEFAULT_WINDOWS_CONFIG_DIR, get_default_config_dir

    # $XDG_CONFIG_DIR/httpie
    os.environ[ENV_XDG_CONFIG_HOME] = '/foo'
    assert get_default_config_dir() == Path('/foo') / DEFAULT_CONFIG_DIRNAME

    # .config/httpie
    del os.environ[ENV_HTTPIE_CONFIG_DIR]
    del os.environ[ENV_XDG_CONFIG_HOME]
    os.environ['HOME'] = '/bar'
    assert get_default_config_dir() == Path('/bar/.config') / DEFAULT_CONFIG_DIRNAME

    # %APPDATA%\httpie
    del os.environ['HOME']
   

# Generated at 2022-06-13 21:33:25.338446
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    path = Path(os.getcwd()) / 'abc'
    test = BaseConfigDict(path)
    if not test.path.exists():
        test.ensure_directory()
        assert test.path.exists(), "test ensure_directory failed"

# Generated at 2022-06-13 21:33:34.721203
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    """
    Write a file and check its content.
    """
    class DummyDict(BaseConfigDict):
        pass
    
    d = DummyDict(Path('tmp/dummy.json'))
    d.save()
    new_content = Path('tmp/dummy.json').read_text()
    expected_content = """\
{
    "__meta__": {
        "httpie": "1.0.3"
    }
}
"""
    assert new_content == expected_content


# Generated at 2022-06-13 21:33:42.156677
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() / '.config' / 'httpie'
    assert get_default_config_dir() != Path.home() / '.config'
    assert get_default_config_dir() != Path.home() / '.httpie'
    assert get_default_config_dir() != Path(os.path.expandvars('%APPDATA%')) / DEFAULT_CONFIG_DIRNAME

    os.environ[ENV_HTTPIE_CONFIG_DIR] = \
        Path.home() / '.config' / 'httpie'

    assert get_default_config_dir() == Path.home() / '.config' / 'httpie'
    assert get_default_config_dir() != Path.home() / '.config'
    assert get_default_config_dir() != Path.home

# Generated at 2022-06-13 21:33:54.895608
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    from config import BaseConfigDict
    from pathlib import Path
    from tempfile import NamedTemporaryFile
    import json

    my_dict = BaseConfigDict(Path(NamedTemporaryFile().name))
    my_dict.save()
    with my_dict.path.open(mode='r') as f:
        a = json.loads(f.read())
        assert a['__meta__']['httpie'] == __version__
        assert a['__meta__']['help'] == None
        assert a['__meta__']['about'] == None
        assert a == {"__meta__": {"httpie": "2.0.9", "help": None, "about": None}}

# Generated at 2022-06-13 21:34:15.840079
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class Foo(BaseConfigDict):
        name = 'foo'
        helpurl = 'https://foo.com/'
        about = 'The Foo'

    try:
        os.remove('/tmp/config.json')
    except:
        pass

    foo = Foo('/tmp/config.json')
    foo.save()

    with open('/tmp/config.json', 'r') as json_file:
        d = json.load(json_file)
        assert d['__meta__']['about'] == 'The Foo'
        assert d['__meta__']['help'] == 'https://foo.com/'


# Generated at 2022-06-13 21:34:24.447809
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # 1. explicitly set through env
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/some/dir'
    assert get_default_config_dir() == Path('/some/dir')
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR)

    # 2. Windows
    assert get_default_config_dir() == Path(
        os.path.expandvars('%APPDATA%')) / DEFAULT_CONFIG_DIRNAME

    # 3. legacy ~/.httpie
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir()
    assert get_default_config_dir() == legacy_config_dir
    legacy_config_dir.rmdir()

    # 4.

# Generated at 2022-06-13 21:34:35.710061
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

    Path.home().mkdir(mode=0o700)


# Generated at 2022-06-13 21:34:45.975086
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # Test directory that can't be created
    test_dir = Path.home() / 'config_test_no_permission'
    test_obj = BaseConfigDict(test_dir / 'test.json')

    # Check that BaseConfigDict raises OSError when directory can't be created
    with pytest.raises(OSError):
        test_obj.ensure_directory()

    # Test directory that's not empty
    test_dir = Path.home() / 'config_test_not_empty'
    (test_dir / 'test').touch()
    test_obj = BaseConfigDict(test_dir / 'test.json')

    # Check that BaseConfigDict raises OSError when directory can't be created
    with pytest.raises(OSError):
        test_obj.ensure_directory()

   

# Generated at 2022-06-13 21:34:57.420206
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    BASE_DIR = Path('/tmp')

    # if xdg_config_dir is not exists, it will auto created.
    xdg_config_dir = BASE_DIR / DEFAULT_CONFIG_DIRNAME
    xdg_config_dir.unlink(missing_ok=True)
    xdg_config_dir_config_file = xdg_config_dir / Config.FILENAME
    xdg_config_dir_config_file.unlink(missing_ok=True)

    assert xdg_config_dir.exists() == False
    assert xdg_config_dir_config_file.exists() == False

    xdg_conf_dict = BaseConfigDict(xdg_config_dir_config_file)
    xdg_conf_dict.ensure_directory()



# Generated at 2022-06-13 21:35:08.010476
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    # save data into file
    data = {'test1': 1, 'test2': '2'}
    test_file = Path.home() / 'deleteme.json'
    json_string = json.dumps(
        obj=data,
        indent=4,
        sort_keys=True,
        ensure_ascii=True,
    )
    test_file.write_text(json_string + '\n')
    # load data and compare
    cfd = BaseConfigDict(test_file)
    cfd.load()
    assert data == cfd
    test_file.unlink()

# Generated at 2022-06-13 21:35:13.680564
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path(
        os.path.expanduser('~/.config/httpie'))


os.environ['XDG_CONFIG_HOME'] = '/tmp/' + ENV_XDG_CONFIG_HOME

# Generated at 2022-06-13 21:35:25.294451
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    import os
    import traceback
    import tempfile

# Generated at 2022-06-13 21:35:36.297369
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    try:
        os.environ[ENV_HTTPIE_CONFIG_DIR] = '/foo/bar'
        assert get_default_config_dir() == Path('/foo/bar')
    finally:
        del os.environ[ENV_HTTPIE_CONFIG_DIR]

    assert get_default_config_dir() == Path.home() / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME

    try:
        os.environ[ENV_XDG_CONFIG_HOME] = '/foo/baz'
        assert get_default_config_dir() == Path('/foo/baz') / DEFAULT_CONFIG_DIRNAME
    finally:
        del os.environ[ENV_XDG_CONFIG_HOME]



# Generated at 2022-06-13 21:35:41.227537
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class TestConfigDict(BaseConfigDict):
        pass
    config = TestConfigDict(path='test.json')
    config.save()
    config['a'] = 1
    config['b'] = 2
    try:
        config.save(fail_silently=True)
    except:
        pass
    config.delete()
    try:
        config.save()
    except:
        pass


# Generated at 2022-06-13 21:36:06.042965
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config = Config()
    config.load()
    config.save()

    assert config['__meta__']['httpie'] == __version__



# Generated at 2022-06-13 21:36:16.917000
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # XDG
    os.environ['XDG_CONFIG_HOME'] = "/tmp/.config"
    assert get_default_config_dir() == Path("/tmp/.config/httpie")

    # Windows
    os.environ['APPDATA'] = "/tmp/"
    assert get_default_config_dir() == Path("/tmp/httpie")

    # Legacy
    os.environ['APPDATA'] = "/tmp"
    assert get_default_config_dir() == Path("/tmp/.httpie")

    # Explicit
    os.environ['XDG_CONFIG_HOME'] = ""
    os.environ['APPDATA'] = ""
    os.environ['HTTPIE_CONFIG_DIR'] = '/tmp/httpie_config'

# Generated at 2022-06-13 21:36:29.636268
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    # For BaseConfigDict, the function save will save the information of a
    # class to a file
    class TestBaseConfigDict(BaseConfigDict):
        def __init__(self, path: Path):
            self.name = 'test'
            self.helpurl = 'testurl'
            self.about = 'testabout'
            super().__init__(path)

    dir_path = Path('./')
    path = dir_path / 'testfile'
    testobj = TestBaseConfigDict(path)
    testobj.save()

    testobj['dict'] = 'dictionary'
    testobj.save()

    file_content = path.read_text()
    assert file_content is not ''
    file_dict = json.loads(file_content)
    assert 'dict' in file_dict



# Generated at 2022-06-13 21:36:44.538992
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    """
    Assert that the config directory is found under the expected paths
    """

    dirs_dict = {
        ENV_HTTPIE_CONFIG_DIR: [
            'path/to/dir',
        ],
        ENV_XDG_CONFIG_HOME: [
            'XDG_CONFIG/config_dir',
            'XDG_CONFIG/dir/config_dir',
            Path('.config/config_dir'),
            Path('.config/dir/config_dir'),
        ],
        '__default': [
            Path('path/.config/config_dir'),
            Path('path/.config/dir/config_dir'),
            Path('.httpie'),
        ],
    }

    # Check each xdg config dir override

# Generated at 2022-06-13 21:36:53.591484
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    def get_default_config_dir():
        return Path('./test_config')

    DEFAULT_CONFIG_DIR = get_default_config_dir()
    config = Config(directory=DEFAULT_CONFIG_DIR)
    assert not os.path.exists('./test_config')
    config['default_options'] = []
    assert os.path.exists('./test_config')
    os.rmdir('./test_config')


if __name__ == '__main__':
    test_BaseConfigDict_ensure_directory()
    print('pass')

# Generated at 2022-06-13 21:37:01.427041
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Check if ~/.httpie directory is created
    assert DEFAULT_WINDOWS_CONFIG_DIR.exists()

    # Check if $XDG_CONFIG_HOME/httpie directory is created
    os.environ[ENV_XDG_CONFIG_HOME] = str(Path.home() / 'MyConfigs')
    assert get_default_config_dir() == Path.home() / 'MyConfigs' / DEFAULT_CONFIG_DIRNAME

# Generated at 2022-06-13 21:37:03.330279
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config = Config()
    config.save()
    assert config.is_new() is False

# Generated at 2022-06-13 21:37:15.503728
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    try:
        del os.environ[ENV_XDG_CONFIG_HOME]
    except KeyError:
        pass

    try:
        del os.environ[ENV_HTTPIE_CONFIG_DIR]
    except KeyError:
        pass

    # 1. explicitly set through env
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/foo/bar'
    assert get_default_config_dir() == Path('/foo/bar')

    # 2. Windows
    # (tested on Windows)

    # 3. legacy ~/.httpie
    (Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR).mkdir()
    assert get_default_config_dir() == Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR

    #

# Generated at 2022-06-13 21:37:26.931013
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    os.environ[ENV_XDG_CONFIG_HOME] = "~/config"
    assert get_default_config_dir() == Path("~/config/httpie")
    os.environ[ENV_HTTPIE_CONFIG_DIR] = "/etc/httpie"
    assert get_default_config_dir() == Path("/etc/httpie")
    del os.environ[ENV_HTTPIE_CONFIG_DIR]
    os.environ[ENV_XDG_CONFIG_HOME] = ""
    assert get_default_config_dir() == Path(".config/httpie")
    del os.environ[ENV_XDG_CONFIG_HOME]
    os.environ["HOME"] = "~"

# Generated at 2022-06-13 21:37:29.977933
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    dir_path = DEFAULT_CONFIG_DIR
    config = BaseConfigDict(dir_path)
    config.ensure_directory()
    assert dir_path.exists()

# Generated at 2022-06-13 21:37:58.440495
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    """
    Verify the function get_default_config_dir, by simulating different
    environment variables and testing the results.
    """
    # Prepare
    expected_path = None
    TEST_HOME = '/tmp/test_home'
    os.environ[ENV_HTTPIE_CONFIG_DIR] = None

    # Exec
    
    path = get_default_config_dir()
    
    # Check
    assert path == expected_path
    
if __name__ == '__main__':
    test_get_default_config_dir()

# Generated at 2022-06-13 21:38:11.046131
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    from config.test import (
        TestPath,
    )
    import os
    import tempfile
    home_dir = Path.home()
    dir_path = TestPath(tempfile.mkdtemp())
    config_test = BaseConfigDict(dir_path / DEFAULT_CONFIG_DIRNAME / Config.FILENAME)
    with pytest.raises(AssertionError):
        config_test.ensure_directory()
    if os.environ.get('TRAVIS_CI'):
        return
    with pytest.raises(ConfigFileError):
        config_test.ensure_directory()
    parent_dir = config_test.path.parent
    parent_dir.mkdir()
    parent_dir.chmod(0o777)
    config_test.ensure_directory()
    assert parent

# Generated at 2022-06-13 21:38:18.029445
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class Test(BaseConfigDict):
        FILENAME = 'test.json'
        DEFAULTS = {
            'default_options': []
        }
    try:
        config = Test(path=Path('/tmp/test.json'))
        config['key'] = 'value'
        config.save()

        # Test if file was written to
        assert os.path.isfile('/tmp/test.json')
    finally:
        try:
            os.remove('/tmp/test.json')
        except:
            pass

# Generated at 2022-06-13 21:38:23.658672
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    test_dir = Path('test_dir')
    test_dir.mkdir(mode=0o700, parents=True)
    test_dict = BaseConfigDict(path=test_dir / 'test.json')
    test_dict.save()
    assert Path(test_dir / 'test.json').exists()
    test_dict.delete()
    assert not Path(test_dir / 'test.json').exists()
    test_dir.rmdir()


# Generated at 2022-06-13 21:38:33.294517
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    import os
    import tempfile
    from pathlib import Path

    tmp_dir = Path(tempfile.mkdtemp())

    test_config_dict = BaseConfigDict(tmp_dir / 'config.json')
    test_config_dict['abc'] = 'abc'
    test_config_dict.save()
    test_config_dict.load()

    assert test_config_dict.get('abc') == 'abc'

    os.rmdir(tmp_dir)



# Generated at 2022-06-13 21:38:46.490172
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    """Test return of get_default_config_dir().
    """
    # Windows
    if is_windows:
        assert (DEFAULT_WINDOWS_CONFIG_DIR == get_default_config_dir())

    # Linux
    else:
        # Case 1: $XDG_CONFIG_HOME is set
        os.environ[ENV_XDG_CONFIG_HOME] = '/test/xdg_config_home'
        assert (
            (
                Path('/test/xdg_config_home')
                / DEFAULT_CONFIG_DIRNAME
            )
            == get_default_config_dir()
        )
        del os.environ[ENV_XDG_CONFIG_HOME]

        # Case 2: $XDG_CONFIG_HOME is not set
        # Case 2.1:

# Generated at 2022-06-13 21:38:55.679897
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    def get_path(path):
        return Path(path)
    assert get_default_config_dir() == get_path(os.path.expanduser("~/.config/httpie"))
    os.environ[ENV_HTTPIE_CONFIG_DIR] = "/var/lib/httpie"
    assert get_default_config_dir() == get_path("/var/lib/httpie")
    del os.environ[ENV_HTTPIE_CONFIG_DIR]
    os.environ[ENV_XDG_CONFIG_HOME] = "/etc/xdg"
    assert get_default_config_dir() == get_path("/etc/xdg/httpie")
    del os.environ[ENV_XDG_CONFIG_HOME]

# Generated at 2022-06-13 21:39:06.579422
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    class TestConfigDict(BaseConfigDict):
        def __init__(self, path):
            super().__init__(path)

    test_config = TestConfigDict(path=Path('test_config.json'))

    with open('test_config.json', 'w') as f:
        f.write('{"name": "test", "dict": {"a": "1", "b": "2"}}')

    test_config.load()

    assert test_config['name'] == 'test'
    assert test_config['dict']['a'] == '1'
    assert test_config['dict']['b'] == '2'



# Generated at 2022-06-13 21:39:17.444277
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    def check(expected,env):
        actual = get_default_config_dir()
        print(expected)
        print(actual)
        assert str(actual) == str(expected)

    # default
    check(Path('/home/naram/.config/httpie'), None)

    # XDG_CONFIG_HOME
    os.environ['XDG_CONFIG_HOME'] = '/path/to/xdg_config_home'
    check(Path('/path/to/xdg_config_home/httpie'), None)

    # Windows
    if is_windows:
        check(Path(os.path.expandvars('%APPDATA%')) / 'httpie', None)

    # HTTPIE_CONFIG_DIR

# Generated at 2022-06-13 21:39:28.704280
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    def get_base_config_dict():
        return BaseConfigDict(path=test_path)

    test_path = Path(__file__).parent.resolve() / 'test_path'
    try:
        test_path.unlink()
    except FileNotFoundError:
        pass

    assert not test_path.exists()

    bcd = get_base_config_dict()
    assert not bcd.is_new()

    bcd.ensure_directory()
    assert test_path.parent.exists()

    test_path.parent.mkdir(mode=0o700, parents=True)
    assert test_path.parent.exists()

    bcd = get_base_config_dict()
    assert not bcd.is_new()
