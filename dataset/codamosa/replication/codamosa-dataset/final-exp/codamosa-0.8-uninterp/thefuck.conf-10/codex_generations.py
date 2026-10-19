

# Generated at 2022-06-14 08:32:42.535005
# Unit test for method init of class Settings
def test_Settings_init():
    """Make sure that the user config path is correct.
    The path to the user config directory should be `~/.config/thefuck` or `~/.thefuck`
    """
    # setup user's config path
    user_dir = os.path.join(os.path.expanduser('~'), '.config/thefuck')
    legacy_user_dir = os.path.join(os.path.expanduser('~'), '.thefuck')
    # check if `~/.config/thefuck` exists
    if not os.path.exists(user_dir):
        # if not, check if `~/.thefuck` exists
        if not os.path.exists(legacy_user_dir):
            # if not, create `~/.config/thefuck`
            os.makedirs(user_dir)

# Generated at 2022-06-14 08:32:55.590400
# Unit test for method init of class Settings
def test_Settings_init():
    args = type('Namespace', (object,), {'yes': True, 'debug': True, 'repeat': 5})
    os.environ['TF_SHELL'] = "zsh"
    os.environ['TF_RULES'] = 'bash:python:zsh'
    os.environ['TF_PRIORITY'] = 'bash=10:python=20:zsh=5'
    os.environ['TF_SEARCH_IN_PATH'] = 'false'
    os.environ['TF_EXCLUDE_RULES'] = 'bash'
    os.environ['TF_NO_COLORS'] = 'true'
    os.environ['TF_ALTER_HISTORY'] = 'true'
    os.environ['TF_HISTORY_LIMIT'] = '20'
    os.en

# Generated at 2022-06-14 08:33:08.437073
# Unit test for method init of class Settings
def test_Settings_init():
    import mock
    import os
    import six

    def _load_source(name, path):
        if six.PY3:
            import importlib.machinery
            loader = importlib.machinery.SourceFileLoader(name, path)
            return loader.load_module()
        else:
            import imp
            return imp.load_source(name, path)

    def _write_settings_file(settings_path, data):
        with settings_path.open(mode='w') as settings_file:
            for setting in const.DEFAULT_SETTINGS.items():
                settings_file.write(u'\n# {} = {}\n'.format(*setting))
            settings_file.write(data)


# Generated at 2022-06-14 08:33:11.171589
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings({})
    with settings_file(const.SETTINGS_HEADER):
        settings.init()
    assert settings['require_confirmation']
    assert not settings['debug']



# Generated at 2022-06-14 08:33:24.585352
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import no_traceback_exception
    from .system import TemporaryDirectory
    from .utils import wrap_streams

    with wrap_streams():
        with TemporaryDirectory() as tempdir:
            user_dir = Path(tempdir) / '.config/thefuck'
            user_dir.mkdir(parents=True)
            settings_path = user_dir / 'settings.py'
            with settings_path.open(mode='w') as settings_file:
                settings_file.write(u'''
from thefuck.conf.const import DEFAULT_SETTINGS

settings = DEFAULT_SETTINGS
settings['require_confirmation'] = False
settings['custom_setting'] = 'custom'
''')
            os.environ['THEFUCK_CUSTOM_SETTING'] = 'env'
            settings_

# Generated at 2022-06-14 08:33:26.871901
# Unit test for method init of class Settings
def test_Settings_init():
    test_settings = Settings(const.DEFAULT_SETTINGS)
    test_settings.init()
    assert test_settings.require_confirmation



# Generated at 2022-06-14 08:33:33.624455
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception

    args = type('', (), {'yes': True, 'debug': False, 'repeat': False})
    settings.update(const.DEFAULT_SETTINGS)

    try:
        settings.init(args)
        assert settings.require_confirmation is False
    except Exception:
        exception("Can't load settings from file", sys.exc_info())

# Generated at 2022-06-14 08:33:44.282371
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import Log

    class DummyLog(Log):
        log_calls = []
        exception_calls = []

        def _log(self, message):
            self.log_calls.append(message)

        def exception(self, message, exc_info):
            self.exception_calls.append(message)

    log = DummyLog()
    settings.log = log
    user_dir = Path('.thefuck')

# Generated at 2022-06-14 08:33:51.885621
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import init_log, set_log_file_level
    assert settings['log_file'] == const.DEFAULT_SETTINGS['log_file']

    init_log(settings['log_file'])
    assert settings['log_file'] == ''

    set_log_file_level(True, False)
    assert settings['log_file'] == const.LOGS_FILE_NAME

# Unit tests for method update of class Settings

# Generated at 2022-06-14 08:34:01.924733
# Unit test for method init of class Settings
def test_Settings_init():
    """Unit test for method init of class Settings"""
    from mock import patch, MagicMock

    # Test init with all good
    _args = MagicMock()
    _args.yes = False
    _args.debug = None
    _args.repeat = None
    with patch.object(settings, '_settings_from_file',
                      return_value={'rules': 'default_rules',
                                    'confirm_exit': False,
                                    'no_colors': False}), \
            patch.object(settings, '_settings_from_env',
                         return_value={'rules': 'env_rules'}), \
            patch.object(settings, '_settings_from_args',
                         return_value={'rules': 'args_rules'}):
        settings.init(_args)

# Generated at 2022-06-14 08:34:51.950262
# Unit test for method init of class Settings
def test_Settings_init():
    import tempfile

    def _remove_if_exists(path):
        try:
            os.remove(path)
        except OSError:
            pass

    def _get_file_path():
        fd, path = tempfile.mkstemp()
        os.close(fd)
        return path

    settings_file = _get_file_path()
    settings_dir = os.path.dirname(settings_file)
    settings_dir = os.path.join(settings_dir, 'thefuck')
    try:
        os.makedirs(settings_dir)
    except OSError:
        pass


# Generated at 2022-06-14 08:34:59.767252
# Unit test for method init of class Settings
def test_Settings_init():
    args = lambda: 0
    setattr(args, "repeat", True)
    setattr(args, "yes", True)
    setattr(args, "debug", True)
    setattr(args, "help", True)
    settings.init(args)
    assert settings.get('repeat') == True
    assert settings.get('require_confirmation') == False
    assert settings.get('debug') == True



# Generated at 2022-06-14 08:35:04.285079
# Unit test for method init of class Settings
def test_Settings_init():
    stats = Settings()
    stats.init()
    assert stats['debug'] == False

test_settings = Settings()
test_settings.init(object())
test_settings.debug = True
test_settings.require_confirmation = True

# Generated at 2022-06-14 08:35:15.856949
# Unit test for method init of class Settings
def test_Settings_init():
    # backup
    orig_user_dir = settings.user_dir
    orig_settings_file = settings.get_user_dir().joinpath('settings.py')
    orig_env = dict(os.environ)
    # tear down
    settings._user_dir = None
    settings._init_settings_file()
    os.environ.clear()
    os.environ['TF_ALTER_HISTORY'] = 'True'
    os.environ['TF_REQUIRE_CONFIRMATION'] = 'False'
    os.environ['TF_RULES'] = ('DEFAULT_RULES:'
                              'pip_no_such_option=pip install')
    os.environ['TF_PRIORITY'] = 'pip_no_such_option=20'

# Generated at 2022-06-14 08:35:26.252380
# Unit test for method init of class Settings
def test_Settings_init():
    import os
    import tempfile

    args = type('args', (object,), {'yes': False, 'debug': False})
    environ = os.environ

# Generated at 2022-06-14 08:35:34.863516
# Unit test for method init of class Settings
def test_Settings_init():
    from . import log

    args = type(u'test', (object,), {u'yes': True, u'debug': True, u'repeat': 1})()
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init(args)
    assert settings['require_confirmation'] == False
    assert settings['debug'] == True
    assert settings['repeat'] == 1
    assert settings['log_file'] == log.DEFAULT_LOG_FILE


# Generated at 2022-06-14 08:35:43.729501
# Unit test for method init of class Settings
def test_Settings_init():
    try:
        import mock
    except ImportError:
        class mock: pass
    sys.modules['thefuck.settings'] = mock.Mock()
    mock_settings = sys.modules['thefuck.settings']
    mock_settings.DEFAULT_SETTINGS = {
        'some_setting': 42,
        'other_setting': 'value'
        }
    mock_settings.ENV_TO_ATTR = {
        'SOME_ENV': 'some_setting',
        'OTHER_ENV': 'other_setting'
        }
    mock_settings.SETTINGS_HEADER = 'settings header'

    with mock.patch('os.environ', {'SOME_ENV': '43'}):
        settings.init()

    mock_settings.from_file.assert_called_with()
    mock

# Generated at 2022-06-14 08:35:53.015591
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings['debug'] == False
    assert settings['require_confirmation'] == True
    assert settings['slow_commands'] == ['lein', 'react-native', 'gradle']
    assert settings['alias'] == {}
    assert settings['exclude_rules'] == []
    assert settings['excluded_search_path_prefixes'] == []
    assert settings['priority'] == {}
    assert settings['repeat'] == False
    assert settings['wait_command'] == 3
    assert settings['wait_slow_command'] == 9
    assert settings['no_colors'] == False
    assert settings['alter_history'] == True
    assert settings['instant_mode'] == False
    assert settings['num_close_matches'] == 3
    assert settings['search_paths'] == []
    assert settings['history_limit']

# Generated at 2022-06-14 08:36:02.889856
# Unit test for method init of class Settings
def test_Settings_init():
    # settings_path = settings.user_dir.joinpath('settings.py')
    # with settings_path.open(mode='w') as settings_file:
    #     settings_file.write(const.SETTINGS_HEADER)
    #     for setting in const.DEFAULT_SETTINGS.items():
    #         settings_file.write(u'# {} = {}\n'.format(*setting))
    settings.init()
    env_to_attr = {'TF_REQUIRE_CONFIRMATION': 'require_confirmation',
                   'TF_HISTORY_LIMIT': 'history_limit', 'TF_WAIT_COMMAND':
                   'wait_command'}
    for env, attr in env_to_attr.items():
        os.environ[env] = '1'
    settings.init

# Generated at 2022-06-14 08:36:15.738648
# Unit test for method init of class Settings

# Generated at 2022-06-14 08:37:47.722711
# Unit test for method init of class Settings
def test_Settings_init():
    # Test if settings are successfully created when settings.py doesn't exist
    user_dir = Path('/tmp/thefuck-test', 'user_dir')
    settings_file = user_dir.joinpath('settings.py')
    try:
        if user_dir.is_dir():
            shutil.rmtree(str(user_dir))
        user_dir.mkdir(parents=True)
        settings.init()
        assert settings_file.is_file()
    finally:
        shutil.rmtree(str(user_dir))


# Generated at 2022-06-14 08:37:57.818654
# Unit test for method init of class Settings
def test_Settings_init():
    import mock
    import argparse
    from .logs import warning
    from .logs import exception

    with mock.patch('thefuck.settings.Settings._setup_user_dir') as _setup_user_dir, \
            mock.patch('thefuck.settings.load_source') as load_source, \
            mock.patch('six.moves.builtins.open') as open_:
        settings._init_settings_file()
        open_.assert_any_call(
            Path('/', 'home', 'Alex', '.config', 'thefuck', 'settings.py'),
            'w')


# Generated at 2022-06-14 08:38:05.205458
# Unit test for method init of class Settings
def test_Settings_init():
    """Check that the function init() keeps some of the default values"""
    # arrange
    new_settings = Settings()
    # act
    new_settings.init()
    # assert
    assert new_settings.get('alter_history') == True
    assert new_settings.get('require_confirmation') == True
    assert new_settings.get('debug') == False
    assert new_settings.get('repeat') == False

# Generated at 2022-06-14 08:38:16.450747
# Unit test for method init of class Settings
def test_Settings_init():
    # Prevent function call of load_settings in .py files
    import __builtin__
    load_settings = __builtin__.__dict__.get('load_settings')
    __builtin__.__dict__['load_settings'] = lambda: {}

    settings.init()
    assert settings.get('wait_command') is None

    os.environ.update({'XDG_CONFIG_HOME': '/tmp/test',
                       'TF_WAIT_COMMAND': '300',
                       'TF_RULES': 'DEFAULT_RULES',
                       'TF_PRIORITY': 'test=2:cat=1:fuck=3'})

    settings.init()
    assert settings.get('wait_command') == 300


# Generated at 2022-06-14 08:38:28.821626
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import _get_history_file
    from .utils import get_all_executables
    from .utils import get_all_executables_by_ext
    from .utils import get_all_scripts
    from .utils import get_all_scripts_by_ext
    from .utils import get_all_search_paths
    from .utils import get_all_search_paths_by_ext

    args = Mock()

    settings.init(args)

    assert settings['debug'] == True
    assert settings['verbose'] == False
    assert settings['require_confirmation'] == True
    assert settings['no_colors'] == False
    assert settings['wait_command'] == 3
    assert settings['wait_slow_command'] == 15
    assert settings['alter_history'] == True

# Generated at 2022-06-14 08:38:31.363898
# Unit test for method init of class Settings
def test_Settings_init():
    dir_path = '/home/thatsme/'
    settings.user_dir = dir_path
    assert(settings.user_dir == dir_path)

# Generated at 2022-06-14 08:38:43.307055
# Unit test for method init of class Settings
def test_Settings_init():
    import tempfile
    import shutil
    from .logs import disable_debug_logging

    tempdir = tempfile.mkdtemp()
    env = os.environ
    try:
        os.environ = {}
        with disable_debug_logging():
            settings.user_dir = Path(tempdir)
            settings.init()
            assert not settings.no_colors
            assert settings.debug is False
            assert settings.history_limit == 5
            assert settings.wait_command == 1
            assert settings.wait_slow_command == 9
            assert settings.repeat is False
    finally:
        os.environ = env
        shutil.rmtree(tempdir)



# Generated at 2022-06-14 08:38:50.068346
# Unit test for method init of class Settings
def test_Settings_init():
    import mock
    from . import settings as _settings
    from .logs import exception, warn

    settings = _settings.Settings()
    settings.user_dir = mock.Mock()

    settings.init(args=mock.Mock())

    settings.user_dir.joinpath.assert_called_once_with('settings.py')
    settings.user_dir.joinpath().is_file.assert_called_once_with()
    settings.user_dir.joinpath().open.assert_called_once_with(mode='w')

# Generated at 2022-06-14 08:38:53.556333
# Unit test for method init of class Settings
def test_Settings_init():
    # Method init of class Settings should call method update of class Settings
    # to update class variables with values from dict
    with patch('thefuck.settings.Settings.update') as mocked_update:
        settings = Settings()
        settings.init()
        mocked_update.assert_called_once_with(settings._settings_from_env())

# Generated at 2022-06-14 08:38:57.735710
# Unit test for method init of class Settings
def test_Settings_init():
    args = {'yes': True, 'debug': True, 'repeat': 2}
    settings.init(args)
    assert settings["require_confirmation"]==False
    assert settings["debug"]==True
    assert settings["repeat"]==2