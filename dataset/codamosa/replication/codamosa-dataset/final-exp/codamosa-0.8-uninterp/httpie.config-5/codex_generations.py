

# Generated at 2022-06-13 21:30:02.373643
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    from httpie.config import BaseConfigDict, ConfigFileError
    from httpie.compat import is_windows
    from pathlib import Path
    try:
        os.environ[ENV_HTTPIE_CONFIG_DIR] = ''
        os.environ[ENV_XDG_CONFIG_HOME] = ''
    except KeyError:
        pass
    
    class TestConfigDict(BaseConfigDict):
        name = None
        helpurl = None
        about = None
    
    file = TestConfigDict(Path(DEFAULT_CONFIG_DIR) / TestConfigDict.FILENAME)
    file.load()
    
    assert file == {}
    
    file = TestConfigDict(Path('/home/user/.config/httpie/config.json'))
    file.load()


# Generated at 2022-06-13 21:30:10.415839
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    # test for new file
    d = BaseConfigDict('./test.json')
    assert d.is_new()
    d['hello'] = 'world'
    d['httpie'] = __version__
    d['about'] = 'test'
    d['helpurl'] = 'www.example.com'
    d.save()
    d2 = BaseConfigDict('./test.json')
    d2.load()
    assert not d2.is_new()
    assert d == d2

    # test for non-exist file
    d3 = BaseConfigDict('./test2.json')
    try:
        d3.load()
    except ConfigFileError:
        assert True
    else:
        assert False

    # test for invalid json format

# Generated at 2022-06-13 21:30:14.012336
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    BASE_PATH = os.path.dirname(__file__)
    file_path = os.path.join(BASE_PATH, 'test_config.json')
    baseConfigDict = BaseConfigDict(file_path)
    baseConfigDict.load()
    # return the result in a list
    return list(baseConfigDict.values())


# Generated at 2022-06-13 21:30:23.253385
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    # Prepare
    test_config_dict = BaseConfigDict('~/.httpie/config.json')
    # Run
    test_config_dict.save(fail_silently=True)
    # Verify
    assert not os.path.exists(os.path.expanduser(
        test_config_dict.path)) or os.path.exists(os.path.expanduser(
        test_config_dict.path))
    # Cleanup
    # Nothing to do, it's just a test



# Generated at 2022-06-13 21:30:33.017823
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    import json
    import random
    import os
    import string
    import tempfile
    import uuid
    
    dirpath = tempfile.mkdtemp()
    filepath = dirpath + '/baseConfigDict_load.json'
    fp = open(filepath, 'w')
    data = {
        'foo': random.choice(string.ascii_letters) + str(uuid.uuid4()),
        'bar': random.choice(string.ascii_letters) + str(uuid.uuid4())
    }
    json.dump(data, fp)
    fp.close()
    config = BaseConfigDict(filepath)
    config.load()
    assert data == config
    os.remove(filepath)
    os.rmdir(dirpath)

# Unit

# Generated at 2022-06-13 21:30:41.162612
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    class test(BaseConfigDict):
        def __init__(self, path:Path):
            super().__init__(path)

    print("\n======Test ensure_directory======")
    test(Path('/tmp/test')).ensure_directory()
    print(os.path.exists('/tmp/test'))

    test(Path('/tmp/test/test')).ensure_directory()
    print(os.path.exists('/tmp/test/test'))


# Generated at 2022-06-13 21:30:50.920150
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    def get_path():
        return get_default_config_dir()

    # Basic
    assert get_path() == Path.home() / '.config' / 'httpie'

    # Legacy default ~/.httpie
    os.environ[ENV_HTTPIE_CONFIG_DIR] = ''
    os.environ[ENV_XDG_CONFIG_HOME] = ''
    assert get_path() == Path.home() / '.httpie'

    # Windows
    os.environ[ENV_HTTPIE_CONFIG_DIR] = ''
    os.environ[ENV_XDG_CONFIG_HOME] = ''
    del os.environ['APPDATA']  # Windows
    os.environ['APPDATA'] = '/foo/AppData/Roaming'

# Generated at 2022-06-13 21:31:02.940391
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # Test case 1:
    # 1. If the environment variable HTTPIE_CONFIG_DIR is set,
    #    the configuration directory is the one specified by environment variable
    # 2. If it's Windows, the configuration directory is the path returned by expanding %APPDATA%
    # 3. If the ~/.httpie directory exists, the configuration directory is ~/.httpie
    # 4. Otherwise, it's $XDG_CONFIG_HOME/.httpie
    # 5. If both $XDG_CONFIG_HOME and HTTPIE_CONFIG_DIR are not set,
    #    the configuration directory is ~/.config/.httpie
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/home/httpie'
    assert get_default_config_dir() == Path('/home/httpie')

# Generated at 2022-06-13 21:31:18.330457
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    """
    Unit test for function get_default_config_dir
    """
    home_dir = str(Path.home())
    default_relative_xdg_config_home = str(DEFAULT_RELATIVE_XDG_CONFIG_HOME)
    default_xdg_config_home = os.path.join(home_dir, default_relative_xdg_config_home)

    env_xdg_config_home = os.path.join(home_dir, 'env_xdg_config_home')

    current_os = os.name

    # 1. explicitly set through env
    os.environ[ENV_HTTPIE_CONFIG_DIR] = env_xdg_config_home
    assert get_default_config_dir() == env_xdg_config_home

# Generated at 2022-06-13 21:31:30.943836
# Unit test for function get_default_config_dir
def test_get_default_config_dir():

    # 1. explicitly set through env
    # 1.1 $HTTPIE_CONFIG_DIR is set
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/path/to/config'
    assert get_default_config_dir() == Path('/path/to/config')
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # 2. Windows
    # 2.1 $HTTPIE_CONFIG_DIR is not set
    # 2.2 platform is Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

    # 3. legacy ~/.httpie
    # 3.1 $HTTPIE_CONFIG_DIR is not set
    # 3.2 platform is not Windows
    # 3.3 ~/.httpie exists
    home

# Generated at 2022-06-13 21:31:47.570259
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config_dir_path = Path('test_config_dir')
    config_dir_path.mkdir()
    config_path = Path(config_dir_path / 'test_config.json')
    with config_path.open('w') as config_file:
        json.dump({"version": "1.0", "data": "test_data"}, config_file)
    config = BaseConfigDict(path=config_path)
    assert config == {}
    config.load()
    assert config["version"] == "1.0"
    assert config["data"] == "test_data"
    config_path.unlink()
    config_dir_path.rmdir()
    

# Generated at 2022-06-13 21:31:57.045572
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    assert get_default_config_dir() == Path.home() / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR

    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/tmp/custom/config/dir'
    assert get_default_config_dir() == Path('/tmp/custom/config/dir')

    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/tmp/custom/config/file'
    assert get_default_config_dir() == Path('/tmp/custom/config')

    os.environ[ENV_XDG_CONFIG_HOME] = '/tmp/xdg/config/home'

# Generated at 2022-06-13 21:32:04.567059
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    f = open("test.json", "w+")
    f.write('{\n')
    f.write('    "favorite_color": "red",\n')
    f.write('    "favorite_number": 42,\n')
    f.write('    "favorite_foods": [\n')
    f.write('        "pizza",\n')
    f.write('        "cheeseburgers"\n')
    f.write('    ]\n')
    f.write('}\n')
    f.close()

    import sys
    sys.path.append('../')  # add httpie module to path
    from httpie.config import BaseConfigDict

    config = BaseConfigDict("test.json")
    config.load()
    print(config)


# Generated at 2022-06-13 21:32:17.108988
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import os
    import tempfile
    tmpdir = tempfile.mkdtemp()
    try:
        os.environ.pop(ENV_XDG_CONFIG_HOME, None)
        os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
        assert get_default_config_dir() == Path.home() / DEFAULT_RELATIVE_XDG_CONFIG_HOME / DEFAULT_CONFIG_DIRNAME

        os.environ[ENV_XDG_CONFIG_HOME] = tmpdir
        assert get_default_config_dir() == Path(tmpdir) / DEFAULT_CONFIG_DIRNAME

    finally:
        os.environ.pop(ENV_XDG_CONFIG_HOME, None)

# Generated at 2022-06-13 21:32:24.380372
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    # input:
    #   string
    # output:
    #   dictionary
    # expected:
    #   dictionary
    filename = 'foo'
    c = BaseConfigDict(path=Path(filename))
    p = Path(filename)
    dic = {'foo': 'bar'}
    with open(filename, 'w') as f:
        json.dump(dic, f)
    try:
        c.load()
    finally:
        os.remove(filename)
    assert c == dic
    

# Generated at 2022-06-13 21:32:31.792496
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config_dict = BaseConfigDict(path=Path("test_config_file.json"))
    config_dict.ensure_directory()
    assert Path("test_config_file.json").parent.exists()


# Generated at 2022-06-13 21:32:45.538103
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)
    os.environ.pop(ENV_XDG_CONFIG_HOME, None)

    def get_default_config_dir():
        return get_default_config_dir()

    httpie_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    xdg_config_home_dir = os.environ.get(ENV_XDG_CONFIG_HOME)
    home_dir = Path.home()

    # $HTTPIE_CONFIG_DIR
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/explicit'
    assert get_default_config_dir() == Path('/explicit')

    # Windows

# Generated at 2022-06-13 21:32:54.555002
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path(os.getenv('HOME')) / '.config' / 'httpie'
    os.environ[ENV_XDG_CONFIG_HOME] = '/tmp/config'
    assert get_default_config_dir() == Path('/tmp/config') / 'httpie'
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/tmp/httpie-config'
    assert get_default_config_dir() == Path('/tmp/httpie-config')

# Generated at 2022-06-13 21:33:00.189117
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    assert BaseConfigDict(Path("./test/file_not_exists")).load() == None
    c = BaseConfigDict(Path("./test/sample.config"))
    c.load()
    assert c['a'] == 1
    assert c['b'] == {'b1': 'bbb', 'b2': [1, 2, 3]}

# Generated at 2022-06-13 21:33:14.118983
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    import pytest
    from .utils import TESTS_ROOT

    temp_dir = TESTS_ROOT / "temp_config"
    # test: ensure_directory does not raise exception when the directory already exists
    temp_dir.mkdir()
    parent_dir = temp_dir / "parent_dir"
    child_dir = parent_dir / "child_dir"
    temp_config = BaseConfigDict(path=child_dir / "file.txt")
    temp_config.ensure_directory()
    # test: ensure_directory creates the parent directory when the parent directory does not exist
    parent_dir.unlink()
    temp_config.ensure_directory()
    with pytest.raises(FileNotFoundError, match=fr"No such file or directory: '{parent_dir}'"):
        parent_dir

# Generated at 2022-06-13 21:33:23.151491
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    p = Path('testing_base.json')
    test = BaseConfigDict(path=p)
    test.load()


# Generated at 2022-06-13 21:33:25.767288
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    assert get_default_config_dir() == Path('.config') / 'httpie'


# Generated at 2022-06-13 21:33:36.678377
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    import uuid
    from tempfile import gettempdir
    from httpie.config import get_default_config_dir, Path

    class DummyEnviron():
        def __init__(self, test_name, xdg_config_home_dir, tmpdir):
            self.test_name = test_name
            self.xdg_config_home_dir = xdg_config_home_dir
            self.tmpdir = tmpdir

        def __getitem__(self, key):
            if key in {'HOME', 'USERPROFILE'}:
                return str(self.xdg_config_home_dir)
            if key in {ENV_XDG_CONFIG_HOME, 'XDG_CONFIG_DIRS'}:
                return str(self.tmpdir)
            else:
                raise KeyError()

# Generated at 2022-06-13 21:33:50.241506
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    config_dir1 = get_default_config_dir()
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/tmp/x/y'
    config_dir2 = get_default_config_dir()
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '' # reset to empty
    config_dir3 = get_default_config_dir()
    del os.environ[ENV_HTTPIE_CONFIG_DIR] # recover
    assert config_dir1 == Path('/tmp/x/y')
    assert config_dir2 == Path('/tmp/x/y')
    assert config_dir3 != Path('/tmp/x/y')
    assert config_dir3 == DEFAULT_CONFIG_DIR

# Generated at 2022-06-13 21:34:01.540752
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    def _assert_dir_eq(dirpath1, dirpath2):
        dirpath1 = os.path.realpath(dirpath1)
        dirpath2 = os.path.realpath(dirpath2)
        assert dirpath1 == dirpath2

    # Explicit
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/my/config/dir'
    assert '/my/config/dir' == get_default_config_dir()
    del os.environ[ENV_HTTPIE_CONFIG_DIR]

    # Windows
    if not is_windows:
        return

    xdg_dir = 'C:\\Users\\Test\\AppData\\Roaming'

# Generated at 2022-06-13 21:34:04.742880
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    c = BaseConfigDict(Path('/test_dir'))
    assert not c.path.exists()

    c.ensure_directory()
    assert c.path.exists()



# Generated at 2022-06-13 21:34:09.206320
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    newConfig = BaseConfigDict("../json/config.json")
    newConfig.load()
    assert newConfig["default_options"] == []
    assert newConfig.__class__.__name__.lower() == "config"


# Generated at 2022-06-13 21:34:11.255707
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config = Config()
    assert config.directory.exists()
    config.ensure_directory()
    assert config.path.exists()

# Generated at 2022-06-13 21:34:20.548033
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    from httpie import ExitStatus
    from httpie.config import BaseConfigDict
    from httpie.cli import parser
    args = parser.parse_args(['--auth=test:test', '--verbose',
                              'https://httpie.org/hello'])
    args = parser.parse_args(['--auth=test:test', '--verbose', args.url])
    args.output_dir = './tests/temp'
    interactive_config_dict = BaseConfigDict(args.output_dir)
    assert os.path.exists(args.output_dir), "Failed to create directory"
    return ExitStatus.OK

# Generated at 2022-06-13 21:34:25.988535
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
    orig_home = Path.home()
    home = orig_home
    legacy_config_dir = home / DEFAULT_RELATIVE_LEGACY_CONFIG_DIR
    legacy_config_dir.mkdir(parents=True, mode=0o700)

# Generated at 2022-06-13 21:34:44.227382
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    # Create a config file at that path in the current directory
    config_path = Path('./httpie_config.json')
    if config_path.exists():
        config_path.unlink()
    test_config = {
        'default_options': []
    }
    json_string = json.dumps(
        obj=test_config,
        indent=4,
        sort_keys=True,
        ensure_ascii=True,
    )
    config_path.write_text(json_string + '\n')

    # Create an object of Config, and load the config file
    config = Config(directory=Path('.'))
    config.load()
    config.save()

    # Now the config file should be loaded with the configs in the file
    # and the direcotry to store the config file

# Generated at 2022-06-13 21:34:49.721967
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    path = DEFAULT_CONFIG_DIR / 'config.json'
    b = BaseConfigDict(path)
    assert(b.is_new() == True)
    assert(b.load() == {})


# Generated at 2022-06-13 21:34:58.809874
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config_file_name = 'config.json'
    file_path = Path(config_file_name)
    dir_path = Path('.')

    config_dict = BaseConfigDict(path=file_path)
    try:
        config_dict.load()
    except ConfigFileError as e:
        print(e)
    print(config_dict)

    config_dict = Config(directory=dir_path)
    try:
        config_dict.load()
    except ConfigFileError as e:
        print(e)
    print(config_dict)

    config_dict = Config()
    try:
        config_dict.load()
    except ConfigFileError as e:
        print(e)
    print(config_dict)


# Generated at 2022-06-13 21:35:10.851093
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    env_config_dir = os.environ.get(ENV_HTTPIE_CONFIG_DIR)
    xdg_config_home = os.environ.get(ENV_XDG_CONFIG_HOME)

    # explicitly set through env
    # os.environ[ENV_HTTPIE_CONFIG_DIR] = os.path.expanduser('~')
    assert get_default_config_dir() == Path.home()
    # os.environ[ENV_HTTPIE_CONFIG_DIR] = None
    os.environ.pop(ENV_HTTPIE_CONFIG_DIR, None)

    # Windows
    if is_windows:
        assert get_default_config_dir() == DEFAULT_WINDOWS_CONFIG_DIR

# Generated at 2022-06-13 21:35:20.744341
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import os
    import tempfile

    config_dir = tempfile.TemporaryDirectory()
    if is_windows:
        # config_dir.name is bytes, but we want to use a str path.
        config_dir_name = config_dir.name.decode()
    else:
        config_dir_name = config_dir.name

    class DummyDict(BaseConfigDict):
        def __init__(self):
            super().__init__(
                path=Path(config_dir_name) / 'foo.json')

    # Ensure the directory exists before we save a file.
    dummy = DummyDict()
    dummy.save()

    dummy['foo'] = 'bar'
    dummy.save()

# Generated at 2022-06-13 21:35:33.903443
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    from contextlib import redirect_stdout
    from io import StringIO

    class mock_BaseConfigDict(BaseConfigDict):
        def __init__(self):
            self.path = ""
            self.directory = ""

    # 1. file does not exist -> no error
    mock_config = mock_BaseConfigDict()
    print(mock_config.load())

    # 2. invalid json file -> raise exception
    mock_config.path = 'mock_path'
    try:
        mock_config.load()
    except ConfigFileError:
        pass
    # 2.1 print error message
    error_message = StringIO()
    with redirect_stdout(error_message):
        try:
            mock_config.load()
        except ConfigFileError:
            pass
        output = error_message.getvalue

# Generated at 2022-06-13 21:35:41.712413
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    directory = "Users"
    file_name = "config.json"
    path = Path(directory) / file_name
    config = BaseConfigDict(path)
    config['default_options'] = [{'--form': 'ewogICAgImJhciI6ICJiYXoiCn0='}]
    config.save()
    config.load()
    assert config == {'default_options': [{'--form': 'ewogICAgImJhciI6ICJiYXoiCn0='}]}


# Generated at 2022-06-13 21:35:51.729709
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    # Create a temporary file to store config data and change directory to it
    cwd = Path.cwd()
    tempdir = Path(os.environ['TEMP'])
    print (cwd)
    print (tempdir)
    os.chdir(tempdir)

    # Create a BaseConfigDict object
    config = BaseConfigDict('httpie.json')
    config.load()

    # Try to save a new config file and load it
    config['default_options'] = ['--json']
    config.save()
    config.load()

    # Test whether the config file is loaded correctly
    assert (config['default_options'] == ['--json'])

    # Remove the temporary file and restore the original working directory
    config.delete()
    os.chdir(cwd)

# Generated at 2022-06-13 21:35:53.601499
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config = BaseConfigDict(Path('sim_config.json'))
    config.load()



# Generated at 2022-06-13 21:35:55.980605
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config_file = Config()
    config_file.ensure_directory()

# Generated at 2022-06-13 21:36:09.410904
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    test_config_dict = BaseConfigDict(path="/test/config/path")
    test_config_dict.save()

# Generated at 2022-06-13 21:36:16.959806
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    from .utils import temp_directory

    with temp_directory(DEFAULT_CONFIG_DIRNAME) as tempdir:
        config = Config(tempdir)
        config.ensure_directory()
        assert config.path.parent.is_dir()

    with temp_directory(DEFAULT_CONFIG_DIRNAME) as tempdir:
        config = Config(tempdir)
        subdir = config.path.parent / "dir"
        config.path = subdir / "config.json"
        config.ensure_directory()
        assert subdir.is_dir()

# Generated at 2022-06-13 21:36:21.193955
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    config_dict = BaseConfigDict(Path('/tmp/httpie/config.json'))
    config_dict.load()
    assert config_dict == {}


# Generated at 2022-06-13 21:36:30.563701
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # Test case
    # Case 1: Case when the directory where the config file will be stored exists
    config_file_path = '/tmp/httpie/.config/httpie/config.json'
    os.makedirs('/tmp/httpie/.config/httpie')
    config = Config({'base':config_file_path})
    config.ensure_directory()
    assert_path = "/tmp/httpie/.config/httpie"
    assert_files = os.listdir(assert_path)
    assert_files.sort()
    assert assert_files == ['httpie']

    # Case 2: Case when the directory where the config file will be stored does not exist
    config_file_path = '/tmp/httpie/.config/httpie/config.json'
    config = Config({'base':config_file_path})
   

# Generated at 2022-06-13 21:36:33.820916
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    path_name = 'test.json'
    path = Path(path_name)
    path.touch()
    test_dict = BaseConfigDict(path=path)
    test_dict.load()
    assert test_dict.is_new()
    path.unlink()


# Generated at 2022-06-13 21:36:34.830289
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    config = Config()
    config.save()



# Generated at 2022-06-13 21:36:38.742459
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    s = BaseConfigDict(Path('.config/httpie/config.json'))
    # test save
    s.save()


# Generated at 2022-06-13 21:36:41.675810
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    from pprint import pprint
    pprint(vars(Config()))

if __name__ == '__main__':
    test_get_default_config_dir()

# Generated at 2022-06-13 21:36:43.637794
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    from importlib.machinery import SourceFileLoader
    config = SourceFileLoader('config', '/Users/xsheng/.httpie/config.json').load_module()
    config.load()


# Generated at 2022-06-13 21:36:52.525272
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    from tempfile import NamedTemporaryFile
    from unittest import mock

    from httpie.config import BaseConfigDict

    mock_json_load = mock.MagicMock()
    mock_json_load.return_value = {'test': 'value'}
    with mock.patch('json.load', mock_json_load):
        f = NamedTemporaryFile()
        d = BaseConfigDict(f.name)
        d.load()
    assert {'test': 'value'} == d


# Generated at 2022-06-13 21:37:10.056984
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    tmp_file = Path(__file__).parent / 'test_BaseConfigDict_save.json'
    if tmp_file.exists():
        tmp_file.unlink()

    data = {
        'foo': 'bar',
        'baz': ['qux', 'quxx']
    }
    config_dict = BaseConfigDict(tmp_file)
    config_dict.update(data)
    config_dict.save()
    assert tmp_file.exists()
    with tmp_file.open('rt') as f:
        assert json.load(f) == data

    tmp_file.unlink()

# Generated at 2022-06-13 21:37:22.936302
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    import os
    import json
    from pathlib import Path
    from httpie.config import DEFAULT_CONFIG_DIR, BaseConfigDict

    test_dir = Path('/tmp/httpie/config/BaseConfigDict')
    test_dir.mkdir(parents=True, exist_ok=True)
    os.environ[ENV_HTTPIE_CONFIG_DIR] = str(DEFAULT_CONFIG_DIR)

    # Check default_options
    test_file = test_dir / Config.FILENAME
    test_file.write_text('')
    config = Config(directory=test_dir)
    assert config.default_options == []
    test_file.unlink()

    # Check meta.httpie, meta.help and meta.about

# Generated at 2022-06-13 21:37:34.497404
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    global DEFAULT_CONFIG_DIR
    assert DEFAULT_CONFIG_DIR == Path.home() / Path('.config') / Path('httpie')
    DEFAULT_CONFIG_DIR.mkdir(mode=0o700, parents=True)
    tmp_path = Path('./tmp/test_directory')
    assert not tmp_path.exists()
    tmp_path.parent.mkdir(mode=0o700, parents=True)
    assert tmp_path.parent.exists()
    tmp_dict = BaseConfigDict(path=tmp_path)
    tmp_dict['foo'] = 'bar'
    tmp_dict.ensure_directory()
    assert tmp_path.parent.exists()
    tmp_path.parent.unlink()

# Generated at 2022-06-13 21:37:43.488018
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    import os
    #this part is to create folder 'test' in current working folder
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    path = Path('test')
    if os.path.exists(path):
        raise ConfigFileError('cannot create the test folder')
    else:
        path.mkdir()

    config = Config(path)
    config.save()

# Generated at 2022-06-13 21:37:47.398717
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    bad_path = os.path.dirname(os.path.abspath(__file__))
    c = BaseConfigDict(path=bad_path)
    try:
        c.load()
        assert False
    except ConfigFileError:
        assert True


# Generated at 2022-06-13 21:37:51.426238
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    print('Starting unit test for method save of class BaseConfigDict')
    config = Config()
    config.save()


if __name__ == '__main__':
    test_BaseConfigDict_save()

# Generated at 2022-06-13 21:38:00.056060
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    from httpie.environment import Environment
    from httpie.config import DEFAULT_CONFIG_DIR
    import re
    env = Environment()
    env.config.is_valid = True  # mock valid config
    env.config_dir = None
    assert get_default_config_dir() == DEFAULT_CONFIG_DIR
    xdg_config = 'testxdg'
    os.environ[ENV_XDG_CONFIG_HOME] = xdg_config
    assert re.match(xdg_config + '/httpie', str(get_default_config_dir()))

# Generated at 2022-06-13 21:38:11.387138
# Unit test for function get_default_config_dir
def test_get_default_config_dir():
    # first time run on linux
    assert(get_default_config_dir() == Path.home() / Path('.config') / DEFAULT_CONFIG_DIRNAME)
    # overwrite XDC_CONFIG_HOME
    os.environ[ENV_XDG_CONFIG_HOME] = '/some_other_path'
    assert(get_default_config_dir() == Path('/some_other_path') / DEFAULT_CONFIG_DIRNAME)
    # overwrite HTTPIE_CONFIG_DIR
    os.environ[ENV_HTTPIE_CONFIG_DIR] = '/some_config_dir'
    assert(get_default_config_dir() == Path('/some_config_dir'))

# Generated at 2022-06-13 21:38:17.953796
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    temp_dir = '/tmp/temp_dir'
    # Delete the directory if it exists
    try:
        os.rmdir(temp_dir)
    except OSError:
        pass
    test_file = ConfigFile(path=temp_dir + '/test.json')
    assert test_file.is_new() == True
    test_file.ensure_directory()
    assert test_file.is_new() == True
    os.rmdir(temp_dir)


# Generated at 2022-06-13 21:38:31.827899
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    import pytest
    from tempfile import TemporaryDirectory
    from pathlib import Path

    def get_config_path(directory):
        return Path(directory) / "config.json"

    with TemporaryDirectory() as tmp:
        config_file = tmp / 'config.json'
        config_file.unlink()
        config = BaseConfigDict(path=config_file)
        config.ensure_directory()
        assert get_config_path(config.path).exists()

    with TemporaryDirectory() as tmp:
        config_file = tmp / 'config.json'
        config_file.parent.chmod(0)
        config_file.unlink()
        config = BaseConfigDict(path=config_file)
        with pytest.raises(OSError):
            config.ensure_directory()

# Generated at 2022-06-13 21:39:06.936076
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    # Test Setup
    # Creating the directory structure
    config_dir = Path('config')
    config_dir.mkdir()
    auth_dir = Path('config') / 'auth'
    auth_dir.mkdir()

    config = Config()
    config.ensure_directory()

    # Creating directory structure for testing BaseConfigDict
    auth_config_dir = Path('config') / 'auth'
    auth_config_dir.mkdir()
    # Unit Test
    ac = AuthConfig(auth_config_dir)
    ac.ensure_directory()

    # Test Teardown
    del_dirs = ['.config', '.httpie', Path(os.environ.get(ENV_HTTPIE_CONFIG_DIR)), 'config']

# Generated at 2022-06-13 21:39:08.062973
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    #1. test invalid config file
    assert 1 == 0

# Generated at 2022-06-13 21:39:18.436565
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():

    import json

    import pytest

    from httpie.config import BaseConfigDict

    config_dir = "httpie/test/test_unit/test_config/config_test"
    path = Path(config_dir)

    def test_success():
        """
        try to load config file in the correct directory, there is no exceptions
        :return: None
        """
        test_config = BaseConfigDict(path)

        test_config.load()

        with path.open('rt') as f:
            data = json.load(f)

        test_config.update(data)

        assert ("__meta__" in test_config.keys()) is True
        assert ("httpie" in test_config["__meta__"].keys()) is True


# Generated at 2022-06-13 21:39:25.006301
# Unit test for method ensure_directory of class BaseConfigDict
def test_BaseConfigDict_ensure_directory():
    config = BaseConfigDict(Path('/tmp/abcd.json'))
    parent_path = config.path.parent
    assert parent_path.exists() == False
    config.ensure_directory()
    assert parent_path.exists() == True
    assert parent_path.is_dir() == True
    assert config.path.exists() == False
    config.path.unlink()



# Generated at 2022-06-13 21:39:28.395792
# Unit test for method load of class BaseConfigDict
def test_BaseConfigDict_load():
    path = Path('/tmp/test_BaseConfigDict_load')
    BaseConfigDict(path).load()


# Generated at 2022-06-13 21:39:40.166175
# Unit test for method save of class BaseConfigDict
def test_BaseConfigDict_save():
    from httpie import __version__

    class BaseConfigDict_sub(BaseConfigDict):
        def __init__(self, path):
            super().__init__(path)
            self['test'] = "test"

    config_path = os.path.join(DEFAULT_CONFIG_DIR, 'test_config.json')
    config = BaseConfigDict_sub(config_path)
    config.save()

    assert config.path.exists()
    assert config.path.read_text().strip() == json.dumps(
        {
            "__meta__": {
                "httpie": __version__
            },
            "test": "test"
        },
        sort_keys=True,
        indent=4
    )

    # remove test file
    config.path.unlink()