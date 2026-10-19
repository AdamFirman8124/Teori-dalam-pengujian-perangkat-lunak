

# Generated at 2022-06-13 21:29:55.280463
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    fpath = Path('/tmp/test.json')
    fpath.write_text('{"a": "1"}\n')
    config = BaseConfigDict(fpath)
    config.load()
    assert config['a'] == '1'



# Generated at 2022-06-13 21:30:03.197952
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    testfile = Path('/tmp/test_BaseConfigDict_save.json')
    testfile.unlink()
    testdict = BaseConfigDict(path=testfile)
    assert testdict.is_new()
    testdict.save()
    assert testfile.exists()
    assert testfile.stat().st_mode & 0o700 == 0o700
    with testfile.open('rt') as f:
        content = f.read()
    assert content == '{"__meta__": {"httpie": "' + __version__ + '"}}\n'



# Generated at 2022-06-13 21:30:11.710270
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    import tempfile
    tmp_dir = tempfile.gettempdir()
    tmp_dir_path = Path(tmp_dir)
    tmp_config_file = tmp_dir_path / 'config.json'
    tmp_config_dir = tmp_dir_path / 'httpie'
    tmp_config_dir_path = tmp_dir_path / 'httpie'
    test_config = Config(tmp_dir_path)
    #test create a new config directory
    test_config.path = tmp_config_dir_path / "config.json"
    test_config.ensure_directory()
    assert(os.path.exists(tmp_config_dir_path))

    #test create a new config file in a new config directory
    test_config.path = tmp_config_dir_path / "config_2.json"

# Generated at 2022-06-13 21:30:13.183572
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config_dict = BaseConfigDict(path='test.json')
    config_dict.load()
    org_dict = {
            '__meta__': {
                'httpie': __version__
            }
        }
    assert config_dict == org_dict


# Generated at 2022-06-13 21:30:21.510739
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    with TemporaryDirectory() as directory_path:
        # assert that the dir is empty
        assert not list(Path(directory_path).iterdir())
        # create the new dir
        BaseConfigDict(Path(directory_path) / 'foo.json').ensure_directory()
        # assert that the new dir exists
        assert Path(directory_path) / 'foo.json'


# Generated at 2022-06-13 21:30:31.380218
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    from pathlib import Path
    from httpie.config import DEFAULT_CONFIG_DIR

    # config dir does not exist
    config_file = DEFAULT_CONFIG_DIR / Config.FILENAME
    config = Config(DEFAULT_CONFIG_DIR)
    # the config file does not exist when config folder is not exist
    assert(not config_file.exists())
    # the following sentence is never executed
    config.load()

    # config dir exists, but the config file does not exist
    DEFAULT_CONFIG_DIR.mkdir(mode=0o700, parents=True)
    assert(DEFAULT_CONFIG_DIR.is_dir())
    # the config file does not exist when config folder exists
    assert(not config_file.exists())
    # the following sentence is never executed
    config.load()

# Generated at 2022-06-13 21:30:41.773525
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    """Unit test for function get_default_config_dir.
    """
    os.environ['HTTPIE_CONFIG_DIR'] = '/tmp/default'
    assert get_default_config_dir() == Path('/tmp/default')
    os.environ['HTTPIE_CONFIG_DIR'] = ''
    os.environ[ENV_XDG_CONFIG_HOME] = '/tmp'
    assert get_default_config_dir() == Path('/tmp/httpie')
    os.environ[ENV_XDG_CONFIG_HOME] = ''
    assert get_default_config_dir() == Path.home() / '.config/httpie'

# Generated at 2022-06-13 21:30:47.545479
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    path = Config().path
    with path.open('wt') as f:
        data = '{"key1":"value1","key2":"value2"}'
        f.write(data)
    config = Config()
    config.load()
    assert config['key1'] == 'value1'
    assert config['key2'] == 'value2'
    path.unlink()


# Generated at 2022-06-13 21:31:01.179953
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    import json
    import os
    import tempfile
    e = ConfigFileError
    # test load a non-existent file or folder
    with tempfile.TemporaryDirectory() as t:
        # load a non-existent file
        t_p = Path(t)
        c = BaseConfigDict(path=t_p / 'foo.json')
        try:
            c.load()
        except ConfigFileError as err:
            assert err.args[0] == f'cannot read baseconfigdict file: [Errno 2] No such file or directory: \'{t_p/ "foo.json"}\''
        # load a non-existent folder
        c = BaseConfigDict(path=t_p / 'foo' / 'foo.json')

# Generated at 2022-06-13 21:31:11.891245
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Test: $XDG_CONFIG_HOME is explicitly set
    env_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    assert env_config_dir is None

    os.environ[ENV_HTTPIE_CONFIG_DIR] = 'test'
    assert get_default_config_dir() == 'test'
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test: Windows
    assert is_windows
    assert get_default_config_dir() == Path('%APPDATA%') / DEFAULT_CONFIG_DIRNAME

    # Test: legacy ~/.httpie
    # Simplified, assuming the directory exists
    home_dir = Path.home()
    legacy_config_dir = home_dir / DEFAULT_RELATIVE_LEGACY

# Generated at 2022-06-13 21:31:19.941455
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    with open('too_bad.conf', 'wt') as f:
        f.write('{"name":"httpie",')
    config = BaseConfigDict('too_bad.conf')
    try:
        config.load()
    except ConfigFileError as e:
        print('This exception should be raised!')


if __name__ == '__main__':
    test_BaseConfigDict_load()

# Generated at 2022-06-13 21:31:30.475923
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    ## config_type = type(self).__name__.lower()
    config_type = "BaseConfigDict"
    ## self.path.open('rt')
    path = Path('test.json')
    f = path.open('w')
    f.write('{"key":"value"}')
    f.close()
    ## json.load(f)
    with path.open('rt') as f:
        data = json.load(f)
    ## self.update(data)
    config = BaseConfigDict(path)
    config.update(data)
    print(config)
    # @TODO how to test the exception



# Generated at 2022-06-13 21:31:44.831862
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    import shutil  # noqa
    import tempfile

    def test_dir_creation(dir_path: Union[Path, str]) -> None:
        dir_path = Path(dir_path)
        config_dir = dir_path / DEFAULT_CONFIG_DIRNAME
        config_dir.mkdir(mode=0o700, parents=True)
        assert config_dir.exists()
        config_dir.unlink()

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        config_dir = Config(directory=tmpdir).directory
        # Normal case
        test_dir_creation(config_dir)
        # Non-ASCII characters
        test_dir_creation(str(tmpdir / 'mötörhead_rules'))

# Generated at 2022-06-13 21:31:47.998129
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    config_dir = get_default_config_dir()
    assert config_dir == Path.home() / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME

# Generated at 2022-06-13 21:32:00.835410
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    test_data_root = Path(__file__).parent / 'data'
    class TestConfigDict(BaseConfigDict):
        def __init__(self, path: Path):
            super().__init__(path)

    test_config1 = TestConfigDict(path=test_data_root / 'config1.json')
    test_config1_dict = {'default_options': ['--form'], 'schema': 'https', 'follow': True, '__meta__': {'httpie': '0.9.9.9'}}
    assert test_config1['default_options'] == test_config1_dict['default_options']
    assert test_config1['schema'] == test_config1_dict['schema']
    assert test_config1['follow'] == test_config1_dict['follow']


# Generated at 2022-06-13 21:32:06.815407
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    import tempfile
    from pathlib import Path

    # invalid json
    with tempfile.TemporaryDirectory() as tmpdir:
        bad_config_path = Path(tmpdir) / 'bad_config.json'
        bad_config_path.write_text('bad json')
        with pytest.raises(ConfigFileError):
            BaseConfigDict(bad_config_path).load()

# Generated at 2022-06-13 21:32:08.052486
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
  pass


# Generated at 2022-06-13 21:32:11.065743
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    try:
        config_file = ConfigFile()
        config_file.ensure_directory()
    except Exception as e:
        assert False, f'Exception occurred: {e}'


# Generated at 2022-06-13 21:32:18.647368
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    global DEFAULT_CONFIG_DIR
    config_dir = Path(__file__).parent / 'test_config_dir'
    DEFAULT_CONFIG_DIR = config_dir
    try:
        config = Config()
    except Exception as e:
        assert 0, e
    config.clear()
    config['some'] = 'some'
    config.save()
    config.load()
    loaded_config = config
    assert loaded_config == {'some': 'some', '__meta__': {'httpie': __version__}}
    assert config.directory == config_dir
    try:
        config['some'] = 'some'
        config.delete()
    except Exception as e:
        assert 0, e
    finally:
        DEFAULT_CONFIG_DIR = get_default_config_dir()

# Generated at 2022-06-13 21:32:21.210932
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():

    class _TestConfigDict(BaseConfigDict):
        pass

    _TestConfigDict(Path('./config.json')).load()

# Generated at 2022-06-13 21:32:34.096563
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    class TestConfig(BaseConfigDict):
        def __init__(self):
            temp_path = Path('/tmp')
            super().__init__(path=temp_path / 'test.json')

    t = TestConfig()
    t.ensure_directory()
    assert t.path.parent.exists()
    t.path.parent.rmdir()

# Generated at 2022-06-13 21:32:38.963803
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config = BaseConfigDict(Path('./tests/resources/config/config.json'))
    config['name'] = 'config'
    config.load()
    assert config['name'] == 'config'
    assert config['default_options'][0] == '--form'

# Generated at 2022-06-13 21:32:40.635631
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:32:47.250632
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    class BaseDict(BaseConfigDict):
        pass

    tmp_dir = Path('tmp')
    assert not tmp_dir.exists()
    tmp_dict = BaseDict(tmp_dir / 'tmp_file')
    tmp_dict.ensure_directory()
    assert tmp_dir.exists()
    assert tmp_dir.is_dir()

    tmp_dict.path.parent.rmdir()
    tmp_dict.path.parent.rmdir()



# Generated at 2022-06-13 21:32:59.734273
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    env_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    windows = is_windows
    xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)
    home_dir = Path.home()


# Generated at 2022-06-13 21:33:00.732890
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    assert Config().ensure_directory() == None

# Generated at 2022-06-13 21:33:07.716227
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    from httpie.config import BaseConfigDict
    from httpie.compat import is_windows
    config = BaseConfigDict('/tmp/httpie/test_BaseConfigDict_save.json')
    config.ensure_directory()
    config['test1'] = 100
    config.save()
    assert True

# Generated at 2022-06-13 21:33:14.443740
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    def setUp(self):
        self.p_path = tempfile.mkdtemp()
        self.p = Path(self.p_path)

    def tearDown(self):
        shutil.rmtree(self.p_path)

    def test_no_parent_dir(self):
        BaseConfigDict(self.p / 'not_there' / 'child').save()
        self.assertTrue(self.p.exists())

# Generated at 2022-06-13 21:33:21.574378
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    import json
    import os
    import tempfile
    from pathlib import Path
    from httpie.config import BaseConfigDict
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmpdir = Path(tmpdirname)
        tmppath = tmpdir / 'config.json'
        baseconfigdict = BaseConfigDict(tmppath)
        try:
            baseconfigdict.load()
        except:
            assert False
        tmppath.write_text(json.dumps(baseconfigdict))
        baseconfigdict = BaseConfigDict(tmppath)
        try:
            baseconfigdict.load()
        except:
            assert False
        tmppath.write_text("err-data")
        baseconfigdict = BaseConfigDict(tmppath)

# Generated at 2022-06-13 21:33:28.490291
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():

    class TestConfig(BaseConfigDict):
        name = 'test'
        helpurl = None
        about = None

    test_path = Path('/tmp/test')
    test_config = TestConfig(test_path)

    assert test_config == {}, f'config dict should be empty: {test_config}'



# Generated at 2022-06-13 21:33:33.164755
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:33:41.861105
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    test_data = {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3"
    }
    class TestConfigDict(BaseConfigDict):
        def __init__(self, path: Path):
            super().__init__(path)
    test_file = 'test_BaseConfigDict_load.json'
    test_path = Path('./') / test_file
    json_string = json.dumps(
        obj=test_data,
        indent=4,
        sort_keys=True,
        ensure_ascii=True,
    )
    if test_path.is_file():
        test_path.unlink()
    test_path.write_text(json_string + '\n')
    config = TestConfigD

# Generated at 2022-06-13 21:33:54.970897
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    from tempfile import mkdtemp
    from shutil import rmtree
    from os import chmod
    from os.path import join

    def tmp_dir_is_a_dir():
        try:
            mkdtemp()
        except FileExistsError:
            return False
        return True

    tmp_dir = mkdtemp() # Creates the tmp_dir temporary directory

    config_dir = join(tmp_dir, 'config_dir')
    config_file = join(config_dir, 'config.json')

    bcd = BaseConfigDict(config_file)
    assert not bcd.is_new() # config.json file should not be new in the newly created directory
    bcd.ensure_directory() # Now we create the directory

    # Checking if the directory was correctly created
    assert tmp_dir_is_a

# Generated at 2022-06-13 21:34:09.835343
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import pytest
    import random
    import string
    import os
    import time

    # create a random file name
    def rand_str(length):
        return ''.join(random.sample(string.ascii_letters + string.digits, length))

    file_name = rand_str(10) + '.json'
    path_dir = os.path.dirname(__file__) + '/' + file_name
    with BaseConfigDict(path=path_dir) as f:
        assert f.load() is None
        assert f.save() is None
    os.remove(path_dir)
    with pytest.raises(ConfigFileError):
        BaseConfigDict(path=path_dir).save()

    file_name = rand_str(10) + '.json'
    path_dir = os

# Generated at 2022-06-13 21:34:16.821394
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    temp_config_dir = Path('/tmp/httpie-temp-config/')
    if temp_config_dir.exists():
        temp_config_dir.rmdir()

    temp_config = BaseConfigDict(path=temp_config_dir)
    temp_config.ensure_directory()

    assert (Path('/tmp/httpie-temp-config') ==
           Path(temp_config.path).parent)

# Generated at 2022-06-13 21:34:21.320083
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    test_path = '/tmp/test_BaseConfigDict_load.json'
    data = dict(a=1, b=2)
    with open(test_path, 'w') as f:
        json.dump(data, f)
    test_obj = BaseConfigDict(Path(test_path))
    test_obj.load()
    assert test_obj == data
    os.unlink(test_path)


# Generated at 2022-06-13 21:34:34.254768
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    def c(p: Path) -> Path:
        """
        Clean up the path, making it more likely to succeed whatever the
        environment, i.e. not relying on HOME or APPDATA.
        """
        return Path(os.path.expandvars(os.path.expanduser(str(p))))

    assert c(get_default_config_dir()) == c(DEFAULT_CONFIG_DIR)
    os.environ['HOME'] = '/home/joe'
    assert c(get_default_config_dir()) == c(Path('/home/joe/.config/httpie'))
    os.environ['XDG_CONFIG_HOME'] = '/etc/xdg'
    assert c(get_default_config_dir()) == c(Path('/etc/xdg/httpie'))
    os

# Generated at 2022-06-13 21:34:39.263385
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    path = os.path.dirname(__file__) + "/../.httpietestsfile"
    c = BaseConfigDict(path = path)
    c.load()
    assert c == {'__meta__': {'httpie': '0.5.0'}}


# Generated at 2022-06-13 21:34:46.731282
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    from unittest import mock
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as tempdir:
        path = Path(tempdir, 'test_BaseConfigDict_save.json')
        config = BaseConfigDict(path=path)
        config.ensure_directory = mock.Mock()
        config.save()
        config.ensure_directory.assert_called_once()
        config.default_options = ['--form']
        config.save()
        with path.open('rt') as f:
            data = json.load(f)
            assert data['default_options'] == ['--form']
        config.delete()

# Generated at 2022-06-13 21:34:53.995018
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    class config(BaseConfigDict):
        pass
    config_path = Path('test.json')
    config_dict = config(config_path)
    config_dict['key'] = 'value'
    config_dict.save()
    data = config(config_path)
    data.load()
    assert data is not config_dict
    assert data['key'] == config_dict['key']


# Generated at 2022-06-13 21:35:07.213083
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdirname:
        path = Path(tmpdirname)/'config.json'
        path.write_text("""{"key": "value"}""")
        config = Config(directory=tmpdirname)
        config.load()
        assert config['key'] == 'value'

# Generated at 2022-06-13 21:35:19.398841
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    def clear(name):
        if name in os.environ:
            del os.environ[name]

    def ensure(name, value):
        os.environ[name] = value
        print(f'{name}: {os.environ[name]}')

    def path_exists(path):
        if path.exists() and path.is_dir():
            print(f'{path} exists')
        else:
            print(f'{path} not exists')

    home = Path.home()
    print(f'home: {home}')
    xdg_config_home = home / DEFAULT_RELATIVE_XDG_CONFIG_HOME
    print(f'xdg_config_home: {xdg_config_home}')
    legacy_config_dir = home / DEFAULT_RELATIVE

# Generated at 2022-06-13 21:35:33.184856
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() / '.config' / 'httpie'
    home_dir = '/some/test/home/dir'
    assert get_default_config_dir(
        os.path.join(home_dir, '.config'),
        os.path.join(home_dir, '.httpie')
    ) == Path(home_dir) / '.config' / 'httpie'
    assert get_default_config_dir(
        os.path.join(home_dir, '.config'),
        os.path.join(home_dir, '.httpie')
    ) == Path(home_dir) / '.config' / 'httpie'

# Generated at 2022-06-13 21:35:38.381799
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    """
    Test the method load of class BaseConfigDict
    """
    # Create a temporary file that contains valid JSON
    with tempfile.NamedTemporaryFile(mode='w+t', delete=False) as temp:
        temp.write('{"test": "value"}')
    baseConfig = BaseConfigDict(temp.name)
    baseConfig.load()
    assert baseConfig['test'] == 'value'
    os.unlink(temp.name)


# Generated at 2022-06-13 21:35:44.985182
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    # create test.json file
    json_string = '{ "1":"1", "2":"2", "3":"3" }'
    test_path = Path('/tmp/test.json')
    with open(test_path, "w") as f:
        f.write(json_string)

    # test load function
    try:
        test = BaseConfigDict(path=test_path)
        test.load()
        assert test['1'] == '1'
        assert test['2'] == '2'
        assert test['3'] == '3'
    except:
        print('BaseConfigDict load function test failed')

    # clean up test.json file
    os.remove(test_path)


# Generated at 2022-06-13 21:35:53.552071
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    from httpie.config import os
    from httpie.compat import is_windows

    os.environ = {}
    assert get_default_config_dir() == Path.home() / '.config' / 'httpie'

    os.environ = {'XDG_CONFIG_HOME': '/xdg'}
    assert get_default_config_dir() == Path('/xdg') / 'httpie'

    os.environ.clear()
    os.path.expandvars = lambda var: str(Path('%APPDATA%'))
    assert get_default_config_dir() == Path('%APPDATA%') / 'httpie'

    os.environ = {'HTTPIE_CONFIG_DIR': '/env'}
    assert get_default_config_dir() == Path('/env')



# Generated at 2022-06-13 21:35:57.724018
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    """The test case for the function get_default_config_dir ."""
    # pylint: disable=protected-access
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR, "Test fail"

# Generated at 2022-06-13 21:36:03.049945
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config = BaseConfigDict(path='test.json')
    if os.path.exists('test'):
        try:
            os.remove('test/test.json')
        except:
            pass
        os.rmdir('test/')
    if os.path.exists('test.json'):
        os.remove('test.json')
    config.ensure_directory()
    assert os.path.exists('test')

# Generated at 2022-06-13 21:36:05.307747
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    dic = BaseConfigDict()
    dic.load()



# Generated at 2022-06-13 21:36:16.410393
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
        return

    home = os.environ['HOME']
    legacy_config_dir = home + '/.httpie'
    expected_xdg_config_dir = home + '/.config/httpie'

    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    os.environ.pop(ENV_XDG_CONFIG_HOME, None)

    assert get_default_config_dir() == Path(legacy_config_dir)

    os.environ[ENV_XDG_CONFIG_HOME] = '/tmp/foo'
    assert get_default_config_dir() == Path('/tmp/foo/httpie')


# Generated at 2022-06-13 21:36:43.359170
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    from httpie.config import get_default_config_dir

    def assert_config_dir_equals(expected: str, env: dict = None):
        if env:
            os.environ.update(env)
        assert expected == str(get_default_config_dir())

    assert_config_dir_equals('/home/user/.config/httpie')
    assert_config_dir_equals(
        '/home/user/.config/httpie',
        env={
            ENV_XDG_CONFIG_HOME: '/home/user/.config'
        }
    )

# Generated at 2022-06-13 21:36:55.512000
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    import io
    import json

    # Test case 1: default malformed json

    sample_data = """{
    "foo": "bar"
    "baz": 42}"""
    content = io.StringIO(sample_data)
    config_dict = BaseConfigDict(Path('sample_file.json'))
    with pytest.raises(ConfigFileError) as config_file_error:
        config_dict.load(content)
    assert 'invalid config file: Expecting property name enclosed in double' in config_file_error.value

    # Test case 2: default malformed json
    sample_data = """{"foo": "bar" "baz": 42}"""
    content = io.StringIO(sample_data)
    config_dict = BaseConfigDict(Path('sample_file.json'))

# Generated at 2022-06-13 21:36:56.852908
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    pass


# Generated at 2022-06-13 21:37:02.173841
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    try:
        config = BaseConfigDict(Path("/home/coin/Desktop/httpie-master/httpie/tests/data/config_examples/config.json"))
        config.load()
    except ConfigFileError as err:
        print(err)



# Generated at 2022-06-13 21:37:05.686745
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    c = BaseConfigDict(Path('test_path_test'))
    assert not c.path.exists()
    c.ensure_directory()
    assert c.path.exists()
    c.path.parent.rmdir()

# Generated at 2022-06-13 21:37:20.037393
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    os.environ[ENV_XDG_CONFIG_HOME] = '.'
    assert get_default_config_dir() == DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME
    os.environ[ENV_XDG_CONFIG_HOME] = '/some/path'
    assert get_default_config_dir() == Path('/some/path') / DEFAULT_CONFIG_DIRNAME
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/some/config/dir'
    assert get_default_config_dir() == Path('/some/config/dir')

# Generated at 2022-06-13 21:37:31.227200
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    test_BaseConfigDict = BaseConfigDict(Path("/home/Oskar/workspace1/httpie"))
    test_BaseConfigDict.save()
    test_BaseConfigDict.path = Path("/home/Oskar/workspace1/httpie/config.json")
    test_BaseConfigDict.load()
    assert test_BaseConfigDict == {'__meta__': {'about': 'https://github.com/jakubroztocil/httpie', 'help': 'https://github.com/jakubroztocil/httpie#config'}, 'default_options': []}



# Generated at 2022-06-13 21:37:37.489703
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    test_dir = Path('./test_dir')
    test_dir.mkdir(mode=0o700, parents=True)

    test_file = test_dir / 'test_config.json'
    test_file.write_text('{}\n')

    test_config = BaseConfigDict(path=test_file)
    test_config.load()

    assert test_config == {}
    
    test_file.unlink()
    test_dir.rmdir()

# Generated at 2022-06-13 21:37:48.719962
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    import tempfile
    import os
    import os.path
    
    class TmpDict(BaseConfigDict):
        def __init__(self):
            f = tempfile.NamedTemporaryFile(delete=False)
            self.path = Path(f.name)
            f.close()

    d = TmpDict()
    assert d.is_new()
    # filename does not exist
    try:
        d.load()
        assert False
    except ConfigFileError as e:
        print(e)

    # write a empty file
    f = open(d.path, "w")
    f.write("")
    f.close()

    # empty file
    try:
        d.load()
        assert False
    except ConfigFileError as e:
        print(e)
    os.remove

# Generated at 2022-06-13 21:37:54.500984
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    d = BaseConfigDict(path=Path("/tmp/test-config"))
    d['test'] = 1
    d.save()
    assert len(d) == 2
    assert d['test'] == 1
    assert d['__meta__']['httpie'] == __version__
    

# Generated at 2022-06-13 21:38:20.585050
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR



# Generated at 2022-06-13 21:38:32.954924
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    from unittest.mock import patch
    from httpie.config import get_default_config_dir, DEFAULT_CONFIG_DIRNAME

    def _test(key, value):
        return get_default_config_dir() == Path(value) / DEFAULT_CONFIG_DIRNAME

    # Test 1.
    with patch.dict(os.environ, {'HTTPIE_CONFIG_DIR': '/tmp'}, clear=True):
        assert _test('HTTPIE_CONFIG_DIR', '/tmp'), 'Test 1 failed'

    # Test 2.
    with patch.dict(os.environ, {'TRAVIS': 'true'}, clear=True):
        assert _test('TRAVIS', Path.home() / DEFAULT_CONFIG_DIRNAME), 'Test 2 failed'

    # Test 3.

# Generated at 2022-06-13 21:38:44.357265
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert Path(os.path.join(Path(__file__).parent, "..", "..", "..", "httpie", ".config", "httpie")).exists()
    if is_windows:
        assert Path("C:\\Users\\zhaoy\\AppData\\Roaming\\httpie\\config.json").exists()
    else:
        assert Path(os.environ['HOME'] + os.sep + ".config" + os.sep + "httpie" + os.sep + "config.json").exists()


# Generated at 2022-06-13 21:38:52.795121
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    from tempfile import mkdtemp
    import json
    import os

    class tconfig_dict(BaseConfigDict):
        pass
    d = tconfig_dict("config.json")
    temp_dir = mkdtemp()
    d.path = os.path.join(temp_dir, "config.json")
    d.save()
    with open(d.path, 'r') as f:
        data = json.load(f)
    assert data == d
    os.remove(d.path)
    os.rmdir(temp_dir)

if __name__ == '__main__':
    test_BaseConfigDict_save()

# Generated at 2022-06-13 21:38:59.046253
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    json_file = """
    {
        "alpha": "foo",
        "beta": "bar",
        "gamma": {
            "some": "thing"
        },
        "__meta__": {
            "httpie": "1.0.0",
            "help": "https://github.com/jakubroztocil/httpie#config",
            "about": "https://httpie.org/"
        }
    }
    """
    config = Config()
    path = Path(config.FILENAME)
    path.write_text(json_file)
    config.load()
    assert type(config) == dict
    assert config['alpha'] == "foo"
    assert config['beta'] == "bar"
    assert config['gamma'] == {"some": "thing"}

# Generated at 2022-06-13 21:39:09.720004
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    # create a config instance
    d = BaseConfigDict(Path('.httpie') / 'config.json')
    # ensure the directory exists
    d.ensure_directory()
    # check taht the file is written only if it doesn't exist
    if d.is_new():
        d.save()

    # check that the file is read when it exists
    d.load()
    # check that the meta data is written to the file
    d.save()
    assert('httpie' in d['__meta__'] and 'help' in d['__meta__'])
    assert(d['__meta__']['about'] == d.about)
    assert(d['__meta__']['help'] == d.helpurl)
    d.delete()


# Generated at 2022-06-13 21:39:19.242438
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    os_env_var = os.environ
    # Neither HTTPIE_CONFIG_DIR or XDG_CONFIG_HOME is set
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    os.environ.pop(ENV_XDG_CONFIG_HOME, None)
    # Get default config dir
    default_config_dir = get_default_config_dir()
    # Check default config dir
    assert default_config_dir == Path.home() / '.config' / 'httpie'
    # Set HTTPIE_CONFIG_DIR
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/home/test/.config/'
    # Get default config dir
    config_dir = get_default_config_dir()
    # Check config dir
    assert config_

# Generated at 2022-06-13 21:39:30.178967
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() / '.config' / 'httpie'

    os.environ[ENV_HTTPIE_CONFIG_DIR] = 'test'
    assert get_default_config_dir() == 'test'
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR)

    assert get_default_config_dir() == Path.home() / '.config' / 'httpie'

    home_dir = Path.home()
    os.environ[ENV_XDG_CONFIG_HOME] = ''
    assert get_default_config_dir() == home_dir / '.config' / 'httpie'
    os.environ.pop(ENV_XDG_CONFIG_HOME)


# Generated at 2022-06-13 21:39:40.769086
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    def test_config_dir(env, expected):
        os.environ.clear()
        os.environ.update(env)
        assert get_default_config_dir() == expected

    def test_custom_xdg_config_home(home_dir: str, env: dict, expected: str):
        os.environ.clear()
        os.environ.update(env)
        assert get_default_config_dir() == Path(home_dir) / expected

    # windows
    env = dict(HTTPIE_CONFIG_DIR='abc', SystemRoot='C:/')
    expected = Path('C:/abc')
    test_config_dir(env, expected)

    # explicitly set
    env = dict(HTTPIE_CONFIG_DIR='abc')
    expected = Path('abc')