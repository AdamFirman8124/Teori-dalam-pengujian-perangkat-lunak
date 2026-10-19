

# Generated at 2022-06-13 21:29:57.798309
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class TestConfig2(BaseConfigDict):
        def __init__(self, path: Path):
            super().__init__(path)
            self.config = []
            self.config.append(self.path)

    test_config_2 = TestConfig2(Path('test.json'))
    test_config_2.save()
    test_config_2 = TestConfig2(Path('test_2.json'))
    test_config_2.save()

test_BaseConfigDict_save()

# Generated at 2022-06-13 21:30:02.334036
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    class TestConfigDict(BaseConfigDict):
        def __init__(self):
            self.path = Path('/tmp/httpie/test_config.json')
            super().__init__(self.path)
    test_config = TestConfigDict()
    test_config.ensure_directory()

# Generated at 2022-06-13 21:30:08.006303
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config_dict = BaseConfigDict(Path())
    config_dict.update({'param1':'val1', 'param2':'val2'})
    config_dict.save()
    config_dict.path.write_bytes(b'Bad JSON')
    try:
        config_dict.load()
    except ConfigFileError as e:
        pass # Ok, fail_silently == False
    config_dict.save(True)
    config_dict.load()
    config_dict.delete()

# Generated at 2022-06-13 21:30:13.480873
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config = BaseConfigDict(path='')
    config.load()



# Generated at 2022-06-13 21:30:17.597389
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir().name == 'httpie'
    assert get_default_config_dir().parent.name == 'http'



# Generated at 2022-06-13 21:30:28.192196
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    class TestConfigDict(BaseConfigDict):
        name = 'test'
        helpurl = 'https://example.org'
        about = 'Unit tester.'
    filename = 'config.json'
    basedir = Path.home()
    path = Path('/etc/httpie')
    dir = path / 'config'
    test_config = TestConfigDict(path=dir / filename)

    try:
        test_config.load()
        assert False
    except ConfigFileError:
        pass

    test_config['a'] = 1
    test_config['b'] = 'test'

# Generated at 2022-06-13 21:30:32.958829
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config_dict = BaseConfigDict(Path('~/httpie/.dir/config.json'))
    config_dict.ensure_directory()
    path = '~/httpie/.dir/config.json'
    config_dict.path = Path(path)
    config_dict.ensure_directory()

# Generated at 2022-06-13 21:30:36.312947
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    bcd = BaseConfigDict("config.json")
    bcd.load()
    #assert len(bcd) > 0


# Generated at 2022-06-13 21:30:44.088600
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    from tempfile import TemporaryDirectory
    from httpie.config import BaseConfigDict
    from httpie.compat import is_windows
    from os import path

    with TemporaryDirectory() as tmpdirname:
        if is_windows:
            tmpdir = path.join(tmpdirname, "test")
        else:
            tmpdir = path.join(tmpdirname, "test/test")
        config = BaseConfigDict(path.join(tmpdir, "config"))
        config.ensure_directory()
        assert path.exists(tmpdir)

# Generated at 2022-06-13 21:30:52.504687
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config_dir = Path('./test_dir')
    if config_dir.exists():
        shutil.rmtree(config_dir)
    config_dir.mkdir()
    assert config_dir.is_dir()

    test_config = BaseConfigDict(config_dir / 'test.json')
    test_config["a"] = 1
    test_config.save()

    # read the test.json file generated
    with (config_dir / 'test.json').open('r') as file:
        text = file.read()
        file.close()
    os.remove(config_dir / 'test.json')
    os.rmdir(config_dir)
    # check whether the structure of json is correct

# Generated at 2022-06-13 21:31:05.174228
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    import tempfile
    config_dir = Path(tempfile.mkdtemp())
    config_file_path = config_dir / 'config.json'
    # ensure config_dir has right permission
    config_dir.chmod(mode=0o700)
    # test, ensure config_dir exists
    config = Config(directory=config_dir)
    assert config.path == config_file_path, 'test failed'
    # test, ensure config_dir/config.json exists
    config.ensure_directory()
    assert config.path.exists() == True, 'test failed'
    # clean up
    config_dir.rmdir()

# Generated at 2022-06-13 21:31:11.083329
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir().is_absolute()
    env_config_dir_name = '/foo'

    # for env HTTPIE_CONFIG_DIR
    os.environ[ENV_HTTPIE_CONFIG_DIR] = env_config_dir_name
    assert get_default_config_dir() == Path(env_config_dir_name)

# Generated at 2022-06-13 21:31:19.812492
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import os
    import sys
    home_dir = Path.home()
    xdg_config_home = Path(os.environ['XDG_CONFIG_HOME'])
    if sys.platform == 'win32' or os.environ['XDG_CONFIG_HOME'] is not '':
        assert get_default_config_dir() == xdg_config_home / DEFAULT_CONFIG_DIRNAME
    else:
        assert get_default_config_dir() == home_dir / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME

# Generated at 2022-06-13 21:31:24.382319
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    xdg_config_home="xdg_config_home"
    home_dir="home_dir"
    global_app_data="global_app_data"
    global_app_data_dirname="dirname"
    class os_:
        environ=dict()
        class path:
            class expandvars:
                @staticmethod
                def __call__(arg1):
                    if arg1 == '%APPDATA%':
                        return global_app_data
                    return arg1
            @staticmethod
            def join(arg1,arg2):
                return global_app_data_dirname
    class Path:
        @staticmethod
        def home():
            return home_dir

# Generated at 2022-06-13 21:31:27.621648
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config = BaseConfigDict('temp.config')
    config.ensure_directory()
    assert os.path.exists('temp.config')
    os.remove('temp.config')


# Generated at 2022-06-13 21:31:44.259144
# Unit test for function get_default_config_dir
def test_get_default_config_dir():

    # Default path
    assert get_default_config_dir() == Path.home() / Path('.config') / 'httpie'

    # Legacy path
    legacy_path = Path.home() / Path('.httpie')
    os.makedirs(legacy_path)
    assert get_default_config_dir() == legacy_path

    # Explicit XDG path
    xdg_config = Path.home() / Path('.config') / 'httpiedir'
    os.environ['XDG_CONFIG_HOME'] = str(xdg_config.parent)
    assert get_default_config_dir() == xdg_config

    # Explicit HTTPIE path
    os.environ['HTTPIE_CONFIG_DIR'] = str(xdg_config)
    assert get_default_config_dir() == xd

# Generated at 2022-06-13 21:31:52.498234
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    os.environ['XDG_CONFIG_HOME'] = '/foo'
    os.environ['HTTPIE_CONFIG_DIR'] = '/bar'
    assert get_default_config_dir() == '/bar'
    del os.environ['HTTPIE_CONFIG_DIR']
    assert get_default_config_dir() == '/foo/httpie'
    del os.environ['XDG_CONFIG_HOME']
    assert get_default_config_dir() == str(Path.home() / '.config/httpie')

# Generated at 2022-06-13 21:32:02.967466
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    import pytest
    from httpie.plugins import DEFAULT_PLUGINS
    import json
    import requests

    test_config_template = '{{"__meta__":{{"httpie":"{httpie_version}"}}}}'
    test_config_str = test_config_template.format(httpie_version=__version__)
    test_config_dict = json.loads(test_config_str)
    test_config_dict['__meta__']['help'] = 'https://httpie.org/'
    test_config_dict['__meta__']['about'] = 'https://github.com/jakubroztocil/httpie'
    test_config_dict['__meta__']['plugins'] = DEFAULT_PLUGINS

    test_server_host = '127.0.0.1'

# Generated at 2022-06-13 21:32:13.150298
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    from tempfile import TemporaryDirectory
    with TemporaryDirectory() as temp_dir:
        test_json_file = Path(temp_dir) / BaseConfigDict.FILENAME
        if test_json_file.exists():
            test_json_file.unlink()

        test_config_dict = BaseConfigDict(path=test_json_file)
        test_config_dict.save()

        assert test_json_file.exists()
        assert test_json_file.read_text() == """\
{
    "__meta__": {
        "httpie": "%(httpie_version)s"
    }
}
""" % {'httpie_version': __version__} % {'httpie_version': __version__}



# Generated at 2022-06-13 21:32:18.236812
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    # Instanciate a class BaseConfigDict
    config_class = BaseConfigDict(path='./test')
    # Save the file
    config_class.save()
    # Delete the file after testing
    config_class.delete()

# Generated at 2022-06-13 21:32:37.592835
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    """
    Test that the configuration directory is created if it doesn't exist.
    """
    from tempfile import TemporaryDirectory
    from unittest import TestCase, main

    class _InheritedClass(BaseConfigDict):
        pass

    class BaseConfigDictTestCase(TestCase):
        def test_new_config_dir_is_created(self):
            with TemporaryDirectory() as tmp_dir:
                tmp_dir = Path(tmp_dir)
                config_dir = tmp_dir / DEFAULT_CONFIG_DIRNAME
                obj = _InheritedClass(path=config_dir / 'mock.json')
                self.assertFalse(config_dir.is_dir())
                obj.ensure_directory()
                self.assertTrue(config_dir.is_dir())

    main()



# Generated at 2022-06-13 21:32:48.046021
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    def _test_get_default_config_dir(
            xdg_config_home: str,
            home_dir: Path,
            expected_config_dir: Path) -> None:
        os.environ[ENV_XDG_CONFIG_HOME] = xdg_config_home
        home_dir_str = str(home_dir)
        home_dir_str_lower = home_dir_str.lower()

# Generated at 2022-06-13 21:33:00.646598
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    xdg_config_dir = Path('.config/httpie')
    old_xdg_config_dir = Path('.config/httpie')
    old_httpie_config_dir = Path('.httpie')

    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    os.environ.pop(ENV_XDG_CONFIG_HOME, None)

    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
    else:
        if (old_httpie_config_dir).exists():
            assert get_default_config_dir() == old_httpie_config_dir
        elif (xdg_config_dir).exists():
            assert get_default_config_dir() == xdg_config_

# Generated at 2022-06-13 21:33:06.247754
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    print("I am running BaseConfigDict_ensure_directory test!")
    config_dict = BaseConfigDict("test.json")
    config_dict.ensure_directory()


# Generated at 2022-06-13 21:33:17.673322
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    test_config = BaseConfigDict(path='httpie.config')
    try:
        test_config.save()
    except:
        try:
            test_config.delete()
            assert False
        except:
            assert False
    test_config.delete()
    try:
        test_config.save(fail_silently=True)
    except:
        assert False
    test_config['test'] = 'test'
    try:
        test_config.save()
    except:
        assert False
    test_config.delete()
    try:
        test_config.save(fail_silently=True)
    except:
        assert False
    test_config['test_list'] = []
    try:
        test_config.save()
    except:
        assert False
    test_config.delete()

# Generated at 2022-06-13 21:33:19.941161
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() / '.config' / 'httpie'

# Generated at 2022-06-13 21:33:34.834208
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # 1. explicitly set through env
    modify_env(env_config_dir='/tmp/HTTPIE_CONFIG_DIR')
    assert get_default_config_dir() == Path('/tmp/HTTPIE_CONFIG_DIR')
    reset_env()

    # 2. Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
    else:
        # reset
        reset_httpie_home_dir()
        reset_xdg_config_home_dir()

        # 3. legacy ~/.httpie
        mk_httpie_home_dir()
        assert get_default_config_dir() == Path('.httpie')
        rmtree('.httpie')

        # 4. XDG
        # 4.1. explicit

# Generated at 2022-06-13 21:33:39.187533
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config_dir = Path('test_config')
    assert (not config_dir.exists())
    test_config = BaseConfigDict(path=config_dir / 'test.json')
    test_config.save()
    assert (config_dir.exists())
    assert (config_dir / 'test.json').exists()
    test_config.delete()
    config_dir.rmdir()

# Generated at 2022-06-13 21:33:53.782294
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # default_config_dir
    env = os.environ.get(ENV_HTTPIE_CONFIG_DIR, False)
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR, (
            "get_default_config_dir should return "
            f"{DEFAULT_CONFIG_DIR} when {ENV_HTTPIE_CONFIG_DIR} is not set")
    # existing config_dir
    os.environ["TEST_HTTPIE_CONFIG_DIR"] = str(Path(os.getcwd()) / "test_hc")

# Generated at 2022-06-13 21:34:01.095044
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    import tempfile
    tempdir = Path(tempfile.gettempdir())
    testfile = tempdir / 'testfile.txt'
    testfile.touch()
    testfile.unlink()
    testdir = tempdir / 'testdir'
    testdir.mkdir(mode = 0o700)
    config = BaseConfigDict(path=testfile)
    with pytest.raises(ConfigFileError) as excinfo:
        config.ensure_directory()
    os.rmdir(testdir)
    assert "No such file or directory" in str(excinfo.value)


# Generated at 2022-06-13 21:34:17.460130
# Unit test for function get_default_config_dir
def test_get_default_config_dir():

    # 1. explicitly set through env
    def test_httpie_config():
        os.environ[ENV_HTTPIE_CONFIG_DIR] = '/foo/bar'
        expected = '/foo/bar'
        assert expected == get_default_config_dir()
        del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # 2. Windows
    def test_windows():
        os.name = 'nt'
        expected = DEFAULT_WINDOWS_CONFIG_DIR
        assert expected == get_default_config_dir()
        del os.name

    # 3. legacy ~/.httpie
    def test_legacy_config_dir():
        legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR

# Generated at 2022-06-13 21:34:19.148727
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path.home() / '.config' / 'httpie'



# Generated at 2022-06-13 21:34:24.925744
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    path_test = Path('test.json')
    config_test = BaseConfigDict(path=path_test)
    config_test['key'] = 'value'
    config_test.save()
    # test if the file created
    assert(os.path.isfile(path_test))
    # test if the content is correct
    assert(Path('test.json').read_text(encoding='utf8') == '{\n    "key": "value",\n    "__meta__": {\n        "httpie": "1.0.3"\n    }\n}')


# Generated at 2022-06-13 21:34:29.827742
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    f = open("test.json","w")
    f.write("""{
  "abc": "def"
}""")
    f.close()
    d = BaseConfigDict("test.json")
    d.load()
    assert("def" == d["abc"])

# Generated at 2022-06-13 21:34:37.566594
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Test case:
    # 0. Windows
    # 1. explicitly set through env
    # 2. legacy ~/.httpie
    # 3. XDG

    # case 0
    # Set the config directory explicitly through environment variable
    os.environ[ENV_HTTPIE_CONFIG_DIR] = str(Path('configdir'))
    assert get_default_config_dir() == Path('configdir')

    # case 1
    # Set the config directory explicitly through environment variable
    if is_windows:
        os.environ[ENV_HTTPIE_CONFIG_DIR] = str(Path('configdir'))
        assert get_default_config_dir() == Path('configdir')
        del os.environ[ENV_HTTPIE_CONFIG_DIR]
        return
    
    # case 2
    # Set 'HOME'

# Generated at 2022-06-13 21:34:46.981091
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # prepare for the test environment
    config_data = {
        'a':'b',
        'c':'d'
        }
    config_data_file = open('config.json','w')
    config_data_file.write(json.dumps(config_data))
    config_data_file.close()
    os.mkdir('config')
    os.mkdir('.config')
    os.mkdir('config/httpie')
    os.mkdir('.config/httpie')
    os.mkdir('.httpie')
    os.mkdir('httpie')
    os.mkdir('httpie/config')
    os.rename('config.json','.config/httpie/config.json')
    os.rename('config.json','.httpie/config.json')
    # test

# Generated at 2022-06-13 21:34:53.094179
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    test_config_dict = BaseConfigDict(Path('./test/test_config_dict.json'))
    try:
        test_config_dict.load()
    except ConfigFileError as e:
        print(e)
        return False
    except FileNotFoundError:
        return True


# Generated at 2022-06-13 21:35:00.042029
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    tmp_dir = Path('/tmp/httpie')
    tmp_file = tmp_dir / 'tmp.json'
    try:
        tmp_file.parent.mkdir(mode=0o700, parents=True)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    class test(BaseConfigDict):
        def __init__(self, path: Path):
            super().__init__(path)

    test_case = test(tmp_file)
    test_case.ensure_directory()
    assert test_case.path.parent.exists()
    assert test_case.path.parent.is_dir()


# Generated at 2022-06-13 21:35:08.956941
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # with $XDG_CONFIG_HOME
    os.environ[ENV_XDG_CONFIG_HOME] = '/home/moo/.xdg'
    assert '/home/moo/.xdg/httpie' == get_default_config_dir()
    del os.environ[ENV_XDG_CONFIG_HOME]
    # without $XDG_CONFIG_HOME
    assert '/home/moo/.config/httpie' == get_default_config_dir()

# Generated at 2022-06-13 21:35:15.339112
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import time

    a = BaseConfigDict(Path('/tmp/httpie_test.json'))
    a['x'] = time.time()
    a['y'] = [1, 2, 3]
    a.save()
    b = BaseConfigDict(Path('/tmp/httpie_test.json'))
    b.load()
    assert a==b

# Generated at 2022-06-13 21:35:23.578129
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config_dict = BaseConfigDict('./')

if __name__ == '__main__':
    test_BaseConfigDict_load()

# Generated at 2022-06-13 21:35:27.532738
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert str(get_default_config_dir()) == Path.home() / '.config' / 'httpie'
    assert str(get_default_config_dir()) == str(DEFAULT_CONFIG_DIR)

# Generated at 2022-06-13 21:35:37.104799
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    path = Path.home() / "test_load.json"
    string = '[1,2,3,4,5]'
    path.write_text(string)
    obj = BaseConfigDict(path)
    assert obj.load() == None
    assert obj == [1, 2, 3, 4, 5]
    # check the invalid json file
    path.write_text('[1, 2, 3]')
    try:
        obj.load()
    except Exception as e:
        assert isinstance(e, ConfigFileError)
        assert str(e) == 'invalid baseconfigdict file: Extra data: line 1 column 8 (char 8) [%s]' % str(path)
    path.unlink()

# Generated at 2022-06-13 21:35:44.415945
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import os
    import shutil
    import tempfile
    import unittest

    test = unittest.TestCase()
    print("Method save of class BaseConfigDict")
    path = Path('test.json')
    if path.exists():
        path.unlink()
    path.parent.mkdir(mode=0o700, parents=True)
    with path.open('wt') as f:
        f.write("{'test' : 'test'}")
    config = BaseConfigDict(path)
    config.ensure_directory()
    test.assertTrue(config.is_new())
    config.load()
    config.save()
    test.assertFalse(config.is_new())
    print("[OK] test baseconfigdict")


# Generated at 2022-06-13 21:35:47.291569
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path('%APPDATA%\\httpie')

# Generated at 2022-06-13 21:35:52.064912
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    aa = BaseConfigDict('./httpiehttpie')
    aa.ensure_directory()
    #print(aa.path)


# Generated at 2022-06-13 21:35:53.498623
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:36:01.966159
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    # when
    file_name = ".test_config.json"
    config_path = DEFAULT_CONFIG_DIR / file_name 
    config = BaseConfigDict(path=config_path)
    config['key1'] = 'value1'
    config.save()
    # then
    assert config_path.is_file()
    with config_path.open('rt') as f:
        data = json.load(f)
        assert data['key1'] == config['key1']
    # cleanup
    config_path.unlink()



# Generated at 2022-06-13 21:36:12.953219
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    try:
        dir_path = Path(str(Path.home()) + '/.httpie/test_directory')
        os.mkdir(dir_path)
    except FileExistsError:
        pass
    finally:
        dir_path = Path(str(Path.home()) + '/.httpie/test_directory/config.json')
        base = BaseConfigDict(dir_path)
        base.ensure_directory()
        assert dir_path.parent.exists() is True
        assert str(dir_path.parent) == str(Path.home() + '/.httpie/test_directory')
        os.rmdir(str(Path.home()) + '/.httpie/test_directory')


# Generated at 2022-06-13 21:36:23.455448
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config = BaseConfigDict(Path('my_config.txt'))
    config.save()

    # test that file exists and the correct data was written to it
    with open('my_config.txt') as f:
        assert f.read() == '{"__meta__": {"httpie": "1.0.2"}}'

    # clean up test
    Path('my_config.txt').unlink()



# Generated at 2022-06-13 21:36:38.893453
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class MyConfig(BaseConfigDict):
        name = 'my config'
        helpurl = 'https://example.com/my-config'
        about = 'my config is for humans'

    config = MyConfig(path=Path('my-config.json'))
    config['x'] = 'y'
    config.save()
    assert 'x' in config
    config.delete()



# Generated at 2022-06-13 21:36:45.530807
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    class TestBaseConfigDict(BaseConfigDict):
        pass

    import tempfile

    with tempfile.TemporaryDirectory() as temp_dir:
        json_file_path = Path(temp_dir) / 'config' / 'test.json'

        # Case 1: no exception
        temp_config = TestBaseConfigDict(json_file_path)
        temp_config.save()

        # Case 2: update json file, no exception
        temp_config.update({'item': 'value'})
        temp_config.save()



# Generated at 2022-06-13 21:36:55.061936
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():

    class TestConfig(BaseConfigDict):
        FILENAME = 'test_config.json'
        DEFAULTS = {
            'test_key': 'test_value',
        }

    directory = Path('./test_directory')
    config = TestConfig(directory=directory)


# Generated at 2022-06-13 21:37:02.519839
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    class BaseConfigDict_test(BaseConfigDict):
        pass
    test_config_directory = '/tmp/httpie/test_BaseConfigDict/config'
    base_config_dict = BaseConfigDict_test(
            path=Path(test_config_directory) / 'config.json')
    base_config_dict.ensure_directory()
    assert Path(test_config_directory).exists()

# Generated at 2022-06-13 21:37:07.757921
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    path = Path("test_dir")
    path.mkdir()
    config = BaseConfigDict(Path("test_dir/test.json"))
    config['test_config'] = "123"
    config.save()
    assert(Path("test_dir/test.json").read_text() == '{\n    "test_config": "123"\n}')
    path.rmdir()


# Generated at 2022-06-13 21:37:16.629366
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    test_config = BaseConfigDict("/tmp/test.json")
    test_config.ensure_directory()
    assert os.path.exists("/tmp")
    for old_file in os.listdir("/tmp"):
        if old_file != "test.json":
            os.unlink("/tmp/" + old_file)
    assert os.path.exists("/tmp/test.json")
    os.unlink("/tmp/test.json")


# Generated at 2022-06-13 21:37:27.728190
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path('.config/httpie')

    # 1. explicitly set through env
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/foo/bar'
    assert get_default_config_dir() == Path('/foo/bar')

    # 2. Windows
    is_windows_orig = is_windows
    try:
        is_windows = True
        assert get_default_config_dir() == Path('%APPDATA%/httpie')
    finally:
        is_windows = is_windows_orig

    # 3. legacy ~/.httpie
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        legacy_config_dir = tmpdir / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
        legacy_

# Generated at 2022-06-13 21:37:38.586972
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    with patch.dict(os.environ, {ENV_HTTPIE_CONFIG_DIR: '/abc/def'}):
        assert get_default_config_dir() == Path('/abc/def')

    with patch.dict(os.environ, {ENV_HTTPIE_CONFIG_DIR: ''}):
        assert get_default_config_dir() == os.path.join(Path.home(), '.httpie')

    with patch.dict(os.environ, {ENV_HTTPIE_CONFIG_DIR: '   '}):
        assert get_default_config_dir() == os.path.join(Path.home(), '.httpie')

    with patch.dict(os.environ, {ENV_XDG_CONFIG_HOME: '/'}):
        assert get_default_config_dir() == Path

# Generated at 2022-06-13 21:37:49.222585
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    import os
    import shutil


# Generated at 2022-06-13 21:37:54.916597
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    try:
        badConfig = BaseConfigDict(Path('.') / 'config.json')
        badConfig.load()
    except ConfigFileError:
        pass
    else:
        raise Exception('Should raise ConfigFileError for a bad JSON config file')



# Generated at 2022-06-13 21:38:12.237904
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    try:
        xdg_config_home_dir = Path(os.environ['XDG_CONFIG_HOME'])
        if 'HTTPIE_CONFIG_DIR' in os.environ:
            del os.environ['HTTPIE_CONFIG_DIR']
        assert get_default_config_dir() == xdg_config_home_dir / DEFAULT_CONFIG_DIRNAME
    except:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR


# Generated at 2022-06-13 21:38:19.797125
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '~/foo'
    assert get_default_config_dir() == Path.home() / 'foo'
    del os.environ[ENV_HTTPIE_CONFIG_DIR]
    os.environ[ENV_XDG_CONFIG_HOME] = '~/foo'
    assert get_default_config_dir() == Path.home() / 'foo' / DEFAULT_CONFIG_DIRNAME
    del os.environ[ENV_XDG_CONFIG_HOME]

# Generated at 2022-06-13 21:38:28.101762
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    with open(DEFAULT_CONFIG_DIR+"/config.json","w") as f:
        json.dump({"test":"test"},f)
    config = Config()
    config.load()
    assert config['test'] == 'test'
    os.remove(DEFAULT_CONFIG_DIR+"/config.json")


# Generated at 2022-06-13 21:38:33.118715
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config_dir = Path('/tmp/')
    config_json_file = config_dir / BaseConfigDict.FILENAME
    if config_json_file.exists():
        config_json_file.unlink()
    config_dict = BaseConfigDict(config_dir)
    if not config_dir.exists():
        config_dir.mkdir()
    config_dict.save()
    assert config_json_file.exists()



# Generated at 2022-06-13 21:38:39.376850
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    bcd = BaseConfigDict(path='/opt/httpie/' + 'config.json')
    try:
        bcd.ensure_directory()
        # assert False, "Exception was not thrown while calling ensure_directory method"
    except OSError as exc:
        assert exc.errno == errno.EEXIST, "Exception was thrown with wrong errno code"
    else:
        assert False, "Exception was not thrown while calling ensure_directory method"


# Generated at 2022-06-13 21:38:46.008841
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    dir_test = DEFAULT_CONFIG_DIR / 'test_BaseConfigDict_ensure_directory'
    if dir_test.exists():
        dir_test.unlink()
    obj_test = BaseConfigDict(dir_test)
    obj_test.ensure_directory()
    try:
        assert dir_test.exists()
    except AssertionError as e:
        raise e
    finally:
        dir_test.unlink()



# Generated at 2022-06-13 21:38:55.553079
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Test XDG - use first environment variable
    os.environ[ENV_XDG_CONFIG_HOME] = "/xdg_config"
    os.environ[ENV_HTTPIE_CONFIG_DIR] = "/httpie_config"
    default_xdg_config_dir = Path("/xdg_config") / DEFAULT_CONFIG_DIRNAME
    assert get_default_config_dir() == default_xdg_config_dir
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Test XDG - use XDG_CONFIG_HOME as default
    del os.environ[ENV_XDG_CONFIG_HOME]
    default_xdg_config_dir = Path.home() / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_

# Generated at 2022-06-13 21:39:08.065166
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # NOTE: this function only tests for Unix-like OSs since
    # DEFAULT_WINDOWS_CONFIG_DIR is not configurable and is
    # only dependent on the system.
    env = os.environ
    # Test for (1) explicit setting through environment
    try:
        env[ENV_HTTPIE_CONFIG_DIR] = '/foo'
        assert get_default_config_dir() == Path('/foo')
    finally:
        del env[ENV_HTTPIE_CONFIG_DIR]

    # Test for (5.1), (5.2), and (3) through simulating
    # presence of legacy ~/.httpie config
    #
    # First, create legacy config file at ~/.httpie
    legacy_config_dir = Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
   

# Generated at 2022-06-13 21:39:11.466442
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config_path = Path('test_httpie_config/config.json')
    BaseConfigDict(config_path).ensure_directory()
    assert config_path.parent.exists()


# Generated at 2022-06-13 21:39:14.417271
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)

    assert get_default_config_dir() == DEFAULT_CONFIG_DIR

    os.environ[ENV_HTTPIE_CONFIG_DIR] = str(Path.home())
    assert get_default_config_dir() == Path.home()

# Generated at 2022-06-13 21:39:33.003279
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR
        return

    home_dir = Path.home()
    default_config_dir = get_default_config_dir()

   # 1. test correct return value when explicitly set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = str(home_dir)
    assert get_default_config_dir() == home_dir
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

   # 2. test correct return value when XDG_CONFIG_HOME is explicitly set
    xdg_config_home_dir = home_dir / DEFAULT_RELATIVE_XDG_CONFIG_HOME

# Generated at 2022-06-13 21:39:37.128349
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config_dir = Path('~/.httpie').expanduser()
    config_dir.mkdir(parents=True, exist_ok=True)
    config_dir.chmod(0o700)
    config_file = config_dir / 'config.json'
    config = Config()
    config.save()
    with config_file.open() as f:
        assert f.read().strip() == '{\n    "__meta__": {\n        "httpie": "2.2.0"\n    }\n}'