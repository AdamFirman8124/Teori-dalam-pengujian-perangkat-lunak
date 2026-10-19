

# Generated at 2022-06-13 21:29:48.558339
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config = BaseConfigDict(path=DEFAULT_CONFIG_DIR)
    config["key"] = "hello"



# Generated at 2022-06-13 21:30:02.654562
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    import subprocess
    import os
    import types

    def mkdir(path):
        try:
            subprocess.run(['mkdir','-p',path])
        except Exception as e:
            print(e)
    def rmdir(path):
        try:
            subprocess.run(['rm','-rf',path])
        except Exception as e:
            print(e)

    def check_and_ensure(path):
        mkdir(path)
        con = BaseConfigDict(Path(path))
        con.ensure_directory()
        rmdir(path)

    check_and_ensure('/tmp/httpie/some/directory')

# Generated at 2022-06-13 21:30:10.727230
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    # create a empty json file
    tmp_dir = Path(tempfile.gettempdir()) / 'test_' + next(tempfile._get_candidate_names())
    config_path = tmp_dir / 'config.json'
    config_path.parent.mkdir(mode=0o700, parents=True)
    config_path.touch()

    # test for valid file content
    json_string = json.dumps({'key': 'value'}, indent=4, sort_keys=True, ensure_ascii=True)
    config_path.write_text(json_string + '\n')
    test_config = Config(config_path.parent)
    test_config.load()
    assert test_config['key'] == 'value'

    # test for invalid file content
    json_string = '{'


# Generated at 2022-06-13 21:30:15.266847
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    class MockConfigDict(BaseConfigDict):
        pass

    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/tmp/httpie-config'
    config = MockConfigDict(path=Path('/tmp/httpie-config/mock_config.json'))
    assert config.path == Path('/tmp/httpie-config/mock_config.json')
    config.ensure_directory()
    assert Path('/tmp/httpie-config').exists()
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR)

# Generated at 2022-06-13 21:30:19.363001
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    test_instance = BaseConfigDict(Path('test_BaseConfigDict_load_path'))
    test_instance.load()



# Generated at 2022-06-13 21:30:27.993694
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    import os
    import sys
    import tempfile
    import textwrap
    fd, path = tempfile.mkstemp(suffix='.json')
    fp = os.fdopen(fd, 'wt')
    fp.write(textwrap.dedent("""\
        {
            "key": "value"
        }
        """))
    fp.close()
    class BaseConfigDict(object):
        def __init__(self, path):
            self.path = path
    config_dict = BaseConfigDict(path)
    config_dict.load()
    assert config_dict == {"key": "value"}
    os.remove(path)


# Generated at 2022-06-13 21:30:30.376715
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    res = get_default_config_dir()
    assert 'httpie' in str(res)
    assert os.path.isdir(str(res)) is False

# Generated at 2022-06-13 21:30:40.246154
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import os

    import tempfile

    temp_path = tempfile.mkdtemp()
    file_path = os.path.join(temp_path, 'test.json')
    d = {
        'test0': 1,
        'test1': 2,
        'test2': 2
    }
    try:
        config = BaseConfigDict(Path(file_path))
        config.save()
        config.update(d)
        config.save()
        assert config.path.exists() == True
    finally:
        os.remove(file_path)
        os.removedirs(temp_path)


# Generated at 2022-06-13 21:30:50.371093
# Unit test for function get_default_config_dir
def test_get_default_config_dir():

    # Default scenario
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    os.environ.pop(ENV_XDG_CONFIG_HOME, None)
    default_config_dir = get_default_config_dir()
    assert default_config_dir == Path.home() / '.config' / DEFAULT_CONFIG_DIRNAME

    # Legacy scenario
    def _legacy_path(path: Path) -> Path:
        return Path.home() / path
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    os.environ.pop(ENV_XDG_CONFIG_HOME, None)
    (Path.home() / '.httpie').touch()
    default_config_dir = get_default_config_dir()

# Generated at 2022-06-13 21:31:02.564491
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    from httpie.config import BaseConfigDict, ConfigFileError
    import json
    import os
    import os.path
    import tempfile
    import unittest

    class BaseConfigDictTestCase(unittest.TestCase):

        def test_load_01(self):
            """
            we try to load a non existent file
            """
            with tempfile.TemporaryDirectory() as tmpdirname:
                path = os.path.join(tmpdirname,"config.json")
                config = BaseConfigDict(path=path)
                self.assertFalse(config.path.exists())
                config.load()
                self.assertTrue(config.path.exists())

        def test_load_02(self):
            """
            we try to load a file with invalid json
            """

# Generated at 2022-06-13 21:31:18.784049
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Given
    assert ENV_HTTPIE_CONFIG_DIR not in os.environ

    # When / Then
    # Test default config dir with $XDG_CONFIG_HOME
    os.environ[ENV_XDG_CONFIG_HOME] = '/home/user/.config'
    expected = Path('/home/user/.config/httpie')
    assert get_default_config_dir() == expected
    # Test default config dir with legacy ~/.httpie
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    os.environ[ENV_XDG_CONFIG_HOME] = '/home/user/.config'
    os.makedirs(legacy_config_dir)
    expected = legacy_config_dir
    assert get_default_config

# Generated at 2022-06-13 21:31:27.704019
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    path = Path('config.json')
    data = {
        'test': 1,
        'test2': 2
    }
    config_type = 'config'
    try:
        with path.open('wt') as f:
            f.write(json.dumps(data))
    except IOError as e:
        raise ConfigFileError(f'cannot read {config_type} file: {e}')

    config = BaseConfigDict(path)
    config.load()
    assert config['test'] == 1
    assert config['test2'] == 2


# Generated at 2022-06-13 21:31:43.667420
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # The directory doesn't exist
    assert not get_default_config_dir().exists()

    # The directory exists
    pathlib.Path(os.environ['HOME'], '.config', 'httpie').mkdir(parents=True)
    assert get_default_config_dir().exists()

    # Environment variables
    os.environ['XDG_CONFIG_HOME'] = '/home/user/.config'
    assert get_default_config_dir() == pathlib.Path(
        '/home/user/.config', 'httpie')

    os.environ['HTTPIE_CONFIG_DIR'] = '/home/user/httpie'
    assert get_default_config_dir() == pathlib.Path('/home/user/httpie')

# Generated at 2022-06-13 21:31:54.938313
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    from pathlib import Path
    from shutil import rmtree
    from tempfile import mkdtemp
    from os import path
    import os

    tmpdir = Path(mkdtemp())
    testdir = tmpdir / "a/b/c"

    # test without parents
    p = Path(os.path.join(str(tmpdir), "a"))
    p.mkdir()
    f = p / "a"
    config = BaseConfigDict(f)

    config.ensure_directory()
    assert path.exists(os.path.join(f, "a"))
    assert path.exists(os.path.join(f, "a"))
    assert path.exists(os.path.join(p, "a"))
    assert path.exists(os.path.join(p, "a"))



# Generated at 2022-06-13 21:32:03.755068
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    """
    Unit test for method load of class BaseConfigDict.

    Test data is config.json. Transfer content
    of config.json to a list.
    Test method load of class BaseConfigDict by
    comparing the list result to the
    original content of config.json with assertEqual.
    """
    config = Config()
    config.load()
    f = config.path.open('rt')
    t = f.readlines()
    f.close()
    tt = []
    for i in t:
        tt.append(i.strip())
    tt[0] = '{'
    tt[-1] = '}'
    assertEqual(tt, ['{', '"__meta__": {', '"httpie": "2.2.0"', '}', '}'])


# Generated at 2022-06-13 21:32:05.153995
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert DEFAULT_CONFIG_DIR == get_default_config_dir()

# Generated at 2022-06-13 21:32:08.146227
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    c = Config(directory=".httpie")
    c.load()
    def _test_cc():
        assert c is not None
    _test_cc()


# Generated at 2022-06-13 21:32:11.920287
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert DEFAULT_CONFIG_DIR == '/home/user/.config/httpie'

    os.environ[ENV_XDG_CONFIG_HOME] = '/home/user/.myconfig'
    assert get_default_config_dir() == '/home/user/.myconfig/httpie'

# Generated at 2022-06-13 21:32:18.184152
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    # test for load successfully
    path = 'temp.json'
    with open(path, 'w+') as f:
        f.write('{"key": "value"}')
    config = BaseConfigDict(path)
    config.load()
    assert config['key'] == 'value'
    os.remove(path)


# Generated at 2022-06-13 21:32:26.805698
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class TestConfigFile(BaseConfigDict):
        FILENAME = 'test.json'
        DEFAULTS = {}

        def __init__(self, directory: Union[str, Path] = DEFAULT_CONFIG_DIR):
            self.directory = Path(directory)
            super().__init__(path=self.directory / self.FILENAME)

    import sys
    import pytest
    # The unlink() method raises an OSError if the file was already removed.
    # We want to capture this exception in order to continue with the tests
    # and verify that the file is not there anymore.
    # Therefore we need to disable the pytest warning that is raised in this
    # case.
    if sys.version_info < (3, 6):
        pytest.register_assert_rewrite('httpie.config')
   

# Generated at 2022-06-13 21:32:43.668931
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    path = Path('/tmp/test/config.json')
    bcd_obj = BaseConfigDict(path)
    assert bcd_obj.is_new()
    assert len(bcd_obj) == 0
    bcd_obj.save()
    assert path.exists()
    bcd_obj = BaseConfigDict(path)
    bcd_obj.load()
    test_key = 'test_key'
    test_value = 'test_value'
    bcd_obj[test_key] = test_value
    bcd_obj.save()
    bcd_obj = BaseConfigDict(path)
    bcd_obj.load()
    assert len(bcd_obj) == 2
    assert test_value == bcd_obj[test_key]

# Generated at 2022-06-13 21:32:56.673068
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import shutil
    import tempfile
    temp_path = tempfile.mkdtemp()
    temp_path = os.path.join(temp_path, 'httpie')
    temp_path += '/'

    bcd = BaseConfigDict(temp_path + 'config.json')
    bcd.save()
    assert os.path.exists(temp_path + 'config.json')

    # Test that save does not fail silently with mode=0o777
    os.chmod(temp_path, 0o777)
    bcd.save(fail_silently=False)
    os.chmod(temp_path, 0o700)

    bcd.delete()
    assert not os.path.exists(temp_path + 'config.json')

    bcd.ensure_directory()

# Generated at 2022-06-13 21:33:05.625916
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    from httpie.config import DEFAULT_CONFIG_DIR
    from httpie import config
    import os
    import shutil

    # Create a config dir for testing
    config_dir = DEFAULT_CONFIG_DIR / 'temp'
    config_dir.mkdir(mode=0o700, parents=True)

    # Create a file in the config dir
    config_file = config_dir / 'config.json'
    config_file.write_text('test')

    # Pass the test file to BaseConfigDict
    obj = config.BaseConfigDict(config_file)

    # Before calling ensure_directory, test to see if the file exists
    assert config_file.exists()


# Generated at 2022-06-13 21:33:10.731200
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    path = Path('.') / 'config' / 'test.json'
    config = BaseConfigDict(path)
    assert not config.path.parent.exists()
    for i in range(0, 5):
        config.ensure_directory()
        assert config.path.parent.exists()

# Generated at 2022-06-13 21:33:20.161743
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # The default configuration path on Windows
    assert DEFAULT_WINDOWS_CONFIG_DIR == Path(os.path.expandvars('%APPDATA%')) / DEFAULT_CONFIG_DIRNAME

    # The default configuration path on other non-Windows platforms.
    # Try to trigger the branch where both $XDG_CONFIG_HOME and $XDG_CONFIG_DIRS are absent.
    try:
        del os.environ[ENV_XDG_CONFIG_HOME]
    except KeyError:
        pass

    # Expect the default configuration path to be set to $HOME/.config/httpie in the absence of $XDG_CONFIG_HOME
    # and $XDG_CONFIG_DIRS environment variables.
    assert get_default_config_dir() == Path.home() / DEFAULT_RELATIVE

# Generated at 2022-06-13 21:33:30.653945
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    f = BaseConfigDict("/Users/weizhu/Desktop/test_config.json")
    f.save()
    with open("/Users/weizhu/Desktop/test_config.json") as test_config_f:
        test_config_string = json.load(test_config_f)
        assert test_config_string.get("httpie") == __version__
        assert test_config_string.get("__meta__")
        assert test_config_string.get("__meta__").get("httpie") == __version__


# Generated at 2022-06-13 21:33:38.068500
# Unit test for function get_default_config_dir

# Generated at 2022-06-13 21:33:39.244453
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    BaseConfigDict.load()

# Generated at 2022-06-13 21:33:53.817036
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # Test path parent
    import httpie

    # temp config path
    httpie.config.config.directory = httpie.config.DEFAULT_CONFIG_DIR

    # Generate a test config file
    httpie.config.config.update({
        'default_options': [],
    })
    httpie.config.config.save()

    # Test parent dir
    config_path = httpie.config.config.directory / httpie.config.config.FILENAME
    config_dir = config_path.parent

    # Delete the old one if it exists
    try:
        httpie.config.config.delete()
    except:
        pass

    # Old file does not exist
    assert os.path.exists(config_dir) is False

    httpie.config.config.ensure_directory()

    # Ensure that

# Generated at 2022-06-13 21:34:02.817010
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Test on Linux
    if not is_windows:
        with mock.patch.dict(os.environ, {}), \
                mock.patch('httpie.config.is_windows', False), \
                mock.patch('httpie.config.Path.home', lambda: Path('/home/user')):
            assert get_default_config_dir() == Path('/home/user/.config/httpie')

            os.environ[ENV_HTTPIE_CONFIG_DIR] = '/opt/config'
            assert get_default_config_dir() == Path('/opt/config')

            del os.environ[ENV_HTTPIE_CONFIG_DIR]
            os.environ[ENV_XDG_CONFIG_HOME] = '/tmp/config/'

# Generated at 2022-06-13 21:34:16.715055
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import json
    import os
    import shutil
    import tempfile
    from httpie import config
    
    temp_path = tempfile.mkdtemp()
    try:
        dst = os.path.join(temp_path, 'config.json')
        c = config.Config(directory=temp_path)
        c['test'] = "test"
        c.save()
        assert c.path.exists()
        assert os.path.getsize(dst)
    finally:
        shutil.rmtree(temp_path)

# Generated at 2022-06-13 21:34:19.274386
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    path = Path("/tmp/httpie/config.json")
    BaseConfigDict(path).ensure_directory()
    assert path.parent.exists()


# Generated at 2022-06-13 21:34:23.870243
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config_dir = Path.cwd()
    if not (config_dir / 'test').exists():
        config_dir.mkdir(mode=0o700, parents=True)

    config_file = config_dir / 'config.json'
    config_file.write_text('{"test": 1}')
    config = Config()
    config.load()
    assert config['test'] == 1
    config_file.unlink()

# Generated at 2022-06-13 21:34:33.960381
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    def check_directory(c):
        assert (c.path.exists())
        assert (c.path.is_dir())
    c = BaseConfigDict(Path(r'./'))
    c.ensure_directory()
    check_directory(c)

    c.path = Path(os.path.join('testdirectory', 'testdirectory1', 'testdirectory2'))
    c.ensure_directory()
    check_directory(c)

    c.path = Path(os.path.join('testdirectory', 'abc', 'abc', 'abc'))
    c.ensure_directory()
    check_directory(c)


# Generated at 2022-06-13 21:34:42.180718
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    with patch.dict(os.environ, {ENV_HTTPIE_CONFIG_DIR: '/custom/dir'}):
        assert get_default_config_dir() == Path('/custom/dir')

    with patch.dict(os.environ, {}):
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    with patch.dict(os.environ, {}, clear=True):
        assert get_default_config_dir() == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:34:48.048255
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() / '.config' / 'httpie'
    os.environ[ENV_XDG_CONFIG_HOME] = '/tmp'
    assert get_default_config_dir() == Path('/tmp') / 'httpie'
    del os.environ[ENV_XDG_CONFIG_HOME]

    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/tmp'
    assert get_default_config_dir() == Path('/tmp')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]


# Generated at 2022-06-13 21:34:58.655452
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    test_config = {
        '__meta__': {
            'httpie': __version__
        },
        'default_options': []
    }
    test_config_path = DEFAULT_CONFIG_DIR / Config.FILENAME
    test_config_obj = Config()
    test_config_obj.load()
    test_config_json_string = json.dumps(
            obj=test_config_obj,
            indent=4,
            sort_keys=True,
            ensure_ascii=True,
        )
    test_config_obj.save(fail_silently=False)
    with test_config_path.open('rt') as f:
        test_save_config = json.load(f)
    assert test_save_config == test_config

# Generated at 2022-06-13 21:35:10.725801
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # remove any HTTPIE_CONFIG_DIR enviromnent variable
    remove_HttpieConfigDirEnv()
    # remove any XDG_CONFIG_HOME enviromnent variable
    remove_XdgConfigHomeEnv()

    # testing under the following conditions:
    # * OS is NOT windows
    # * local directory does NOT exist, but with her parents existing
    def temp_testing(os, local_dir_parent, local_dir):
        # assert that the local config directory does NOT exist
        assert not os.path.exists(local_dir)
        # assert that the local config directory's parent does exist
        assert os.path.exists(local_dir_parent)
        # test default config directory returned by function
        assert get_default_config_dir() == Path(local_dir)


# Generated at 2022-06-13 21:35:11.403113
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    pass


# Generated at 2022-06-13 21:35:14.314966
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config_dir = Path('./test_cache')
    test_config_dict = BaseConfigDict(config_dir)
    try:
        test_config_dict.ensure_directory()
        config_dir.parent.rmdir()
    except OSError as err:
        if err.errno == errno.EEXIST:
            config_dir.parent.rmdir()



# Generated at 2022-06-13 21:35:27.803244
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    """Unit test for method load of class BaseConfigDict"""
    # fail_silently on load is False by default
    # so an exception of IOError will be raised
    config_dict = BaseConfigDict('test')
    try:
        config_dict.load()
    except ConfigFileError:
        assert True
    else:
        assert False


# Generated at 2022-06-13 21:35:30.388611
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    path = get_default_config_dir()
    assert path == '/home/hongbin/.config/httpie'



# Generated at 2022-06-13 21:35:32.871474
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    path = Path("test.json")
    config = BaseConfigDict(path)
    config.load()



# Generated at 2022-06-13 21:35:40.544063
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Test if legacy ~/.httpie is returned if present
    # and $XDG_CONFIG_HOME is not set
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    os.environ.pop(ENV_XDG_CONFIG_HOME, None)
    assert get_default_config_dir() == DEFAULT_RELATIVE_LEGACY_CONFIG_DIR

    # Test if legacy ~/.httpie is ignored if $XDG_CONFIG_HOME is set
    os.environ[ENV_XDG_CONFIG_HOME] = '/tmp/'
    assert get_default_config_dir() == Path('/tmp/') / DEFAULT_CONFIG_DIRNAME

    # Test if legacy ~/.httpie is ignored if $HTTPIE_CONFIG_DIR is set

# Generated at 2022-06-13 21:35:51.574583
# Unit test for function get_default_config_dir
def test_get_default_config_dir():

    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    else:
        try:
            import xdg.BaseDirectory
        #stderr is sent to log_base.DEBUG by default
        except ImportError:
            print(
                "xdg.BaseDirectory not available: "
                "skipping unit tests for XBD support"
            )
        else:
            os.environ[ENV_HTTPIE_CONFIG_DIR] = '/httpie_config_dir'
            assert get_default_config_dir() == '/httpie_config_dir'

            del(os.environ[ENV_HTTPIE_CONFIG_DIR])

            os.environ[ENV_XDG_CONFIG_HOME] = '/xdg_config_home'

# Generated at 2022-06-13 21:36:02.694409
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Test some tricky cases on Windows
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    os.environ[ENV_XDG_CONFIG_HOME] = r'C:\Foo\\Bar'
    assert get_default_config_dir()[-10:] == '\\Foo\\Bar'
    os.environ[ENV_XDG_CONFIG_HOME] = ''
    assert get_default_config_dir()[-17:] == '\\AppData\\Roaming'

    # Test a bunch of common cases on Linux
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    os.environ.pop(ENV_XDG_CONFIG_HOME, None)

# Generated at 2022-06-13 21:36:15.029174
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class A(BaseConfigDict):
        name = 'a'
        helpurl = 'http://njh.me/a'
        about = 'About A'

    config_dir = Path('/tmp/httpie-test/configdir')
    config_dir.mkdir(mode=0o700, parents=True, exist_ok=True)
    config_file = config_dir / A.FILENAME
    config_file.unlink(missing_ok=True)

    a = A(config_file)
    assert a.is_new() is True
    a.save()
    assert a.is_new() is False

    with config_file.open('rt') as f:
        a_config = json.load(f)

    assert a_config['__meta__']['httpie'] == __version__


# Generated at 2022-06-13 21:36:21.502933
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    try:
        # should return default value firstly
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
        # should support with HTTPIE_CONFIG_DIR set
        os.environ[ENV_HTTPIE_CONFIG_DIR] = 'dummy'
        assert get_default_config_dir() == 'dummy'
        # should support with XDG_CONFIG_HOME set
        os.environ[ENV_XDG_CONFIG_HOME] = 'dummy'
        assert get_default_config_dir() == ('dummy' / DEFAULT_CONFIG_DIRNAME)
    finally:
        if ENV_HTTPIE_CONFIG_DIR in os.environ:
            del os.environ[ENV_HTTPIE_CONFIG_DIR]

# Generated at 2022-06-13 21:36:22.933303
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config_dict = BaseConfigDict('config.json')
    config_dict.load()


# Generated at 2022-06-13 21:36:34.612099
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    class MyConfigDict(BaseConfigDict):
        def __init__(self, dir: str, filename: str):
            super().__init__(Path(dir) / filename)
            self.test_dir = dir + '/.test'
            self.test_filename = self.test_dir + '/temp.json'
            self.test_file = Path(self.test_filename)

    my_dict = MyConfigDict('/', 'test.json')
    my_dict.test_file.unlink(missing_ok=True)
    my_dict.test_file.parent.rmdir(missing_ok=True)
    my_dict.ensure_directory()
    assert(my_dict.test_file.parent.exists())
    my_dict.test_file.parent.rmdir()

# Generated at 2022-06-13 21:36:55.113208
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # Non existent directory
    path = Path('/tmp/test_httpie/config')
    d = BaseConfigDict(path)
    d.ensure_directory()
    assert d.path.parent.exists()
    assert d.path.parent.is_dir()
    assert d.path.parent.is_symlink() is False

    # Non existent directory with unaccessible parent directory
    path = Path('/tmp_does_not_exist/test_httpie/config')
    d = BaseConfigDict(path)
    try:
        d.ensure_directory()
    except OSError as e:
        assert e.errno == errno.ENOENT
    else:
        assert False

    # Existent directory
    path = Path('/tmp/test_httpie/config')
    d

# Generated at 2022-06-13 21:37:04.563459
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Test config dir in ENV_HTTPIE_CONFIG_DIR
    os.environ[ENV_HTTPIE_CONFIG_DIR] = "httpie_test_env"
    assert get_default_config_dir() == "httpie_test_env"
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    if is_windows:
        # Test config dir in APPDATA
        with patch('os.environ') as mock_env_vars:
            mock_env_vars.get = MagicMock(return_value=(DEFAULT_CONFIG_DIR.parent / "httpie_test_appdata").as_posix())
            assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR.parent / "httpie_test_appdata" / DEFAULT_CONFIG

# Generated at 2022-06-13 21:37:06.146444
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert str(get_default_config_dir()).endswith(DEFAULT_CONFIG_DIRNAME)


# Generated at 2022-06-13 21:37:10.481239
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config = BaseConfigDict('config.json')
    config.update({"author": "thosakwe"})
    config.save()
    assert config.load() == True

# Generated at 2022-06-13 21:37:23.148322
# Unit test for function get_default_config_dir

# Generated at 2022-06-13 21:37:25.361425
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:37:29.786880
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    parent = './test_directory'
    path = parent + '/config.json'
    config_dict = BaseConfigDict(path)
    config_dict.ensure_directory()
    assert os.path.exists(parent)
    os.rmdir(parent)

# Generated at 2022-06-13 21:37:39.833310
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    env_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    if env_config_dir:
        del os.environ[ENV_HTTPIE_CONFIG_DIR]  # type: ignore

    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
    else:
        home_dir = Path.home()
        legacy_config_dir = home_dir / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
        if legacy_config_dir.exists():
            assert get_default_config_dir() == legacy_config_dir

# Generated at 2022-06-13 21:37:50.273215
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() / '.config' / 'httpie'
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/custom/config/dir'
    assert get_default_config_dir() == Path('/custom/config/dir')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]
    os.environ[ENV_XDG_CONFIG_HOME] = '/custom/config/dir'
    assert get_default_config_dir() == Path('/custom/config/dir') / 'httpie'
    del os.environ[ENV_XDG_CONFIG_HOME]

# Generated at 2022-06-13 21:37:52.061039
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:38:21.847554
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    config_dir = Path(
        os.environ.get(ENV_HTTPIE_CONFIG_DIR, get_default_config_dir()))
    assert config_dir.exists() or config_dir.parent.exists()

# Generated at 2022-06-13 21:38:30.769264
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    path = './test_fixtures/test_ensure_directory/test_file'
    # ensure_directory makes file's parent directory if it doesn't exist.
    os.makedirs(os.path.dirname(path), exist_ok=True)
    assert os.path.exists(os.path.dirname(path))
    # Let's see if our test succeeds.
    test_dict = BaseConfigDict(path)
    test_dict.ensure_directory()


# Generated at 2022-06-13 21:38:33.770139
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert (get_default_config_dir()
            == Path('/home/user/.config/httpie'))

# Generated at 2022-06-13 21:38:39.570599
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config = BaseConfigDict(
        path=Path('~') / DEFAULT_CONFIG_DIRNAME / Config.FILENAME)
    config.ensure_directory()
    config.load()



# Generated at 2022-06-13 21:38:47.681548
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    def test_get_default_config_dir_with(**env):
        ENV_HTTPIE_CONFIG_DIR = env.get('ENV_HTTPIE_CONFIG_DIR')
        ENV_XDG_CONFIG_HOME = env.get('ENV_XDG_CONFIG_HOME')
        home_path = env.get('home_path')

        if ENV_HTTPIE_CONFIG_DIR:
            del os.environ[ENV_HTTPIE_CONFIG_DIR]

        if ENV_XDG_CONFIG_HOME:
            del os.environ[ENV_XDG_CONFIG_HOME]

        os.path.expandvars = lambda path: path.replace('%APPDATA%', str(Path(home_path, 'AppData')))

# Generated at 2022-06-13 21:38:56.247454
# Unit test for function get_default_config_dir

# Generated at 2022-06-13 21:39:07.253160
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import tempfile
    temp_file = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
    temp_path = temp_file.name
    temp_file.write('''{"name": "gossie"}''')
    temp_file.flush()
    temp_file.close()
    
    temp_config_file = BaseConfigDict(temp_path)
    temp_config_file.save()
    data = temp_config_file
    temp_config_file.delete()
    assert data == {'name': 'gossie', '__meta__': {'httpie': __version__}}, f'config file {temp_path} is not loaded'


# Generated at 2022-06-13 21:39:11.514310
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    from os import environ
    assert '/foo/bar' == str(get_default_config_dir())
    del environ['XDG_CONFIG_HOME']
    assert '/home/name/.config/httpie' == str(get_default_config_dir())

# Generated at 2022-06-13 21:39:17.866551
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    from pathlib import Path

    # set enviroment variables relevant for testing
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/tmp/config'
    os.environ[ENV_XDG_CONFIG_HOME] = '/home/user/.config'

    if is_windows:
        assert get_default_config_dir() == Path(
            os.path.expandvars('%APPDATA%')) / DEFAULT_CONFIG_DIRNAME
    else:
        assert get_default_config_dir() == Path('/tmp/config')



# Generated at 2022-06-13 21:39:26.635951
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import json
    import os
    import tempfile

    class SubClass(BaseConfigDict):
        name = None
        helpurl = None
        about = None

    with tempfile.TemporaryDirectory() as td:
        tmp_file = os.path.join(td, 'config.json')
        s = SubClass(tmp_file)
        s.update({'foo': 'bar'})
        s.save()
        with open(tmp_file, 'rt') as f:
            result = json.load(f)

    assert result == {'foo': 'bar', '__meta__': {'httpie': __version__}}