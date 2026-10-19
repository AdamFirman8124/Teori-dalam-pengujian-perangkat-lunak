

# Generated at 2022-06-14 08:31:56.242794
# Unit test for method init of class Settings
def test_Settings_init():
    import mock

    saved_user_dir = settings.user_dir
    saved_settings = settings._settings_from_file.__code__
    saved_env = settings._settings_from_env.__code__
    saved_args = settings._settings_from_args.__code__

    settings.user_dir = None
    settings._settings_from_file.__code__ = None
    settings._settings_from_env.__code__ = None
    settings._settings_from_args.__code__ = None


# Generated at 2022-06-14 08:32:06.662279
# Unit test for method init of class Settings
def test_Settings_init():
    settings_dict = {
        'require_confirmation': False,
        'rules': ['test_rules'],
        'exclude_rules': ['test_exclude_rules'],
        'priority': {'test_priority_key': 5},
        'wait_command': 3,
        'history_limit': 4,
        'wait_slow_command': 5,
        'no_colors': False,
        'debug': True,
        'alter_history': False,
        'instant_mode': False,
        'repeat': False,
        'slow_commands': ['test_slow_commands'],
        'excluded_search_path_prefixes': ['test_excluded_search_path_prefixes'],
        'num_close_matches': 6
    }

    assert settings.init() == settings_

# Generated at 2022-06-14 08:32:20.165317
# Unit test for method init of class Settings
def test_Settings_init():
    user_dir_path = os.path.join(os.path.dirname(__file__), '..', 'tests', 'dummy_home')
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()
    assert settings.user_dir == Path(user_dir_path)
    assert settings['require_confirmation'] == True
    os.environ['THEFUCK_NO_COLORS'] = 'True'
    settings.init()
    assert settings['no_colors'] == True
    os.environ['THEFUCK_EXCLUDE_RULES'] = 'git:DEFAULT_RULES'
    settings.init()
    assert 'git' in settings['exclude_rules']
    assert 'git_push' in settings['rules']

# Generated at 2022-06-14 08:32:27.430637
# Unit test for method init of class Settings
def test_Settings_init():
    #
    # given
    os.environ['THEFUCK_RULES'] = 'DEFAULT_RULES'
    os.environ['THEFUCK_PRIORITY'] = 'git_push=60:git_commit=55'
    os.environ['THEFUCK_EXCLUDE_RULES'] = 'git_push'
    os.environ['THEFUCK_EXCLUDE_RULES'] = 'git_push'
    os.environ['THEFUCK_WAIT_COMMAND'] = '5'
    # os.environ['THEFUCK_NO_COLORS'] = 'True'
    os.environ['THEFUCK_REQUIRE_CONFIRMATION'] = 'True'
    os.environ['THEFUCK_ALTER_HISTORY'] = 'True'


# Generated at 2022-06-14 08:32:40.122520
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import patch_logger
    from .config import clear_cache, get_settings
    from .logs import reset_loggers
    from .utils import wrap_streams
    from mock import patch, Mock
    from io import StringIO


# Generated at 2022-06-14 08:32:51.527676
# Unit test for method init of class Settings
def test_Settings_init():
    """Settings.init() should initalize settings attributes by settings.py and env."""
    assert sys.argv[0].endswith("tools/runner.py")
    from .system import get_current_dir, restore_current_dir
    settings_path = settings.user_dir.joinpath("settings.py")
    assert settings_path.is_file()

    settings.init()
    test_path = settings.user_dir.joinpath("test")
    test_path.mkdir()
    saved_path = get_current_dir()

# Generated at 2022-06-14 08:32:59.246957
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception

    global settings
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init(args=None)
    assert settings.user_dir == settings._get_user_dir_path()
    settings_path = settings.user_dir.joinpath('settings.py')
    assert settings_path.is_file()
    settings.init(args=None)
    settings['key'] = 'val'
    assert settings['key'] == settings.key
    try:
        settings.init(args=None)
        assert 0
    except SystemExit:
        assert 1
    try:
        settings.init(args=None)
    except:
        assert 1
    settings['user_dir'] = '/tmp'

# Generated at 2022-06-14 08:33:10.708603
# Unit test for method init of class Settings
def test_Settings_init():
    from mock import patch, Mock
    from datetime import datetime

    with patch('thefuck.settings.Settings.update'):
        settings.init()


# Generated at 2022-06-14 08:33:24.018680
# Unit test for method init of class Settings
def test_Settings_init():
    settings.update(paths=[])
    settings.init()
    assert settings['paths'] == os.environ['PATH'].split(':')
    assert isinstance(settings['rules'], list) or isinstance(settings['rules'], tuple)
    assert isinstance(settings['exclude_rules'], list) or \
           isinstance(settings['exclude_rules'], tuple)
    assert isinstance(settings['priority'], dict)

    # Test for init from file
    with settings.user_dir.joinpath('settings.py').open() as fd:
        fd.write('rules = ("ls",)')
    settings.update(rules=None)
    settings.init()
    assert settings['rules'] == ('ls',)

    # Test for init from env

# Generated at 2022-06-14 08:33:31.424171
# Unit test for method init of class Settings
def test_Settings_init():
    import mock

    args = mock.Mock()

    assert settings.get('prioritize_by_number_of_words', None) is None
    settings.init(args)
    settings.update(const.DEFAULT_SETTINGS)
    assert settings.get('prioritize_by_number_of_words', None) is None
    assert settings.get('alter_history', None) is True
    assert settings.get('repeat', None) is None

    args.yes = True
    settings.init(args)
    assert settings.get('require_confirmation', None) is False
    assert settings.get('repeat', None) is None

    args.yes = False
    settings.init(args)
    assert settings.get('require_confirmation', None) is True
    assert settings.get('repeat', None) is None

# Generated at 2022-06-14 08:34:01.197168
# Unit test for method init of class Settings
def test_Settings_init():
    # Init settings.py and env
    settings.init()

    # Test for method _settings_from_file
    assert settings['require_confirmation'] == True
    assert settings['exclude_rules'] == ('root',)
    assert settings['wait_command'] == 1
    assert settings['no_colors'] == False

    # Test for method _settings_from_env
    os.environ['THEFUCK_REQUIRE_CONFIRMATION'] = 'false'
    os.environ['THEFUCK_EXCLUDE_RULES'] = 'root:git_push'
    os.environ['THEFUCK_WAIT_COMMAND'] = '2'
    os.environ['THEFUCK_NO_COLORS'] = 'true'

# Generated at 2022-06-14 08:34:08.058760
# Unit test for method init of class Settings
def test_Settings_init():
    class Args:
        yes = True
        debug = True
        repeat = True

    settings.init(Args)
    assert settings.require_confirmation is False
    assert settings.debug is True
    assert settings.repeat == 3
    settings.init()
    assert settings.require_confirmation is True
    assert settings.debug is False
    assert settings.repeat == 1

# Generated at 2022-06-14 08:34:18.425859
# Unit test for method init of class Settings
def test_Settings_init():
    args = ''
    settings_obj = Settings(const.DEFAULT_SETTINGS)
    settings_obj.init(args)
    assert settings_obj['require_confirmation'] == True
    assert settings_obj['wait_command'] == 3
    assert settings_obj['slow_commands'] == ['lein', 'gradle', './gradlew', 'rebar3', './rebar3']
    assert settings_obj['history_limit'] == 0
    assert settings_obj['repeat'] == 0
    assert settings_obj['wait_slow_command'] == 15
    assert settings_obj['num_close_matches'] == 3
    assert settings_obj['alter_history'] == False

# Generated at 2022-06-14 08:34:25.305268
# Unit test for method init of class Settings
def test_Settings_init():
    settings_ = Settings(const.DEFAULT_SETTINGS)
    settings_.init()
    assert isinstance(settings_, Settings)
    assert settings_.user_dir == Path(os.environ['XDG_CONFIG_HOME'], 'thefuck').expanduser()
    assert settings_['rules'] == const.DEFAULT_RULES


# Generated at 2022-06-14 08:34:36.864420
# Unit test for method init of class Settings
def test_Settings_init():
    """ settings.init()
        Given
            1. In user_dir there is no settings.py
            2. There are no env vars
        When
            Call settings.init()
        Then
            1. settings.py was created
            2. All values of settings were set to default values
        Given
            1. In user_dir there is settings.py with valid settings
            2. There are no env vars
        When
            Call settings.init()
        Then
            1. settings.py was not changed
            2. All values of settings were set to values from settings.py
    """
    import os, shutil
    from .logs import exception
    from .system import Path
    from . import const
    from .settings import Settings

    # init settings to default values
    user_dir = Path(__file__).parent.parent.join

# Generated at 2022-06-14 08:34:50.476753
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import logger
    from .utils import memoize
    from .system import DO_NOT_PARSE_COMMANDS
    args = {
        'yes': False,
        'debug': False,
        'repeat': 0
    }
    settings = Settings()
    settings.init(args)

    assert settings.user_dir == Path('~', '.config', 'thefuck').expanduser()
    assert settings.require_confirmation is True
    assert settings.debug is False
    assert settings.repeat == 0
    assert settings.priority == {'man': 10,
                                 'brew': 9,
                                 'cd': 8,
                                 'ls': 7,
                                 'git': 6,
                                 'history': 5}
    assert Path(settings.user_dir.joinpath('settings.py')).is_file

# Generated at 2022-06-14 08:34:58.281768
# Unit test for method init of class Settings
def test_Settings_init():
    import pytest
    settings.update({'require_confirmation': False, 'debug': True, 'repeat': 2})
    sys.argv = ['thefuck', '--yes', '--debug=False', '--repeat=3']
    from . import main
    settings.init(main.get_args())
    assert settings['require_confirmation'] == True
    assert settings['debug'] == False
    assert settings['repeat'] == 3



# Generated at 2022-06-14 08:35:09.252200
# Unit test for method init of class Settings
def test_Settings_init():
    import os
    import shutil

    settings.clear()

    test_file_path = Path('.').joinpath('test_settings.py')
    test_file_path.open(mode='w').close()

    os.environ['TF_WAIT_COMMAND'] = '42'

    args = type('args', (object,), {'debug': None})

    try:
        settings.init(args)

        assert settings.debug
        assert settings.wait_command == 42
        assert settings.repeat is None
    finally:
        os.remove(str(test_file_path))
        if 'TF_WAIT_COMMAND' in os.environ:
            del os.environ['TF_WAIT_COMMAND']

# Generated at 2022-06-14 08:35:18.634576
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings['require_confirmation'] == True
    assert settings['no_colors'] == False
    assert settings['wait_command'] == 0.5
    assert settings['history_limit'] == 1000
    assert settings['wait_slow_command'] == 1
    assert settings['rules'] == ['fuck_lazy_command']
    assert settings['exclude_rules'] == []
    assert settings['priority'] == {'fuck_lazy_command': 1}
    assert settings['debug'] == False


# Generated at 2022-06-14 08:35:28.139576
# Unit test for method init of class Settings
def test_Settings_init():
    from .rules import RulesCollection

    def get_settings_from_env(settings_dict):
        from mock import patch
        from six import iteritems

        env_patch = {}
        for env, attr in iteritems(const.ENV_TO_ATTR):
            env_patch[env] = settings_dict.get(attr)
        env_patch['XDG_CONFIG_HOME'] = '/test/'
        user_dir = '/test/thefuck'

        with patch.dict('os.environ', env_patch):
            settings = Settings(const.DEFAULT_SETTINGS)
            settings.init()
        return settings

    # Test settings from file
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.user_dir = '/test/thefuck'

# Generated at 2022-06-14 08:36:07.825931
# Unit test for method init of class Settings
def test_Settings_init():
    settings_init = Settings(const.DEFAULT_SETTINGS)
    with pytest.raises(Exception):
        settings_init.init()
    settings_init.init(args=Namespace(yes=True, debug=False, repeat=2))
    assert settings_init['require_confirmation'] is False
    assert settings_init['debug'] is False
    assert settings_init['repeat'] == 2

settings.init()

# Generated at 2022-06-14 08:36:11.917571
# Unit test for method init of class Settings
def test_Settings_init():
    global settings
    settings.init()
    assert settings['require_confirmation'] == True
    assert settings.user_dir == Path('/home/user/.config/thefuck')
    assert settings.rules == [u'fuck']

# Generated at 2022-06-14 08:36:20.105005
# Unit test for method init of class Settings

# Generated at 2022-06-14 08:36:33.250691
# Unit test for method init of class Settings
def test_Settings_init():
    """Unit test for method init of class Settings"""
    settings.init()

    assert settings['require_confirmation'] == False
    assert settings['no_colors'] == False
    assert settings['debug'] == False
    assert settings['rules'] == const.DEFAULT_RULES
    assert settings['exclude_rules'] == []
    assert settings['alter_history'] == True
    assert settings['wait_command'] == 0
    assert settings['wait_slow_command'] == 15
    assert settings['prefix_queue_length'] == 1
    assert settings['priority'] == {}
    assert settings['history_limit'] == None
    assert settings['slow_commands'] == ['lein', 'gradle', 'rebar', 'tsc', 'bower']
    assert settings['instant_mode'] == False

# Generated at 2022-06-14 08:36:34.502539
# Unit test for method init of class Settings
def test_Settings_init():
    assert settings.init() == None

# Generated at 2022-06-14 08:36:35.737932
# Unit test for method init of class Settings
def test_Settings_init():
    assert settings.init() == {}
    assert settings.init() == {}

# Generated at 2022-06-14 08:36:46.403782
# Unit test for method init of class Settings
def test_Settings_init():
    global settings
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()

    assert settings.get('require_confirmation') == True
    assert settings.get('wait_command') == 3
    assert settings.get('history_limit') == 10
    assert settings.get('priority') == {
        'echo': 100
    }
    assert settings.get('rules') == ['echo']
    assert settings.get('exclude_rules') == ['git_push']
    assert settings.get('no_colors') == False
    assert settings.get('debug') == False
    assert settings.get('alter_history') == False
    assert settings.get('insert_before') == 'eval $(thefuck $(fc -ln -1))'
    assert settings.get('wait_slow_command') == 15
    assert settings.get

# Generated at 2022-06-14 08:36:54.407093
# Unit test for method init of class Settings
def test_Settings_init():
    test_settings = Settings()
    test_settings.init()
    assert test_settings['rules'] == ([
        'confirm',
        'python',
        'system',
        'brew',
        'gem',
        'docker',
        'gcloud',
        'git'])
    assert test_settings['history_limit'] == 100000
    assert test_settings['wait_command'] == 10
    assert test_settings['require_confirmation'] == True
    assert test_settings['exclude_rules'] == []
    assert test_settings['no_colors'] == False
    assert test_settings['slow_commands'] == [
        r'((^|/|\\)g?(ba|z)?sh(\s|\z)|curl\s)']
    assert test_settings['wait_slow_command'] == 15


# Generated at 2022-06-14 08:36:56.804146
# Unit test for method init of class Settings
def test_Settings_init():
    """Test method init of class Settings"""
    args = type('argparse.Namespace', (), {'debug': True, 'repeat': 3})
    settings.init(args)
    assert settings['debug'] == True

# Generated at 2022-06-14 08:37:00.661792
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings(const.DEFAULT_SETTINGS)

    settings.user_dir = Path(__file__).parent.joinpath('config')
    settings.init()

    print(settings['debug'])

# Generated at 2022-06-14 08:38:16.373248
# Unit test for method init of class Settings
def test_Settings_init():  # NOQA
    from os import environ
    from os import remove
    from os import rmdir
    from os import mkdir
    from tempfile import mkdtemp
    from shutil import rmtree
    from six import print_

    settings.init()
    assert settings.user_dir == Path('~/.config/thefuck').expanduser()

    settings.init()
    settings.user_dir = Path('~/.config/thefuck').expanduser()
    assert settings.user_dir == Path('~/.config/thefuck').expanduser()

    settings.init()
    del settings.user_dir
    assert settings.user_dir == Path('~/.config/thefuck').expanduser()


# Generated at 2022-06-14 08:38:29.371686
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()

    assert settings['require_confirmation']
    assert settings['wait_command'] == const.DEFAULT_SETTINGS['wait_command']
    assert settings['wait_slow_command'] == const.DEFAULT_SETTINGS['wait_slow_command']
    assert settings['rules'] == const.DEFAULT_RULES
    assert settings['exclude_rules'] == []
    assert settings['slow_commands'] == []
    assert settings['priority'] == {}
    assert settings['history_limit'] == const.DEFAULT_SETTINGS['history_limit']
    assert settings['num_close_matches'] == const.DEFAULT_SETTINGS['num_close_matches']
    assert settings['no_colors'] == const.DEFAULT_SETTINGS['no_colors']

# Generated at 2022-06-14 08:38:38.879291
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception, log
    from contextlib import contextmanager

    @contextmanager
    def mock_exception(text):
        try:
            yield
        except Exception as e:
            assert str(e) == text

    def test_method_call(method_name, value, message=None):
        def mock_method():
            return {'value': value}
        mock = Mock()
        mock.method = mock_method
        with mock_exception(message):
            settings._init_settings_file()
            setattr(settings, method_name, mock.method)
            settings.init()
            assert getattr(settings, 'value', None) == value

    test_method_call('_settings_from_file', {'value': 'from_file'})

# Generated at 2022-06-14 08:38:48.671822
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import capture_logs
    from .system import CalledProcessError
    from .utils import get_closest, prepare_for_history
    from .exceptions import FailedCommand

    # with prepare_for_history, it will read the command from history
    settings.init()
    with prepare_for_history('fuck', 'echo "fuck_echo"', 'echo "fuck_echo"'):
        assert settings.get_command() == 'echo "fuck_echo"'

    # with capture_logs, it will also read the command from history, but will
    # log the command

# Generated at 2022-06-14 08:39:01.919768
# Unit test for method init of class Settings
def test_Settings_init():
    from .config import settings
    from .logs import exception
    from .system import Path
    from unittest.mock import patch
    import sys

    def raise_exc(ex):
        raise ex

    @patch.object(Path, 'expanduser', return_value=Path('HOME'))
    def test_settings_from_file(_):
        args = patch.object(settings, '_settings_from_args', return_value={})
        exception_ = patch('thefuck.config.exception', return_value=None)
        default_settings = {'correct': 'True', 'wait_command': 3,
                            'require_confirmation': True}


# Generated at 2022-06-14 08:39:15.104454
# Unit test for method init of class Settings
def test_Settings_init():
    args = type('args', (object,), {'yes': False, 'debug': False, 'repeat': False})
    def _settings_from_args(args):
        return {'require_confirmation': True, 'debug': False, 'repeat': False}
    settings._settings_from_args = _settings_from_args

    old_user_dir = os.environ.get('XDG_CONFIG_HOME', None)
    os.environ['XDG_CONFIG_HOME'] = '~/.config'
    settings['user_dir'] = Path('~/.config/thefuck')
    settings['user_dir'].joinpath('settings.py').touch()
    settings['user_dir'].joinpath('rules').mkdir(parents=True)

# Generated at 2022-06-14 08:39:22.750455
# Unit test for method init of class Settings
def test_Settings_init():
    import sys
    import os
    from ._testcase import TestCase
    from thefuck.settings import Settings, const
    from thefuck.logs import _log_file
    env_val = "_ENV_VAL_"
    file_val = "_FILE_VAL_"
    args_val = "_ARGS_VAL_"
    env_to_attr = const.ENV_TO_ATTR.items()
    settings = Settings()
    test = TestCase()
    test.settings = settings
    test.settings.clear()

    # Test different value combinations of method init, change env,
    # settings file, args when necessary

# Generated at 2022-06-14 08:39:24.023601
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()


# Generated at 2022-06-14 08:39:34.252525
# Unit test for method init of class Settings
def test_Settings_init():
    """Checks initialization of settings"""

    default_settings = const.DEFAULT_SETTINGS.copy()
    default_settings['user_dir'] = Path(settings['user_dir'])

    assert settings == default_settings

    os.environ['XDG_CONFIG_HOME'] = '/some/path/to'
    settings.init()
    assert settings['user_dir'] == Path('/some/path/to/thefuck')
    del os.environ['XDG_CONFIG_HOME']

    settings.init('not empty args')

    assert settings['user_dir'] == Path(settings['user_dir'])
    assert settings['repeat'] == -1



# Generated at 2022-06-14 08:39:42.696734
# Unit test for method init of class Settings
def test_Settings_init():
    """
    This unit test for Settings.init() method
    """
    from tempfile import mkdtemp
    from shutil import rmtree
    from .test_utils import CopiedSettings, CopiedRules

    with CopiedSettings(), CopiedRules():
        try:
            settings.init()
            assert settings.user_dir == const.DEFAULT_USER_DIR
            assert settings.confirmation_timeout == const.DEFAULT_TIMEOUT
            assert settings.require_confirmation == True
        finally:
            pass