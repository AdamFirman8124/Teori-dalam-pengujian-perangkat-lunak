

# Generated at 2022-06-14 09:04:05.165809
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = 'ls'
    side_effect = False
    prefix = '> '

    confirm_text(corrected_command, side_effect, prefix)
    assert sys.stderr.write.called
    assert sys.stderr.write.call_args[0][0] == \
           u'> {clear}{bold}ls{reset} {green}enter{reset}/{blue}↑{reset}/{blue}↓{reset}/{red}ctrl+c{reset}'  # noqa

    corrected_command = 'ls'
    side_effect = True
    prefix = '> '

    confirm_text(corrected_command, side_effect, prefix)
    assert sys.stderr.write.called
    assert sys.stderr.write.call_args_list[1][0][0]

# Generated at 2022-06-14 09:04:11.848664
# Unit test for function debug_time
def test_debug_time():
    import os, time

    # Create temporary file
    tmp_file = '/tmp/test_debug_time_tmp'
    with open(tmp_file, 'w') as f:
        f.write('test')

    # Remove temporary file
    with debug_time('Remove temporary file'):
        os.remove(tmp_file)

    # Wait one second
    with debug_time('Wait one second'):
        time.sleep(1)

    os.remove(tmp_file)

# Generated at 2022-06-14 09:04:13.462789
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)
    assert True

# Generated at 2022-06-14 09:04:24.703915
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    print(u'''Seems like {bold}fuck{reset} alias isn't configured!

Please put {bold}{content}{reset} in your {bold}{path}{reset} and apply changes with {bold}{reload}{reset} or restart your shell.

Or run {bold}fuck{reset} a second time to configure it automatically.

More details - https://github.com/nvbn/thefuck#manual-installation
'''.format(
        bold=color(colorama.Style.BRIGHT),
        reset=color(colorama.Style.RESET_ALL),
        path=u'/home/nvbn/.bashrc',
        content=u'eval $(thefuck --alias)',
        reload=u'eval $(thefuck --alias)'))



# Generated at 2022-06-14 09:04:28.062603
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    from nose.tools import assert_less

    with debug_time('test'):
        pass

    with debug_time('test'):
        assert_less(timedelta(seconds=1),
                    debug_time.func_dict['t'])



# Generated at 2022-06-14 09:04:33.023390
# Unit test for function confirm_text
def test_confirm_text():
    """test confirm_text"""
    class CorrectedCommand(object):
        """create class CorrectedCommand"""
        def __init__(self, script, side_effect):
            self.script = script
            self.side_effect = side_effect
    confirm_text(CorrectedCommand('test', True))

# Generated at 2022-06-14 09:04:45.174560
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .shells.bash import Bash
    from .shells import get_shell_info

    shell_info = get_shell_info(Bash())
    configuration_details = shell_info.configuration_details

    print("Break point 1")
    print("Expected output:")
    print("Seems like fuck alias isn't configured!")
    print("Please put alias fuck='eval $(thefuck $(fc -ln -1)); history -r' in your"
          " /Users/lyk323/.bash_profile and apply changes with source /Users/lyk323/.bash_profile or restart your shell.")
    print("Or run fuck a second time to configure it automatically.")
    print("More details - https://github.com/nvbn/thefuck#manual-installation")

    how_to_configure_alias(configuration_details)




# Generated at 2022-06-14 09:05:00.195485
# Unit test for function debug
def test_debug():
    from mock import patch
    from .conf import settings
    from . import log

    settings.debug = False
    with patch('os.environ.copy', return_value={'TF_SHELL': 'bash'}):
        with patch('sys.stderr.write') as write:
            log.debug('msg')
            write.assert_not_called()

    settings.debug = True
    with patch('os.environ.copy', return_value={'TF_SHELL': 'bash'}):
        with patch('sys.stderr.write') as write:
            log.debug('msg')
            write.assert_called_with('\x1b[34m\x1b[1mDEBUG:\x1b[0m msg\n')


# Generated at 2022-06-14 09:05:09.664381
# Unit test for function debug_time
def test_debug_time():
    import time
    import StringIO
    stream = StringIO.StringIO()
    try:
        old_stream = sys.stderr
        sys.stderr = stream
        with debug_time('time'):
            time.sleep(0.03)
    finally:
        sys.stderr = old_stream
    assert 'time took:' in stream.getvalue()

# Generated at 2022-06-14 09:05:13.021769
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import TheFuck
    corrected_command = TheFuck.corrected_command.CorrectedCommand(
        TheFuck.corrected_command.Command('ls', '', ''),
        ['ls', '-la'], False)
    show_corrected_command(corrected_command)



# Generated at 2022-06-14 09:05:22.693008
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from thefuck.types import CorrectedCommand
    show_corrected_command(
        CorrectedCommand(u'git push', True)) ==\
        u'{}git push{} (+side effect)'.format(const.USER_COMMAND_MARK,
                                              color(colorama.Style.RESET_ALL))
    show_corrected_command(
        CorrectedCommand(u'git push', False)) ==\
        u'{}git push'.format(const.USER_COMMAND_MARK)



# Generated at 2022-06-14 09:05:26.143013
# Unit test for function color
def test_color():
    assert color('', get_output=True) == ''
    with settings.override('no_colors', True):
        assert color('', get_output=True) == ''



# Generated at 2022-06-14 09:05:29.829237
# Unit test for function confirm_text
def test_confirm_text():
    class CorrectedCommand(object):
        def __init__(self, script):
            self.script = script
            self.side_effect = False
    confirm_text(CorrectedCommand('git push'))

# Generated at 2022-06-14 09:05:42.493447
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .shells import Shell
    from thefuck.rules.git_branch_checkout import match, get_new_command
    from thefuck.types import Command
    from datetime import datetime

    settings.no_colors = False
    settings.wait_command = False
    settings.fast_mode = True
    settings.require_confirmation = False
    settings.repeat = False
    settings.wait_slow_command = 3
    settings.history_limit = None
    settings.priority = {}
    settings.rules = [
        ('git', 'branch_checkout', match, get_new_command)]
    settings.alias = 'fuck'
    settings.exclude_rules = []
    settings.env = {}
    settings.shell = Shell.from_shell(settings.shell)

# Generated at 2022-06-14 09:05:48.624093
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .shells import ShellType
    configuration_details = ShellType(
        name='bash',
        path='.bashrc',
        content='eval $(thefuck --alias)',
        reload='source ~/.bashrc',
        can_configure_automatically=True)
    how_to_configure_alias(configuration_details)

# Generated at 2022-06-14 09:05:50.852479
# Unit test for function debug_time
def test_debug_time():
    import time
    with debug_time('test'):
        time.sleep(2)

# Generated at 2022-06-14 09:06:02.728019
# Unit test for function confirm_text
def test_confirm_text():
    import six
    from .shells import Generic
    from .rules import Command
    from .utils import get_closest
    from .utils import get_all_executables
    from .utils import get_history_without_current
    from contextlib import nested
    from mock import patch, Mock

    with nested(
        patch('__builtin__.raw_input'),
        patch('sys.stdout', six.StringIO()),
        patch('sys.stderr', six.StringIO())):
        raw_input.return_value = 'yes'
        confirm_text(Command('ls', 'ls -a', '', get_all_executables,
                             get_closest, get_history_without_current))

# Generated at 2022-06-14 09:06:04.562186
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text(CorrectedCommand('ls -ls'))



# Generated at 2022-06-14 09:06:11.457715
# Unit test for function debug_time
def test_debug_time():
    from .utils import EmptyContextManager

    from datetime import timedelta
    from mock import Mock

    with EmptyContextManager(lambda: debug('in debug_time')) as mock_debug:
        with debug_time('in test_debug_time'):
            pass

    assert mock_debug.call_count == 1
    assert 'in test_debug_time took: ' in mock_debug.call_args[0][0]

# Generated at 2022-06-14 09:06:13.590503
# Unit test for function debug_time
def test_debug_time():
    start = datetime.now()
    with debug_time('time'):
        import time
        time.sleep(1)
    assert start + timedelta(seconds=1) == datetime.now()

# Generated at 2022-06-14 09:06:18.812319
# Unit test for function debug_time
def test_debug_time():
    import time
    with debug_time('test'):
        time.sleep(0.5)

# Generated at 2022-06-14 09:06:30.511532
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .corrected_command import CorrectedCommand
    from .command import Command
    from .shells import Bash

    corrected_command = CorrectedCommand(
        Command('command1', 'git banch', 'cd /tmp',
                datetime(2015, 1, 1, 0, 0, 0)),
        Bash(),
        'ls')

    output = u'{prefix}{bold}{script}{reset}{side_effect}\n'.format(
        prefix=const.USER_COMMAND_MARK,
        script=corrected_command.script,
        side_effect=u' (+side effect)' if corrected_command.side_effect else u'',
        bold=color(colorama.Style.BRIGHT),
        reset=color(colorama.Style.RESET_ALL))

    import os
    import sys
    old_error_output = os

# Generated at 2022-06-14 09:06:31.272161
# Unit test for function debug
def test_debug():
    debug('testing debug')

# Generated at 2022-06-14 09:06:44.898225
# Unit test for function confirm_text
def test_confirm_text():
    import random
    import re
    regexp = re.compile(r'^(?P<prefix>.*)(?P<clear>\033\[1K\r)(?P<bold>\x1b\[1m)(?P<script>.*)(?P<reset>\x1b\[0m)(?P<side_effect> \+side effect)? \[(?P<green>.*)enter(?P<reset>.*)\/(?P<blue>.*)↑(?P<reset>.*)\/(?P<blue>.*)↓(?P<reset>.*)\/(?P<red>.*)ctrl\+c(?P<reset>.*)\]$')
    # Check the formatting of the command
    from .models import CorrectedCommand

# Generated at 2022-06-14 09:06:46.568433
# Unit test for function color
def test_color():
    assert color(1) == 1
    assert color(1) == 1

# Generated at 2022-06-14 09:06:52.142894
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    from StringIO import StringIO
    from tests.utils import capture_stderr

    with capture_stderr(StringIO()), debug_time('test'), settings(debug=True):
        pass

    out = unicode(sys.stderr.getvalue())
    assert 'DEBUG: test took' in out
    assert timedelta(0) < timedelta.strptime(
        out.split('test took: ')[1].rstrip(), '%H:%M:%S.%f')

# Generated at 2022-06-14 09:06:56.079918
# Unit test for function show_corrected_command
def test_show_corrected_command():
    show_corrected_command(corrected_command="cd /tmp")
    show_corrected_command(corrected_command="cat project/tests/test_utils.py")


# Generated at 2022-06-14 09:07:06.310160
# Unit test for function debug
def test_debug():
    import StringIO
    import contextlib
    @contextlib.contextmanager
    def captured_output():
        new_out, new_err = StringIO.StringIO(), StringIO.StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err
    settings.debug = True
    with captured_output() as (out, err):
        debug(u'debug')
    output = err.getvalue().strip()
    assert output == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m debug'

# Generated at 2022-06-14 09:07:15.465574
# Unit test for function debug
def test_debug():
    from contextlib import contextmanager
    from io import BytesIO
    from sys import stderr

    @contextmanager
    def debug_io():
        io = BytesIO()
        old_stderr = stderr
        stderr = io
        try:
            yield io
        finally:
            stderr = old_stderr

    with debug_io() as io:
        debug(u'It works!')
    assert io.getvalue() == u'DEBUG: It works!\n'

# Generated at 2022-06-14 09:07:16.932012
# Unit test for function debug_time
def test_debug_time():
    with debug_time('timer'):
        time.sleep(1)
        assert True

# Generated at 2022-06-14 09:07:21.030172
# Unit test for function debug_time
def test_debug_time():
    with debug_time(u'debug time test'):
        pass

# Generated at 2022-06-14 09:07:31.951988
# Unit test for function debug
def test_debug():
    from contextlib import contextmanager, nested
    from io import BytesIO
    from mock import patch
    from click.testing import CliRunner

    from thefuck.cli import cli
    from thefuck.main import debug
    from . import conf


# Generated at 2022-06-14 09:07:32.714569
# Unit test for function debug_time
def test_debug_time():
    debug_time('test')



# Generated at 2022-06-14 09:07:33.978952
# Unit test for function color
def test_color():
    """
    >>> color(colorama.Style.BRIGHT)
    ''
    """



# Generated at 2022-06-14 09:07:43.484576
# Unit test for function confirm_text
def test_confirm_text():
    from thefuck.shells import Bash
    import os
    import tempfile

    with tempfile.NamedTemporaryFile() as temp:
        os.environ[Bash.confirm_env] = temp.name
        os.environ[Bash.history_env] = temp.name

        confirm_text(const.CorrectedCommand('ls', True))
        assert(temp.read() == 'ls (+side effect) '
                              '[\x1b[32menter\x1b[0m/\x1b[34m↑\x1b[0m/\x1b[34m↓\x1b[0m/\x1b[31mctrl+c\x1b[0m]')

# Generated at 2022-06-14 09:07:47.701966
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = "git pull"
    show_corrected_command(corrected_command)
    corrected_command = "ls"
    show_corrected_command(corrected_command)


# Generated at 2022-06-14 09:07:56.630078
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .utils import _get_output_text
    from .types import CorrectedCommand

    corrected_command = CorrectedCommand('ls -al', 'ls -al')
    show_corrected_command(corrected_command)
    assert _get_output_text() == u'\tls -al\n'

    corrected_command = CorrectedCommand('ls -al', 'ls -al', True)
    show_corrected_command(corrected_command)
    assert _get_output_text() == u'\tls -al (+side effect)\n'


# Generated at 2022-06-14 09:08:09.570693
# Unit test for function confirm_text
def test_confirm_text():
    from mock import patch, Mock

    with patch('sys.stderr') as stderr:
        confirm_text(Mock(script='foo', side_effect=False))
        stderr.write.assert_called_with(u'\x1b[1K\r\x1b[1mfuck\x1b[m '
                                        u'foo [\x1b[32menter\x1b[m/'
                                        u'\x1b[34m↑\x1b[m/'
                                        u'\x1b[34m↓\x1b[m/'
                                        u'\x1b[31mctrl+c\x1b[m]')

# Generated at 2022-06-14 09:08:18.299063
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = type('', (object,), {'script': 'cp ./* .',
                                             'side_effect': True,
                                             'changed': True})
    expected_text = (
        u'\x1b[1K\r\x1b[92m    fuck  cp ./* . +side effect '
        u'[enter/\x1b[94m↑\x1b[92m/\x1b[94m↓\x1b[92m/\x1b[91mctrl+c\x1b[92m] ')
    assert expected_text == confirm_text(corrected_command)

# Generated at 2022-06-14 09:08:29.417325
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    from .application import Application

    seconds = 0.1
    application = Application(settings)

    with debug_time('test'):
        application.run(['sleep', str(seconds)])

    def get_command_line(debug_time_msg):
        return debug_time_msg[debug_time_msg.find('test'):]

    assert 'test took' in get_command_line(application.log)
    assert '0:' in get_command_line(application.log)
    assert timedelta(seconds=seconds) < timedelta.fromtimedelta(
        get_command_line(application.log)) < timedelta(seconds=seconds * 1.1)

# Generated at 2022-06-14 09:08:33.417069
# Unit test for function confirm_text
def test_confirm_text():
    assert u'[enter/↑/↓/ctrl+c]' in confirm_text([])

# Generated at 2022-06-14 09:08:36.716911
# Unit test for function color
def test_color():
    assert color(':)') == ':)'
    assert color(u'привет') == u'привет'



# Generated at 2022-06-14 09:08:42.792650
# Unit test for function debug_time
def test_debug_time():
    started = datetime.now()
    with debug_time("test"):
        time = datetime.now() - started

# Generated at 2022-06-14 09:08:48.158817
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = corrected_command()
    u'fuck\n'
    return show_corrected_command(corrected_command)


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)

# Generated at 2022-06-14 09:08:51.393600
# Unit test for function confirm_text
def test_confirm_text():
    from . import application as app
    application = app.Application()
    corrected_command = application.correct_command('git fuxk')
    confirm_text(corrected_command)

# Generated at 2022-06-14 09:08:52.040093
# Unit test for function show_corrected_command
def test_show_corrected_command():
    pass

# Generated at 2022-06-14 09:08:53.330881
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test function'):
        assert 1 == 1

# Generated at 2022-06-14 09:08:59.292773
# Unit test for function show_corrected_command
def test_show_corrected_command():
    class Corrected_command:
        def __init__(self, script, side_effect):
            self.script = script
            self.side_effect = side_effect
    corrected_command = Corrected_command("script", False)
    show_corrected_command(corrected_command)


# Generated at 2022-06-14 09:09:02.430429
# Unit test for function color
def test_color():
    assert color(colorama.Fore.BLUE) == colorama.Fore.BLUE
    assert color(colorama.Fore.BLUE) == ''

# Generated at 2022-06-14 09:09:06.202044
# Unit test for function debug_time
def test_debug_time():
    # Gets debug time result
    test_time = debug_time(u'test')

    # Checks if the function decorator is working
    assert isinstance(test_time, contextmanager)

# Generated at 2022-06-14 09:09:15.301211
# Unit test for function show_corrected_command
def test_show_corrected_command():
    class CorrectedCommand(object):
        def __init__(self, script, side_effect):
            self.script = script
            self.side_effect = side_effect

    assert (show_corrected_command(CorrectedCommand(
        u'ls', False)) ==
            u'# ls\n')
    assert (show_corrected_command(CorrectedCommand(
        u'ls', True)) ==
            u'# ls (+side effect)\n')



# Generated at 2022-06-14 09:09:22.037507
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from thefuck.shells.bash import Bash

    bash = Bash()
    with bash.prefix(''):
        show_corrected_command(bash.from_shell(u'ls /usr/bin'))
        show_corrected_command(bash.from_shell(u'ls /usr/lib',
                                               side_effect='rm -rf /'))



# Generated at 2022-06-14 09:09:23.582494
# Unit test for function debug
def test_debug():
    debug(u'Debug is work')

# Generated at 2022-06-14 09:09:24.381861
# Unit test for function show_corrected_command
def test_show_corrected_command():
    pass

# Generated at 2022-06-14 09:09:26.213858
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text(corrected_command='echo hello world') == 'echo hello world'

# Generated at 2022-06-14 09:09:30.945455
# Unit test for function debug_time
def test_debug_time():
    import time
    from . import settings
    from . import utils
    from .compat import str_to_bytes

    settings.debug = True

    utils.debug_time('test_debug_time')
    time.sleep(1)

# Generated at 2022-06-14 09:09:35.724832
# Unit test for function debug_time
def test_debug_time():
    import time
    debug_message = 'debug message'
    with debug_time(debug_message):
        time.sleep(0.5)
    # I don't know how to check print the output in stderr
    # to do it, feel free to add a pull request

# Generated at 2022-06-14 09:09:43.314668
# Unit test for function show_corrected_command
def test_show_corrected_command():
    show_corrected_command(const.CorrectedCommand(script='echo hello', side_effect=True))
    show_corrected_command(const.CorrectedCommand(script='echo hello', side_effect=False))
    settings.no_colors = True
    show_corrected_command(const.CorrectedCommand(script='echo hello', side_effect=True))
    show_corrected_command(const.CorrectedCommand(script='echo hello', side_effect=False))
    settings.no_colors = False


# Generated at 2022-06-14 09:09:45.111112
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug(u'Test string')
    settings.debug = False
    debug(u'Test string')

# Generated at 2022-06-14 09:09:46.062326
# Unit test for function debug
def test_debug():
    pass

# Generated at 2022-06-14 09:10:00.456468
# Unit test for function confirm_text
def test_confirm_text():
    from StringIO import StringIO
    from tempfile import TemporaryFile
    from thefuck.conf import settings

    # create a temp file for the terminal
    terminal = TemporaryFile()

    # Change the default terminal stdout to the temporarily created terminal
    stdout_ = sys.stdout
    sys.stdout = terminal

    # store the terminal input
    result = StringIO()

    # call confirm_text and write the text to stringIO
    stdout_.write(confirm_text(result))

    # change the terminal stdout back to original stdout stream
    sys.stdout = stdout_

    # get the result back to a string
    res = result.getvalue()

    terminal.close()

    # now check if confirm_text() has the correct prompt

# Generated at 2022-06-14 09:10:12.523470
# Unit test for function debug
def test_debug():
    import os
    import sys
    import mock

    def clean_environ():
        environ = os.environ
        for key in [key for key in environ if key.startswith('THEFUCK_')]:
            del os.environ[key]

    from thefuck.conf import reload_settings
    reload_settings()
    debug('Test')
    assert '' == sys.stderr.getvalue()

    os.environ['THEFUCK_DEBUG'] = 'true'
    reload_settings()
    debug('Test')
    assert 'DEBUG: Test\n' == sys.stderr.getvalue()

    clean_environ()
    reload_settings()
    with mock.patch('thefuck.debug.input', return_value='true'):
        debug('Test')
    assert 'DEBUG: Test\n'

# Generated at 2022-06-14 09:10:19.192169
# Unit test for function confirm_text
def test_confirm_text():
    from .application import Application
    from .rules.git import git_rule
    from .shells import shell_factory

    with Application(rules=[git_rule],
                     settings=settings,
                     shells=[shell_factory()]) as app:
        app._corrected_command = app._corrected_command_class(
            app._command, app._rule, 'corrected script')
        result = confirm_text(app._corrected_command)
        assert result == None

# Generated at 2022-06-14 09:10:24.140760
# Unit test for function confirm_text
def test_confirm_text():
    import sys
    import StringIO
    confirmed_command = \
        StringIO.StringIO()
    sys.stderr = confirmed_command
    from . import commands
    confirm_text(commands.CorrectedCommand(u"ls", True))


# Generated at 2022-06-14 09:10:27.922360
# Unit test for function debug_time
def test_debug_time():
    # import thefuck.ui
    # thefuck.ui.debug = lambda msg: sys.stderr.write(msg + u'\n')
    debug_time('fuck')(lambda x: x)()

# Generated at 2022-06-14 09:10:30.354110
# Unit test for function show_corrected_command
def test_show_corrected_command():
    show_corrected_command("git status")
    assert "git status" in sys.stderr.getvalue()

# Generated at 2022-06-14 09:10:33.907964
# Unit test for function debug
def test_debug():
    from tests.utils import capture_stderr

    with capture_stderr() as captured:
        debug(u'foo')
        debug(u'bar')

    assert u'DEBUG: foo' in captured.getvalue()
    assert u'DEBUG: bar' in captured.getvalue()

# Generated at 2022-06-14 09:10:36.690873
# Unit test for function debug_time
def test_debug_time():
    with debug_time('foo'):
        pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 09:10:46.450396
# Unit test for function debug
def test_debug():
    class _stream:
        def __init__(self):
            self.str = u''

        def write(self, str):
            self.str += str

    old_stderr = sys.stderr
    try:
        sys.stderr = _stream()
        debug(u'Test string')
        assert sys.stderr.str == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m Test string\n'
    finally:
        sys.stderr = old_stderr

# Generated at 2022-06-14 09:10:48.597845
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        time.sleep(1)

# End of unit test

# Generated at 2022-06-14 09:11:01.147870
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .command import Command

    corrected_command = Command(script=u'abc', side_effect=False)
    show_corrected_command(corrected_command)
    #assert sys.stderr.write.call_args == mock.call(u'{}{}{}'.format(const.USER_COMMAND_MARK, 'abc', '\n'))
    sys.stderr.write.assert_called_with(u'{}{}{}'.format(const.USER_COMMAND_MARK, 'abc', '\n'))


# Generated at 2022-06-14 09:11:08.324043
# Unit test for function color
def test_color():
    assert color('') == ''
    settings.no_colors = False
    assert color(colorama.Back.RED + colorama.Fore.WHITE
                 + colorama.Style.BRIGHT) == colorama.Back.RED + colorama.Fore.WHITE + colorama.Style.BRIGHT
    settings.no_colors = True
    assert color(colorama.Back.RED + colorama.Fore.WHITE
                 + colorama.Style.BRIGHT) == ''

# Generated at 2022-06-14 09:11:09.876971
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)


# Generated at 2022-06-14 09:11:14.369327
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import io
    import sys
    sys.stderr = io.StringIO()
    show_corrected_command("git fukk origin master")
    assert sys.stderr.getvalue() == "git push -f origin master\n"

# Generated at 2022-06-14 09:11:19.591742
# Unit test for function debug
def test_debug():
    global settings
    debug(u"msg")
    settings.debug = False
    debug(u"msg")

# Generated at 2022-06-14 09:11:24.655889
# Unit test for function color
def test_color():
    assert color('red text') == 'red text'



# Generated at 2022-06-14 09:11:37.627418
# Unit test for function debug_time
def test_debug_time():
    import time
    import StringIO

    with debug_time('test'):
        time.sleep(0.3)

    import mock
    with mock.patch('sys.stderr', StringIO.StringIO()) as stderr:
        with debug_time('test1'):
            with debug_time('test2'):
                time.sleep(0.3)
            time.sleep(0.1)

        assert 'test2 took' in stderr.getvalue()
        assert 'test1 took' in stderr.getvalue()
        assert 'test took' not in stderr.getvalue()
        with debug_time('test3'):
            time.sleep(0.3)
        assert 'test3 took' in stderr.getvalue()
        with debug_time('test4'):
            time.sleep

# Generated at 2022-06-14 09:11:40.633277
# Unit test for function color
def test_color():
    assert color('red') == ''
    settings.no_colors = False
    assert color('red') == colorama.Fore.RED
    settings.no_colors = True



# Generated at 2022-06-14 09:11:46.914892
# Unit test for function confirm_text
def test_confirm_text():
    from .conf import settings
    settings.use_temprorary_history = False
    sys.stderr.write('\n')
    sys.stderr.write('\n')
    sys.stderr.write('\n')
    sys.stderr.write('\n')
    sys.stderr.write('\n')
    sys.stderr.write('\n')
    sys.stderr.write('\n')
    sys.stderr.write('\n')
    sys.stderr.write('\n')
    sys.stderr.write('\n')
    sys.stderr.write('\n')
    sys.stderr.write('\n')
    sys.stderr.write('\n')

# Generated at 2022-06-14 09:11:48.314228
# Unit test for function debug
def test_debug():
    assert debug('test') is None


# Generated at 2022-06-14 09:11:54.933039
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug(u'Testing debug') == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m Testing debug\n'
    settings.debug = False

# Generated at 2022-06-14 09:11:55.732832
# Unit test for function debug_time
def test_debug_time():
    pass



# Generated at 2022-06-14 09:12:03.033090
# Unit test for function confirm_text
def test_confirm_text():
    from .utils import environ

    with environ(**{'COLUMNS': '80'}):
        confirm_text('test') == 'test'
    with environ(**{'COLUMNS': '22'}):
        confirm_text('test') == 'test'
    with environ(**{'COLUMNS': '20'}):
        confirm_text('test') == 'test'
    with environ(**{'COLUMNS': '19'}):
        confirm_text('test') == 'test'
    with environ(**{'COLUMNS': '18'}):
        confirm_text('test') == 'test'
    with environ(**{'COLUMNS': '17'}):
        confirm_text('test') == 'test'

# Generated at 2022-06-14 09:12:08.812979
# Unit test for function debug
def test_debug():
    from io import StringIO
    stream = StringIO()
    sys.stderr = stream
    debug('test')
    assert stream.getvalue().endswith('test\n')
    stream.close()


# Generated at 2022-06-14 09:12:17.896131
# Unit test for function debug_time
def test_debug_time():
    class A:
        def __init__(self):
            self.msg = ''

    a = A()  # noqa

    def set_debug(msg):
        a.msg = msg

    def debug(msg):
        set_debug(msg)

    settings.debug = True
    with debug_time('Hello'):
        pass
    assert a.msg.startswith("Hello took: 0")

    settings.debug = False
    with debug_time('World'):
        pass
    assert a.msg == 'Hello took: 0'

# Generated at 2022-06-14 09:12:19.932477
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text('* hi') == 'fuck * hi [enter/↑/↓/ctrl+c]'

# Generated at 2022-06-14 09:12:23.097211
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test_debug_time'):
        import time
        time.sleep(0.1)

# Generated at 2022-06-14 09:12:24.336825
# Unit test for function debug
def test_debug():
    debug("Debug test")


# Generated at 2022-06-14 09:12:35.130073
# Unit test for function debug
def test_debug():
    import sys
    import StringIO

    stderr = sys.stderr
    sys.stderr = StringIO.StringIO()

# Generated at 2022-06-14 09:12:47.885016
# Unit test for function confirm_text
def test_confirm_text():
    from thefuck.shells import get_corrected_command

    assert confirm_text(get_corrected_command({'cmd': 'touch new_file'}))\
        == u'\x1b[2K\r\x1b[0m\x1b[1m\x1b[0m\x1b[0m\x1b[1mtouch new_file\x1b[0m ' \
           u'[\x1b[32menter\x1b[0m/\x1b[34m↑\x1b[0m/\x1b[34m↓\x1b[0m/\x1b[31mctrl+c\x1b[0m]'



# Generated at 2022-06-14 09:13:02.680084
# Unit test for function confirm_text
def test_confirm_text():
    def test_corrected_command(script, side_effect):
        class FakeCorrectedCommand(object):
            def __init__(self, script, side_effect):
                self.side_effect = side_effect
                self.script = script

        return FakeCorrectedCommand(script, side_effect)

    assert confirm_text(test_corrected_command('ls', False)) == (
        '\r\033[1K\x1b[1m$ ls\x1b[0m \x1b[32menter\x1b[0m/\x1b[34m↑\x1b[0m/'
        '\x1b[34m↓\x1b[0m/\x1b[31mctrl+c\x1b[0m')

# Generated at 2022-06-14 09:13:05.746441
# Unit test for function debug
def test_debug():
    debug('abc')
    assert sys.stderr.getvalue() == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m abc\n'



# Generated at 2022-06-14 09:13:07.295333
# Unit test for function debug
def test_debug():
    debug('Test')

# Generated at 2022-06-14 09:13:15.489907
# Unit test for function debug_time
def test_debug_time():
    import time, re

    # Suppose to be called with message "Test", and takes a bit more than 1 second
    def test():
        time.sleep(1.1)
        debug("Test")

    with debug_time("Test"):
        test()

    # This regexp is supposed to match message that contains floating point
    # number >= 1.0 (1.1 seconds)
    assert re.match("^Test took: .*s$", sys.stderr.getvalue().strip())

# Generated at 2022-06-14 09:13:20.289833
# Unit test for function debug
def test_debug():
    from StringIO import StringIO
    import sys
    saved_stderr = sys.stderr
    debug_output = StringIO()
    try:
        sys.stderr = debug_output
        debug('hello world')
        assert debug_output.getvalue() == 'hello world\n'
    finally:
        sys.stderr = saved_stderr

# Generated at 2022-06-14 09:13:22.321313
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug('test')
    settings.debug = False
    debug('test')

# Generated at 2022-06-14 09:13:23.612694
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text({'script': 'ls'})

# Generated at 2022-06-14 09:13:36.972462
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import thefuck.shells
    from thefuck.shells.base import BaseShell

    class Shell(BaseShell):
        @property
        def history(self):
            return []

        @property
        def _script_from_history(self):
            return u'thefuck'

        def confirm(self, text, ok_text, fail_text):
            assert text == u'thefuck (+side effect) [\x1b[32menter\x1b[0m/\x1b[34m↑\x1b[0m/\x1b[34m↓\x1b[0m/\x1b[31mctrl+c\x1b[0m]'
            return False

        def put_to_history(self, command):
            pass


# Generated at 2022-06-14 09:13:47.929244
# Unit test for function confirm_text
def test_confirm_text():
    # Importing readline is a hack to make mock testing possible
    # https://docs.python.org/3/library/unittest.mock.html#module-unittest.mock
    import readline
    readline.insert_text('ls')
    readline.redisplay()

    for script in ['ls', 'clear', 'sudo !!']:
        for side_effect in [True, False]:
            corrected_command = type('Command', (object,), {
                'script': script,
                'side_effect': side_effect})
            confirm_text(corrected_command)



# Generated at 2022-06-14 09:13:56.397405
# Unit test for function debug_time
def test_debug_time():
    from tempfile import NamedTemporaryFile

    with NamedTemporaryFile(delete=False) as debug_file:
        with debug_time('test'):
            pass
        assert len(debug_file.readlines()) == 2, \
            'debug_time should add one line in debug mode, but has added {}' \
            .format(len(debug_file.readlines()))

    with NamedTemporaryFile(delete=False) as debug_file:
        with debug_time('test'):
            pass
        assert len(debug_file.readlines()) == 0, \
            'debug_time should not add any lines in non-debug mode, but has added {}' \
            .format(len(debug_file.readlines()))

