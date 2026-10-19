

# Generated at 2022-06-14 09:03:57.367544
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text(None) == None


# Generated at 2022-06-14 09:04:06.353881
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    assert color('\033[0m') == ''
    assert color(colorama.Back.RED + colorama.Fore.WHITE
                 + colorama.Style.BRIGHT) == ''

    warn('')
    rule_failed(None, None)
    exception('', None)
    failed('')
    show_corrected_command(None)
    confirm_text(None)
    debug('')
    with debug_time(''):
        pass
    how_to_configure_alias(None)
    already_configured(None)
    configured_successfully(None)
    version(None, None, None)

# Generated at 2022-06-14 09:04:07.616344
# Unit test for function show_corrected_command
def test_show_corrected_command():
    # assert show_corrected_command(corrected_command) == sys.stderr.write(...)
    pass



# Generated at 2022-06-14 09:04:08.701562
# Unit test for function debug
def test_debug():
    debug(u'Unit test')

# Generated at 2022-06-14 09:04:09.719848
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:04:11.781236
# Unit test for function confirm_text
def test_confirm_text():
    assert(confirm_text(None) == None)

# Generated at 2022-06-14 09:04:18.686680
# Unit test for function show_corrected_command
def test_show_corrected_command():
    cmd = corrected_command('ls', 'ls -l', True)
    stdout = StringIO()
    with patch('sys.stdout', stdout):
        show_corrected_command(cmd)
    assert stdout.getvalue() == '\x1b[43m\x1b[30m\x1b[1m(tf) ls -l (+side effect)\x1b[0m\n'


# Generated at 2022-06-14 09:04:21.086629
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = {'script': 'test', 'side_effect': True}
    show_corrected_command(corrected_command)

# Generated at 2022-06-14 09:04:24.523784
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = corrected_command('ls -ltr /')
    assert show_corrected_command(corrected_command) == '> ls -ltr /'



# Generated at 2022-06-14 09:04:26.198184
# Unit test for function debug
def test_debug():
    settings.debug = False
    debug('debug message')
    settings.debug = True
    debug('debug message')

# Generated at 2022-06-14 09:04:31.520089
# Unit test for function debug_time
def test_debug_time():
    import time

    def sleeping():
        time.sleep(0.1)

    with debug_time('sleeping'):
        sleeping()

# Generated at 2022-06-14 09:04:33.033466
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text('hello') == 'hello world'

# Generated at 2022-06-14 09:04:36.560473
# Unit test for function debug
def test_debug():
    from mock import Mock
    patch = Mock()
    patch.configure_mock(**{
        '__getattr__.return_value': u'mock'
    })
    with patch as sys:
        debug(u'unit-test')
    sys.stderr.write.assert_called_once_with(
        u'{blue}{bold}DEBUG:{reset} unit-test\n'.format(
            blue=color(colorama.Fore.BLUE),
            bold=color(colorama.Style.BRIGHT),
            reset=color(colorama.Style.RESET_ALL)))


# Generated at 2022-06-14 09:04:40.941011
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .corrected_command import CorrectedCommand
    show_corrected_command(CorrectedCommand('comm --text "text"', False))
    show_corrected_command(CorrectedCommand('comm --text "text"', True))



# Generated at 2022-06-14 09:04:47.289164
# Unit test for function debug
def test_debug():
    settings.debug = True
    sys.stderr = sys.__stderr__
    debug('foo')
    assert sys.stderr.getvalue() == '\x1b[34m\x1b[1mDEBUG:\x1b[0m foo\n'


# Generated at 2022-06-14 09:04:50.354036
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .shells import get_shell_info
    how_to_configure_alias(get_shell_info('zsh')['configuration_details'])



# Generated at 2022-06-14 09:04:52.480988
# Unit test for function color
def test_color():
    colorama.init()

    assert color('red') == colorama.Fore.RED
    assert color('red') == ''

# Generated at 2022-06-14 09:04:56.202959
# Unit test for function debug
def test_debug():
    assert debug('message') is None



# Generated at 2022-06-14 09:05:04.026653
# Unit test for function confirm_text
def test_confirm_text():
    from . import utils
    utils.settings.no_colors = False
    confirm_text(utils.Rule(
        name='name',
        match='(?<!sudo )rm -rf',
        get_new_command=lambda *args: 'sudo rm -rf',
        side_effect=True))



# Generated at 2022-06-14 09:05:07.824194
# Unit test for function debug
def test_debug():
    from mock import patch
    with patch('thefuck.shells.get_closest', return_value=4):
        debug(u'Привет')

# Generated at 2022-06-14 09:05:13.021873
# Unit test for function show_corrected_command
def test_show_corrected_command():
    print(show_corrected_command('ls'))
    print(show_corrected_command('ls').strip())
    assert show_corrected_command('ls').strip() == 'Fuck -> ls'

# Generated at 2022-06-14 09:05:14.932358
# Unit test for function debug_time
def test_debug_time():
    debug_time("test_debug_time").__enter__()

# Generated at 2022-06-14 09:05:24.508252
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    # pylint: disable=protected-access
    assert u"Seems like {bold}fuck{reset} alias isn't configured!".format(
        bold=color(colorama.Style.BRIGHT),
        reset=color(colorama.Style.RESET_ALL)) == how_to_configure_alias(None)
    assert u"Please put {bold}{content}{reset} in your {bold}{path}{reset} and apply changes with {bold}{reload}{reset} or restart your shell.".format(
        bold=color(colorama.Style.BRIGHT),
        reset=color(colorama.Style.RESET_ALL),
        content=None,
        path=None,
        reload=None) == how_to_configure_alias(True)

# Generated at 2022-06-14 09:05:36.532052
# Unit test for function debug
def test_debug():
    from tempfile import NamedTemporaryFile
    from StringIO import StringIO

    stream = StringIO()
    try:
        sys.stderr, origin_stderr = stream, sys.stderr
        debug(u"foo")
        assert stream.getvalue() == u"foo\n"
    finally:
        sys.stderr = origin_stderr

    stream = NamedTemporaryFile()
    try:
        sys.stderr, origin_stderr = stream, sys.stderr
        settings.debug = True
        debug(u"foo")
        assert stream.read() == u"foo\n"
    finally:
        settings.debug = False
        sys.stderr = origin_stderr



# Generated at 2022-06-14 09:05:45.865070
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    expected_result = '''\
Seems like {bold}fuck{reset} alias isn't configured!
Please put {bold}.pyenv/versions/3.4.3/bin/thefuck{reset} in your \
{bold}/Users/Alex/.config/fish/functions/fuck.fish{reset} and apply \
changes with {bold}source ~/.config/fish/functions/fuck.fish{reset} or \
restart your shell.
Or run {bold}fuck{reset} a second time to configure it automatically.
More details - https://github.com/nvbn/thefuck#manual-installation\
'''.format(bold=color(colorama.Style.BRIGHT),
           reset=color(colorama.Style.RESET_ALL))

# Generated at 2022-06-14 09:05:47.757940
# Unit test for function debug_time
def test_debug_time():
    assert datetime.now() == datetime.now()


# Generated at 2022-06-14 09:06:00.170777
# Unit test for function show_corrected_command
def test_show_corrected_command():
    # In order to test if the output is correct TTY is required
    user_input = """
    import sys
    import os
    import fire
    import pexpect
    from .utils import get_closest, replace_argument, wrap_settings
    from .commands import git

    @fire.Fire({})
    def main():
        pass
    """
    import pty
    master, slave = pty.openpty()
    stdout = sys.stdout.fileno()
    old_stdout = os.dup(stdout)
    os.dup2(slave, stdout)
    try:
        os.write(master, user_input.encode("utf-8"))
        show_corrected_command(
            wrap_settings({'command': "ls"}))
    finally:
        os.dup

# Generated at 2022-06-14 09:06:10.444663
# Unit test for function debug
def test_debug():
    import pytest
    from six import StringIO
    from .which import which

    def get_debug_output():
        with pytest.raises(SystemExit):
            debug('test')
        out, err = capsys.readouterr()
        return err

    def set_debug(value):
        settings.debug = value
        settings.no_colors = True

    with pytest.raises(SystemExit):
        debug('test')

    # debug disabled
    set_debug(False)
    assert get_debug_output() == u''

    # debug enabled
    set_debug(True)
    assert get_debug_output() == u'DEBUG: test\n'

    # debug disabled
    set_debug(False)
    test_stream = StringIO()

# Generated at 2022-06-14 09:06:15.351596
# Unit test for function confirm_text
def test_confirm_text():
    from .conf import settings
    settings.debug = True
    settings.no_colors = True
    test_command = 'cd /'
    assert confirm_text(test_command) == "fuck cd / [enter/↑/↓/ctrl+c] "



# Generated at 2022-06-14 09:06:18.214664
# Unit test for function color
def test_color():
    assert color(u'foo') == ''
    settings.no_colors = False
    assert color(u'foo') == u'foo'

# Generated at 2022-06-14 09:06:26.791813
# Unit test for function debug
def test_debug():
    from StringIO import StringIO
    stream = StringIO()
    settings.debug = False
    sys.stderr = stream
    debug('test')
    assert not stream.getvalue()
    stream = StringIO()
    settings.debug = True
    sys.stderr = stream
    debug('test')
    assert stream.getvalue()

# Generated at 2022-06-14 09:06:31.865449
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    call(how_to_configure_alias, None)
    assert_lines(
        'Seems like {bold}fuck{reset} alias isn\'t configured!\n'
        '\n'
        'More details - https://github.com/nvbn/thefuck#manual-installation'.format(
            bold=color(colorama.Style.BRIGHT),
            reset=color(colorama.Style.RESET_ALL)))



# Generated at 2022-06-14 09:06:33.451302
# Unit test for function debug_time
def test_debug_time():
    # this is a trick to cause name error
    with debug_time('a'):
        pass


# Generated at 2022-06-14 09:06:34.332298
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias({})


# Generated at 2022-06-14 09:06:42.221157
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    import os
    import tempfile
    tmpdir = tempfile.mkdtemp()
    os.chdir(tmpdir)
    configuration_details = _ConfigurationDetails(
        path='~/.bashrc',
        content='eval "$(thefuck --alias)"',
        reload='source ~/.bashrc',
        can_configure_automatically=True,
    )
    how_to_configure_alias(configuration_details)



# Generated at 2022-06-14 09:06:49.216374
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from mock import patch, Mock

    with patch('sys.stderr') as mock_stderr:
        corrected_command = Mock()
        corrected_command.script = 'ls'
        corrected_command.side_effect = None
        show_corrected_command(corrected_command)
        mock_stderr.write.assert_called_with(
            u'{}{}{}\n'.format(const.USER_COMMAND_MARK,
                               corrected_command.script,
                               ''))



# Generated at 2022-06-14 09:06:54.429571
# Unit test for function debug
def test_debug():
    from _six import StringIO
    buffer = StringIO()
    old_stdout = sys.stderr
    sys.stderr = buffer
    debug('Debug message')
    sys.stderr = old_stdout
    assert 'Debug message' in buffer.getvalue()



# Generated at 2022-06-14 09:07:00.420741
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = 'SOME_COMMAND'
    expected = u'\x1b[4musername@host\x1b[0m$ SOME_COMMAND\n'

    computed = u'\x1b[4m{prefix}{script}{reset}\n'.format(
        prefix=const.USER_COMMAND_MARK,
        script=corrected_command,
        reset=color(colorama.Style.RESET_ALL))

    assert computed == expected

# Generated at 2022-06-14 09:07:06.691757
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .configuration_details import ConfigurationDetails
    from .shells import Bash
    import random

    details = ConfigurationDetails(can_configure_automatically=True)
    shell_class = Bash
    how_to_configure_alias(details)
    how_to_configure_alias(None)



# Generated at 2022-06-14 09:07:10.438735
# Unit test for function show_corrected_command
def test_show_corrected_command():
    class Command(object):
        script = 'ls'
        side_effect = False

    show_corrected_command(Command)



# Generated at 2022-06-14 09:07:14.729059
# Unit test for function debug
def test_debug():
    assert debug('First debug message') is None


# Generated at 2022-06-14 09:07:15.912473
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug("test")

# Generated at 2022-06-14 09:07:24.642815
# Unit test for function confirm_text
def test_confirm_text():
    from test.output_tests import colors_disabled, colors_enabled

    with colors_enabled():
        with colors_disabled():
            assert confirm_text(
                {'script': 'command', 'side_effect': False}
            ) == u'{prefix}{clear}{script} [{green}enter{reset}/{blue}↑{reset}/{blue}↓{reset}/{red}ctrl+c{reset}]'.format(
                prefix=const.USER_COMMAND_MARK,
                clear='\033[1K\r',
                green='',
                red='',
                reset='',
                blue='',
                script='command'
            )

# Generated at 2022-06-14 09:07:28.804929
# Unit test for function debug_time
def test_debug_time():
    now = datetime.now()

    with debug_time('tester'):
        pass

    assert(u'tester took: 0:00:00.000001' == debug.last_printed)



# Generated at 2022-06-14 09:07:35.507683
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    import mock
    import sys
    with mock.patch.object(sys, 'stdout', mock.Mock()) as mock_stdout:
        how_to_configure_alias(None)
        mock_stdout.write.assert_called_with(const.HOW_TO_CONFIGURE_ALIAS_TEXT)



# Generated at 2022-06-14 09:07:39.088986
# Unit test for function debug
def test_debug():
    from .. import utils
    from mock import patch
    from io import StringIO

    debug_buffer = StringIO()
    with patch.object(utils.sys, 'stderr', debug_buffer):
        utils.debug('Fuck')
        assert (u'{blue}{bold}DEBUG:{reset} Fuck\n'.format(
            reset=color(colorama.Style.RESET_ALL),
            blue=color(colorama.Fore.BLUE),
            bold=color(colorama.Style.BRIGHT))) == debug_buffer.getvalue()

# Generated at 2022-06-14 09:07:48.690826
# Unit test for function debug
def test_debug():
    import mock
    import io
    import cStringIO

    with mock.patch('sys.stderr', new=cStringIO.StringIO()) as s, \
            mock.patch.dict(settings.__dict__, {'debug': True}):
        debug(u'msg')
        assert u'DEBUG: msg' in s.getvalue()

    with mock.patch('sys.stderr', new=cStringIO.StringIO()) as s, \
            mock.patch.dict(settings.__dict__, {'debug': False}):
        debug(u'msg')
        assert len(s.getvalue()) == 0

# Generated at 2022-06-14 09:07:58.415051
# Unit test for function color
def test_color():
    from thefuck.utils import which
    from thefuck.shells.bash import Bash

    assert color('red') == u'\x1b[31m'
    assert color('red') == ''

    settings.no_colors = False
    assert color('red') == u'\x1b[31m'

    settings.require_confirmation = True
    settings.no_colors = False


# Generated at 2022-06-14 09:08:00.127441
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:08:12.913026
# Unit test for function confirm_text
def test_confirm_text():
    import io
    import sys
    from types import SimpleNamespace
    from .utils import confirm_text
    
    class EmptyStringIO(io.StringIO):
        def getvalue(self):
            return ''
    
    class MockArgs(SimpleNamespace):
        pass
    
    args = MockArgs()
    
    args.no_colors = False
    sys.stderr = EmptyStringIO()
    confirm_text(SimpleNamespace(script='test-script', side_effect=False))
    assert sys.stderr.getvalue() == (u'fuck >test-script [enter/↑/↓/ctrl+c]')
    
    args.no_colors = True
    sys.stderr = EmptyStringIO()

# Generated at 2022-06-14 09:08:27.603072
# Unit test for function confirm_text
def test_confirm_text():
    u"""
    from thefuck.ui import confirm_text, show_corrected_command, failed, warn
    from thefuck.rules.sudo import match, get_new_command
    from thefuck.rules.git_push import match, get_new_command
    from thefuck.rules.python_pip import match, get_new_command
    confirm_text(get_new_command('sudo apt-get install fuck'))
    confirm_text(get_new_command('git push'))
    confirm_text(get_new_command('pip install fuck'))
    show_corrected_command(get_new_command('git push', side_effect=True))
    failed('Failed')
    warn('Warn')
    """

# Generated at 2022-06-14 09:08:33.612492
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import StringIO
    import sys
    sys.stderr = StringIO.StringIO()

    show_corrected_command('ls -alh')
    assert sys.stderr.getvalue() == '$ ls -alh\n'

    show_corrected_command('ls -alh +side-effect')
    assert sys.stderr.getvalue() == '$ ls -alh +side-effect\n'

# Generated at 2022-06-14 09:08:37.817610
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import StringIO
    import sys
    buf = StringIO.StringIO()
    sys.stderr = buf
    show_corrected_command('pip install numpy')
    assert(buf.getvalue() == '> pip install numpy\n')
    buf.close()

# Generated at 2022-06-14 09:08:44.202188
# Unit test for function debug_time
def test_debug_time():
    from datetime import datetime
    from datetime import timedelta
    from .conf import settings
    from .utils import duration
    import time
    settings.debug = True

    start = datetime.now()
    time.sleep(1)
    stop = datetime.now()
    assert abs(duration(start, stop) - 1) < 0.1

# Generated at 2022-06-14 09:08:47.377128
# Unit test for function color
def test_color():
    assert not color(colorama.Style.BRIGHT)
    settings.no_colors = False
    assert color(colorama.Style.BRIGHT) == u'\x1b[1m'

# Generated at 2022-06-14 09:08:53.114627
# Unit test for function debug_time
def test_debug_time():
    from mock import patch
    from datetime import datetime, timedelta
    with patch('sys.stderr') as sys_stderr:
        with debug_time('msg'):
            datetime.now = lambda: datetime.now() + timedelta(seconds=1.5)
        sys_stderr.write.assert_called_with(u'msg took: 0:00:01.500000\n')

# Generated at 2022-06-14 09:08:55.456187
# Unit test for function debug_time
def test_debug_time():
    import time

    with debug_time('test'):
        time.sleep(0.5)



# Generated at 2022-06-14 09:09:06.561529
# Unit test for function debug
def test_debug():
    import StringIO
    import os
    import sys
    saved_stderr = sys.stderr
    s = StringIO.StringIO()
    sys.stderr = s
    try:
        os.environ['THEFUCK_DEBUG'] = 'true'
        debug(u'Hello, world')
        os.environ['THEFUCK_DEBUG'] = 'False'
        debug(u'Hello, world')
    finally:
        sys.stderr = saved_stderr
    assert s.getvalue() == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m Hello, world\n'
# test_debug()

# Generated at 2022-06-14 09:09:08.748872
# Unit test for function show_corrected_command
def test_show_corrected_command():
    show_corrected_command(const.CorrectedCommand('git log', False))


# Generated at 2022-06-14 09:09:12.061488
# Unit test for function show_corrected_command

# Generated at 2022-06-14 09:09:23.554020
# Unit test for function confirm_text
def test_confirm_text():
    from .utils import wrap_streams
    from .compat import check_output

    with wrap_streams() as (stdin, stdout, stderr):
        confirm_text(CorrectedCommand('ls'))
        assert stderr.read() == (u'\033[1K\r[>] ls [enter/↑/↓/ctrl+c]')

# Generated at 2022-06-14 09:09:33.442202
# Unit test for function debug
def test_debug():
    from . import common
    from .conf import Settings
    import unittest
    import sys
    import io
    import contextlib
    from datetime import datetime

    @contextlib.contextmanager
    def captured_output():
        new_out, new_err = io.StringIO(), io.StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err

    class OutputTest(unittest.TestCase):
        def test_debug(self):
            with captured_output() as (out, err):
                common.debug('msg')



# Generated at 2022-06-14 09:09:35.992463
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass


# Generated at 2022-06-14 09:09:39.439924
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from thefuck.utils import _how_to_configure_alias
    assert _how_to_configure_alias() == how_to_configure_alias(None)



# Generated at 2022-06-14 09:09:41.124065
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)


# Generated at 2022-06-14 09:09:43.921067
# Unit test for function show_corrected_command
def test_show_corrected_command():
    class corrected_command_dummy:
        script = "ls -l"
        side_effect = True
    show_corrected_command(corrected_command_dummy)
    assert True


# Generated at 2022-06-14 09:09:50.311681
# Unit test for function debug
def test_debug():
    debug(u'Ъбственно я решавам да тествам (за успокояване на съвестта ми)')

# Generated at 2022-06-14 09:10:03.604333
# Unit test for function debug
def test_debug():
    from contextlib import contextmanager
    from datetime import datetime, timedelta

    @contextmanager
    def mock_time():
        start = datetime.now()
        try:
            yield
        finally:
            delta = datetime.now() - start
            delta.seconds = 1
            delta.microseconds = 2

    with mock_time():
        debug_time('test message')
    assert sys.stderr.getvalue() == '\x1b[34m\x1b[1mDEBUG:\x1b[0m test message took: 0:00:01.000002\n'
    sys.stderr.truncate(0)
    sys.stderr.seek(0)
    with mock_time():
        debug('simple message')

# Generated at 2022-06-14 09:10:08.008984
# Unit test for function color
def test_color():
    assert color(const.GREEN) == const.GREEN
    assert color('') == ''
    settings.no_colors = True
    assert color(const.GREEN) == ''
    settings.no_colors = False
    assert color(const.GREEN) == const.GREEN

# Generated at 2022-06-14 09:10:12.429821
# Unit test for function debug_time
def test_debug_time():
    import re

    import mock
    import pytest

    @pytest.yield_fixture()
    def debug_mock(monkeypatch):
        mock_debug = mock.MagicMock()
        monkeypatch.setattr('thefuck.log.debug', mock_debug)
        yield mock_debug

    with debug_time('foo'):
        pass

    debug_mock.assert_called_once_with(re.compile(r'foo took \d+:\d+:\d+\.\d+'))

# Generated at 2022-06-14 09:10:25.747734
# Unit test for function confirm_text
def test_confirm_text():
    from .conf import settings

    settings.no_colors = True
    from . import const
    from .types import CorrectedCommand
    command = CorrectedCommand('ls', False)
    assert confirm_text(command) == '\033[1K\r>>ls [enter/↑/↓/ctrl+c]'
    settings.no_colors = False
    assert confirm_text(command) == '\033[1K\r>>ls [enter/↑/↓/ctrl+c]'

# Generated at 2022-06-14 09:10:27.493527
# Unit test for function confirm_text
def test_confirm_text():
    #default value
    assert confirm_text(None) == None



# Generated at 2022-06-14 09:10:36.074097
# Unit test for function color
def test_color():
    from mock import patch
    from itertools import product
    from functools import partial

    test_cases = [
        ('\x1b[31;1m', 'red', True),
        ('\x1b[31;1m', 'red', False),
        ('', 'red', False),
        ('\x1b[0m', 'reset', True),
        ('\x1b[0m', 'reset', False)
    ]

    def run_test_case(color, color_name, no_colors):
        with patch('thefuck.shells.colorama.init') as init, \
                patch('thefuck.shells.settings.no_colors', no_colors):
            init.return_value = True
            assert color == color_(color_name)


# Generated at 2022-06-14 09:10:40.283085
# Unit test for function debug_time

# Generated at 2022-06-14 09:10:50.221955
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .correct import CorrectedCommand
    from .command import Command
    import sys
    from mock import patch
    from .conf import settings
    from . import const

    sys.argv = ['thefuck', 'ls']
    settings.no_colors = True
    settings.priority = {}

    with patch('sys.stderr', new_callable=lambda: sys.stdout) as sys_stderr:
        show_corrected_command(CorrectedCommand(Command('ls -al'), 'pwd'))
        assert sys_stderr.getvalue() == (
            '{prefix}{bold}{script}{reset}{side_effect}\n'.format(
                prefix=const.USER_COMMAND_MARK,
                script='pwd',
                side_effect='',
                bold='',
                reset=''))



# Generated at 2022-06-14 09:10:52.818644
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    assert 'alias fuck >/dev/null' in how_to_configure_alias(None)



# Generated at 2022-06-14 09:10:54.068074
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text(('ls', True))

# Generated at 2022-06-14 09:10:55.862187
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass



# Generated at 2022-06-14 09:10:57.862847
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text(corrected_command="fuck")
    assert True

# Generated at 2022-06-14 09:11:01.476534
# Unit test for function color
def test_color():
    assert color('test') == 'test'
    settings.no_colors = True
    assert color('test') == ''
    settings.no_colors = False


if __name__ == '__main__':
    test_color()

# Generated at 2022-06-14 09:11:13.280741
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = type("", (object,),
                             {"script": "ls -la",
                              "side_effect": True})
    fake_output = "hell"
    global sys
    old_sys = sys
    sys = type("", (object,),
               {"stderr": StringIO()})
    show_corrected_command(corrected_command)
    sys = old_sys
    assert fake_output == sys.stderr.getvalue()

# Generated at 2022-06-14 09:11:26.484624
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = type('CorrectedCommand', (), {'script': 'ls', 'side_effect': True})
    assert confirm_text(corrected_command) == u'{prefix}ls (+side effect) [{green}enter{reset}/{blue}↑{reset}/{blue}↓{reset}/{red}ctrl+c{reset}]'.format(
            prefix=const.USER_COMMAND_MARK,
            green=color(colorama.Fore.GREEN),
            red=color(colorama.Fore.RED),
            reset=color(colorama.Style.RESET_ALL),
            blue=color(colorama.Fore.BLUE))



# Generated at 2022-06-14 09:11:32.248155
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .rule import Command

    class Dummy:
        pass

    corrected_command = Dummy()
    corrected_command.script = u'ls'
    corrected_command.side_effect = False
    show_corrected_command(corrected_command)

    corrected_command.side_effect = True
    show_corrected_command(corrected_command)

# Generated at 2022-06-14 09:11:40.507047
# Unit test for function debug
def test_debug():
    output = []
    sys.stderr.write = lambda content: output.append(content)

    # DEBUG is disabled
    settings.set('debug', False)
    debug('test')
    assert not output

    # DEBUG is enabled
    settings.set('debug', True)
    debug('test')
    assert output == [u'\x1b[34m\x1b[1mDEBUG:\x1b[0m test\n']



# Generated at 2022-06-14 09:11:45.645643
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .command import Command
    from cStringIO import StringIO
    sys.stderr = StringIO()
    show_corrected_command(Command('git status', 'git status', True))
    expected = u'\x1b[1K\r\x1b[1mfuck\x1b[22m \x1b[1mgit status\x1b[22m (+side effect)\n'
    assert sys.stderr.getvalue() == expected


# Generated at 2022-06-14 09:11:47.449910
# Unit test for function debug_time
def test_debug_time():
    with debug_time('time'):
        pass



# Generated at 2022-06-14 09:11:50.908647
# Unit test for function debug_time
def test_debug_time():
    # Show how long the given code takes.
    import time
    with debug_time('test_debug_time'):
        time.sleep(1)


# Generated at 2022-06-14 09:11:56.708454
# Unit test for function debug
def test_debug():
    import mock
    debug('test')
    mock.assert_called_with(u'{blue}{bold}DEBUG:{reset} test\n'.format(
        reset=color(colorama.Style.RESET_ALL),
        blue=color(colorama.Fore.BLUE),
        bold=color(colorama.Style.BRIGHT)))



# Generated at 2022-06-14 09:11:59.025497
# Unit test for function debug
def test_debug():
    msg = "Test"
    settings.debug = False
    assert debug(msg) == None
    settings.debug = True
    assert debug(msg) == None


# Generated at 2022-06-14 09:12:01.493134
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .corrected_command import CorrectedCommand
    show_corrected_command(CorrectedCommand('ls', False))

# Generated at 2022-06-14 09:12:13.234007
# Unit test for function debug
def test_debug():
    from cStringIO import StringIO
    buff = StringIO()
    old_stderr = sys.stderr
    try:
        sys.stderr = buff
        debug(u'123')
        debug(u'321')
        output = buff.getvalue()
    finally:
        sys.stderr = old_stderr
    assert u'DEBUG: 123\n' in output
    assert u'DEBUG: 321\n' in output



# Generated at 2022-06-14 09:12:16.299716
# Unit test for function color
def test_color():
    assert '\x1b[1m' == color(colorama.Style.BRIGHT)
    assert '' == color(colorama.Style.BRIGHT, force_colors=False)

# Generated at 2022-06-14 09:12:24.956438
# Unit test for function color
def test_color():
    settings.no_colors = True
    assert color(u'\x1b[41m') == ''
    settings.no_colors = False
    assert color(u'\x1b[41m') == u'\x1b[41m'



# Generated at 2022-06-14 09:12:26.540483
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)
# End of unit test

# Generated at 2022-06-14 09:12:36.102513
# Unit test for function show_corrected_command
def test_show_corrected_command():
    sys.stderr.write(u'\033[1K\r[{time}] {command}'
                     u' [{green}enter{reset}/{blue}↑{reset}/{blue}↓{reset}'
                     u'/{red}ctrl+c{reset}]\n'.format(
                         time=datetime.now().strftime('%H:%M:%S'),
                         command=corrected_command.script,
                         green=color(colorama.Fore.GREEN),
                         red=color(colorama.Fore.RED),
                         reset=color(colorama.Style.RESET_ALL),
                         blue=color(colorama.Fore.BLUE)))

# Generated at 2022-06-14 09:12:41.700733
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = 'git push origin master'
    assert u'[test] git push origin master' == show_corrected_command(corrected_command)
    assert u'[test] git push origin master' == confirm_text(corrected_command)

# Generated at 2022-06-14 09:12:44.446703
# Unit test for function show_corrected_command
def test_show_corrected_command():
    expected = const.USER_COMMAND_MARK + 'ls -l -a'
    assert show_corrected_command(expected) == None



# Generated at 2022-06-14 09:12:48.438716
# Unit test for function show_corrected_command
def test_show_corrected_command():
    _ = show_corrected_command("ls -al")
    _ = show_corrected_command("sudo ls -al")
    _ = show_corrected_command("sudo ls -al", True)
    return True



# Generated at 2022-06-14 09:12:54.503358
# Unit test for function color
def test_color():
    assert color(colorama.Style.BRIGHT) == ''
    assert color(u'\n') == u'\n'
    settings.no_colors = False
    assert color(colorama.Style.BRIGHT) == colorama.Style.BRIGHT
    assert color(u'\n') == colorama.Style.RESET_ALL + u'\n' + colorama.Style.RESET_ALL

# Generated at 2022-06-14 09:12:57.833894
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .correct import CorrectedCommand
    assert 'You fucked up' in show_corrected_command(CorrectedCommand('You fucked up', False, 'ls'))


# Generated at 2022-06-14 09:13:08.637767
# Unit test for function debug
def test_debug():
    from test.test_utils import MockPrint
    with MockPrint() as mock_stdout:
        debug('test')
    assert mock_stdout.call_count == 1
    assert mock_stdout.previous.split() == [
        color(colorama.Fore.BLUE + colorama.Style.BRIGHT + 'DEBUG:'),
        color(colorama.Style.RESET_ALL),
        'test']



# Generated at 2022-06-14 09:13:11.955853
# Unit test for function color
def test_color():
    colorama.init()

    assert '\033[31m' == color(colorama.Fore.RED)
    assert '' == color(colorama.Fore.RED, True)

# Generated at 2022-06-14 09:13:21.018394
# Unit test for function debug
def test_debug():
    from mock import Mock, patch
    sys.stderr = Mock()
    settings.debug = False
    debug('debug msg')
    settings.debug = True
    debug('debug msg')
    sys.stderr.write.assert_called_with(
        u'{blue}{bold}DEBUG:{reset} {msg}\n'.format(
            blue=color(colorama.Fore.BLUE),
            bold=color(colorama.Style.BRIGHT),
            msg='debug msg',
            reset=color(colorama.Style.RESET_ALL)))
    settings.debug = False

    with patch('thefuck.shells.get_shell') as get_shell:
        get_shell.return_value.app_alias = 'ls'

# Generated at 2022-06-14 09:13:22.586280
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)

# Generated at 2022-06-14 09:13:23.869011
# Unit test for function debug_time
def test_debug_time():
    with debug_time('a'):
        pass

# Generated at 2022-06-14 09:13:37.162490
# Unit test for function debug
def test_debug():
    import sys
    import StringIO
    from contextlib import contextmanager
    from datetime import datetime, timedelta
    from .conf import settings

    @contextmanager
    def capture():
        oldout,olderr = sys.stdout, sys.stderr
        try:
            out=[StringIO.StringIO(), StringIO.StringIO()]
            sys.stdout,sys.stderr = out
            yield out
        finally:
            sys.stdout,sys.stderr = oldout, olderr
            out[0] = out[0].getvalue()
            out[1] = out[1].getvalue()

    debug('foo')
    assert not 'foo' in sys.stderr.getvalue()

    with capture() as out:
        settings.debug = True
        debug('bar')

# Generated at 2022-06-14 09:13:44.282240
# Unit test for function debug
def test_debug():
    debug('\n') == u'\033[1K\r\x1b[34m\x1b[1mDEBUG:\x1b[0m \n\n' == \
        u'\x1b[1K\r\x1b[34m\x1b[1mDEBUG:\x1b[0m \n\n'

# Generated at 2022-06-14 09:13:47.539862
# Unit test for function color
def test_color():
    assert color(colorama.Fore.BLACK) == u'\x1b[30m'
    assert color(colorama.Fore.BLACK) == ''



# Generated at 2022-06-14 09:13:50.445975
# Unit test for function color
def test_color():
    assert color(u'bold') == u'\x1b[1mbold\x1b[21;39;22m'

# Generated at 2022-06-14 09:13:51.973618
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    # how_to_configure_alias(None)
    pass