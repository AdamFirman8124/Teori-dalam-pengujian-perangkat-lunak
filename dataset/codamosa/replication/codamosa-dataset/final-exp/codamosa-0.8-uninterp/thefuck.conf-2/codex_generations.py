

# Generated at 2022-06-14 08:31:42.739881
# Unit test for method init of class Settings
def test_Settings_init():
    from .utils import generate_command

    args = type('Args', (object,), dict(yes=True))
    settings.init(args)
    assert not settings.require_confirmation

    os.environ['TF_REQUIRE_CONFIRMATION'] = 'True'
    settings.init()
    assert settings.require_confirmation

    os.environ['TF_RULES'] = 'ps:ls'
    settings.init()
    assert settings.rules == ['ps', 'ls']

    os.environ['TF_SLOW_COMMANDS'] = 'ls:sleep 1'
    settings.init()
    assert settings.slow_commands == ['ls', 'sleep 1']

    os.environ['TF_WAIT_COMMAND'] = '10'
    settings.init()

# Generated at 2022-06-14 08:31:48.150898
# Unit test for method init of class Settings
def test_Settings_init():
    global settings
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()
    assert settings
    assert settings['debug']
    assert settings['require_confirmation']
    assert settings['repeat']
    assert settings['wait_command']
    assert settings['wait_slow_command']


# Generated at 2022-06-14 08:31:57.364607
# Unit test for method init of class Settings
def test_Settings_init():
    test_settings = Settings(const.DEFAULT_SETTINGS)
    test_settings._settings_from_file = lambda: {}
    test_settings._settings_from_env = lambda: {}
    test_settings._settings_from_args = lambda args: {}

    test_settings.init()
    assert settings.confirm is False
    assert settings.history_limit is None
    assert settings.no_colors is False
    assert settings.wait_command is None
    assert settings.wait_slow_command is 15
    assert settings.require_confirmation is True
    assert settings.slow_commands == ['(^|/)brew($| )']
    assert settings.exclude_rules == []
    assert settings.priority == {}
    assert settings.alter_history is False
    assert settings.instant_mode is False


# Generated at 2022-06-14 08:32:01.183510
# Unit test for method init of class Settings
def test_Settings_init():
    new_settings = Settings(const.DEFAULT_SETTINGS)
    new_settings.init(None)
    assert new_settings == settings



# Generated at 2022-06-14 08:32:04.142786
# Unit test for method init of class Settings
def test_Settings_init():
    settings.update(const.DEFAULT_SETTINGS)
    settings.init()
    assert settings == const.DEFAULT_SETTINGS



# Generated at 2022-06-14 08:32:09.333607
# Unit test for method init of class Settings
def test_Settings_init():
    """When `settings.py` is absent, we should create it and init with defaults.
    """
    args = Mock(spec=Namespace)
    settings.init(args=args)
    assert settings.require_confirmation is True
    assert settings.repeat is False
    assert settings.debug is False



# Generated at 2022-06-14 08:32:15.060990
# Unit test for method init of class Settings
def test_Settings_init():
    import mock

    s = Settings()
    s.init(mock.Mock(yes=True, debug=True, repeat=True))
    assert not s['require_confirmation']
    assert s['debug']
    assert s['repeat']

# Generated at 2022-06-14 08:32:22.554409
# Unit test for method init of class Settings
def test_Settings_init():
    import mock
    import sys
    args = mock.Mock()

    global settings
    settings = Settings(const.DEFAULT_SETTINGS)

    from .logs import exception
    exception_mock = mock.Mock()
    exception.side_effect = exception_mock

    settings.init()

    assert exception_mock.call_count == 0

    exception.side_effect = Exception()
    settings.init()

    assert exception_mock.call_count == 2



# Generated at 2022-06-14 08:32:30.209005
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import Log

    test_log = Log()
    test_settings = Settings(dict(rules = [], require_confirmation = True,
                                  history_limit = None, priority = {}))
    test_settings.user_dir = Path('test_user_dir')
    test_settings.user_dir.is_dir = Mock(return_value=True)
    test_settings.user_dir.joinpath('settings.py').is_file = Mock(return_value=True)
    test_settings.log = test_log
    test_settings.init()

    assert not test_log.error_log

# Generated at 2022-06-14 08:32:41.239918
# Unit test for method init of class Settings
def test_Settings_init():
    import os

    import mock
    from thefuck.settings import const

    settings.update(const.DEFAULT_SETTINGS)
    settings.init()

    assert settings.user_dir.joinpath('settings.py').is_file()
    with settings.user_dir.joinpath('settings.py').open() as settings_file:
        settings_py = settings_file.read()

    for setting in sorted(const.DEFAULT_SETTINGS.iteritems()):
        assert '# {} = {}'.format(*setting) in settings_py

    with mock.patch.object(settings, '_settings_from_env',
                           return_value={'rules': ['no, this is not ok']}):
        settings.init()
        assert settings['rules'] == ['no, this is not ok']


# Generated at 2022-06-14 08:32:56.309335
# Unit test for method init of class Settings
def test_Settings_init():
    settings.clear()
    class MockArgs(object):
        pass
    args = MockArgs()
    args.yes = True
    args.debug = True
    settings.init(args)
    settings.user_dir = '~/.thefuck' 
    assert settings.repeat == 1 and settings.require_confirmation == False and settings.debug == True


# Generated at 2022-06-14 08:33:08.606033
# Unit test for method init of class Settings
def test_Settings_init():
    from .system import create_file, remove_file

    path = Path('~/.thefuck_test').expanduser()
    # Remove the old config file
    try:
        remove_file(path)
    except OSError:
        pass

    settings.init()

    assert path.is_dir()
    # Remove the created config file
    remove_file(path)

    with path.open(mode='w') as settings_file:
        settings_file.write(const.SETTINGS_HEADER)
        settings_file.write(u'rules = ["test_rules"]\n')
        settings_file.write(u'exclude_rules = ["test_exclude_rules"]\n')
        settings_file.write(u'priority = {"test_rules": 100}\n')

# Generated at 2022-06-14 08:33:18.178790
# Unit test for method init of class Settings
def test_Settings_init():
    # create base_dir
    base_dir = Path('testdir')
    if base_dir.is_dir():
        base_dir.rmtree()
    assert not base_dir.is_dir()
    base_dir.mkdir()
    assert base_dir.is_dir()
    base_dir = base_dir.abspath()

    # create rules_dir
    rules_dir = base_dir.joinpath('rules')
    if rules_dir.is_dir():
        rules_dir.rmtree()
    assert not rules_dir.is_dir()
    rules_dir.mkdir()
    assert rules_dir.is_dir()
    rules_dir = rules_dir.abspath()

    # create settings file
    settings_file = base_dir.joinpath('settings.py')

# Generated at 2022-06-14 08:33:27.915552
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import logs
    from .manager import Manager
    from .utils import memoize

    args = attr.evolve(const.NamedArgs(), yes=True)
    logs.loggers = {}
    Manager._rules = Manager._exclude_rules = Manager._enabled_rules = None
    Manager._priority = const.DEFAULT_PRIORITY
    Manager._slow_commands = const.DEFAULT_SLOW_COMMANDS
    Manager._excluded_search_path_prefixes = []

    @memoize
    def _get_settings():
        return settings

    with settings.user_dir.joinpath('settings.py').open(mode='w') as _file:
        _file.write(u'rules = [\'ls\']\n')

# Generated at 2022-06-14 08:33:40.778674
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception
    assert const.DEFAULT_SETTINGS == settings
    settings.init()
    assert const.DEFAULT_SETTINGS == settings
    user_dir = settings._get_user_dir_path()
    assert user_dir.is_dir()
    assert user_dir.joinpath('settings.py').is_file()
    assert settings.user_dir == user_dir
    try:
        settings.update(settings._settings_from_file())
    except Exception:
        exception("Can't load settings from file", sys.exc_info())
    try:
        settings.update(settings._settings_from_env())
    except Exception:
        exception("Can't load settings from env", sys.exc_info())
    settings.update(settings._settings_from_args())

# Generated at 2022-06-14 08:33:44.390870
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()
    assert settings.user_dir != None
    assert const.DEFAULT_SETTINGS == settings

# Generated at 2022-06-14 08:33:47.333231
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()

    assert settings.user_dir.exists()
    assert settings.user_dir.joinpath('settings.py').is_file()

# Generated at 2022-06-14 08:34:00.229034
# Unit test for method init of class Settings
def test_Settings_init():
    # Check settings_from_env when ENV is the same as DEFAULT_SETTINGS
    env = settings.copy()
    env['require_confirmation'] = True
    result_when_env_match_default = settings._settings_from_env(env)
    assert result_when_env_match_default is None

    # Check settings_from_env when ENV is the same as DEFAULT_SETTINGS
    env['require_confirmation'] = False
    result_when_env_not_match_default = settings._settings_from_env(env)
    assert result_when_env_not_match_default is not None
    assert result_when_env_not_match_default['require_confirmation'] == env['require_confirmation']

    # Generate args

# Generated at 2022-06-14 08:34:00.929483
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()

# Generated at 2022-06-14 08:34:04.006157
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()
    assert settings == const.DEFAULT_SETTINGS


# Generated at 2022-06-14 08:34:20.409656
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings({'a': 1, 'b': 2})
    settings.init()
    assert settings['a'] == 1
    assert settings['b'] == 2
    assert settings.user_dir == Path('~/.config/thefuck').expanduser()


# Generated at 2022-06-14 08:34:33.338755
# Unit test for method init of class Settings
def test_Settings_init():
    from mock import patch, ANY
    from thefuck.conf.settings import Settings
    from thefuck.utils import get_closest, get_all_executables
    from textwrap import dedent
    import os

    with patch('thefuck.conf.settings.Settings._setup_user_dir') as setup_user_dir:
        with patch('thefuck.conf.settings.Settings._settings_from_file') as settings_from_file:
            with patch('thefuck.conf.settings.Settings._settings_from_env') as settings_from_env:
                with patch('thefuck.conf.settings.Settings._settings_from_args') as settings_from_args:
                    settings = Settings(const.DEFAULT_SETTINGS)
                    args = lambda: None
                    settings._init_settings_file()
                    args.yes = False


# Generated at 2022-06-14 08:34:45.311033
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception
    from .system import get_aliases
    from .match import get_closest

    called_exception = False
    def mock_exception(str, exc_info):
        global called_exception
        called_exception = True

    settings = Settings()
    settings.update({'get_closest': get_closest, 'get_aliases': get_aliases})
    exception = mock_exception
    settings['user_dir'] = '/foo/bar/user_dir'
    settings['settings_file'] = '/foo/bar/user_dir/settings.py'
    settings.init()
    assert not called_exception
    settings['user_dir'] = '~/.fuck/user_dir'

# Generated at 2022-06-14 08:34:48.150656
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings.get('require_confirmation')
    assert settings.get('wait_command') == 9
    assert settings.user_dir == Path('~/.config/thefuck').expanduser()

# Generated at 2022-06-14 08:34:50.059626
# Unit test for method init of class Settings
def test_Settings_init():
    assert settings.init().__class__.__name__ == "Settings"

# Generated at 2022-06-14 08:34:58.405189
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings.user_dir == settings._get_user_dir_path()
    assert settings.debug == False
    assert settings.require_confirmation == True
    assert settings.history_limit == None
    assert settings.rules == ['fuck']
    assert settings.exclude_rules == []
    assert settings.priority == {}
    assert settings.wait_command == 1
    assert settings.wait_slow_command == 15
    assert settings.slow_commands == []
    assert settings.excluded_search_path_prefixes == []
    assert settings.num_close_matches == 3
    assert settings.alter_history == True
    assert settings.repeat == False
    assert settings.no_colors == False
    assert settings.instant_mode == False


# Generated at 2022-06-14 08:35:09.281060
# Unit test for method init of class Settings
def test_Settings_init():
    import sys
    import os

    restore_env = dict(os.environ)
    restore_argv = sys.argv
    restore_stderr = sys.stderr
    restore_stdout = sys.stdout
    restore_settings = settings

    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import StringIO


# Generated at 2022-06-14 08:35:19.824943
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings.change_history == True
    settings.init(args = argparse.Namespace(yes = True, debug = False, repeat = False))
    assert settings.require_confirmation == False
    assert settings.change_history == True
    settings.init(args = argparse.Namespace(yes = False, debug = True, repeat = False))
    assert settings.debug == True
    assert settings.change_history == True
    settings.init(args = argparse.Namespace(yes = False, debug = False, repeat = True))
    assert settings.repeat == True
    assert settings.change_history == True
    settings.init(args = argparse.Namespace(yes = True, debug = True, repeat = True))
    assert settings.require_confirmation == False
    assert settings.debug == True
    assert settings

# Generated at 2022-06-14 08:35:28.608923
# Unit test for method init of class Settings
def test_Settings_init():
    import os
    from .logs import exception
    from .command import Command
    from .system import TmpDir
    from .utils import memoize
    from .rules import Rule
    from .match import always_true
    from unittest.mock import patch, Mock

    # prepare mock
    exception_mock = Mock()
    exception_method = exception.__wrapped__


# Generated at 2022-06-14 08:35:41.137493
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init(args=None)
    # first check 'rules'
    rules_list = {'bash': 3, u'git': 3, u'hg': 3, u'mvn': 2, u'perl': 3,
                  u'pip': 2, u'python': 3, u'ruby': 3, u'vim': 3}
    for rule in rules_list.items():
        code_file = settings.user_dir.joinpath('rules', '{}.py'.format(rule[0]))
        if not code_file.is_file():
            return False
    # then check other basic key-pairs
    default_settings = const.DEFAULT_SETTINGS
    for key, value in default_settings.items():
        if settings[key] != value:
            return False
    # then check env-related

# Generated at 2022-06-14 08:36:15.620231
# Unit test for method init of class Settings
def test_Settings_init():
    from .tests import unit

    def check():
        assert settings.rules == const.DEFAULT_RULES
        assert settings.require_confirmation == True
        assert settings.alias == 'fuck'
        assert settings.priority == {}
        assert settings.no_colors == False
        assert settings.debug == False
        assert settings.script == None
        assert settings.exclude_rules == []
        assert settings.history_limit == None
        assert settings.wait_command == 0
        assert settings.alter_history == True
        assert settings.repeat == False
        assert settings.wait_slow_command == 3
        assert settings.slow_commands == ['lein', 'react-native', 'gradle', './gradlew', 'vagrant']
        assert settings.excluded_search_path_prefixes == ['/usr/local/bin']


# Generated at 2022-06-14 08:36:16.704325
# Unit test for method init of class Settings
def test_Settings_init():
    global settings
    settings.init()


# Generated at 2022-06-14 08:36:28.451090
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings['rules'] == const.DEFAULT_RULES
    assert settings['exclude_rules'] == []
    assert settings['history_limit'] == None
    assert settings['replace_command'] == False

    settings.init(args=('thefuck', '--yes'))
    assert settings['require_confirmation'] == False
    assert settings['debug'] == False
    assert settings['repeat'] == False

    settings.init(args=('thefuck', '--debug', '--repeat'))
    assert settings['require_confirmation'] == True
    assert settings['debug'] == True
    assert settings['repeat'] == True

# Generated at 2022-06-14 08:36:39.759600
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings(const.DEFAULT_SETTINGS)
    from .logs import exception
    from .logs import warning
    from .logs import log

    settings.init()

    exception.assert_called_with(u"Can't load settings from file (%s: %s)", (Exception, Exception()), {})
    exception.assert_called_with(u"Can't load settings from env (%s: %s)", (Exception, Exception()), {})
    warning.assert_called_with(u'Config path ~/.thefuck is deprecated. Please move to ~/.config/thefuck')
    log.assert_called_with(u"Settings loaded from {}".format(settings.user_dir.joinpath('settings.py')))


# Generated at 2022-06-14 08:36:48.575823
# Unit test for method init of class Settings
def test_Settings_init():
    args = None
    path = '/tmp/.config/thefuck/settings.py'
    # expected = {'require_confirmation': {'require': False, 'reason': 'order'}, 'history_limit': 0, 'wait_command': {'wait': False, 'reason': ''}, 'alter_history': False, 'exclude_rules': ['git_push'], 'rules': ['git_root_check'], 'priority': {'git_root_check': 1, 'git_push': 2}, 'wait_slow_command': {'wait': False, 'reason': ''}, 'slow_commands': ['lein', 'reboot', 'vagrant'], 'num_close_matches': 0, 'no_colors': False, 'instant_mode': False, 'excluded_search_path_prefixes': [], 'debug': False}



# Generated at 2022-06-14 08:36:50.142544
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()


# Generated at 2022-06-14 08:36:57.014989
# Unit test for method init of class Settings
def test_Settings_init():
    """
    Asserts if the init method of the class Settings loads the constants
    correctly and updates them if a value is passed through arguments
    """
    new_settings = Settings(const.DEFAULT_SETTINGS)
    new_settings.init(args=type('Test', (object,), {'yes': True}))
    assert new_settings.require_confirmation == False

# Generated at 2022-06-14 08:36:58.687586
# Unit test for method init of class Settings
def test_Settings_init():
    if settings.init(args=True):
        print("Settings is set up")
    else:
        print("Settings is not set up")

# Generated at 2022-06-14 08:37:09.653802
# Unit test for method init of class Settings
def test_Settings_init():
    """
    Test Settings.init() with different cases
    """
    import sys
    from test_settings import create_temp_config
    from thefuck.utils import get_closest

    class EmptyPath(object):
        def is_dir(self):
            return True

    class EmptyFile(object):
        def is_file(self):
            return True

    class EmptyArgs(object):
        def __init__(self):
            self.yes = None
            self.debug = None
            self.repeat = None

    class CustomArgs(object):
        def __init__(self, yes=True, debug=True, repeat=True):
            self.yes = yes
            self.debug = debug
            self.repeat = repeat

    class Args:
        _rules_from_env = Settings()._rules_from_env
       

# Generated at 2022-06-14 08:37:23.395681
# Unit test for method init of class Settings
def test_Settings_init():
    """
    check if the `init` method fills the `settings` attribute of class Settings
    with correct values
    """
    settings.init()
    assert settings['require_confirmation'] == const.DEFAULT_SETTINGS['require_confirmation']
    assert settings['rules'] == const.DEFAULT_SETTINGS['rules']
    assert settings['wait_command'] == const.DEFAULT_SETTINGS['wait_command']
    assert settings['history_limit'] == const.DEFAULT_SETTINGS['history_limit']
    assert settings['slow_commands'] == const.DEFAULT_SETTINGS['slow_commands']
    assert settings['wait_slow_command'] == const.DEFAULT_SETTINGS['wait_slow_command']

# Generated at 2022-06-14 08:37:56.932561
# Unit test for method init of class Settings
def test_Settings_init():
    # override _get_user_dir_path
    old_get_user_dir_path = Settings._get_user_dir_path

# Generated at 2022-06-14 08:38:11.031857
# Unit test for method init of class Settings
def test_Settings_init():
    from tempfile import mkdtemp
    from shutil import rmtree

    def touch(name):
        file(name, 'a').close()

    config = mkdtemp()
    touch(os.path.join(config, 'settings.py'))
    touch(os.path.join(os.path.join(config, 'thefuck'), 'settings.py'))
    rules = mkdtemp()
    touch(os.path.join(rules, '__init__.py'))
    touch(os.path.join(os.path.join(rules, 'thefuck'), '__init__.py'))
    os.environ['XDG_CONFIG_HOME'] = config
    os.environ['TF_SOMEVAR'] = 'FOO'

# Generated at 2022-06-14 08:38:19.477850
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import log_to_file, log_command
    from .config import _get_version
    from .utils import get_closest

    args=defs.args
    settings.init(args)

    assert settings.user_dir.is_dir()
    assert settings.config_dir.is_dir()
    assert settings.bin_path.is_file()
    assert settings.wait_command
    assert settings.alter_history
    assert settings.history_limit
    assert settings.wait_slow_command
    assert settings.slow_commands
    assert settings.require_confirmation
    assert settings.env
    assert settings.exclude_rules
    assert settings.priority
    assert settings.no_colors
    assert settings.excluded_search_path_prefixes
    assert settings.num_close_matches


# Generated at 2022-06-14 08:38:25.444455
# Unit test for method init of class Settings
def test_Settings_init():
    _settings = Settings(const.DEFAULT_SETTINGS)
    _settings.init()
    assert _settings.user_dir == Path('~/.config/thefuck').expanduser()
    assert _settings.user_dir.joinpath('settings.py').is_file()
    assert _settings.confirm == const.DEFAULT_SETTINGS['confirm']

# Generated at 2022-06-14 08:38:31.530948
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import logger
    from .logs import set_log_level

    _logger = logger

    try:
        logger = lambda: None
        logger.exception = Exception

        set_log_level('')
        settings_init = Settings(const.DEFAULT_SETTINGS)
        settings_init.init()
    finally:
        logger = _logger

# Generated at 2022-06-14 08:38:35.755626
# Unit test for method init of class Settings
def test_Settings_init():
    from .system import Path

    settings.init()
    defaults = const.DEFAULT_SETTINGS
    assert settings.user_dir == Path(defaults['user_dir'])


# Generated at 2022-06-14 08:38:42.734959
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import logger
    assert settings == const.DEFAULT_SETTINGS
    old_exception = logger.exception
    exception_count = 0
    def new_exception(msg, *args):
        nonlocal exception_count
        exception_count += 1
    logger.exception = new_exception
    settings.init()
    assert exception_count == 2
    logger.exception = old_exception

# Generated at 2022-06-14 08:38:48.109299
# Unit test for method init of class Settings
def test_Settings_init():
    args = type('args', (), {})

    actual = settings.init(args)
    assert actual is None
    assert settings.user_dir == Path('.thefuck')
    assert settings['require_confirmation']
    assert settings['history_limit'] == 8
    assert settings['no_colors']
    assert settings['wait_command'] == 2
    assert settings['repeat'] == 1

# Generated at 2022-06-14 08:38:49.774576
# Unit test for method init of class Settings
def test_Settings_init():
    settings_init = Settings()
    settings_init.init()
    assert settings == settings_init

# Generated at 2022-06-14 08:38:57.856934
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception
    from .system import TemporaryDirectory
    from .exceptions import TheFuckException
    from six import StringIO
    import mock
    import sys

    with TemporaryDirectory() as tmp:
        user_dir = Path(tmp) / 'settings.py'
        user_dir.write_text(const.SETTINGS_HEADER)
        settings = Settings()

        with mock.patch.object(settings, '_settings_from_file', side_effect=TheFuckException):
            with mock.patch.object(settings, '_setup_user_dir'):
                with mock.patch.object(sys, 'stderr', new_callable=StringIO):
                    exception('Can\'t load settings from file', (TheFuckException, TheFuckException('test'), None))
                    settings.init()

# Generated at 2022-06-14 08:39:54.204332
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception
    from . import test

    import io
    import os
    from thefuck.settings import Settings
    from thefuck.const import DEFAULT_SETTINGS
    from thefuck.system import Path

    def get_user_dir_path(*args):
        return Path('~/.config/thefuck').expanduser()

    def _init_settings_file(*args):
        return None

    def _settings_from_file(*args):
        return {}

    def _settings_from_env(*args):
        return {}

    def _settings_from_args(args):
        if args == None:
            return {}
        return {'repeat': args.repeat}

    settings = Settings(DEFAULT_SETTINGS)
    settings._setup_user_dir = get_user_dir_path
    settings._init

# Generated at 2022-06-14 08:39:57.532275
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings.get('require_confirmation') == True
    settings.init({'yes': True})
    assert settings.get('require_confirmation') == False

# Generated at 2022-06-14 08:40:02.986043
# Unit test for method init of class Settings
def test_Settings_init():
    assert settings.init() == {'rules': ()}
    assert settings.init({'yes': True}) == {'rules': (), 'require_confirmation': False}
    assert settings.init({'debug': True}) == {'rules': (), 'debug': True}
    assert settings.init({'repeat': True}) == {'rules': (), 'repeat': True}

# Generated at 2022-06-14 08:40:07.795607
# Unit test for method init of class Settings
def test_Settings_init():
    args = argparse.Namespace(yes=True, debug=True, repeat=1)
    settings.init(args)
    assert settings.require_confirmation == False
    assert settings.debug == True
    assert settings.repeat == 1

# Generated at 2022-06-14 08:40:16.204680
# Unit test for method init of class Settings
def test_Settings_init():
    # test_file_not_exist
    settings.init(None)
    assert True

    # test_file_exist
    settings.init(None)
    with settings.user_dir.joinpath('settings.py').open() as fd:
        assert fd.read() == const.SETTINGS_HEADER

        for setting in const.DEFAULT_SETTINGS.items():
            assert u'# {} = {}\n'.format(*setting) in fd.readlines()

# Generated at 2022-06-14 08:40:25.407809
# Unit test for method init of class Settings
def test_Settings_init():

    test_args = {'yes': True, 'debug': True, 'repeat': 3}
    class Test_args:
        def __init__(self, **test_args):
            self.__dict__.update(test_args)

    # test _init_settings_file:
    test_setting = Settings({})
    test_setting._init_settings_file()
    assert test_setting.user_dir.joinpath('settings.py').is_file()

    # test _setup_user_dir:
    test_setting = Settings({})
    test_setting._setup_user_dir()
    assert test_setting.user_dir.joinpath('rules').is_dir() is True

    # test _settings_from_file:
    test_setting = Settings({})
    test_setting._init_settings_file()

# Generated at 2022-06-14 08:40:35.350625
# Unit test for method init of class Settings
def test_Settings_init():
    global settings
    args = lambda yes=False, debug=False, repeat=False: type('', (object,), {'yes': yes, 'debug': debug, 'repeat': repeat})()
    settings.init()
    settings.init(args(yes=True))
    settings.init(args(debug=True))
    settings.init(args(repeat=10))
    assert settings.get('require_confirmation') == False
    assert settings.get('debug') == True
    assert settings.get('repeat') == 10


# Generated at 2022-06-14 08:40:39.448939
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    expected = Path.home().joinpath('.config', 'thefuck')
    assert settings.user_dir == expected

# Generated at 2022-06-14 08:40:40.906648
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()

    assert settings.user_dir

# Generated at 2022-06-14 08:40:42.799479
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings.user_dir.endswith('.config/thefuck')