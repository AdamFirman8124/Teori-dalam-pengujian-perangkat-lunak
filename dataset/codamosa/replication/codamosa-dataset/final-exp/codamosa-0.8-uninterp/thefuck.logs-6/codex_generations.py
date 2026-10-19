

# Generated at 2022-06-14 09:03:57.185675
# Unit test for function confirm_text
def test_confirm_text():
    text = 'sudo echo'
    confirm_text('')

# Generated at 2022-06-14 09:03:58.517532
# Unit test for function debug
def test_debug():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:04:03.760772
# Unit test for function debug
def test_debug():
    import mock
    with mock.patch('sys.stderr') as stderr:
        debug('test debug')
        stderr.write.assert_called_once_with(u'\x1b[36m\x1b[1mDEBUG:\x1b[0m test debug\n')

# Generated at 2022-06-14 09:04:09.924848
# Unit test for function debug
def test_debug():
    from contextlib import contextmanager
    import sys
    from io import StringIO

    @contextmanager
    def capture():
        saved_stdout = sys.stdout
        sys.stdout = stream = StringIO()
        try:
            yield stream
        finally:
            sys.stdout = saved_stdout

    with capture() as stream:
        debug("test")

    assert stream.getvalue() == "test\n"

# Generated at 2022-06-14 09:04:13.960887
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    assert debug_time('').__enter__()
    assert debug_time('').__exit__(None, None, None)

# Generated at 2022-06-14 09:04:15.648579
# Unit test for function color
def test_color():
    assert color('green') == colorama.Fore.GREEN
    assert color('green') == ''

# Generated at 2022-06-14 09:04:20.569622
# Unit test for function confirm_text
def test_confirm_text():
    assert(confirm_text('git lg') == u'{prefix}{clear}{bold}git lg{reset} [{green}enter{reset}/{blue}↑{reset}/{blue}↓{reset}/{red}ctrl+c{reset}]')

# Generated at 2022-06-14 09:04:22.383572
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text(1)

# Generated at 2022-06-14 09:04:25.258656
# Unit test for function confirm_text
def test_confirm_text():
    class Command(object):
        script = 'env'
        side_effect = False

    confirm_text(Command())



# Generated at 2022-06-14 09:04:30.651850
# Unit test for function debug
def test_debug():
    assert debug(u'test') == sys.stderr.write(u'{blue}{bold}DEBUG:{reset} test\n'.format(
        reset=color(colorama.Style.RESET_ALL),
        blue=color(colorama.Fore.BLUE),
        bold=color(colorama.Style.BRIGHT)))

# Generated at 2022-06-14 09:04:40.024152
# Unit test for function confirm_text
def test_confirm_text():
    python_version = sys.version
    if python_version[0] == "3":
        assert confirm_text("ls") == '\x1b[1K\r'+const.USER_COMMAND_MARK+"ls"
    else:
        assert confirm_text("ls") == '\r'+const.USER_COMMAND_MARK+"ls"


# Generated at 2022-06-14 09:04:45.225546
# Unit test for function color
def test_color():
    assert color(u'XXX') == u'XXX'
    assert color(u'XXX') != u''

    assert color(u'XXX') != u''
    settings.no_colors = True
    assert color(u'XXX') == u''

# Generated at 2022-06-14 09:04:47.769852
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text('/bin/ls') == u'👉/bin/ls [enter/↑/↓/ctrl+c]'

# Generated at 2022-06-14 09:04:55.608533
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from io import StringIO
    import sys
    import colorama

    original_stdout = sys.stdout
    original_stderr = sys.stderr
    sys.stdout = output = StringIO()
    try:
        how_to_configure_alias(None)
        return output.getvalue()
    finally:
        sys.stdout = original_stdout
        sys.stderr = original_stderr



# Generated at 2022-06-14 09:04:58.542691
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    assert how_to_configure_alias() == 'Seems like fuck alias isn\'t configured!'


# Generated at 2022-06-14 09:05:02.115023
# Unit test for function debug
def test_debug():
    settings.debug = False
    debug('test')
    assert True
    settings.debug = True
    debug('test')
    assert True



# Generated at 2022-06-14 09:05:13.507105
# Unit test for function confirm_text

# Generated at 2022-06-14 09:05:20.884709
# Unit test for function debug
def test_debug():
    from mock import patch

    with patch('sys.stderr', create=True) as stderr:
        debug(u'123')
        debug(u'abc')
    assert stderr.write.call_args_list == [
        (('\x1b[34m\x1b[1mDEBUG:\x1b[0m 123\n',),),
        (('\x1b[34m\x1b[1mDEBUG:\x1b[0m abc\n',),)]

# Generated at 2022-06-14 09:05:23.858957
# Unit test for function color
def test_color():
    assert color('') == ''
    settings.no_colors = True
    assert color('abc') == ''

# Generated at 2022-06-14 09:05:36.885266
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    configuration_details = ('content', 'path', 'reload', False)

# Generated at 2022-06-14 09:05:50.153723
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    class FakeConfigurationDetails(object):
        def __init__(self, can_configure_automatically):
            self.can_configure_automatically = can_configure_automatically

    how_to_configure_alias(None)
    how_to_configure_alias(FakeConfigurationDetails(True))
    how_to_configure_alias(FakeConfigurationDetails(False))

# Generated at 2022-06-14 09:05:56.234523
# Unit test for function debug_time
def test_debug_time():
    import time
    from mock import patch
    from os import devnull
    from datetime import timedelta
    with patch('sys.stderr', open(devnull, 'w')):
        with debug_time('test'):
            time.sleep(0.03)
        assert timedelta(seconds=0, microseconds=30000) < \
            datetime.now() - started < timedelta(seconds=0, microseconds=35000)

# Generated at 2022-06-14 09:05:58.831828
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = ("pwd", False)
    assert show_corrected_command(corrected_command) == "Fuck! pwd"

# Generated at 2022-06-14 09:06:00.753470
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(settings.PATH)


# Generated at 2022-06-14 09:06:04.241870
# Unit test for function color
def test_color():
    assert color('color') == 'color'
    settings.no_colors = True
    assert color('color') == ''
    settings.no_colors = False

# Generated at 2022-06-14 09:06:11.203688
# Unit test for function debug
def test_debug():
    from contextlib import contextmanager

    @contextmanager
    def debug_time(msg):
        started = datetime.now()
        try:
            yield
        finally:
            debug(u'{} took: {}'.format(msg, datetime.now() - started))

    debug(u'{} took: {}'.format(msg, datetime.now() - started))

# Generated at 2022-06-14 09:06:13.119287
# Unit test for function debug
def test_debug():
    """Test for function debug."""
    # Debug disabled
    settings.debug = False
    debug('some debug message')

    # Debug enabled
    settings.debug = True
    debug('some debug message')

# Generated at 2022-06-14 09:06:15.289080
# Unit test for function color
def test_color():
    assert color('') == ''
    settings.no_colors = True
    assert color('') == ''



# Generated at 2022-06-14 09:06:16.541996
# Unit test for function debug
def test_debug():
    debug('test msg')


# Generated at 2022-06-14 09:06:18.945032
# Unit test for function debug_time
def test_debug_time():
    started = datetime.now()
    debug_time('test')
    assert datetime.now() > started



# Generated at 2022-06-14 09:06:32.545699
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .shells import Shell
    from .shells.bash import Bash, get_alias, BashAlias
    from .utils import get_closest, get_all

    def mock_get_closest(path):
        return get_all()[path]


# Generated at 2022-06-14 09:06:33.748659
# Unit test for function show_corrected_command
def test_show_corrected_command():
    sys.stderr.write('tests-command')


# Generated at 2022-06-14 09:06:36.071759
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)
    how_to_configure_alias(None)  # tested only first print


# Generated at 2022-06-14 09:06:40.703266
# Unit test for function color
def test_color():
    assert color(u'проверка') == u'проверка'
    settings.no_colors = True
    assert color(u'проверка') == u''

# Generated at 2022-06-14 09:06:45.620545
# Unit test for function debug_time
def test_debug_time():
    get_debug = []

    def debug(msg):
        get_debug.append(msg)

    with debug_time('test'):
        pass

    assert len(get_debug) == 1
    assert get_debug[0] == u'test took: 0:00:00'

# Generated at 2022-06-14 09:06:48.970020
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text({'script': 'rm -r`'}) \
        == const.USER_COMMAND_MARK + 'rm -r`' + ' ' + '[enter/↑/↓/ctrl+c]'



# Generated at 2022-06-14 09:06:53.013709
# Unit test for function debug_time
def test_debug_time():
    import time
    started = datetime.now()
    time.sleep(1)
    finished = datetime.now()
    with debug_time('test'):
        time.sleep(1)
        assert started < finished

# Generated at 2022-06-14 09:06:56.286445
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .shells import Bash
    bash = Bash()
    command = bash.from_shell('echo "Fuck"')
    show_corrected_command(command)


# Generated at 2022-06-14 09:07:06.371518
# Unit test for function debug
def test_debug():

    test_msg = u"Hello World!"
    from io import StringIO
    from contextlib import contextmanager

    @contextmanager
    def captured_output():
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err

    with captured_output() as (out, _):
        debug(test_msg)

# Generated at 2022-06-14 09:07:08.219765
# Unit test for function debug
def test_debug():
    assert debug('message')



# Generated at 2022-06-14 09:07:17.923787
# Unit test for function confirm_text
def test_confirm_text():
    class corrected_command_:
        def __init__(self):
            self.script = u'ls'
            self.side_effect = True

    corrected_command = corrected_command_()

    confirm_text(corrected_command)

# Generated at 2022-06-14 09:07:20.753042
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = const.Command('git', 'remote add origin')
    assert const.USER_COMMAND_MARK + 'git remote add origin\n' == show_corrected_command(corrected_command)

# Generated at 2022-06-14 09:07:22.252426
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text(corrected_command=None)

# Generated at 2022-06-14 09:07:27.959165
# Unit test for function confirm_text
def test_confirm_text():
    stdin_fake = sys.stdin.read
    sys.stdin.read = lambda x: 'y'

    confirm_text(Command('ls', False))
    assert sys.stdin.read == stdin_fake


if __name__ == '__main__':
    test_confirm_text()

# Generated at 2022-06-14 09:07:31.797602
# Unit test for function debug
def test_debug():
    from mock import patch
    with patch('sys.stderr') as stderr:
        debug('foo')
        stderr.write.assert_called_once_with(
            '\x1b[34m\x1b[1mDEBUG:\x1b[0m foo\n')

# Generated at 2022-06-14 09:07:36.808468
# Unit test for function debug_time
def test_debug_time():
    try:
        with debug_time('test'):
            pass
    except KeyboardInterrupt:
        pass
    else:
        assert False, 'Exception not raised'



# Generated at 2022-06-14 09:07:43.422622
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .shells.bash import ConfigurationDetails
    how_to_configure_alias(ConfigurationDetails(
        path=u'/etc/profile.d/fuck.sh',
        content=u'. ~/.fuck/venv/bin/activate\nalias fuck=\'.fuck\'',
        reload=u'sudo service sshd reload'))



# Generated at 2022-06-14 09:07:51.315867
# Unit test for function color
def test_color():
    color()
    is_monochrome = (colorama.Style.BRIGHT == '')
    assert color(colorama.Fore.RED) == colorama.Fore.RED
    assert color(colorama.Style.BRIGHT) == colorama.Style.BRIGHT
    assert color(colorama.Style.RESET_ALL) == colorama.Style.RESET_ALL
    assert color(colorama.Fore.RED) == '' == color(colorama.Style.BRIGHT) == color(colorama.Style.RESET_ALL) == ''

# Generated at 2022-06-14 09:07:54.699600
# Unit test for function show_corrected_command
def test_show_corrected_command():
    assert show_corrected_command(u'sudo echo "Fuck"') == u'\033[1K\r' \
        u'>> sudo echo "Fuck"\033[m'

# Generated at 2022-06-14 09:07:57.530562
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test_debug_time'):
        from time import sleep
        sleep(1)

# Generated at 2022-06-14 09:08:14.115688
# Unit test for function debug_time
def test_debug_time():
    import time

    class MockStdErr(object):
        def __init__(self):
            self.wrote = None

        def write(self, msg):
            if self.wrote is None:
                self.wrote = msg

    start_time = datetime(2000, 1, 1, 1, 0)
    end_time = datetime(2000, 1, 1, 1, 0, 1)
    time_delta = end_time - start_time
    msg = 'test'
    settings.debug = True
    sys.stderr = MockStdErr()

    time.time = lambda: time.mktime(start_time.timetuple())
    with debug_time(msg):
        time.time = lambda: time.mktime(end_time.timetuple())

# Generated at 2022-06-14 09:08:21.649362
# Unit test for function debug
def test_debug():
    import StringIO
    stream = StringIO.StringIO()
    std_err, sys.stderr = sys.stderr, stream
    try:
        debug('test')
        assert stream.getvalue() == u"\x1b[34m\x1b[1mDEBUG:\x1b[0m test\n"
    finally:
        sys.stderr = std_err

# Generated at 2022-06-14 09:08:31.921393
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    import pytest
    from mock import Mock
    
    configuration_details = Mock()
    configuration_details._asdict = lambda: {
        'content': 'test_content',
        'path': 'test_path',
        'reload': 'test_reload',
        'can_configure_automatically': True
    }

    with pytest.capture_stderr() as stderr:
        how_to_configure_alias(configuration_details)
        

# Generated at 2022-06-14 09:08:34.805183
# Unit test for function confirm_text
def test_confirm_text():
    """
    test the function confirm_text
    """
    confirm_text(corrected_command="cd ddfds")
    confirm_text(corrected_command="cd ..")

# Generated at 2022-06-14 09:08:36.264519
# Unit test for function debug
def test_debug():
    try:
        debug('msg')
    except:
        pass

# Generated at 2022-06-14 09:08:52.713833
# Unit test for function confirm_text
def test_confirm_text():
    from mock import call, patch
    from .shells.posix import PosixLikeShell

    with patch('sys.stderr', create=True) as mock_stderr:
        import colorama
        colorama.init = lambda: None
        settings.no_colors = False
        shell = PosixLikeShell()
        confirm_text(shell.get_corrected_command(shell.script, ''))
        assert mock_stderr.write.call_args == call('{}fuck\n [enter/↑/↓/ctrl+c]'.format(const.USER_COMMAND_MARK))

        settings.no_colors = True
        confirm_text(shell.get_corrected_command(shell.script, ''))

# Generated at 2022-06-14 09:08:55.077916
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .command import Command
    show_corrected_command(Command(u'ls', u'ls -al'))


# Generated at 2022-06-14 09:09:00.399427
# Unit test for function debug
def test_debug():
    from tempfile import NamedTemporaryFile
    with NamedTemporaryFile() as tmp:
        settings.debug_to_file = tmp.name
        debug('foo')
        tmp.seek(0)
        assert tmp.read() == 'DEBUG: foo\n'



# Generated at 2022-06-14 09:09:01.759632
# Unit test for function debug
def test_debug():
    assert debug('test') is None

# Generated at 2022-06-14 09:09:07.801797
# Unit test for function color
def test_color():
    assert color('red')('red text') == u'\x1b[31mred text\x1b[0m'
    assert color(colorama.Fore.RED)('red text') ==\
        u'\x1b[31mred text\x1b[0m'



# Generated at 2022-06-14 09:09:19.988719
# Unit test for function confirm_text
def test_confirm_text():
    import pytest
    import textwrap
    confirm_text(const.Command('foo', None))
    assert sys.stderr.getvalue() == \
           textwrap.dedent(u'{prefix}foo [enter/↑/↓/ctrl+c]'.format(
                               prefix=const.USER_COMMAND_MARK))

# Generated at 2022-06-14 09:09:32.404123
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .shells import Bash
    from .utils import esc
    assert how_to_configure_alias(Bash.from_shell('/bin/bash')) == \
        u"""Seems like {bold}fuck{reset} alias isn't configured!
Please put {bold}eval "$(thefuck --alias)"{reset} in your {bold}/home/user/.bashrc{reset} and apply changes with {bold}source "~/.bashrc"{reset} or restart your shell.
Or run {bold}fuck{reset} a second time to configure it automatically.
More details - https://github.com/nvbn/thefuck#manual-installation""".format(
            bold=color(colorama.Style.BRIGHT),
            reset=color(colorama.Style.RESET_ALL))



# Generated at 2022-06-14 09:09:40.328505
# Unit test for function confirm_text
def test_confirm_text():
    class TestCmd(object):
        def __init__(self, script, side_effect):
            self.script = script
            self.side_effect = side_effect
    # Test script is printed
    corrected_command = TestCmd('script', False)
    confirm_text(corrected_command)
    # Test side_effect is printed
    corrected_command = TestCmd('script', True)
    confirm_text(corrected_command)


# Generated at 2022-06-14 09:09:45.515568
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import os
    import tempfile
    fd, temp_file_path = tempfile.mkstemp()
    os.close(fd)
    fd = os.open(temp_file_path, os.O_WRONLY)
    os.dup2(fd, sys.stderr.fileno())
    show_corrected_command('echo "a"')
    os.close(fd)
    with open(temp_file_path, 'r') as f:
        assert f.read() == '> echo "a"'

# Generated at 2022-06-14 09:09:51.089256
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .shells import Bash, Zsh

    for shell in Bash, Zsh:
        shell.get_history = lambda: [u'rm -rf /']
        show_corrected_command(shell().get_command())



# Generated at 2022-06-14 09:09:52.274265
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:10:00.517934
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from collections import namedtuple
    command = namedtuple('Command', ['script'])
    script = 'echo hello'
    corrected_command = command(script=script)
    show_corrected_command(corrected_command)
    assert sys.stderr.getvalue() == '{}echo hello{}\n'.format(
        const.USER_COMMAND_MARK, color(colorama.Style.RESET_ALL))



# Generated at 2022-06-14 09:10:12.596784
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .application import CorrectedCommand
    from .utils import sudo_support
    from datetime import datetime
    import mock
    import sys

    assert(show_corrected_command(CorrectedCommand(
        script='mkdir a|echo b',
        side_effect=True,
        timestamp=datetime.now(),
        )
        ) == 'sudo mkdir a|echo b (+side effect)')
    assert(show_corrected_command(CorrectedCommand(
        script='mkdir a;echo b',
        side_effect=False,
        timestamp=datetime.now(),
        )
        ) == 'sudo mkdir a;echo b')

# Generated at 2022-06-14 09:10:13.389372
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text('test') == 'test\n'

# Generated at 2022-06-14 09:10:18.143388
# Unit test for function confirm_text
def test_confirm_text():
    correct_text = (u'env PYTHONPATH=~/.config/thefuck/rules python '
                    u'~/.config/thefuck/thefuck --alias fuck '
                    u'ls /etc/ | grep -v s/ | grep -v X11/ ')
    confirm_text(correct_text)



# Generated at 2022-06-14 09:10:25.113912
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text('ls')

# Generated at 2022-06-14 09:10:32.490328
# Unit test for function debug
def test_debug():
    from collections import namedtuple
    from mock import patch

    with patch('sys.stderr') as stderr:
        debug('debug')
        assert stderr.write.called

    Settings = namedtuple('Settings', 'no_colors debug')
    settings = Settings(no_colors=True, debug=True)

    with patch.object(settings, 'debug', True):
        debug('debug')
        assert stderr.write.called

# Generated at 2022-06-14 09:10:40.504233
# Unit test for function confirm_text
def test_confirm_text():
    from .conf import load_settings
    from .rules import Rule
    settings = load_settings()
    settings.no_colors = True
    rule = Rule(
        name='test',
        match='test',
        get_new_command=lambda: u'test',
        enabled_by_default=True)
    confirm_text(rule.get_new_command('', 0, settings=settings))

# Generated at 2022-06-14 09:10:43.211002
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug(u"Привет, мир!")

# Generated at 2022-06-14 09:10:52.438187
# Unit test for function debug
def test_debug():
    from mock import patch

    with patch.object(sys.stderr, 'write') as write:
        settings.debug = True
        debug(u'Hello, World!')
        write.assert_called_with(
            '\x1b[34m\x1b[1mDEBUG:\x1b[0m Hello, World!\n')

    with patch.object(sys.stderr, 'write') as write:
        settings.debug = False
        debug(u'Hello, World!')
        write.assert_not_called()



# Generated at 2022-06-14 09:10:55.349096
# Unit test for function color
def test_color():
    assert color(colorama.Fore.RED) == colorama.Fore.RED
    assert color('') == ''



# Generated at 2022-06-14 09:10:59.385470
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import core.corrected_command
    command = core.corrected_command.CorrectedCommand(script='git status', side_effect=True)
    show_corrected_command(command)


# Generated at 2022-06-14 09:11:04.469343
# Unit test for function debug
def test_debug():
    from StringIO import StringIO
    test_str = StringIO()
    sys.stderr = test_str
    debug(u"Hello World")
    assert sys.stderr.getvalue() == color('\x1b[34m\x1b[1mDEBUG:\x1b[0m Hello World\n')

# Generated at 2022-06-14 09:11:08.164928
# Unit test for function debug
def test_debug():
    """
    Test function debug to check if DEBUG is printing the message
    """
    import os

    os.environ['TF_DEBUG'] = '1'
    debug("debug message")
    assert True == os.environ.get('TF_DEBUG')

# Generated at 2022-06-14 09:11:24.072622
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from thefuck.types import ConfigurationDetails
    from mock import call

    default_args = {
        'bold': color(colorama.Style.BRIGHT),
        'reset': color(colorama.Style.RESET_ALL),
    }

    def assert_call(expected):
        calls = [call(msg) for msg in expected]
        assert config == calls

    with settings(no_colors=False):
        config = []

        def print_(msg):
            config.append(msg)

        how_to_configure_alias(ConfigurationDetails(
            can_configure_automatically=False,
            path='.bashrc',
            reload='exec $SHELL',
            content='eval $(thefuck --alias)'))

# Generated at 2022-06-14 09:11:42.433637
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = corrected_command = type(
        'CorrectedCommand',
        (),
        {'script': 'ls -lah',
         'side_effect': False})

# Generated at 2022-06-14 09:11:48.573253
# Unit test for function confirm_text
def test_confirm_text():
    import pytest
    corrected_command = type('Command', (object,), {'script': 'my_script', 'side_effect': 'my_side_effect'})
    confirm_text(corrected_command)
    assert pytest.out == u'my_script (+side effect) [enter/↑/↓/ctrl+c]'

# Generated at 2022-06-14 09:11:51.434404
# Unit test for function debug
def test_debug():
    sys.stderr = open('/dev/null', 'w')
    debug('debug message')
    debug('debug message')

# Generated at 2022-06-14 09:11:55.346176
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .correct import CorrectedCommand
    show_corrected_command(CorrectedCommand("git piss", True))

if __name__ == '__main__':
    test_show_corrected_command()

# Generated at 2022-06-14 09:11:56.896691
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .command import Command
    show_corrected_command(Command('pwd', ''))



# Generated at 2022-06-14 09:11:58.605861
# Unit test for function debug_time
def test_debug_time():
    debug_time('test')

if __name__ == '__main__':
    test_debug_time()

# Generated at 2022-06-14 09:12:12.778890
# Unit test for function debug
def test_debug():
    import cStringIO
    import sys
    old_stderr = sys.stderr
    sys.stderr = cStringIO.StringIO()

    settings.debug = True
    debug(u'test')
    assert sys.stderr.getvalue() == u"\x1b[36m\x1b[1mDEBUG:\x1b[0m test\n"

    settings.debug = False
    debug(u'test')
    assert sys.stderr.getvalue() == u"\x1b[36m\x1b[1mDEBUG:\x1b[0m test\n"

    settings.no_colors = True
    debug(u'test')

# Generated at 2022-06-14 09:12:16.943903
# Unit test for function color
def test_color():
    assert color(colorama.Fore.RED) == ''
    # Disable colors
    settings.no_colors = True
    assert color(colorama.Fore.RED) == ''
    # Enable colors
    settings.no_colors = False
    assert color(colorama.Fore.RED) == '\x1b[31m'

# Generated at 2022-06-14 09:12:32.845540
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    import thefuck.main
    from thefuck.conf import ConfigurationDetails

    class mockshellinfo:
        name = 'zsh'
        current_version = '5.2'

    def check():
        assert None == thefuck.main.how_to_configure_alias(None)

    def check_empty_configuration_details():
        assert None == thefuck.main.how_to_configure_alias(
            ConfigurationDetails()
        )

    def check_empty_configuration_details_with_autoconfigure_support():
        assert None == thefuck.main.how_to_configure_alias(
            ConfigurationDetails(
                can_configure_automatically=True
            )
        )

    def check_filled_configuration_details():
        assert None == thefuck.main.how_to_configure_

# Generated at 2022-06-14 09:12:42.898610
# Unit test for function confirm_text
def test_confirm_text():
    from thefuck.conf import settings
    from thefuck.shells.zsh import Zsh
    from mock import patch
    from itertools import chain
    import colorama
    settings.side_effect.prompt = True
    settings.prompt_prefix = '{} '.format(const.USER_COMMAND_MARK)
    settings.no_colors = False
    settings.require_confirmation = True
    with patch('thefuck.main.sys.stderr.write') as stderr_mock:
        settings.shell = Zsh()
        confirm_text(shell=Zsh(), script='python')

# Generated at 2022-06-14 09:12:55.655705
# Unit test for function confirm_text
def test_confirm_text():
    from . import output
    corrected_command = output.CorrectedCommand('echo "hello"', False)
    confirm_text(corrected_command)
    print(output.const.USER_COMMAND_MARK + 'echo "hello"')
    corrected_command = output.CorrectedCommand('echo "hello"', True)
    confirm_text(corrected_command)
    print(output.const.USER_COMMAND_MARK + 'echo "hello" (+side effect)')

# Generated at 2022-06-14 09:12:58.579551
# Unit test for function show_corrected_command
def test_show_corrected_command():
    # pylint: disable=W0212
    show_corrected_command(corrected_command=3)


# Generated at 2022-06-14 09:13:00.457660
# Unit test for function debug
def test_debug():
    debug('this is debug info')
    debug('this is debug info with spaces in it')

# Generated at 2022-06-14 09:13:10.490079
# Unit test for function confirm_text
def test_confirm_text():
    from .types import CorrectedCommand
    from .shells import Shell
    from .conf import DEFAULT_HISTORY_MAX_SIZE
    import io
    import colorama
    colorama.init()
    history = []
    corrected_command = CorrectedCommand('echo 1', history, 'echo 1',
                                         True, DEFAULT_HISTORY_MAX_SIZE,
                                         Shell.from_cls(Shell))
    o = io.StringIO()
    sys.stderr = o
    confirm_text(corrected_command)
    sys.stderr = sys.__stderr__

# Generated at 2022-06-14 09:13:18.982621
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .utils import wrap_input
    from .core import CorrectedCommand

    class DummyInput:
        def __init__(self, value):
            self.value = value

        def raw_input(self):
            return self.value

    with wrap_input(DummyInput('a')):
        show_corrected_command(CorrectedCommand(u'echo fuck', []))
        assert sys.stdout.getvalue() == u"\x1b[33m>\x1b[0m\x1b[1mecho fuck\x1b[0m\n"

# Generated at 2022-06-14 09:13:21.811604
# Unit test for function color
def test_color():
    assert not color(colorama.Fore.RED)
    settings.no_colors = False
    assert color(colorama.Fore.RED) == colorama.Fore.RED



# Generated at 2022-06-14 09:13:26.223036
# Unit test for function confirm_text
def test_confirm_text():
    from .shells.some_shell import _confirm_text
    assert (u'[enter/↑/↓/ctrl+c]' ==
            _confirm_text(u'ls', '', '', '').split(' ')[-1])



# Generated at 2022-06-14 09:13:29.060918
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    expected_text = u"Seems like \x1b[1mfuck\x1b[21m alias isn't configured!"
    assert expected_text in unicode(how_to_configure_alias('configuration_details'))



# Generated at 2022-06-14 09:13:32.675303
# Unit test for function debug_time
def test_debug_time():
    from datetime import datetime
    from datetime import timedelta
    from mock import Mock
    from . import log

    debug = Mock()

    with log.debug_time('msg'):
        debug.assert_called_with('msg took: 0:00:00')
        debug.reset_mock()

    with log.debug_time('msg'):
        datetime.now = Mock(return_value=datetime.now() + timedelta(seconds=2))
        debug.assert_called_with('msg took: 0:00:02')

# Generated at 2022-06-14 09:13:40.879178
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from collections import namedtuple
    ConfigurationDetails = namedtuple(
        'ConfigurationDetails', 'can_configure_automatically,path,content,reload')
    configuration_details = ConfigurationDetails(True, '~/.bashrc',
        'eval $(thefuck --alias)', 'source ~/.bashrc')
    how_to_configure_alias(configuration_details)