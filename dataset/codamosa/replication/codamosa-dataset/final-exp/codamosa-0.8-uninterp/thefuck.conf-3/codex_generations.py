

# Generated at 2022-06-14 08:31:53.692856
# Unit test for method init of class Settings
def test_Settings_init():
    def init_settings():
        settings.__init__()
        settings.update(const.DEFAULT_SETTINGS)
        settings.init()

    try:
        from mock import patch
        with patch('os.environ.get', return_value='./tests/test_config'):
            # If user config directory not exist, Settings will create it
            init_settings()
            assert settings.user_dir.joinpath('settings.py').is_file()
    except ImportError:
        warn(u'Can\'t test `test_Settings_init` without mock')

# Generated at 2022-06-14 08:32:05.547471
# Unit test for method init of class Settings
def test_Settings_init():
    args = type('', (), {})
    # test init
    print('it will test method init of class Settings')
    settings.init()
    print(settings)
    print(settings['rules'])
    assert ('sudo_rule' in settings['rules'])
    assert ('pip_rule' in settings['rules'])
    assert ('npm_rule' in settings['rules'])
    print('test method init of class Settings successfully')

    # test update from args
    print('it will test method init with update from args of class Settings')
    settings.init(args)
    assert ('sudo_rule' not in settings['rules'])
    assert ('pip_rule' not in settings['rules'])
    assert ('npm_rule' not in settings['rules'])
    print('test method init with update from args of class Settings successfully')

# Generated at 2022-06-14 08:32:18.835995
# Unit test for method init of class Settings
def test_Settings_init():
    def _del_item_from_dict(dict_item, key):
        dict_item.pop(key)

    dict_settings = dict(const.DEFAULT_SETTINGS)
    dict_from_file = dict(settings._settings_from_file())
    dict_from_env = dict(settings._settings_from_env())
    dict_from_args = dict(settings._settings_from_args({"yes": True}))

    settings.init({"yes": True})

    # dict_from_args must be first in the settings dict

# Generated at 2022-06-14 08:32:26.582744
# Unit test for method init of class Settings
def test_Settings_init():
    args = lambda **kwargs: type(
        'Arg', (), {key: value for key, value in kwargs.items()})()

# Generated at 2022-06-14 08:32:30.841342
# Unit test for method init of class Settings
def test_Settings_init():
    test_settings = Settings(const.DEFAULT_SETTINGS)
    test_settings.init(argparse.Namespace(yes=True, debug=True, repeat=True))
    assert test_settings['require_confirmation'] == False
    assert test_settings['debug'] == True
    assert test_settings['repeat'] == True



# Generated at 2022-06-14 08:32:41.301147
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import capture_logs
    from .types import Settings as SettingsType
    from .main import get_aliases
    from .logs import print_command, print_error, print_exception

    settings.init(get_aliases())

    assert settings.alter_history
    assert settings.no_colors
    assert settings.wait_command == 0

    with capture_logs() as capus:
        settings.init()
        print_command('test')
        print_error('test')
        try:
            1/0
        except:
            print_exception()
        assert capus('print_command') == ''
        assert capus('print_error') == ''
        assert capus('print_exception') == ''



# Generated at 2022-06-14 08:32:44.505086
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception_logger

    try:
        settings.init()
    except Exception:
        exception_logger(sys.exc_info())
        return False

    return True

# Generated at 2022-06-14 08:32:56.267972
# Unit test for method init of class Settings
def test_Settings_init():
    args = lambda d: type('', (), d)()
    env = lambda d: type('', (), d)()

    # Test normal
    settings.init()
    assert settings == const.DEFAULT_SETTINGS
    for rule in settings['rules']:
        assert rule.startswith('.')

    # Test args
    settings.init(args=args({'yes': True, 'debug': True, 'repeat': 1}))
    assert not settings['require_confirmation']
    assert settings['debug'] == 1
    assert settings['repeat'] == 1
    assert settings['rules'] == const.DEFAULT_RULES

    # Test env
    os.environ['TF_REQUIRE_CONFIRMATION'] = 'False'
    os.environ['TF_DEBUG'] = '1'

# Generated at 2022-06-14 08:33:08.608036
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings()
    settings.init()
    assert isinstance(settings, Settings)
    assert isinstance(settings['rules'], list)
    assert isinstance(settings['exclude_rules'], list)
    assert isinstance(settings['priority'], dict)
    assert isinstance(settings['require_confirmation'], bool)
    assert isinstance(settings['wait_command'], int)
    assert isinstance(settings['no_colors'], bool)
    assert isinstance(settings['alter_history'], bool)
    assert isinstance(settings['history_limit'], int)
    assert isinstance(settings['slow_commands'], list)
    assert isinstance(settings['wait_slow_command'], int)
    assert isinstance(settings['excluded_search_path_prefixes'], list)
    assert isinstance

# Generated at 2022-06-14 08:33:17.677564
# Unit test for method init of class Settings
def test_Settings_init():
    import unittest
    import mock
    class TestSettingsInit(unittest.TestCase):
        def setUp(self):
            self.args = mock.Mock()
            self.s = Settings()

        def test_init_without_args(self):
            self.s.init()
            self.assertIsNotNone(self.s.user_dir)

        def test_init_with_args(self):
            self.args.debug = True
            self.args.yes = True
            self.args.repeat = 3
            self.s.init(self.args)
            self.assertEqual(self.s['debug'], True)
            self.assertEqual(self.s['require_confirmation'], False)
            self.assertEqual(self.s['repeat'], 3)


# Generated at 2022-06-14 08:33:44.055130
# Unit test for method init of class Settings

# Generated at 2022-06-14 08:33:47.014056
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings.wait_command == 1
    assert settings.get('command') is None



# Generated at 2022-06-14 08:34:00.072303
# Unit test for method init of class Settings
def test_Settings_init():
    default_settings = const.DEFAULT_SETTINGS
    env_to_attr = const.ENV_TO_ATTR

    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init('true')

    expected_settings = {}
    expected_settings.update(default_settings)
    expected_settings.update({'require_confirmation': False})
    assert settings == expected_settings

    settings.init('--no-colors')
    expected_settings.update({'require_confirmation': True})
    expected_settings.update({'no_colors': True})
    assert settings == expected_settings

    os.environ['THEFUCK_DEBUG'] = 'true'
    settings.init(args=None)
    expected_settings.update({'debug': True})
    assert settings == expected_settings

    os

# Generated at 2022-06-14 08:34:13.387609
# Unit test for method init of class Settings
def test_Settings_init():
    from mock import patch
    from .environ import env
    from .logs import exception

    old_settings = dict(settings)

    class _Args:
        yes = False
        debug = True


# Generated at 2022-06-14 08:34:21.477635
# Unit test for method init of class Settings
def test_Settings_init():
    # GIVEN
    class Options(object):
        debug=False
    
    old_user_dir = settings.user_dir
    old_settings_file = settings._init_settings_file
    old_settings_from_file = settings._settings_from_file

    options = Options()
    settings._init_settings_file = MagicMock()
    settings._settings_from_file = MagicMock(return_value={'require_confirmation': False})
    settings._settings_from_env = MagicMock()
    settings._settings_from_args = MagicMock(return_value={'debug': True})

    # WHEN
    settings.init(args=options)
    # THEN

    assert settings.user_dir == old_user_dir
    assert settings.debug == True
    assert settings.require_confirmation == False



# Generated at 2022-06-14 08:34:25.561926
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings()
    settings.init({'yes': False, 'debug': True, 'repeat': False})
    assert settings.require_confirmation
    assert settings.debug
    assert not settings.repeat



# Generated at 2022-06-14 08:34:36.980192
# Unit test for method init of class Settings
def test_Settings_init():
    """testing init the class of Settings
    """
    import os
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir))
    os.environ['XDG_CONFIG_HOME'] = path + '/tests'
    args = None
    settings.init(args)
    user_dir = settings._get_user_dir_path()
    assert user_dir == path + '/tests/thefuck'
    assert settings['repeat'] == False
    assert settings['debug'] == False
    assert settings['require_confirmation'] == True
    args = Namespace(yes=True, debug=True, repeat=None)
    settings.init(args)
    assert settings['repeat'] == False
    assert settings['debug'] == True

# Generated at 2022-06-14 08:34:48.037895
# Unit test for method init of class Settings
def test_Settings_init():
    import unittest
    import mock
    import os
    const.DEFAULT_SETTINGS["settings_path"]='test'
    const.DEFAULT_SETTINGS["user_dir"]='test'

    class Mock_Path:
        def __init__(self, color):
            self.color = color
        def __truediv__(self, item):
            return self
        def __str__(self):
            return self.color
        def is_dir(self):
            return True
        def is_file(self):
            return True
        def open(self, mode):
            return Mock_File()
        def joinpath(self, path):
            return Mock_Path(path)
        def expanduser(self):
            return Mock_Path('expanded')

# Generated at 2022-06-14 08:34:56.913124
# Unit test for method init of class Settings
def test_Settings_init():
    import os
    from .logs import patch_logger

    if os.path.exists('/tmp/thefuck'):
        # FIXME: If previous test failed, the directory exists
        # and the permissions should be fixed.
        os.chmod('/tmp/thefuck', 0o700)
        os.removedirs('/tmp/thefuck')
    assert not os.path.exists('/tmp/thefuck')

    with patch_logger('thefuck.settings') as mock_logger:
        settings.init()
        assert os.path.exists('/tmp/thefuck')
        assert os.path.exists('/tmp/thefuck/settings.py')
        assert mock_logger.exception.call_args_list == []

# Generated at 2022-06-14 08:35:08.786458
# Unit test for method init of class Settings
def test_Settings_init():
    import os
    import tempfile
    import shutil
    import unittest

    class SettingsInitTestCase(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.tempdir = tempfile.mkdtemp()
            os.environ['THEFUCK_RULES'] = 'bash:fish:python'
            os.environ['THEFUCK_PRIORITY'] = 'bash=10:fish=20'
            os.environ['THEFUCK_EXCLUDE_RULES'] = 'bash:fish:python'
            os.environ['THEFUCK_WAIT_COMMAND'] = '3'
            os.environ['THEFUCK_HISTORY_LIMIT'] = '5'

# Generated at 2022-06-14 08:35:38.306579
# Unit test for method init of class Settings
def test_Settings_init():
    import mock
    import __main__
    from .logs import LOG
    from .logs import LOG_LEVEL
    from .logs import LOG_FORMAT
    from test.fixtures import reset_settings
    with mock.patch.dict('__main__.__dict__', {'args': None}):
        reset_settings()
        settings.init()
        assert settings.user_dir == '~/.config/thefuck'
        assert settings.alter_history is True
        assert settings.confirm_loud is False
        assert settings.history_limit == None
        assert settings.no_colors is False
        assert settings.require_confirmation is True

# Generated at 2022-06-14 08:35:49.278294
# Unit test for method init of class Settings
def test_Settings_init():

    settings = Settings()
    assert hasattr(settings, 'user_dir')
    assert settings.user_dir.is_dir()
    assert settings.user_dir.joinpath('rules').is_dir()
    assert settings.user_dir.joinpath('settings.py').is_file()
    assert settings.require_confirmation
    assert not settings.no_colors
    assert settings.rules == const.DEFAULT_RULES
    assert settings.exclude_rules == []
    assert settings.priority == {}
    assert settings.wait_command == 1
    assert settings.history_limit == 1000
    assert settings.wait_slow_command == 15
    assert settings.slow_commands == ['lein', 'gradle', 'rebake', 'make']
    assert settings.excluded_search_path_prefixes == ['.']

# Generated at 2022-06-14 08:35:59.780078
# Unit test for method init of class Settings
def test_Settings_init():
    """
    Test for _settings_from_env function in Settings class

    """
    import os
    import sys
    import shutil
    from .system import get_all_executables

    def test_env_rules(env_rules, expected_rules):
        """
        testing env rules -> python rules
        :param env_rules: env_rules
        :param expected_rules: python rules
        :return: None
        """
        settings.init()
        settings_from_args = settings._settings_from_env()
        os.environ['THEFUCK_RULES'] = env_rules

        assert(settings._val_from_env('THEFUCK_RULES', 'rules') == expected_rules)


# Generated at 2022-06-14 08:36:01.730870
# Unit test for method init of class Settings
def test_Settings_init():
    global settings
    settings.init()
    assert settings.user_dir == settings._get_user_dir_path()



# Generated at 2022-06-14 08:36:14.466490
# Unit test for method init of class Settings
def test_Settings_init():
    import mock
    import os

    test_args = mock.Mock()
    test_args.yes = True
    test_args.debug = True
    test_args.repeat = 1


# Generated at 2022-06-14 08:36:21.051045
# Unit test for method init of class Settings
def test_Settings_init():
    from .system import is_mac, is_windows
    from .logs import exception
    def get_output(src):
        class Dummy:
            def __init__(self, src):
                self.src = src
            def __str__(self):
                return self.src
        return Dummy(src)

    with Path(Path.cwd(), 'temp_settings.py').open(mode='w+') as f:
        f.write(const.SETTINGS_HEADER+'rules = [\'ls\']\n')
        f.close()
        
        settings_path = settings._get_user_dir_path()
        settings.user_dir = settings_path
        settings._setup_user_dir()

        class Args:
            def __init__(self, src):
                self.src = src


# Generated at 2022-06-14 08:36:33.749948
# Unit test for method init of class Settings
def test_Settings_init():
    args = Mock(yes=False, debug=False, repeat=False)
    settings.update({'require_confirmation': True, 'debug': False, 'repeat': False})
    settings.init(args)
    assert_equal(settings['require_confirmation'], False)
    assert_equal(settings['debug'], False)
    assert_equal(settings['repeat'], False)

    settings.update({'require_confirmation': True})
    args = Mock(yes=True, debug=False, repeat=False)
    settings.init(args)
    assert_equal(settings['require_confirmation'], False)

    settings.update({'debug': False})
    args = Mock(yes=False, debug=True, repeat=False)
    settings.init(args)
    assert_equal(settings['debug'], True)

   

# Generated at 2022-06-14 08:36:35.699982
# Unit test for method init of class Settings
def test_Settings_init():
    settings.clear()
    settings.init()
    assert settings == const.DEFAULT_SETTINGS
    assert settings.user_dir

# Generated at 2022-06-14 08:36:46.375809
# Unit test for method init of class Settings
def test_Settings_init():
    above = {'priority': {'fuck': 1, 'python': 3},
             'exclude_rules': ['python'],
             'alter_history': True,
             'require_confirmation': True,
             'no_colors': True,
             'dev': True,
             'wait_command': 1,
             'history_limit': 1,
             'rules': ['fuck'],
             'wait_slow_command': 1,
             'excluded_search_path_prefixes': ['fuck'],
             'num_close_matches': 1,
             'slow_commands': ['fuck'],
             'debug': True,
             'repeat': 1}

    # _init_settings_file
    settings.user_dir = Path('~/.thefuck').expanduser()
    settings._init_settings_file()

   

# Generated at 2022-06-14 08:36:54.407188
# Unit test for method init of class Settings
def test_Settings_init():
    """Test Settings class init method."""
    import argparse

    def parse_args(*args, **kwargs):
        parser = argparse.ArgumentParser()
        parser.add_argument('--debug', action='store_true',
                            help=('Show debug information. '
                                  'By default only errors are shown.'))
        parser.add_argument('-y', '--yes', action='store_true',
                            help=('Don\'t prompt for confirmation. '
                                  'Just fix it.'))
        parser.add_argument('-r', '--repeat', default=1, type=int,
                            help=('Repeat n times.'))
        return parser.parse_args()

    settings.init(parse_args([]))
    assert settings == Settings(const.DEFAULT_SETTINGS)


# Generated at 2022-06-14 08:37:36.554108
# Unit test for method init of class Settings
def test_Settings_init():
    # When env is empty and args are None
    # it should return default values
    init_settings = Settings(const.DEFAULT_SETTINGS).init()
    assert init_settings == const.DEFAULT_SETTINGS
    # When env is specified and args are None
    # it should return the combination of default and env values
    init_settings_from_env = Settings(const.DEFAULT_SETTINGS).init()
    assert init_settings_from_env == const.DEFAULT_SETTINGS
    # When env is empty and args are not None
    # it should return the combination of default and args values
    init_settings_from_args = Settings(const.DEFAULT_SETTINGS).init()
    assert init_settings_from_args == const.DEFAULT_SETTINGS
    # When env is specified and args are not None
   

# Generated at 2022-06-14 08:37:47.722035
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings.user_dir.match('~/.config/thefuck/')
    assert settings.confirmation_timeout == 3
    assert settings.require_confirmation
    assert settings.rules == const.DEFAULT_RULES
    assert settings.exclude_rules == []
    assert settings.priority == {}
    assert settings.history_limit == 100
    assert settings.wait_command == 3
    assert settings.slow_commands == []
    assert settings.wait_slow_command == 10
    assert settings.no_colors is False
    assert settings.debug is False
    assert settings.alter_history is False
    assert settings.instant_mode is False
    assert settings.num_close_matches == 3
    assert settings.excluded_search_path_prefixes == []


# Generated at 2022-06-14 08:37:57.818521
# Unit test for method init of class Settings
def test_Settings_init():
    """
    Test method init of class Settings
    """
    # Run init()
    settings.init()

    # Asserts
    # Assert user_dir is created.
    assert settings.user_dir.is_dir()

    locale_path = settings.user_dir.joinpath('locales')
    assert locale_path.is_dir()

    # Assert settings.py is created
    settings_path = settings.user_dir.joinpath('settings.py')
    assert settings_path.is_file()

    # Assert settings.py can be loaded
    settings_file = load_source('settings', text_type(settings_path))
    assert hasattr(settings_file, 'no_colors')
    assert hasattr(settings_file, 'debug')

# Generated at 2022-06-14 08:37:59.344198
# Unit test for method init of class Settings
def test_Settings_init():
    t_settings = Settings()
    t_settings.init()
    assert(t_settings.user_dir)

# Generated at 2022-06-14 08:38:07.331236
# Unit test for method init of class Settings
def test_Settings_init():
    class DummySettings(object):
        def __init__(self, settings):
            self.settings = settings

        def _init_settings_file(self):
            pass

        def _get_user_dir_path(self):
            return Path('~', '.thefuck').expanduser()

        def _setup_user_dir(self):
            self.settings.user_dir = Path('~', '.thefuck').expanduser()

        def _settings_from_file(self):
            return {'require_confirmation': False,
                    'rules': ['brew', 'sudo']}

        def _rules_from_env(self, val):
            return val

        def _priority_from_env(self, val):
            for part in val.split(':'):
                rule, priority = part.split('=')
                yield

# Generated at 2022-06-14 08:38:15.122251
# Unit test for method init of class Settings
def test_Settings_init():
    # Given
    settings._setup_user_dir = lambda: settings.user_dir == '/home/user/.thefuck'

    settings._settings_from_file = lambda: {'priority': {'cd': 1}}
    settings._settings_from_env = lambda: {'priority': {'ls': 2}}
    settings._settings_from_args = lambda args: {}
    settings.init()

    # Then
    assert settings['priority'] == {'cd': 1, 'ls': 2}


# Generated at 2022-06-14 08:38:28.239905
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception, log
    from .system import Path

    class args:
        yes = True
        debug = True
        repeat = 2

    mock_os = {}

# Generated at 2022-06-14 08:38:38.083826
# Unit test for method init of class Settings
def test_Settings_init():
    import tempfile
    temp_dir = tempfile.TemporaryDirectory()
    settings.user_dir = Path(temp_dir.name)
    settings.init()

    assert settings.user_dir.joinpath('rules').is_dir()
    assert settings.user_dir.joinpath('settings.py').is_file()

    with settings.user_dir.joinpath('settings.py').open(mode='r') as fp:
        assert fp.read() == const.SETTINGS_HEADER
        fp.seek(0)
        for line in fp:
            if line.startswith('# '):
                setting = tuple(line[2:].strip().split(' = '))
                assert const.DEFAULT_SETTINGS[setting[0]] == eval(setting[1])

# Generated at 2022-06-14 08:38:42.851027
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings['rules'] == const.DEFAULT_RULES
    assert settings['aliases'] == const.DEFAULT_ALIASES
    assert 'user_dir' in settings
    assert settings['history_limit'] == const.DEFAULT_HISTORY_LIMIT
    assert settings['require_confirmation'] == const.DEFAULT_REQUIRE_CONFIRMATION
    assert settings['no_colors'] == const.DEFAULT_NO_COLORS
    assert settings['wait_command'] == const.DEFAULT_WAIT_COMMAND

# Generated at 2022-06-14 08:38:50.948996
# Unit test for method init of class Settings
def test_Settings_init():
    import environ  # pip install django-environ
    from thefuck.settings import Settings
    from thefuck.logs import log
    environ.Env.read_env()
    mySettings = Settings('/tmp')
    mySettings.init()
    assert len(mySettings) > 0
    mySettings = Settings('/tmp')
    mySettings._setup_user_dir()
    mySettings.init()
    assert len(mySettings) > 0
    mySettings = Settings()
    mySettings._setup_user_dir = lambda : None
    mySettings._get_user_dir_path = lambda : ''
    mySettings.init()
    assert len(mySettings) > 0


# Generated at 2022-06-14 08:40:10.356777
# Unit test for method init of class Settings
def test_Settings_init():
    # Example:
    #   $ env FOO='BAR' env THEFUCK_BAR='FOO' \
    #   > THEFUCK_PRIORITY='foo=42:bar=24' thefuck
    #   > --yes --repeat=3 --debug
    import argparse
    from .test_utils import Mock, Call

    args = argparse.Namespace(yes=True, repeat=3, debug=True)


# Generated at 2022-06-14 08:40:20.031628
# Unit test for method init of class Settings
def test_Settings_init():
    from mock import patch

    class Args(object):
        def __init__(self, yes, debug, repeat):
            self.yes = yes
            self.debug = debug
            self.repeat = repeat

    with patch('thefuck.settings._settings_from_file', return_value={'key': 'file'}), \
            patch('thefuck.settings._settings_from_env', return_value={'key': 'env'}), \
            patch('thefuck.settings._settings_from_args', return_value={'key': 'args'}):
        settings.init(Args(yes=True, debug=True, repeat=True))
        assert settings == {'key': 'args'}

        settings.init(Args(yes=False, debug=False, repeat=False))
        assert settings == {'key': 'env'}

# Generated at 2022-06-14 08:40:31.444862
# Unit test for method init of class Settings
def test_Settings_init():
    import sys
    import os
    from .logs import exception
    from .system import Path
    from . import const
    from . import config
    from . import settings
    from . import manager
    from . import logs
    from . import utils
    # Test exception when init method of settings class can't load settings from file
    setattr(settings, 'user_dir', Path("~/.config/thefuck").expanduser())
    setattr(settings, '_init_settings_file', lambda : None)
    update_called_count = 0
    def _update_settings_from_file():
        nonlocal update_called_count
        update_called_count += 1
        raise Exception("can't load settings from file")
    setattr(settings, '_update_settings_from_file', _update_settings_from_file)
   

# Generated at 2022-06-14 08:40:36.711263
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init(args=None)
    assert settings['require_confirmation'] == const.DEFAULT_SETTINGS['require_confirmation']
    assert settings['require_confirmation'] == False
    assert settings['repeat'] == const.DEFAULT_SETTINGS['repeat']
    assert settings['repeat'] == False
    settings.init(args=Namespace(yes=True, repeat=True))
    assert settings['require_confirmation'] == True
    assert settings['repeat'] == True

# Generated at 2022-06-14 08:40:38.274230
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings.user_dir.is_dir()

# Generated at 2022-06-14 08:40:45.058328
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init(args=None)
    assert settings['rules'] == [
        'cd_parent', 'git_push', 'git_commit', 'man', 'brew_install',
        'npm_install', 'pip_install', 'ruby_install', 'vagrant', 'brew_cask_install',
        'archlinux_install', 'grep']
    assert settings['history_limit'] == 100
    assert settings['require_confirmation'] == False
    assert settings['no_colors'] == False
    assert settings['instant_mode'] == False
    assert settings['debug'] == False
    assert settings['prioirty'] == {}
    assert settings['slow_commands'] == ['git']
    assert settings['excluded_search_path_prefixes'] == ['/usr']

# Generated at 2022-06-14 08:40:57.004075
# Unit test for method init of class Settings
def test_Settings_init():
    from .utils import get_all_settings_from_file
    from .utils import get_all_settings_from_env

    def _check_for_settings_default_settings(settings):
        for key in const.DEFAULT_SETTINGS.keys():
            assert settings.get(key) == const.DEFAULT_SETTINGS[key]

    def _check_for_settings_from_file():
        orig_settings = get_all_settings_from_file()
        settings.init()
        for key in orig_settings.keys():
            assert settings.get(key) == orig_settings[key]

    def _check_for_settings_from_env():
        orig_settings = get_all_settings_from_env()
        settings.init()

# Generated at 2022-06-14 08:41:02.646982
# Unit test for method init of class Settings
def test_Settings_init():
    settings.update(const.DEFAULT_SETTINGS)
    settings.init()
    if (settings.user_dir == '~/.thefuck' and
          settings.require_confirmation == False and
          settings.repeat == False and
          settings.wait_command == 1 and
          settings.debug == False):
        return True
    else:
        return False

# Generated at 2022-06-14 08:41:13.837370
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings()
    test_args = type('TestArgs', (object,), {'yes': True})
    settings.init(test_args)
    assert settings['require_confirmation'] == False
    test_args.yes = False
    settings.init(test_args)
    assert settings['require_confirmation'] == True
    test_args.repeat = 10
    settings.init(test_args)
    assert settings['repeat'] == 10
    test_args.debug = True
    settings.init(test_args)
    assert settings['debug'] == True
    settings['debug'] = False
    settings['repeat'] = 3
    settings['require_confirmation'] = True
    settings.init()
    assert settings['debug'] == False
    assert settings['repeat'] == 3
    assert settings['require_confirmation'] == True

# Generated at 2022-06-14 08:41:19.954000
# Unit test for method init of class Settings
def test_Settings_init():
    from mock import mock_open, patch

    with patch('thefuck.settings.sys.exc_info', return_value=('exc', 'val', 'tb')), \
            patch('thefuck.settings.load_source', side_effect=Exception('Boom!')), \
            patch('thefuck.settings.os.environ', {'XDG_CONFIG_HOME': '~/dir', 'LOL': 'KEK'}), \
            patch('thefuck.settings.Path.mkdir', return_value=None), \
            patch('thefuck.settings.Path.expanduser', return_value=Path('/home/user')), \
            patch('thefuck.settings.warn', return_value=None):
        from thefuck.settings import settings
        settings.init()