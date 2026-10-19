

# Generated at 2022-06-14 08:32:32.028065
# Unit test for method init of class Settings
def test_Settings_init():
    """Unit test for method init of class Settings"""
    from . import const
    from .logs import exception
    from .system import Path

    settings._init_settings_file()


    # _init_settings_file()
    file = const.CONFIG_PATH.joinpath('settings.py')
    assert file.is_file()


    # init(): _init_settings_file()
    file = const.CONFIG_PATH.joinpath('settings.py')
    with file.open() as settings_file:
        lines = settings_file.readlines()
    assert lines[0] == const.SETTINGS_HEADER
    for index, setting in enumerate(const.DEFAULT_SETTINGS.items()):
        assert lines[index+1] == '# {} = {}\n'.format(*setting)


    # _

# Generated at 2022-06-14 08:32:41.641808
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings()
    settings.init()
    assert 'require_confirmation' in settings
    assert 'no_colors' in settings
    assert 'debug' in settings
    assert 'history_limit' in settings
    assert 'rules' in settings
    assert 'exclude_rules' in settings
    assert 'wait_command' in settings
    assert 'slow_commands' in settings
    assert 'priority' in settings
    assert 'excluded_search_path_prefixes' in settings
    assert 'alter_history' in settings
    assert 'instant_mode' in settings

    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init('--no-colors')
    assert settings['no_colors'] is True

    settings = Settings(const.DEFAULT_SETTINGS)

# Generated at 2022-06-14 08:32:44.329880
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings.get('require_confirmation') == True
    assert settings.get('rules') == const.DEFAULT_RULES

# Generated at 2022-06-14 08:32:56.179393
# Unit test for method init of class Settings
def test_Settings_init():
    """Test cases for Settings.init method"""
    # Create temp dir
    import tempfile
    temp_dir = tempfile.TemporaryDirectory()
    user_dir = Path(temp_dir.name)

    # Save original user_dir
    original_user_dir = settings.user_dir

    # Replace user_dir
    settings.user_dir = user_dir
    # Replace file with init settings
    settings._init_settings_file()

    # Mock settings from file and env to use test values
    settings._settings_from_file = lambda: {'command_not_found': 'Foo'}
    settings._settings_from_env = lambda: {'command_not_found': 'Bar'}

    # Mock settings from args to use test values

# Generated at 2022-06-14 08:33:09.046083
# Unit test for method init of class Settings
def test_Settings_init():
    from .settings import Settings
    from .system import get_alias, get_path_to_history_file_for_testing
    from thefuck.logs import LoggingSettings
    from thefuck.rules import get_rules, get_exclude_rules

    arg_yes = type('args_yes', (object,), {'yes': True})
    arg_debug = type('args_debug', (object,), {'debug': True})
    arg_repeat = type('args_repeat', (object,), {'repeat': True})

    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()

    os.environ['TF_ALIAS'] = 'fuck'

    settings.init()
    assert settings.alias == get_alias()

    os.environ['TF_NO_COLOR'] = 'true'
    settings

# Generated at 2022-06-14 08:33:18.390256
# Unit test for method init of class Settings
def test_Settings_init():
    from .rules import get_all_rules
    from .logs import get_logger
    from thefuck.third_party.six.moves import reload_module

    _init_settings_file()

    reload_module(settings)
    reload_module(get_logger)
    reload_module(get_all_rules)

    _reset_env()

    settings.init()
    assert settings['require_confirmation'] is True
    assert settings['slow_commands'] == []
    assert settings['repeat'] == 1
    assert settings['debug'] is False
    assert settings['history_limit'] == None
    assert settings['exclude_rules'] == []
    assert settings['priority'] == {}
    assert settings['rules'] == const.DEFAULT_RULES


# Generated at 2022-06-14 08:33:25.782989
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings(const.DEFAULT_SETTINGS)
    user_dir = settings._get_user_dir_path()
    settings._setup_user_dir()
    assert settings.user_dir == user_dir
    settings._setup_user_dir()
    assert settings.user_dir == user_dir
    params = {'yes': True, 'debug': False, 'repeat': 3}
    settings.update(settings._settings_from_args(params))
    assert settings['require_confirmation'] == False
    assert settings['debug'] == False
    assert settings['repeat'] == 3

# Generated at 2022-06-14 08:33:32.608313
# Unit test for method init of class Settings
def test_Settings_init():
    """Unit-tests for method init of class Settings."""
    from .logs import exception

    def reset_logging():
        exception.exceptions = 0

    # TODO: maybe, use mock module

    # Check the case when rules_dir was created
    settings.init()
    assert settings.user_dir.joinpath('rules').is_dir()
    settings.user_dir.joinpath('rules').rmdir()

    # Check the case when settings.py wasn't created and was created
    reset_logging()
    settings.user_dir.joinpath('settings.py').unlink()
    assert not settings.user_dir.joinpath('settings.py').is_file()
    settings.init()
    assert settings.user_dir.joinpath('settings.py').is_file()
    assert exception.exceptions == 1


# Generated at 2022-06-14 08:33:35.251883
# Unit test for method init of class Settings
def test_Settings_init():
    global settings
    args = ['fuck']
    settings.init(args)
    assert settings['history_limit'] == 10

settings.init()

# Generated at 2022-06-14 08:33:45.026949
# Unit test for method init of class Settings
def test_Settings_init():
    args = type('args', (object,), {'debug': True, 'yes': True, 'repeat': 5})()
    old_user_dir = settings.user_dir
    old_settings = settings.copy()

    settings.update(const.ENV_TO_ATTR)
    settings['init'](args)

    assert settings != old_settings
    assert settings != const.ENV_TO_ATTR
    assert settings['debug']

    assert settings['user_dir'] != old_user_dir
    assert settings['user_dir'] == old_user_dir.expanduser()

# Generated at 2022-06-14 08:34:41.418864
# Unit test for method init of class Settings
def test_Settings_init():
    test_args = type('_', (object,), {'yes': True, 'debug': True, 'repeat': 5})()
    test_settings = Settings(const.DEFAULT_SETTINGS)
    test_settings.init(args=test_args)
    assert test_settings == {"require_confirmation": False, "debug": True, "repeat": 5}



# Generated at 2022-06-14 08:34:51.240967
# Unit test for method init of class Settings
def test_Settings_init():
    # setup
    from .logs import exception
    exception.__name__ = 'exception'
    args = Mock()
    args.yes = None
    args.debug = None
    args.repeat = None
    _settings_from_file = Mock(return_value={})
    _settings_from_env = Mock(return_value={})
    _settings_from_args = Mock(return_value={})
    _init_settings_file = Mock()
    _setup_user_dir = Mock()
    settings.user_dir = Mock()
    settings._settings_from_file = _settings_from_file
    settings._settings_from_env = _settings_from_env
    settings._settings_from_args = _settings_from_args
    settings._init_settings_file = _init_settings_file
    settings._setup

# Generated at 2022-06-14 08:35:05.075242
# Unit test for method init of class Settings
def test_Settings_init():
    import tempfile
    import os
    from shutil import rmtree

    from .logs import disable_stderr
    from .system import remove_line

    temp_dir = tempfile.mkdtemp()
    os.environ['XDG_CONFIG_HOME'] = temp_dir
    settings.init()
    settings_path = os.path.join(temp_dir, 'thefuck', 'settings.py')
    with open(settings_path, 'a') as settings_file:
        settings_file.write('rules = ["test1", "test2"]')
    os.environ['THEFUCK_NO_COLORS'] = 'true'
    os.environ['THEFUCK_DEBUG'] = 'true'
    settings.init()
    assert settings.no_colors
    assert settings.debug

# Generated at 2022-06-14 08:35:12.036132
# Unit test for method init of class Settings
def test_Settings_init():
    settings.clear()
    assert settings.keys() == []
    settings.init()
    assert settings.keys() == const.DEFAULT_SETTINGS.keys()
    assert settings.get('require_confirmation') == True
    assert settings.get('no_colors') == False
    assert settings.get('debug') == False
    assert settings.get('wait_command') == 15
    assert settings.get('slow_commands') == []

# Generated at 2022-06-14 08:35:25.003035
# Unit test for method init of class Settings
def test_Settings_init():
    # test _get_user_dir_path
    # XDG_CONFIG_HOME=''
    # Legacy user config directory exists
    os.environ['XDG_CONFIG_HOME'] = ''
    assert Settings(const.DEFAULT_SETTINGS)._get_user_dir_path().__str__() == os.path.expanduser(
        '~/.thefuck')

    # XDG_CONFIG_HOME=not empty
    # Legacy user config directory doesn't exist
    os.environ['XDG_CONFIG_HOME'] = '~/.haha'
    assert Settings(const.DEFAULT_SETTINGS)._get_user_dir_path().__str__() == os.path.expanduser(
        '~/.haha/thefuck')

    # test _init_settings_file
    settings

# Generated at 2022-06-14 08:35:38.095428
# Unit test for method init of class Settings
def test_Settings_init():
    # Assume
    user_dir = Path('~', '.thefuck').expanduser()
    settings_path = user_dir.joinpath('settings.py')
    os.environ['TF_ALTER_HISTORY'] = 'True'
    os.environ['TF_COLORS'] = os.environ['TF_NO_COLORS'] = 'False'
    os.environ['TF_DEBUG'] = 'True'
    os.environ['TF_HISTORY_LIMIT'] = '42'
    os.environ['TF_WAIT_COMMAND'] = '13'
    os.environ['TF_RULES'] = 'DEFAULT_RULES:some_rule'
    os.environ['TF_EXCLUDE_RULES'] = 'some_rule:some_other_rule'


# Generated at 2022-06-14 08:35:42.522160
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings['rules'][0] == 'git_push_current_branch'
    assert settings['require_confirmation'] == True
    
if __name__ == '__main__':
    test_Settings_init()

# Generated at 2022-06-14 08:35:57.143323
# Unit test for method init of class Settings
def test_Settings_init():
    # testing for not existing file
    global settings
    settings = Settings(const.DEFAULT_SETTINGS)
    settings._get_user_dir_path = lambda: '~/empty_path'
    settings._setup_user_dir = lambda: None
    settings.init()
    assert settings['require_confirmation'] == True
    assert settings['wait_command'] == 3
    assert settings['rules'] == const.DEFAULT_RULES

    # testing for file with all standard values
    settings = Settings(const.DEFAULT_SETTINGS)
    settings._get_user_dir_path = lambda: '~/.thefuck/'
    settings._setup_user_dir = lambda: None
    path = Path('~/.thefuck/settings.py')

# Generated at 2022-06-14 08:36:05.549184
# Unit test for method init of class Settings
def test_Settings_init():
    """Test Settings.init method"""
    from six.moves import reload_module
    reload_module(sys.modules['thefuck.settings'])
    settings.init()
    assert not settings.user_dir.joinpath('rules').exists()
    assert settings.user_dir.joinpath('settings.py').is_file()
    assert settings.slow_commands == ['lein', 'rebar', './gradlew']
    assert settings.exclude_rules == []
    assert settings.rules == ['git_push', 'git_add', 'python_command',
                              'sudo', 'cd', 'man', 'brew_install_formula',
                              'pip_requirements', 'apt_get_install', 'cabal_install',
                              'stack_install']
    assert settings.env == {}

# Generated at 2022-06-14 08:36:07.232379
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()

test_Settings_init()

# Generated at 2022-06-14 08:37:58.070552
# Unit test for method init of class Settings
def test_Settings_init():
    import sys
    from .system import get_aliases_with_command, get_aliases_with_command_from_shell, get_all_executables
    from .logs import log_to_file, log_to_output, exception


    def _init():
        settings.init()
        return settings

    def _restore_defaults():
        for key, value in const.DEFAULT_SETTINGS.items():
            setattr(settings, key, value)

    # Unit test for method init of class Settings
    def test_Settings_init():
        import sys
        from .system import get_aliases_with_command, get_aliases_with_command_from_shell
        from .logs import log_to_file, log_to_output, exception


        def _init():
            settings.init()


# Generated at 2022-06-14 08:38:01.062232
# Unit test for method init of class Settings
def test_Settings_init():
    sys.modules[__name__] = Settings()
    import thefuck.conf

    thefuck.conf.settings = Settings()
    thefuck.conf.settings.init({})
    assert thefuck.conf.settings.user_dir == thefuck.conf._get_user_dir_path()


# Generated at 2022-06-14 08:38:07.967269
# Unit test for method init of class Settings
def test_Settings_init():
    class TestClass(object):
        def __init__(self):
            self.user_dir = None
            self.require_confirmation = self.no_colors = self.debug = None

    settings = TestClass()

    def _settings_from_file():
        return {'require_confirmation': False}

    def _settings_from_env():
        return {'no_colors': True}

    def _settings_from_args(args):
        return {'debug': True}

    settings.init = Settings.init.__get__(settings)
    settings.init()

    settings._settings_from_file = _settings_from_file
    settings._settings_from_env = _settings_from_env
    settings._settings_from_args = _settings_from_args

# Generated at 2022-06-14 08:38:18.491181
# Unit test for method init of class Settings
def test_Settings_init():
    from .tests.utils import replace_attr
    from .logs import init_log
    import logging

    def mock_get_user_dir_path():
        return 'user_dir'

    def mock_init_settings_file(self):
        self._settings_file = 'settings_file'

    def mock_settings_from_file(self):
        return {'key1': 'val1'}

    def mock_settings_from_env(self):
        return {'key2': 'val2'}

    def mock_settings_from_args(self, args):
        return {'key3': 'val3'}


# Generated at 2022-06-14 08:38:30.456923
# Unit test for method init of class Settings
def test_Settings_init():
    """
    Settings.init() should fill the settings with the default settings, with
    the settings loaded from the settings.py file, with the settings loaded
    from env and with the settings loaded from arguments.
    """
    from .logs import exception
    from .system import TemporaryDirectory

    _settings_from_file = Settings._settings_from_file
    _settings_from_env = Settings._settings_from_env
    _settings_from_args = Settings._settings_from_args

    def assert_called_once(mock):  # TODO: use mock.assert_called_once_with()
        if mock.call_count != 1:
            raise AssertionError(
                'Expected call_count is 1, but actual call_count is {}'.
                format(mock.call_count))


# Generated at 2022-06-14 08:38:40.799222
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert 'require_confirmation'  in settings
    assert 'no_colors'  in settings
    assert 'alter_history'  in settings
    assert 'wait_command'  in settings
    assert 'wait_slow_command'  in settings
    assert 'history_limit'  in settings
    assert 'rules'  in settings
    assert 'exclude_rules'  in settings
    assert 'priority'  in settings
    assert 'debug'  in settings
    assert 'slow_commands'  in settings
    assert 'excluded_search_path_prefixes'  in settings

# Generated at 2022-06-14 08:38:50.531919
# Unit test for method init of class Settings
def test_Settings_init():
    from tempfile import mkdtemp
    from shutil import rmtree
    from os import environ, path
    from contextlib import contextmanager

    @contextmanager
    def tempdir():
        tmpdir = mkdtemp()
        try:
            yield tmpdir
        finally:
            rmtree(tmpdir)

    @contextmanager
    def env(values):
        old_values = {}
        for key, value in values.items():
            old_values[key] = os.environ.get(key)
            environ[key] = value
        try:
            yield
        finally:
            for key, value in old_values.items():
                if value is None:
                    del environ[key]
                else:
                    environ[key] = value


# Generated at 2022-06-14 08:38:53.676409
# Unit test for method init of class Settings
def test_Settings_init():
    args = Settings.Settings(const.DEFAULT_SETTINGS)._settings_from_args(True)
    assert args['require_confirmation'] == False
    args = Settings.Settings(const.DEFAULT_SETTINGS)._settings_from_args(False)
    assert args == {}

# Generated at 2022-06-14 08:38:55.960558
# Unit test for method init of class Settings
def test_Settings_init():
    settings2 = Settings()
    settings2.init()

    assert settings2.user_dir.joinpath('settings.py').is_file()
    assert settings2.user_dir.joinpath('rules').is_dir()

# Generated at 2022-06-14 08:38:58.914258
# Unit test for method init of class Settings
def test_Settings_init():
    """Unit test for method init of class Settings."""
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()
    assert(settings.get('require_confirmation') == const.DEFAULT_SETTINGS.get('require_confirmation'))



# Generated at 2022-06-14 08:40:47.744700
# Unit test for method init of class Settings
def test_Settings_init():
    class TestClass(object):
        def __init__(self):
            self.user_dir = Path('~/.thefuck_test').expanduser()
            self.user_dir.mkdir()

            settings_path = self.user_dir.joinpath('settings.py')
            with settings_path.open(mode='w') as settings_file:
                settings_file.write(const.SETTINGS_HEADER)
                for setting in const.DEFAULT_SETTINGS.items():
                    settings_file.write(u'# {} = {}\n'.format(*setting))

            self.settings = Settings(const.DEFAULT_SETTINGS)

        def teardown(self):
            self.user_dir.rmdir()

        def test_normal_Settings_init(self):
            self.settings.init()



# Generated at 2022-06-14 08:40:50.891054
# Unit test for method init of class Settings
def test_Settings_init():
    # test init of class Settings,
    # assert all attributes in settings are not None
    settings.init()
    for key, val in settings.items():
        assert val is not None

# Generated at 2022-06-14 08:40:59.001419
# Unit test for method init of class Settings
def test_Settings_init():
    args = None
    settings._setup_user_dir()
    settings._init_settings_file()
    settings.update(settings._settings_from_file())
    settings.update(settings._settings_from_env())
    settings.update(settings._settings_from_args(args))
    assert settings.pop('pop') == 5
    assert settings.pop('pop') == 2
    assert settings.pop('pop') == 1

# Generated at 2022-06-14 08:41:04.180841
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings.require_confirmation == True
    assert settings.require_confirmation == const.DEFAULT_SETTINGS['require_confirmation']
    assert settings.repeat == 1
    assert settings.repeat == const.DEFAULT_SETTINGS['repeat']

# Unit tests for method _settings_from_env of class Settings

# Generated at 2022-06-14 08:41:16.230151
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception
    from .system import Path
    from . import const
    from .utils import get_all_scripts_from_path

    # settings._init_settings_file()  # in test settings.py file, set
    settings._setup_user_dir()

    settings.user_dir = Path(settings.user_dir)  # settings.user_dir
    # settings.user_dir = settings.user_dir.expanduser()  # settings.user_dir
    settings_path = settings.user_dir.joinpath('settings.py')

    settings.update(settings._settings_from_file())
    settings.update(settings._settings_from_env())

    args = ''
    settings.update(settings._settings_from_args(args))

    from .logs import debug, exception

# Generated at 2022-06-14 08:41:27.619628
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception
    from .system import path
