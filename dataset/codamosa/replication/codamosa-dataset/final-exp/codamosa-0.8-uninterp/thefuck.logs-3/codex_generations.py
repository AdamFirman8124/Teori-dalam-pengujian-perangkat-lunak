

# Generated at 2022-06-14 09:03:57.308964
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .command import Command
    show_corrected_command(Command('ls -la'))

# Generated at 2022-06-14 09:04:00.291266
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = Command(script='git status', side_effect=True)
    show_corrected_command(corrected_command)


# Generated at 2022-06-14 09:04:02.589266
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    from time import sleep
    with debug_time('test message'):
        sleep(1)

# Generated at 2022-06-14 09:04:05.282304
# Unit test for function color
def test_color():
    assert '\033[0;36m' == color(colorama.Fore.CYAN)
    assert '' == color(colorama.Fore.CYAN)

# Generated at 2022-06-14 09:04:06.177345
# Unit test for function debug
def test_debug():
    return debug('debug')


# Generated at 2022-06-14 09:04:09.158722
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    
    with debug_time('Hello World'):
        import time
        time.sleep(0.001)

# Generated at 2022-06-14 09:04:20.455747
# Unit test for function confirm_text
def test_confirm_text():
    from mock import Mock
    corrected_command = Mock()
    corrected_command.script = 'git push'
    corrected_command.side_effect = None
    assert confirm_text(corrected_command) == '\x1b[1K\r\x1b[1m\x1b[1m\x1b[34mgit push\x1b[0m [\x1b[32menter\x1b[0m/\x1b[34m↑\x1b[0m/\x1b[34m↓\x1b[0m/\x1b[31mctrl+c\x1b[0m] '  # noqa E501



# Generated at 2022-06-14 09:04:29.789206
# Unit test for function show_corrected_command
def test_show_corrected_command():
    class CorrectedCommand(object):
        def __init__(self, script, side_effect):
            self.script = script
            self.side_effect = side_effect

    assert show_corrected_command(CorrectedCommand('echo fuck', True)) == u'{prefix}{bold}{script}{reset}{side_effect}\n'.format(
        prefix=const.USER_COMMAND_MARK,
        script='echo fuck',
        side_effect=u' (+side effect)',
        bold=color(colorama.Style.BRIGHT),
        reset=color(colorama.Style.RESET_ALL))


# Generated at 2022-06-14 09:04:33.342218
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    # Fixtures
    configuration_details = None
    # Call function to be tested
    how_to_configure_alias(configuration_details)



# Generated at 2022-06-14 09:04:40.521855
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from StringIO import StringIO
    import sys
    old_stdout = sys.stderr
    string_io = StringIO()
    sys.stderr = string_io
    show_corrected_command("ls -al")
    sys.stderr = old_stdout
    assert string_io.getvalue(), "ls -al\n"


# Generated at 2022-06-14 09:04:46.226056
# Unit test for function debug
def test_debug():
    def run_debug():
        debug('some message')
    settings._debug = True
    assert run_debug() == None



# Generated at 2022-06-14 09:05:01.169320
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .types import CorrectedCommand
    sys.stdout._orig_write = sys.stdout._orig_write or sys.stdout.write

    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO
    out = StringIO()
    sys.stdout.write = out.write

    corrected_command = CorrectedCommand('test', False)
    show_corrected_command(corrected_command)
    assert out.getvalue() == 'sudo vim /etc/nginx/nginx.conf ' \
                             '[enter/↑/↓/ctrl+c]\n'

    corrected_command = CorrectedCommand('test', True)
    show_corrected_command(corrected_command)
    assert out.getvalue() == 'sudo vim /etc/nginx/nginx.conf '

# Generated at 2022-06-14 09:05:05.642387
# Unit test for function debug_time
def test_debug_time():
    """
    >>> with debug_time('test debug_time'):
    ...     pass
    """

try:
    from unittest import mock  # noqa
except ImportError:
    import mock  # noqa
    from .conf import settings

    settings.no_colors = True

# Generated at 2022-06-14 09:05:11.140796
# Unit test for function color
def test_color():
    assert color('') == ''
    assert color('red') == colorama.Fore.RED + 'red'
    assert color('\033[2mbold\033[0m') == colorama.Style.BRIGHT + 'bold'
    assert color('\033[30m') == ''



# Generated at 2022-06-14 09:05:14.600324
# Unit test for function confirm_text
def test_confirm_text():
    """Test for function confirm_text"""
    confirm_text(CorrectedCommand('ls --help', False))
    confirm_text(CorrectedCommand('ls --help', True))



# Generated at 2022-06-14 09:05:17.235196
# Unit test for function color
def test_color():
    assert color(colorama.Fore.GREEN) == colorama.Fore.GREEN
    assert color(colorama.Fore.GREEN) == ''

# Generated at 2022-06-14 09:05:23.006674
# Unit test for function debug
def test_debug():
    import tempfile
    stderr = sys.stderr
    try:
        tmp = tempfile.TemporaryFile()
        sys.stderr = tmp
        settings.debug = True  # Set it to True
        debug('test')
        tmp.seek(0)
        assert u'\x1b[34m\x1b[1mDEBUG:\x1b[0m test\n' in tmp.read()
    finally:
        sys.stderr = stderr

# Generated at 2022-06-14 09:05:24.860691
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    print(how_to_configure_alias())

# Generated at 2022-06-14 09:05:26.143470
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text(None)

# Generated at 2022-06-14 09:05:32.625462
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)
    how_to_configure_alias(True)
    how_to_configure_alias(
        const.ConfigurationDetails(
            path='file',
            content='alias fuck=\'eval $(thefuck $(fc -ln -1))\'',
            reload='reload',
            can_configure_automatically=True))

# Generated at 2022-06-14 09:05:41.806181
# Unit test for function debug
def test_debug():
    from .conf import settings
    from .utils import Mock

    settings.debug = True
    with Mock(sys, 'stderr') as mock_stderr:
        debug(u'Foo')
        assert mock_stderr.write.called
        assert u'DEBUG: Foo' in mock_stderr.write.calls[0].kwargs['data'].decode('utf-8')
    settings.debug = False

# Generated at 2022-06-14 09:05:44.048582
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = MockCorrectedCommand()
    confirm_text(corrected_command)
    assert(corrected_command.called == True)


# Generated at 2022-06-14 09:05:51.122384
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias((u'.fuckrc', u'/root/.bash', u'fuck --reload'))
    how_to_configure_alias((u'.fuckrc', u'/root/.bash', u'fuck --reload',
                            True))
    how_to_configure_alias(None)

# Generated at 2022-06-14 09:05:53.170114
# Unit test for function color
def test_color():
    colorama.init()
    assert color(colorama.Fore.BLUE) == colorama.Fore.BLUE

# Generated at 2022-06-14 09:05:54.596023
# Unit test for function confirm_text
def test_confirm_text():
    command = 'ls'
    confirm_text(command)


# Generated at 2022-06-14 09:05:55.402282
# Unit test for function debug
def test_debug():
    assert True

# Generated at 2022-06-14 09:05:57.818539
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text('test') == (u'test [enter/↑/↓/ctrl+c]')

# Generated at 2022-06-14 09:06:10.769291
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .command import Command

    command = Command('ls', 'cd ~ && ls')
    show_corrected_command(command)
    assert sys.stderr.getvalue() == u'\x1b[33m> \x1b[0mls\n'
    sys.stderr.truncate(0)

    command = Command('ls', 'cd ~ && ls', side_effect=True)
    show_corrected_command(command)
    assert sys.stderr.getvalue() == (
        u'\x1b[33m> \x1b[0mls\x1b[1m (+side effect)\x1b[0m\n')
    sys.stderr.truncate(0)


# Generated at 2022-06-14 09:06:12.963601
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    from time import sleep

    with debug_time('testing') as timed_block:
        sleep(0.2)
        assert timed_block.min_duration > timedelta(seconds=0.1)

# Generated at 2022-06-14 09:06:14.655466
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug('debug')



# Generated at 2022-06-14 09:06:31.892254
# Unit test for function debug
def test_debug():
    import os
    import mock
    from .conf import Settings

    def _mock_stderr(msg):
        return os.write(self.stderr, msg)

    with mock.patch('sys.stderr', autospec=True) as stderr:
        with mock.patch('os.write', autospec=True):
            stderr.write = _mock_stderr
            debug('test')
            assert stderr.write.called

    stderr = mock.Mock()
    with mock.patch('thefuck.utils.settings') as settings:
        settings.debug = True
        debug("test", stderr=stderr)
        assert stderr.write.called

    stderr = mock.Mock()

# Generated at 2022-06-14 09:06:33.874366
# Unit test for function color
def test_color():
    assert color('') == ''
    settings.no_colors = True
    assert color('foo') == ''
    settings.no_colors = False

# Generated at 2022-06-14 09:06:36.836214
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test_debug_time'):
        print("test_debug_time")

if __name__ == '__main__':
    test_debug_time()

# Generated at 2022-06-14 09:06:40.485493
# Unit test for function color
def test_color():
    assert color("red") == ""

    settings.no_colors = False
    assert color("red") == "red"

    settings.no_colors = True

# Generated at 2022-06-14 09:06:43.377491
# Unit test for function confirm_text
def test_confirm_text():
    assert(confirm_text('gitt')=='git commit -m"" [enter]/[↑]/[↓]/[ctrl+c]')

# Generated at 2022-06-14 09:06:45.078986
# Unit test for function debug_time
def test_debug_time():
     with debug_time('test'):
         pass

# Generated at 2022-06-14 09:06:50.464663
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .configuration_details import ConfigurationDetails
    test_info1 = ConfigurationDetails('test_content', 'test_path', 'test_reload', 'test_can_configure_automatically')
    test_info2 = ConfigurationDetails('test_content', 'test_path', 'test_reload', 'test_can_configure_automatically')
    how_to_configure_alias(test_info1)



# Generated at 2022-06-14 09:07:03.935751
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .utils import wrap_streams
    from .conf import ConfigurationDetails
    # use empty configuration details, no need to test content of configuration details
    configuration_details = ConfigurationDetails(None, None, None, None)

    with wrap_streams('', '', '', '') as (out, err):
        how_to_configure_alias(configuration_details)

# Generated at 2022-06-14 09:07:09.974089
# Unit test for function debug
def test_debug():
    import sys
    import StringIO
    class Capturing(list):
        def __enter__(self):
            self._stdout = sys.stdout
            sys.stdout = self._stringio = StringIO.StringIO()
            return self
        def __exit__(self, *args):
            self.extend(self._stringio.getvalue().splitlines())
            sys.stdout = self._stdout
    with Capturing() as output:
        debug("Debug!")
    assert len(output) == 1
    assert "Debug!" in output

# Generated at 2022-06-14 09:07:12.123239
# Unit test for function color
def test_color():
    assert color('green') == colorama.Fore.GREEN
    assert color('') == ''



# Generated at 2022-06-14 09:07:21.173835
# Unit test for function confirm_text
def test_confirm_text():
    from .utils import settings_from_pyfile

    settings_from_pyfile('thefuck.config.py.example')
    settings.no_colors = False

    confirm_text('ls')
    assert color(colorama.Style.BRIGHT) + 'ls' + color(colorama.Style.RESET_ALL) in confirm_text('')

    settings.no_colors = True
    confirm_text('ls')
    assert 'ls' == confirm_text('')

# Generated at 2022-06-14 09:07:25.045810
# Unit test for function debug_time
def test_debug_time():
    try:
        with debug_time('message'):
            pass
    except:
        raise AssertionError

    with debug_time('message'):
        raise Exception

    with debug_time('message'):
        pass

# Generated at 2022-06-14 09:07:25.645427
# Unit test for function debug
def test_debug():
    debug('some text')

# Generated at 2022-06-14 09:07:27.801341
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text('alias fuck="echo fuck"') == [
        'alias fuck="echo fuck" ',
        '[enter/↑/↓/ctrl+c]'
    ]

# Generated at 2022-06-14 09:07:29.622192
# Unit test for function show_corrected_command
def test_show_corrected_command():
    show_corrected_command(CorrectedCommand("command", False))


# Generated at 2022-06-14 09:07:36.728706
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text(
        thefuck.utils.CorrectedCommand('ls --help', 'ls --help')) == \
        '<USER COMMAND>ls --help<RESET> [<GREEN>enter<RESET>/<BLUE>↑<RESET>/<BLUE>↓<RESET>/<RED>ctrl+c<RESET>]'

# Generated at 2022-06-14 09:07:47.974292
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from fuck.conf import ConfigurationDetails
    from thefuck import get_version, pyversion, get_shell_info
    from subprocess import call
    call(['./test_how_to_configure_alias_command'])
    configuration_details = ConfigurationDetails(
        fuck='fuck', path='./test_how_to_configure_alias',
        reload='fuck --alias', content='fuck=\'$(thefuck $(fc -ln -1))\'', can_configure_automatically='True')
    how_to_configure_alias(configuration_details)
    assert not call(['./test_how_to_configure_alias_command'])



# Generated at 2022-06-14 09:07:48.922987
# Unit test for function show_corrected_command
def test_show_corrected_command():
    pass

# Generated at 2022-06-14 09:07:50.882768
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug('Should be debug')
    settings.debug = False
    debug('Should not be debug')

# Generated at 2022-06-14 09:07:53.789829
# Unit test for function debug_time
def test_debug_time():
    def single_debug_time_call():
        with debug_time('msg'):
            pass
    single_debug_time_call()

# Generated at 2022-06-14 09:08:02.682244
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import cStringIO as StringIO
    out = StringIO.StringIO()
    sys.stderr = out

    corrected_command = 'test_command'
    show_corrected_command(corrected_command)

    assert out.getvalue() == 'test_command'

# Generated at 2022-06-14 09:08:04.141424
# Unit test for function debug_time
def test_debug_time():
    from time import sleep
    with debug_time('foo'):
        sleep(1)

# Generated at 2022-06-14 09:08:05.452642
# Unit test for function confirm_text
def test_confirm_text():
    print(confirm_text(5))

# Generated at 2022-06-14 09:08:12.954210
# Unit test for function debug
def test_debug():
    test_string = 'test'
    settings.debug = True
    old_stderr = sys.stderr
    try:
        from StringIO import StringIO
        sys.stderr = myout = StringIO()
        debug(test_string)
        assert myout.getvalue() == '\x1b[34m\x1b[1mDEBUG:\x1b[0m ' + test_string + '\n'
        sys.stderr = myout = StringIO()
        settings.no_colors = True
        debug(test_string)
        assert myout.getvalue() == 'DEBUG: ' + test_string + '\n'
    finally:
        sys.stderr = old_stderr
    settings.debug = False



# Generated at 2022-06-14 09:08:16.066840
# Unit test for function debug
def test_debug():
    import sys
    import mock
    with mock.patch.object(sys, 'stderr') as stderr:
        debug('test message')
        assert stderr.write.called

# Generated at 2022-06-14 09:08:29.062624
# Unit test for function confirm_text
def test_confirm_text():
    sys.stderr.write(u'{prefix}{clear}{bold}{script}{reset}{side_effect} [{green}enter{reset}/{blue}↑{reset}/{blue}↓{reset}/{red}ctrl+c{reset}]').\
        format(prefix=const.USER_COMMAND_MARK, script=u'sudo virsh start vm1', side_effect='', clear='\033[1K\r', bold=color(colorama.Style.BRIGHT),
               green=color(colorama.Fore.GREEN), red=color(colorama.Fore.RED), reset=color(colorama.Style.RESET_ALL),
               blue=color(colorama.Fore.BLUE))


# Generated at 2022-06-14 09:08:31.538189
# Unit test for function color
def test_color():
    assert color('foo') == 'foo'
    settings.no_colors = True
    assert color('foo') == ''



# Generated at 2022-06-14 09:08:32.709357
# Unit test for function debug_time
def test_debug_time():
    debug(u'test_debug_time')



# Generated at 2022-06-14 09:08:39.507267
# Unit test for function debug_time
def test_debug_time():
    def correct_output_format(text):
        return text
    orig_debug = debug
    debug_output = []

    def mock_debug(text):
        debug_output.append(text)
    debug = mock_debug

    with debug_time('test_debug_time'):
        debug('hello world')

    debug = orig_debug
    assert len(debug_output) == 1
    assert 'test_debug_time' in debug_output[0]

# Generated at 2022-06-14 09:08:43.185449
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = create_command('ls')
    assert show_corrected_command(corrected_command) == '$ ls'


# Generated at 2022-06-14 09:08:47.259236
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:08:51.397254
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import unittest
    class Test(unittest.TestCase):
        def test(self):
            self.assertEqual(show_corrected_command('ls'), u'ls\n')
    Test().test()


# Generated at 2022-06-14 09:08:57.656123
# Unit test for function confirm_text
def test_confirm_text():
    from . import rules
    from .shells import Shell

    rule = rules.get_command_rule(u'gitt push',
                                  rules.Command(u'git add . && git commit && git push',
                                                u'git push'))
    corrected_command = ShellCommand(u'git add . && git commit && git push',
                                     shell=Shell())

    import mock
    with mock.patch('sys.stdout') as mock_stdout:
        confirm_text(corrected_command)

# Generated at 2022-06-14 09:09:09.433705
# Unit test for function debug
def test_debug():
    import mock
    import thefuck.shells.safe_shell
    from thefuck.shells.safe_shell import debug
    from thefuck import settings

    with mock.patch('sys.stderr.write') as write:
        with mock.patch('thefuck.shells.safe_shell.settings.debug',
                        True):
            debug(u'Mocked debug output')
            debug('Mocked debug output')
            assert write.call_count == 2
    with mock.patch('sys.stderr.write') as write:
        with mock.patch('thefuck.shells.safe_shell.settings.debug',
                        False):
            debug(u'Mocked debug output')
            debug('Mocked debug output')
            assert write.call_count == 0

# Generated at 2022-06-14 09:09:12.185332
# Unit test for function color
def test_color():
    assert color('bold') == colorama.Style.BRIGHT
    assert color(colorama.Style.BRIGHT) == colorama.Style.BRIGHT



# Generated at 2022-06-14 09:09:25.903707
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .corrected_command import CorrectedCommand
    from .rule import Rule
    from .shells import Shell
    import mock
    import sys

    with mock.patch.object(sys.stdout, 'isatty', return_value=True):
        # Test - with side effect
        show_corrected_command(CorrectedCommand('echo', 'test', Shell('test'), Rule('test'), True))

# Generated at 2022-06-14 09:09:32.470024
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    out = u'''
Seems like The Fuck isn't configured!
Please put `eval $(thefuck --alias)` in your `/home/nvbn/.bashrc` and apply changes with `source /home/nvbn/.bashrc` or restart your shell.
Or run The Fuck a second time to configure it automatically.
More details - https://github.com/nvbn/thefuck#manual-installation
'''
    with colorama.init():
        assert out.strip() == how_to_configure_alias(None).strip()

# Generated at 2022-06-14 09:09:34.336655
# Unit test for function debug_time
def test_debug_time():
    with debug_time("test"):
        pass


# Generated at 2022-06-14 09:09:36.379055
# Unit test for function color
def test_color():
    assert color('red') == '\x1b[31m'



# Generated at 2022-06-14 09:09:40.317547
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(
        {'path': '/home/nvbn/.bashrc', 'content': 'eval $(thefuck --alias)',
         'reload': 'source ~/.bashrc'})



# Generated at 2022-06-14 09:09:44.663484
# Unit test for function color
def test_color():
    assert color(u'foo') == u'foo'



# Generated at 2022-06-14 09:09:48.530991
# Unit test for function show_corrected_command
def test_show_corrected_command():
    assert show_corrected_command({'script': 'test.py', 'side_effect': False}) == None



# Generated at 2022-06-14 09:09:54.831638
# Unit test for function confirm_text
def test_confirm_text():
    from io import StringIO
    from .shells import Bash, Fish
    out = StringIO()
    with settings(no_colors=True):
        with settings(output=out):
            for shell in Bash(), Fish():
                confirm_text(shell.get_command('pwd', 'cd'))
    assert u'pwd; cd' in out.getvalue()



# Generated at 2022-06-14 09:09:58.613764
# Unit test for function color
def test_color():
    assert color('test') == 'test'
    settings.no_colors = True
    assert color('test') == ''



# Generated at 2022-06-14 09:10:09.098640
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from thefuck.shells import Bash
    from thefuck.types import Command, CorrectedCommand
    import os
    old_stdout = sys.stderr
    old_stderr = sys.stdout
    from six import StringIO
    sys.stderr = StringIO()
    sys.stdout = StringIO()
    try:
        bash = Bash()
        corrected_command = bash.parse_alias('fuck ls')
        show_corrected_command(corrected_command)
        assert sys.stderr.getvalue().startswith('Fuck ls\n') or (
            sys.stderr.getvalue().startswith(u'Fuck ls \u2192 '))
        assert sys.stderr.getvalue().endswith('ls --color=auto\n')
    finally:
        sys.stder

# Generated at 2022-06-14 09:10:18.249978
# Unit test for function confirm_text
def test_confirm_text():
    for confirm_text in [
            const.USER_COMMAND_MARK + 'fuck',
            const.USER_COMMAND_MARK + 'fuck ',
            const.USER_COMMAND_MARK + 'fuck +s\n',
            const.USER_COMMAND_MARK + 'fuck +s\n\r',
            const.USER_COMMAND_MARK + 'fuck +s\r\n']:
        sys.stdin.write(confirm_text)
        sys.stdin.seek(0)
        show_corrected_command(
            corrected_command.CorrectedCommand(
                u'fuck', side_effect=True))
        assert sys.stdout.getvalue() == confirm_text[:-1] + ' '
        sys.stdout.seek(0)
        sys.stdout

# Generated at 2022-06-14 09:10:31.521041
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .command import Command
    from .rule import CommandRule
    from .utils import memoize
    from .types import Settings, CorrectedCommand, ShellInfo

    @memoize
    def get_rules(settings):
        return [CommandRule(
            name='test',
            match='',
            get_new_command=lambda cmd: cmd,
            disabled_by_alias=True)]

    @memoize
    def load_settings(settings):
        return settings

    corrected_command = CorrectedCommand(
        Command('ls foo', ''),
        'ls foo',
        True)

    import sys
    s = sys.stderr

# Generated at 2022-06-14 09:10:33.033052
# Unit test for function debug_time
def test_debug_time():
    with debug_time('foo'):
        pass



# Generated at 2022-06-14 09:10:35.145864
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)


# Generated at 2022-06-14 09:10:46.861861
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import StringIO
    from .const import USER_COMMAND_MARK
    from .correct import CorrectedCommand

    user_input = 'fuck'
    corrected_command = CorrectedCommand('ls', '')
    new_output = StringIO.StringIO()
    old_output = sys.stderr
    sys.stderr = new_output
    try:
        show_corrected_command(corrected_command)
    finally:
        sys.stderr = old_output
    output = new_output.getvalue().strip()
    assert output == (USER_COMMAND_MARK + corrected_command.script)
    new_output.close()



# Generated at 2022-06-14 09:10:51.206123
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text(corrected_command=None)

# Generated at 2022-06-14 09:10:53.619834
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug('debug')
    settings.debug = False
    debug('debug')

# Generated at 2022-06-14 09:10:55.991542
# Unit test for function debug_time
def test_debug_time():
    from time import sleep
    with debug_time('sleep'):
        sleep(0.002)

# Generated at 2022-06-14 09:11:06.976504
# Unit test for function how_to_configure_alias

# Generated at 2022-06-14 09:11:09.182163
# Unit test for function debug_time
def test_debug_time():
    with debug_time('lol'):
        import time
        time.sleep(0.2)

# Generated at 2022-06-14 09:11:17.061574
# Unit test for function confirm_text
def test_confirm_text():
    # Arrange
    corrected_command = 'ls'

    # Act
    confirm_text(corrected_command)

    # Assert
    output = sys.stderr.getvalue()
    assert output.startswith(u'(fuck) ls\033[1K\r(fuck) ls [\x1b[32menter\x1b[0m/\x1b[34m↑\x1b[0m/\x1b[34m↓\x1b[0m/\x1b[31mctrl+c\x1b[0m]')

# Generated at 2022-06-14 09:11:18.834443
# Unit test for function debug_time
def test_debug_time():
    import time
    with debug_time('test'):
        time.sleep(0.1)

# Generated at 2022-06-14 09:11:21.677829
# Unit test for function color
def test_color():
    assert(color('red') == 'red')
    settings.no_colors = True
    assert(color('red') == '')

# Generated at 2022-06-14 09:11:23.024384
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text(corrected_command='fuck')

# Generated at 2022-06-14 09:11:25.132333
# Unit test for function debug
def test_debug():
    import mock
    with mock.patch('sys.stderr') as stderr:
        debug(u'hello')
        assert stderr.write.called
        stderr.write.assert_called_with(u'\x1b[94m\x1b[1mDEBUG:\x1b[0m hello\n')



# Generated at 2022-06-14 09:11:34.268459
# Unit test for function color
def test_color():
    assert color('red') == colorama.Fore.RED
    assert color('red') == ''
    settings.no_colors = True
    assert color('red') == ''
    settings.no_colors = False

# Generated at 2022-06-14 09:11:42.987819
# Unit test for function debug
def test_debug():
    from io import StringIO

    debug_stream = StringIO()

    def _debug(*args, **kwargs):
        print(*args, file=debug_stream, **kwargs)

    old_settings_debug = settings.debug
    settings.debug = True
    try:
        debug(u'фыва')
        assert debug_stream.getvalue() == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m фыва\n'  # noqa
    finally:
        settings.debug = old_settings_debug

# Generated at 2022-06-14 09:11:56.437508
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import tempfile

    f_out, f_err = tempfile.TemporaryFile(), tempfile.TemporaryFile()
    sys.stdout, sys.stderr = f_out, f_err
    settings.no_colors = False

    show_corrected_command(
        const.CorrectedCommand(script='ls', side_effect=True))

    f_err.seek(0)
    assert f_err.read() == u'{}ls (+side effect)\n'.format(
        const.USER_COMMAND_MARK).encode('utf-8')

    settings.no_colors = True

    show_corrected_command(
        const.CorrectedCommand(script='ls', side_effect=True))

    f_err.seek(0)

# Generated at 2022-06-14 09:11:58.118519
# Unit test for function confirm_text
def test_confirm_text():
    import StringIO

    confirm_text(StringIO.StringIO())
    confirm_text(StringIO.StringIO())

# Generated at 2022-06-14 09:11:59.360037
# Unit test for function debug_time
def test_debug_time():
    assert debug_time('') == ()

# Generated at 2022-06-14 09:12:06.915040
# Unit test for function debug_time
def test_debug_time():
    from .time import sleep
    import re
    import os

    with debug_time('test'):
        sleep(0.2)
        assert re.match(
            r'test took: \d+ [a-z]+ \d{2}:\d{2}:\d{2}.\d+',
            os.readlink('debug.log'))

# Generated at 2022-06-14 09:12:16.282657
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import sys
    import io
    import mock

    class FakeCorrectedCommand(object):
        def __init__(self, script, side_effect):
            self.script = script
            self.side_effect = side_effect

    with mock.patch('sys.stdout', new=io.StringIO()) as stdout:
        show_corrected_command(FakeCorrectedCommand("ls -la", False))
        assert stdout.getvalue() == 'fuck ls -la\n'

    with mock.patch('sys.stdout', new=io.StringIO()) as stdout:
        show_corrected_command(FakeCorrectedCommand("ls -la", True))
        assert stdout.getvalue() == 'fuck ls -la (+side effect)\n'



# Generated at 2022-06-14 09:12:18.801794
# Unit test for function confirm_text
def test_confirm_text():
    while True:
        confirm_text(script)
        event = yield
        if event.kind == 'user input':
            break

# Generated at 2022-06-14 09:12:19.932704
# Unit test for function debug_time

# Generated at 2022-06-14 09:12:24.587091
# Unit test for function confirm_text
def test_confirm_text():
    assert(
        confirm_text(
            const.CorrectedCommand('lshell', False))
        ==
        u'fuck lshel [enter/↑/↓/ctrl+c]'
    )



# Generated at 2022-06-14 09:12:35.982554
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from thefuck.types import CorrectedCommand
    import sys
    import mock

    m = mock.mock_open()
    with mock.patch(const.OPEN, m, create=True) as f:
        show_corrected_command(CorrectedCommand('git pso', 'git push'))
        m.assert_called_once_with(sys.stdout.fileno(), 'w')
        f.write.assert_called_once_with('{}git push'.format(const.USER_COMMAND_MARK))

# Generated at 2022-06-14 09:12:49.580967
# Unit test for function confirm_text
def test_confirm_text():
    from os import devnull
    from tempfile import NamedTemporaryFile, mkstemp
    from subprocess import Popen, PIPE
    from contextlib import contextmanager
    import shutil

    @contextmanager
    def _std_replacer():
        _old_stdout = sys.stdout
        _old_stderr = sys.stderr
        sys.stdout = sys.stderr = open(os.devnull, "w")
        yield
        sys.stdout = _old_stdout
        sys.stderr = _old_stderr

    with NamedTemporaryFile() as tf:
        _, out_file = mkstemp()
        with open(out_file, "w"):
            pass

        with _std_replacer():
            from . import main

# Generated at 2022-06-14 09:12:51.512157
# Unit test for function color
def test_color():
    assert color('colored') == 'colored'
    settings.no_colors = True
    assert color('colored') == ''

# Generated at 2022-06-14 09:12:54.433495
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test_msg'):
        pass

if __name__ == '__main__':
    test_debug_time()

# Generated at 2022-06-14 09:12:56.776605
# Unit test for function color
def test_color():
    assert color(u'foo') == u'foo'
    assert color(u'foo') == u''

# Generated at 2022-06-14 09:13:08.676187
# Unit test for function confirm_text
def test_confirm_text():
    class DummyCorrectedCommand :
        script = u'ls -la'
        side_effect = True

    import sys
    import io
    sys.stderr = io.StringIO()
    confirm_text(DummyCorrectedCommand())

# Generated at 2022-06-14 09:13:10.385138
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)


# Generated at 2022-06-14 09:13:11.649137
# Unit test for function debug
def test_debug():
    debug('message')



# Generated at 2022-06-14 09:13:22.499583
# Unit test for function confirm_text
def test_confirm_text():
    actual = '\x1b[1K\r\x1b[32mfuck --help\x1b[0m [\x1b[0m\x1b[32menter\x1b[0m/\x1b[34m↑\x1b[0m/\x1b[34m↓\x1b[0m/\x1b[31mctrl+c\x1b[0m]'

# Generated at 2022-06-14 09:13:29.592271
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    from contextlib import closing
    import mock

    assert debug_time('foo') is closing(mock.Mock())
    with debug_time('foo'):
        pass
    assert mock.call(u'foo took: {:.4f}'.format(timedelta().total_seconds())) \
        in mock.Mock().method_calls


# Generated at 2022-06-14 09:13:36.896776
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta

    with debug_time('testing'):
        pass

# Generated at 2022-06-14 09:13:38.817340
# Unit test for function debug_time
def test_debug_time():
    with debug_time('Test'):
        pass

# Generated at 2022-06-14 09:13:44.149864
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    template_msg = u'Test msg'
    with debug_time(msg=template_msg) as now:
        pass
    assert u'Test msg took: {}'.format(timedelta(0)) in debug_msg

# Generated at 2022-06-14 09:13:53.467078
# Unit test for function confirm_text
def test_confirm_text():
    # Without side_effect
    corrected_command = type('CorrectedCommand', (object,), dict(script='ls',
                                                                 side_effect=False))
    assert confirm_text(corrected_command) == '''
[LS] ls [enter/↑/↓/ctrl+c]'''
    # With side_effect
    corrected_command = type('CorrectedCommand', (object,), dict(script='ls',
                                                                 side_effect=True))
    assert confirm_text(corrected_command) == '''
[LS] ls (+side effect) [enter/↑/↓/ctrl+c]'''