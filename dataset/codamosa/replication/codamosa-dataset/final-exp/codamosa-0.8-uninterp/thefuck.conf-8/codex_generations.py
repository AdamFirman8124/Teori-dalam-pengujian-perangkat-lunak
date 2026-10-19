

# Generated at 2022-06-14 08:31:59.512487
# Unit test for method init of class Settings
def test_Settings_init():
    _os_environ = os.environ
    os.environ = {}

    try:
        settings.init()
        assert settings == const.DEFAULT_SETTINGS
    finally:
        os.environ = _os_environ


# Generated at 2022-06-14 08:32:03.865874
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import Log
    from tests.utils import patch, MagicMock
    import thefuck
    with patch.object(Log, 'warning', MagicMock()):
        thefuck.settings.init()

# Generated at 2022-06-14 08:32:12.990166
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings(test_settings_source)
    settings.init(args=test_args)

    temp_dir = Path(settings.user_dir)
    settings_file = temp_dir.joinpath('settings.py')
    temp_dir.rmtree()

    assert settings.key == 'value'
    assert settings_file.is_file()

test_settings_source = {'key': 'value'}
test_args = lambda: None
test_args.yes = 0
test_args.debug = False
test_args.repeat = 0
test_args.rules = 'DEFAULT_RULES'
test_args.priorities = 'DEFAULT_PRIORITIES'
test_args.no_colors = 1
test_args.require_confirmation = 0
test_args.wait_command = 0
test

# Generated at 2022-06-14 08:32:23.896040
# Unit test for method init of class Settings
def test_Settings_init():
    os.environ["THEFUCK_REQUIRE_CONFIRMATION"] = "False"
    os.environ["THEFUCK_NO_COLORS"] = "True"
    os.environ["THEFUCK_WAIT_COMMAND"] = "1"
    os.environ["THEFUCK_HISTORY_LIMIT"] = "1"
    os.environ["THEFUCK_WAIT_SLOW_COMMAND"] = "2"
    os.environ["THEFUCK_PRIORITY"] = "fuck=1:ls=2:git=3"
    os.environ["THEFUCK_RULES"] = "ls:fuck:git"
    os.environ["THEFUCK_REPEAT"] = "2"

# Generated at 2022-06-14 08:32:26.704622
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings(const.DEFAULT_SETTINGS)
    args = ['fuck', '-y']
    settings.init(args)



# Generated at 2022-06-14 08:32:36.132936
# Unit test for method init of class Settings
def test_Settings_init():
    from imp import load_source
    from os.path import expanduser
    from .logs import exception
    from .system import Path
    from . import const

    _settings = Settings(const.DEFAULT_SETTINGS)
    _settings._setup_user_dir = lambda: setattr(_settings, 'user_dir', Path(expanduser('~'), '.thefuck'))
    _settings._init_settings_file = lambda: setattr(_settings, '_settings_from_file', lambda: {'require_confirmation': False})
    _settings._settings_from_env = lambda: {'history_limit': '2000'}
    _settings._settings_from_args = lambda val: {'debug': True}
    _settings.init()
    assert _settings.require_confirmation == False
    assert _settings.history_limit == 2000

# Generated at 2022-06-14 08:32:41.645430
# Unit test for method init of class Settings
def test_Settings_init():
    args = type('Args', (object,),
                {'debug': True, 'yes': True})()
    env = os.environ
    env['THEFUCK_REPEAT'] = '0'
    env['THEFUCK_DEBUG'] = 'True'
    env['THEFUCK_REQUIRE_CONFIRMATION'] = 'False'
    settings.init(args)
    assert settings.require_confirmation == True
    assert settings.repeat == 0
    assert settings.debug == True

# Generated at 2022-06-14 08:32:53.044950
# Unit test for method init of class Settings
def test_Settings_init():
    from tempfile import mkdtemp
    from .logs import exception

    settings.init()

    assert const.DEFAULT_SETTINGS.items() <= settings.items()

    with mkdtemp() as tmpdir:
        user_dir = Path(tmpdir)

        xdg_config_home = Path(user_dir).joinpath('thefuck')
        os.environ['XDG_CONFIG_HOME'] = text_type(xdg_config_home.parent)
        settings.init()

        assert xdg_config_home == settings.user_dir
        assert (user_dir.joinpath('thefuck', 'settings.py').is_file())

        legacy_user_dir = user_dir.joinpath('.thefuck')
        legacy_user_dir.mkdir()
        settings.init()


# Generated at 2022-06-14 08:32:56.649794
# Unit test for method init of class Settings
def test_Settings_init():
    args = None
    settings.init(args)
    
    args = []
    settings.init(args)
    
    args = ['--yes']
    settings.init(args)
    
    args = ['--debug', 'true']
    settings.init(args)
    
    args = ['--repeat', 4]
    settings.init(args)

# Generated at 2022-06-14 08:33:08.923821
# Unit test for method init of class Settings
def test_Settings_init():
    os.environ['FUCK_RULES'] = 'alpha'
    os.environ['FUCK_PRIORITY'] = 'beta=2:gamma=1'
    os.environ['FUCK_EXCLUDE_RULES'] = 'delta:epsilon'
    os.environ['FUCK_SLOW_COMMANDS'] = '1:2:3'
    os.environ['FUCK_EXCLUDED_SEARCH_PATH_PREFIXES'] = 'a:b:c'
    os.environ['FUCK_REQUIRE_CONFIRMATION'] = 'TRUE'
    os.environ['FUCK_HISTORY_LIMIT'] = '1000'
    os.environ['FUCK_WAIT_SLOW_COMMAND'] = '10'

# Generated at 2022-06-14 08:33:43.403969
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings.require_confirmation is True
    assert settings.repeat is False
    assert settings.debug is False
    assert settings.no_colors is False
    assert settings.history_limit == 0
    assert settings.alter_history is False
    assert settings.wait_command == 3
    assert settings.wait_slow_command == 10
    assert settings.exclude_rules == []
    assert settings.excluded_search_path_prefixes == []
    assert settings.priority == {}
    assert settings.slow_commands == ['lein', 'gradle', './gradlew', 'sbt', './sbt']
    assert settings.num_close_matches == 3
    assert settings.instant_mode is False

    os.environ['THEFUCK_REQUIRE_CONFIRMATION'] = 'False'

# Generated at 2022-06-14 08:33:45.153571
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()

# Generated at 2022-06-14 08:33:50.208224
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init(args=None)
    assert settings.get('user_dir') == Path(os.environ.get('XDG_CONFIG_HOME', '~/.config'), 'thefuck').expanduser()
    assert settings.get('user_dir').is_dir()

# Generated at 2022-06-14 08:33:52.196179
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()
    assert settings['require_confirmation'] == False


# Generated at 2022-06-14 08:34:04.759766
# Unit test for method init of class Settings
def test_Settings_init():
    from tempfile import TemporaryDirectory
    from textwrap import dedent
    import os

    def _touch(path):
        Path(path).touch()

    with TemporaryDirectory() as folder:
        _touch(os.path.join(folder, 'settings.py'))
        os.environ['THEFUCK_WAIT_COMMAND'] = '10'
        os.environ['THEFUCK_RULES'] = 'DEFAULT_RULES'
        os.environ['THEFUCK_PRIORITY'] = 'f00=100:foo=10'
        os.environ['THEFUCK_INSTANT_MODE'] = 'true'
        settings.init()

    assert settings.user_dir == Path(folder)
    assert settings.wait_command == 10
    assert settings.rules == const.DEFAULT_RULES

# Generated at 2022-06-14 08:34:15.985948
# Unit test for method init of class Settings
def test_Settings_init():
    global settings

    def _init(args=None):
        """Reset the settings and initialize it again."""
        global settings
        settings = Settings(const.DEFAULT_SETTINGS)
        settings.init(args)

    # Initialize the settings.
    _init()
    assert not settings.rules
    assert not settings.exclude_rules
    assert not settings.priority
    assert settings.require_confirmation
    assert not settings.no_colors
    assert not settings.debug
    assert settings.alter_history
    assert settings.wait_command == 1
    assert not settings.slow_commands
    assert not settings.excluded_search_path_prefixes
    assert settings.history_limit == 0
    assert not settings.instant_mode
    assert settings.wait_slow_command == 15
    assert settings.num_close

# Generated at 2022-06-14 08:34:29.427610
# Unit test for method init of class Settings
def test_Settings_init():
    from .utils import memoize
    from .logs import logger
    from .utils import get_closest
    import os

    def del_keys(source, keys):
        for key in keys:
            source.pop(key, None)

    settings.init(args)
    # Check if keys are in settings
    keys = [key for key in const.DEFAULT_SETTINGS]
    assert all(key in settings for key in keys) is True
    # Check if keys are not in settings
    del_keys(settings, keys)
    keys = ['_get_user_dir_path', '_setup_user_dir', '_settings_from_file']
    assert all(key not in settings for key in keys) is True
    # Check if function keys are in settings
    keys = ['get_priority']

# Generated at 2022-06-14 08:34:36.221499
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings.get('wait_command') == 5
    assert settings.get('require_confirmation') == True
    assert settings.get('no_colors') == False
    assert settings.get('slow_commands') == ['(^| )sudo ']
    assert settings.get('repeat') == 1
    assert settings.get('excluded_search_path_prefixes') == \
        ['~/.pyenv/versions', '/usr/local/bin', '/usr/bin']

# Generated at 2022-06-14 08:34:50.222529
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()

    assert settings['history_limit'] == 100
    assert settings['wait_command'] == 1
    assert settings['wait_slow_command'] == 15
    assert settings['no_colors'] == False
    assert settings['debug'] == False
    assert settings['rules'] == const.DEFAULT_RULES
    assert settings['exclude_rules'] == []
    assert settings['priority'] == {}
    assert settings['require_confirmation'] == False
    assert settings['alter_history'] == True
    assert settings['instant_mode'] == False
    assert settings['repeat'] == 1
    assert settings['slow_commands'] == []
    assert settings['excluded_search_path_prefixes'] == \
        [u'/usr/local/', u'/usr/lib/']

# Generated at 2022-06-14 08:34:58.487620
# Unit test for method init of class Settings
def test_Settings_init():
    from unittest import mock
    from .logs import exception

    # init should set user_dir property
    settings.init()
    assert settings.user_dir

    # init should load settings from file
    settings.init()

# Generated at 2022-06-14 08:35:40.045327
# Unit test for method init of class Settings
def test_Settings_init():
    settings.clear()
    settings.init()
    assert settings == const.DEFAULT_SETTINGS
    assert settings.user_dir == Path(__file__).absolute().parent.joinpath('..', '..')



# Generated at 2022-06-14 08:35:50.019605
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import logs
    from .system import create_shell
    from .utils import wrap_settings
    from mock import Mock, call, patch

    args = Mock()
    args.debug = True
    args.yes = True

    _settings = Settings(const.DEFAULT_SETTINGS)
    _settings._init_settings_file = Mock()
    _settings._setup_user_dir = Mock()
    _settings.update = Mock()
    _settings._settings_from_file = Mock()
    _settings._settings_from_env = Mock()
    _settings._settings_from_args = Mock()


# Generated at 2022-06-14 08:35:58.999073
# Unit test for method init of class Settings
def test_Settings_init():
    """
    GIVEN: no requirements
    WHEN: Settings.init() is called and settings.py is created
    THEN: settings.py is created and filled with default settings and settings
            object is filled with default settings
    """
    settings.init()
    assert settings._get_user_dir_path().joinpath('settings.py').is_file()
    user_settings = settings._settings_from_file()
    diff = settings.viewitems() - user_settings.viewitems()
    assert len(diff) == 0


# Generated at 2022-06-14 08:36:07.708375
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init(object)

    assert os.path.exists(settings.user_dir)
    assert os.path.exists(os.path.join(settings.user_dir, 'rules'))
    assert os.path.exists(os.path.join(settings.user_dir, 'settings.py'))
    assert not os.path.exists(os.path.join(settings.user_dir, 'histofy.db'))


# Generated at 2022-06-14 08:36:11.309511
# Unit test for method init of class Settings
def test_Settings_init():
    result = Settings()
    result.init()
    assert result.get('require_confirmation') == True
    assert result.get('no_colors') == False

# Generated at 2022-06-14 08:36:14.926907
# Unit test for method init of class Settings
def test_Settings_init():
    test_settings = Settings()
    test_settings.init()
    assert test_settings['rules']
    assert test_settings['alter_history']
    assert test_settings['require_confirmation']


# Generated at 2022-06-14 08:36:17.409863
# Unit test for method init of class Settings
def test_Settings_init():
    _settings = Settings(const.DEFAULT_SETTINGS)
    _settings.init()
    assert _settings.get('require_confirmation') is True


# Generated at 2022-06-14 08:36:31.662889
# Unit test for method init of class Settings
def test_Settings_init():
    settings.user_dir = '/home/vitalk/.config/thefuck'
    assert settings.init() == {
        'alter_history': True,
        'debug': False,
        'exclude_rules': ['system'],
        'no_colors': False,
        'priority': {},
        'require_confirmation': True,
        'rules': ['git_dirty', 'git_new', 'git_untracked', 'python', 'sudo', 'man'],
        'slow_commands': [],
        'excluded_search_path_prefixes': []
    }
    os.environ['TF_DEBUG'] = 'True'
    os.environ['TF_DONT_ASK_CONFIRMATION'] = 'True'
    os.environ['TF_COLOR_MODE'] = 'False'


# Generated at 2022-06-14 08:36:34.683410
# Unit test for method init of class Settings
def test_Settings_init():
    import thefuck

    settings = thefuck.Settings({})
    settings.init()
    assert settings["repeat"] == False
    assert settings["wait_command"] == 3
    assert settings["no_colors"] == False
    assert settings["history_limit"] == None

# Generated at 2022-06-14 08:36:38.331529
# Unit test for method init of class Settings
def test_Settings_init():
    settings.user_dir = 'test'
    settings._init_settings_file()
    assert settings.user_dir.joinpath('settings.py').is_file()


# Generated at 2022-06-14 08:37:26.325626
# Unit test for method init of class Settings
def test_Settings_init():
    import tempfile
    import shutil

    with tempfile.TemporaryDirectory() as tmpdirname:
        config_path = os.path.join(tmpdirname, '.config')
        os.mkdir(config_path)
        os.environ['XDG_CONFIG_HOME'] = config_path
        settings = Settings()
        settings.init()
        assert settings.user_dir.endswith('.config/thefuck')
        assert settings['rules'] == const.DEFAULT_RULES
        assert settings['require_confirmation'] is True
        assert settings['no_colors'] is False

        # settings from file
        with open(settings.user_dir + '/settings.py', 'w') as f:
            f.write('require_confirmation = False\n')

# Generated at 2022-06-14 08:37:40.383489
# Unit test for method init of class Settings
def test_Settings_init():
    """
    $XDG_CONFIG_HOME is not set.
    $XDG_CONFIG_HOME is set.
    """
    del os.environ['XDG_CONFIG_HOME']
    test_settings = Settings(const.DEFAULT_SETTINGS)
    test_settings.init()

    assert test_settings['require_confirmation'] == True
    assert test_settings['history_limit'] == None
    assert test_settings['alter_history'] == False
    assert test_settings['wait_command'] == 0
    assert test_settings['wait_slow_command'] == 15
    assert test_settings['rules'] == const.DEFAULT_RULES
    assert test_settings['exclude_rules'] == []
    assert test_settings['priority'] == {}
    assert test_settings['no_colors']

# Generated at 2022-06-14 08:37:50.948321
# Unit test for method init of class Settings
def test_Settings_init():
    import argparse

    settings.update(const.DEFAULT_SETTINGS)
    # test from file
    settings.user_dir = 'tests/test_settings'  # without trailing slash
    settings.init()
    for k in const.DEFAULT_SETTINGS.keys():
        assert settings[k] == const.DEFAULT_SETTINGS[k]

    # test from env
    settings.update(const.DEFAULT_SETTINGS)
    os.environ.update({'THEFUCK_WAIT_COMMAND': '10',
                       'THEFUCK_RULES': 'DEFAULT_RULES:first:second',
                       'THEFUCK_PRIORITY': 'first=10:second=0'})
    settings.init()
    assert settings.wait_command == 10
    assert settings.rules == const

# Generated at 2022-06-14 08:37:58.804307
# Unit test for method init of class Settings
def test_Settings_init():
    from .tests import mock

    settings.update({'require_confirmation': True, 'repeat': None})
    args = mock.Mock()
    args.yes = True
    args.debug = True
    args.repeat = 2
    settings.init(args)
    global_settings = copy.deepcopy(const.DEFAULT_SETTINGS)
    global_settings.update({'require_confirmation': False, 'debug': True,
                            'repeat': 2})
    assert settings == global_settings


# Generated at 2022-06-14 08:38:01.452302
# Unit test for method init of class Settings
def test_Settings_init():
    args = lambda val: type('', (object,), {'debug': val})

    settings = Settings()
    settings.init(args(True))
    assert settings['debug']
    try:
        settings.init(args('false'))
    except RuntimeError:
        assert not settings['debug']



# Generated at 2022-06-14 08:38:08.161314
# Unit test for method init of class Settings
def test_Settings_init():
    _settings = Settings()
    _settings['debug'] = True
    _settings['rules'] = ('fuck',)
    _settings['require_confirmation'] = False
    _settings._setup_user_dir()
    _settings._init_settings_file()
    _settings.init()
    assert(settings['debug'])
    assert(settings['rules'] == ('fuck',))
    assert not(settings['require_confirmation'])

    _settings['debug'] = False
    _settings['rules'] = ('fuck',)
    _settings['require_confirmation'] = False
    _settings._setup_user_dir()
    _settings._init_settings_file()
    _settings.init()
    assert not(settings['debug'])
    assert(settings['rules'] == ('fuck',))

# Generated at 2022-06-14 08:38:15.421982
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings.require_confirmation
    assert settings.wait_command == 1
    assert settings.wait_slow_command == 15
    assert settings.history_limit == None
    assert settings.alter_history == False
    assert settings.instant_mode == False
    assert settings.no_colors == False
    assert settings.priority == {}
    assert settings.rules == const.DEFAULT_RULES



# Generated at 2022-06-14 08:38:28.487002
# Unit test for method init of class Settings
def test_Settings_init():
    from mock import patch, Mock, call
    from tempfile import mkdtemp, mkstemp
    from os import remove, environ, close
    from .logs import exception
    import sys

    # Create temp dir and prepare temp files.
    tmp_dir = Path(mkdtemp())
    tmp_path = tmp_dir.joinpath('settings.py')
    fd, tmp_path = mkstemp(text=True)
    tmp_file = open(tmp_path)
    tmp_file.write('FOO = "bar"\n')
    tmp_file.write('BAR = "foo"\n')
    tmp_file.close()

    # Prepare mocked objects.
    mock_path = Mock(spec=Path)
    mock_path.__str__.return_value = str(tmp_path)
    mock_

# Generated at 2022-06-14 08:38:38.463473
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import logger

    _logger = logger
    logger = DummyLogger()
    _user_dir = settings._get_user_dir_path()

    settings._get_user_dir_path = lambda: Path('./test_user')
    settings._settings_from_file = lambda: {'wait_command': 10, 'repeat': True}
    settings._settings_from_env = lambda: {'no_colors': True, 'require_confirmation': False}
    settings._settings_from_args = lambda args: {'alter_history': True}
    settings.init()

    assert settings.user_dir == Path('./test_user')
    assert settings.wait_command == 10
    assert settings.repeat
    assert settings.no_colors
    assert not settings.require_confirmation
    assert settings

# Generated at 2022-06-14 08:38:45.840491
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception

    settings = Settings()
    settings['key'] = 'value'
    settings.update = lambda x: x


# Generated at 2022-06-14 08:39:34.011980
# Unit test for method init of class Settings
def test_Settings_init():
    from mock import patch
    import sys

    _settings = Settings()

    def _mock_init_settings_file():
        _settings.user_dir = None

    def _mock_settings_from_file():
        _settings.user_dir = None
        return {'rules': [],
                'exclude_rules': []}

    def _mock_settings_from_env():
        return {'rules': []}

    def _mock_settings_from_args(args):
        return {'rules': [],
                'exclude_rules': []}


# Generated at 2022-06-14 08:39:41.626807
# Unit test for method init of class Settings
def test_Settings_init():
    """Unit test for method init"""
    # Check version for const.DEFAULT_SETTINGS
    assert const.DEFAULT_SETTINGS.get('version')
    # Check version for settings
    assert settings.get('version')
    # Value of version for const.DEFAULT_SETTINGS must not differ from value of version for settings
    assert const.DEFAULT_SETTINGS.get('version') == settings.get('version')



# Generated at 2022-06-14 08:39:52.955607
# Unit test for method init of class Settings
def test_Settings_init():
    """
    Tests the basic behaviour of the method init.
    All other methods are used are tested separately.
    """
    settings_file = settings.user_dir.joinpath('settings.py')
    with settings_file.open(encoding='utf-8') as settings:
        settings_copy = settings_file.with_suffix('.copy')
        settings_copy.write_text(settings.read())

    # Initialize settings with default values
    settings.init()
    assert settings.user_dir == settings._get_user_dir_path()
    assert settings.settings_file == settings.user_dir.joinpath('settings.py')
    assert settings.settings_file.is_file()
    assert settings.settings_file.read_text() == const.SETTINGS_HEADER

# Generated at 2022-06-14 08:39:58.784722
# Unit test for method init of class Settings
def test_Settings_init():
    global settings
    settings.init()
    class Settings(dict):
        pass
    settings = Settings(settings)
    settings.update(const.DEFAULT_SETTINGS)
    settings.init()
    for key in settings:
        for value in (const.DEFAULT_SETTINGS, settings):
            assert settings[key] == value[key]

# Generated at 2022-06-14 08:40:08.430870
# Unit test for method init of class Settings
def test_Settings_init():
    from mock import patch
    from sys import argv

    with patch('thefuck.settings.Settings._settings_from_file') as from_file,\
            patch('thefuck.settings.Settings._settings_from_env') as from_env,\
            patch('thefuck.settings.Settings._settings_from_args') as from_args,\
            patch('thefuck.settings.Settings._get_user_dir_path') as user_dir:

        user_dir.return_value = Path('.')
        from_file.return_value = {'test': 'test'}
        from_env.return_value = {'test2': 'test2'}
        from_args.return_value = {'test3': 'test3'}

        Settings().init()

        from_file.assert_called_once_with()


# Generated at 2022-06-14 08:40:17.223048
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings(const.DEFAULT_SETTINGS)
    # remove the user config dir if it already exists
    try:
        settings.user_dir.rmdir()
    except OSError:
        pass
    # init() will create the user config dir if it doesn't exist
    settings.init()
    assert settings.user_dir == settings._get_user_dir_path()
    assert settings.require_confirmation == True
    assert settings.history_limit == const.DEFAULT_HISTORY_LIMIT

# Generated at 2022-06-14 08:40:30.249401
# Unit test for method init of class Settings
def test_Settings_init():
    # init with default settings
    settings = Settings(const.DEFAULT_SETTINGS)
    assert settings == const.DEFAULT_SETTINGS
    settings.init()
    assert settings == const.DEFAULT_SETTINGS
    # init with not-default settings
    settings = Settings({'require_confirmation': False, 'repeat': True})
    assert settings.require_confirmation == False
    assert settings.repeat == True
    settings.init()
    assert settings.require_confirmation == False
    assert settings.repeat == True
    # init with env
    settings = Settings(const.DEFAULT_SETTINGS)
    assert settings != {'require_confirmation': False}
    settings.init()
    assert settings != {'require_confirmation': False}
    # init with args

# Generated at 2022-06-14 08:40:36.578705
# Unit test for method init of class Settings
def test_Settings_init():
    test_args = type('Args', (), {'yes': True, 'debug': True, 'repeat': 10})()
    settings.update(const.DEFAULT_SETTINGS)
    settings.init(test_args)
    assert settings.get('require_confirmation') == False
    assert settings.get('debug') == True
    assert settings.get('repeat') == 10

# Generated at 2022-06-14 08:40:50.241004
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception
    from mock import patch

    def _init_settings_file():
        pass

    def _setup_user_dir():
        settings.user_dir = None
        settings.rules = ''
        settings.exclude_rules = ''

    def _settings_from_file():
        return {'rules':'bc:cd:ls'}

    def _settings_from_env():
        return {'exclude_rules':'bc:cd:ls'}

    def _settings_from_args(args):
        return {'require_confirmation':False}


# Generated at 2022-06-14 08:41:03.885422
# Unit test for method init of class Settings