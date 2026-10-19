

# Generated at 2022-06-14 08:32:18.422466
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()

    def test():
        settings.update(settings._settings_from_file())
        settings.update(settings._settings_from_env())
        settings.update(settings._settings_from_args(['--yes', '--debug', '--repeat', '2']))

        #compare settings get from settings.py and settings get from env
        assert settings.get('history_limit') == 42
        assert settings.get('no_colors') == True
        assert settings.get('verbose') == False

        #compare settings get from args
        assert settings.get('require_confirmation') == False
        assert settings.get('debug') == True
        assert settings.get('repeat') == 2

    test()

# Generated at 2022-06-14 08:32:29.273594
# Unit test for method init of class Settings
def test_Settings_init():
    import collections
    import copy
    import os
    import sys
    from mock import patch

    sys.modules['settings'] = type('settings', (object, ),
                                   collections.defaultdict(lambda: 'value'))
    os.environ['THEFUCK_RULES'] = ':'.join(['DEFAULT_RULES', 'zsh'])
    os.environ['THEFUCK_PRIORITY'] = 'zsh=2:python=1'
    os.environ['THEFUCK_WAIT_COMMAND'] = '5'
    os.environ['THEFUCK_WAIT_SLOW_COMMAND'] = '2'
    os.environ['THEFUCK_NO_COLORS'] = 'True'
    os.environ['THEFUCK_DEBUG'] = 'True'
    os

# Generated at 2022-06-14 08:32:38.339346
# Unit test for method init of class Settings
def test_Settings_init():
    import sys

    import mock
    from thefuck.logs import exception

    args = mock.MagicMock()
    args.yes = True
    args.repeat = 10
    args.debug = True

    settings.init(args)

    sys.modules['settings'] = mock.Mock()
    settings.init(args)

    settings._settings_from_file = mock.Mock(side_effect=Exception)
    with mock.patch('thefuck.settings.exception') as exception_mock:
        settings.init(args)
        assert exception_mock.call_count == 1

    settings._settings_from_env = mock.Mock(side_effect=Exception)
    with mock.patch('thefuck.settings.exception') as exception_mock:
        settings.init(args)

# Generated at 2022-06-14 08:32:50.527672
# Unit test for method init of class Settings
def test_Settings_init():
    # Args test
    settings_args = Settings({'require_confirmation': False, 'yes': False})
    settings_args.init(args=None)
    assert settings_args.require_confirmation == False

    settings_args.init(args=('-y',))
    assert settings_args.require_confirmation == True

    # Env test
    settings_env = Settings({})
    settings_env.init(args=None)
    assert settings_env.require_confirmation == True

    settings_env.init(args=None)
    assert settings_env.require_confirmation == True
    os.environ["THEFUCK_REQUIRE_CONFIRMATION"] = "False"
    settings_env.init(args=None)
    assert settings_env.require_confirmation == False

    settings_env.init

# Generated at 2022-06-14 08:32:58.830059
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception
    from mock import patch

    def fake_init(*args, **kwargs):
        pass

    with patch.object(Settings, '_init_settings_file', fake_init) as init:
        with patch.object(Settings, 'update') as update:
            settings.init()
            init.assert_called_once_with()
            assert init.return_value is None
            update.assert_called_once_with(settings._settings_from_file())
            update.return_value = False
            with patch.object(sys, 'exc_info') as exc_info:
                with patch.object(exception, 'assert_called_once_with') \
                        as assert_called_once_with:
                    settings.init()

# Generated at 2022-06-14 08:33:10.519989
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings(const.DEFAULT_SETTINGS)

    from mock import Mock, patch
    from .logs import exception

    with patch.object(settings, '_settings_from_env', return_value={'require_confirmation': True}):
        with patch.object(settings, '_settings_from_args', return_value={'require_confirmation': False}):
            with patch.object(settings, 'update'):
                settings.init()
                settings.update.assert_called_with({'require_confirmation': False})


# Generated at 2022-06-14 08:33:12.432332
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings['require_confirmation'] == True


# Generated at 2022-06-14 08:33:16.347018
# Unit test for method init of class Settings
def test_Settings_init():
    import sys
    sys.argv = ['thefuck']
    settings = Settings({'require_confirmation': True})
    settings.init()
    assert settings['require_confirmation'] == False



# Generated at 2022-06-14 08:33:28.261842
# Unit test for method init of class Settings
def test_Settings_init():
    """Run test for method init of class Settings"""
    from test.runner import run

    exp_user_dir = Path('~/.config/thefuck').expanduser()
    exp_settings_path = exp_user_dir.joinpath('settings.py')

# Generated at 2022-06-14 08:33:33.046310
# Unit test for method init of class Settings
def test_Settings_init():
    print(settings)
    settings.init()
    print(settings)
    print(settings.user_dir)
    print(settings['rules'])
    print(settings.rules)
    print(settings.exclude_rules)
    print(settings.priority)


# Generated at 2022-06-14 08:34:20.308375
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception
    from .system import Path
    from . import config

    res_settings = {}
    res_settings.update(const.DEFAULT_SETTINGS)

    def _init_settings_file():
        settings_path = Path('tests/settings_file')
        if not settings_path.is_file():
            with settings_path.open(mode='w') as settings_file:
                settings_file.write(const.SETTINGS_HEADER)
                for setting in const.DEFAULT_SETTINGS.items():
                    settings_file.write(u'# {} = {}\n'.format(*setting))
    
    def _settings_from_file():
        settings = load_source('settings', text_type('settings_file'))

# Generated at 2022-06-14 08:34:33.260835
# Unit test for method init of class Settings
def test_Settings_init():
    test_args = None
    test_env = None


# Generated at 2022-06-14 08:34:45.273427
# Unit test for method init of class Settings
def test_Settings_init():
    from mock import MagicMock

    settings.init()
    assert settings['require_confirmation'] == True
    assert settings['priority'] == const.DEFAULT_PRIORITY
    settings.init(MagicMock())
    assert settings['require_confirmation'] == True
    assert settings['priority'] == const.DEFAULT_PRIORITY

    settings.init(MagicMock(yes=True))
    assert settings['require_confirmation'] == False

    settings.init(MagicMock(debug=True))
    assert settings['debug'] == True
    settings.init(MagicMock())
    assert settings['debug'] == False

    settings.init(MagicMock(repeat=1))
    assert settings['repeat'] == 1
    settings.init(MagicMock())
    assert settings['repeat'] == 1



# Generated at 2022-06-14 08:34:54.507101
# Unit test for method init of class Settings
def test_Settings_init():
    from unittest.mock import patch

    from thefuck.rules import get_all_executables

    with patch.dict('os.environ', CLEAR='true',
                    REQUIRE_CONFIRMATION='false',
                    PRIORITY='fuck=5',
                    NO_COLORS='true',
                    SLOW_COMMANDS='python:man',
                    RULES='fuck',
                    EXCLUDE_RULES='test',
                    EXCLUDED_SEARCH_PATH_PREFIXES='/usr/bin',
                    WAIT_COMMAND=5,
                    WAIT_SLOW_COMMAND=1,
                    NUM_CLOSE_MATCHES=5,
                    HISTORY_LIMIT=100,
                    ALTER_HISTORY='true',
                    INSTANT_MODE='true'):
        args

# Generated at 2022-06-14 08:35:06.634394
# Unit test for method init of class Settings

# Generated at 2022-06-14 08:35:08.537852
# Unit test for method init of class Settings
def test_Settings_init():
    args = ['test']
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init(args)

# Generated at 2022-06-14 08:35:22.165138
# Unit test for method init of class Settings
def test_Settings_init():
    new_config_folder = tempfile.TemporaryDirectory().name
    os.environ['XDG_CONFIG_HOME'] = new_config_folder
    os.environ['THEFUCK_RULES'] = 'bash:fish:zsh:DEFAULT_RULES'
    os.environ['THEFUCK_PRIORITY'] = 'bash=10:fish=1:zsh=2'
    os.environ['THEFUCK_WAIT_COMMAND'] = '1'
    os.environ['THEFUCK_WAIT_SLOW_COMMAND'] = '2'
    os.environ['THEFUCK_HISTORY_LIMIT'] = '3000'
    os.environ['THEFUCK_EXCLUDE_RULES'] = 'bash:fish:zsh'
    os

# Generated at 2022-06-14 08:35:24.534475
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings({'a': 1, 'b': 2})
    settings.init()
    assert settings['a'] == 1
    assert settings['b'] == 2

# Generated at 2022-06-14 08:35:31.686906
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings.user_dir == Path(os.environ.get('XDG_CONFIG_HOME', '~/.config'), 'thefuck').expanduser()
    assert settings['history_limit'] == None
    assert settings['require_confirmation'] == True
    assert settings['no_colors'] == False

# Generated at 2022-06-14 08:35:41.204241
# Unit test for method init of class Settings
def test_Settings_init():
    args = type('', (object,), {'yes': True, 'debug': True, 'repeat': 2})
    settings._settings_from_env = lambda: {'require_confirmation': False,
                                           'exclude_rules': 'DEFAULT_RULES'}
    settings._settings_from_file = lambda: {'alter_history': False}
    settings.init(args)
    assert settings == {'require_confirmation': False,
                        'exclude_rules': 'DEFAULT_RULES',
                        'alter_history': False,
                        'debug': True,
                        'repeat': 2}


# Generated at 2022-06-14 08:36:28.576522
# Unit test for method init of class Settings
def test_Settings_init():
    # init
    settings.init()
    assert settings.user_dir.is_dir()
    assert settings.user_dir.joinpath('settings.py').is_file()

    # init when settings file is exist
    settings.init()
    assert settings.user_dir.is_dir()
    assert settings.user_dir.joinpath('settings.py').is_file()

    # init from env
    settings.init(args=object())
    assert settings.require_confirmation is False
    assert settings.debug is True
    assert settings.repeat is 3



# Generated at 2022-06-14 08:36:40.890699
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception

    class Error():
        def __init__(self):
            self.args = None

        def raise_exception(self, *args):
            self.args = args

    error = Error()
    exception = exception
    exception.side_effect = error.raise_exception

    class Args():
        pass

    settings.clear()
    assert settings == {}

    settings._setup_user_dir()

    settings.init()
    assert set(settings) == set(const.DEFAULT_SETTINGS)

    settings.init(Args())
    assert set(settings) == set(const.DEFAULT_SETTINGS)

# Generated at 2022-06-14 08:36:43.150385
# Unit test for method init of class Settings
def test_Settings_init():
    print(settings.init())
    print(settings.init(args=True))
    print(settings.init(args=False))

# Generated at 2022-06-14 08:36:52.654188
# Unit test for method init of class Settings
def test_Settings_init():
    from thefuck.types import Settings as SettingsData

    os.environ['THEFUCK_RULES'] = 'bash:python:zsh'
    os.environ['THEFUCK_PRIORITY'] = 'python=10'
    os.environ['THEFUCK_SUDO_COMMAND'] = 'sudo'
    os.environ['THEFUCK_WAIT_COMMAND'] = '0.5'
    os.environ['THEFUCK_HISTORY_LIMIT'] = '50'
    os.environ['THEFUCK_WAIT_SLOW_COMMAND'] = '1'
    os.environ['THEFUCK_NUM_CLOSE_MATCHES'] = '2'
    os.environ['THEFUCK_REQUIRE_CONFIRMATION'] = 'False'
    os

# Generated at 2022-06-14 08:37:05.824027
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import Logger
    logger = Logger()
    settings = Settings(const.DEFAULT_SETTINGS)
    settings._setup_user_dir()
    settings._init_settings_file()
    settings.init()
    assert settings['require_confirmation']
    assert settings['wait_command'] == 1
    assert settings['wait_slow_command'] == 3
    assert settings['no_colors'] == False
    assert settings['debug'] == False
    assert settings['alter_history'] == False
    assert settings['exclude_rules'] == ['git_push', 'sudo']
    assert settings['instant_mode'] == False
    assert settings['num_close_matches'] == 3
    assert settings['history_limit'] ==  10000

# Generated at 2022-06-14 08:37:12.186573
# Unit test for method init of class Settings
def test_Settings_init():
    test_args = namedtuple("args", "yes debug repeat")(
        yes=True, debug=True, repeat=True)

    settings.init(test_args)

    assert settings.get("require_confirmation") == False
    assert settings.get("debug") == True
    assert settings.get("repeat") == True
    assert settings.get("hist_file") == settings.user_dir.joinpath("history")

    settings.init()

    assert settings.get("require_confirmation") == True
    assert settings.get("debug") == False
    assert settings.get("repeat") == False



# Generated at 2022-06-14 08:37:24.813037
# Unit test for method init of class Settings

# Generated at 2022-06-14 08:37:38.966265
# Unit test for method init of class Settings
def test_Settings_init():
    # Emulate the effect of sys.argv
    args = []
    settings.init(args)
    assert(settings['require_confirmation'] == True)
    assert(settings['no_colors'] == False)
    assert(settings['debug'] == False)
    assert(settings['alter_history'] == True)
    # Check the effect of yes option
    args = ['thefuck', '--yes']
    settings.init(args)
    assert(settings['require_confirmation'] == False)
    # Check the effect of debug option
    args = ['thefuck', '--debug']
    settings.init(args)
    assert(settings['debug'] == True)
    # Check the effect of repeat option
    args = ['thefuck', '--repeat']
    settings.init(args)
    assert(settings['repeat'] == 1)

# Generated at 2022-06-14 08:37:49.717852
# Unit test for method init of class Settings
def test_Settings_init():
    import tempfile
    import shutil
    import os
    import sys
    import types

    temp_dir = tempfile.gettempdir()
    user_dir = os.path.join(temp_dir, 'thefuck')
    settings_path = os.path.join(user_dir, 'settings.py')
    os.mkdir(user_dir)
    with open(settings_path, 'w') as settings_file:
        settings_file.writelines(const.SETTINGS_HEADER)

# Generated at 2022-06-14 08:37:58.306786
# Unit test for method init of class Settings
def test_Settings_init():
    # imitate args
    args = ('TheFuck', 'git commit -am "test", args.repeat=2, args.yes=True')

    # clean attributes
    settings = Settings(const.DEFAULT_SETTINGS)
    user_dir = settings._get_user_dir_path()
    for root, dirs, files in os.walk(user_dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

    # imitate env
    os.environ['THEFUCK_WAIT_COMMAND'] = '999999999'

# Generated at 2022-06-14 08:39:21.143290
# Unit test for method init of class Settings
def test_Settings_init():
    def _get_args():
        class Args(object):
            def __init__(self):
                self.repeat = 1
                self.yes = True
                self.debug = True

        return Args()

    class Settings(object):
        def __init__(self):
            self.user_dir = '/abc/def'
            self.update = lambda x: print(x)
            self._settings_from_file = lambda: {'x': 3}
            self._settings_from_env = lambda: {'y': 4}
            self._settings_from_args = lambda x: {'z': 5}

    settings = Settings()
    settings.init(_get_args())
    assert settings.user_dir == '/abc/def'
    assert settings.get('x') == 3

# Generated at 2022-06-14 08:39:33.749553
# Unit test for method init of class Settings
def test_Settings_init():
    args = Mock()
    args.yes = False
    args.debug = False
    args.repeat = False
    args2 = Mock()
    args2.yes = True
    args2.debug = True
    args2.repeat = True
    real_init_settings_file = settings.init_settings_file
    real_settings_from_file = settings.settings_from_file
    real_settings_from_env = settings.settings_from_env
    real_settings_from_args = settings.settings_from_args
    settings.init_settings_file = Mock()
    settings.settings_from_file = Mock()
    settings.settings_from_env = Mock()
    settings.settings_from_args = Mock()

# Generated at 2022-06-14 08:39:46.686654
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings.rules == ['git_push', 'git_rebase', 'hg_update', 'sudo']
    assert settings.require_confirmation
    assert settings.alias == 'fuck'
    assert settings.wait_slow_command == 3
    assert settings.num_close_matches == 3
    assert settings.priority['git_push'] == 900
    assert settings.alter_history
    assert settings.exclude_rules == []
    assert settings.wait_command == 10
    assert settings.slow_commands == ['lein']
    assert settings.excluded_search_path_prefixes == ['/anaconda', '/usr/local/go']
    assert settings.no_colors
    assert settings.instant_mode
    assert settings.history_limit == 100
    assert settings.repeat == 1

# Generated at 2022-06-14 08:39:57.046212
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings()
    settings.init()
    assert settings.rules == const.DEFAULT_RULES
    assert settings.require_confirmation is True
    assert settings.no_colors is False
    assert settings.alter_history is True
    assert settings.wait_command is 10
    assert settings.wait_slow_command is 3
    assert settings.slow_commands == []
    assert settings.history_limit is 1000
    assert settings.exclude_rules == []
    assert settings.priority == {}
    assert settings.num_close_matches == 3
    assert settings.excluded_search_path_prefixes == []
    assert settings.instant_mode is False
    assert settings.repeat == 1

# Generated at 2022-06-14 08:40:07.608186
# Unit test for method init of class Settings
def test_Settings_init():
    import mock
    import os.path
    with mock.patch('thefuck.settings.Settings._setup_user_dir',
                    return_value='/home/fake/') as user_dir, \
         mock.patch('thefuck.settings.Settings._init_settings_file'), \
         mock.patch('thefuck.settings.os.path.expanduser',
                    return_value='/home/fake/') as expanduser, \
         mock.patch('thefuck.settings.load_source',
                    return_value=mock.Mock(foo='bar')), \
         mock.patch.dict('thefuck.settings.os.environ', {'FOO': 'bar'}):
        settings.init()

    assert settings == {'foo': 'bar'}
    user_dir.assert_called_with(settings)
   

# Generated at 2022-06-14 08:40:20.909702
# Unit test for method init of class Settings
def test_Settings_init():
    os.environ['THEFUCK_DEBUG'] = 'True'
    os.environ['THEFUCK_RULES'] = 'DEFAULT_RULES:';
    os.environ['thefuck_history_limit'] = '10'
    os.environ['thefuck_require_confirmation'] = 'False'
    os.environ['thefuck_wait_slow_command'] = '1'
    os.environ['thefuck_wait_command'] = '2'
    os.environ['thefuck_num_close_matches'] = '3'
    os.environ['thefuck_slow_commands'] = 'a:b'
    os.environ['thefuck_excluded_search_path_prefixes'] = 'c:d'

# Generated at 2022-06-14 08:40:33.294361
# Unit test for method init of class Settings
def test_Settings_init():
    # get settings from file
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.user_dir = '/tmp/.thefuck'
    settings._settings_from_file = lambda: {'priority': {'brew': 1}}
    settings._settings_from_env = lambda: {}
    settings._settings_from_args = lambda: {'require_confirmation': False}
    settings.init()
    assert settings.priority == {'brew': 1}
    # get settings from env
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.user_dir = '/tmp/.thefuck'
    settings._settings_from_file = lambda: {}
    settings._settings_from_env = lambda: {'priority': {'brew': 1}}

# Generated at 2022-06-14 08:40:35.376422
# Unit test for method init of class Settings
def test_Settings_init():
    path = '~/.cache'
    args = object()
    settings = Settings()
    settings.init(args)
    assert settings.user_dir.expanduser().as_posix() == path

# Generated at 2022-06-14 08:40:48.842420
# Unit test for method init of class Settings
def test_Settings_init():
    try:
        testing_settings = Settings(const.DEFAULT_SETTINGS)
        testing_settings.init()
        assert testing_settings is not None
    except Exception:
        assert False

    try:
        testing_settings = Settings(const.DEFAULT_SETTINGS)
        testing_settings._get_user_dir_path()
        assert testing_settings is not None
    except Exception:
        assert False

    try:
        testing_settings = Settings(const.DEFAULT_SETTINGS)
        testing_settings._settings_from_file()
        assert testing_settings is not None
    except Exception:
        assert False


# Generated at 2022-06-14 08:40:59.074006
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception

    settings.update(const.DEFAULT_SETTINGS)
    args = Mock()
    args.repeat = True
    args.yes = True
    args.debug = True
    settings_file = settings.user_dir.joinpath('settings.py')
    settings_file.write_lines(['rules = []', 'require_confirmation = False'])
    settings_file.write_lines(['rules = [DEFAULT_RULES]'])
    settings_file.write_lines(['priority = wrong_syntax'])
    os.environ['TF_REQUIRE_CONFIRMATION'] = 'TRUE'
    os.environ['TF_RULES'] = 'DEFAULT_RULES'
    os.environ['TF_PRIORITY'] = 'some_rule=1'

