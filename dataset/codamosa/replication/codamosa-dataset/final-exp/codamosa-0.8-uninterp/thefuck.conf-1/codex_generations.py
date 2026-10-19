

# Generated at 2022-06-14 08:31:56.518128
# Unit test for method init of class Settings
def test_Settings_init():
    global settings
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init({'yes': True, 'debug': True, 'repeat': 2})
    assert settings.require_confirmation == False
    assert settings.debug == True
    assert settings.repeat == 2

# Generated at 2022-06-14 08:31:57.483165
# Unit test for method init of class Settings
def test_Settings_init():
    pass


settings.init()


# Generated at 2022-06-14 08:32:10.344925
# Unit test for method init of class Settings
def test_Settings_init():
    from mock import patch
    from .logs import exception

    settings.clear()

    with patch.dict(settings, {'_settings_from_file': {'key': 'value'}}):
        settings.init()
    assert settings['key'] == 'value'

    with patch.dict(settings, {'_settings_from_env': {'key': 'value2'}}):
        settings.init()
    assert settings['key'] == 'value2'

    with patch.dict(settings, {'_settings_from_args': {'key': 'value3'}}):
        settings.init(object())
    assert settings['key'] == 'value3'

    with patch.dict(settings, {'_settings_from_file': Exception()}):
        with patch.object(exception, 'disable') as mocker:
            settings

# Generated at 2022-06-14 08:32:22.999922
# Unit test for method init of class Settings
def test_Settings_init():
    import sys,os
    import tempfile

    sys.stderr = tempfile.NamedTemporaryFile(delete=False)
    if hasattr(settings, 'user_dir'):
        del settings.user_dir

    settings.init()
    assert settings.user_dir.is_dir()

    settings.init(type('args', (object,), {'yes': True}))
    assert settings.require_confirmation is False
    assert settings.repeat is None

    settings.init(type('args', (object,), {'debug': True}))
    assert settings.debug is True

    settings.init(type('args', (object,), {'repeat': 0}))
    assert settings.repeat is 0

    settings.init()
    assert settings.repeat is None


# Generated at 2022-06-14 08:32:28.298918
# Unit test for method init of class Settings
def test_Settings_init():
    args = Mock(yes=True, debug=False, repeat=False)
    settings_obj = Settings()
    settings_obj.init(args=args)
    assert settings_obj['require_confirmation'] is False
    assert settings_obj['debug'] is False
    assert settings_obj['repeat'] == 1

# Generated at 2022-06-14 08:32:40.392120
# Unit test for method init of class Settings
def test_Settings_init():
    # config_user_dir does not exists
    from .logs import exception

    is_dir_called = 0
    def is_dir(dir_path):
        nonlocal is_dir_called
        is_dir_called += 1
        return False

    is_file_called = 0
    def is_file(file_path):
        nonlocal is_file_called
        is_file_called += 1
        return False

    tmp_settings_path = 'path'
    expanduser_called = 0
    def expanduser(path):
        nonlocal expanduser_called
        expanduser_called += 1
        return tmp_settings_path


# Generated at 2022-06-14 08:32:49.005397
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import log

    settings.init()
    assert settings.user_dir.is_dir()
    assert settings.user_dir.joinpath('rules').is_dir()
    assert settings.user_dir.joinpath('settings.py').is_file()

    res = log.exception('Can\'t load settings from file', sys.exc_info())
    assert "<class 'settings.Settings'>" in res

    res = log.exception('Can\'t load settings from env', sys.exc_info())
    assert "<class 'settings.Settings'>" in res

# Generated at 2022-06-14 08:32:58.200377
# Unit test for method init of class Settings
def test_Settings_init():
    # Clear all the settings
    settings.clear()

    # Init settings first time
    settings.init()
    assert settings['require_confirmation'] == True
    assert settings.user_dir == Path('~/.config/thefuck').expanduser()

    # Keep the state of settings
    old_settings = settings.copy()

    # Init settings second time
    settings.init()
    assert settings == old_settings

    # Dummy args for method _settings_from_args
    args = type('', (), {'yes': False, 'repeat': None, 'debug': False})
    assert settings._settings_from_args(args) == {}

    # Dummy args for method _settings_from_args
    args = type('', (), {'yes': True, 'repeat': None, 'debug': False})
    assert settings._settings_from_args

# Generated at 2022-06-14 08:33:10.171666
# Unit test for method init of class Settings
def test_Settings_init():
    # create a temporary dir
    tmp_dir = tempfile.gettempdir()
    tmp_dir = os.path.join(tmp_dir, 'fuck_test')
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)

    # ## create the user settings file
    settings_path = os.path.join(tmp_dir, 'settings.py')
    with open(settings_path, 'w') as settings_file:
        settings_file.write(const.SETTINGS_HEADER)
        for setting in const.DEFAULT_SETTINGS.items():
            settings_file.write(u'# {} = {}\n'.format(*setting))

    # ## create the env var
    os.environ['THEFUCK_REQUIRE_CONFIRMATION'] = 'false'

# Generated at 2022-06-14 08:33:18.285697
# Unit test for method init of class Settings
def test_Settings_init():
    global settings
    env = {}
    args = None
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.all_rules = ['dummy_rule']
    settings.init(env=env, args=args)
    assert settings.rules == ['dummy_rule']

    env = {'THEFUCK_REQUIRE_CONFIRMATION': 'False'}
    args = None
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.all_rules = ['dummy_rule']
    settings.init(env=env, args=args)
    assert settings.rules == ['dummy_rule']
    assert settings.require_confirmation is False


# Generated at 2022-06-14 08:33:40.272946
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings.rules == const.DEFAULT_RULES

# Generated at 2022-06-14 08:33:51.581338
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import reset_loggers
    reset_loggers()

    try:
        del os.environ['TF_COLOR_MODE']
    except KeyError:
        pass

    try:
        del os.environ['TF_NO_COLOR']
    except KeyError:
        pass

    settings.init()
    assert settings.user_dir.is_dir()
    assert settings.get('debug', False) is False
    assert settings.get('require_confirmation', True) is True
    assert settings.get('no_colors', False) is False
    assert settings.get('alter_history', True) is True
    assert settings.get('history_limit', None) is None
    assert settings.get('wait_slow_command', 15) == 15
    assert settings.get('wait_command', 0) == 0
   

# Generated at 2022-06-14 08:33:55.842757
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import capture_logs

    class Args(object):
        pass
    args = Args()
    args.yes = True
    args.debug = True
    args.repeat = True

    settings.init(args)
    assert settings["require_confirmation"] != const.DEFAULT_SETTINGS["require_confirmation"]
    assert settings["debug"] != const.DEFAULT_SETTINGS["debug"]
    assert settings["repeat"] != const.DEFAULT_SETTINGS["repeat"]



# Generated at 2022-06-14 08:34:08.173337
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception

    def mock_exception(*_):
        pass

    exception.side_effect = mock_exception

    settings.init()
    assert settings.require_confirmation
    assert not hasattr(settings, 'no_colors')

    settings = Settings(require_confirmation=False)
    settings.init()
    assert not settings.require_confirmation

    os.environ['THEFUCK_RULES'] = 'bash:zsh:python'
    settings.init()
    assert settings.rules == ['bash', 'zsh', 'python']

    os.environ['THEFUCK_EXCLUDE_RULES'] = 'man:sudo'
    settings.init()
    assert settings.exclude_rules == ['man', 'sudo']


# Generated at 2022-06-14 08:34:19.975586
# Unit test for method init of class Settings
def test_Settings_init():
    from mock import patch, MagicMock
    with patch('thefuck.main.settings._settings_from_file') as mock_from_file:
        mock_from_file.return_value = {'rules': ['test_rule'],
                                       'require_confirmation': True}
        new_settings = {'key': 'value'}
        with patch('thefuck.main.settings._settings_from_env') as mock_from_env:
            mock_from_env.return_value = new_settings
            with patch('thefuck.main.settings._settings_from_args') as mock_from_args:
                mock_from_args.return_value = {'rules': ['test_rule2']}

# Generated at 2022-06-14 08:34:32.591133
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings()
    settings.init()
    assert settings.user_dir == Path(os.getcwd()).joinpath('thefuck')
    assert settings.settings_path == Path(os.getcwd()).joinpath('thefuck', 'settings.py')
    assert settings.rules == [
        'echo_date',
        'python_command',
        'sudo',
        'git_push',
        'apt_get',
        'systemctl',
        'pip_install',
        'man',
        'gem_install',
        'stack',
        'npm_install',
        'vagrant',
        'brew_install',
        'brew_update',
        'ghci_load',
        'reload_macos',
        'gcloud'
    ]

# Generated at 2022-06-14 08:34:44.878906
# Unit test for method init of class Settings
def test_Settings_init():
    """Test Settings class init method."""
    import sys
    import tempfile

    settings.init()
    assert settings.get('rules', '') == ['python', 'git', 'gem']
    assert settings.get('priority', '') == {'python': 10}
    assert settings.get('require_confirmation', '') is True
    assert settings.get('wait_command', '') == 1
    assert settings.get('wait_slow_command', '') == 3
    assert settings.get('num_close_matches', '') == 3
    assert settings.get('history_limit', '') == 10000
    assert settings.get('exclude_rules', '') == []
    assert not settings.get('no_colors')
    assert not settings.get('debug')
    assert not settings.get('alter_history')

# Generated at 2022-06-14 08:34:52.992770
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings()
    settings.init(None)
    assert settings.require_confirmation
    assert settings.rules == const.DEFAULT_RULES
    assert settings.exclude_rules == ()
    assert settings.priority == {}
    assert settings.wait_command == 0
    assert settings.history_limit == 0
    assert settings.wait_slow_command == 0
    assert settings.slow_commands == ()
    assert not settings.no_colors
    assert not settings.debug
    assert settings.repeat == 1
    assert not settings.alter_history
    assert not settings.instant_mode
    assert settings.num_close_matches == 0
    assert settings.excluded_search_path_prefixes == ()

# Generated at 2022-06-14 08:35:00.001899
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception
    from .logs import warning

    mock_exception = [None]
    mock_warning = [None]

    def mock_exception(msg, exc_info):
        mock_exception[0] = msg, exc_info

    def mock_warning(msg):
        mock_warning[0] = msg


# Generated at 2022-06-14 08:35:09.442682
# Unit test for method init of class Settings
def test_Settings_init():
    import sys
    import os
    from tests.utils import TestCase
    from .system import TemporaryDirectory, Path
    from .settings import Settings
    from .logs import exception

    class TestSettings(TestCase):
        def setUp(self):
            self._settings_file = Path(__file__).parent.joinpath('settings.py')
            self._test_dir = Path(TemporaryDirectory().name)
            self._test_dir.joinpath('settings.py').write_text(self._settings_file.read_text(encoding='utf-8'))
            os.environ['THEFUCK_SETTINGS_PATH'] = text_type(self._test_dir.joinpath('settings.py'))
            os.environ['THEFUCK_WAIT_COMMAND'] = '5'

# Generated at 2022-06-14 08:36:02.817987
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert all([getattr(settings, key) == const.DEFAULT_SETTINGS[key]
                for key in const.DEFAULT_SETTINGS.keys()])

# Generated at 2022-06-14 08:36:15.660271
# Unit test for method init of class Settings
def test_Settings_init():
    import os
    import shutil
    from mock import Mock

    def clear_env():
        os.environ.pop('THEFUCK_DEBUG', None)
        os.environ.pop('THEFUCK_REQUIRE_CONFIRMATION', None)
        os.environ.pop('THEFUCK_RULES', None)
        os.environ.pop('THEFUCK_WAIT_COMMAND', None)
        os.environ.pop('THEFUCK_WAIT_SLOW_COMMAND', None)
        os.environ.pop('THEFUCK_NO_COLOR', None)

    def clear_settings():
        settings.clear()
        settings.update(const.DEFAULT_SETTINGS)


# Generated at 2022-06-14 08:36:29.699892
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert isinstance(settings.wait_command, int)
    assert isinstance(settings.require_confirmation, bool)
    assert isinstance(settings.exclude_rules, list)
    assert isinstance(settings.rules, list)
    assert isinstance(settings.history_limit, int)
    assert isinstance(settings.priority, dict)
    assert isinstance(settings.no_colors, bool)
    assert isinstance(settings.debug, bool)
    assert isinstance(settings.wait_slow_command, int)
    assert isinstance(settings.slow_commands, tuple)
    assert isinstance(settings.excluded_search_path_prefixes, tuple)
    assert isinstance(settings.rules_dir, Path)
    assert isinstance(settings.user_dir, Path)

# Generated at 2022-06-14 08:36:34.242516
# Unit test for method init of class Settings
def test_Settings_init():
    """Unit test for init of class Settings"""
    settings = Settings(const.DEFAULT_SETTINGS)
    # Mock global variable os.environ

# Generated at 2022-06-14 08:36:42.892610
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception

    args = Settings(const.DEFAULT_SETTINGS)
    args._setup_user_dir()
    args._init_settings_file()

    try:
        args.update(args._settings_from_file())
    except Exception:
        exception("Can't load settings from file", sys.exc_info())

    try:
        args.update(args._settings_from_env())
    except Exception:
        exception("Can't load settings from env", sys.exc_info())

    args.update(args._settings_from_args())

# Generated at 2022-06-14 08:36:49.418344
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import _log_dir
    repo_dir = Path(__file__).parent
    user_dir = Path.home().joinpath('.config', 'thefuck')

    env = {'TF_CONF_FILE': '/tmp/tf_conf_file'}
    args = namedtuple('args', ['yes', 'debug', 'repeat'])
    args.yes = True
    args.debug = True
    args.repeat = 2

    # Case 1: Configuration directory exists and there are no env or args.
    settings.init()
    assert settings['conf_file'] == repo_dir.joinpath('thefuck.conf')
    assert settings['history_limit'] == 0

# Generated at 2022-06-14 08:37:01.569599
# Unit test for method init of class Settings
def test_Settings_init():
    test_settings = Settings(const.DEFAULT_SETTINGS)
    test_settings.user_dir.removedirs_p()
    test_settings.init()

    assert test_settings.user_dir.joinpath('rules').isdir() is True
    assert test_settings.user_dir.joinpath('settings.py').isfile() is True

    settings_file = test_settings.user_dir.joinpath('settings.py')
    src_file = open(const.SRC_ROOT_DIR + '/settings.py', 'r')
    assert settings_file.open(mode='r').read() == src_file.read()

    test_settings.user_dir.removedirs_p()

# Generated at 2022-06-14 08:37:11.181919
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception
    from mock import patch

    def init_settings_file_mock(self):
        pass

    def settings_from_file_mock(self):
        return {'rules': ['rules-something']}

    def settings_from_env_mock(self):
        return {'rules': ['rules-env']}

    def settings_from_args_mock(self, args):
        return {'rules': ['rules-args']}

    def setup_user_dir_mock(self):
        self.user_dir = Path('~', '.thefuck').expanduser()

    def legacy_user_dir_mock(self):
        return Path('~', '.thefuck').expanduser()


# Generated at 2022-06-14 08:37:21.584801
# Unit test for method init of class Settings
def test_Settings_init():
    # Given
    settings.init()

    # Then
    assert settings.user_dir.endswith('.config/thefuck')
    assert settings.user_dir.exists()

    settings_path = settings.user_dir + '/settings.py'
    assert settings_path.isfile()

    with settings_path.open() as settings_file:
        assert settings_file.read() == const.SETTINGS_HEADER
        for key, value in const.DEFAULT_SETTINGS.items():
            assert u'# {} = {}\n'.format(key, value) in settings



# Generated at 2022-06-14 08:37:23.855271
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    # Init settings.py
    assert settings['rules'] == const.DEFAULT_RULES

# Generated at 2022-06-14 08:38:57.098306
# Unit test for method init of class Settings
def test_Settings_init():
    import mock
    import os
    import subprocess
    from thefuck.shells import Bash, Fish, Zsh
    from thefuck.shell import Shell
    from thefuck.types import CorrectedCommand
    from thefuck.main import shit, main
    from thefuck.utils import cache, wrap_settings
    from thefuck.logs import log_exception

    settings.init()

    os.environ['TF_COLOR_ENABLED'] = 'True'
    os.environ['TF_SLOW_COMMANDS'] = 'ls:cd:cat:tree:python:pip'
    os.environ['TF_HISTORY_LIMIT'] = '10000'
    settings.init()



# Generated at 2022-06-14 08:38:57.892026
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init(args=None)

# Generated at 2022-06-14 08:39:04.218841
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings['require_confirmation'] is True
    assert settings['wait_command'] == 0
    assert settings['wait_slow_command'] == 15

    settings.init(args=Namespace())
    assert settings['require_confirmation'] is True
    assert settings['wait_command'] == 0
    assert settings['wait_slow_command'] == 15

    settings.init(args=Namespace(yes=True))
    assert settings['require_confirmation'] is False
    assert settings['wait_command'] == 0
    assert settings['wait_slow_command'] == 15

    settings.init(args=Namespace(debug=True))
    assert settings['require_confirmation'] is True
    assert settings['wait_command'] == 0
    assert settings['wait_slow_command'] == 15
    assert settings['debug'] is True

# Generated at 2022-06-14 08:39:14.465768
# Unit test for method init of class Settings
def test_Settings_init():
    class Args:
        debug = True
        repeat = 1
        yes = True

    #create empty settings file
    settings_path = Path(settings._get_user_dir_path()).joinpath('settings.py')
    with open(settings_path, 'w') as f:
        f.write(const.SETTINGS_HEADER)

    settings.init(Args)

    # check if settings was updated
    assert settings['require_confirmation'] == False
    assert settings['debug'] == True
    assert settings['repeat'] == 1

    # remove settings file
    import os
    os.remove(settings_path)

# Generated at 2022-06-14 08:39:22.489174
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import Logger
    from .utils import get_closest

    Logger._logger = None # clear logger cache to avoid test pollution

    settings.init()

    assert get_closest(settings.rules, 'pwd') in settings.rules
    assert get_closest(settings.rules, 'pwd', key=lambda r: -r.priority) in settings.rules
    assert get_closest(settings.exclude_rules, 'cd') in settings.exclude_rules
    assert get_closest(settings.exclude_rules, 'cd', key=lambda r: -r.priority) in settings.exclude_rules
    assert settings.rules_dir

    settings.init(args=argparse.Namespace(yes=True, debug=True))
    assert not settings.require_confirmation

# Generated at 2022-06-14 08:39:31.164780
# Unit test for method init of class Settings
def test_Settings_init():
    # init(args)
    assert settings.init(argparse.Namespace(yes=True))['require_confirmation'] == False
    assert settings.init(argparse.Namespace(yes=False))['require_confirmation'] == True
    assert settings.init(argparse.Namespace(debug=True))['debug'] == True
    assert settings.init(argparse.Namespace(debug=False))['debug'] == False
    assert settings.init(argparse.Namespace(repeat=2))['repeat'] == 2

# Generated at 2022-06-14 08:39:37.807930
# Unit test for method init of class Settings
def test_Settings_init():
    os.environ['THEFUCK_REQUIRE_CONFIRMATION'] = 'False'
    settings.init()
    assert settings.require_confirmation == False
    assert settings.no_colors == False
    settings.init(args=argparse.Namespace(yes=True, debug=True, repeat=10))
    assert settings.require_confirmation == True
    assert settings.debug == True
    assert settings.repeat == 10

# Generated at 2022-06-14 08:39:44.368095
# Unit test for method init of class Settings
def test_Settings_init():
    """Test init() method"""
    try:
        settings.init()
        assert settings['user_dir'] == settings._get_user_dir_path()
        assert settings['require_confirmation'] == \
            const.DEFAULT_SETTINGS['require_confirmation']
        assert settings['debug'] == const.DEFAULT_SETTINGS['debug']
    finally:
        pass


# Generated at 2022-06-14 08:39:54.311679
# Unit test for method init of class Settings
def test_Settings_init():
    temp_dir = Path('/tmp/.thefuck')
    temp_settings = temp_dir.joinpath('settings.py')
    temp_log = temp_dir.joinpath('output.log')

    if not temp_dir.is_dir():
        temp_dir.mkdir()


# Generated at 2022-06-14 08:39:57.317713
# Unit test for method init of class Settings
def test_Settings_init():
    settings.clear()
    settings.init()
    assert settings.get('require_confirmation')
    assert settings.get('rules')
    assert settings.get('history_limit')