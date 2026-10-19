

# Generated at 2022-06-14 08:32:10.331513
# Unit test for method init of class Settings
def test_Settings_init():
    from ..tests.utils import patch, FakeArgs

    settings.init()

    user_dir_path = settings._get_user_dir_path()

    with patch('thefuck.conf.settings_file.load_source') as load_source:
        settings.init()
        assert load_source.called
        name, (filename, filepath, description) = load_source.call_args
        assert filename == 'settings'
        assert filepath == str(settings.user_dir.joinpath('settings.py'))
        assert description == ('', 'r', imp.PY_SOURCE)

        load_source.side_effect = Exception()
        settings.init()

    assert settings['verbose']
    assert settings['require_confirmation']
    assert settings['wait_command'] == 1
    assert settings['history_limit'] == 0
   

# Generated at 2022-06-14 08:32:12.971444
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init({})
    assert settings.get("history_limit") == 100

# Generated at 2022-06-14 08:32:23.884298
# Unit test for method init of class Settings
def test_Settings_init():
    settings['a'] = 1
    settings['b'] = 2
    settings['c'] = 3
    settings['d'] = 4
    settings['e'] = 5
    settings['f'] = 6
    settings['g'] = 7
    settings['h'] = 8
    settings['i'] = 9
    settings['j'] = 10
    settings['k'] = 11
    settings['l'] = 12
    settings['m'] = 13
    settings['n'] = 14
    settings['o'] = 15
    settings['p'] = 16
    settings['q'] = 17
    settings['r'] = 18
    settings['s'] = 19
    settings['t'] = 20
    settings['u'] = 21
    settings['v'] = 22
    settings['w'] = 23
    settings['x'] = 24


# Generated at 2022-06-14 08:32:32.519466
# Unit test for method init of class Settings
def test_Settings_init():
    #Default
    testsettings = Settings()
    testsettings.init()
    assert testsettings['require_confirmation'] == True 
    #args.yes = True
    testsettings = Settings()
    testsettings.init(args=argparse.Namespace(yes=True))
    assert testsettings['require_confirmation'] == False 
    #env.THEFUCK_REQUIRE_CONFIRMATION = False
    testsettings = Settings()
    os.environ['THEFUCK_REQUIRE_CONFIRMATION'] = 'False'
    testsettings.init()
    assert testsettings['require_confirmation'] == False 
    #env.THEFUCK_REQUIRE_CONFIRMATION = True
    testsettings = Settings()
    os.environ['THEFUCK_REQUIRE_CONFIRMATION'] = 'True'
    test

# Generated at 2022-06-14 08:32:42.134657
# Unit test for method init of class Settings
def test_Settings_init():
    # DummyClass for class Settings
    class DummyClass(object):
        def __init__(self, user_dir):
            self.user_dir = user_dir
            self.args = None
        def is_file(self):
            return True
        def open(self, mode):
            return True
        def is_dir(self):
            return True
        def mkdir(self, parents):
            return True
        def update(self, settings_from_file):
            return True
        def _settings_from_file(self):
            return True
        def _settings_from_env(self):
            return True
        def _settings_from_args(self):
            return True
    settings = DummyClass(user_dir=True)
    settings.init()
    assert settings.user_dir

# Generated at 2022-06-14 08:32:55.513793
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()
    user_dir = settings._get_user_dir_path()
    xdg_config_home = os.environ.get('XDG_CONFIG_HOME', '~/.config')
    Path(xdg_config_home, 'thefuck').expanduser().mkdir(parents=True)
    assert settings.user_dir == user_dir
    assert settings.user_dir.joinpath('rules').exists()
    assert settings.user_dir.joinpath('settings.py').exists()
    assert const.DEFAULT_SETTINGS['alter_history'] == settings['alter_history']
    assert_settings_from_file(settings)
    assert_settings_from_env(settings)

# Generated at 2022-06-14 08:32:58.368118
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import ExceptionLogger

    settings = Settings()
    with ExceptionLogger():
        settings.init()

# Generated at 2022-06-14 08:33:06.035931
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()
    assert settings['priority'] == {'cd_parent': 10, 'brew_install_formula': -1, 'pip_install_package': -1, 'apt_install_packages': -1}
    assert settings['exclude_rules'] == []
    assert settings['num_close_matches'] == 3
    assert settings['instant_mode'] == False
    assert settings['require_confirmation'] == True

# Generated at 2022-06-14 08:33:11.823076
# Unit test for method init of class Settings
def test_Settings_init():
    argv = ['', '--yes', '--debug']
    args = parse_arguments(argv)
    settings.init(args)

    expected = {'require_confirmation': False,
                'debug': True}
    assert settings.from_file == const.DEFAULT_SETTINGS
    assert settings.from_env == {}
    assert settings.from_args == expected



# Generated at 2022-06-14 08:33:16.855433
# Unit test for method init of class Settings
def test_Settings_init():
    """Test if settings are loaded before running init"""
    settings = {}
    settings.update(const.DEFAULT_SETTINGS)
    target = Settings()
    target.init()
    result = target.keys()
    for key in settings.keys():
        assert key in result

# Generated at 2022-06-14 08:33:40.896380
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings(const.DEFAULT_SETTINGS)
    args = type('', (), {})
    settings.init(args)
    assert settings['require_confirmation'] == True
    assert settings['no_colors'] == False
    assert settings['debug'] == False
    assert settings['alter_history'] == True
    assert settings['repeat'] == False

# Generated at 2022-06-14 08:33:51.709489
# Unit test for method init of class Settings
def test_Settings_init():
    import mock
    import os
    from thefuck.settings import const
    from thefuck.settings import Settings

    args = mock.Mock()
    args.yes = False
    args.debug = False
    args.repeat = 0

    os.environ['THEFUCK_REQUIRE_CONFIRMATION'] = 'False'
    const.DEFAULT_SETTINGS['require_confirmation'] = True
    assert Settings().init(args=args)['require_confirmation']

    args.yes = True
    assert not Settings().init(args=args)['require_confirmation']
    del os.environ['THEFUCK_REQUIRE_CONFIRMATION']
    const.DEFAULT_SETTINGS['require_confirmation'] = False

    os.environ['THEFUCK_DEBUG'] = 'True'
    const.DEFAULT

# Generated at 2022-06-14 08:34:04.121507
# Unit test for method init of class Settings
def test_Settings_init():
    from .system import reset_settings_dir, reset_settings_env
    from .logs import reset_logs, log_output

    def _test(settings_path, settings_env, settings_args, settings_actual, logs_actual):
        reset_settings_dir(settings_path)
        reset_settings_env(settings_env)
        reset_logs()

        log_output(lambda: settings.init(settings_args))

        assert settings == settings_actual
        assert log_output() == logs_actual

    # pylint: disable=unused-variable

# Generated at 2022-06-14 08:34:16.864258
# Unit test for method init of class Settings
def test_Settings_init():
    # Testing for parse correctly
    # when settings.py is empty
    settings.init()
    assert loaded_settings_from_file()
    # when settings.py is not empty
    settings.update({"require_confirmation": False})
    settings.init()
    assert loaded_settings_from_file()
    assert not settings.require_confirmation
    settings.update({"require_confirmation": True})

    # Testing for parse correctly
    # when env is empty
    settings.init()
    assert loaded_settings_from_env()
    # when env is not empty
    os.environ["TF_DEBUG"] = "True"
    settings.init()
    assert loaded_settings_from_env()
    assert settings.debug
    del os.environ["TF_DEBUG"]

    # Testing for parse correctly
    # when args is

# Generated at 2022-06-14 08:34:30.578489
# Unit test for method init of class Settings
def test_Settings_init():
    import tempfile
    import os

    def _create_dir(dir):
        if not os.path.exists(dir):
            os.makedirs(dir)

    with tempfile.TemporaryDirectory() as temp_dir:
        _create_dir(os.path.join(temp_dir, 'rules'))

        user_dir = os.path.join(temp_dir, 'user')
        _create_dir(user_dir)

        temp_settings = os.path.join(user_dir, 'settings.py')

        def _write_settings(key, val):
            with open(temp_settings, 'w') as f:
                f.write("{} = '{}'".format(key, val))

        old_xdg = os.environ.get('XDG_CONFIG_HOME')


# Generated at 2022-06-14 08:34:43.325570
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import log_exception

    settings.init({'repeat' : 3, 'debug' : True, 'yes' : True})
    assert settings.repeat == 3
    assert settings.debug is True
    assert settings.require_confirmation is False

    os.environ['THEFUCK_NO_COLORS'] = 'True'
    os.environ['THEFUCK_RULES'] = 'default_rules'
    os.environ['THEFUCK_HISTORY_LIMIT'] = '500'
    os.environ['THEFUCK_WAIT_COMMAND'] = '1000'
    os.environ['THEFUCK_WAIT_SLOW_COMMAND'] = '1010'
    os.environ['THEFUCK_NUM_CLOSE_MATCHES'] = '1'

# Generated at 2022-06-14 08:34:52.786869
# Unit test for method init of class Settings
def test_Settings_init():
    from .rules import RulesCollection
    import argparse

    argparse_args = argparse.Namespace(
        yes=False, debug=False, repeat=None)
    settings.init(argparse_args)
    assert settings.require_confirmation == True
    assert isinstance(settings.rules, RulesCollection)

    argparse_args = argparse.Namespace(
        yes=True, debug=False, repeat=None)
    settings.init(argparse_args)
    assert settings.require_confirmation == False

    argparse_args = argparse.Namespace(
        yes=False, debug=True, repeat=None)
    settings.init(argparse_args)
    assert settings.debug == True

    argparse_args = argparse.Namespace(
        yes=False, debug=False, repeat=True)
    settings

# Generated at 2022-06-14 08:35:06.229965
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert isinstance(settings.user_dir, Path)
    assert isinstance(settings.rules, list)
    assert isinstance(settings.exclude_rules, list)
    assert isinstance(settings.priority, dict)
    assert isinstance(settings.require_confirmation, bool)
    assert isinstance(settings.no_colors, bool)
    assert isinstance(settings.debug, bool)
    assert isinstance(settings.wait_command, int)
    assert isinstance(settings.history_limit, int)
    assert isinstance(settings.wait_slow_command, int)
    assert isinstance(settings.alter_history, bool)
    assert isinstance(settings.slow_commands, list)
    assert isinstance(settings.num_close_matches, int)

# Generated at 2022-06-14 08:35:16.368785
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import capture_log
    from .system import TemporaryDirectory
    from .tests.utils import change_env
    from .utils import get_all_executables_in_path

    with TemporaryDirectory() as tmp_dir:
        test_dir = Path(tmp_dir)
        settings_file = test_dir.joinpath('settings.py')
        with settings_file.open(mode='w') as f:
            f.write('require_confirmation = False\n')

        with capture_log() as log_capture:
            with change_env({'XDG_CONFIG_HOME': tmp_dir}):
                settings.init()

        assert settings.require_confirmation is False
        assert len(log_capture.errors) == 0
        assert 'Can\'t load settings from file' not in log_capt

# Generated at 2022-06-14 08:35:26.691955
# Unit test for method init of class Settings
def test_Settings_init():
    import thefuck.conf.settings
    def _get_user_dir_path():
        return thefuck.conf.settings.Path('res')

    def _settings_from_file():
        return {'priority': {'git': 1, 'bower': 2}}

    def _settings_from_env():
        return {'priority': {'bower': 1, 'git': 2}, 'rules': ['git', 'bower']}

    def _settings_from_args(args):
        return {'priority': {'bower': 3, 'git': 4}, 'no_colors': True}


# Generated at 2022-06-14 08:35:58.086995
# Unit test for method init of class Settings
def test_Settings_init():
    # set env to default value
    for key in const.ENV_TO_ATTR.keys():
        if key in os.environ:
            os.environ.pop(key)
    # call init method of class Settings
    settings.init()
    # test if env is set as default value
    assert settings[const.ENV_TO_ATTR['FUCK_WAIT_COMMAND']] == const.DEFAULT_SETTINGS['wait_command']
    assert settings[const.ENV_TO_ATTR['FUCK_WAIT_SLOW_COMMAND']] == const.DEFAULT_SETTINGS['wait_slow_command']
    assert settings[const.ENV_TO_ATTR['FUCK_HISTORY_LIMIT']] == const.DEFAULT_SETTINGS['history_limit']

# Generated at 2022-06-14 08:36:06.138143
# Unit test for method init of class Settings
def test_Settings_init():
    new_settings = Settings()
    new_settings.init()
    assert new_settings.get('require_confirmation') == True
    assert new_settings.get('repeat') == False
    assert new_settings.get('debug') == False
    new_settings.init(args=object)
    assert new_settings.get('require_confirmation') == True
    assert new_settings.get('repeat') == False
    assert new_settings.get('debug') == False
    assert new_settings.get('rule') == None
    assert new_settings.get('rules') == ['git_push', 'git_add', 'git_commit', 'sudo']
    assert new_settings.get('exclude_rules') == []
    assert new_settings.get('history_limit') == None
    assert new_settings.get('no_colors')

# Generated at 2022-06-14 08:36:07.800739
# Unit test for method init of class Settings
def test_Settings_init():
    # todo: test
    pass

# Generated at 2022-06-14 08:36:17.557289
# Unit test for method init of class Settings
def test_Settings_init():
    import inspect
    import thefuck

    def _test_init():
        settings.init()

    # Catch output from init
    saved = sys.stdout
    try:
        from io import StringIO
        out = StringIO()
        sys.stdout = out
        _test_init()
        output = out.getvalue().strip()
    finally:
        sys.stdout = saved

    # check that output prints a warning
    assert 'deprecated' in output

    # check that settings[rules] is [DEFAULT_RULES]
    assert settings['rules'] == const.DEFAULT_RULES

    # teardown files created by init
    thefuck.settings.user_dir.rmtree()

# Generated at 2022-06-14 08:36:19.882072
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()

# Generated at 2022-06-14 08:36:26.940791
# Unit test for method init of class Settings
def test_Settings_init():
    def _update_settings(r):
        r.update(settings._settings_from_file())
        r.update(settings._settings_from_env())
    r = {}
    _update_settings(r)
    assert r['require_confirmation'] == False and r['repeat'] == False
    assert r['history_limit'] == None and r['rules'] == ['sudo']

# Generated at 2022-06-14 08:36:31.239767
# Unit test for method init of class Settings
def test_Settings_init():
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()
    assert settings.user_dir == Path('~/.config/thefuck/').expanduser()

# Generated at 2022-06-14 08:36:42.935211
# Unit test for method init of class Settings
def test_Settings_init():
    from _pytest.monkeypatch import MonkeyPatch
    import sys
    import os
    m = MonkeyPatch()

    settings = Settings(const.DEFAULT_SETTINGS)
    settings._get_user_dir_path = lambda: Path("~/.config/thefuck/")
    m.setenv("TF_INSTANT_MODE", "true")
    m.setenv("TF_ALTER_HISTORY", "true")
    m.setenv("TF_NO_COLORS", "true")
    m.setattr(settings, "_settings_from_file", lambda: {'priority': {"ls": 1, "cd": 2}})
    settings._settings_from_args = lambda x: {'require_confirmation': False, 'debug': False, 'repeat': 1}
    settings.init()


# Generated at 2022-06-14 08:36:53.006401
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception

    def raise_exception(*_, **__):
        raise Exception()

    def mock_open(_, mode='r'):
        if mode == 'r':
            return ['print(5)']
        return []

    args = type('arg', (object, ), {'yes': True, 'debug': True, 'repeat': '2'})
    env_to_attr = {'TF_REQUIRE_CONFIRMATION': 'require_confirmation',
                   'TF_DEBUG': 'debug',
                   'TF_REPEAT': 'repeat'}

    with patch.object(settings, '_settings_from_file', raise_exception):
        settings.init()
        assert exception.called


# Generated at 2022-06-14 08:37:06.197767
# Unit test for method init of class Settings
def test_Settings_init():
    _settings = Settings()
    # _settings.init()
    # ugly hack to make sure unittests don't write anything to ~/.config/thefuck
    _settings._get_user_dir_path = lambda: Path('tests/testdir')
    _settings.init()

    assert _settings._get_user_dir_path() == Path('tests/testdir')
    assert _settings.user_dir == Path('tests/testdir')

    assert _settings.get('no_colors') == False
    assert _settings.get('wait_command') == 3
    assert _settings.get('require_confirmation') == True

    _settings = Settings()
    # _settings.init()
    # ugly hack to make sure unittests don't write anything to ~/.config/thefuck
    _settings._get_user_dir_path = lambda: Path

# Generated at 2022-06-14 08:37:48.791250
# Unit test for method init of class Settings
def test_Settings_init():
    old_dir = os.getcwd()
    os.chdir(os.path.dirname(__file__))
    try:
        result = settings.init(object)
    finally:
        os.chdir(old_dir)
    # Firstly, we load the content of settings.py file to result

# Generated at 2022-06-14 08:37:59.581094
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings['require_confirmation'] == True
    assert settings['wait_command'] == 1
    assert settings['wait_slow_command'] == 15
    assert settings['history_limit'] == 10
    assert settings['rules'] == []
    assert settings['exclude_rules'] == []
    assert settings['priority'] == {}
    assert settings['no_colors'] == False
    assert settings['debug'] == False
    assert settings['slow_commands'] == []
    assert settings['excluded_search_path_prefixes'] == []
    assert settings['alter_history'] == False
    assert settings['instant_mode'] == False
    assert settings['num_close_matches'] == 3


# Generated at 2022-06-14 08:38:07.329886
# Unit test for method init of class Settings
def test_Settings_init():
    from unittest import TestCase, main
    from os import environ, remove
    from os.path import abspath
    from .system import TemporaryDirectory
    from .const import DEFAULT_SETTINGS, SETTINGS_HEADER

    class SettingsTestCase(TestCase):
        def setUp(self):
            self.settings = Settings()

        def test_init(self):
            self.settings.init()
            self.assertEqual(self.settings['DEBUG'], False)
            self.assertEqual(self.settings['REQUIRE_CONFIRMATION'], True)
            self.assertEqual(self.settings['WAIT_COMMAND'], 0)
            with TemporaryDirectory() as tmp_dir:
                environ['XDG_CONFIG_HOME'] = tmp_dir
                self.settings.init()
               

# Generated at 2022-06-14 08:38:17.999006
# Unit test for method init of class Settings
def test_Settings_init():
    os.environ['THEFUCK_WAIT_COMMAND'] = '1'
    os.environ['THEFUCK_PRIORITY'] = 'sudo=100'
    os.environ['THEFUCK_INSTANT_MODE'] = 'false'
    os.environ['THEFUCK_SHOW_SUDO'] = 'true'
    os.environ['THEFUCK_SUDO_COMMANDS'] = 'sudo:yum:apt-get'
    os.environ['THEFUCK_SLOW_COMMANDS'] = 'brew'
    os.environ['THEFUCK_ALTER_HISTORY'] = 'no'
    os.environ['THEFUCK_DEBUG'] = 'True'
    os.environ['THEFUCK_REQUIRE_CONFIRMATION'] = '1'
   

# Generated at 2022-06-14 08:38:30.091287
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception, error
    from .utils import get_closest, wrap_color
    from .tools import Tool
    from functools import partial

    rules_dir = settings.user_dir.joinpath('rules')
    assert rules_dir.is_dir() is True

    settings_path = settings.user_dir.joinpath('settings.py')
    assert settings_path.is_file() is True
    with settings_path.open() as settings_file:
        assert settings_file.read() == '{}\n'.format(const.SETTINGS_HEADER)

    settings.init(args=None)
    for key in const.DEFAULT_SETTINGS.keys():
        assert getattr(settings, key) == const.DEFAULT_SETTINGS[key]

    settings_path.unlink()


# Generated at 2022-06-14 08:38:43.306341
# Unit test for method init of class Settings
def test_Settings_init():
    assert settings.__class__.__name__ == 'Settings'
    assert settings['debug'] == False
    assert settings['require_confirmation'] == True
    assert settings['rules'] == const.DEFAULT_RULES
    assert settings['exclude_rules'] == []
    assert settings['wait_command'] == 1
    assert settings['slow_commands'] == []
    assert settings['history_limit'] == 0
    assert settings['wait_slow_command'] == 15
    assert settings['alter_history'] == False
    assert settings['no_colors'] == False
    assert settings['priority'] == {}
    assert settings['excluded_search_path_prefixes'] == []
    assert settings['num_close_matches'] == 3
    assert settings['instant_mode'] == False
    assert settings['repeat'] == False

# Generated at 2022-06-14 08:38:50.739452
# Unit test for method init of class Settings
def test_Settings_init():
    from tempfile import mkdtemp
    from .path import Path

    settings.__dict__.pop('user_dir', None)
    try:
        tmp_dir = Path(mkdtemp())
        os.environ['XDG_CONFIG_HOME'] = text_type(tmp_dir)

        settings.init(None)
        assert settings.user_dir == tmp_dir.joinpath('.config', 'thefuck')
    finally:
        settings.__dict__.pop('user_dir', None)
        settings.__dict__.pop('require_confirmation', None)
        tmp_dir.rmtree()

# Generated at 2022-06-14 08:38:59.598434
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings['wait_command'] == 3
    assert settings['rules'] == ['sudo_rm_rf', 'man', 'ldconfig', 'brew_cask_upgrade', 'brew_upgrade', 'apt_get_purge', 'apt_get_remove', 'brew_wip_uninstall']
    settings.init(args=None)
    assert settings['wait_command'] == 3
    assert settings['rules'] == ['sudo_rm_rf', 'man', 'ldconfig', 'brew_cask_upgrade', 'brew_upgrade', 'apt_get_purge', 'apt_get_remove', 'brew_wip_uninstall']
    settings.init(args=object())
    assert settings['wait_command'] == 3

# Generated at 2022-06-14 08:39:01.461298
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings == const.DEFAULT_SETTINGS

# Generated at 2022-06-14 08:39:08.810554
# Unit test for method init of class Settings
def test_Settings_init():
    settings._setup_user_dir = lambda: settings.user_dir
    settings._init_settings_file = lambda: None
    settings._settings_from_file = lambda: settings
    settings._settings_from_env = lambda: settings
    settings._settings_from_args = lambda x: settings
    settings['test'] = 'test'
    settings.init()
    assert 'test' in settings.keys()

# Generated at 2022-06-14 08:40:19.968704
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()


# Generated at 2022-06-14 08:40:31.396857
# Unit test for method init of class Settings
def test_Settings_init():
    from . import get_settings_path, logs

    def mock_logs(level, msg, *args):
        assert level == 'WARNING'
        assert msg == 'Config path {} is deprecated. Please move to {}'
        from .system import Path
        assert args == (Path('~', '.thefuck').expanduser(),
                        Path('~/.config', 'thefuck').expanduser())

    logs.log = mock_logs
    assert settings.init() is None
    assert settings.debug is False
    assert settings.history_limit == 0
    assert settings.require_confirmation is True

# Generated at 2022-06-14 08:40:38.888551
# Unit test for method init of class Settings
def test_Settings_init():
    user_dir = Path('~/.thefuck/').expanduser()
    os.environ['THEFUCK_RULE'] = 'test_rule'
    os.environ['THEFUCK_REQUIRE_CONFIRMATION'] = 'True'
    os.environ['THEFUCK_RULES_EXCLUDE'] = ':DEFAULT_RULES:'
    os.environ['THEFUCK_PRIORITY'] = 'test_rule=1'
    os.environ['THEFUCK_ALIAS'] = 'fuck'

    settings.init()

    assert settings['rules'] == const.DEFAULT_RULES + ['test_rule']
    assert settings['require_confirmation'] is True
    assert settings['priority'] == {'test_rule': 1}
    assert settings['alias'] == 'fuck'



# Generated at 2022-06-14 08:40:51.228702
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import capture_exceptions, is_debug
    from .logs import log_exception, log_to_file, set_log_file
    from .logs import log_to_null
    from .logs import set_log_file, set_log_null
    import os
    import sys
    import tempfile
    import shutil
    import mock
    from . import const
    from .utils import memoize
    from .system import Path

    # Create a temp directory and clean it
    env = os.environ.copy()
    temp_dir = tempfile.mkdtemp()
    env['XDG_CONFIG_HOME'] = temp_dir
    env['TF_ARG_yes'] = 'yes'
    env['TF_ARG_debug'] = 'yes'


# Generated at 2022-06-14 08:40:52.970061
# Unit test for method init of class Settings
def test_Settings_init():
    assert settings.user_dir == '~/.config/thefuck'

# Generated at 2022-06-14 08:41:06.161580
# Unit test for method init of class Settings
def test_Settings_init():
    import argparse
    import tempfile
    import shutil
    import os

    settings.init()
    settings.init(args=argparse.Namespace(yes=True))
    settings.init(args=argparse.Namespace(debug=True))
    settings.init(args=argparse.Namespace(repeat=2))
    settings.init(args=argparse.Namespace(yes=True, debug=False))

    temp_dir = tempfile.mkdtemp()
    old_user_dir = settings.user_dir
    settings.user_dir = Path(temp_dir)

    test_settings = {}


# Generated at 2022-06-14 08:41:18.743473
# Unit test for method init of class Settings
def test_Settings_init():
    import unittest
    import mock
    import six

    class TestSettings(unittest.TestCase):
        def test_init_settings_file(self):
            with mock.patch.object(settings.user_dir, 'open') as mock_open:
                mock_open.return_value = mock.Mock(spec=six.StringIO)
                mock_open.return_value.__enter__.return_value = mock_open.return_value
                mock_open.return_value.__exit__.return_value = None
                mock_open.return_value.write = mock.Mock()

                settings.init()

                mock_open.assert_called_once_with(mode='w')


# Generated at 2022-06-14 08:41:28.512220
# Unit test for method init of class Settings
def test_Settings_init():
    # When there is no user config file, creates it.
    def _load_settings_file(self):
        raise Exception

    settings = Settings(const.DEFAULT_SETTINGS)
    settings._load_settings_file = _load_settings_file
    settings._setup_user_dir()
    settings.init()

    assert settings.user_dir.joinpath('settings.py').is_file()

    # Loads data from settings.py.
    def _load_settings_file(self):
        return {'require_confirmation': True, 'debug': False}
    settings = Settings(const.DEFAULT_SETTINGS)
    settings._load_settings_file = _load_settings_file
    settings.init()
    assert settings['require_confirmation'] is True
    assert settings['debug'] is False

    # Loads