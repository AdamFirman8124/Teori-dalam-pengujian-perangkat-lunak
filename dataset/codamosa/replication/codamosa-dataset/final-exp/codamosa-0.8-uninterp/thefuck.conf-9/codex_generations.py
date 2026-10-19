

# Generated at 2022-06-14 08:31:57.192608
# Unit test for method init of class Settings
def test_Settings_init():
    from mock import patch
    from thefuck import settings as thefuck_settings
    from thefuck import const
    from thefuck.utils import python_version
    from thefuck.settings import Settings

    with patch('thefuck.settings.logs.exception', return_value=None) as mock_logs:
        settings = Settings()
        settings.init()
        assert settings == thefuck_settings.settings
        assert mock_logs.call_count == 0

    # test `init` w/o file
    with patch('thefuck.settings.logs.exception') as mock_logs:
        settings = Settings()
        with patch('thefuck.settings.settings.user_dir', new_callable=Path) as mock_path:
            mock_path.return_value = 'mocked_path'

# Generated at 2022-06-14 08:32:10.079130
# Unit test for method init of class Settings
def test_Settings_init():
    def clear_settings():
        for key in list(settings.keys()):
            del settings[key]


# Generated at 2022-06-14 08:32:22.178946
# Unit test for method init of class Settings
def test_Settings_init():
    from tempfile import mkdtemp
    from shutil import rmtree
    from textwrap import dedent

    args = type('', (), {})()
    args.yes, args.repeat, args.debug = True, 2, True

# Generated at 2022-06-14 08:32:35.771104
# Unit test for method init of class Settings
def test_Settings_init():
    from thefuck.rules.git_dirty_worktree import match, get_new_command
    import thefuck.shells.shell as shell_factory

    settings.init()

    assert settings.user_dir == Path('~/.config/thefuck').expanduser()
    assert settings.rules == [match,] # expected: (<thefuck.rules.git_dirty_worktree.match object at 0x7fa4e1a6fdd8>,)
    assert settings.exclude_rules == ()
    assert settings.priority == {}
    assert settings.history_limit == 100
    assert settings.wait_command == 0
    assert settings.require_confirmation == False
    assert settings.slow_commands == []
    assert settings.wait_slow_command == 5
    assert settings.no_colors == False
    assert settings.alter_

# Generated at 2022-06-14 08:32:43.978629
# Unit test for method init of class Settings
def test_Settings_init():
    """Unit test for method init of class Settings"""
    from .logs import get_logger

    logger = get_logger('test')
    try:
        settings['user_dir'] = Path('/tmp/thefuck')
        settings['user_dir'].rmtree()
        settings.init()
        settings['user_dir'].joinpath('settings.py').remove()
        settings['user_dir'].rmtree()
    except Exception:
        logger.exception('Can\'t clear created files')

    # check settings work
    settings['user_dir'] = Path('/tmp/thefuck')
    settings.init()
    assert(settings['user_dir'].is_dir())
    settings['user_dir'].joinpath('settings.py').remove()
    settings['user_dir'].rmtree()



# Generated at 2022-06-14 08:32:56.018432
# Unit test for method init of class Settings
def test_Settings_init():
    import sys
    import os
    import imp
    import shutil

    def _create_user_dir(rules_dir=False, settings_file=False):
        user_dir = os.path.join(os.path.expanduser('~'), '.thefuck')
        if not os.path.exists(user_dir):
            os.mkdir(user_dir)
        if rules_dir:
            os.mkdir(os.path.join(user_dir, 'rules'))
        if settings_file:
            set_file = open(os.path.join(user_dir, 'settings.py'), 'w')
            set_file.write('require_confirmation = False')

    def _remove_user_dir():
        shutil.rmtree(os.path.expanduser('~/.thefuck'))

# Generated at 2022-06-14 08:33:08.548531
# Unit test for method init of class Settings
def test_Settings_init():
    import tempfile
    import shutil
    import os
    import os.path

    temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-14 08:33:17.361003
# Unit test for method init of class Settings
def test_Settings_init():
    import os
    from mock import patch, call
    from six import StringIO
    from .logs import exception
    from . import settings_loader

    test_user_dir = Path('tests/.thefuck')
    test_settings_file_path = test_user_dir / 'settings.py'
    test_args = StringIO('--help')
    test_args.name = 'settings_file'
    test_args.__enter__ = lambda x: x
    test_args.__exit__ = lambda x, y, z, w: x
    test_args_yes = StringIO('--yes')
    test_args_yes.name = 'settings_file'
    test_args_yes.__enter__ = lambda x: x
    test_args_yes.__exit__ = lambda x, y, z, w: x
    test

# Generated at 2022-06-14 08:33:19.617852
# Unit test for method init of class Settings
def test_Settings_init():
    assert type(settings.init()) == dict
    assert 'require_confirmation' in settings.init()

# Generated at 2022-06-14 08:33:30.637819
# Unit test for method init of class Settings
def test_Settings_init():
    set_default = dict(const.DEFAULT_SETTINGS)
    set_default['user_dir'] = Path('/home/user', '.config', 'thefuck')
    set_default['history_limit'] = '50'
    set_default['no_colors'] = 'True'
    set_default['require_confirmation'] = 'FALSE'
    os.environ['THEFUCK_RULES'] = 'bash:python:ruby:DEFAULT_RULES'
    os.environ['THEFUCK_PRIORITY'] = 'bash=1:python=2:ruby=3'
    os.environ['THEFUCK_SLOW_COMMANDS'] = 'ff:gg:hh'
    os.environ['THEFUCK_DEBUG'] = 'True'

# Generated at 2022-06-14 08:33:59.512742
# Unit test for method init of class Settings
def test_Settings_init():
    result = settings.init()
    assert result is None

# Generated at 2022-06-14 08:34:01.538701
# Unit test for method init of class Settings
def test_Settings_init():
    global settings
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()



# Generated at 2022-06-14 08:34:14.986618
# Unit test for method init of class Settings
def test_Settings_init():
    # Test for _init_settings_file method
    test_settings = Settings()
    test_settings._init_settings_file()
    settings_path = test_settings._get_user_dir_path().joinpath('settings.py')
    assert settings_path.is_file()
    assert settings_path.read_text() == const.SETTINGS_HEADER
    settings_path.remove()

    # Test for _setup_user_dir method
    settings._setup_user_dir()
    rules_dir = settings.user_dir.joinpath('rules')
    assert rules_dir.is_dir()

    # Test for _settings_from_env method
    os.environ['THEFUCK_RULES'] = 'DEFAULT_RULES:zoo'
    os.environ['THEFUCK_PRIORITY']

# Generated at 2022-06-14 08:34:19.889400
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import Logger

    args = type('args', (), {'yes': True, 'debug': True, 'repeat': True})

    def exception(message, exc_info):
        raise exc_info[0](exc_info[1])

    Logger.exception = exception
    settings.init(args=args)
    assert settings.require_confirmation is False
    assert settings.debug is True
    assert settings.repeat is True



# Generated at 2022-06-14 08:34:30.692687
# Unit test for method init of class Settings
def test_Settings_init():
	import unittest
	from unittest import TestCase, TestSuite, TextTestRunner

	class TestSettings(TestCase):
		def setUp(self):
			self.settings = Settings(const.DEFAULT_SETTINGS)

		def test_settings_init(self):
			self.settings.init(args=None)

	def test_suite():
		suite = TestSuite()
		suite.addTest(TestSettings('test_settings_init'))
		return suite

	if __name__ == '__main__':
		TextTestRunner().run(test_suite())

# Generated at 2022-06-14 08:34:34.959795
# Unit test for method init of class Settings
def test_Settings_init():
    default_settings = const.DEFAULT_SETTINGS
    default_settings['user_dir'] = Path(u'~')
    # Thefuck doesn't affect on PYTHONPATH.
    if 'PYTHONPATH' in os.environ:
        del os.environ['PYTHONPATH']
    settings.init()
    assert settings == default_settings

# Generated at 2022-06-14 08:34:40.596073
# Unit test for method init of class Settings
def test_Settings_init():
    """
    settings is a Singleton object. This functions will test that init
    is indeed updating settings.
    """
    old_settings = settings.copy()
    settings.init()
    for key in settings.keys():
        assert old_settings[key] == settings[key]

# Generated at 2022-06-14 08:34:51.237525
# Unit test for method init of class Settings
def test_Settings_init():
    import mock
    from .logs import print_debug

    settings_ = Settings(const.DEFAULT_SETTINGS)
    settings_.init(mock.Mock())
    # Change settings
    settings_._settings_from_file = lambda: {'alter_history': True}
    settings_._settings_from_env = lambda: {'require_confirmation': False}
    settings_._settings_from_args = lambda x: {'repeat': 'echo'}
    settings_.init(mock.Mock())
    assert settings.alter_history is True
    assert settings.require_confirmation is False
    assert settings.repeat == 'echo'
    assert print_debug.called is True

# Generated at 2022-06-14 08:35:02.962390
# Unit test for method init of class Settings
def test_Settings_init():
    settings.clear()

    try:
        settings.init()
        assert not settings.require_confirmation
        assert not settings.no_colors
        assert settings.rules == const.DEFAULT_RULES
        assert settings.wait_command == 1
        assert settings.exclude_rules == []
        assert not settings.debug
        assert settings.history_limit == None
        assert settings.slow_commands == []
        assert settings.wait_slow_command == 9
        assert settings.priority == {}
        assert not settings.alter_history
        assert not settings.instant_mode
        assert settings.num_close_matches == 3
    finally:
        settings.clear()


# Generated at 2022-06-14 08:35:03.906477
# Unit test for method init of class Settings
def test_Settings_init():
    pass

# Generated at 2022-06-14 08:36:01.159208
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception

    from mock import patch
    from six import StringIO
    from .system import Path
    from .main import parse_args

    with patch('thefuck.settings.Settings._init_settings_file'):
        with patch.object(Path, 'joinpath', return_value=Path('settings.py')):
            with patch('thefuck.settings.Settings._settings_from_file',
                       return_value=dict(key='value')):
                with patch('thefuck.settings.Settings._settings_from_env',
                           return_value=dict(number=42)):
                    settings.init(parse_args(''))
    
    assert settings['key'] == 'value'
    assert settings['number'] == 42

    # Test for exception with error in _settings_from_file

# Generated at 2022-06-14 08:36:14.064767
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings['require_confirmation'] == True
    assert settings['slow_commands'] == ['lein']
    assert settings['alter_history'] == False
    assert settings['exclude_rules'] == []
    assert settings['excluded_search_path_prefixes'] == []
    assert settings['history_limit'] == 10
    assert settings['wait_command'] == 1
    assert settings['wait_slow_command'] == 15
    assert settings['priority'] == {}

# Generated at 2022-06-14 08:36:20.928674
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import capture_logs

    with capture_logs() as logs, \
            Path('settings').joinpath('settings.py').open(mode='w') as f:
        f.write(const.SETTINGS_HEADER)

    # init settings with default settings
    settings.init()
    assert not logs
    assert settings['require_confirmation']
    assert settings['rules'] == const.DEFAULT_RULES

    # overwrite setting
    with Path('settings').joinpath('settings.py').open(mode='a') as f:
        f.write(u'require_confirmation = False')
    with capture_logs() as logs:
        settings.init()
    assert not logs
    assert not settings['require_confirmation']
    assert settings['rules'] == const.DEFAULT_RULES

    #

# Generated at 2022-06-14 08:36:26.872963
# Unit test for method init of class Settings
def test_Settings_init():
    class TestArgs:
        pass
    args = TestArgs()
    args.yes = True
    args.debug = True
    args.repeat = True
    settings.init(args)
    assert settings.require_confirmation == False
    assert settings.debug == True
    assert settings.repeat == True

# Generated at 2022-06-14 08:36:35.541177
# Unit test for method init of class Settings
def test_Settings_init():
    set_obj = Settings(const.DEFAULT_SETTINGS)
    set_obj.init()
    assert(set_obj['history_limit'] == const.DEFAULT_SETTINGS['history_limit'])
    assert(set_obj.user_dir == Path('~', '.thefuck').expanduser())
    assert(set_obj.user_dir.joinpath('settings.py').is_file())
    assert(set_obj['require_confirmation'] == const.DEFAULT_SETTINGS['require_confirmation'])
    assert(set_obj['priority'] == const.DEFAULT_SETTINGS['priority'])
    assert(set_obj['rules'] == const.DEFAULT_SETTINGS['rules'])

# Generated at 2022-06-14 08:36:43.136151
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings.user_dir == settings._get_user_dir_path()
    settings_file_path = settings.user_dir.joinpath('settings.py')
    assert settings_file_path.is_file()
    with settings_file_path.open('rb') as settings_file:
        assert settings_file.read().decode('utf-8').startswith(const.SETTINGS_HEADER)

# Generated at 2022-06-14 08:36:45.673340
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings.user_dir
    user_dir_path = settings.user_dir.joinpath('settings.py')
    assert user_dir_path.is_file()


# Generated at 2022-06-14 08:36:48.986289
# Unit test for method init of class Settings
def test_Settings_init():
    """
    omit test in pycharm,
    because it can't read the code in thefuck.py
    """
    my_settings = Settings(const.DEFAULT_SETTINGS)
    my_settings.init('settings.py')

# Generated at 2022-06-14 08:36:56.901851
# Unit test for method init of class Settings
def test_Settings_init():
    args = '--no-colors'
    os.environ['TF_INSTANT_MODE'] = 'True'
    os.environ['TF_ALTER_HISTORY'] = 'False'
    os.environ['TF_HISTORY_LIMIT'] = '777'
    os.environ['TF_PRIORITY'] = 'fuck = 1:f**k = 2'
    os.environ['TF_RULES'] = 'DEFAULT_RULES'
    os.environ['TF_EXCLUDE_RULES'] = 'f**k'
    os.environ['TF_WAIT_COMMAND'] = '888'
    os.environ['TF_WAIT_SLOW_COMMAND'] = '999'
    os.environ['TF_DEBUG'] = 'True'
    os

# Generated at 2022-06-14 08:37:08.073757
# Unit test for method init of class Settings
def test_Settings_init():
    class MockArgs(object):
        def __init__(self, yes=False, repeat=0, debug=False):
            self.yes = yes
            self.repeat = repeat
            self.debug = debug

    test_env_vars = [('XDG_CONFIG_HOME', 'test_user_dir')]
    # Create a fake user dir for test
    with mock.patch.dict(os.environ, test_env_vars.items(), clear=True):
        tmp_user_dir = Path("test_user_dir", "thefuck").expanduser()
        if not tmp_user_dir.is_dir():
            tmp_user_dir.mkdir(parents=True, exist_ok=True)

# Generated at 2022-06-14 08:38:53.277409
# Unit test for method init of class Settings
def test_Settings_init():
    s = Settings(const.DEFAULT_SETTINGS)
    os.environ['THEFUCK_REQUIRE_CONFIRMATION'] = 'true'
    os.environ['THEFUCK_DEBUG'] = 'true'
    os.environ['THEFUCK_WAIT_COMMAND'] = '0'
    os.environ['THEFUCK_SLOW_COMMANDS'] = 'git:pip'
    os.environ['THEFUCK_RULES'] = ':'.join(const.DEFAULT_RULES + ['cd2', 'nv'])
    s.init()

    assert s.get('require_confirmation')
    assert s.get('debug')
    assert s.get('wait_command') == 0
    assert s.get('slow_commands') == ['git', 'pip']

# Generated at 2022-06-14 08:38:56.495933
# Unit test for method init of class Settings
def test_Settings_init():
    settings.init()
    assert settings.user_dir
    assert settings.user_dir.isdir()

    user_dir = settings.user_dir
    settings.init()
    assert settings.user_dir == user_dir

    settings.init(object())
    assert settings.user_dir == user_dir

# Generated at 2022-06-14 08:39:03.321998
# Unit test for method init of class Settings
def test_Settings_init():
    import copy
    from .logs import exception

    class Mock(object): pass
    fake_args = Mock()
    fake_args.yes = ""
    fake_args.repeat = 0
    fake_args.no_color = ""
    fake_args.debug = ""

    # There are two variables that were defined in __init__, but
    # got assigned to each time init is called, therefore making
    # them different after each call. We need to pop them
    # before comparing 'settings' with DEFAULT_SETTINGS.
    settings.pop("require_confirmation", None)
    settings.pop("repeat", None)

    assert settings == const.DEFAULT_SETTINGS
    settings.init()
    assert settings == const.DEFAULT_SETTINGS
    settings.init(fake_args)

    copy_settings = copy.deep

# Generated at 2022-06-14 08:39:15.955501
# Unit test for method init of class Settings
def test_Settings_init():
    xdg_config_home = os.environ.get('XDG_CONFIG_HOME', '~/.config')
    user_dir = Path(xdg_config_home, 'thefuck').expanduser()
    if not user_dir.is_dir():
        user_dir.mkdir(parents=True)
    with user_dir.joinpath('settings.py').open(mode='w') as settings_file:
        settings_file.write(const.SETTINGS_HEADER)
        for setting in const.DEFAULT_SETTINGS.items():
            settings_file.write(u'# {} = {}\n'.format(*setting))
    settings.init()
    # print(settings)
    assert settings == const.DEFAULT_SETTINGS

    cwd = os.getcwd()
    os.en

# Generated at 2022-06-14 08:39:29.200106
# Unit test for method init of class Settings
def test_Settings_init():
    import os

    settings.init()
    assert 'require_confirmation' in settings
    assert 'no_colors' in settings
    settings_file = os.path.join(settings.user_dir,'settings.py')
    assert os.path.exists(settings_file)

    settings = Settings()
    settings['user_dir'] = os.path.join(os.path.dirname(__file__), '..', 'test')
    settings.init()
    assert 'require_confirmation' in settings
    assert 'no_colors' in settings
    assert 'require_confirmation' in settings
    assert 'no_colors' in settings
    settings_file = os.path.join(settings.user_dir,'settings.py')
    assert not os.path.exists(settings_file)


# Generated at 2022-06-14 08:39:37.757582
# Unit test for method init of class Settings
def test_Settings_init():
    """Returns list of three elements - errors and two lists with error and success tests."""
    from .logs import exception
    from ..__version__ import __version__

    # load open to mock
    import imp

# Generated at 2022-06-14 08:39:45.455584
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import log
    from .logs import exception

    settings = Settings(const.DEFAULT_SETTINGS)
    args = type('obj', (object,), {'debug': 'true',
                                   'repeat': '3',
                                   'yes': 'True'})()
    settings.init(args)

    assert settings['debug'] == True
    assert settings['repeat'] == 3
    assert settings['require_confirmation'] == False



# Generated at 2022-06-14 08:39:55.759455
# Unit test for method init of class Settings
def test_Settings_init():
    global settings
    settings = Settings(const.DEFAULT_SETTINGS)
    settings.init()
    assert settings.user_dir == Path('~/').expanduser().joinpath('.config', 'thefuck')
    assert settings.rules == const.DEFAULT_RULES
    assert settings.require_confirmation == True
    assert settings.history_limit == None
    assert settings.no_colors == False
    assert settings.debug == False
    assert settings.alter_history == False


u"""
Unit tests for methods _settings_from_file, _settings_from_env, _settings_from_args,
_rules_from_env, _priority_from_env, _val_from_env
"""

# Generated at 2022-06-14 08:40:03.846841
# Unit test for method init of class Settings
def test_Settings_init():
    from .logs import exception

    settings = Settings()
    with Path('/tmp/settings.py').open(mode='w') as settings_file:
        settings_file.write(const.SETTINGS_HEADER)
        for setting in const.DEFAULT_SETTINGS.items():
            settings_file.write(u'# {} = {}\n'.format(*setting))
    os.environ['LANG'] = 'ru'
    os.environ['WAIT_COMMAND'] = '2'
    os.environ['DEBUG'] = 'True'
    os.environ['REQUIRE_CONFIRMATION'] = 'False'
    os.environ['WAIT_SLOW_COMMAND'] = '1'
    os.environ['HISTORY_LIMIT'] = '5'
    os.environ

# Generated at 2022-06-14 08:40:08.185952
# Unit test for method init of class Settings
def test_Settings_init():
    old_user_dir = settings.user_dir
    settings.init()
    assert settings.user_dir == old_user_dir
    assert settings.user_dir == settings._get_user_dir_path()
    settings.init(args=None)
    settings.init(args=type('', (), {'yes': False, 'debug': False, 'repeat': False})())
