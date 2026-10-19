

# Generated at 2022-06-14 08:31:56.457787
# Unit test for method init of class Settings
def test_Settings_init():
    """
    Testing method init of class Settings
    """
    from .logs import LOGS
    _init_settings_file = Settings._init_settings_file
    _setup_user_dir = Settings._setup_user_dir
    _settings_from_file = Settings._settings_from_file
    _settings_from_args = Settings._settings_from_args
    _settings_from_env = Settings._settings_from_env
    _get_user_dir_path = Settings._get_user_dir_path
    _val_from_env = Settings._val_from_env


# Generated at 2022-06-14 08:32:09.524454
# Unit test for method init of class Settings
def test_Settings_init():
    import os
    import shutil
    from unittest import mock
    from thefuck.settings import const
    from thefuck.settings import Settings
    from thefuck.settings import settings
    from thefuck.tests.utils import TestCase

    user_dir = Path('~/.config/thefuck').expanduser()

    class _Settings(Settings):
        def _settings_from_env(self):
            return {}

        def _settings_from_args(self, args):
            return {}

        def _get_user_dir_path(self):
            return user_dir

    class SettingsTest(TestCase):
        def setUp(self):
            user_dir.mkdir(parents=True)

        def tearDown(self):
            shutil.rmtree(user_dir)

        def test_init(self):
            _

# Generated at 2022-06-14 08:32:11.605923
# Unit test for method init of class Settings
def test_Settings_init():
    pass

# Generated at 2022-06-14 08:32:16.283346
# Unit test for method init of class Settings
def test_Settings_init():
    test_Settings = Settings({})
    test_Settings.init()
    assert hasattr(test_Settings, 'user_dir')
    assert test_Settings['require_confirmation'] == const.DEFAULT_SETTINGS['require_confirmation']


# Generated at 2022-06-14 08:32:27.799520
# Unit test for method init of class Settings
def test_Settings_init():
    # Initialize variable
    user_dir_path_ = 'XDG_CONFIG_HOME/thefuck'
    path_settings_file_ = 'settings.py'
    test_user_dir_ = '/home/pcmagas/.config/thefuck'
    # Get user config dir
    test_user_dir = user_dir_path_.split('/', 1)[1]
    test_user_dir_path = '/home/pcmagas/.'
    test_user_dir_path = test_user_dir_path + test_user_dir
    # Test if user_dir is true
    assert user_dir_path_ == test_user_dir_
    # Test if user_dir_path is true
    assert test_user_dir_path_ == test_user_dir_path
    # Test if the chosen path

# Generated at 2022-06-14 08:32:35.021899
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings()
    settings.init()
    settings.init({'yes': True, 'debug': True, 'repeat': 2})
    assert settings['require_confirmation'] == False
    assert settings['debug'] == True
    assert settings['repeat'] == 2
    # We don't assert the other settings because it's hard to get the current
    # value of the environment variables.

# Generated at 2022-06-14 08:32:43.724422
# Unit test for method init of class Settings
def test_Settings_init():
    import os
    import shutil
    import tempfile
    import unittest

    from mock import patch
    from thefuck import settings

    def get_settings_file(content):
        path = tempfile.mkdtemp()
        settings_path = os.path.join(path, 'settings.py')
        with open(settings_path, 'w') as settings_file:
            settings_file.write(content)
        return path, settings_path


# Generated at 2022-06-14 08:32:46.618953
# Unit test for method init of class Settings
def test_Settings_init():
    cur_settings = Settings(const.DEFAULT_SETTINGS)
    cur_settings.init()
    assert cur_settings == settings



# Generated at 2022-06-14 08:32:57.204886
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import _logger
    from test.factories import create_entry, create_history
    from test.utils import Mock


# Generated at 2022-06-14 08:33:09.341320
# Unit test for method init of class Settings
def test_Settings_init():
    # Variables for _init_settings_file test
    SETTINGS_HEADER = '###This is a default config file###'
    DEFAULT_SETTINGS = {
        'require_confirmation': True,
        'wait_command': 5,
    }
    # Variables for _settings_from_file test
    user_dir = Path.home().joinpath('user_dir')
    settings_content = """
# This is a comment
require_confirmation = False
wait_command = 10
"""
    # Variables for _settings_from_env test
    ENV_TO_ATTR = {
        'THEFUCK_REQUIRE_CONFIRMATION': 'require_confirmation',
        'THEFUCK_WAIT_COMMAND': 'wait_command',
    }

    # Variables for _settings_from_

# Generated at 2022-06-14 08:33:41.100281
# Unit test for method init of class Settings
def test_Settings_init():
    import thefuck
    thefuck.settings = Settings(const.DEFAULT_SETTINGS)
    s = thefuck.settings
    s.init()
    #The only test is to check if paths are set up

    assert (s._get_user_dir_path() == s.user_dir) == s.user_dir.is_dir()
    assert (s._get_user_dir_path().joinpath('settings.py') == s.user_dir.joinpath('settings.py')) == s.user_dir.joinpath('settings.py').is_file()
    assert (s._get_user_dir_path().joinpath('rules') == s.user_dir.joinpath('rules')) == s.user_dir.joinpath('rules').is_dir()
    #Some non-existing directories:

# Generated at 2022-06-14 08:33:51.793314
# Unit test for method init of class Settings
def test_Settings_init():
    from mock import patch, PropertyMock


# Generated at 2022-06-14 08:34:04.155912
# Unit test for method init of class Settings
def test_Settings_init():
    """Tests `Settings.init` method."""
    from .logs import exception
    from mock import patch

    settings._init_settings_file()


# Generated at 2022-06-14 08:34:11.702413
# Unit test for method init of class Settings
def test_Settings_init():
    s = Settings()

    assert s['require_confirmation']
    assert s['repeat']

    s = Settings()
    s.init()

    assert s['require_confirmation']
    assert s['repeat']

    assert s.user_dir
    assert s.user_dir.joinpath('settings.py').is_file()

    s.init(args)

    assert not s['require_confirmation']
    assert not s['repeat']

# Generated at 2022-06-14 08:34:18.181160
# Unit test for method init of class Settings
def test_Settings_init():
    settings.__init__()
    assert settings.get('require_confirmation') == True
    assert settings.get('wait_command') == 5
    assert settings.get('repeat') == False
    assert settings.get('history_limit') == None
    assert settings.get('wait_slow_command') == 15
    assert settings.get('num_close_matches') == 3
    assert settings.get('alter_history') == True
    assert settings.get('instant_mode') == False



# Generated at 2022-06-14 08:34:31.727558
# Unit test for method init of class Settings
def test_Settings_init():
    import types
    import unittest

    import thefuck.settings as s
    from thefuck.tests.utils import create_file, create_files

    _init_settings_file = s.Settings.init

    class SettingsInitTest(unittest.TestCase):
        def setUp(self):
            self.init = s.Settings.init

            # Make sure the settings file is present
            self.user_dir = '/tmp/thefuck-test'
            create_files(self.user_dir, 'settings.py')

            s.settings.init()
            s.settings.user_dir = Path(self.user_dir)

            s.Settings.init = _init_settings_file

        def tearDown(self):
            s.Settings.init = self.init


# Generated at 2022-06-14 08:34:44.776444
# Unit test for method init of class Settings
def test_Settings_init():
    # Test init with empty input
    settings.update(const.DEFAULT_SETTINGS)
    settings.init()
    for key in const.DEFAULT_SETTINGS.keys():
        assert settings[key] == const.DEFAULT_SETTINGS[key]

    # Test init with args and environment variables
    # Save current settings in variables
    old_settings = dict()
    for key in const.DEFAULT_SETTINGS.keys():
        old_settings[key] = settings[key]

    old_user_dir = settings.user_dir

    from argparse import Namespace
    # Create mock args
    args = Namespace()
    args.yes = True
    args.debug = True
    args.repeat = True

    # Create mock environment variables
    import tempfile
    tempdir = tempfile.mkdtemp()
   

# Generated at 2022-06-14 08:34:52.094760
# Unit test for method init of class Settings
def test_Settings_init():
    temp_dir = Path("/tst")
    settings._setup_user_dir = lambda: None
    settings._init_settings_file = lambda: None
    settings._settings_from_file = lambda: {"environ_key": "environ_value"}
    settings._settings_from_env = lambda: {"environ_key": "environ_value"}
    settings._settings_from_args = lambda x: {"arg_key": "arg_value"}
    assert settings.init() == {"arg_key": "arg_value", "environ_key": "environ_value"}

# Generated at 2022-06-14 08:34:54.555369
# Unit test for method init of class Settings
def test_Settings_init():
    settings.update(
        {'rules': ['fuck1', 'fuck2', 'fuck3']})
    assert settings['rules'] == ['fuck1', 'fuck2', 'fuck3']

# Generated at 2022-06-14 08:35:06.635425
# Unit test for method init of class Settings
def test_Settings_init():
    settings_test = Settings(const.DEFAULT_SETTINGS)
    settings_test._get_user_dir_path = lambda: Path('~/.thefuck_test')
    settings_test._setup_user_dir()

    assert settings_test.user_dir == Path('~/.thefuck_test').expanduser()

    settings_path = settings_test.user_dir.joinpath('settings.py')
    if settings_path.is_file():
        settings_path.unlink()

    settings_test.init()

    assert settings_test.user_dir == Path('~/.thefuck_test').expanduser()

    assert settings_path.is_file()
    with settings_path.open() as f:
        text = f.read()

    assert text == const.SETTINGS_HEADER

# Generated at 2022-06-14 08:36:00.947489
# Unit test for method init of class Settings
def test_Settings_init():
    args = type('', (), {})
    settings.init(args)
    settings.get('repeat').should.be.none
    settings.get('require_confirmation').should.be.true
    settings.get('debug').should.be.false

    args.yes = True
    settings.init(args)
    settings.get('require_confirmation').should.be.false

    args.debug = True
    settings.init(args)
    settings.get('debug').should.be.true

    args.repeat = 3
    settings.init(args)
    settings.get('repeat').should.be(3)

    args.yes = False
    settings.init(args)
    settings.get('require_confirmation').should.be.true

# Generated at 2022-06-14 08:36:14.064654
# Unit test for method init of class Settings
def test_Settings_init():
    orig_user_dir = settings.user_dir
    orig_debug = settings.debug
    orig_require_confirmation = settings.require_confirmation

    sys.argv = ['thefuck']
    settings.init()
    assert settings.user_dir == orig_user_dir
    assert settings.debug == orig_debug
    assert settings.require_confirmation == orig_require_confirmation

    _user_dir = Path('.')
    sys.argv = ['thefuck', '--settings-path', 'settings.py']
    settings.init()
    assert settings.user_dir == _user_dir.joinpath('settings.py').dirname()
    assert settings.debug == orig_debug
    assert settings.require_confirmation == orig_require_confirmation

    _user_dir = Path('.')
    sys.argv

# Generated at 2022-06-14 08:36:20.380643
# Unit test for method init of class Settings
def test_Settings_init():
    s = Settings(const.DEFAULT_SETTINGS)
    args = Mock()
    args.debug = False
    args.yes = False
    args.repeat = 1

# Generated at 2022-06-14 08:36:33.395152
# Unit test for method init of class Settings
def test_Settings_init():
    # init successfully
    sys.argv = ['thefuck', 'Control-t', 'git', 'status', '--']
    settings.init()
    assert settings.match_type == 'fuzzy'
    assert settings.wait_command == 3
    assert settings.history_limit == 10
    assert settings.require_confirmation == const.DEFAULT_SETTINGS['require_confirmation']
    assert settings.shell == 'bash'
    assert settings.wait_slow_command == 15
    assert settings.slow_commands == const.DEFAULT_SETTINGS['slow_commands']
    assert settings.alter_history == const.DEFAULT_SETTINGS['alter_history']
    assert settings.exclude_rules == []
    assert settings.priority == {}
    assert settings.num_close_matches == 3
    assert settings.inst

# Generated at 2022-06-14 08:36:44.603409
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception
    settings = Settings()
    settings._settings_from_env = lambda: {'rule': 'rule'}
    settings._settings_from_file = lambda: {'rules': 'rules', 'require_confirmation': True}
    settings._settings_from_args = lambda args: {'require_confirmation': False}
    with settings.user_dir.joinpath('settings.py').open(mode='w') as settings_file:
        settings_file.write(const.SETTINGS_HEADER)

    settings.init()
    assert settings.rule == 'rule'
    assert settings.rules == 'rules'
    assert settings.require_confirmation == False

    settings._settings_from_args = lambda args: {'rules': 'from_args'}
    settings.init()

# Generated at 2022-06-14 08:36:53.722354
# Unit test for method init of class Settings
def test_Settings_init():
    if os.environ.get('THEFUCK_SETTINGS_FROM_ENV'):
        del os.environ['THEFUCK_SETTINGS_FROM_ENV']
    if os.environ.get('THEFUCK_EXCLUDE_RULES_FROM_ENV'):
        del os.environ['THEFUCK_EXCLUDE_RULES_FROM_ENV']
    if os.environ.get('THEFUCK_PRIORITY_FROM_ENV'):
        del os.environ['THEFUCK_PRIORITY_FROM_ENV']

# Generated at 2022-06-14 08:37:03.378772
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings()
    # Test settings from args
    settings.init(args=lambda: None)
    assert settings['require_confirmation']
    settings.init(args=lambda: None)
    assert settings['require_confirmation']


    settings.init(args=lambda: setattr(args, 'yes', True))
    assert not settings['require_confirmation']
    settings.init(args=lambda: setattr(args, 'yes', False))
    assert settings['require_confirmation']


    settings.init(args=lambda: setattr(args, 'debug', True))
    assert settings['debug']
    settings.init(args=lambda: setattr(args, 'debug', False))
    assert not settings['debug']


    settings.init(args=lambda: setattr(args, 'repeat', 0))
    assert settings

# Generated at 2022-06-14 08:37:10.369846
# Unit test for method init of class Settings
def test_Settings_init():
    import mock
    import sys
    import six

    class TestSettings(Settings):
        def __init__(self, *args):
            super(TestSettings, self).__init__(*args)
            self.user_dir = Path('/tmp/thefuck-test')
        def _settings_from_file(self):
            return {}
        def _settings_from_env(self):
            return {}
        def _settings_from_args(self, args):
            return {}

    os.system(six.u('rm -rf /tmp/thefuck-test'))

    settings = TestSettings(const.DEFAULT_SETTINGS)

# Generated at 2022-06-14 08:37:20.116612
# Unit test for method init of class Settings
def test_Settings_init():
    # check that user dir exists and that settings file is created
    settings.user_dir.rmdir()
    settings.init()
    assert settings.user_dir.is_dir()

    with settings.user_dir.joinpath('settings.py').open() as settings_file:
        assert settings_file.read().startswith(const.SETTINGS_HEADER)

    # delete settings file
    settings.user_dir.joinpath('settings.py').unlink()
    settings.init()
    assert settings.user_dir.joinpath('settings.py').is_file()

    # check that we load settings from file
    with settings.user_dir.joinpath('settings.py').open(mode='w') as settings_file:
        settings_file.write(u"rules = ['rule1', 'rule2']\n")

# Generated at 2022-06-14 08:37:27.957735
# Unit test for method init of class Settings
def test_Settings_init():
    # Test all of the settings passed from env and from args
    from argparse import Namespace
    test_args = Namespace(yes=True, debug=True, repeat=True)
    settings.init(test_args)

# Generated at 2022-06-14 08:38:58.043406
# Unit test for method init of class Settings
def test_Settings_init():
    # this test is to ensure Settings.init will not raise exception
    # and the settings variable has value of 'const.DEFAULT_SETTINGS'
    # after being initialized
    global settings

    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init(None)

    assert settings == const.DEFAULT_SETTINGS

# Generated at 2022-06-14 08:39:04.291630
# Unit test for method init of class Settings
def test_Settings_init():
    from thefuck.rules.git import git_add_command
    from thefuck.rules.man import man_command
    import thefuck
    def test_setting_from_file(settings_file, env_val, params,
                               expected_settings):
        from thefuck import settings
        from .logs import logger
        from .system import Path
        from .utils import import_path
        def mock_settings_from_file(settings):
            return settings_file

        def mock_settings_from_env(env_val):
            return env_val

        def mock_settings_from_args(params):
            return params

        import_path('thefuck.settings._settings_from_args')\
            .side_effect = mock_settings_from_args

# Generated at 2022-06-14 08:39:16.381892
# Unit test for method init of class Settings
def test_Settings_init():
    # pylint: disable=unused-variable
    import sys
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.update({'user_dir': Path('./dir')})
    settings.update({'_init_settings_file': lambda: False})
    settings.update({'_settings_from_file': lambda: False})
    settings.update({'_settings_from_env': lambda: False})
    settings.update({'_settings_from_args': lambda args: {'require_confirmation': False}})
    settings.update({'require_confirmation': False})
    settings.update({'rules': ['sed', 'python']})
    settings.update({'exclude_rules': []})
    settings.update({'priority': {'sed': 100, 'python': 99}})

# Generated at 2022-06-14 08:39:29.551213
# Unit test for method init of class Settings
def test_Settings_init():
    """Check that result of method `init` of class `Settings` is correct"""
    from .logs import exception

    def side_effect(name):
        if name == 'settings':
            return 'settings.py'
        elif name == 'thefuck.settings':
            return {'rules': 'BASE_RULES', 'history_limit': 10,
                    'require_confirmation': 'True',
                    'exclude_rules': 'DEFAULT_RULES',
                    'wait_slow_command': '10'}
        elif name == 'XDG_CONFIG_HOME':
            return '~/.config'
        elif name == 'THEFUCK_RULES':
            return 'base'

# Generated at 2022-06-14 08:39:34.052037
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    user_dir = settings._get_user_dir_path()
    settings_path = user_dir.joinpath('settings.py')
    assert settings.user_dir == user_dir
    assert settings_path.is_file()
    assert settings.get('require_confirmation') == True

# Generated at 2022-06-14 08:39:46.961222
# Unit test for method init of class Settings
def test_Settings_init():
    import unittest
    from .tests.utils import (
        TEST_ENV_VARIABLES,
        reset_env,
        set_env,
        restore_env,
        no_colors
    )

    @no_colors
    class SettingsInitTests(unittest.TestCase):

        def setUp(self):
            reset_env()
            self.save_env_variables = {}

        def tearDown(self):
            restore_env(self.save_env_variables)

        def test_init_should_return_default_values_when_settings_file_is_empty(
                self):
            settings.user_dir.joinpath('settings.py').remove()

            settings.init(None)

            self.assertEqual(const.DEFAULT_SETTINGS, settings)



# Generated at 2022-06-14 08:39:55.339144
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import ColoredFormatter

    settings.init(args=None)
    assert settings.alter_history
    assert settings.require_confirmation
    assert settings.slow_commands == const.DEFAULT_SLOW_COMMANDS
    assert settings.wait_command == const.DEFAULT_WAIT_COMMAND
    assert settings.wait_slow_command == const.DEFAULT_WAIT_SLOW_COMMAND
    assert settings.history_limit == const.DEFAULT_HISTORY_LIMIT
    assert settings.no_colors is False
    assert settings.priority == const.DEFAULT_PRIORITY
    assert settings.rules == const.DEFAULT_RULES
    assert settings.exclude_rules == []
    assert settings.excluded_search_path_prefixes == []
    assert settings.num_close

# Generated at 2022-06-14 08:40:03.669121
# Unit test for method init of class Settings
def test_Settings_init():
    # clear environment variables for testing
    for env in const.ENV_TO_ATTR.keys():
        if env in os.environ:
            del os.environ[env]

    # create `settings.py` file with some config

# Generated at 2022-06-14 08:40:10.274184
# Unit test for method init of class Settings
def test_Settings_init():
    args = lambda: None
    setattr(args, 'yes', True)
    setattr(args, 'repeat', 3)
    setattr(args, 'debug', True)
    def getenv(x):
        return {'THEFUCK_REQUIRE_CONFIRMATION': 'False',
                'THEFUCK_RULES': 'git,tmux',
                'THEFUCK_PRIORITY': 'git=999'}.get(x)
    setattr(os, 'getenv', getenv)

    settings.init(args)
    assert settings.require_confirmation is False
    assert settings.rules == ['git', 'tmux', 'python']
    assert settings.priority == {'git': 999}
    assert settings.repeat == 3
    assert settings.debug is True

test_Settings_init()

# Generated at 2022-06-14 08:40:22.586310
# Unit test for method init of class Settings
def test_Settings_init():
    args_namespace = type('args_namespace', (), {})()
    for key, val in const.ENV_TO_ATTR.items():
        os.environ[key] = str(val)
    for key, val in const.DEFAULT_SETTINGS.items():
        setattr(args_namespace, key, val)
    args_namespace.yes = True
    args_namespace.debug = True
    args_namespace.repeat = True

    settings.update(const.DEFAULT_SETTINGS)
    settings.update({key: val for key, val in zip(const.DEFAULT_SETTINGS.keys(),
                                                 const.ENV_TO_ATTR.values())})
    settings['require_confirmation'] = False
    settings['debug'] = True
    settings['repeat'] = True
