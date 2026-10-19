

# Generated at 2022-06-14 09:04:01.646249
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .corrector import CorrectedCommand

    corrected_command = CorrectedCommand(u"git status -s", u"git status -suno")
    show_corrected_command(corrected_command)

    assert sys.stderr.getvalue() == "!{}git status -suno\n".format(const.USER_COMMAND_MARK)

# Generated at 2022-06-14 09:04:03.456375
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)


# Generated at 2022-06-14 09:04:05.853847
# Unit test for function confirm_text
def test_confirm_text():
    from thefuck.shells.bash import Bash
    corrected_command = Bash("echo 123", "pb").script

    confirm_text(corrected_command)

# Generated at 2022-06-14 09:04:08.321558
# Unit test for function debug
def test_debug():
    settings.debug = True
    assert debug(u'foo') is None
    assert debug(u'foo') is None

# Generated at 2022-06-14 09:04:10.454128
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from datetime import datetime
    from .command import Command
    show_corrected_command(Command('ls', 'ls -F', datetime.now()))

# Generated at 2022-06-14 09:04:13.797558
# Unit test for function debug
def test_debug():
    settings.debug=True
    debug('Debug message')
    settings.debug=False
    debug('Debug message')


# Generated at 2022-06-14 09:04:20.698997
# Unit test for function debug
def test_debug():
    from .tests.utils import capture_stderr
    with capture_stderr() as stderr:
        debug(u'foo')
        debug(u'bar')
    assert stderr == u'\x1b[1mDEBUG:\x1b[0m foo\n\x1b[1mDEBUG:\x1b[0m bar\n'



# Generated at 2022-06-14 09:04:26.313757
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text(CorrectedCommand('foo', False)) == u'{prefix}foo [{green}enter{reset}/{blue}↑{reset}/{blue}↓{reset}/{red}ctrl+c{reset}]'
    assert confirm_text(CorrectedCommand('foo bar', False)) == u'{prefix}foo bar [{green}enter{reset}/{blue}↑{reset}/{blue}↓{reset}/{red}ctrl+c{reset}]'
    assert confirm_text(CorrectedCommand('foo', True)) == u'{prefix}foo (+side effect) [{green}enter{reset}/{blue}↑{reset}/{blue}↓{reset}/{red}ctrl+c{reset}]'

# Generated at 2022-06-14 09:04:29.459378
# Unit test for function debug
def test_debug():
    sys.stderr = out = open('/dev/null', 'w')
    debug('foo')
    assert out.closed
    assert not out.fileno()

# Generated at 2022-06-14 09:04:42.853052
# Unit test for function show_corrected_command
def test_show_corrected_command():
    def assert_is_correct(expected, corrected_command):
        buff = sys.stderr.write
        sys.stderr.write = lambda _: None
        try:
            show_corrected_command(corrected_command)
        finally:
            sys.stderr.write = buff
            try:
                assert expected == sys.stderr.getvalue()
            except:
                print('expected: ' + expected)
                print('got:      ' + sys.stderr.getvalue())
                raise
    assert_is_correct('&lt;@&gt; ls /foo/bar\n',
                      Command('ls /foo/bar', ''))
    assert_is_correct('&lt;@&gt; sudo ls /foo/bar\n',
                      Command('sudo ls /foo/bar', ''))
   

# Generated at 2022-06-14 09:05:00.465563
# Unit test for function show_corrected_command
def test_show_corrected_command():
    """Test show_corrected_command function"""

    from .shells import Shell

    shell = Shell()
    command = u'l'
    # construct the corrected_command
    corrected_command = shell.get_command_from_history(command)
    # call function show_corrected_command and catch the output
    _output = sys.stderr
    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO
    sys.stderr = StringIO()
    show_corrected_command(corrected_command)
    output = sys.stderr.getvalue().strip()
    # set output to console
    sys.stderr = _output

    # assert if the output is correct
    assert output == const.USER_COMMAND_MARK + u'ls'

# Generated at 2022-06-14 09:05:07.958935
# Unit test for function debug_time
def test_debug_time():
    import mock

    with mock.patch('thefuck.shells.utils.debug') as debug:
        with debug_time(u'test'):
            pass
        debug.assert_called_once_with(u'test took: 0:00:00')

# Generated at 2022-06-14 09:05:12.943961
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text('git push -f') == '    git push -f [enter/↑/↓/ctrl+c]'
    assert confirm_text('git pull') == '\033[1K\r    git pull [enter/↑/↓/ctrl+c]'

# Generated at 2022-06-14 09:05:17.279899
# Unit test for function confirm_text
def test_confirm_text():
    p =  confirm_text
    assert p('git checkout feature') ==u'{prefix}git checkout feature [{green}enter{reset}/{blue}↑{reset}/{blue}↓{reset}/{red}ctrl+c{reset}]'

# Generated at 2022-06-14 09:05:21.961793
# Unit test for function debug
def test_debug():
    """
    Unit test for `debug` function.
    """
    settings.debug = True
    assert debug('hello') == None
    assert debug('hello') == None
    assert debug('hello') == None
    settings.debug = False
    assert debug('hello') == None
    assert debug('hello') == None
    assert debug('hello') == None


# Generated at 2022-06-14 09:05:25.434080
# Unit test for function debug_time
def test_debug_time():

    try:
        with debug_time('test'):
            pass
    except Exception as e:
        assert False, u'Failed with: {}'.format(e)

# Generated at 2022-06-14 09:05:36.317857
# Unit test for function confirm_text
def test_confirm_text():
    original_stdout = sys.stdout
    sys.stdout = open('/tmp/test_confirm_text', 'w')
    confirm_text(u'foo')
    sys.stdout.flush()
    sys.stdout.close()
    sys.stdout = original_stdout

    with open('/tmp/test_confirm_text') as fd:
        content = fd.read()

    assert(u'foo' in content)
    assert(u'[enter/↑/↓/ctrl+c]' in content)
    assert(u'\033' not in content)

# Generated at 2022-06-14 09:05:41.668274
# Unit test for function show_corrected_command
def test_show_corrected_command():
    def mock_exception(title, exc_info):
        mock_exception.exc_info = exc_info

    def mock_debug(msg):
        mock_debug.msg = msg


# Generated at 2022-06-14 09:05:46.571301
# Unit test for function confirm_text
def test_confirm_text():
    from .shells import Shell
    from .types import CorrectedCommand

    shell = Shell()
    corrected_command = CorrectedCommand(
        'git pull origin master', True, 'git pull --rebase origin master')
    confirm_text(corrected_command)



# Generated at 2022-06-14 09:05:59.608111
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .utils import escape_unix
    from .shells import Shell

    saved_stderr = sys.stderr

# Generated at 2022-06-14 09:06:08.740512
# Unit test for function debug
def test_debug():
    from mock import patch

    with patch('sys.stderr') as stderr:
        debug(u'This is a test')
        stderr.write.assert_called_once_with(u'\x1b[34m\x1b[1mDEBUG:\x1b[0m This is a test\n')

        stderr.reset_mock()
        settings.debug = False
        debug(u'This is a test')
        assert not stderr.write.mock_calls

# Generated at 2022-06-14 09:06:19.987429
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from argparse import Namespace
    corrected_command = Namespace(script='test', side_effect=False)
    show_corrected_command(corrected_command)
    corrected_command.script = 'test1'
    show_corrected_command(corrected_command)
    corrected_command.script = 'test2'
    show_corrected_command(corrected_command)
    corrected_command.script = 'test3'
    show_corrected_command(corrected_command)



# Generated at 2022-06-14 09:06:31.918160
# Unit test for function debug
def test_debug():
    from io import StringIO
    from .application import Application

    class DebugApplication(Application):
        def __init__(self, *args, **kwargs):
            self.debug_output = StringIO()
            super(DebugApplication, self).__init__(*args, **kwargs)

        def get_debug_stream(self):
            stream = self.debug_output
            stream.truncate(0)
            stream.seek(0)
            return stream

        def print_debug(self, *args):
            super(DebugApplication, self).print_debug(*args)
            self.debug_output.flush()

    app = DebugApplication(None, lambda *args: None, [], None)
    app.settings.debug = True
    debug(u'foo')

# Generated at 2022-06-14 09:06:34.205331
# Unit test for function debug
def test_debug():
    settings._debug = True
    debug('test')
    assert open('/tmp/test.log').readline() == 'test\n'
    settings._debug = False



# Generated at 2022-06-14 09:06:45.366712
# Unit test for function confirm_text
def test_confirm_text():
    from thefuck.shells import Bash
    assert confirm_text(Bash('ruby -v', 'echo ruby -v')) == \
        '{prefix}$ ruby -v [{green}enter{reset}/{blue}↑{reset}/' \
        '{blue}↓{reset}/{red}ctrl+c{reset}]'.format(
            prefix=const.USER_COMMAND_MARK,
            green=color(colorama.Fore.GREEN),
            reset=color(colorama.Style.RESET_ALL),
            blue=color(colorama.Fore.BLUE),
            red=color(colorama.Fore.RED))

# Generated at 2022-06-14 09:06:50.911127
# Unit test for function debug_time
def test_debug_time():
    import datetime
    from contextlib import contextmanager
    from mock import patch
    from thefuck.utils import debug_time

    with patch('thefuck.utils.settings') as settings, \
         patch('thefuck.utils.debug') as debug, \
         patch('datetime.datetime', return_value='now'):
        settings.debug = True
        with debug_time('test'):
            pass
    debug.assert_called_once_with('test took: now')



# Generated at 2022-06-14 09:06:53.675172
# Unit test for function debug_time
def test_debug_time():
    import time

    with debug_time('Test task'):
        time.sleep(1)

    assert True

# Generated at 2022-06-14 09:07:02.627415
# Unit test for function confirm_text
def test_confirm_text():
    import os
    import tempfile
    import io
    from . import ui
    stdout = sys.stdout
    sys.stdout = io.BytesIO()

# Generated at 2022-06-14 09:07:09.008354
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    configuration_details = const.ConfigurationDetails(True,
                                                        '~/.bashrc',
                                                        '.bashrc',
                                                        '~/.bashrc',
                                                        "eval $(thefuck --alias)",
                                                        "source ~/.bashrc",
                                                        "source ~/.bashrc")

    sys.argv = ['thefuck']
    how_to_configure_alias(configuration_details)



# Generated at 2022-06-14 09:07:11.629315
# Unit test for function show_corrected_command
def test_show_corrected_command():
    show_corrected_command(corrected_command='git commmit -m "test"')
    assert True

# Generated at 2022-06-14 09:07:22.043780
# Unit test for function debug
def test_debug():
    from mock import patch
    from .conf import settings
    with patch('sys.stderr') as stderr:
        settings.debug = False
        debug('DEBUG')
        assert(not stderr.write.called)

        settings.debug = True
        debug('DEBUG')
        assert(stderr.write.called)

# Generated at 2022-06-14 09:07:23.559991
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text(const.CorrectedCommand('script', False))

# Generated at 2022-06-14 09:07:24.829012
# Unit test for function debug
def test_debug():
    assert debug.__name__ == 'debug'

# Generated at 2022-06-14 09:07:26.763395
# Unit test for function debug_time
def test_debug_time():
    seconds = 0
    with debug_time('test'):
        seconds = 1

    assert seconds == 1

# Generated at 2022-06-14 09:07:27.860005
# Unit test for function color
def test_color():
    assert color('color') == ''

# Generated at 2022-06-14 09:07:29.271299
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text('hello') == 'hello'


# Generated at 2022-06-14 09:07:32.501407
# Unit test for function debug_time
def test_debug_time():
    from mock import patch
    with patch('sys.stderr') as sys_stderr:
        with debug_time('test message'):
            pass
        sys_stderr.write.assert_called_once_with(u'DEBUG: test message took: 0:00:00')

# Generated at 2022-06-14 09:07:35.318449
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .types import CorrectedCommand
    from .utils import _get_user_input
    # save user input from test!!!
    user_input = _get_user_input
    def mocked_input(*args):
        return ''
    _get_user_input = mocked_input
    show_corrected_command(CorrectedCommand(script='ls /tmp', side_effect=True))
    _get_user_input = user_input

# Generated at 2022-06-14 09:07:42.259566
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(
        ConfigurationDetails(
            False,
            False,
            False,
            '~/.bashrc',
            'source ~/.bashrc',
            'alias {}=\'eval $(thefuck $(fc -ln -1))\'\n'.format(const.ALIAS),
            '/etc/bash.bashrc'))

    how_to_configure_alias(
        ConfigurationDetails(
            False,
            False,
            False,
            '/etc/bash.bashrc',
            'source ~/.bashrc',
            'alias {}=\'eval $(thefuck $(fc -ln -1))\'\n'.format(const.ALIAS),
            '~/.bashrc'))


# Generated at 2022-06-14 09:07:53.347050
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .configuration_details import ConfigurationDetails
    global settings
    settings.debug = False
    settings.no_colors = False
    expected = u"""Seems like \x1b[1mfuck\x1b[21m alias isn't configured!
Please put \x1b[1m#eval "$(thefuck --alias)"\x1b[21m in your \x1b[1m/home/birger/.bashrc\x1b[21m and apply changes with \x1b[1msource /home/birger/.bashrc\x1b[21m or restart your shell.
Or run \x1b[1mfuck\x1b[21m a second time to configure it automatically.
More details - https://github.com/nvbn/thefuck#manual-installation"""
    import io

# Generated at 2022-06-14 09:08:05.680217
# Unit test for function color
def test_color():
    from .which import Which

    assert color('foo') == ''

    settings.no_colors = False
    assert color('foo') == 'foo'

    settings.no_colors = True
    Which.support_colors = True
    assert color('foo') == ''

    settings.no_colors = False
    Which.support_colors = True
    assert color('foo') == 'foo'

    Which.support_colors = False
    assert color('foo') == ''

# Generated at 2022-06-14 09:08:08.649411
# Unit test for function color
def test_color():
    assert color(colorama.Fore.RED) == colorama.Fore.RED
    assert color(colorama.Fore.RED) == ''

# Generated at 2022-06-14 09:08:13.156875
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from . import shell

    corrected_command = shell.And(
        script='sudo kate /etc/apt/sources.list',
        side_effect=shell.Print('apt-get update'))

    show_corrected_command(corrected_command)

# Generated at 2022-06-14 09:08:16.543432
# Unit test for function debug_time
def test_debug_time():
    import time

    times = []
    for i in range(10):
        with debug_time("foo") as t:
            time.sleep(0.5)
            times.append(t)

    assert times == [None] * 10

# Generated at 2022-06-14 09:08:29.068038
# Unit test for function debug
def test_debug():
    from mock import call
    from tempfile import NamedTemporaryFile
    from .conf import load_settings
    from .utils import get_closest
    log_file = NamedTemporaryFile()
    settings = load_settings(conf_file=get_closest('settings.py', log_file.name),
                             no_colors=True,
                             alias='fuck',
                             wait_command=True,
                             require_confirmation=False,
                             priority=1000,
                             env={},
                             log_file=log_file.name)
    settings.debug = True
    debug(u'Test debug')
    log_file.seek(0)
    assert log_file.readlines() == [u'DEBUG: Test debug\n']

# Generated at 2022-06-14 09:08:38.787520
# Unit test for function confirm_text
def test_confirm_text():
    import os
    import sys
    import cStringIO

    stream_out = cStringIO.StringIO()
    stream_err = cStringIO.StringIO()

    # Save original streams
    o_stream_out = sys.stdout
    o_stream_err = sys.stderr

    # Associate standard streams with fake streams
    sys.stdout = stream_out
    sys.stderr = stream_err

    # Run a test code
    confirm_text('test_command')

    # Restore original streams
    sys.stdout = o_stream_out
    sys.stderr = o_stream_err

    assert sys.stderr.isatty() == True
    assert stream_err.getvalue() != 'test_command'

    # Test with os.environ, because it doesn't work using sys.stder

# Generated at 2022-06-14 09:08:43.242181
# Unit test for function debug
def test_debug():
    import StringIO
    from .log import _debug
    stderr = StringIO.StringIO()
    _debug('msg', stderr)
    assert stderr.getvalue() == "DEBUG: msg\n"

# Generated at 2022-06-14 09:08:44.498734
# Unit test for function show_corrected_command
def test_show_corrected_command():
    show_corrected_command('test')



# Generated at 2022-06-14 09:08:47.879724
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text('git push origin master') == \
        u'[git] git push origin master [enter/↑/↓/ctrl+c]'



# Generated at 2022-06-14 09:08:51.600368
# Unit test for function debug
def test_debug():
    import mock
    with mock.patch('sys.stderr') as stderr:
        debug('test')
        stderr.write.assert_called_once_with('\x1b[34m\x1b[1mDEBUG:\x1b[0m test\n')

# Generated at 2022-06-14 09:09:08.237215
# Unit test for function debug
def test_debug():
    import sys
    from tests.utils import capture_stderr

    with capture_stderr():
        debug(u'Test message')
    assert sys.stderr.getvalue()[-42:-7] == u'\u001b[34mDEBUG:\u001b[0m Test message', \
        "Debug message wasn't printed"

# Generated at 2022-06-14 09:09:16.019855
# Unit test for function debug_time
def test_debug_time():
    import os
    import time
    import StringIO

    def debug(msg):
        sys.stderr.write(msg)

    def subprocess_call(cmd):
        time.sleep(1)
        os.system(cmd)

    with debug_time('test'):
        subprocess_call('touch /tmp/thefuck-debug-time')

    f = StringIO.StringIO()
    sys.stderr = f
    settings.debug = True

    with debug_time('test'):
        subprocess_call('echo "123"')

    assert f.getvalue() == 'test took: 0:00:01.000001\n'

# Generated at 2022-06-14 09:09:27.687994
# Unit test for function confirm_text
def test_confirm_text():
    from copy import copy
    from .correct import Command
    command = Command('ls -l', 'ls -la')
    correct_output = u'$ ls -l'
    confirm_text(command)
    assert sys.stderr.getvalue().endswith(correct_output)

    sys.stderr.truncate(0)
    confirm_text(command)
    assert sys.stderr.getvalue().endswith(correct_output)

    command = copy(command)
    command.side_effect = True
    correct_output = u'$ ls -l (+side effect)'
    confirm_text(command)
    assert sys.stderr.getvalue().endswith(correct_output)

    sys.stderr.truncate(0)
    confirm_text(command)
    assert sys.st

# Generated at 2022-06-14 09:09:39.188117
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .types import CorrectedCommand
    import os
    import sys

    original_stdout = sys.stdout
    sys.stdout = mystdout = os.fdopen(os.dup(sys.stdout.fileno()), 'w')

    show_corrected_command(CorrectedCommand('Hello', True))
    mystdout.seek(0)
    assert mystdout.read() == 'fuck Hello +side effect\n'

    show_corrected_command(CorrectedCommand('Hello', False))
    mystdout.seek(0)
    assert mystdout.read() == 'fuck Hello\n'

    sys.stdout = original_stdout

# Generated at 2022-06-14 09:09:44.404031
# Unit test for function debug_time
def test_debug_time():
    from unittest import TestCase

    from .conf import settings
    from . import debug

    settings.debug = True

    class DebugTimeTestCase(TestCase):
        def setUp(self):
            settings.debug = True

        def test_debug_time(self):
            with debug.debug_time('foo'):
                pass

# Generated at 2022-06-14 09:09:49.220230
# Unit test for function color
def test_color():
    colorama.init()
    assert color(colorama.Fore.RED) == ''
    settings.no_colors = False
    assert color(colorama.Fore.RED) == colorama.Fore.RED

# Generated at 2022-06-14 09:09:55.595324
# Unit test for function confirm_text
def test_confirm_text():
    # Given
    corrected_command = u'python manage.py runserver'

    # When
    confirm_text(corrected_command)

    # Then
    output = u'$ python manage.py runserver [enter/↑/↓/ctrl+c]'
    sys.stderr.write(u'\n{}\n'.format(output))



# Generated at 2022-06-14 09:10:07.080313
# Unit test for function confirm_text
def test_confirm_text():
    c = colorama.Fore.GREEN
    reset = colorama.Style.RESET_ALL
    assert confirm_text(const.CorrectedCommand(u'fuck', False)) == \
           u'{prefix}\033[1K\r{bold}fuck{reset} [{green}enter{reset}/{blue}↑{reset}/{blue}↓{reset}/{red}ctrl+c{reset}]'.format(
               prefix=const.USER_COMMAND_MARK,
               green=c,
               reset=reset,
               script='fuck',
               blue=colorama.Fore.BLUE,
               red=colorama.Fore.RED,
               side_effect='',
               bold=colorama.Style.BRIGHT)

# Generated at 2022-06-14 09:10:10.126662
# Unit test for function color
def test_color():
    assert color('test') == 'test'
    settings.no_colors = True
    assert color('test') == ''
    settings.no_colors = False

# Generated at 2022-06-14 09:10:17.640662
# Unit test for function debug
def test_debug():
    sys.stderr = sys.__stderr__
    import StringIO
    debug_output = StringIO.StringIO()
    sys.stderr = debug_output

    try:
        debug(u'Проверка')
    finally:
        sys.stderr = sys.__stderr__
        assert u'Проверка' in debug_output.getvalue()

# Generated at 2022-06-14 09:10:35.505512
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .shells import Bash
    from .shells.bash import Command
    from .utils import wrap_command_in_shell
    from .utils import get_corrected_bash_script

    script = "rm -rf /tmp/nonexistent"
    corrected_script = "rmdir /tmp/nonexistent"
    corrected_command = Command(script, corrected_script, False)

    bash = Bash()
    with wrap_command_in_shell(bash, script) as command:
        _, env = bash.get_aliases()
        corrected_command = get_corrected_bash_script(command, env)
        show_corrected_command(corrected_command)


# Generated at 2022-06-14 09:10:48.656572
# Unit test for function confirm_text
def test_confirm_text():
    from mock import patch

    with patch('sys.stderr') as mock_stderr:
        confirm_text(object())

# Generated at 2022-06-14 09:10:49.917963
# Unit test for function show_corrected_command
def test_show_corrected_command():
    pass



# Generated at 2022-06-14 09:10:58.945560
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import StringIO
    import sys
    sys.stderr = StringIO.StringIO()
    show_corrected_command('fuck')
    sys.stderr.write(u'{prefix}{bold}{script}{reset}{side_effect}\n'.format(
        prefix="$",
        script='fuck',
        side_effect=u' (+side effect)',
        bold=color(colorama.Style.BRIGHT),
        reset=color(colorama.Style.RESET_ALL)))


# Generated at 2022-06-14 09:11:02.282264
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text(Command(script='ls', side_effect=True))
    assert sys.stderr.getvalue() == (
        '$ls +side effect [enter/↑/↓/ctrl+c]')

# Generated at 2022-06-14 09:11:11.728699
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import mock
    with mock.patch('sys.stderr') as mock_stderr:
        show_corrected_command(mock.MagicMock(script='script',
                                              side_effect=False))
        mock_stderr.write.assert_called_once_with(
            u'{prefix}{bold}{script}{reset}\n'.format(
                prefix=const.USER_COMMAND_MARK,
                script='script',
                bold=color(colorama.Style.BRIGHT),
                reset=color(colorama.Style.RESET_ALL)))

        show_corrected_command(mock.MagicMock(script='script',
                                              side_effect=True))

# Generated at 2022-06-14 09:11:18.877192
# Unit test for function debug_time
def test_debug_time():
    print("Run this unit-test with args:\n\tpython3 -m thefuck.shells.zsh --debug")
    with debug_time("'" + str(datetime.now()) + "'"): 
        print('Unit test')

# Generated at 2022-06-14 09:11:22.395521
# Unit test for function color
def test_color():
    assert '\x1b[31m' == color(colorama.Fore.RED)

# Generated at 2022-06-14 09:11:26.897385
# Unit test for function show_corrected_command
def test_show_corrected_command():
    sys.stderr = open('test_show_corrected_command.tmp', 'w')
    show_corrected_command('foo')
    assert open('test_show_corrected_command.tmp').read() == '>  foo \n'
    from os import remove
    remove('test_show_corrected_command.tmp')

# Generated at 2022-06-14 09:11:29.211758
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = u'test'
    show_corrected_command(corrected_command)



# Generated at 2022-06-14 09:11:40.177054
# Unit test for function how_to_configure_alias

# Generated at 2022-06-14 09:11:47.185618
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from thefuck.commands import CorrectedCommand
    from thefuck.conf import settings
    from thefuck.utils import colorama

    # test for the case of the colorama is imported
    assert sys.modules.get(colorama.__name__) is colorama
    # test for the case of colors shouldn't be applied
    settings.no_colors = True
    show_corrected_command(CorrectedCommand(script='ls', side_effect=False))
    assert sys.stdout.getvalue() == '$ ls\n'
    sys.stdout.seek(0)
    sys.stdout.truncate(0)
    show_corrected_command(CorrectedCommand(script='ls', side_effect=True))
    assert sys.stdout.getvalue() == '$ ls (+side effect)\n'
    sys.std

# Generated at 2022-06-14 09:11:59.092376
# Unit test for function debug_time
def test_debug_time():
    _debug_time_started = None
    _debug_time_msg = None

    def debug_time_mock(msg):
        global _debug_time_started
        _debug_time_started = datetime.now()
        global _debug_time_msg
        _debug_time_msg = msg
        yield

    def debug_mock(msg):
        assert u'debug_time_mock' in msg
        assert str(datetime.now() - _debug_time_started) in msg

    settings.debug = True
    old_debug_time = globals()['debug_time']
    old_debug = globals()['debug']
    globals()['debug_time'] = debug_time_mock
    globals()['debug'] = debug_mock

# Generated at 2022-06-14 09:12:13.137534
# Unit test for function debug_time
def test_debug_time():
    from .conf import settings
    from . import const
    from contextlib import contextmanager
    from datetime import datetime
    import sys
    from traceback import format_exception
    import colorama
    from .conf import settings
    from . import const
    import time
    import os

    # Create fake stdout and stderr
    f = open('stdout', 'wb')
    old_stdout, sys.stdout = sys.stdout, f
    g = open('stderr', 'wb')
    old_stderr, sys.stderr = sys.stderr, g

    settings.debug = True

    with debug_time('test'):
        time.sleep(1)

    # Restore stdout and stderr
    sys.stdout = old_stdout
    f.close()

# Generated at 2022-06-14 09:12:16.235851
# Unit test for function debug_time
def test_debug_time():
    """
      >>> settings.debug = True
      >>> with debug_time('foo'): pass
      DEBUG: foo took: 0:00:00.000...
    """



# Generated at 2022-06-14 09:12:19.196444
# Unit test for function color
def test_color():
    assert color(colorama.Fore.RED) == ''
    settings.no_colors = False
    assert color(colorama.Fore.RED) == colorama.Fore.RED

# Generated at 2022-06-14 09:12:24.944855
# Unit test for function debug_time
def test_debug_time():
    # 1. Arrange
    import datetime
    start_time = datetime.datetime.now()
    end_time = datetime.datetime.now()
    duration = end_time - start_time
    msg = "The quick brown fox jumps over the lazy dog"

    # 2. Act
    debug_time(msg)

    # 3. Assert
    # We can't check the exact time, instead we will check the
    # duration appears in the output

# Generated at 2022-06-14 09:12:26.945602
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    with debug_time('took'):
        a = timedelta(seconds=1)

# Generated at 2022-06-14 09:12:28.997731
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    assert(how_to_configure_alias(configuration_details=None) == None)


# Generated at 2022-06-14 09:12:39.573922
# Unit test for function confirm_text
def test_confirm_text():
    import sys
    import StringIO
    sys.stdout = StringIO.StringIO()
    from .conf import settings
    settings.no_colors = False
    from . import output
    output.confirm_text([u'ls'])

# Generated at 2022-06-14 09:12:53.225636
# Unit test for function debug_time
def test_debug_time():
    import time
    id(time)
    with debug_time('test_debug_time'):
        a = 1
        time.sleep(2)
        b = 2



# Generated at 2022-06-14 09:13:02.435211
# Unit test for function debug_time
def test_debug_time():
    from datetime import datetime, timedelta
    class MySettings(object):
        debug = True
    settings.override(MySettings())
    @contextmanager
    def debug_time(msg):
        class Time(object):
            def __init__(self):
                self.time = timedelta(seconds=1)
            def __sub__(self, other):
                return self.time
        started = Time()
        try:
            yield
        finally:
            debug(u'{} took: {}'.format(msg, started - started))
    with debug_time('time'):
        pass

# Generated at 2022-06-14 09:13:04.624370
# Unit test for function color
def test_color():
    assert color('foo') == 'foo'
    settings.no_colors = True
    assert color('foo') == ''

# Generated at 2022-06-14 09:13:07.919976
# Unit test for function color
def test_color():
    assert color('') == ''
    settings.no_colors = True
    assert color('test') == ''
    settings.no_colors = False
    assert color('test') == 'test'



# Generated at 2022-06-14 09:13:10.264482
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
	how_to_configure_alias('hii')
	assert how_to_configure_alias == 'hii'

# Generated at 2022-06-14 09:13:19.276717
# Unit test for function debug_time
def test_debug_time():
    from contextlib import contextmanager
    from datetime import datetime

    class Capture:
        def __init__(self):
            self.output = []

        def write(self, data):
            self.output.append(data)

    with Capture() as captured:
        with debug_time('test'):
            pass

        assert u'test took: 0:00:00' in captured.output[0]

    with Capture() as captured:
        with debug_time('test'):
            sleep(0.01)

        assert u'test took: 0:00:00.0100' in captured.output[0]

# Generated at 2022-06-14 09:13:20.906886
# Unit test for function debug_time
def test_debug_time():
    debug_time(u'test')

# Generated at 2022-06-14 09:13:32.586996
# Unit test for function debug
def test_debug():
    from StringIO import StringIO

    with debug_time('test_debug'):
        pass

    with debug_time('test_debug') as debug:
        pass

    old_stdout = sys.stderr
    sys.stderr = StringIO()

    try:
        debug('test_debug')
    except NameError:
        pass
    else:
        assert False, 'debug function should be undefined'

    if settings.debug:
        debug('test_debug')
        assert sys.stderr.getvalue() == '\x1b[34m\x1b[1m' \
                                        'DEBUG:\x1b[0m test_debug\n'

    sys.stderr = old_stdout

# Generated at 2022-06-14 09:13:36.600430
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)


# Generated at 2022-06-14 09:13:42.874258
# Unit test for function confirm_text
def test_confirm_text():
    from .repository import Command, CorrectedCommand
    from .conf import Config
    config = Config()
    config.no_colors = False
    config.shell = 'zsh'
    correct_command = Command('git log', 'OK', 'git log\n')
    corrected_command = CorrectedCommand(correct_command, correct_command.script, False)
    confirm_text(corrected_command)