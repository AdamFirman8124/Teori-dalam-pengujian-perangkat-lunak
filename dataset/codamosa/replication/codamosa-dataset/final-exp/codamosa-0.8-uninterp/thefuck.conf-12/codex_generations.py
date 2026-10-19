

# Generated at 2022-06-14 08:31:54.543298
# Unit test for method init of class Settings
def test_Settings_init():
    import tempfile
    from .tests.utils import support_dir, set_os_environ

    rules = u'ls\nsudo\nfck'
    os_environ = {
        'THEFUCK_RULES': rules,
        'THEFUCK_CONFIRM': 'false',
        'THEFUCK_PRIORITY': 'sudo=666\nls=666'
    }
    with tempfile.TemporaryDirectory() as home_dir:
        settings_file = Path(home_dir) / 'settings.py'
        with set_os_environ(os_environ, home_dir):
            settings.init()
    assert settings.rules == const.DEFAULT_RULES + rules.split('\n')
    assert settings.require_confirmation is False

# Generated at 2022-06-14 08:32:06.012421
# Unit test for method init of class Settings
def test_Settings_init():
    from thefuck.types import Settings
    from thefuck.utils import wrap_settings
    settings = Settings()
    settings.init()
    settings = wrap_settings(settings)
    assert settings.debug == False
    title = "settings.py"

# Generated at 2022-06-14 08:32:07.617737
# Unit test for method init of class Settings
def test_Settings_init():
    assert settings.init() == None

# Generated at 2022-06-14 08:32:20.677296
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import _settings_from_env, _rules_from_env, _priority_from_env, _val_from_env

    const.DEFAULT_SETTINGS['settings_file'] = 'settings_file.py'
    const.DEFAULT_SETTINGS['user_dir'] = 'user_dir'

    mock_user_dir = Mock()
    mock_user_dir.joinpath = lambda path: path

    const.ENV_TO_ATTR['TF_RULES'] = 'rules'
    const.ENV_TO_ATTR['TF_PRIORITY'] = 'priority'
    const.ENV_TO_ATTR['TF_REQUIRE_CONFIRMATION'] = 'require_confirmation'

# Generated at 2022-06-14 08:32:23.691195
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init({'yes': True, 'repeat': 2})
    from .system import is_debug
    assert settings.require_confirmation is False
    assert settings.debug is False
    assert settings.history_limit is 3
    assert settings.repeat is 2
    assert is_debug() is False

# Generated at 2022-06-14 08:32:32.422557
# Unit test for method init of class Settings
def test_Settings_init():
    class Args():
        def __init__(self, debug=False, yes=False, repeat=None):
            self.debug = debug
            self.yes = yes
            self.repeat = repeat
    # test the method _settings_from_args
    assert settings._settings_from_args(Args(debug=True)) == {'debug':True}
    assert settings._settings_from_args(Args(yes=True)) == {'require_confirmation':False}
    assert settings._settings_from_args(Args(repeat='cat')) == {'repeat': 'cat'}
    # test the method _settings_from_env
    os.environ.update({'TF_POPEN_TIMEOUT': '10', 'TF_RULES': ':DEFAULT_RULES:ls'})
    assert settings._settings_from_

# Generated at 2022-06-14 08:32:36.186076
# Unit test for method init of class Settings
def test_Settings_init():
    assert settings.init({'yes': True}) == {'require_confirmation': False}
    assert settings.init({'debug': True}) == {'debug': True}
    assert settings.init({'repeat': 1}) == {'repeat': 1}


# Generated at 2022-06-14 08:32:41.986249
# Unit test for method init of class Settings
def test_Settings_init():
    _settings = Settings(const.DEFAULT_SETTINGS)
    args = lambda x: lambda: x
    class args:
        pass
    args.yes = False
    args.no_colors = True
    args.repeat = 2
    args.debug = False
    _settings.init(args)
    assert not _settings['require_confirmation']
    assert _settings['no_colors']
    assert _settings['repeat'] == 2
    assert not _settings['debug']

settings.init()

# Generated at 2022-06-14 08:32:53.500697
# Unit test for method init of class Settings
def test_Settings_init():
    # Unit test for method init of class Settings
    from unittest.mock import patch
    path = 'thefuck.settings.Settings'
    with patch(path + '._settings_from_env') as get_settings_from_env, \
        patch(path + '._settings_from_file') as get_settings_from_file, \
        patch(path + '._settings_from_args') as get_settings_from_args:
        get_settings_from_env.return_value = {'key_env': 'val_env'}
        get_settings_from_file.return_value = {'key_file': 'val_file'}
        get_settings_from_args.return_value = {'key_args': 'val_args'}

        settings.init(args={})

# Generated at 2022-06-14 08:32:59.664177
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()

    assert settings.user_dir.is_dir()
    assert settings.user_dir.joinpath('rules').is_dir()

    # settings.py should be created
    assert settings.user_dir.joinpath('settings.py').is_file()
    # Load settings from default settings.py
    assert settings.require_confirmation is False
    assert settings.no_colors is False
    assert settings.priority == {}
    assert settings.history_limit == 9
    assert settings.wait_command == 1
    assert settings.wait_slow_command == 15
    assert settings.env.__class__ is dict
    assert settings.rules == ['git_add_command', 'git_push_command']

# Generated at 2022-06-14 08:33:26.542223
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings.get('require_confirmation') is True
    assert settings.get('wait_command') == 3
    assert settings.get('debug') is False
    assert settings.get('repeat') is False

    settings.init(args=type('Foo', (), {'yes': True, 'debug': True, 'repeat': 1}))
    assert settings.get('require_confirmation') is False
    assert settings.get('debug') is True
    assert settings.get('repeat') == 1


# Generated at 2022-06-14 08:33:27.989715
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init(args=None)
    assert settings.user_dir == Path('~/.thefuck').expanduser()

# Generated at 2022-06-14 08:33:40.778217
# Unit test for method init of class Settings
def test_Settings_init():
    settings_init = Settings({"rules": [], "require_confirmation": True, "no_colors": False, "priority": {}})
    user_dir_path = settings_init._get_user_dir_path()
    settings_init._setup_user_dir()
    settings_init._init_settings_file()
    settings_init._settings_from_file()
    settings_init._settings_from_env()
    args = None
    settings_init._settings_from_args(args)
    assert settings_init.user_dir == user_dir_path
    assert settings_init.user_dir.joinpath('settings.py').is_file()
    assert settings_init.get("rules") == []
    assert settings_init.get("require_confirmation") is True

# Generated at 2022-06-14 08:33:44.031093
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings['rules'] == const.DEFAULT_RULES
    assert settings['confirm_exit'] == True

# Generated at 2022-06-14 08:33:46.421594
# Unit test for method init of class Settings
def test_Settings_init():
    return settings.init()

# Unit test method _get_user_dir_path of class Settings

# Generated at 2022-06-14 08:33:59.593152
# Unit test for method init of class Settings
def test_Settings_init():
    class Assert:
        def __init__(self, target):
            self.target = target
        def __eq__(self, other):
            assert self.target == other
            return True

    args = type('FakeArgsNamespace', (object,), {'yes': True})
    fake_env = {'TF_INSTANT_MODE': 'False', 'TF_RULES': '',
                'TF_PRIORITY': 'p:p=10',
                'TF_EXCLUDED_SEARCH_PATH_PREFIXES': '/a:/b'}
    with mock.patch.object(Settings, '_get_user_dir_path') as mock_get_user_dir_path:
        mock_get_user_dir_path.return_value = ''

# Generated at 2022-06-14 08:34:10.663824
# Unit test for method init of class Settings
def test_Settings_init():
    """
    Test for init method of class Settings.
    Args: None
    Returns: None
    """
    from .logs import exception

    from .logs import stderr
    from .logs import test_logs
    def test_stderr(message, *args, **kwargs):
        stderr(message, *args, **kwargs)
        test_logs.append(message)

    test_logs = []
    test_settings_path = '/tmp/test_settings'
    test_settings_dir = os.path.dirname(test_settings_path)
    test_args = type('', (object,), {'yes': True, 'debug': True, 'repeat': True})()

    test_settings = Settings(const.DEFAULT_SETTINGS)
    test_settings._get_user

# Generated at 2022-06-14 08:34:21.884099
# Unit test for method init of class Settings
def test_Settings_init():
    from mock import patch

    from thefuck.shells.bash import Bash

    with patch('thefuck.settings.load_source') as load_source, \
            patch('thefuck.settings.os.environ.get') as get, \
            patch('thefuck.settings.Settings._settings_from_args') as _settings_from_args, \
            patch('thefuck.settings.Settings._rules_from_env') as _rules_from_env, \
            patch('thefuck.settings.Settings._priority_from_env') as _priority_from_env:
        settings.init(Bash('cd'))

        load_source.assert_called_once_with(
            'settings',
            u'~/.config/thefuck/settings.py'
        )


# Generated at 2022-06-14 08:34:34.005929
# Unit test for method init of class Settings
def test_Settings_init():
    from unittest.mock import patch, Mock

    settings.init(args=Mock())

    assert os.path.exists(settings.user_dir), "User dir doesn't exist"
    assert os.path.exists(settings.user_dir.joinpath('rules')), "Rules dir doesn't exist"
    assert os.path.exists(settings.user_dir.joinpath('settings.py')),\
           "Settings file doesn't exist"


# Generated at 2022-06-14 08:34:48.124911
# Unit test for method init of class Settings
def test_Settings_init():

    _environ = os.environ

# Generated at 2022-06-14 08:35:38.089931
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings(const.DEFAULT_SETTINGS)
    settings._setup_user_dir = lambda: 1
    settings._init_settings_file = lambda: 1
    settings._settings_from_file = lambda: 1
    settings._settings_from_env = lambda: 1
    settings._settings_from_args = lambda: 1
    settings.init()
    assert settings['rules'] == [
        '<command> && sudo !!',
        'git commit && git push',
        'git checkout <file>',
        '(ssh|vagrant) <command>',
        'sudo <command>']

# Generated at 2022-06-14 08:35:42.160171
# Unit test for method init of class Settings
def test_Settings_init():
    # Test if settings sets up pythonpath
    assert sys.path[0] == str(settings.user_dir)
    assert settings.user_dir == settings._get_user_dir_path()


# Generated at 2022-06-14 08:35:47.083441
# Unit test for method init of class Settings
def test_Settings_init():
    class Args(object):
        yes = False
        repeat = None
        debug = False

    settings.init(Args())

    assert settings.require_confirmation == True
    assert settings.debug == False
    assert settings.repeat is None

# Generated at 2022-06-14 08:36:00.415374
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import clear_logger

    settings_path = settings._get_user_dir_path()

# Generated at 2022-06-14 08:36:08.235040
# Unit test for method init of class Settings
def test_Settings_init():
    new_settings = Settings(const.DEFAULT_SETTINGS)
    new_settings.init()
    assert new_settings.user_dir.is_dir()
    assert new_settings.user_dir.joinpath('settings.py').is_file()
    assert 'settings.py' in os.listdir(new_settings.user_dir)
    assert len(new_settings) == len(const.DEFAULT_SETTINGS)

# Generated at 2022-06-14 08:36:12.732745
# Unit test for method init of class Settings
def test_Settings_init():
    assert settings.user_dir == Path('~/.config/thefuck').expanduser()

    try:
        settings.init(args=False)
        settings.init(args=True)
    except Exception:
        assert False


# Generated at 2022-06-14 08:36:15.457779
# Unit test for method init of class Settings
def test_Settings_init():
    test_settings = Settings(const.DEFAULT_SETTINGS)
    test_settings.init()
    assert test_settings['alter_history']

# Generated at 2022-06-14 08:36:29.450302
# Unit test for method init of class Settings
def test_Settings_init():
    def test_init(settings):
        settings.init()
        assert settings.rules
        assert settings.require_confirmation

    settings.init(object())
    assert settings.debug
    assert settings.repeat

    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()
    assert not settings.debug
    assert not settings.repeat

    settings = Settings(const.DEFAULT_SETTINGS)
    settings['debug'] = True
    settings['repeat'] = 0
    test_init(settings)
    assert settings.debug
    assert settings.repeat

    settings = Settings(const.DEFAULT_SETTINGS)
    settings['debug'] = True
    settings['repeat'] = 1
    settings['no_colors'] = True
    test_init(settings)
    assert settings.debug
    assert settings.repeat
   

# Generated at 2022-06-14 08:36:34.047908
# Unit test for method init of class Settings
def test_Settings_init():
    # is_file() will not return True because we don't have the test file
    assert settings._init_settings_file() == None
    # check if the class Settings returns User_dir or Not
    assert settings._setup_user_dir() == '.config/thefuck'
    # check if the user config dir can be returned or Not
    assert settings._get_user_dir_path() == '~/.config/thefuck'
    # check if the user config dir contains the file settings.py or Not
    assert settings._settings_from_file() == load_source(
        'settings', text_type(settings.user_dir.joinpath('settings.py')))
    # check if it is the correct environment variable for rules

# Generated at 2022-06-14 08:36:45.129906
# Unit test for method init of class Settings
def test_Settings_init():
    def test_Settings_init_fail():
        class ErrorInSettings(object):
            def __getattr__(self, item):
                raise Exception("Incorrect settings")
        fail_settings = ErrorInSettings()
        fail_settings.init()

    assert 'user_dir' not in settings
    assert 'require_confirmation' not in settings
    assert 'no_colors' not in settings
    assert 'priority' not in settings

    settings.init()
    assert settings.user_dir
    assert settings.require_confirmation
    assert settings.no_colors
    assert settings.priority

    os.environ['THEFUCK_REQUIRE_CONFIRMATION'] = 'false'
    os.environ['THEFUCK_NO_COLORS'] = 'true'

# Generated at 2022-06-14 08:37:35.105863
# Unit test for method init of class Settings
def test_Settings_init():
    # Test settings.init() when no settings in file or env
    settings.init()
    assert settings == const.DEFAULT_SETTINGS
    assert settings.user_dir == Path(os.path.expanduser("~/.config/thefuck"))

    # Test settings.init() when there are settings in file and env
    settings.init()
    assert settings.user_dir == Path(os.path.expanduser("~/.config/thefuck"))



# Generated at 2022-06-14 08:37:46.321112
# Unit test for method init of class Settings
def test_Settings_init():
    args = lambda **kwargs: type('args', (object,), kwargs)()

    settings.init(args())
    assert settings.rules == const.DEFAULT_RULES
    assert settings.require_confirmation is True
    assert settings.wait_command is 0
    assert settings.priority == {}
    assert settings.no_colors is False
    assert settings.debug is False
    assert settings.exclude_rules == []
    assert settings.alter_history is True
    assert settings.wait_slow_command is 10
    assert settings.slow_commands == []
    assert settings.excluded_search_path_prefixes == []
    assert settings.priority == {}
    assert settings.instant_mode is False
    assert settings.repeat is False

    settings.init(args(yes=True))
    assert settings.require_conf

# Generated at 2022-06-14 08:37:57.071536
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception
    import sys
    import mock
    sys.modules.pop('thefuck.settings', None)

    settings.init()
    assert settings['debug'] == False
    
    with mock.patch('thefuck.settings.Settings._settings_from_file') as mock_settings_from_file, \
        mock.patch('thefuck.settings.Settings._settings_from_env') as mock_settings_from_env, \
        mock.patch('thefuck.settings.Settings._settings_from_args') as mock_settings_from_args, \
        mock.patch('thefuck.settings.exception') as mock_exception:

        mock_settings_from_file.return_value = {'debug': True}
        mock_settings_from_env.return_value = {'repeat': True}
        mock_

# Generated at 2022-06-14 08:38:11.232789
# Unit test for method init of class Settings
def test_Settings_init():
    # Add test path in order not to change original settings
    settings.user_dir = Path('/tmp')
    settings.user_dir.joinpath('settings.py').unlink_p()
    settings.init()

    # TODO: Check if settings.py was created

    settings.user_dir.joinpath('settings.py').write_text(
        "require_confirmation = True\n")
    settings.init()
    assert settings.require_confirmation

    settings.user_dir.joinpath('settings.py').write_text(
        "require_confirmation = False\n")
    settings.init()
    assert not settings.require_confirmation

    os.environ['THEFUCK_REQUIRE_CONFIRMATION'] = 'False'
    settings.init()
    assert not settings.require_confirmation

    settings

# Generated at 2022-06-14 08:38:18.697113
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()

    assert settings.user_dir == Path('~/.config/thefuck').expanduser()
    assert settings.rules == const.DEFAULT_RULES

    assert settings.command_format == '{script} {piped_command}', settings.command_format
    assert settings.clear_command_format == False
    assert settings.debug == False
    assert settings.require_confirmation == True
    assert settings.hist_file == Path('~/.config/thefuck/history').expanduser()
    assert settings.no_colors == False
    assert settings.repeat == False
    assert settings.wait_command == 0.8
    assert settings.wait_slow_command == 3
    assert settings.exclude_rules == []
    assert settings.history_limit == 200
    assert settings.alter_history == True

# Generated at 2022-06-14 08:38:22.480607
# Unit test for method init of class Settings
def test_Settings_init():
    reload(const)
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()
    assert settings.user_dir is not None
    assert settings.script_dir is not None

# Generated at 2022-06-14 08:38:34.657957
# Unit test for method init of class Settings
def test_Settings_init():
    """Test if _settings_from_env() function can import correct value from env variable THEFUCK_RULE_ENABLED and update
    key 'enable_rules' of dict Settings.
    """
    success = False
    old_env = os.environ.copy()
    try:
        os.environ['THEFUCK_REQUIRE_CONFIRMATION'] = 'True'
        # these lines below must be run before call settings.init()
        os.environ['THEFUCK_RULE_ENABLED'] = 'alter_history:no_colors'
        settings.init()
        success = settings.get('require_confirmation')
    finally:
        os.environ.clear()
        os.environ.update(old_env)
    assert success == True


# Generated at 2022-06-14 08:38:46.645602
# Unit test for method init of class Settings
def test_Settings_init():
    args = object
    args.yes = True
    args.repeat = False
    args.debug = False

    class FakeUserConfig:
        pass
    user_config = FakeUserConfig
    user_config.joinpath = lambda x: x
    user_config.isdir = lambda x: False
    user_config.open = lambda x, mode: x

    class FakeEnv:
        pass
    os.environ = FakeEnv()
    os.environ.__contains__ = lambda x: True
    os.environ.__getitem__ = lambda x: x

    settings.init(args)
    assert settings.repeat is False
    assert settings.require_confirmation is False
    assert settings.debug is False



# Generated at 2022-06-14 08:38:55.235043
# Unit test for method init of class Settings
def test_Settings_init():
    """
    Test method settings.init

    Not all possible combinations are tested. Just a few.
    """
    import sys
    # sys.modules['settings'] = None
    if 'settings' in sys.modules.keys():
        del sys.modules['settings']
    settings.init()

    settings._setup_user_dir()
    import shutil
    shutil.rmtree(settings.user_dir)
    settings._init_settings_file()

    settings.init()
    settings._init_settings_file()
    with (settings.user_dir.joinpath('settings.py').open('w')) as settings_file:
        settings_file.write('''
rules = ['echo_rules']
num_close_matches = 0
require_confirmation = False
wait_command = 5
''')
    settings.init

# Generated at 2022-06-14 08:39:01.770872
# Unit test for method init of class Settings
def test_Settings_init():
    import sys, os
    from thefuck.conf import settings

    _exit = sys.exit


# Generated at 2022-06-14 08:40:00.211381
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception
    import sys
    import os
    import tempfile
    from six import text_type

    def populate_env(settings_from_env):
        for env, attr in const.ENV_TO_ATTR.items():
            if attr in settings_from_env:
                os.environ[env] = settings_from_env[attr]
            else:
                os.environ.pop(env, None)

    def _test_settings_file(filename, settings_from_file):
        with tempfile.NamedTemporaryFile(mode='wt', suffix='.py',
                                         dir=text_type(settings.user_dir),
                                         delete=False) as settings_file:
            settings_file.write(const.SETTINGS_HEADER)

# Generated at 2022-06-14 08:40:09.005899
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import init_log
    from .utils import get_closest

    # Mock settings_file
    settings.user_dir = settings.user_dir.joinpath('test')
    settings.user_dir.mkdir()
    settings.user_dir.joinpath('settings.py').touch()

    settings.init()

    # Test settings from env

# Generated at 2022-06-14 08:40:21.822958
# Unit test for method init of class Settings
def test_Settings_init():
    global settings
    def test_settings_from_args():
        settings.init(get_args(['--yes']))
        assert settings.require_confirmation == False
        settings.init(get_args(['--debug']))
        assert settings.debug == True
        settings.init(get_args(['--repeat=3']))
        assert settings.repeat == 3
        settings.init(get_args())
        assert settings.repeat == 0
    def test_settings_from_env():
        os.environ['THEFUCK_ALIAS'] = "fuck"
        os.environ['THEFUCK_WAIT_COMMAND'] = "3"
        os.environ['THEFUCK_WAIT_SLOW_COMMAND'] = "3"

# Generated at 2022-06-14 08:40:33.891484
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import log_to_stderr
    from .utils import get_closest
    from .rules import load_rules
    from .command import Command
    from .utils import get_all_executables
    from functools import partial

    def reset_settings():
        global settings
        settings = Settings(const.DEFAULT_SETTINGS)
        settings._init_settings_file()

    def setup_module():
        reset_settings()

        # mockups
        settings.user_dir = Path('~/.thefuck').expanduser()
        log_to_stderr()
        # disable changing history
        settings.alter_history = False
        # setup absolute path to executables
        settings.require_confirmation = False
        settings.no_colors = True
        settings.command_timeout = 0.1

# Generated at 2022-06-14 08:40:47.194218
# Unit test for method init of class Settings
def test_Settings_init():
    # Prepare test settings
    except_settings = {
        'require_confirmation': False,
        'no_colors': True,
        'wait_command': 5,
        'rules': ['bash', 'python'],
        'priority': {'bash': 100},
        'exclude_rules': ['sudo'],
        'slow_commands': ['ls'],
        'history_limit': 100,
        'wait_slow_command': 0,
        'debug': False,
        'alter_history': True,
        'exclude_rules': [],
        'excluded_search_path_prefixes': [],
        'num_close_matches': 3,
        'instant_mode': False,
        'repeat': 1
    }

    # Assume that settings will be correct

# Generated at 2022-06-14 08:40:58.073102
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings()
    settings._get_user_dir_path = lambda: Path('~/.thefuck')
    settings._settings_from_env = lambda: {'wait_slow_command': 10}
    settings._settings_from_args = lambda: {'require_confirmation': False}
    settings._init_settings_file = lambda: None
    settings._settings_from_file = lambda: {
        'rules': ['bash', 'something_else'],
        'exclude_rules': ['git'],
        'require_confirmation': True,
        'wait_slow_command': 20,
        'no_colors': True,
        'priority': {'git_push': 100, 'git_commit': 500}}
    settings._setup_user_dir = lambda: None

    settings.init()


# Generated at 2022-06-14 08:41:07.685138
# Unit test for method init of class Settings
def test_Settings_init():
    """Unit test for method init of class Settings

    Note:
        The test is based on the premise that the config folder is empty.
    """
    import os
    import json
    from mock import patch

    # prepare environment
    test_dir = os.path.dirname(__file__)
    settings_dir = os.path.join(test_dir, '../../', '.thefuck')
    rules_dir = os.path.join(settings_dir, 'rules')
    rules_file = os.path.join(rules_dir, 'bash.py')
    settings_file = os.path.join(settings_dir, 'settings.py')
    env = os.environ
    rules_default = set(const.DEFAULT_RULES)

    # start test

# Generated at 2022-06-14 08:41:12.098177
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()

    user_dir = settings._get_user_dir_path()
    settings_path = user_dir.joinpath('settings.py')

    assert(settings_path.is_file())



# Generated at 2022-06-14 08:41:25.237700
# Unit test for method init of class Settings
def test_Settings_init():
    settings._setup_user_dir = lambda: True
    settings._settings_from_file = lambda: {'rules': ['echo']}
    settings._settings_from_env = lambda: {'wait_command': '1'}
    settings._settings_from_args = lambda x: {'require_confirmation': False}