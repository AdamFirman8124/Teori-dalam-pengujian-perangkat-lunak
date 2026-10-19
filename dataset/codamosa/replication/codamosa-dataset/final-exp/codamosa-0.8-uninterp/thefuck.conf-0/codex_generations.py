

# Generated at 2022-06-14 08:31:54.617845
# Unit test for method init of class Settings
def test_Settings_init():
    settings.clear()
    with settings.user_dir.joinpath('settings.py').open(mode='w') as file:
        file.write(u'print(\'This is mock for settings.py\')')
    settings.init()
    assert settings.get('history_limit') == const.DEFAULT_SETTINGS['history_limit']
    assert settings['history_limit'] == 10
    settings.user_dir.joinpath('settings.py').unlink()

# Generated at 2022-06-14 08:32:06.046941
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init(args=None)
    assert settings['require_confirmation'] == True
    assert settings['history_limit'] == None
    assert settings['wait_command'] == 3
    assert settings['wait_slow_command'] == 9
    assert settings['alter_history'] == True
    assert settings['no_colors'] == False
    assert settings['debug'] == False
    assert settings['rules'] == ['~/.thefuck/rules/*.py']
    assert settings['exclude_rules'] == []
    assert settings['require_confirmation'] == True
    assert settings['alter_history'] == True
    assert settings['instant_mode'] == False
    assert settings['repeat'] == False
    assert settings['excluded_search_path_prefixes'] == ['/usr', '/Library']

# Generated at 2022-06-14 08:32:07.669240
# Unit test for method init of class Settings
def test_Settings_init():
    assert settings.init() == None

# Generated at 2022-06-14 08:32:20.747310
# Unit test for method init of class Settings
def test_Settings_init():
    """
    `init` must fill `settings` with values from `settings.py` and env.
    """
    from .system import PATH
    from .rules import add_rule
    from .tools import get_all_executables
    from .utils import wrap_settings

    path = PATH.copy()

# Generated at 2022-06-14 08:32:21.709473
# Unit test for method init of class Settings
def test_Settings_init():
    assert settings
    assert settings['require_confirmation']

# Generated at 2022-06-14 08:32:31.784578
# Unit test for method init of class Settings
def test_Settings_init():
    import pytest
    import tempfile
    # Init the settings with a custom user dir
    settings.init(args=None)
    testargs = ['thefuck']
    with tempfile.TemporaryDirectory() as tempdir:
        testargs = pytest.helpers.ArgvSetter(
            testargs,
            {'--user-dir': tempdir, '--no-require-confirmation': True})
        settings.init(args=testargs.get_parsed_argv())
        assert settings.user_dir == Path(tempdir)
        assert settings.require_confirmation is False

# Generated at 2022-06-14 08:32:34.824923
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    for i in const.DEFAULT_SETTINGS.keys():
        assert hasattr(settings, i)


# Generated at 2022-06-14 08:32:39.189793
# Unit test for method init of class Settings
def test_Settings_init():
    """Test that settings are properly loaded."""
    settings = Settings(const.DEFAULT_SETTINGS)
    import six
    with six.moves.mock.patch.dict(os.environ, {'TF_NO_COLORS': 'True'}):
        settings.init()
    assert settings.no_colors

# Generated at 2022-06-14 08:32:52.109113
# Unit test for method init of class Settings
def test_Settings_init():
    import os
    import tempfile

    custom_xdg_config_home = tempfile.mkdtemp()
    from .logs import exception
    os.environ['XDG_CONFIG_HOME'] = custom_xdg_config_home

    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()
    if hasattr(settings, 'XDG_CONFIG_HOME'):
        del os.environ['XDG_CONFIG_HOME']
    else:
        del os.environ['XDG_CONFIG_HOME']
        os.rmdir(custom_xdg_config_home)
        assert False

    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()
    custom_xdg_config_home = settings.user_dir.parent
   

# Generated at 2022-06-14 08:32:59.555304
# Unit test for method init of class Settings
def test_Settings_init():
    args = Namespace(yes=True, debug=True, repeat=True)
    settings.init(args)
    settings.user_dir = '~/.thefuck'

# Generated at 2022-06-14 08:33:22.746360
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings.user_dir.is_dir()
    assert settings.user_dir.joinpath('settings.py').is_file()
    assert settings._settings_from_file()

# Generated at 2022-06-14 08:33:25.740522
# Unit test for method init of class Settings
def test_Settings_init():
    settings.update(
        {'require_confirmation': True, 'rules': [], 'repeat': None}
    )
    settings.init()
    assert settings.require_confirmation is True
    assert settings.repeat is None



# Generated at 2022-06-14 08:33:32.577072
# Unit test for method init of class Settings
def test_Settings_init():
    def _assert_update(updates, settings=settings):
        for key, value in updates.iteritems():
            assert settings[key] == value

    def _assert_no_update(keys, settings=settings):
        for key in keys:
            assert key not in settings

    settings._setup_user_dir = lambda: setattr(settings, 'user_dir',
                                               Path('/user/dir'))
    settings._settings_from_file = lambda: {'attr1': 'value1'}
    settings._settings_from_env = lambda: {'attr2': 'value2'}
    settings._settings_from_args = lambda args: {'attr3': 'value3'}
    settings.init(args=['--repeat'])

# Generated at 2022-06-14 08:33:39.093628
# Unit test for method init of class Settings
def test_Settings_init():
    settings._get_user_dir_path = lambda: Path('~/.thefuck').expanduser()
    settings.init()
    assert settings.user_dir.exists()
    assert settings.user_dir.joinpath('settings.py').exists()
    assert 'rules' in const.DEFAULT_SETTINGS
    assert settings.rules == const.DEFAULT_RULES



# Generated at 2022-06-14 08:33:46.078147
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings.user_dir == Path('~/.config/thefuck').expanduser()
    assert settings.rules == ['git_push', 'git_commit', 'git_add']
    assert settings.exclude_rules == []
    assert settings.no_colors is False
    assert settings.debug is False
    assert settings.alter_history is False
    assert settings.wait_command == 1
    assert settings.priority == {}
    assert settings.require_confirmation is True
    assert settings.slow_commands == ['lein', 'react-native', 'gradle', './gradlew']
    assert settings.excluded_search_path_prefixes == ['/usr', '/Library/Python']
    assert settings.pattern == '(?<=: )[^ ]+ not (?:found|recognized)$'
   

# Generated at 2022-06-14 08:33:59.348178
# Unit test for method init of class Settings
def test_Settings_init():
    """To test init() method of the class Settings"""
    from .logs import LOG_FILE_TEST_PATH, LOG_FILE_USER_PATH
    settings.init()
    assert settings.user_dir.endswith('.config/thefuck')
    assert settings.require_confirmation == False
    assert settings.priority == {'sudo': 100, 'brew': 99, 'apt-get': 99, 'emerge': 99, 'pip': 99, 'guix': 99, 'crontab': 99, 'cargo': 99, 'npm': 99}

# Generated at 2022-06-14 08:34:02.010020
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert os.path.exists(settings.user_dir)
    assert os.path.exists(os.path.join(settings.user_dir, 'settings.py'))


# Generated at 2022-06-14 08:34:15.496758
# Unit test for method init of class Settings
def test_Settings_init():
    import argparse
    from StringIO import StringIO
    from contextlib import contextmanager

    @contextmanager
    def _mocked_open(content):
        fake_file = StringIO(content)
        try:
            yield fake_file
        finally:
            fake_file.close()

    @contextmanager
    def _mocked_environ(env):
        orig_env = os.environ
        try:
            os.environ = env
            yield
        finally:
            os.environ = orig_env


# Generated at 2022-06-14 08:34:22.566295
# Unit test for method init of class Settings
def test_Settings_init():
    from unittest.mock import patch, mock_open

    def _open(name):
        if name.endswith('settings.py'):
            return mock_open(read_data=(const.SETTINGS_HEADER + u"""
                require_confirmation = False
                rules = [
                    'ssh',
                    'git'
                ]
                debug = True""")).return_value
        elif name.endswith('rules/custom.py'):
            return mock_open(read_data=u"""
                from thefuck.types import Command
                from thefuck.rules.shell import match

                def get_new_command(command: Command) -> str:
                    return 'yes'""").return_value
        else:
            return mock_open().return_value


# Generated at 2022-06-14 08:34:23.883728
# Unit test for method init of class Settings
def test_Settings_init():
    settings.clear()
    settings.init()

# Generated at 2022-06-14 08:35:17.160256
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()

    # test if keys in settings are all in DEFAULT_SETTINGS
    for key in settings.keys():
        assert(key in const.DEFAULT_SETTINGS)

    # test writing the default settings to the user settings file
    user_settings_path = settings.user_dir.joinpath('settings.py')
    user_settings = load_source('settings', text_type(user_settings_path))
    for attr, val in const.DEFAULT_SETTINGS.items():
        assert(getattr(user_settings, attr) == val)

    # test if settings are successfully loaded from env
    env_settings = settings._settings_from_env()
    for attr, val in env_settings.items():
        assert(attr in const.ENV_TO_ATTR.values())

    # test

# Generated at 2022-06-14 08:35:27.264331
# Unit test for method init of class Settings
def test_Settings_init():
    import sys
    from os import environ as env
    from contextlib import contextmanager

    from thefuck.utils import get_closest
    from thefuck.shells import shell

    old_shell = shell

    @contextmanager
    def set_shell(new_shell):
        """Set thefuck.shells.shell.current_shell to `new_shell`."""
        shell.current_shell = new_shell
        yield
        shell.current_shell = old_shell

    def test_setup_user_dir():
        del(env['THEFUCK_RULES'])
        del(env['THEFUCK_PRIORITY'])
        del(env['THEFUCK_WAIT_COMMAND'])
        del(env['THEFUCK_HISTORY_LIMIT'])

# Generated at 2022-06-14 08:35:40.368410
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception
    from mock import patch

    args = Mock(spec=['debug', 'yes', 'repeat'], debug=True, yes=True, repeat=3)

# Generated at 2022-06-14 08:35:50.199284
# Unit test for method init of class Settings
def test_Settings_init():
    """Test Settings.init method"""
    class Args():
        def __init__(self, yes=False, debug=False, repeat=None):
            self.yes = yes
            self.debug = debug
            self.repeat = repeat

    def get_settings(yes=False, debug=False, repeat=None):
        """Returns Settings object for testing"""
        args = Args(yes, debug, repeat)
        settings = Settings(const.DEFAULT_SETTINGS)
        settings.init(args)
        return settings

    def test_defaults():
        """Tests that Settings.init returns correct defaults"""
        settings = get_settings()
        for setting, value in const.DEFAULT_SETTINGS.items():
            assert settings[setting] == value


# Generated at 2022-06-14 08:36:01.506181
# Unit test for method init of class Settings
def test_Settings_init():
    print("start test_Settings_init")
    settings_path = settings.user_dir.joinpath('settings.py')

# Generated at 2022-06-14 08:36:14.123471
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings(const.DEFAULT_SETTINGS)
    settings._init_settings_file()

    import inspect
    import sys

    def exec_func(func):
        spec = inspect.getargspec(func)
        if spec.defaults is not None:
            func_args = spec.args[-len(spec.defaults):]
            return dict(zip(func_args, spec.defaults))
        else:
            return {}

    path = settings.user_dir.joinpath('settings.py')
    with path.open() as f:
        code = f.read()
    assert code.startswith('# encoding: utf-8')
    assert code.endswith('# {} = {}\n'.format('num_close_matches', 3))

# Generated at 2022-06-14 08:36:16.647686
# Unit test for method init of class Settings
def test_Settings_init():
    new_settings = Settings(const.DEFAULT_SETTINGS) 
    new_settings.init()
    assert new_settings == settings


# Generated at 2022-06-14 08:36:30.860379
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception
    from .tests.utils import patch_exception_logger
    from thefuck.shells import shell

    with patch_exception_logger() as mock_exception:
        settings.init()

    assert mock_exception.call_count == 0
    assert settings['debug'] == const.DEFAULT_SETTINGS['debug']
    assert settings['repeat'] == const.DEFAULT_SETTINGS['repeat']
    assert settings['require_confirmation'] == const.DEFAULT_SETTINGS['require_confirmation']

    with patch_exception_logger() as mock_exception:
        with patch_exception_logger() as mock_exception_log:
            settings.init()

    assert mock_exception.call_count == 0
    assert mock_exception_log.call_count

# Generated at 2022-06-14 08:36:39.135632
# Unit test for method init of class Settings
def test_Settings_init():
    import os
    import tempfile
    import shutil
    import subprocess
    import logging
    import pytest
    from .logs import log


# Generated at 2022-06-14 08:36:44.416556
# Unit test for method init of class Settings
def test_Settings_init():
    args = type('', (), {})()
    args.yes = True
    args.debug = 3
    args.repeat = 5
    settings.init(args)
    assert settings.require_confirmation is False
    assert settings.debug is True
    assert settings.repeat == 5

# Generated at 2022-06-14 08:37:34.457844
# Unit test for method init of class Settings
def test_Settings_init():
    import platform
    d = {'user_dir': '~/.config/thefuck'}
    if platform.system() != 'Windows':
        d['script_dir'] = '~/bin'
    settings.init()
    assert settings == d

# Generated at 2022-06-14 08:37:42.023693
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception
    args = {
        "yes": True,
        "debug": False,
        "repeat": 0
    }
    try:
        _settings = Settings(const.DEFAULT_SETTINGS)
        _settings.init(args)
    except Exception as e:
        exception("Settings.init fail", sys.exc_info())

    assert _settings.require_confirmation == False
    assert _settings.debug == False
    assert _settings.repeat == 0

# Generated at 2022-06-14 08:37:54.043994
# Unit test for method init of class Settings
def test_Settings_init():
    # Init
    settings = Settings({'rules': [], 'exclude_rules': []})
    settings.user_dir = Path.cwd()

    # Data
    default_settings = {'rules': [], 'exclude_rules': []}
    file_settings = {'rules': ['one'], 'exclude_rules': ['two']}
    env_settings = {'rules': ['three'], 'exclude_rules': ['four']}
    args_settings = {'rules': ['five'], 'exclude_rules': ['six']}

    # Mocks
    settings._init_settings_file = lambda: None
    settings._settings_from_file = lambda: file_settings
    settings._settings_from_env = lambda: env_settings
    settings._settings_from_args = lambda args: args_settings

    # Test

# Generated at 2022-06-14 08:38:02.293203
# Unit test for method init of class Settings
def test_Settings_init():
    # if there is not `settings.py` in `user_dir`,
    # settings.init should create a template one.
    import tempfile
    import shutil
    import os

    path = tempfile.mkdtemp()

# Generated at 2022-06-14 08:38:07.481559
# Unit test for method init of class Settings
def test_Settings_init():

    from .logs import Logger
    from .utils import memoize
    from .rules import get_available_rules

    # Check if we're executing or not
    if not os.environ.get('_THEFUCK_TEST_SETTINGS', False):
        from . import application
        logging = Logger(True, 'ERROR')
        application.main(rules=get_available_rules(logging=logging),
                         logging=logging)
    else:

        # Define a class to override the user config resource
        class SettingsPath(Path):
            def joinpath(self, *path):
                return Path(
                    '/tmp/thefuck_settings_init/settings.py').expanduser()

            def is_dir(self):
                return True

            def mkdir(self, **kw):
                pass


# Generated at 2022-06-14 08:38:15.108741
# Unit test for method init of class Settings
def test_Settings_init():
    import config as module
    import os

    test_settings = module.Settings()
    test_settings.init(None)
    assert test_settings._get_user_dir_path().joinpath('settings.py').is_file()
    if os.environ.get('XDG_CONFIG_HOME', '~/.config') != '~/.config':
        assert test_settings._get_user_dir_path().joinpath('settings.py').is_file() is False

# Generated at 2022-06-14 08:38:17.889931
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert type(settings) is Settings
    assert settings.user_dir is not None


# Generated at 2022-06-14 08:38:29.995416
# Unit test for method init of class Settings
def test_Settings_init():
    class FakeArgs(object):
        def __init__(self, yes, debug, repeat):
            self.yes = yes
            self.debug = debug
            self.repeat = repeat

    # testing _setup_user_dir
    assert settings.user_dir == Path(u'~/.config', 'thefuck').expanduser()

    # testing _settings_from_args
    settings.init(FakeArgs(yes=True, debug=True, repeat=3))
    assert settings.require_confirmation is False
    assert settings.debug is True
    assert settings.repeat == 3

    # testing _settings_from_env
    os.environ['THEFUCK_WAIT_COMMAND'] = '2'
    settings.init()
    assert settings.wait_command == 2

    # testing settings.py

# Generated at 2022-06-14 08:38:32.116094
# Unit test for method init of class Settings
def test_Settings_init():
    global settings
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()

# Generated at 2022-06-14 08:38:33.629057
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()


# Generated at 2022-06-14 08:40:20.062658
# Unit test for method init of class Settings
def test_Settings_init():
    import mock
    from contextlib import contextmanager

    @contextmanager
    def mock_settings_file(content):
        with mock.patch('__builtin__.open') as open_:
            with mock.patch('os.path.isfile') as isfile:
                open_().__enter__.return_value.__iter__.return_value = content
                isfile.return_value = True
                yield

    settings.init()

    with mock_settings_file('require_confirmation=True'):
        settings.init()
        assert settings['require_confirmation'] is True

    with mock_settings_file('require_confirmation=False'):
        settings.init()
        assert settings['require_confirmation'] is False

    with mock_settings_file(''):
        settings.init()

# Generated at 2022-06-14 08:40:26.504667
# Unit test for method init of class Settings
def test_Settings_init():
        from .logs import capture_log

        with capture_log() as logs:
            with Path('dir_test').mkdir() as user_dir:
                Path(user_dir, 'settings.py').touch()
                settings.init()
                assert not logs.values()


# Generated at 2022-06-14 08:40:32.360480
# Unit test for method init of class Settings
def test_Settings_init():
    test_settings = Settings(const.DEFAULT_SETTINGS)
    test_settings.init({'yes': True, 'repeat': True, 'debug': True})
    assert test_settings == {'require_confirmation': False, 'debug': True, 'repeat': True}


# Generated at 2022-06-14 08:40:41.726994
# Unit test for method init of class Settings
def test_Settings_init():
    import unittest

    from . import system
    from .system import DEFAULT_HISTORY, DEFAULT_HISTORY_FILE

    class SettingsInitCase(unittest.TestCase):
        def runTest(self):
            self._test_file_init()
            self._test_env_init()
            self._test_args_init()

        def _test_file_init(self):
            import tempfile
            from .system import DEFAULT_HISTORY_FILE
            with tempfile.NamedTemporaryFile('w',
                                             suffix='settings.py') as f:
                f.write(const.SETTINGS_HEADER)
                f.write('require_confirmation = False\n')
                f.flush()
                settings.init()
                self.assertFalse(settings.require_confirmation)

# Generated at 2022-06-14 08:40:42.478908
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init(args=None)


# Generated at 2022-06-14 08:40:44.305874
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import log

    settings.init()
    assert settings['log_file'] == log.baseFilename


# Generated at 2022-06-14 08:40:56.421321
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()

    assert(settings.user_dir is not None)

    assert(settings.key_to_interrupt == const.DEFAULT_SETTINGS['key_to_interrupt'])
    assert(settings.history_limit == const.DEFAULT_SETTINGS['history_limit'])
    assert(settings.wait_command == const.DEFAULT_SETTINGS['wait_command'])
    assert(settings.wait_slow_command == const.DEFAULT_SETTINGS['wait_slow_command'])
    assert(settings.require_confirmation == const.DEFAULT_SETTINGS['require_confirmation'])
    assert(settings.repeat == const.DEFAULT_SETTINGS['repeat'])
    assert(settings.no_colors == const.DEFAULT_SETTINGS['no_colors'])

# Generated at 2022-06-14 08:40:59.542467
# Unit test for method init of class Settings
def test_Settings_init():
    c = Settings()
    c.init()
    assert c._get_user_dir_path().find('thefuck') > 0


# Generated at 2022-06-14 08:41:04.013563
# Unit test for method init of class Settings
def test_Settings_init():
    # prepare
    args = type('', (object,), {})
    args.yes = True
    args.debug = False
    args.repeat = None

    # run
    settings.init(args)

    # assert
    assert not settings.require_confirmation

# Generated at 2022-06-14 08:41:11.698615
# Unit test for method init of class Settings
def test_Settings_init():
    old_user_dir = settings.user_dir
    old_settings_file = settings.user_dir.joinpath('settings.py')

    settings.init()
    assert settings.user_dir == old_user_dir
    assert old_settings_file.is_file()

    settings.user_dir.rmdir()
    settings.init()
    assert settings.user_dir != old_user_dir
    assert not old_settings_file.is_file()
    assert settings.user_dir.joinpath('settings.py').is_file()