

# Generated at 2022-06-14 09:03:53.386916
# Unit test for function debug_time
def test_debug_time():
    import time
    with debug_time('test'):
        time.sleep(1)


if __name__ == '__main__':
    test_debug_time()

# Generated at 2022-06-14 09:03:54.710574
# Unit test for function debug_time
def test_debug_time():
    with debug_time('temp'):
        pass

# Generated at 2022-06-14 09:04:01.952113
# Unit test for function debug_time
def test_debug_time():
    import time
    import mock
    open_mock = mock.mock_open()
    with mock.patch('sys.stderr.write', open_mock):
        with debug_time('test'):
            time.sleep(0.5)
    assert any(u'test took: ' in x[0][0] for x in open_mock.mock_calls)

# Generated at 2022-06-14 09:04:03.588720
# Unit test for function color
def test_color():
    assert color(colorama.Style.DIM) == colorama.Style.DIM
    assert color(colorama.Style.DIM) != ''
    assert color(colorama.Style.DIM) is not None



# Generated at 2022-06-14 09:04:06.404990
# Unit test for function debug_time
def test_debug_time():
    from thefuck.utils import get_time

    @debug_time('do something')
    def test():
        return get_time()

    time = test()
    assert time == 0

# Generated at 2022-06-14 09:04:14.536433
# Unit test for function confirm_text
def test_confirm_text():
    original = sys.stdout
    sys.stdout = open('tests.txt','w')
    sys.stderr.write(u'{prefix}{clear}{script}{reset} {msg}\n'.format(
        prefix='fuck',
        script='vim',
        msg='[enter/↑/↓/ctrl+c]',
        clear='\033[1K\r'))
    txt = open('tests.txt').read()
    sys.stdout.close()
    sys.stdout = original
    assert txt == 'fuck\x1b[1K\rvim [enter/↑/↓/ctrl+c]\n', "confirm_text failed"

# Generated at 2022-06-14 09:04:15.846485
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)

# Generated at 2022-06-14 09:04:17.662256
# Unit test for function debug_time

# Generated at 2022-06-14 09:04:20.505618
# Unit test for function debug_time
def test_debug_time():
    import time
    import random
    print(time)
    with debug_time('test'):
        print(random.randint(1, 1000))

# Generated at 2022-06-14 09:04:26.275814
# Unit test for function debug
def test_debug():
    import sys
    import StringIO
    class TestCase(unittest.TestCase):
        def setUp(self):
            self.tempbuf = StringIO.StringIO()
            self.oldstderr = sys.stderr
            sys.stderr = self.tempbuf

        def tearDown(self):
            sys.stderr = self.oldstderr

        def test_debug(self):
            settings.debug = True
            debug(u'привет')
            self.assertTrue(u'привет' in self.tempbuf.getvalue())
            settings.debug = False
            debug(u'привет')
            self.assertFalse(u'привет' in self.tempbuf.getvalue())

    import unittest

# Generated at 2022-06-14 09:04:32.973746
# Unit test for function color
def test_color():
    assert color('\x1b[32m') == '\x1b[32m'
    settings.no_colors = True
    assert color('\x1b[32m') == ''

# Generated at 2022-06-14 09:04:40.155975
# Unit test for function debug
def test_debug():
    class Logger(object):
        def __init__(self):
            self.log = []

        def write(self, msg):
            self.log.append(msg)

        def writelines(self, msg):
            self.log.append(msg)
    logger = Logger()
    old_error = sys.stderr
    sys.stderr = logger
    debug('test message')
    sys.stderr = old_error
    assert logger.log[0] == u'\x1b[94m\x1b[1mDEBUG:\x1b[0m test message\n'

# Generated at 2022-06-14 09:04:46.345089
# Unit test for function debug_time
def test_debug_time():
    from .main import get_aliases
    from .utils import get_closest

    debug_time('get aliases')
    get_aliases()
    debug_time('get closest')
    get_closest('fuck')
    debug_time('get closest')
    get_closest('fuck it')

# Generated at 2022-06-14 09:04:56.711895
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    const.USER_CONFIG_PATH = ''
    const.USER_ALIAS = ''
    const.AUTO_CONFIGURABLE_SHELLS = ['shell']

    configuration_details = namedtuple(
        'ConfigDetails',
        ['can_configure_automatically',
         'content',
         'path',
         'reload'])

    configuration_details.can_configure_automatically = True
    configuration_details.content = 'content'
    configuration_details.path = 'path'
    configuration_details.reload = 'reload'

    how_to_configure_alias(configuration_details)



# Generated at 2022-06-14 09:05:05.407366
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    from .utils import wrap_retry
    from .conf import Config
    from .rules import Rule
    from .parser import Command
    from .command_runner import CommandRunner

    fake_output_patcher = 'fake_output_patcher'

    config = Config(
        rules={Rule(name='a',
                    match='',
                    script='',
                    get_new_command=lambda x: x)},
        no_colors=True,
        debug=True,
        alias='f',
        wait_command=False,
        wait_slow_command=timedelta(seconds=1),
        priority={'a': 1},
        history_limit=0)


# Generated at 2022-06-14 09:05:10.197079
# Unit test for function confirm_text
def test_confirm_text():
    class command(object):
        def __init__(self, script, side_effect):
            self.script = script
            self.side_effect = side_effect

    confirm_text(command('git commit', False))

# Generated at 2022-06-14 09:05:17.530030
# Unit test for function confirm_text
def test_confirm_text():
    import os
    import shutil
    import tempfile
    from .shells.bash import Bash
    from .shells.zsh import Zsh
    from .shells.fish import Fish

    def get_confirm_text(shell_type, script, side_effect=False, clear=True):
        # Create temp file
        temp_dir = tempfile.mkdtemp()
        temp_file = open(os.path.join(temp_dir, 'fuck'), 'w')
        temp_file.close()

        # Create shell with temp hell
        shell = shell_type(path=temp_file.name)

        # Cleanup temp dir
        shutil.rmtree(temp_dir)

        # Get confirm text
        corrected_command = shell.from_shell(script, side_effect)
        return shell._get_confirm

# Generated at 2022-06-14 09:05:21.646483
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .configuration_details import ConfigurationDetails
    configuration_details = ConfigurationDetails(
        path='.bashrc',
        content='OK',
        reload='RELOAD',
        can_configure_automatically=False)
    how_to_configure_alias(configuration_details)
    assert(True)



# Generated at 2022-06-14 09:05:25.632866
# Unit test for function confirm_text
def test_confirm_text():
    # TODO: read unicode test string from file
    # TODO: read function output to variable and compare it with expectations
    pass

if __name__ == '__main__':
    test_confirm_text()

# Generated at 2022-06-14 09:05:38.145722
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .utils import HowToConfigureAlias
    from .conf import ConfigurationDetails
    from . import const
    import os
    import platform
    configuration_details = None
    if os.name == 'posix' and platform.system() != 'Linux':
        configuration_details = HowToConfigureAlias.CreatePosix(const.DEFAULT_SHELL, const.DEFAULT_SHELL, '')
    elif os.name == 'posix' and platform.system() == 'Linux':
        configuration_details = HowToConfigureAlias.CreateLinux(const.DEFAULT_SHELL, const.DEFAULT_SHELL, '')
    else:
        configuration_details = HowToConfigureAlias.CreateWindows(const.DEFAULT_SHELL, const.DEFAULT_SHELL, '')

# Generated at 2022-06-14 09:05:42.094705
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)

# Generated at 2022-06-14 09:05:50.795201
# Unit test for function debug
def test_debug():
    from tempfile import NamedTemporaryFile
    from re import search

    with NamedTemporaryFile() as tmp:
        settings.debug_to_file = tmp.name
        debug(u'функция debug')
        tmp.seek(0)
        assert search(u'функция debug', tmp.read())

    settings.debug_to_file = False
    debug(u'функция debug')

# Generated at 2022-06-14 09:05:57.960993
# Unit test for function debug
def test_debug():
    from mock import Mock
    from .conf import settings as _settings
    settings = Mock(_settings)
    settings.debug = True

    with Mock() as mock_stderr:
        sys.stderr = mock_stderr
        debug(u'test')
    mock_stderr.write.assert_called_with(u'test\n')

    with Mock() as mock_stderr:
        sys.stderr = mock_stderr
        settings.debug = False
        debug(u'test')
    assert not mock_stderr.write.called

# Generated at 2022-06-14 09:06:08.829691
# Unit test for function debug
def test_debug():
    from pytest import fixture

    @fixture
    def debug_patch(monkeypatch):
        debug_patch = []
        monkeypatch.setattr('sys.stderr.write',
                            lambda msg: debug_patch.append(msg))
        return debug_patch

    def test_debug_if_settings_debug_enabled(debug_patch):
        settings.debug = True
        debug('foo')
        assert debug_patch == [u'DEBUG: foo\n']

    def test_no_debug_if_settings_debug_disabled(debug_patch):
        settings.debug = False
        debug('foo')
        assert debug_patch == []

# Generated at 2022-06-14 09:06:11.615315
# Unit test for function show_corrected_command
def test_show_corrected_command():
    assert show_corrected_command(['echo', 'hello', 'ye'])

# Generated at 2022-06-14 09:06:17.195359
# Unit test for function confirm_text
def test_confirm_text():
    from .shells import Shell
    from .correct import CorrectedCommand

    confirm_text(CorrectedCommand('ls', side_effect=False))

    Shell.init(lambda: 'ls', lambda _: None)
    Shell.get_executor().get_alias = lambda _: 'fuck'
    confirm_text(CorrectedCommand('ls', side_effect=True))

# Generated at 2022-06-14 09:06:27.971031
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text('hello') == u'[0/1/2/3/anyother]hello'
    assert confirm_text(1) == u'[0/1/2/3/anyother]1'
    assert confirm_text(1.1) == u'[0/1/2/3/anyother]1.1'

# Generated at 2022-06-14 09:06:30.217966
# Unit test for function color
def test_color():
    assert '\x1b[31m' == color(colorama.Fore.RED)
    assert not color(colorama.Fore.RED)


colorama.init()

# Generated at 2022-06-14 09:06:34.204566
# Unit test for function debug
def test_debug():
    # We can't to check sys.stderr.write in output because line end
    # depends on platform.
    msg = u'Test debug message'
    debug(msg)
    assert sys.stderr.getvalue().endswith(u'DEBUG: {}\n'.format(msg))



# Generated at 2022-06-14 09:06:47.145543
# Unit test for function confirm_text
def test_confirm_text():
    import mock
    from thefuck.shells import Bash, Zsh
    from thefuck.utils import CorrectedCommand, confirm_text

    assert len(Bash('ls').get_history()) == 0
    with mock.patch('thefuck.utils.sys.stdout', mock.MagicMock()):
        confirm_text('ls')
    assert len(Bash('ls').get_history()) == 1

    assert len(Zsh('ls').get_history()) == 0
    with mock.patch('thefuck.utils.sys.stdout', mock.MagicMock()):
        confirm_text('ls')
    assert len(Zsh('ls').get_history()) == 1

    assert len(Bash('ls').get_history()) == 1

# Generated at 2022-06-14 09:06:58.175256
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .shells import Shell
    from .command import Command
    import io
    import sys

    sys.stderr = io.StringIO()
    show_corrected_command(Command(script='ls -l', side_effect=True))

    assert sys.stderr.getvalue() == u'{prefix}ls -l (+side effect)\n'.format(prefix=const.USER_COMMAND_MARK)

    sys.stderr.close()
    sys.stderr = sys.__stderr__

# Generated at 2022-06-14 09:06:59.627554
# Unit test for function debug
def test_debug():
    debug('Привет')



# Generated at 2022-06-14 09:07:01.964537
# Unit test for function color
def test_color():
    assert color('red') == ''
    settings.no_colors = False
    assert color('red') == '\x1b[31m'



# Generated at 2022-06-14 09:07:11.320685
# Unit test for function confirm_text
def test_confirm_text():
    # Required because sys.stderr is not closed and we need to reset STD_ERR
    # after our tests
    old_stderr = sys.stderr

    # NOTE: We need to mock the output of sys.stderr so we can test the
    # function. But... sys.stderr.write returns 'None' so we need to
    # create our own version of sys.stderr.write which we can mock.
    class MockOutput(object):
        def __init__(self):
            self.content = []

        def write(self, s):
            self.content.append(s)

        def __getattr__(self, attr):
            return getattr(sys.stderr, attr)

    # Create instance of mock object. This will be used to test the function
    mock_io = Mock

# Generated at 2022-06-14 09:07:21.929744
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from StringIO import StringIO
    import sys, os
    try:
        import colorama
    except ImportError:
        pass

    def reset_stdout():
        sys.stdout = sys.__stdout__

    def get_stdout():
        return sys.__stdout__

    stdout = StringIO()

# Generated at 2022-06-14 09:07:31.460511
# Unit test for function confirm_text
def test_confirm_text():
    expected = "\r\033[1K\x1b[37mfuck\x1b[0m \x1b[37m\x1b[1mtest\x1b[0m \x1b[32menter\x1b[0m/\x1b[34m↑\x1b[0m/\x1b[34m↓\x1b[0m/\x1b[31mctrl+c\x1b[0m]"
    actual = confirm_text('test')
    assert expected == actual

# Generated at 2022-06-14 09:07:35.919690
# Unit test for function confirm_text
def test_confirm_text():
    from mock import patch
    with patch('sys.stderr') as mock:
        confirm_text(const.CorrectedCommand('ls', False))
        mock.write.assert_called_with(
            u'$ls [\x1b[32menter\x1b[0m/\x1b[34m↑\x1b[0m/\x1b[34m↓\x1b[0m/\x1b[31mctrl+c\x1b[0m]')

# Generated at 2022-06-14 09:07:39.553657
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = type('', (), {})
    corrected_command.script = 'git push'
    corrected_command.side_effect = False
    show_corrected_command(corrected_command)

# Generated at 2022-06-14 09:07:44.972918
# Unit test for function color
def test_color():
    assert color('red')('red') == '\x1b[31mred\x1b[0m'
    assert settings.no_colors is False
    settings.no_colors = True
    assert color('red')('red') == 'red'
    settings.no_colors = False

# Generated at 2022-06-14 09:07:53.490262
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    from datetime import datetime
    from time import sleep
    from . import settings

    settings.debug = True
    settings.slow_threshold = 0
    test_msg = 'test'
    
    with debug_time(test_msg):
        sleep(1.5)

    start_time = datetime.now()

    with debug_time(test_msg):
        sleep(1.5)

    end_time = datetime.now()

    assert ((end_time - start_time) > timedelta(seconds=1))
    assert settings.debug == True
    assert settings.slow_threshold == 0

# Generated at 2022-06-14 09:07:58.483753
# Unit test for function debug
def test_debug():
    debug('test')
    settings.debug = False
    debug('test')

# Generated at 2022-06-14 09:08:03.570497
# Unit test for function confirm_text
def test_confirm_text():
    test_string = 'ls -lah'
    mock_input = ('ls -lah\n', 'ls -lah\n', 'ls -lah\n\n', 'ls -lah\n\n\n')
    const.input = lambda x: mock_input.pop()
    assert confirm_text(test_string) == 'ls -lah\n'

# Generated at 2022-06-14 09:08:05.790230
# Unit test for function debug_time
def test_debug_time():
    def test_function():
        with debug_time('test'):
            pass
    test_function()

# Generated at 2022-06-14 09:08:10.519140
# Unit test for function debug
def test_debug():
    import io
    temp_stdout = io.StringIO()
    try:
        sys.stderr = temp_stdout
        debug(u'HELLO')
        assert u'HELLO' in temp_stdout.getvalue()
    finally:
        sys.stderr = sys.__stderr__



# Generated at 2022-06-14 09:08:13.806616
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from StringIO import StringIO
    sys.stderr = StringIO()
    show_corrected_command('fuck it')
    sys.stderr.getvalue()

# Generated at 2022-06-14 09:08:20.598642
# Unit test for function color
def test_color():
    assert color(colorama.Back.RED + colorama.Fore.WHITE + colorama.Style.BRIGHT) == ''
    settings.no_colors = False
    assert color(colorama.Back.RED + colorama.Fore.WHITE + colorama.Style.BRIGHT) == colorama.Back.RED + colorama.Fore.WHITE + colorama.Style.BRIGHT

# Generated at 2022-06-14 09:08:31.435184
# Unit test for function debug
def test_debug():
    from unittest import TestCase
    import sys

    class TestDebug(TestCase):

        def setUp(self):
            self.old_stdout = sys.stderr
            self.old_stderr = sys.stderr
            sys.stdout = sys.stderr = self._stdout = self._stderr = open(
                '/dev/null', 'w')

        def tearDown(self):
            sys.stdout = self.old_stdout
            sys.stderr = self.old_stderr

        def test_debug_disabled(self):
            settings.debug = False
            debug(u'some debug')
            self.assertEqual(self._stdout.getvalue(), '')

        def test_debug_enabled(self):
            settings.debug = True

# Generated at 2022-06-14 09:08:33.544470
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(False)
    how_to_configure_alias(True)

# Generated at 2022-06-14 09:08:37.768870
# Unit test for function show_corrected_command
def test_show_corrected_command():
    """Test for function show_corrected_command."""
    sys.stderr = open('log', 'w')
    corrected_command = "ls dir"
    show_corrected_command(corrected_command)



# Generated at 2022-06-14 09:08:42.661789
# Unit test for function color
def test_color():
    colorama.init()
    assert u'Hello' == color(u'Hello')

    settings.no_colors = True
    assert u'' == color(u'World')
    settings.no_colors = False



# Generated at 2022-06-14 09:08:51.770015
# Unit test for function show_corrected_command
def test_show_corrected_command():  # pylint: disable=unused-variable
    from tests.utils import Command

    show_corrected_command(Command('git commit', 'git commit -v'))
    assert const.USER_COMMAND_MARK + 'git commit -v\n' == sys.stderr.getvalue()



# Generated at 2022-06-14 09:08:54.240022
# Unit test for function debug_time
def test_debug_time():
    from mock import MagicMock, call
    debug = MagicMock()
    with debug_time('foo')(debug):
        pass
    debug.assert_has_calls([call('foo took: ')])

# Generated at 2022-06-14 09:08:58.803411
# Unit test for function debug
def test_debug():
    text = "some text"
    debug(text)
    #assert sys.stderr.write.called == True
    #assert sys.stderr.write.called_with == "some text"

# Generated at 2022-06-14 09:09:10.028251
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import os
    import tempfile
    import time
    import subprocess
    from thefuck.conf import Command
    from tests.utils import patch_settings

    with patch_settings(no_colors=True):
        _, temp_file = tempfile.mkstemp()
        with open(temp_file, 'w') as f:
            f.write('1')

        p = subprocess.Popen(['script', '-q', '/dev/null', 'bash'],
                             stdout=subprocess.PIPE,
                             stdin=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             universal_newlines=True)
        time.sleep(.1)

        command = Command(script=u'date', stdout=u'', stderr=u'')


# Generated at 2022-06-14 09:09:12.693408
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = corrected_command = const.CorrectedCommand('fuck',
        False)
    confirm_text(corrected_command)



# Generated at 2022-06-14 09:09:24.102315
# Unit test for function debug
def test_debug():
    from .conf import load_settings
    old_stdout = sys.stderr

    try:
        from StringIO import StringIO
        sys.stderr = StringIO()

        settings = load_settings()
        settings.debug = False
        debug('message')
        assert sys.stderr.getvalue() == ''

        settings.debug = True
        debug('message')
        debug_lines = sys.stderr.getvalue().splitlines()
        assert len(debug_lines) == 1
        assert debug_lines[0].endswith('DEBUG: message')
    finally:
        sys.stderr = old_stdout

# Generated at 2022-06-14 09:09:25.940117
# Unit test for function debug_time
def test_debug_time():
    from time import sleep
    with debug_time('debug'):
        sleep(1)

# Generated at 2022-06-14 09:09:27.956157
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text(u'test') == u'  $ test [enter/↑/↓/ctrl+c] '

# Generated at 2022-06-14 09:09:31.838904
# Unit test for function color
def test_color():
    colorama.init()
    assert color(colorama.Back.RED) == colorama.Back.RED
    settings.no_colors = True
    assert color(colorama.Back.RED) == ''

# Generated at 2022-06-14 09:09:43.153690
# Unit test for function debug
def test_debug():
    class TestStream(object):
        def __init__(self):
            self.msg = ''
            self.is_debug = True

        def write(self, msg):
            self.msg = msg

        def flush(self):
            pass

    test_stream = TestStream()
    real_stderr = sys.stderr
    sys.stderr = test_stream

    try:
        settings.debug = True
        debug("Test Debug")
        assert test_stream.msg == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m Test Debug\n'
    finally:
        sys.stderr = real_stderr

# Generated at 2022-06-14 09:09:53.688210
# Unit test for function debug
def test_debug():
    import mock
    import sys
    check_output = mock.mock_open(read_data=u'some data')
    print(check_output.read_data)
    with mock.patch('thefuck.utils.open', check_output, create=True):
       debug(sys.stderr)
       check_output.assert_called_once_with('thefuck/last_command', 'r')



# Generated at 2022-06-14 09:10:05.633098
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .shells import ConfigurationDetails
    from prettytable import PrettyTable

    # Test no configuration_details
    t = PrettyTable()
    t.field_names = ['input', 'output']
    try:
        how_to_configure_alias(None)
        t.add_row(['how_to_configure_alias(None)', ''])
    except:
        t.add_row(['how_to_configure_alias(None)', 'exception'])

    # Test can_configure_automatically=False
    config_details = ConfigurationDetails()
    config_details.can_configure_automatically = False

# Generated at 2022-06-14 09:10:13.470610
# Unit test for function debug
def test_debug():
    def debug_mock(msg):
        debug_mock.called = msg

    settings.debug = True
    settings.no_colors = True
    try:
        sys.stderr = debug_mock
        debug('foo')
        assert debug_mock.called == u'DEBUG: foo\n'

        settings.no_colors = False
        debug('foo')
        assert debug_mock.called == u'foo\n'
    finally:
        settings.debug = False

# Generated at 2022-06-14 09:10:19.376359
# Unit test for function debug_time
def test_debug_time():
    import mock
    import datetime
    with mock.patch('sys.stderr') as stderr:
        with debug_time('Test'):
            pass
        stderr.write.assert_called_once_with(u'\x1b[34m\x1b[1mDEBUG:\x1b[0m Test took: 0:00:00\n')

# Generated at 2022-06-14 09:10:20.589710
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:10:22.019546
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test_msg'):
        pass

# Generated at 2022-06-14 09:10:27.801162
# Unit test for function debug_time
def test_debug_time():
    import time, datetime
    time.sleep(0.4)
    started = datetime.datetime.now()
    time.sleep(0.2)
    debug_time('test_debug_time')
    assert ((datetime.datetime.now() - started).total_seconds() > 0.3)
    sys.exit(0)

# Generated at 2022-06-14 09:10:32.201736
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    configuration_details = namedtuple('configuration_details', ['can_configure_automatically'])
    configuration_details.can_configure_automatically = True
    assert how_to_configure_alias(configuration_details) == None

# Generated at 2022-06-14 09:10:39.511594
# Unit test for function debug_time
def test_debug_time():
    import datetime
    import time
    with debug_time('start'):
        time.sleep(.001)
    started = datetime.datetime.now()
    with debug_time('test'):
        time.sleep(.001)
    delta = datetime.datetime.now() - started
    assert delta >= datetime.timedelta(.001)

# Generated at 2022-06-14 09:10:42.254135
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .correct import CorrectedCommand
    show_corrected_command(CorrectedCommand('ls', ''))



# Generated at 2022-06-14 09:10:47.800865
# Unit test for function color
def test_color():
    assert color(colorama.Fore.BLUE) == ''
    settings.no_colors = False
    assert color(colorama.Fore.BLUE) == colorama.Fore.BLUE

# Generated at 2022-06-14 09:10:53.376797
# Unit test for function color
def test_color():
    assert color('') == ''
    assert const.NO_COLORS_ENV in os.environ
    os.environ.pop(const.NO_COLORS_ENV)
    assert color('\x1b[31mfoo') == '\x1b[31mfoo'

# Generated at 2022-06-14 09:10:55.901493
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text(const.CorrectedCommand(u'echo oops!', False)) == u'fuck oops! [enter/↑/↓/ctrl+c]'

# Generated at 2022-06-14 09:11:03.347785
# Unit test for function confirm_text
def test_confirm_text():
    import pytest
    from mock import patch

    with patch('sys.stderr.write') as mock:
        confirm_text(
            corrected_command=CorrectedCommand('script', True))
        assert mock.called
        args, kwargs = mock.call_args
        assert const.USER_COMMAND_MARK in args[0]
        assert 'script' in args[0]
        assert '+side effect' in args[0]



# Generated at 2022-06-14 09:11:12.133484
# Unit test for function debug
def test_debug():
    import sys
    import StringIO

    if sys.version_info[0] == 2:
        from mock import Mock
    else:
        from unittest.mock import Mock
    from . import debug as debug_function

    settings.debug = True
    stderr = sys.stderr

# Generated at 2022-06-14 09:11:23.025176
# Unit test for function debug_time
def test_debug_time():
    import mock

    with mock.patch('datetime.datetime') as mock_datetime:
        mock_datetime.now.side_effect = range(10)

        with mock.patch('sys.stderr') as mock_stderr:
            with debug_time('test_msg'):
                pass

            assert mock_stderr.write.call_args_list == [
                mock.call('test_msg took: 0\n')]



# Generated at 2022-06-14 09:11:29.994660
# Unit test for function confirm_text
def test_confirm_text():
    from thefuck.rules.git_branch import match, get_new_command
    from thefuck.shells import Shell
    from thefuck.main import confirm
    from mock import patch
    from six.moves import input as mock_input

    def confirm(rule, new_command):
        assert new_command == 'git checkout master'
        return True

    def mock_input(confirm_text):
        assert confirm_text == (const.USER_COMMAND_MARK + 'git chechkut master '
                                '[\x1b[32menter\x1b[0m/\x1b[34m↑\x1b[0m/\x1b[34m↓\x1b[0m/\x1b[31mctrl+c\x1b[0m]')
        return ''

# Generated at 2022-06-14 09:11:33.573616
# Unit test for function color
def test_color():
    assert settings.no_colors is False
    assert color('') == ''
    settings.no_colors = True
    assert color('') == ''
    settings.no_colors = False

# Generated at 2022-06-14 09:11:44.478187
# Unit test for function debug
def test_debug():
    def test_output_with_settings(settings):
        output = []
        settings.debug = True

        def write(string):
            output.append(string)
        settings.print_result = write
        debug('lol')
        assert output == [
            '\x1b[34m\x1b[1mDEBUG:\x1b[0m lol\n']

        settings.debug = False
        del output[:]
        debug('lol')
        assert output == []

    with settings.mocked_context(), settings.mocked_modules(
            'colorama') as mocked:
        mocked.Fore.BLUE = 'BLUE'
        mocked.Style.BRIGHT = 'BRIGHT'
        mocked.Style.RESET_ALL = 'RESET_ALL'
        test_output_with_settings(settings)


# Unit

# Generated at 2022-06-14 09:11:46.149618
# Unit test for function debug
def test_debug():
    debug('debugging')



# Generated at 2022-06-14 09:11:59.787902
# Unit test for function confirm_text
def test_confirm_text():
    import os
    import tempfile
    from collections import namedtuple

    file = tempfile.NamedTemporaryFile(delete=False)
    file.close()

# Generated at 2022-06-14 09:12:02.635454
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .types import CorrectedCommand
    show_corrected_command(CorrectedCommand('ls .', ''))



# Generated at 2022-06-14 09:12:10.875139
# Unit test for function confirm_text
def test_confirm_text():
    from tempfile import NamedTemporaryFile
    from os import remove

    with NamedTemporaryFile() as f:
        sys.stderr = f
        command = 'ls -la'
        confirm_text(command)
        f.seek(0)
        output = f.read()
        confirm_text('python')
        assert ('[enter/↑/↓/ctrl+c]' in output) == True

# Generated at 2022-06-14 09:12:16.357943
# Unit test for function show_corrected_command
def test_show_corrected_command():
    class Command():
        def __init__(self, script, side_effect):
            self.script = script
            self.side_effect = side_effect
    show_corrected_command(Command(script='ls', side_effect=True))


# Generated at 2022-06-14 09:12:18.409569
# Unit test for function color
def test_color():
    assert color('test') == 'test'
    settings.no_colors = True
    assert color('test') == ''

# Generated at 2022-06-14 09:12:19.541524
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:12:22.536522
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test debug_time'):
        pass


# Generated at 2022-06-14 09:12:26.657911
# Unit test for function confirm_text
def test_confirm_text():
    old = sys.stderr
    sys.stderr = sys.stdout
    try:
        confirm_text('git commit -a')
        confirm_text('git commit')
    finally:
        sys.stderr = old


# Generated at 2022-06-14 09:12:36.262439
# Unit test for function debug_time
def test_debug_time():
    class Test(object):
        def __init__(self):
            self.vals = []

        def write(self, x):
            self.vals.append(x)

    class TestSettings(object):
        def __init__(self, debug):
            self.debug = debug

    with Test() as test:
        sys.stderr = test

        with debug_time('test'):
            pass

        settings = TestSettings(True)

        with debug_time('test'):
            pass

        assert test.vals == ['DEBUG: test took: 0:00:00.000112\n',
                             'DEBUG: test took: 0:00:00.000037\n']

# Generated at 2022-06-14 09:12:41.374191
# Unit test for function debug
def test_debug():
    settings.debug = True
    sys.stderr = open('/dev/null', 'w')
    debug('test debug message')


if __name__ == '__main__':
    test_debug()

# Generated at 2022-06-14 09:12:47.661593
# Unit test for function confirm_text
def test_confirm_text():
    assert ("f " == confirm_text(['f']))
    assert ("f " == confirm_text(['f', 'a']))
    assert ("f " == confirm_text(['f', 'a', 'b']))

# Generated at 2022-06-14 09:12:49.576823
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text(const.CorrectedCommand(u'git push origin master', True))

# Generated at 2022-06-14 09:12:50.605230
# Unit test for function debug
def test_debug():
    debug(u'foo')

# Generated at 2022-06-14 09:12:52.727520
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .shells import Command
    show_corrected_command(Command('test', '', ''))

# Generated at 2022-06-14 09:13:04.942830
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    from unittest import mock
    from functools import partial

    # Temporarily mock debug function
    debug_mock = mock.MagicMock()
    original_debug = debug
    debug = debug_mock

    with debug_time('foo'):
        pass

    assert debug_mock.call_count == 1
    assert debug_mock.call_args[0][0].startswith('foo took')

    fake_now = partial(lambda: datetime.now() + timedelta(seconds=60))
    with mock.patch('datetime.datetime.now', side_effect=fake_now):
        with debug_time('foo'):
            pass

    assert debug_mock.call_count == 2

# Generated at 2022-06-14 09:13:07.000346
# Unit test for function debug
def test_debug():
    assert debug('foo') \
           == sys.stderr.write(u'foo\n')

# Generated at 2022-06-14 09:13:13.869000
# Unit test for function debug
def test_debug():
    import StringIO
    sys.stderr = StringIO.StringIO()
    settings.debug = True
    debug(u'foobar')
    assert sys.stderr.getvalue() == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m foobar\n'


if __name__ == '__main__':
    test_debug()

# Generated at 2022-06-14 09:13:15.490013
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)



# Generated at 2022-06-14 09:13:18.781520
# Unit test for function confirm_text
def test_confirm_text():
    show_corrected_command("corrected_command") == u'\033[1K\rfuck corrected_command'

if __name__ == '__main__':
    test_confirm_text()

# Generated at 2022-06-14 09:13:21.615496
# Unit test for function color
def test_color():
    assert color('red') == ''

    settings.no_colors = False
    assert color('red') == 'red'

# Generated at 2022-06-14 09:13:29.837268
# Unit test for function confirm_text
def test_confirm_text():
    corrected_script = 'ls -a'
    correct_line = const.USER_COMMAND_MARK + corrected_script
    confirm_text(corrected_script)
    assert sys.stderr.getvalue() == correct_line + \
                                   ' [\x1b[32menter\x1b[0m/\x1b[34m\x1b[1m↑\x1b[0m/\x1b[34m\x1b[1m↓\x1b[0m/\x1b[31mctrl+c\x1b[0m]'
    sys.stderr.flush()

# Generated at 2022-06-14 09:13:31.654942
# Unit test for function color
def test_color():
    assert '\x1b[31m' == color(colorama.Fore.RED)



# Generated at 2022-06-14 09:13:38.202494
# Unit test for function debug_time
def test_debug_time():
    def test_func(msg):
        with debug_time(msg):
            import time
            time.sleep(0.5)

    import StringIO
    from contextlib import contextmanager

    @contextmanager
    def capture():
        old_stdout, old_stderr, old_sdterr = sys.stdout, sys.stderr, sys.stderr
        try:
            sys.stdout, sys.stderr, sys.stderr = StringIO.StringIO(), StringIO.StringIO(), StringIO.StringIO()
            yield sys.stdout, sys.stderr, sys.stderr
        finally:
            sys.stdout, sys.stderr, sys.stderr = old_stdout, old_stderr, old_sdterr


# Generated at 2022-06-14 09:13:49.484101
# Unit test for function debug
def test_debug():
    from StringIO import StringIO
    from datetime import datetime
    debug('debug message')
    assert sys.stderr.getvalue() == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m debug message\n'