

# Generated at 2022-06-14 09:04:03.156075
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    import os
    import tempfile

    def get_configuration_details():
        return conf.ConfigurationDetails(
            path=os.path.join(tempfile.mkdtemp(), '.bashrc'),
            content=u'eval "$(thefuck --alias)"',
            reload=u'exec -l "$SHELL"',
            can_configure_automatically=True)

    how_to_configure_alias(get_configuration_details())

# Generated at 2022-06-14 09:04:05.215489
# Unit test for function debug_time
def test_debug_time():
    # nothing to test.
    # i don't know how to test a function which could run forever.
    pass

# Generated at 2022-06-14 09:04:09.611840
# Unit test for function color
def test_color():
    assert color(colorama.Style.RESET_ALL) == ''
    assert color(colorama.Style.RESET_ALL) == ''
    settings.no_colors = False
    assert color(colorama.Style.RESET_ALL) == colorama.Style.RESET_ALL

# Generated at 2022-06-14 09:04:12.585264
# Unit test for function debug_time
def test_debug_time():
    import time
    with debug_time('test'):
        time.sleep(1)



# Generated at 2022-06-14 09:04:15.756739
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .corrector import CorrectedCommand
    corrected_command = CorrectedCommand('command', True)
    show_corrected_command(corrected_command)
    assert True



# Generated at 2022-06-14 09:04:25.342162
# Unit test for function debug
def test_debug():
    from textwrap import dedent

    with debug_time('foo'):
        debug(u'bar')
        debug(u'baz')

    assert sys.stderr.getvalue() == dedent(u"""\
        {blue}{bold}DEBUG:{reset} bar
        {blue}{bold}DEBUG:{reset} baz
        {blue}{bold}DEBUG:{reset} foo took: 0:00:00.000
        """.format(
            blue=color(colorama.Fore.BLUE),
            bold=color(colorama.Style.BRIGHT),
            reset=color(colorama.Style.RESET_ALL)))

# Generated at 2022-06-14 09:04:26.861401
# Unit test for function debug
def test_debug():
    sys.stderr = StringIO()

# Generated at 2022-06-14 09:04:29.033146
# Unit test for function debug_time
def test_debug_time():
    """Unit test for function debug_time."""
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:04:38.361092
# Unit test for function debug
def test_debug():
    from cStringIO import StringIO
    from .conf import settings
    from . import const
    settings.debug = True
    msg = 'Debug message'
    stream = StringIO()
    with settings.captured_output(stream):
        debug(msg)
    assert stream.getvalue().strip() == const.USER_COMMAND_MARK + \
        color(colorama.Fore.BLUE + colorama.Style.BRIGHT) + \
        'DEBUG:' + color(colorama.Style.RESET_ALL) + ' ' + msg



# Generated at 2022-06-14 09:04:45.419420
# Unit test for function debug
def test_debug():
    from .conf import settings
    from io import StringIO
    from datetime import timedelta
    settings.debug = True
    old = sys.stderr
    sys.stderr = StringIO()
    debug('test')
    result = sys.stderr.getvalue()
    sys.stderr.close()
    sys.stderr = old
    assert result == '\x1b[94m\x1b[1mDEBUG:\x1b[0m test\n'



# Generated at 2022-06-14 09:05:01.230277
# Unit test for function color
def test_color():
    from os import environ
    from os import devnull
    from os import remove
    from os import environ
    from os import devnull
    from os import remove
    from tempfile import mkstemp
    from shutil import move
    from thefuck.utils import capture

    true = 'true'
    alias = 'alias fuck="env PYTHONUNBUFFERED=true {0}"'.format(true)

    with open(devnull, 'w') as null:
        # Set alias without color test
        environ['TF_NO_COLORS'] = '1'
        with open(devnull, 'w') as null:
            with capture(null) as out:
                fix([true])
        assert out.read() == alias, "Color was added to alias when TF_NO_COLORS=1"

# Generated at 2022-06-14 09:05:07.246334
# Unit test for function show_corrected_command
def test_show_corrected_command():
    class FakeCorrectedCommand(object):
        def __init__(self, script):
            self.script = script
            self.side_effect = False

    show_corrected_command(FakeCorrectedCommand('test_script/test'))
    assert sys.stderr.getvalue() == u'$ test_script/test\n'

    sys.stderr.truncate(0)

    show_corrected_command(FakeCorrectedCommand('test_script/test'))
    assert sys.stderr.getvalue() == u'$ test_script/test\n'

    sys.stderr.truncate(0)

    show_corrected_command(
        FakeCorrectedCommand('test_script/test.plus.side.effect'))

# Generated at 2022-06-14 09:05:10.253689
# Unit test for function debug
def test_debug():
    debug("Hello")



# Generated at 2022-06-14 09:05:13.645781
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .shells.bash import Bash
    from .utils import attr

    corrected_command = attr(script=u'ls', side_effect=True)
    show_corrected_command(corrected_command)


if __name__ == '__main__':
    test_show_corrected_command()

# Generated at 2022-06-14 09:05:15.393991
# Unit test for function show_corrected_command
def test_show_corrected_command():
    assert show_corrected_command(corrected_command) == None

# Generated at 2022-06-14 09:05:19.600821
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = type('', (), {
        'script': 'echo "Hello, World!"',
        'side_effect': True})
    show_corrected_command(corrected_command)
    assert '' in sys.stderr.getvalue()



# Generated at 2022-06-14 09:05:24.690189
# Unit test for function confirm_text
def test_confirm_text():
    from .shells.base import Shell
    from .command import Command

    with Shell('bash') as shell:
        confirm_text(Command('echo "corrected"', 'echo "original"', '',
                             side_effect=True))

# Generated at 2022-06-14 09:05:26.549569
# Unit test for function color
def test_color():
    assert color('test') == 'test'
    settings.no_colors = True
    assert color('test') == ''

# Generated at 2022-06-14 09:05:33.874868
# Unit test for function show_corrected_command
def test_show_corrected_command():
    sys.stderr.write("\033[1K\r")
    show_corrected_command("vim")
    sys.stderr.write("\033[1K\r")
    show_corrected_command("vim -p")
    sys.stderr.write("\033[1K\r")
    show_corrected_command("vim -p")

# Generated at 2022-06-14 09:05:35.277152
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:05:45.192046
# Unit test for function debug
def test_debug():
    import StringIO
    stream = StringIO.StringIO()
    settings.debug = True
    sys.stderr = stream
    debug("test debug message")
    assert "DEBUG: test debug message" in stream.getvalue()[:-1]
    settings.debug = False
    stream.close()

if __name__ == '__main__':
    test_debug()

# Generated at 2022-06-14 09:05:51.210416
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(
        ConfigurationDetails('.', 'fuck --alias', 'source ~/.bashrc'))
    how_to_configure_alias(
        ConfigurationDetails('.', 'fuck --alias', 'source ~/.zshrc'))
    how_to_configure_alias(None)



# Generated at 2022-06-14 09:06:01.793421
# Unit test for function confirm_text
def test_confirm_text():
    import io
    import sys
    import tempfile
    from contextlib import contextmanager

    @contextmanager
    def _stdout_redirected(stdout=None):
        old_stdout = sys.stdout
        if stdout is None:
            stdout = tempfile.TemporaryFile()
        sys.stdout = stdout
        try:
            yield stdout
        finally:
            sys.stdout = old_stdout
            stdout.seek(0)

    with _stdout_redirected() as fake_stdout:
        confirm_text('test')
        fake_stdout.read() == '>test [enter/↑/↓/ctrl+c] '

# Generated at 2022-06-14 09:06:05.578880
# Unit test for function color
def test_color():
    assert color(colorama.Fore.RED + 'red') == colorama.Fore.RED + 'red'
    assert color(colorama.Fore.RED + 'red') != ''
    assert color('') == ''


# Generated at 2022-06-14 09:06:06.968920
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = u'command1'
    confirm_text(corrected_command)

# Generated at 2022-06-14 09:06:16.705165
# Unit test for function debug
def test_debug():
    from StringIO import StringIO
    output = StringIO()
    old_stdout = sys.stderr
    try:
        sys.stderr = output
        debug(u'foo')
        output.seek(0)
        assert output.read() == 'foo\n'

        output.seek(0)
        output.truncate()
        settings.debug = False
        debug(u'foo')
        output.seek(0)
        assert output.read() == ''
    finally:
        sys.stderr = old_stdout

# Generated at 2022-06-14 09:06:18.551505
# Unit test for function debug
def test_debug():
    """Test function debug()."""
    debug('debug msg')
    assert True

# Generated at 2022-06-14 09:06:24.085066
# Unit test for function color
def test_color():
    assert color(colorama.Fore.BLACK + 'test') == '\033[30mtest'
    assert color(colorama.Fore.BLACK + 'test', True) == '\033[30mtest'
    assert color(colorama.Fore.BLACK + 'test', False) == 'test'

# Generated at 2022-06-14 09:06:30.971007
# Unit test for function color
def test_color():
    assert(color('') == '')
    assert(color('\x03{}') == '\x03{}')
    assert(color(colorama.Back.RED) == '\x1b[41m')
    assert(color(colorama.Fore.WHITE) == '\x1b[37m')
    assert(color(colorama.Style.BRIGHT) == '\x1b[1m')
    assert(color(colorama.Style.RESET_ALL) == '\x1b[0m')



# Generated at 2022-06-14 09:06:32.624480
# Unit test for function debug
def test_debug():
    from thefuck.utils import set_debug

    set_debug(True)
    debug('msg')



# Generated at 2022-06-14 09:06:41.070523
# Unit test for function debug_time
def test_debug_time():
    import time

    with debug_time('foo'):
        time.sleep(0.1)


if __name__ == '__main__':
    test_debug_time()

# Generated at 2022-06-14 09:06:42.670887
# Unit test for function color
def test_color():
    assert color(None) == ''

# Generated at 2022-06-14 09:06:44.770597
# Unit test for function debug_time
def test_debug_time():
    import time

    with debug_time('testing function debug_time'):
        time.sleep(1)

# Generated at 2022-06-14 09:06:46.469803
# Unit test for function color
def test_color():
    assert color('red') == colorama.Fore.RED
    assert color('red') == ''

# Generated at 2022-06-14 09:06:48.012013
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = {'history.at': 'some_command',
                         'corrected_command': 'some_',
                         'side_effect': False,
                         'script': 'some_command',
                         'side_effect_message': None}
    confirm_text(corrected_command)

# Generated at 2022-06-14 09:06:53.142459
# Unit test for function debug_time
def test_debug_time():
    # python -m thefuck.shells.posix --debug
    #     >> DEBUG:TTTT took: 0:00:00.000001
    with debug_time("TTTT"):
        pass

if __name__ == '__main__':
    test_debug_time()

# Generated at 2022-06-14 09:06:55.349045
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        for i in range(1, 1000000):
            i += i

# Generated at 2022-06-14 09:07:00.077473
# Unit test for function debug
def test_debug():
    from test.utils import captured_output

    with captured_output() as (out, err):
        debug('foo')

    out, err = out.getvalue(), err.getvalue()
    assert out == '\n'
    assert err == '\x1b[34m\x1b[1mDEBUG:\x1b[0m foo\n'



# Generated at 2022-06-14 09:07:01.069927
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:07:03.871889
# Unit test for function debug
def test_debug():
    """
    >>> debug('test')
    \x1b[34m\x1b[1mDEBUG:\x1b[0m test
    """

# Generated at 2022-06-14 09:07:14.260106
# Unit test for function debug_time
def test_debug_time():
    from mock import patch
    with patch('sys.stderr.write') as write:
        with debug_time('test'):
            pass
        assert ('test took: ' in write.call_args[0][0])


if __name__ == '__main__':
    test_debug_time()

# Generated at 2022-06-14 09:07:18.562082
# Unit test for function debug
def test_debug():
    import sys
    import mock

    with mock.patch.object(sys, 'stderr', autospec=True) as stderr:
        debug(u'test')
        stderr.write.assert_called_once_with(u'DEBUG: test\n')
    settings.debug = False
    debug(u'test')
    assert stderr.write.call_count == 1

# Generated at 2022-06-14 09:07:20.799376
# Unit test for function debug
def test_debug():
    with debug_time('test') as debug_time_f:
        debug(u'test message')
        assert True



# Generated at 2022-06-14 09:07:22.214031
# Unit test for function confirm_text
def test_confirm_text():
    show_corrected_command('ls -la')

# Generated at 2022-06-14 09:07:24.145012
# Unit test for function debug_time
def test_debug_time():
    test_data = '12345678'
    with debug_time(test_data):
        pass

# Generated at 2022-06-14 09:07:28.926217
# Unit test for function debug
def test_debug():
    from StringIO import StringIO
    std = sys.stderr
    try:
        sys.stderr = StringIO()
        debug(u'msg')
        assert sys.stderr.getvalue() == u'DEBUG: msg\n'
    finally:
        sys.stderr = std



# Generated at 2022-06-14 09:07:33.443053
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = const.CorrectedCommand('pip install', True)
    confirm_text(corrected_command)
    assert writer == "  ~$ pip install +side effec [enter/↑/↓/ctrl+c]"

# Generated at 2022-06-14 09:07:36.821128
# Unit test for function color
def test_color():
    assert color('red')('red') == '\x1b[31mred\x1b[0m'
    assert color('red') == 'red'

# Generated at 2022-06-14 09:07:44.915038
# Unit test for function debug
def test_debug():
    from io import StringIO
    io = StringIO()
    sys.stderr = io
    debug('debug message')
    assert io.getvalue() == ''

    sys.stderr = StringIO()
    settings.debug = True
    debug('debug message')
    assert io.getvalue() == '\x1b[34m\x1b[1mDEBUG:\x1b[0m debug message\n'



# Generated at 2022-06-14 09:07:52.435280
# Unit test for function debug
def test_debug():
    msg = 'Hello'
    result = u'{blue}{bold}DEBUG:{reset} {msg}\n'.format(
        msg=msg,
        reset=color(colorama.Style.RESET_ALL),
        blue=color(colorama.Fore.BLUE),
        bold=color(colorama.Style.BRIGHT))
    
    assert debug(msg) == result

# Generated at 2022-06-14 09:08:02.348646
# Unit test for function color
def test_color():
    assert color(colorama.Fore.GREEN + 'hello') == '\x1b[32mhello'
    settings.no_colors = True
    assert color(colorama.Fore.GREEN + 'hello') == ''

# Generated at 2022-06-14 09:08:13.632373
# Unit test for function debug
def test_debug():
    class MockStderr(object):
        def __init__(self):
            self._msg = None

        def write(self, msg):
            self._msg = msg

        @property
        def msg(self):
            return self._msg

    mock = MockStderr()
    with settings.using(debug=True):
        debug(u'foo')
        assert mock.msg == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m foo\n'

    mock = MockStderr()
    with settings.using(debug=True, no_colors=True):
        debug(u'foo')
        assert mock.msg == u'DEBUG: foo\n'

    with settings.using(debug=False):
        debug(u'foo')

# Generated at 2022-06-14 09:08:16.898084
# Unit test for function debug_time
def test_debug_time():
    result = u'test'
    with debug_time(u'test_debug'):
        result = u'test1'

    assert result == u'test1'

# Generated at 2022-06-14 09:08:18.944835
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test') as result:
        pass



# Generated at 2022-06-14 09:08:23.928643
# Unit test for function debug
def test_debug():
    debug_msg = 'debug test'
    settings.debug = False
    debug(debug_msg)
    settings.debug = True
    settings.no_colors = True
    debug(debug_msg)
    settings.no_colors = False
    debug(debug_msg)

# Generated at 2022-06-14 09:08:30.093285
# Unit test for function debug
def test_debug():
    from StringIO import StringIO
    from . import conf

    stdout = sys.stdout
    try:
        sys.stdout = StringIO()
        conf.settings.debug = True
        debug('debug message')
        assert 'DEBUG' in sys.stdout.getvalue()
    finally:
        sys.stdout = stdout

# Generated at 2022-06-14 09:08:31.221500
# Unit test for function debug
def test_debug():
    assert debug('test') is None

# Generated at 2022-06-14 09:08:31.907281
# Unit test for function debug
def test_debug():
    debug('Whatever')

# Generated at 2022-06-14 09:08:35.618035
# Unit test for function color
def test_color():
    colorama.init()
    assert color(colorama.Fore.RED) == colorama.Fore.RED

    settings.no_colors = True
    assert color(colorama.Fore.RED) == u''

# Generated at 2022-06-14 09:08:39.386482
# Unit test for function debug_time
def test_debug_time():
    from mock import patch

    with patch('sys.stderr') as stderr:
        with debug_time('foo'):
            pass
        debug_time('foo')

    stderr.write.assert_has_calls(
        [mock.call(u'\033[94m\033[1mDEBUG:\033[0m foo took: 0:00:00\n')] * 2)

# Generated at 2022-06-14 09:08:48.966264
# Unit test for function debug
def test_debug():

    from contextlib import contextmanager
    from mock import MagicMock, patch
    from nose.tools import istest
    from thefuck.main import debug

    @istest
    @contextmanager
    def debug_enabled():
        with patch('thefuck.main.settings') as settings:
            settings.debug = True
            stderr = MagicMock()
            with patch('thefuck.main.sys') as sys:
                sys.stderr = stderr
                yield stderr

    @istest
    def shows_message_when_enabled():
        with debug_enabled() as stderr:
            debug(u'Test message')
            assert stderr.write.called

    @istest
    def doesnt_show_message_without_debug():
        with patch('thefuck.main.sys') as sys:
            sys

# Generated at 2022-06-14 09:08:56.722354
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from thefuck.utils import ConfigurationDetails
    configuration_details = ConfigurationDetails(
        '~/.profile',
        'alias fuck=\'eval `thefuck $(fc -ln -1)`\'',
        'source ~/.profile',
        False
    )


# Generated at 2022-06-14 09:08:57.673659
# Unit test for function debug_time
def test_debug_time():
    pass

# Generated at 2022-06-14 09:09:01.583483
# Unit test for function debug_time
def test_debug_time():
    import thefuck
    from datetime import datetime, timedelta
    from freezegun import freeze_time
    import mock

    with mock.patch.object(thefuck.log, 'debug') as mock_debug, \
            freeze_time(datetime.now() + timedelta(seconds=5)):
        with thefuck.log.debug_time('test'):
            pass

    mock_debug.assert_called_once_with('test took: 0:00:05')

# Generated at 2022-06-14 09:09:06.365444
# Unit test for function color
def test_color():
    assert color(u'Bold') == u'\x1b[1mBold\x1b[22m'
    assert color(u'Bold') != u'Bold'



# Generated at 2022-06-14 09:09:12.922663
# Unit test for function confirm_text
def test_confirm_text():
    original_command = u'echo "Hello World"'
    corrected_command = u'echo "Hello, World"'
    user_command_mark = u'/bin/bash -c "cd $(dirname $0); '
    user_command_mark += corrected_command + '"'
    confirm_text(user_command_mark)
    assert user_command_mark == sys.stderr.getvalue()
    sys.stderr.close()

# Generated at 2022-06-14 09:09:14.176874
# Unit test for function debug
def test_debug():
    assert debug("test") is None
    return True

# Generated at 2022-06-14 09:09:16.520861
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        time.sleep(1)

# Generated at 2022-06-14 09:09:17.997229
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:09:19.516770
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:09:26.049479
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text({'script': 'thefuck',
                  'side_effect': None})

# Generated at 2022-06-14 09:09:34.512450
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .shells.posix import Posix
    from .shells.get_alias import get_alias
    from .shells.get_shell import get_shell
    from .shells.which import which
    import sys
    import os

    configuration_details = Posix.get_aliases()[0]().from_shell(
        get_shell(), get_alias())
    debug(configuration_details)

    tmp_file = u'fuck-the-example-config'
    path = os.path.abspath(tmp_file)
    config_lines = u'\n'.join(configuration_details.prefix + configuration_details.suffix)
    with open(path,'w') as f:
        f.write(config_lines)

    configuration_details = which(tmp_file)
    configuration_details = configuration_

# Generated at 2022-06-14 09:09:38.399000
# Unit test for function color
def test_color():
    assert color(u'red') == ''
    assert color(u'\033[31mred\033[0m') == '\033[31mred\033[0m'

# Generated at 2022-06-14 09:09:39.491632
# Unit test for function debug_time
def test_debug_time():
    with debug_time('msg'):
        pass

# Generated at 2022-06-14 09:09:40.932260
# Unit test for function debug_time
def test_debug_time():
    with debug_time('Foo'):
        pass

# Generated at 2022-06-14 09:09:47.846625
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = type('Command', (object,), {'script':
                                                    'git push origin master --force-with-lease',
                                                    'side_effect': True})

# Generated at 2022-06-14 09:09:49.126236
# Unit test for function debug
def test_debug():
    assert debug('Hello!') == None



# Generated at 2022-06-14 09:10:00.140822
# Unit test for function confirm_text
def test_confirm_text():
    import pytest
    from mock import Mock, patch
    sys.stderr = Mock()
    confirm_text(Mock(side_effect=True, script='foo'))
    sys.stderr.write.assert_called_once_with(
        u'f{clear}foo (+side effect) [{green}enter{reset}/{blue}↑{reset}/{blue}↓{reset}/{red}ctrl+c{reset}]'.format(
            clear='\033[1K\r',
            green=color(colorama.Fore.GREEN),
            red=color(colorama.Fore.RED),
            reset=color(colorama.Style.RESET_ALL),
            blue=color(colorama.Fore.BLUE)))

# Generated at 2022-06-14 09:10:03.719161
# Unit test for function debug_time
def test_debug_time():
    return 1
    started = datetime.now()
    try:
        yield
    finally:
        debug(u'{} took: {}'.format(msg, datetime.now() - started))

# Generated at 2022-06-14 09:10:04.766632
# Unit test for function debug_time
def test_debug_time():
    with debug_time(u'something'):
        pass


# Generated at 2022-06-14 09:10:18.509974
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    fake_details = const.ConfigurationDetails(
        path='path',
        content='content',
        can_configure_automatically=True)

    def _test(expected, details):
        got = list(how_to_configure_alias(fake_details))
        assert expected == got

    colorama.init(autoreset=True)

# Generated at 2022-06-14 09:10:20.805583
# Unit test for function color
def test_color():
    assert color(colorama.Fore.BLUE) == colorama.Fore.BLUE
    assert color('Color') == ''

# Generated at 2022-06-14 09:10:21.215204
# Unit test for function debug
def test_debug():
    debug('debug')

# Generated at 2022-06-14 09:10:22.174152
# Unit test for function color
def test_color():
    assert color(42) == 42

# Generated at 2022-06-14 09:10:31.901615
# Unit test for function confirm_text
def test_confirm_text():
    from .application import Application
    from .conf import Settings
    from .shells import Shell
    from .completion import Completion
    from .rules import Rule
    from .replacements import Replacement
    from tests.utils import mock, patch
    from thefuck import shells
    with patch('sys.stderr') as stderr:
        with patch.multiple(
                shells, bash=mock.MagicMock(), zsh=mock.MagicMock()):
            shell = Shell(
                'bash', 'bash', Completion(),
                '/usr/local/bin/fuck', '', '', '')

# Generated at 2022-06-14 09:10:40.850508
# Unit test for function debug
def test_debug():
    def test(value):
        settings.debug = value
        debug(u'foo')
    assert test(True) == sys.stderr.write(u'{blue}{bold}DEBUG:{reset} {msg}\n'.format(
            msg=u'foo',
            reset=color(colorama.Style.RESET_ALL),
            blue=color(colorama.Fore.BLUE),
            bold=color(colorama.Style.BRIGHT)))
    assert test(False) is None

# Generated at 2022-06-14 09:10:43.933644
# Unit test for function color
def test_color():
    assert color(u'') == u''
    settings.no_colors = False
    assert color(u'abc') == u'abc'

# Generated at 2022-06-14 09:10:45.462443
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:10:53.504293
# Unit test for function debug
def test_debug():
    import mock
    import random
    import string
    with mock.patch('thefuck.utils.settings') as settings_mock:
        settings_mock.debug = True
        test_string = ''.join([random.choice(string.letters) for i in xrange(1000)])
        with mock.patch('thefuck.utils.sys.stderr.write') as sys_mock:
            sys_mock.return_value = None
            debug(test_string)
        sys_mock.assert_called_with(test_string)



# Generated at 2022-06-14 09:10:54.282696
# Unit test for function debug
def test_debug():
    debug('test debug')

# Generated at 2022-06-14 09:11:02.293137
# Unit test for function debug_time
def test_debug_time():
    import time
    with debug_time('test'):
        time.sleep(0.3)
    with debug_time('test'):
        time.sleep(0.3)

# Generated at 2022-06-14 09:11:04.644404
# Unit test for function confirm_text
def test_confirm_text():
    script = 'git commit'
    side_effect = True
    confirm_text(script, side_effect)

# Generated at 2022-06-14 09:11:12.295935
# Unit test for function debug
def test_debug():
    """
    Test for checking if messages output to stderr have 'DEBUG' prefix if
    debug mode is enabled.
    """
    import six
    from test.lib import mock_settings
    from mock import patch, Mock

    stderr_mock = Mock()
    with mock_settings(debug=True):
        with patch('sys.stderr', stderr_mock):
            debug('message_without_prefix')
    stderr_mock.write.assert_called_once_with(six.u('\x1b[34m\x1b[1m'
                                                    'DEBUG:'
                                                    '\x1b[m message_'
                                                    'without_prefix\n'))



# Generated at 2022-06-14 09:11:15.745726
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    configuration_details = settings.Configuration('', '', '', False, False)
    how_to_configure_alias(configuration_details)


# Generated at 2022-06-14 09:11:20.946897
# Unit test for function color
def test_color():
    assert color('string') == 'string'
    settings.no_colors = True
    assert color('string') == ''

# Generated at 2022-06-14 09:11:28.468575
# Unit test for function confirm_text
def test_confirm_text():
    from . import shell
    shell.Shell('bash')
    from .conf import settings
    settings.no_colors = False
    confirm_text(None)
    confirm_text()



# Generated at 2022-06-14 09:11:31.722210
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    from time import sleep
    debug_time('dd')
    assert (datetime.now() - started) > timedelta(0)

# Generated at 2022-06-14 09:11:32.925141
# Unit test for function debug_time
def test_debug_time():
    debug_time('test_debug_time')

# Generated at 2022-06-14 09:11:34.774100
# Unit test for function debug_time
def test_debug_time():
    with debug_time('time'):
        pass

# Generated at 2022-06-14 09:11:37.252326
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test') as td:
        pass

test_debug_time()

# Generated at 2022-06-14 09:11:49.009967
# Unit test for function confirm_text
def test_confirm_text():
    from .utils import wrap_streams, confirm_text, read_input

    with wrap_streams() as (out, _):
        confirm_text('ls /nonexistent')
        assert out.getvalue().startswith(const.USER_COMMAND_MARK)
        assert out.getvalue().endswith('[enter/↑/↓/ctrl+c]')



# Generated at 2022-06-14 09:11:54.571288
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(const.ConfigureDetails(
        reload='reload',
        path='path',
        can_configure_automatically='can_configure_automatically',
        content='contents'))

    how_to_configure_alias(None)


# Generated at 2022-06-14 09:11:57.354156
# Unit test for function debug_time
def test_debug_time():
    started = datetime.now()
    with debug_time('test'):
        pass
    debug(u'{} took: {}'.format('test', datetime.now() - started))

# Generated at 2022-06-14 09:12:03.997835
# Unit test for function confirm_text
def test_confirm_text():
    # test correct output
    confirm_text_result = u'[fuck]$ npm install express [enter/↑/↓/ctrl+c] '
    settings.no_colors = True
    assert confirm_text('npm install express') == confirm_text_result
    # test correct output with colorama
    settings.no_colors = False
    assert confirm_text('npm install express') == (u'\033[1K\r[fuck]$ npm install express '
                                                   u'[\x1b[0m\x1b[32menter\x1b[0m/\x1b[34m↑\x1b[0m/\x1b[34m↓\x1b[0m/\x1b[31mctrl+c\x1b[0m] ')

# Generated at 2022-06-14 09:12:08.812902
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text('ls -l') == '{prefix}{script} [{green}enter{reset}/{blue}↑{reset}/{blue}↓{reset}/{red}ctrl+c{reset}]'

# Generated at 2022-06-14 09:12:14.177917
# Unit test for function confirm_text
def test_confirm_text():
    class Mock(object):
        def __init__(self, script, side_effect=False):
            self.script = script
            self.side_effect = side_effect
    corrected_command = Mock(u'echo abc', True)
    confirm_text(corrected_command)

# Generated at 2022-06-14 09:12:16.768853
# Unit test for function color
def test_color():
    assert color('green') == colorama.Fore.GREEN
    assert color('') == ''
    assert color('green') == ''

# Generated at 2022-06-14 09:12:32.845461
# Unit test for function confirm_text
def test_confirm_text():
    import textwrap
    import sys
    sys.stdout = open('test.txt', 'w')

# Generated at 2022-06-14 09:12:34.905616
# Unit test for function debug
def test_debug():
    assert debug('message') == None

# Generated at 2022-06-14 09:12:38.953364
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from thefuck.shells import BourneAgainShell

    how_to_configure_alias(BourneAgainShell().get_configuration_file_path())



# Generated at 2022-06-14 09:12:44.973213
# Unit test for function color
def test_color():
    assert color(u'foo') == u'foo'
    settings.no_colors = True
    assert color(u'foo') == u''

# Generated at 2022-06-14 09:12:48.620496
# Unit test for function debug
def test_debug():
    import StringIO
    import re
    buf = StringIO.StringIO()
    sys.stderr = buf
    debug('Testing')
    buf.seek(0)
    assert(re.match('^DEBUG: Testing\n', buf.read()))



# Generated at 2022-06-14 09:12:53.167382
# Unit test for function confirm_text
def test_confirm_text():
    sys.stderr.write = lambda x: sys.stdout.write(x.encode('utf-8'))
    confirm_text(const.CorrectedCommand(script='test', side_effect=False))
    confirm_text(const.CorrectedCommand(script='test', side_effect=True))

# Generated at 2022-06-14 09:13:04.351409
# Unit test for function debug
def test_debug():
    from . import application
    application.settings = type('TestSettings', (object,), {'debug': False})

    debug('msg')  # Nothing to be printed
    assert sys.stderr.getvalue() == ''

    application.settings = type('TestSettings', (object,), {'debug': True})

    debug('msg')  # Message to be printed
    assert sys.stderr.getvalue() == 'DEBUG: msg\n'

    sys.stderr.seek(0)
    sys.stderr.truncate(0)  # Clean buffer

    application.settings = type('TestSettings', (object,), {'debug': False})

    debug('msg')  # Nothing to be printed
    assert sys.stderr.getvalue() == ''

# Generated at 2022-06-14 09:13:05.361461
# Unit test for function debug_time
def test_debug_time():
    with debug_time('time'):
        assert True

# Generated at 2022-06-14 09:13:09.437314
# Unit test for function color
def test_color():
    assert color(u'foo') == u'foo'
    settings.no_colors = True
    assert color(u'foo') == u''

# Generated at 2022-06-14 09:13:10.806700
# Unit test for function debug
def test_debug():
    assert 'DEBUG: hello_world' in debug('hello_world')



# Generated at 2022-06-14 09:13:13.929263
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .shells import Shell

    configuration_details = Shell.from_cls(None).get_alias()

    how_to_configure_alias(configuration_details)
    assert True

# Generated at 2022-06-14 09:13:15.991994
# Unit test for function debug_time
def test_debug_time():
    @contextmanager
    def a():
        yield
    with debug_time('foo'):
        a()
    assert True

# Generated at 2022-06-14 09:13:24.473687
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from StringIO import StringIO
    output = StringIO()
    sys.stderr = output
    how_to_configure_alias(None)
    assert output.getvalue()[1:] == """Seems like \x1b[1mfuck\x1b[22m alias isn't configured!
More details - https://github.com/nvbn/thefuck#manual-installation
"""

    output = StringIO()
    sys.stderr = output
    class ConfigurationDetails:
        def __init__(self, can_configure_automatically):
            self.can_configure_automatically = can_configure_automatically
            self.path = '/home/nvbn/.bashrc'
            self.content = 'eval $(thefuck --alias)'
            self.reload = 'source ~/.bashrc'



# Generated at 2022-06-14 09:13:33.318264
# Unit test for function debug
def test_debug():
    from mock import patch

    with patch('sys.stderr') as stderr:
        debug('foo')
        stderr.write.assert_called_once_with(u'\x1b[34m\x1b[1mDEBUG:\x1b[0m foo\n')

# Generated at 2022-06-14 09:13:36.093977
# Unit test for function debug
def test_debug():
    assert not debug('foo bar')



# Generated at 2022-06-14 09:13:47.797588
# Unit test for function confirm_text

# Generated at 2022-06-14 09:13:49.862222
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test_debug_time'):
        assert True

# Generated at 2022-06-14 09:13:57.287774
# Unit test for function confirm_text
def test_confirm_text():
    from contextlib import contextmanager
    from StringIO import StringIO

    @contextmanager
    def nostderr():
        save_stderr = sys.stderr
        sys.stderr = StringIO()
        yield
        sys.stderr = save_stderr

    with nostderr():
        confirm_text('ls abcd')
        assert sys.stderr.getvalue() == (u'$ ls abcd [enter/↑/↓/ctrl+c]')
        confirm_text('ls abcd')
        assert sys.stderr.getvalue() == (
            u'$ ls abcd [enter/↑/↓/ctrl+c]\r\x1b[1K$ ls abcd [enter/↑/↓/ctrl+c]')