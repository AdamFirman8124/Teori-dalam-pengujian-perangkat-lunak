

# Generated at 2022-06-14 09:03:55.585232
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = const.Command('echo hi', side_effect=True)
    confirm_text(corrected_command)

# Generated at 2022-06-14 09:03:57.716751
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(0)


# Generated at 2022-06-14 09:04:01.072325
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .tools import ConfigurationDetails
    how_to_configure_alias(
        ConfigurationDetails('/home/nvbn/.zshrc', 'fuck --alias', True))



# Generated at 2022-06-14 09:04:02.167363
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:04:03.453889
# Unit test for function debug
def test_debug():
    with debug_time("Test message"):
        pass

# Generated at 2022-06-14 09:04:05.502717
# Unit test for function color
def test_color():
    assert color(colorama.Fore.RED)(u'abc') == u'abc'



# Generated at 2022-06-14 09:04:06.448982
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text(corrected_command('ls s'))

# Generated at 2022-06-14 09:04:12.932876
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    """Test function how_to_configure_alias"""
    config_details = namedtuple(
        'config_details',
        ['content', 'path', 'reload', 'can_configure_automatically'])
    configuration_details = config_details('testcontent', 'testpath', 'testreload', True)
    how_to_configure_alias(configuration_details)

test_how_to_configure_alias()


# Generated at 2022-06-14 09:04:15.716970
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)
    how_to_configure_alias('123')

    # unit test for function already_configured

# Generated at 2022-06-14 09:04:27.817652
# Unit test for function confirm_text
def test_confirm_text():
    input_data = ['\n', '\r\n', '\r', ' ']
    expected_data = [const.USER_COMMAND_MARK + 'command +side effect ' +
                     color(colorama.Fore.GREEN) + 'enter' +
                     color(colorama.Style.RESET_ALL) + '/' +
                     color(colorama.Fore.BLUE) + '↑' +
                     color(colorama.Style.RESET_ALL) + '/' +
                     color(colorama.Fore.BLUE) + '↓' +
                     color(colorama.Style.RESET_ALL) + '/' +
                     color(colorama.Fore.RED) + 'ctrl+c' +
                     color(colorama.Style.RESET_ALL)]

# Generated at 2022-06-14 09:04:38.557226
# Unit test for function confirm_text
def test_confirm_text():
    import sys
    sys.stderr = sys.stdout
    from thefuck.conf import load_settings
    settings = load_settings()
    settings.no_colors = False
    from thefuck.rules.shells import Shell

    class CorrectedCommand:
        script = u"git push origin HEAD:master"
        side_effect = False

    show_corrected_command(CorrectedCommand())
    confirm_text(CorrectedCommand())

# Generated at 2022-06-14 09:04:40.883082
# Unit test for function debug_time
def test_debug_time():
    import time
    with debug_time('test'):
        time.sleep(0.2)

# Generated at 2022-06-14 09:04:44.865568
# Unit test for function debug_time
def test_debug_time():
    import time
    x = 0
    with debug_time("test message"):
        time.sleep(2)


# Generated at 2022-06-14 09:04:49.332202
# Unit test for function color
def test_color():
    assert (color('') == ''), 'Passed argument is empty'
    assert (color('\033[1mabc') == 'abc')
    assert (color('\033[1mabc\033[0m') == 'abc'), 'Passed argument is not empty'



# Generated at 2022-06-14 09:05:01.979700
# Unit test for function confirm_text
def test_confirm_text():
    from .shells import Bash
    from .shells.bash import FuckBash

    class BashTest(Bash):
        key_mapping = {}
        priority = 999
        requires_output = True
        _script_re = FuckBash.script_re


# Generated at 2022-06-14 09:05:10.145182
# Unit test for function debug
def test_debug():
    import mock
    import io
    stderr = io.StringIO()

    with mock.patch('sys.stderr', stderr):
        debug(u'Hello, World!')
        debug(u'Привет, Мир!')

    assert u'DEBUG: Hello, World!' in stderr.getvalue()
    assert u'DEBUG: Привет, Мир!' in stderr.getvalue()

# Generated at 2022-06-14 09:05:11.560274
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    assert how_to_configure_alias(None) is None


# Generated at 2022-06-14 09:05:14.625946
# Unit test for function debug
def test_debug():
    debug('test message')
    assert True


# Generated at 2022-06-14 09:05:20.178201
# Unit test for function debug
def test_debug():
    for debug_msg in ["Debug info", u"Отладочная информация"]:
        settings.debug = True
        debug(debug_msg)
        settings.debug = False
assert settings.debug is False



# Generated at 2022-06-14 09:05:24.061645
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = 'ls'
    assert confirm_text(corrected_command) == 'ls [enter/↑/↓/ctrl+c]'



# Generated at 2022-06-14 09:05:29.046069
# Unit test for function color
def test_color():
    assert color('red') == 'red'
    settings.no_colors = True
    assert color('red') == ''

# Generated at 2022-06-14 09:05:36.788012
# Unit test for function debug
def test_debug():
    from StringIO import StringIO
    from .conf import settings

    debug_msg = 'test debug msg'
    settings.debug = True
    buf = StringIO()
    sys.stderr = buf

    debug(debug_msg)

    sys.stderr = sys.__stderr__
    buf.close()
    assert debug_msg in buf.getvalue()



# Generated at 2022-06-14 09:05:42.434754
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import sys
    import StringIO
    old__stdout__, sys.stdout = sys.stdout, StringIO.StringIO()
    import thefuck.utils
    thefuck.utils.show_corrected_command('fuck')
    output = sys.stdout.getvalue()
    sys.stdout = thefuck.utils.old__stdout__
    return output


# Generated at 2022-06-14 09:05:46.868714
# Unit test for function debug_time
def test_debug_time():
    reached = [False]

    def debug_time_called():
        with debug_time(''):
            reached[0] = True

    debug_time_called()
    assert reached[0]

# Generated at 2022-06-14 09:05:57.808594
# Unit test for function confirm_text
def test_confirm_text():
    from thefuck.shells.base import Shell

    class FakeCorrectedCommand(object):
        script = u'foo'
        side_effect = False

    class FakeShell(Shell):
        def and_(self, *commands):
            return u' and '.join(commands)

    confirm_text(FakeCorrectedCommand())
    import mock
    with mock.patch.object(FakeShell, 'and_') as patched_and_:
        confirm_text(FakeCorrectedCommand())
    assert patched_and_.called
    assert patched_and_().startswith('\033[1K\r')

# Generated at 2022-06-14 09:06:05.622499
# Unit test for function debug
def test_debug():
    from mock import Mock, patch
    with patch('thefuck.utils.settings', debug=True):
        with patch('thefuck.utils.sys.stderr') as patched_stderr:
            debug('new msg')
            patched_stderr.write.assert_called_once_with(
                u'\x1b[34m\x1b[1mDEBUG:\x1b[0m new msg\n')



# Generated at 2022-06-14 09:06:07.008399
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass



# Generated at 2022-06-14 09:06:12.598282
# Unit test for function confirm_text
def test_confirm_text():
    sys.stderr = open('/dev/null', 'w')
    settings.no_colors = True
    confirm_text(
        const.CorrectedCommand('ls', '', '', ''))

# Generated at 2022-06-14 09:06:13.274503
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    pass

# Generated at 2022-06-14 09:06:16.025528
# Unit test for function debug_time
def test_debug_time():
    import time
    import thefuck.main
    with thefuck.main.debug_time('test'):
        time.sleep(1)
        assert True

# Generated at 2022-06-14 09:06:21.604449
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .command import Command
    show_corrected_command(Command('ls', 'echo ls'))


if __name__ == '__main__':
    test_show_corrected_command()

# Generated at 2022-06-14 09:06:32.342853
# Unit test for function debug_time
def test_debug_time():
    # pylint: disable=unused-variable
    @contextmanager
    def mock_datetime(time):
        old_datetime = datetime
        class Datetime(object):
            @classmethod
            def now(cls):
                return time
        datetime = Datetime
        try:
            yield
        finally:
            datetime = old_datetime

    # pylint: disable=redefined-outer-name

# Generated at 2022-06-14 09:06:33.874301
# Unit test for function debug
def test_debug():
    debug('test debug')
if __name__ == '__main__':
    test_debug()

# Generated at 2022-06-14 09:06:41.716477
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    assert how_to_configure_alias() == \
        "Seems like {} alias isn't configured!\n" \
        "Please put {content} in your {path}\n" \
        "and apply changes with {reload} or restart your shell.\n" \
        "Or run {fuck} a second time to configure it automatically.\n" \
        "More details - https://github.com/nvbn/thefuck#manual-installation"


# Generated at 2022-06-14 09:06:48.111284
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = 'corrected_command'
    show_corrected_command(corrected_command)
    confirm_text(corrected_command)
    warn('warn title')
    exception('exception title', 'exc_info')
    rule_failed('rule', 'exc_info')
    failed('failed')


if __name__ == '__main__':
    test_confirm_text()

# Generated at 2022-06-14 09:06:51.399669
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(configuration_details = 'abc')


# Generated at 2022-06-14 09:06:56.286208
# Unit test for function debug_time
def test_debug_time():
    from datetime import datetime
    from mock import patch

    with patch('sys.stderr') as fake_stderr:
        with debug_time('test') as debug_time:
            datetime.now

    assert not debug_time
    fake_stderr.write.called

# Generated at 2022-06-14 09:06:57.272134
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test_debug'):
        pass

# Generated at 2022-06-14 09:07:04.626271
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = type('', (), {
        'script': u'gut',
        'side_effect': False,
        '_asdict': classmethod(lambda cls: {})
    })()

    try:
        show_corrected_command_stderr = StringIO()
        sys.stderr = show_corrected_command_stderr
        show_corrected_command(corrected_command)
        sys.stderr = sys.__stderr__
        assert show_corrected_command_stderr.getvalue() == u'{}gut\n'.format(const.USER_COMMAND_MARK)
    except AssertionError:
        sys.stderr = sys.__stderr__
        print(u'Incorrect corrected command output')



# Generated at 2022-06-14 09:07:12.123322
# Unit test for function debug_time
def test_debug_time():
    from unittest import TestCase
    from datetime import timedelta

    class DebugTimeTestCase(TestCase):
        def test_debug_time(self):
            with debug_time('test'):
                pass
        #     self.assertGreaterEqual(timedelta(seconds=1), timedelta(seconds=0))

    test = DebugTimeTestCase()
    test.test_debug_time()

# Generated at 2022-06-14 09:07:16.398575
# Unit test for function debug
def test_debug():
    debug('message')



# Generated at 2022-06-14 09:07:21.076440
# Unit test for function debug
def test_debug():
    msg = u'test'
    expected = u'$ thefuck --debug > /dev/null\n\033[1K\r\x1b[34;1mDEBUG:\x1b[0m test\n'
    assert debug(msg) == sys.stderr.write(expected)



# Generated at 2022-06-14 09:07:31.605049
# Unit test for function debug
def test_debug():
    from mock import patch, call
    from .main import debug

    debug_msg = 'foo'

    with patch("sys.stderr") as stderr:
        debug(debug_msg)
        assert stderr.method_calls == []

    with patch("sys.stderr") as stderr:
        with patch("thefuck.conf.settings.debug", True):
            debug(debug_msg)
            assert stderr.method_calls == [
                call.write(u'{blue}{bold}DEBUG:{reset} foo\n'.format(
                    blue=color(colorama.Fore.BLUE),
                    reset=color(colorama.Style.RESET_ALL),
                    bold=color(colorama.Style.BRIGHT)))]



# Generated at 2022-06-14 09:07:37.080644
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from thefuck.types import CorrectedCommand

    show_corrected_command(CorrectedCommand('ls .', ''))
    show_corrected_command(CorrectedCommand('ls .', 'side effect'))

# Generated at 2022-06-14 09:07:49.544870
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = type('CorrectedCommand', (object,), {'script': 'corrected command', 'side_effect': None})
    src = ('\n' 
           '\033[1K\r' 
           '> ' 
           'corrected command' 
           '\n')
    assert show_corrected_command(corrected_command) == src
    corrected_command = type('CorrectedCommand', (object,), {'script': 'corrected command', 'side_effect': 'side effect'})
    src = ('\n' 
           '\033[1K\r' 
           '> ' 
           'corrected command' 
           ' +side effect' 
           '\n')
    assert show_corrected_command(corrected_command) == src

# Generated at 2022-06-14 09:07:53.044535
# Unit test for function debug_time
def test_debug_time():
    # Set debug to True
    settings.debug = True
    # Print original time.sleep() and then print modified time.sleep()
    with debug_time('time.sleep()'):
        import time
        time.sleep(2)

# Generated at 2022-06-14 09:08:03.357275
# Unit test for function confirm_text
def test_confirm_text():
    user_command = type(
        'UserCommand', (object,), {'script': 'echo lol',
                                   'side_effect': False})()
    confirm_text(user_command)
    assert sys.stderr.getvalue() == (
        u'@echo lol [\x1b[32menter\x1b[0m/\x1b[34m\x1b[0m]'
        u'/\x1b[34m\x1b[0m/\x1b[31mctrl+c\x1b[0m]')
    sys.stderr.close()

# Generated at 2022-06-14 09:08:03.854552
# Unit test for function debug_time
def test_debug_time():
    with debug_time('Some awesome code'):
        pass

# Generated at 2022-06-14 09:08:08.854912
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    from unittest import TestCase
    from mock import patch


# Generated at 2022-06-14 09:08:18.772457
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from datetime import datetime
    from .conf import ConfigurationDetails
    from . import conf
    from . import shell

    _time = datetime.now()
    configuration_details = ConfigurationDetails(path='~/.bashrc',
                                                 content='alias fuck=\'eval $(thefuck $(fc -ln -1))\'',
                                                 reload='$ source ~/.bashrc',
                                                 start_time=_time,
                                                 can_configure_automatically=shell.from_shell('can configure'))
    conf.ConfigurationDetails = configuration_details

    how_to_configure_alias(configuration_details)
    conf.ConfigurationDetails = None


if __name__ == '__main__':
    test_how_to_configure_alias()

# Generated at 2022-06-14 09:08:29.983709
# Unit test for function confirm_text
def test_confirm_text():
    from cStringIO import StringIO
    from contextlib import contextmanager
    from .shells import Shell

    @contextmanager
    def mock_stdout():
        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            yield out
        finally:
            sys.stdout = saved_stdout

    assert confirm_text(Shell('echo test', 'echo test', None, None).
                        get_history_commands()) == None
    assert len(mock_stdout().getvalue()) > 0



# Generated at 2022-06-14 09:08:31.608763
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug('message')
    settings.debug = False



# Generated at 2022-06-14 09:08:42.883970
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    import pytest
    from .utils import how_to_configure_alias, ConfigurationDetails

    def _check_output(expected_output):
        # pylint: disable=unused-variable
        # needed for better pytest output
        with pytest.raises(SystemExit):
            how_to_configure_alias([])
        out, err = capsys.readouterr()
        assert out == expected_output

    # Without any details
    expected_output = (u'\n'
                       u'\n'
                       u'Seems like \x1b[1mfuck\x1b[0m alias isn\'t configured!\n'
                       u'\n'
                       u'\n'
                       u'More details - https://github.com/nvbn/thefuck#manual-installation\n')
   

# Generated at 2022-06-14 09:08:49.059265
# Unit test for function debug_time
def test_debug_time():
    from nose.tools import assert_greater, assert_true

    import time

    with debug_time('Foo'):
        sleep_time = 0.05
        time.sleep(sleep_time)

    assert_true(settings.debug)
    assert_greater(sleep_time, 0)

# Generated at 2022-06-14 09:08:59.806465
# Unit test for function confirm_text
def test_confirm_text():
    from .utils import _get_input, _term_supports_colors, _term_width
    from .rules.python import python
    from .shells.bash import Bash
    from .shells.zsh import Zsh
    from .shells.fish import Fish

    if not _get_input or not _term_supports_colors or not _term_width:
        # These functions require `mock` library.
        raise RuntimeError('This test requires `mock` library.')

    with _get_input(u'\n') as get_input, \
            _term_supports_colors(True), \
            _term_width(8):
        confirm_text(python.get_new_command(u'fuck'))

# Generated at 2022-06-14 09:09:01.585419
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)

# Generated at 2022-06-14 09:09:04.535928
# Unit test for function show_corrected_command
def test_show_corrected_command():
    assert show_corrected_command() == "git push\n"



# Generated at 2022-06-14 09:09:08.523524
# Unit test for function confirm_text
def test_confirm_text():
    print(colorama.ansi.clear_screen())
    confirm_text(const.CorrectedCommand(u'cp * /tmp',
                                        False))
    confirm_text(const.CorrectedCommand(u'cp * /tmp',
                                        True))

# Generated at 2022-06-14 09:09:12.709982
# Unit test for function debug_time
def test_debug_time():
    err = sys.stderr
    sys.stderr = sys.stdout
    settings.debug = True
    from time import sleep

    debug_time('123')
    sleep(1)
    debug_time('321')
    sys.stderr = err

# Generated at 2022-06-14 09:09:26.303877
# Unit test for function confirm_text
def test_confirm_text():
    import tempfile
    import os
    test_file = tempfile.NamedTemporaryFile(delete=False)
    test_file.close()
    with open(test_file.name, 'w') as conf:
        conf.write("""[main]

no_colors = True

rules = I hate colors""")
    settings.clear()
    settings.reload(test_file.name)
    print("""Seems like fuck alias isn't configured!
Please put
	alias fuck='eval $(thefuck $(fc -ln -1));'
in your
	~/.bashrc
and apply changes with
	source ~/.bashrc
or restart your shell.
Or run fuck a second time to configure it automatically.
More details - https://github.com/nvbn/thefuck#manual-installation""")

# Generated at 2022-06-14 09:09:42.576382
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import tempfile
    import os
    from pkg_resources import parse_version
    from six.moves import input as raw_input
    from .utils import which
    from .shells.bash import Bash

    is_py2 = parse_version(sys.version) < parse_version('3.0')
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp:
        temp.write('echo "TEST"')
        temp.close()
        os.chmod(temp.name, 0o755)

# Generated at 2022-06-14 09:09:49.904415
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from thefuck.utils import (ConfigurationDetails,
                               get_closest_executable)
    from thefuck.shells import Shell
    from tests.utils import support_dir, home_dir
    import pytest
    import getpass
    import os
    user = getpass.getuser()
    bashrc_path = os.path.join(home_dir, ".bashrc")
    bash_profile_path = os.path.join(home_dir, ".bash_profile")
    bash_path = get_closest_executable('bash')
    zsh_path = get_closest_executable('zsh')
    fish_path = get_closest_executable('fish')
    csh_path = get_closest_executable('csh')


# Generated at 2022-06-14 09:09:56.857426
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta

    from . import main
    from . import utils

    def sleep_and_return(s):
        import time
        time.sleep(s)
        return s

    with utils.debug_time('function'):
        assert sleep_and_return(0.1) == 0.1

    with main.debug_time('function'):
        assert sleep_and_return(0.1) == 0.1

# Generated at 2022-06-14 09:09:59.588402
# Unit test for function debug_time
def test_debug_time():
    import time
    debug_time('sleep')(time.sleep)(1)

# Generated at 2022-06-14 09:10:03.719602
# Unit test for function confirm_text
def test_confirm_text():
    from io import StringIO
    confirm_text('blablabla')
    output = sys.stdout.getvalue().strip()
    assert output == u'\033[1K\rblablabla '


# Generated at 2022-06-14 09:10:04.821597
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:10:05.966972
# Unit test for function show_corrected_command
def test_show_corrected_command():
    show_corrected_command('test')

# Generated at 2022-06-14 09:10:07.807415
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = "googing"
    show_corrected_command(corrected_command)



# Generated at 2022-06-14 09:10:10.053427
# Unit test for function color
def test_color():
    assert color('red') == ''
    settings.no_colors = False
    assert color('red') == 'red'



# Generated at 2022-06-14 09:10:15.944437
# Unit test for function debug
def test_debug():
    import StringIO
    buffer = StringIO.StringIO()
    save_stdout = sys.stdout
    try:
        sys.stderr = buffer
        debug('message')
        assert buffer.getvalue() == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m message\n'
    finally:
        sys.stderr = save_stdout

# Generated at 2022-06-14 09:10:21.318924
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug('test')
    settings.debug = False
    debug('fail')



# Generated at 2022-06-14 09:10:25.609184
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text(['python', '-c', 'print 1'])
    confirm_text(['python', '-c', 'print x'])


if __name__ == '__main__':
    test_confirm_text()

# Generated at 2022-06-14 09:10:35.389464
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = TestCommand(script="git commit -m", side_effect=True)
    formatted_text = confirm_text(corrected_command)

# Generated at 2022-06-14 09:10:45.798802
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = u'bash -c "echo 1"'
    assert show_corrected_command(corrected_command) \
           == u'{prefix}{bold}{script}{reset}{side_effect}\n'.format(
               prefix=const.USER_COMMAND_MARK,
               script=corrected_command.script,
               side_effect=u' (+side effect)' if corrected_command.side_effect else u'',
               bold=color(colorama.Style.BRIGHT),
               reset=color(colorama.Style.RESET_ALL))


# Generated at 2022-06-14 09:10:47.063220
# Unit test for function confirm_text
def test_confirm_text():
    show_corrected_command(corrected_command)

# Generated at 2022-06-14 09:10:48.711442
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    assert how_to_configure_alias(None) is None

# Generated at 2022-06-14 09:10:59.762275
# Unit test for function confirm_text
def test_confirm_text():
    # We need to check the output manually because pytest's capsys
    # doesn't work with unicode data correctly
    from cStringIO import StringIO
    stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        correct_output = u'\r\033[1Kfuck: command not found [+side effect] [enter/↑/↓/ctrl+c]\n'
        confirm_text(corrected_command=CorrectedCommand(
            script=u'fuck', side_effect=True))
        assert sys.stdout.getvalue() == correct_output
    finally:
        sys.stdout = stdout



# Generated at 2022-06-14 09:11:04.760101
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .corrected_command import CorrectedCommand
    show_corrected_command(CorrectedCommand('echo "lalala"', False))
    assert sys.stderr.getvalue() == u'{prefix}echo "lalala"\n'.format(
        prefix=const.USER_COMMAND_MARK)

# Generated at 2022-06-14 09:11:12.734580
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    try:
        import StringIO
    except ImportError:
        import io as StringIO

    def how_to_configure_alias_in_tests(configuration_details):
        how_to_configure_alias(configuration_details)
        print(colorama.Style.RESET_ALL)

    def call_how_to_configure_alias(configuration_details,
                                    expected_result):
        buf = StringIO.StringIO()
        sys.stdout = buf
        how_to_configure_alias_in_tests(configuration_details)
        sys.stdout = sys.__stdout__
        expected_result = expected_result.format(
            bold='\033[1m',
            reset='\033[0m')
        assert buf.getvalue() == expected_result + '\n'



# Generated at 2022-06-14 09:11:27.195273
# Unit test for function debug
def test_debug():
    try:
        with debug_time('test'):
            raise Exception()
    except:
        pass



# Generated at 2022-06-14 09:11:33.175506
# Unit test for function color
def test_color():
    assert color('test') == ''
    settings.no_colors = False
    assert color('test') == 'test'
    settings.no_colors = True

# Generated at 2022-06-14 09:11:34.488221
# Unit test for function debug_time
def test_debug_time():
    import time


# Generated at 2022-06-14 09:11:37.992995
# Unit test for function show_corrected_command
def test_show_corrected_command():
    """
    >>> show_corrected_command(CorrectedCommand('test command', False))
    (None, '$ test command\\n')
    """

# Generated at 2022-06-14 09:11:42.134328
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    i = 0
    for configuration_details in [None, True, False]:
        i += 1
        how_to_configure_alias(configuration_details)
    assert i == 3  # не вылетает


# Generated at 2022-06-14 09:11:46.529769
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .repl import CorrectedCommand
    show_corrected_command
    assert show_corrected_command(CorrectedCommand('ls')) == None
    assert show_corrected_command(CorrectedCommand('ls', side_effect=True)) == None

# Generated at 2022-06-14 09:11:56.602608
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .command import CorrectedCommand
    show_corrected_command(CorrectedCommand('git foo', False))

    # Unit test for function check_output
    def test_check_output():
        from .shells import Shell
        from .shells.bash import Bash
        shell = Shell()

        def check_output(cmd):
            return shell.check_output(
                cmd, 'pwd', 'username')

        assert check_output('pwd') == 'pwd\n'

    # Unit test for function debug
    def test_debug():
        debug('dummy message')



# Generated at 2022-06-14 09:11:58.646011
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .command import CorrectedCommand
    show_corrected_command(CorrectedCommand('ls', 'ls -CF', False))



# Generated at 2022-06-14 09:12:12.828560
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from StringIO import StringIO
    from .conf import ConfigurationDetails
    import sys
    import colorama
    colorama.init()

    sys.stderr = StringIO()

    how_to_configure_alias(None)
    assert sys.stderr.getvalue() == (
        u"Seems like {bold}fuck{reset} alias isn't configured!\n"
        u"More details - https://github.com/nvbn/thefuck#manual-installation\n"
        "".format(bold=color(colorama.Style.BRIGHT),
                  reset=color(colorama.Style.RESET_ALL)))

    sys.stderr = StringIO()


# Generated at 2022-06-14 09:12:14.737755
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = corrected_command()
    assert show_corrected_command(corrected_command) is None

# Generated at 2022-06-14 09:12:16.395900
# Unit test for function debug_time
def test_debug_time():
    from thefuck.shells import shell

    with debug_time('time'):
        shell()


# Generated at 2022-06-14 09:12:21.797011
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    with debug_time('test'):
        import time
        time.sleep(0.1)
    # If not working properly this call will raise error
    with debug_time(u'тест') as debug_time:
        import time
        time.sleep(0.1)
        assert isinstance(debug_time, timedelta)

# Generated at 2022-06-14 09:12:31.289393
# Unit test for function show_corrected_command
def test_show_corrected_command():
    sys.stderr = open('/tmp/thefuck.pytest.stderr.txt', 'w')
    try:
        show_corrected_command(
            const.CorrectedCommand(
                script='echo hello world',
                side_effect=False))
        assert u'fuck echo hello world' + '\n' in open('/tmp/thefuck.pytest.stderr.txt').read()
    finally:
        sys.stderr = sys.__stderr__
        open('/tmp/thefuck.pytest.stderr.txt', 'w').close()


# Generated at 2022-06-14 09:12:35.306207
# Unit test for function debug_time
def test_debug_time():
    from time import sleep
    from mock import patch
    debug_time_output = []
    with patch('sys.stderr', debug_time_output):
        with debug_time('foo'):
            sleep(0.1)
    assert 'foo took: 0:00:00.1' in ''.join(debug_time_output)

# Generated at 2022-06-14 09:12:41.314496
# Unit test for function debug_time
def test_debug_time():
    from mock import patch
    from contextlib import contextmanager

    @contextmanager
    def debug_time_fixture(msg):
        yield

    with patch('thefuck.utils.debug_time', debug_time_fixture):
        with debug_time('test'):
            pass

# Generated at 2022-06-14 09:12:51.955322
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .shells import Generic as GenericShell
    from .correct import CorrectedCommand
    import os
    import sys
    import mock
    from tests.utils import Rule, Command

    with mock.patch('sys.stderr', new_callable=mock.PropertyMock) as mock_stderr:
        with mock.patch.object(GenericShell, 'from_shell', return_value='sh'):
            show_corrected_command(CorrectedCommand(
                Command('pwd', '', '', 'pwd'),
                [Rule('', lambda c: CorrectedCommand(c, ''), '')], True))
    assert os.linesep.join([
        const.USER_COMMAND_MARK +
        'pwd (+side effect)' +
        colorama.Style.RESET_ALL +
        os.linesep])

# Generated at 2022-06-14 09:12:57.045390
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text(corrected_command='lsa') == u'{prefix}{clear}{bold}{script}{reset}{side_effect} [{green}enter{reset}/{blue}↑{reset}/{blue}↓{reset}/{red}ctrl+c{reset}]'

# Generated at 2022-06-14 09:13:01.883564
# Unit test for function debug_time
def test_debug_time():
    """assert that it prints time only in debug mode."""
    from mock import patch
    with patch('thefuck.shells.get_settings', lambda:[mock.DEFAULT, False, False]):
        with debug_time('Mock debug message'):
            pass

# Generated at 2022-06-14 09:13:06.447737
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import StringIO

    try:
        sys.stderr = output = StringIO.StringIO()
        show_corrected_command('test')

        assert output.getvalue() == '> test\n'

    finally:
        sys.stderr = sys.__stderr__

# Generated at 2022-06-14 09:13:11.589021
# Unit test for function confirm_text
def test_confirm_text():
    prev_len = len(const.USER_COMMAND_MARK)
    confirm_text(const.USER_COMMAND_MARK + "ls")
    assert len(const.USER_COMMAND_MARK + "ls") == prev_len

# Generated at 2022-06-14 09:13:13.977676
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text('pwd') == '>>> pwd [enter/↑/↓/ctrl+c]'

# Generated at 2022-06-14 09:13:22.517320
# Unit test for function debug_time
def test_debug_time():
    import time

    with debug_time('test'):
        time.sleep(1)


if __name__ == '__main__':
    test_debug_time()

# Generated at 2022-06-14 09:13:35.944893
# Unit test for function debug
def test_debug():
    from .conf import update_settings
    from .config import _load_config
    from .utils import debug
    from .compat import py2, py3
    from . import const
    from . import __version__

    import sys
    if py2:
        from StringIO import StringIO
    else:
        from io import StringIO

    stdout = sys.stdout
    stderr = sys.stderr

    with StringIO() as buf:
        sys.stdout = buf
        sys.stderr = buf

        update_settings(None, _load_config(), None, None, None)
        settings.no_colors = True
        settings.debug = True
        debug('Debug message')

# Generated at 2022-06-14 09:13:38.156028
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = 'git push origin'
    show_corrected_command(corrected_command)
    return True

# Generated at 2022-06-14 09:13:51.744332
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .repl import CorrectedCommand
    from .shells import Shell
    from .shells.bash import Bash
    from .shells.zsh import Zsh
    from .shells.fish import Fish
    from .shells.tcsh import Tcsh
    from .shells.xonsh import Xonsh

    # Inputs
    cmd_a = 'sudo !!'
    cmd_b = 'sudo ls'
    cmd_c = 'remove --help'
    cmd_d = ''
    cmd_e = 'echo Hello, world'

    # Outputs
    out_a = 'sudo '
    out_b = 'sudo mv'
    out_c = 'remove -h'
    out_d = 'rm'
    out_e = 'echo Hello, world'

    side_effect_a = False
    side