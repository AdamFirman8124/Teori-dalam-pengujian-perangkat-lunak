

# Generated at 2022-06-14 08:31:50.197888
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception, log_to_file, set_log

    log_calls = []
    log_to_file = lambda msg: log_calls.append(msg)
    set_log = lambda: None
    exception = lambda msg, exc: log_calls.append(
        "{}: {}".format(msg, exc[1]))

    try:
        import xdg.BaseDirectory
    except ImportError:
        def xdg_BaseDirectory_xdg_config_home(fallback):
            return '~/.config'
        xdg.BaseDirectory.xdg_config_home = xdg_BaseDirectory_xdg_config_home

    import tempfile
    import shutil
    import sys
    import os

    class Args(object):
        def __init__(self):
            self

# Generated at 2022-06-14 08:31:57.422654
# Unit test for method init of class Settings
def test_Settings_init():
    settings_test_path = './tests/settings_test.py'
    if os.path.isfile(settings_test_path):
        os.remove(settings_test_path)
    settings.init()
    assert os.path.isfile(settings_test_path)
    settings.init()
    assert settings.get('history_limit') == 100
    assert settings.get('exclude_rules') == []
    assert settings.get('require_confirmation') == True
    assert settings.get('no_colors') == False
    if os.path.isfile(settings_test_path):
        os.remove(settings_test_path)


# Generated at 2022-06-14 08:32:10.260450
# Unit test for method init of class Settings
def test_Settings_init():
    s = Settings()
    s.init()
    assert s.nosuggest == const.DEFAULT_SETTINGS['nosuggest']
    assert s.user_dir == settings.user_dir
    assert s.require_confirmation == const.DEFAULT_SETTINGS['require_confirmation']
    assert s.repeat == const.DEFAULT_SETTINGS['repeat']
    assert s.wait_slow_command == const.DEFAULT_SETTINGS['wait_slow_command']
    assert s.wait_command == const.DEFAULT_SETTINGS['wait_command']
    assert s.alter_history == const.DEFAULT_SETTINGS['alter_history']
    assert s.wait_slow_command == const.DEFAULT_SETTINGS['wait_slow_command']
    assert s.no_colors == const.DEFAULT_SET

# Generated at 2022-06-14 08:32:22.277608
# Unit test for method init of class Settings
def test_Settings_init():
    from mock import Mock
    from .system import Path
    from .utils import wrap_streams
    from .logs import exception

    settings.init()
    assert settings.user_dir == Path('.config', 'thefuck').expanduser()
    settings.init()
    settings.user_dir.joinpath('rules').rmdir()
    assert settings.user_dir == Path('.config', 'thefuck').expanduser()

    with open(settings.user_dir.joinpath('settings.py'), 'w') as file:
        file.write('ERROR')

    with wrap_streams([], ['error message']):
        settings.init()

    assert settings._settings_from_file() == {'require_confirmation': True}
    assert settings._settings_from_env() == {}


# Generated at 2022-06-14 08:32:35.835356
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings(const.DEFAULT_SETTINGS)

# Generated at 2022-06-14 08:32:44.005104
# Unit test for method init of class Settings
def test_Settings_init():
    import tempfile
    import shutil

    # Creates a temporary directory and a file and a variable `temp_dir`
    temp_dir = tempfile.mkdtemp()
    temp_file = tempfile.NamedTemporaryFile()
    # Adds a variable `XDG_CONFIG_HOME` to env
    os.environ['XDG_CONFIG_HOME'] = temp_dir
    # Initializes a Settings object
    settings.init()
    # Checks the user_dir is the same as the `temp_dir`
    assert settings.user_dir == Path(temp_dir, 'thefuck')
    # Checks the rules_dir is the same as the `temp_dir`
    assert settings.user_dir.joinpath('rules') == Path(temp_dir, 'thefuck', 'rules')
    # Checks the rules_dir

# Generated at 2022-06-14 08:32:55.123733
# Unit test for method init of class Settings
def test_Settings_init():
    def mock_getattr(self, attr):
        if attr == '_settings_from_file':
            return lambda: {'rules': ['fuck'], 'wait_command': 3}
        elif attr == '_settings_from_env':
            return lambda: {'rules': ['bash'], 'require_confirmation': 'true'}
        elif attr == '_settings_from_args':
            return lambda: {'require_confirmation': 'false'}

    settings = Settings(const.DEFAULT_SETTINGS)
    settings.__getattr__ = mock_getattr
    settings.init()
    assert settings['rules'] == ['bash', 'fuck']
    assert not settings['require_confirmation']

# Generated at 2022-06-14 08:33:08.381303
# Unit test for method init of class Settings
def test_Settings_init():
    """Test for method init of class Settings."""
    from .logs import exception
    from .conf import settings
    from .utils import get_closest
    from .system import get_aliases, get_shell

    def _test_settings():
        """Test settings."""
        # Default settings
        assert settings.alter_history
        assert settings.require_confirmation
        assert settings.wait_command == 1
        assert not settings.no_colors
        assert settings.priority == {
            'same_file': 1,
            'get_aliases': 2,
            'get_shell': 3
        }
        assert settings.rules == const.DEFAULT_RULES
        assert settings.exclude_rules == const.DEFAULT_EXCLUDE_RULES
        assert settings.wait_slow_command == 15

# Generated at 2022-06-14 08:33:11.328677
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init(object)
    assert settings.require_confirmation == True
    assert settings.wait_command == 0
    assert settings.slow_commands == [
        'sudo', 'apt-get', 'brew', 'emerge', 'git']



# Generated at 2022-06-14 08:33:14.556397
# Unit test for method init of class Settings
def test_Settings_init():
    settings_ = Settings(const.DEFAULT_SETTINGS)
    settings_.init()
    settings_.get("require_confirmation") == True

# Generated at 2022-06-14 08:33:42.127398
# Unit test for method init of class Settings
def test_Settings_init():
    def mock_settings_from_file(self):
        return {'require_confirmation': True}

    def mock_settings_from_env(self):
        return {'require_confirmation': False}

    def mock_settings_from_args(self, args):
        return {'require_confirmation': False, 'debug': True}

    settings._settings_from_file = mock_settings_from_file
    settings._settings_from_env = mock_settings_from_env
    settings._settings_from_args = mock_settings_from_args

    settings.init(args=Mock(yes=True, debug=True, repeat=1))
    assert settings['require_confirmation'] == False
    assert settings['debug'] == True
    assert settings['repeat'] == 1



# Generated at 2022-06-14 08:33:48.369521
# Unit test for method init of class Settings
def test_Settings_init():
    import sys
    from .system import path_from_module

    settings = Settings(const.DEFAULT_SETTINGS)
    sys.modules.pop("settings", None)
    user_dir = path_from_module("settings")
    settings.user_dir = user_dir
    settings.init()

    assert settings.require_confirmation is True
    assert settings.alt_src_len == 0
    assert settings.no_colors is False



# Generated at 2022-06-14 08:34:00.231196
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    
    # assert settings.rules == const.DEFAULT_RULES
    # assert settings.exclude_rules == []
    # assert settings.priority == {}
    # assert settings.require_confirmation is True
    # assert settings.no_colors is False
    # assert settings.debug is False
    # assert settings.wait_command is 1
    # assert settings.history_limit == 0
    # assert settings.wait_slow_command is 15
    # assert settings.slow_commands == []
    # assert settings.excluded_search_path_prefixes == []
    assert settings.alter_history is True
    assert settings.instant_mode is False
    assert settings.num_close_matches == 3

# Generated at 2022-06-14 08:34:13.578636
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception

    args = Mock(yes=True, debug=True, repeat=4)
    settings_from_file = {'require_confirmation': False, 'debug': False, 'repeat': 1}
    settings_from_env = {'no_colors': True, 'history_limit': 10}
    settings_from_args = {'require_confirmation': False, 'debug': True, 'repeat': 4}
    settings = Mock(user_dir='/tmp/foo', repeat=1, **settings_from_file)

    settings.init(args)

    settings._setup_user_dir.assert_called_once_with()
    settings._init_settings_file.assert_called_once_with()

# Generated at 2022-06-14 08:34:21.579985
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception
    from .notify import Notifier
    from .rules import get_rules
    from .exceptions import NoRuleMatched
    from .shells import Bash, Zsh
    from .utils import init_logger, replace_argument
    import os
    import sys
    import unittest
    import mock

    warnings_mock = mock.Mock()
    warn_mock = mock.Mock()
    exception_mock = mock.Mock()

    class SettingsInitTests(unittest.TestCase):
        settings_file = settings_file_content = user_dir = home_dir = \
            bash_history = rules = notifier = settings_from_file = \
            rules_from_env = priority_from_env = None
        settings_from_env = settings_from_args = None

# Generated at 2022-06-14 08:34:33.908646
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception
    from .system import Path

    settings._setup_user_dir = lambda: '/user/dir'
    settings._settings_from_file = lambda: {'rules': 'first_rule',
                                            'exclude_rules': 'first_exclude_rule'}
    settings._settings_from_env = lambda: {'rules': 'second_rule',
                                           'exclude_rules': 'second_exclude_rule'}
    settings._settings_from_args = lambda: {'rules': 'third_rule',
                                            'exclude_rules': 'third_exclude_rule'}

    exception_mock = MagicMock()
    exception.side_effect = exception_mock
    settings.init()
    assert settings['rules'] == 'third_rule'

# Generated at 2022-06-14 08:34:35.506182
# Unit test for method init of class Settings
def test_Settings_init():
    settings._init_settings_file()
    settings.init()

# Generated at 2022-06-14 08:34:49.748832
# Unit test for method init of class Settings
def test_Settings_init():
    os.environ['THEFUCK_REQUIRE_CONFIRMATION'] = 'true'
    os.environ['THEFUCK_RULES'] = 'DEFAULT_RULES'
    os.environ['THEFUCK_EXCLUDE_RULES'] = ''
    os.environ['THEFUCK_PRIORITY'] = 'bash=42'
    os.environ['THEFUCK_WAIT_COMMAND'] = '2'
    os.environ['THEFUCK_HISTORY_LIMIT'] = '1'
    os.environ['THEFUCK_WAIT_SLOW_COMMAND'] = '3'
    os.environ['THEFUCK_SLOW_COMMANDS'] = 'git:hg:svn'

# Generated at 2022-06-14 08:34:58.204320
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception
    from .system import Path

    class FakeArg:
        def __init__(self, yes=False, debug=False, repeat=None):
            self.yes = yes
            self.debug = debug
            self.repeat = repeat

    class FakeSettings:
        class _settings_from_file:
            correct = None

        class _settings_from_env:
            correct = None

    settings = Settings({})

    # If no error raises, then `settings` will be cleared.
    settings.init()
    assert settings == {}

    # If error raises, then `settings` will be unchanged.
    settings.init(FakeArg(yes=True))
    assert settings == {}


# Generated at 2022-06-14 08:35:09.228949
# Unit test for method init of class Settings
def test_Settings_init():
    import tempfile
    settings = {}
    settings_file = os.path.join(tempfile.gettempdir(), 'settings.py')
    with open(settings_file, 'w') as settings_file:
        settings_file.write('rules = ["ls"]\n')
    os.environ['THEFUCK_REQUIRE_CONFIRMATION'] = 'False'
    os.environ['THEFUCK_RULES'] = 'git:python'
    os.environ['THEFUCK_PRIORITY'] = 'git=77:python=88'
    os.environ['THEFUCK_ALTER_HISTORY'] = 'True'
    os.environ['THEFUCK_EXCLUDE_RULES'] = 'ls'

# Generated at 2022-06-14 08:35:27.808083
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()

# Generated at 2022-06-14 08:35:34.624709
# Unit test for method init of class Settings
def test_Settings_init():
    import mock
    from tests.utils import assert_equals

    settings.init(mock.Mock())
    assert_equals(settings.user_dir.expanduser(), '~/.config/thefuck')
    assert_equals(
        settings.user_dir.joinpath('settings.py').expanduser(),
        '~/.config/thefuck/settings.py')

# Generated at 2022-06-14 08:35:43.645069
# Unit test for method init of class Settings
def test_Settings_init():
    os.environ['THEFUCK_RULES'] = 'DEFAULT_RULES:some_rules'
    os.environ['THEFUCK_REQUIRE_CONFIRMATION'] = 'true'
    os.environ['THEFUCK_WAIT_COMMAND'] = '0'
    os.environ['THEFUCK_PRIORITY'] = 'some_rules=100:some_other_rules=200'
    os.environ['THEFUCK_SLOW_COMMANDS'] = 'some:nope:slow:commands'
    os.environ['THEFUCK_WAIT_SLOW_COMMAND'] = '10'
    os.environ['THEFUCK_ALTER_HISTORY'] = 'true'
    os.environ['THEFUCK_EXCLUDE_RULES']

# Generated at 2022-06-14 08:35:52.954523
# Unit test for method init of class Settings
def test_Settings_init():
    """
    Test setting.init()
    """
    import pytest

    settings.init()
    assert settings.user_dir == Path(settings._get_user_dir_path())
    assert settings.history_limit == 20

    # if XDG_CONFIG_HOME is set, use it
    os.environ['XDG_CONFIG_HOME'] = 'config path'
    settings.init()
    assert settings.user_dir == Path(settings._get_user_dir_path())
    assert settings.user_dir == Path('config path', 'thefuck')

    # no exception raised
    os.environ['XDG_CONFIG_HOME'] = 'config path'
    os.environ['THEFUCK_RULES'] = 'DEFAULT_RULES'

# Generated at 2022-06-14 08:35:57.530036
# Unit test for method init of class Settings
def test_Settings_init():
    """
    >>> from .system import Path
    >>> settings.init(None)
    >>> settings.user_dir == Path('~/.thefuck').expanduser()
    True
    """
    settings.clear()
    settings.init(None)
    assert settings.user_dir == Path('~/.thefuck').expanduser()
    settings.clear()

# Generated at 2022-06-14 08:36:05.849545
# Unit test for method init of class Settings
def test_Settings_init():
    import argparse
    settings.init(argparse.Namespace())
    assert settings.history_limit == const.DEFAULT_SETTINGS['history_limit']
    settings.init(argparse.Namespace(yes=False))
    assert settings.require_confirmation is False
    settings.init(argparse.Namespace(debug=True))
    assert settings.debug is True
    settings.init(argparse.Namespace(repeat=10))
    assert settings.repeat == 10

    # Test legacy settings file
    settings.init() # restore defaults
    legacy_settings_file = Path('~/.thefuck/settings.py').expanduser()
    legacy_settings_file.write_text(
        'wrong_command_interval = 1\n'
        'repeat = 2\n')
    settings.init()
    assert settings.wrong

# Generated at 2022-06-14 08:36:14.286522
# Unit test for method init of class Settings
def test_Settings_init():
    # When I call init method
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()

    # Then it should have values from file and env
    from_file = settings._settings_from_file()
    from_env = settings._settings_from_env()
    for key, _ in const.DEFAULT_SETTINGS.items():
        assert settings[key] == from_env[key] or settings[key] == from_file[key]


# Generated at 2022-06-14 08:36:20.995262
# Unit test for method init of class Settings
def test_Settings_init():
    os.environ['TF_REQUIRE_CONFIRMATION'] = 'false'
    os.environ['TF_DEBUG'] = 'true'
    os.environ['TF_RULES'] = ':'.join(['f', 's', 'DEFAULT_RULES', 'p'])
    os.environ['TF_PRIORITY'] = 'f=9:s=1:p=2'

    settings.init(None)

    assert not settings.require_confirmation
    assert settings.debug

# Generated at 2022-06-14 08:36:33.712930
# Unit test for method init of class Settings
def test_Settings_init():
    # *_from_env returns dict with key and value from const.ENV_TO_ATTR
    # *_from_file returns dict with key and value from const.ENV_TO_ATTR
    # *_from_args returns dict with key and value from const.ENV_TO_ATTR

    # test if init runs correctly when all functions returns dict
    # with key and value from const.ENV_TO_ATTR
    # and args.yes, args.debug and args.repeat = False
    # In this case dicts with key and value from const.ENV_TO_ATTR
    # are in settings
    settings_from_env = {env: attr for env, attr in const.ENV_TO_ATTR.items()}

# Generated at 2022-06-14 08:36:44.427672
# Unit test for method init of class Settings
def test_Settings_init():
    def _settings_from_file():
        return {'require_confirmation': False, 'rules': ['ls']}
    def _settings_from_env():
        return {'require_confirmation': True}
    def _settings_from_args(args=None):
        return {'require_confirmation': False, 'repeat': 3}
    settings.init = _settings_from_file
    settings.init = _settings_from_env
    settings.init = _settings_from_args
    settings.init()
    assert settings['require_confirmation'] == False
    assert settings['rules'] == ['ls']
    assert settings['repeat'] == 3

# Generated at 2022-06-14 08:37:02.795144
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()

# Generated at 2022-06-14 08:37:11.962495
# Unit test for method init of class Settings
def test_Settings_init():
    import tempfile, shutil

    args = None
    user_dir, settings_path = tempfile.mkdtemp(), os.path.join(tempfile.mkdtemp(), 'settings.py')

    os.environ['TF_INSTANT_MODE'] = 'True'


# Generated at 2022-06-14 08:37:13.350304
# Unit test for method init of class Settings
def test_Settings_init():
    assert settings.init() is None


# Generated at 2022-06-14 08:37:25.227382
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception
    from .system import Path
    from unittest import TestCase
    from unittest.mock import patch

    class TestSettings(Settings):
        def _init_settings_file(self):
            pass

        def _setup_user_dir(self):
            self.user_dir = Path('.')

    def exception_callback(*args):
        pass

    class TestCase(TestCase):
        @classmethod
        def setUpClass(cls):
            settings.clear()

        @classmethod
        def tearDownClass(cls):
            settings.clear()


# Generated at 2022-06-14 08:37:39.404688
# Unit test for method init of class Settings
def test_Settings_init():
    """
    Method Settings.init fills the `settings` object with values from
    `settings.py` and env.
    """
    import tempfile
    import shutil
    import os

    os.environ['XDG_CONFIG_HOME'] = tempfile.mkdtemp()
    os.environ['THEFUCK_REQUIRE_CONFIRMATION'] = 'False'
    os.environ['THEFUCK_PRIORITY'] = 'fuck=9000'
    os.environ['THEFUCK_RULES'] = 'fuck:DEFAULT_RULES:bar'
    os.environ['THEFUCK_SLOW_COMMANDS'] = 'foo:bar'
    os.environ['THEFUCK_EXCLUDE_RULES'] = 'fuu:bar'

# Generated at 2022-06-14 08:37:50.023713
# Unit test for method init of class Settings
def test_Settings_init():
    def TestSettingsFile():
        os.chdir(os.path.expanduser('~'))
        test_folder = os.path.join(os.getcwd(), '.thefuck_test')
        test_settings_file = os.path.join(test_folder, 'settings.py')
        os.mkdir(test_folder)
        settings.user_dir = Path(test_folder)
        settings._init_settings_file()
        assert os.path.isfile(test_settings_file)
        os.remove(test_settings_file)
        os.rmdir(test_folder)

    def TestSettingsFromFile():
        settings.user_dir = Path('.')
        with open('settings.py', 'w') as f:
            f.write('require_confirmation = False')
        assert settings._

# Generated at 2022-06-14 08:38:01.004414
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import _exception
    from .system import Path
    from .utils import _get_history_file_name
    import sys
    import os

    sys.argv = ['thefuck', 'ssh']
    _exception = lambda e, info: None
    settings_path = Path('~/.config/thefuck/settings.py').expanduser()
    history_file = Path(_get_history_file_name()).expanduser()
    test_python_path = 'test-python-path'

    # If no user dir, create one and settings file
    settings.user_dir = None
    settings.init()
    assert settings.user_dir == Path('~/.config/thefuck').expanduser()
    assert settings_path.is_file()

    # If settings file doesn't exist, create it
    settings

# Generated at 2022-06-14 08:38:13.919494
# Unit test for method init of class Settings
def test_Settings_init():
    from test.output_collector import OutputCollector
    from test.utils import cd
    from test.captured_input import CapturedInput
    from . import logs
    from .logs import EXCEPTIONS

    logs.EXCEPTION = EXCEPTIONS.append
    logs.EXCEPTIONS = EXCEPTIONS

    with cd('test/test-data/empty-dir'):
        with CapturedInput(), OutputCollector():
            settings.init()
            assert settings.user_dir == Path('~/.config/thefuck').expanduser()
            assert settings.user_dir.joinpath('rules').is_dir()
            assert settings.user_dir.joinpath(
                'settings.py').read_text() == const.SETTINGS_HEADER



# Generated at 2022-06-14 08:38:18.894090
# Unit test for method init of class Settings
def test_Settings_init():
    args = type('Args', (), {'yes': True, 'debug': True})()
    settings.init(args)
    assert settings['require_confirmation'] == False
    assert settings['debug'] == True

# Generated at 2022-06-14 08:38:30.651372
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import logger

    def mock_logger_exception(msg, *args):
        assert msg == 'Can\'t load settings from env'
        assert len(args) == 1

    def mock_logger_warning(msg):
        assert msg == 'Config path {Path(u\'~/.thefuck\')} is deprecated. Please move to {Path(u\'~/.config/thefuck\')}'.format(**locals())

    def mock_logger_exception_msg(msg):
        return mock_logger_exception(msg)

    def mock_logger_warning_msg(msg):
        return mock_logger_warning(msg)

    def mock_logger_exception_msg_args(msg, *args):
        return mock_logger_exception(msg, *args)


# Generated at 2022-06-14 08:39:02.022045
# Unit test for method init of class Settings
def test_Settings_init():
    from StringIO import StringIO
    sys.stdout = StringIO()
    settings.init()
    assert settings.user_dir == Path.home().joinpath('.thefuck')
    assert settings.require_confirmation == True
    assert settings.rules == ['git_push', 'git_add', 'git_commit', 'pip_install',
                              'gem_install', 'brew_install', 'apt_get_install',
                              'cargo_install', 'npm_install', 'sudo', 'python', 'cd']
    assert settings.exclude_rules == []
    assert settings.aliases == {}
    assert settings.history_limit == None
    assert settings.wait_command == 3
    assert settings.debug == False
    assert settings.slow_commands == []
    assert settings.wait_slow_command == 15
   

# Generated at 2022-06-14 08:39:07.528844
# Unit test for method init of class Settings
def test_Settings_init():
    class Args():
        def __init__(self):
            self.yes = False
            self.debug = True
            self.repeat = 10

    assert settings.init(Args()) == \
        {'require_confirmation': False, 'debug': True, 'repeat': 10}

# Generated at 2022-06-14 08:39:16.877733
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception
    import sys
    from . import const

    d = {'user_dir': '~/.config/thefuck'}
    setattr(sys, 'excepthook', exception)
    s = Settings(d)
    s.init()
    assert(s.get('user_dir') == d['user_dir'])
    assert(s.get('priority') == const.DEFAULT_SETTINGS['priority'])

    s = Settings()
    s.init()
    assert(s.get('user_dir') == d['user_dir'])
    assert(s.get('priority') == const.DEFAULT_SETTINGS['priority'])


# Generated at 2022-06-14 08:39:21.537679
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init({})
    assert settings.user_dir == Path('~/.config/thefuck').expanduser()
    assert settings.require_confirmation == True
    assert settings.rules_dir == settings.user_dir.joinpath('rules')



# Generated at 2022-06-14 08:39:33.973229
# Unit test for method init of class Settings
def test_Settings_init():
    global settings
    # settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()

    assert settings['require_confirmation'] == True
    assert settings['use_notify'] == False
    assert settings['notify_in_terminal'] == False
    assert settings['wait_command'] == 3
    assert settings['wait_slow_command'] == 10
    assert settings['history_limit'] == None
    assert settings['alter_history'] == True
    assert settings['instant_mode'] == False
    assert settings['rules'] == const.DEFAULT_RULES
    assert settings['exclude_rules'] == []
    assert settings['priority'] == const.DEFAULT_PRIORITY
    assert settings['no_colors'] == False
    assert settings['debug_level'] == 'ERROR'

# Generated at 2022-06-14 08:39:41.626244
# Unit test for method init of class Settings
def test_Settings_init():
    _args = lambda **kwargs: type('Args', (object,), kwargs)
    args = _args(yes=True)
    settings.init(args)
    assert settings.require_confirmation == False
    args = _args(debug=True)
    settings.init(args)
    assert settings.debug == True
    args = _args(repeat=2)
    settings.init(args)
    assert settings.repeat == 2

# Generated at 2022-06-14 08:39:42.886268
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init(args=None)

# Generated at 2022-06-14 08:39:53.558422
# Unit test for method init of class Settings
def test_Settings_init():
    """
    Test for `settings.init()` method
    """
    from .logs import log_to_null
    from .shells import Bash, Python, Zsh

    with log_to_null():
        settings.init()
        assert settings.require_confirmation
        assert settings.history_limit == 500
        assert settings.wait_slow_command == 10
        assert settings.rules == Bash.Rules.DEFAULT_RULES + Zsh.Rules.DEFAULT_RULES + Python.Rules.DEFAULT_RULES
        assert settings.exclude_rules == []
        assert issubclass(settings._shell, Bash)
        assert settings.priority == {}
        assert settings.no_colors
        assert not settings.debug
        assert not settings.alter_history
        assert not settings.instant_mode

# Generated at 2022-06-14 08:39:54.855934
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()



# Generated at 2022-06-14 08:40:02.400096
# Unit test for method init of class Settings
def test_Settings_init():
    # init is not raising any exception in a normal usage
    settings.init()

    # init is not raising any exception with a wrong settings.py
    settings_file = settings.user_dir.joinpath('settings.py')
    with settings_file.open('a') as f:
        f.write('\nraise Exception()')
    settings.init()
    with settings_file.open('w') as f:
        f.write(const.SETTINGS_HEADER)



# Generated at 2022-06-14 08:40:41.400061
# Unit test for method init of class Settings
def test_Settings_init():
    """Test function test_Settings_init"""
    # given
    class Args():
        def __init__(self):
            self.yes = 1
            self.debug = 'debug'
            self.repeat = 'repeat'

    # when
    settings.init(Args())

    # then
    assert settings.require_confirmation == False
    assert settings.debug == 'debug'
    assert settings.repeat == 'repeat'


test_Settings_init()

# Generated at 2022-06-14 08:40:51.629688
# Unit test for method init of class Settings
def test_Settings_init():
    from tempfile import mkdtemp
    from shutil import rmtree
    import imp
    import os

    def check_settings_exists(user_dir):
        assert user_dir.joinpath('settings.py').is_file()
        assert user_dir.joinpath('rules').is_dir()

    def check_settings_file(user_dir):
        with user_dir.joinpath('settings.py').open() as f:
            assert const.SETTINGS_HEADER == f.readline()
            assert 2 == len(list(f))

    def check_settings_env(user_dir, new_settings):
        settings_env = settings_from_file(user_dir.joinpath('settings.py'))
        for attr in new_settings:
            assert getattr(settings_env, attr) == new

# Generated at 2022-06-14 08:41:04.950837
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import patch_logger
    from mock import Mock, patch, PropertyMock


# Generated at 2022-06-14 08:41:14.609164
# Unit test for method init of class Settings
def test_Settings_init():
    from collections import namedtuple
    from .logs import capture_logs

    settings.init()

    Args = namedtuple('Args', ['yes', 'debug', 'repeat'])
    with capture_logs() as logs:
        settings.init(Args(True, False, 0))

    assert settings.user_dir.is_dir()
    assert settings.user_dir.joinpath('settings.py').is_file()
    assert settings.user_dir.joinpath('rules').is_dir()
    assert 'Please move to' in logs.buffer
    assert settings['require_confirmation'] is False
    assert settings['repeat'] == 0


# Generated at 2022-06-14 08:41:20.159605
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings['rules_dir'] == Path('~', '.config', 'thefuck', 'rules').expanduser()
    assert settings['history_file'] == Path('~', '.config', 'thefuck', 'history').expanduser()

# Generated at 2022-06-14 08:41:29.455491
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import Log
    from .system import Path
    from .config import get_settings_path
    import os
    import shutil
    import tempfile
    import sys
    import unittest

    class SettingsInitTest(unittest.TestCase):
        def setUp(self):
            self.settings_path = Path(tempfile.mkdtemp(suffix='_thefuck_tests'))
            os.environ['XDG_CONFIG_HOME'] = text_type(self.settings_path)
            os.mkdir(self.settings_path.joinpath('rules'))
            os.mkdir(self.settings_path.joinpath('settings'))
            self._settings_path = Path(tempfile.mkdtemp(suffix='_thefuck_tests'))
