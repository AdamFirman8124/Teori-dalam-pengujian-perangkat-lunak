

# Generated at 2022-06-14 09:03:53.435920
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = CorrectedCommand('fuck', False)
    assert confirm_text(corrected_command) == u'$ fuck [enter/↑/↓/ctrl+c]'

# Generated at 2022-06-14 09:03:54.199562
# Unit test for function debug_time
def test_debug_time():
    pass

# Generated at 2022-06-14 09:03:55.421226
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug('hello')

# Generated at 2022-06-14 09:04:01.694775
# Unit test for function debug
def test_debug():
    sys.stderr = StringIO()
    debug('test')
    assert u'DEBUG: test' in sys.stderr.getvalue()


if __name__ == "__main__":
    import doctest
    from StringIO import StringIO
    sys.stderr = StringIO()
    doctest.testmod()

# Generated at 2022-06-14 09:04:12.238668
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import tempfile
    import os
    from .corrector import CorrectedCommand
    import subprocess

    class FooCommand(object):
        def __init__(self, script):
            self.script = script

    commands = (FooCommand('pwd'), FooCommand('ls -ali'))

    with tempfile.TemporaryFile(mode='w+') as f:
        stdout = sys.stderr
        sys.stderr = f
        show_corrected_command(CorrectedCommand('pwd', commands))
        show_corrected_command(CorrectedCommand('ls -ali', commands))
        f.flush()
        f.seek(0)
        result = f.read()
    sys.stderr = stdout

# Generated at 2022-06-14 09:04:13.383026
# Unit test for function debug_time
def test_debug_time():
    with debug_time('some debug'):
        pass

# Generated at 2022-06-14 09:04:26.683413
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import os
    import tempfile
    from .command import Command
    from .shells.base import BaseShell
    from .shells import get_shell
    from .types import CorrectedCommand

    shell = BaseShell()
    _, tmp = tempfile.mkstemp()
    os.close(_)

    # Positive test
    shell.file_system.touch(tmp)

    command = Command(script=u'ls', side_effect=True)
    corrected_command = CorrectedCommand(u'cat {}'.format(tmp),
                                         side_effect=False)
    show_corrected_command(corrected_command)

    # Negative text
    corrected_command = CorrectedCommand(u'ls', side_effect=False)
    show_corrected_command(corrected_command)



# Generated at 2022-06-14 09:04:37.988342
# Unit test for function confirm_text
def test_confirm_text():
    # Test with some examples
    assert confirm_text(corrected_command = {
                            'script': '/usr/bin/fuck',
                            'side_effect': True}) \
                        == u'$ {clear}{bold}/usr/bin/fuck{reset} (+side effect) [{green}enter{reset}/{blue}↑{reset}/{blue}↓{reset}/{red}ctrl+c{reset}]'
    assert confirm_text(corrected_command = {
                            'script': '/usr/bin/fuck',
                            'side_effect': False}) \
                        == u'$ {clear}{bold}/usr/bin/fuck{reset} [{green}enter{reset}/{blue}↑{reset}/{blue}↓{reset}/{red}ctrl+c{reset}]'

#

# Generated at 2022-06-14 09:04:44.136439
# Unit test for function show_corrected_command
def test_show_corrected_command():
    class CorrectedCommand():
        script = 'ls -l'
        side_effect = False
    assert show_corrected_command(CorrectedCommand) == u'$ls -l\n'
    CorrectedCommand.side_effect = True
    assert show_corrected_command(CorrectedCommand) == u'$ls -l (+side effect)\n'


# Generated at 2022-06-14 09:04:51.371624
# Unit test for function debug
def test_debug():
    import os
    import sys

    temp_filename = 'temp_file.txt'
    f = open(temp_filename, 'w')
    sys.stderr = f
    debug("Debugging message.")
    f.close()
    f = open(temp_filename, 'r')
    l = f.readline()
    f.close()
    os.remove(temp_filename)
    assert "DEBUG:" in l
    assert "Debugging message." in l

# Generated at 2022-06-14 09:04:56.285065
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:05:05.234909
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from mock import patch
    from thefuck.utils import get_closest
    from thefuck.shells import GnuLike

    with patch('sys.stderr') as stderr:
        show_corrected_command(get_closest(u'git ci', {}))
        show_corrected_command(get_closest(u'git ci', {},
                                           side_effect="git config --global user.email 'nvbn@thefuck.io'"))
    stderr.write.assert_called_with(u'\x1b[1m$ git commit\x1b[21m\n')
    stderr.write.assert_called_with(u'\x1b[1m$ git commit\x1b[21m (+side effect)\n')

# Generated at 2022-06-14 09:05:18.821347
# Unit test for function debug_time
def test_debug_time():
    import time
    from .utils import capture_stdout
    from .versions import python_version
    from .conf import load_settings

    settings = load_settings(['debug'])

    with capture_stdout() as output:
        with debug_time('Test of debug_time'):
            time.sleep(1)

    assert output.stdout.startswith('[DEBUG] Test of debug_time took:')

    with capture_stdout() as output:
        with debug_time('Test of debug_time'):
            time.sleep(1)

    assert output.stdout.startswith('[DEBUG] Test of debug_time took:')

    with capture_stdout() as output:
        with debug_time('Test of debug_time'):
            time.sleep(1)

    assert output.stdout.startswith

# Generated at 2022-06-14 09:05:20.971029
# Unit test for function color
def test_color():
    assert color(colorama.Back.RED + colorama.Fore.WHITE + colorama.Style.BRIGHT) == const.COLORS_MARK

# Generated at 2022-06-14 09:05:23.383678
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)



# Generated at 2022-06-14 09:05:28.212568
# Unit test for function debug_time
def test_debug_time():
    import StringIO
    import time

    stream = StringIO.StringIO()
    with debug_time('xyz', stream=stream):
        time.sleep(0.2)
    assert 'DEBUG: xyz took: ' in stream.getvalue()
    assert 'seconds' in stream.getvalue()

# Generated at 2022-06-14 09:05:32.392859
# Unit test for function confirm_text
def test_confirm_text():
    show_corrected_command('test')
    assert sys.stderr.getvalue() == '>test [enter/↑/↓/ctrl+c]\n'

# Generated at 2022-06-14 09:05:43.500218
# Unit test for function confirm_text
def test_confirm_text():
    def call_confirm_text(corrected_command, capsys):
        confirm_text(corrected_command)
        out, err = capsys.readouterr()
        return out, err
    from .shells import Bash, Fish, Zsh
    from .correct import Command
    for shell_object in [Bash, Fish, Zsh]:
        with shell_object.from_shell(None, 'fish') as shell:
            corrected_command = Command('brew', 'brew', 'brew update')
            script = confirm_text(corrected_command)
            out, err = call_confirm_text(corrected_command, capsys)

# Generated at 2022-06-14 09:05:56.378568
# Unit test for function debug
def test_debug():
    from StringIO import StringIO
    from contextlib import contextmanager
    from thefuck.utils import wrap_streams

    @contextmanager
    def debug_env():
        with wrap_streams(stderr=StringIO()) as (out, err):
            yield out, err

    with debug_env() as (out, err):
        debug("First debug message")
        debug("Second debug message")
        debug("Third debug message")


# Generated at 2022-06-14 09:05:59.537148
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .rule import Command
    x = Command('hey', 'key')
    show_corrected_command(x)


if __name__ == "__main__":
    test_show_corrected_command()

# Generated at 2022-06-14 09:06:07.795251
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import tempfile
    import os
    sys.stderr = open(tempfile.mkstemp()[1], 'w')
    show_corrected_command("ls")
    sys.stderr.close()
    with open(sys.stderr.name) as f:
        assert f.read() == "  $ ls\n"
    os.remove(sys.stderr.name)

# Generated at 2022-06-14 09:06:13.530369
# Unit test for function color
def test_color():
    from . import Shell

    __builtins__['__name__'] = '__main__'
    settings.no_colors = True
    assert color('abc') == ''

    settings.no_colors = False
    assert color('abc') == 'abc'



# Generated at 2022-06-14 09:06:25.238423
# Unit test for function debug
def test_debug():
    # test single messages
    debug('Test')
    assert sys.stderr.getvalue() == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m Test\n'

    # test several messages
    sys.stderr.truncate(0)
    sys.stderr.seek(0)
    debug('Test1')
    debug('Test2')
    assert sys.stderr.getvalue() == (
        u'\x1b[34m\x1b[1mDEBUG:\x1b[0m Test1\n'
        u'\x1b[34m\x1b[1mDEBUG:\x1b[0m Test2\n')

# Generated at 2022-06-14 09:06:29.621838
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .correct import CorrectedCommand

    assert show_corrected_command(CorrectedCommand('ls')) == \
        const.USER_COMMAND_MARK + 'ls\n'

    assert show_corrected_command(CorrectedCommand('ls', True)) == \
        const.USER_COMMAND_MARK + 'ls (+side effect)\n'



# Generated at 2022-06-14 09:06:30.397693
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text('git pull')

# Generated at 2022-06-14 09:06:40.406843
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    import mock
    from thefuck.utils import debug_time

    m = mock.Mock()

    with debug_time('test'):
        m()

    m.assert_called_with()
    debug_logs = [call[0][0]
                  for call in mock.call_args_list
                  if call[0][0].startswith('test took')]
    assert len(debug_logs) == 1
    assert timedelta(seconds=0) < timedelta.fromtimestamp(
        float(debug_logs[0].split()[2]))

# Generated at 2022-06-14 09:06:42.452251
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass



# Generated at 2022-06-14 09:06:47.718426
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from . import types

    corrected_command1 = types.CorrectedCommand(script='ls', side_effect=False)
    show_corrected_command(corrected_command1)

    corrected_command2 = types.CorrectedCommand(script='ls', side_effect=True)
    show_corrected_command(corrected_command2)

# Generated at 2022-06-14 09:06:52.819429
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .correct import CorrectedCommand
    corrected_command = CorrectedCommand('ls', 'ls -lha', False)
    show_corrected_command(corrected_command)
    assert u'fuck ls -lha\n' == sys.stderr.getvalue()


# Generated at 2022-06-14 09:06:57.390439
# Unit test for function color
def test_color():
    assert color(u'привет') == u'привет'
    settings.no_colors = True
    assert color(u'привет') == u''
    settings.no_colors = False



# Generated at 2022-06-14 09:07:09.195147
# Unit test for function confirm_text
def test_confirm_text():
    from StringIO import StringIO
    import sys
    import const

    old_stdout = sys.stderr
    mystdout = StringIO()
    sys.stderr = mystdout
    from . import output
    corrected_command = u'git commig --message "some message"'
    output.confirm_text(corrected_command)
    assert mystdout.getvalue() == u'{}git commig --message "some message" [] [enter/↑/↓/ctrl+c]'.format(const.USER_COMMAND_MARK)
    sys.stderr = old_stdout

# Generated at 2022-06-14 09:07:13.334489
# Unit test for function show_corrected_command
def test_show_corrected_command():
    show_corrected_command(__builtins__['CorrectedCommand'](script='touch', side_effect=False))


if __name__ == '__main__':
    test_show_corrected_command()

# Generated at 2022-06-14 09:07:22.761539
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .shells import shell_info, get_aliases
    from .utils import get_closest

    closest_shell_info = get_closest('/bin/bash')
    assert closest_shell_info.name == 'bash'
    assert closest_shell_info.path == '/bin/bash'

# Generated at 2022-06-14 09:07:30.628934
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import os
    show_corrected_command('ls -lah')
    if os.name != 'nt':
        assert sys.stderr.getvalue() == const.USER_COMMAND_MARK + 'ls -lah\n'
    else:
        assert sys.stderr.getvalue() == const.USER_COMMAND_MARK + 'ls -lah\n'
    sys.stderr = sys.__stderr__

# Generated at 2022-06-14 09:07:41.098436
# Unit test for function debug
def test_debug():
    from ..utils import wrap_streams

    with wrap_streams('', 'stderr') as (stdin, stderr):
        debug(u'генерал')
        stderr.seek(0)
        assert u'DEBUG: генерал' in stderr.read()

        debug(u'\nгенерал')
        stderr.seek(0)
        assert u'DEBUG: генерал' in stderr.read()

        debug(u'генерал\n')
        stderr.seek(0)
        assert u'DEBUG: генерал\n' in stderr.read()


# Generated at 2022-06-14 09:07:42.821384
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text(u'fuck')
    confirm_text(u'fuck')

# Generated at 2022-06-14 09:07:45.889148
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from thefuck.rules.git import match, get_new_command
    match, get_new_command(u'git add ', u'git add ')


# Generated at 2022-06-14 09:07:50.133712
# Unit test for function color
def test_color():
    assert color(colorama.Fore.RED) == colorama.Fore.RED
    assert not settings.no_colors
    settings.no_colors = True
    assert not color(colorama.Fore.RED)
    settings.no_colors = False



# Generated at 2022-06-14 09:07:52.803167
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text(const.CorrectedCommand('python fuck.py', False))



# Generated at 2022-06-14 09:07:55.003004
# Unit test for function debug_time
def test_debug_time():
    import time
    with debug_time('test'):
        time.sleep(1)

# Generated at 2022-06-14 09:08:03.340216
# Unit test for function debug
def test_debug():
    def func1():
        debug('this is a debug message')
    func1()
    # output debug message when debug is set to True


# Generated at 2022-06-14 09:08:12.407283
# Unit test for function color
def test_color():
    @contextmanager
    def disabled():
        old_value = settings.no_colors
        settings.no_colors = True
        try:
            yield
        finally:
            settings.no_colors = old_value

    with disabled():
        assert color('') == ''
        assert color('\033[1m') == ''
        assert color('\033[1m\033[31m') == ''
        assert color('\033[1m\033[31m\033[0m') == ''

    assert color('') == ''
    assert color('\033[1m') == '\033[1m'
    assert color('\033[1m\033[31m') == '\033[1m\033[31m'

# Generated at 2022-06-14 09:08:16.583638
# Unit test for function debug
def test_debug():
    try:
        result = ''
        with settings.debug(True):
            debug(u'hello')
            result = sys.stderr.getvalue()
    finally:
        sys.stderr = sys.__stderr__
    assert 'hello' in result

# Generated at 2022-06-14 09:08:29.101413
# Unit test for function confirm_text
def test_confirm_text():
    from .shells import Bash

    class Config(object):
        no_colors = False
        require_confirmation = True

    corrected_command = Bash.from_shell('pwd', 'pwd -P')
    settings.no_colors = False
    settings.require_confirmation = True

    assert confirm_text(corrected_command) == (
        u'f  pwd -P [\x1b[32menter\x1b[0m/\x1b[34m↑\x1b[0m/\x1b[34m↓'
        u'\x1b[0m/\x1b[31mctrl+c\x1b[0m]')

    del settings.require_confirmation
    del settings.no_colors

# Generated at 2022-06-14 09:08:31.221466
# Unit test for function debug_time
def test_debug_time():
    from time import sleep

    with debug_time('test'):
        sleep(1)



# Generated at 2022-06-14 09:08:37.328907
# Unit test for function debug
def test_debug():
    import StringIO
    import sys
    settings.debug = True
    old_stdout = sys.stderr
    try:
        new_stdout = sys.stderr = StringIO.StringIO()
        debug('Hello World!')
        assert 'Hello World!' in new_stdout.getvalue()
    finally:
        sys.stderr = old_stdout

# Generated at 2022-06-14 09:08:43.813256
# Unit test for function color
def test_color():
    assert color(colorama.Fore.RED)('foo') == colorama.Fore.RED + 'foo'
    assert color()(None) == ''



# Generated at 2022-06-14 09:08:50.998744
# Unit test for function debug
def test_debug():
    from mock import patch
    from io import StringIO
    with patch('thefuck.utils.sys') as mock_sys:
        mock_sys.stderr = StringIO()
        debug('Test debug')
        assert mock_sys.stderr.getvalue() == '\x1b[34m\x1b[1mDEBUG:\x1b[0m Test debug\n'



# Generated at 2022-06-14 09:08:59.878182
# Unit test for function show_corrected_command
def test_show_corrected_command():
  class CorrectedCommand:
      def __init__(self, script, side_effect):
          self.script = script
          self.side_effect = side_effect
  corrected_command = CorrectedCommand("ls -1", False)
  expected = const.USER_COMMAND_MARK + "ls -1\n"
  actual = show_corrected_command(corrected_command)
  assert actual == expected
  corrected_command = CorrectedCommand("ls -1", True)
  expected = const.USER_COMMAND_MARK + "ls -1 (+side effect)\n"
  actual = show_corrected_command(corrected_command)
  assert actual == expected

# Generated at 2022-06-14 09:09:04.337400
# Unit test for function confirm_text
def test_confirm_text():
    class Command:
        def __init__(self):
            self.script = "echo 'hi'"
            self.side_effect = False

    confirm_text(Command())

# Generated at 2022-06-14 09:09:10.838305
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:09:18.382908
# Unit test for function debug
def test_debug():
    from StringIO import StringIO
    orig_stderr = sys.stderr
    sys.stderr = StringIO()
    try:
        debug(u'hello')
        assert sys.stderr.getvalue() == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m hello\n'
    finally:
        sys.stderr = orig_stderr

# Generated at 2022-06-14 09:09:25.272213
# Unit test for function color
def test_color():
    assert (color(colorama.Back.RED + colorama.Fore.WHITE
                  + colorama.Style.BRIGHT)) == ''
    settings.no_colors = False
    assert (color(colorama.Back.RED + colorama.Fore.WHITE
                  + colorama.Style.BRIGHT)) != ''

# Generated at 2022-06-14 09:09:28.843863
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    print("###################################################################")
    print("UNIT TEST FOR FUNCTION how_to_configure_alias")
    print("###################################################################")
    how_to_configure_alias("test")

# Generated at 2022-06-14 09:09:42.274594
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from datetime import datetime
    from .shells import ShellInfo

    # Success case
    configuration_details = ShellInfo(
        name=u'shell',
        conf_file=u'file',
        conf_file_exists=True,
        reload_command=u'reload',
        reload_method=u'how',
        can_configure_automatically=True)
    how_to_configure_alias(configuration_details)

    # Failure case
    configuration_details = ShellInfo(
        name=u'shell',
        conf_file=u'file',
        conf_file_exists=False,
        reload_command=u'reload',
        reload_method=u'how',
        can_configure_automatically=False)

# Generated at 2022-06-14 09:09:43.811138
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test_debug_time'):
        pass

# Generated at 2022-06-14 09:09:45.294308
# Unit test for function show_corrected_command
def test_show_corrected_command():
    show_corrected_command(None)



# Generated at 2022-06-14 09:09:49.068549
# Unit test for function show_corrected_command

# Generated at 2022-06-14 09:09:50.594649
# Unit test for function debug
def test_debug():
    debug('test debug')



# Generated at 2022-06-14 09:09:52.811286
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test_debug_time'):
        import time
        time.sleep(2)

# Generated at 2022-06-14 09:10:08.820126
# Unit test for function debug
def test_debug():
    import StringIO
    try:
        orig_stderr = sys.stderr
        sys.stderr = StringIO.StringIO()
        try:
            settings.debug = True
            debug(u'test')
            assert u'debug' in sys.stderr.getvalue().lower()
            assert u'test' in sys.stderr.getvalue().lower()
            sys.stderr.truncate(0)

            settings.debug = False
            debug(u'test')
            assert u'debug' not in sys.stderr.getvalue().lower()
            assert u'test' not in sys.stderr.getvalue().lower()
        finally:
            sys.stderr = orig_stderr
    except ImportError:
        pass

# Generated at 2022-06-14 09:10:14.748314
# Unit test for function debug
def test_debug():
    from mock import Mock
    from .settings import Settings, NoColors
    from . import utils as u
    sett = Settings(debug=True, no_colors=NoColors())
    u.settings = sett
    mock = Mock()
    u.debug(mock)
    assert mock in sys.stderr.write.call_args[0][0]


# Generated at 2022-06-14 09:10:19.193472
# Unit test for function show_corrected_command
def test_show_corrected_command():
    command = "ls -l"
    corrected_command = command + " && cd .."
    expected = "> ls -l && cd .."

    show_corrected_command(corrected_command)

# Generated at 2022-06-14 09:10:21.196739
# Unit test for function show_corrected_command
def test_show_corrected_command():
    assert show_corrected_command(corrected_command=None) == None


# Generated at 2022-06-14 09:10:22.465910
# Unit test for function debug
def test_debug():
    assert debug('test') is None



# Generated at 2022-06-14 09:10:28.832917
# Unit test for function debug_time
def test_debug_time():
    import mock

    with mock.patch('thefuck.shells.atf_sh.atf_sh.debug',
                    mock.Mock(side_effect=lambda x: x)) as debug:
        with debug_time('test_debug_time'):
            pass

    debug.assert_called_once_with('test_debug_time took: 0:00:00.000000')

# Generated at 2022-06-14 09:10:32.604486
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from thefuck.utils import get_closest
    command = get_closest('correct_command', lambda x: x.script == 'git push origin master')
    show_corrected_command(command)

# Generated at 2022-06-14 09:10:34.832790
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta

    debug_time('context-manager')
    assert True

# Generated at 2022-06-14 09:10:48.195347
# Unit test for function confirm_text
def test_confirm_text():
    from StringIO import StringIO
    import sys

    result = StringIO()
    sys.stderr = result
    from commands import CorrectedCommand
    from . import utils

    corrected_command = CorrectedCommand(script="test script",
                                         side_effect=True)

    utils.confirm_text(corrected_command)
    assert result.getvalue() == u'\x00\033[1K\r\x00\x1b[1mtest script\x1b[0m ' \
                                u'(+side effect) [\x1b[32menter\x1b[0m/' \
                                u'\x1b[34m\u2191\x1b[0m/\x1b[34m\u2193\x1b[0m/' \
                

# Generated at 2022-06-14 09:10:50.570866
# Unit test for function color
def test_color():
    assert color('blue') == ''
    assert color('bold') == ''
    assert color('red') == ''



# Generated at 2022-06-14 09:11:05.698370
# Unit test for function debug_time
def test_debug_time():
    from cStringIO import StringIO
    from datetime import timedelta
    from . import log
    from . import const
    import mock

    new_log = []

    def debug(*args):
        new_log.append(args[0])

    old_handler = log.log_handler
    log.log_handler = debug

    try:
        with log.debug_time('test'):
            import time
            time.sleep(0.1)
        assert new_log[0] == 'test took: 0:00:00.101000'
    finally:
        log.log_handler = old_handler

# Generated at 2022-06-14 09:11:09.723072
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .rule import Command
    from .shells import Bash
    show_corrected_command(Command('pwd', 'ls', side_effect=True,
        script='pwd', shell=Bash()))



# Generated at 2022-06-14 09:11:19.143130
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import io
    sys.stderr = buffer = io.StringIO()

    from .utils import show_corrected_command
    from .command import CorrectedCommand

    show_corrected_command(CorrectedCommand(u'ls', True))

    sys.stderr = sys.__stderr__
    assert buffer.getvalue().strip() == u'f! ls (+side effect)'

# Generated at 2022-06-14 09:11:21.002109
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)


# Generated at 2022-06-14 09:11:26.887713
# Unit test for function show_corrected_command
def test_show_corrected_command():
    show_corrected_command('Corrected_command')
    assert(1 == 1)


# Generated at 2022-06-14 09:11:29.689891
# Unit test for function debug
def test_debug():
    msg = u"test"
    debug(msg)
    assert msg in sys.stderr.getvalue()

# Generated at 2022-06-14 09:11:31.417526
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    assert how_to_configure_alias() == None


# Generated at 2022-06-14 09:11:38.450989
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    from .conf import Config
    from .shells import Shell
    from .utils import get_time

    with debug_time('Test') as timed_context:
        assert isinstance(timed_context, timedelta)
        get_time.return_value = timedelta(seconds=42, microseconds=147000)
        debug_time('Fuck')

# Generated at 2022-06-14 09:11:41.007323
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .shells import SimpleCommand
    corrected_command = SimpleCommand('git', 'log', output='git branch')
    const._OLD_STDOUT = sys.stdout
    out = const._StringIO()
    sys.stdout = out
    show_corrected_command(corrected_command)
    result = out.getvalue().strip()
    assert result == const.USER_COMMAND_MARK + corrected_command.script

# Generated at 2022-06-14 09:11:45.315847
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .utils import wrap_command, Command
    def print_corrected_command(script, side_effect=False):
        show_corrected_command(Command(wrap_command(script), side_effect=side_effect))

    print_corrected_command(u'ls')
    print_corrected_command(u'git branch --format="%(refname)")')
    print_corrected_command(u'git branch --format="%(refname)")', True)

# Generated at 2022-06-14 09:12:01.967090
# Unit test for function debug
def test_debug():
    import io
    import sys
    import unittest.mock
    sys.stderr = io.StringIO()
    debug('foo')
    debug('bar')
    sys.stderr = unittest.mock.Mock()
    assert sys.stderr.write.call_args_list == [
        ((u'\x1b[34m\x1b[1mDEBUG:\x1b[0m foo\n',), {}),
        ((u'\x1b[34m\x1b[1mDEBUG:\x1b[0m bar\n',), {})]

# Generated at 2022-06-14 09:12:15.104803
# Unit test for function debug
def test_debug():
    messages = []

    def mock_sys_stderr_write(msg):
        messages.append(msg)

    settings.debug = True
    old_sys_stderr_write = sys.stderr.write
    sys.stderr.write = mock_sys_stderr_write
    try:
        debug(u'Enabled')
        assert messages[-1] == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m Enabled\n'
        settings.debug = False
        debug(u'Disabled')
        assert messages[-1] == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m Disabled\n'
    finally:
        sys.stderr.write = old_sys_stderr_write

# Generated at 2022-06-14 09:12:15.989108
# Unit test for function debug_time
def test_debug_time():
    with debug_time('Smthg'):
        pass

# Generated at 2022-06-14 09:12:25.134823
# Unit test for function debug
def test_debug():
    import StringIO
    from contextlib import closing
    with closing(StringIO.StringIO()) as output:
        with debug_time('test'):
            with closing(sys.stderr):
                sys.stderr = output
                debug('test')
        assert 'DEBUG: test' in output.getvalue()

# Generated at 2022-06-14 09:12:29.233629
# Unit test for function debug_time
def test_debug_time():
    import os
    if 'DEBUG' not in os.environ:
        try:
            os.environ['DEBUG'] = 'true'
            with debug_time("msg"):
                pass
        finally:
            del os.environ['DEBUG']

# Generated at 2022-06-14 09:12:37.357574
# Unit test for function show_corrected_command
def test_show_corrected_command():
    for corrected_command in [["cd /tmp", False], ["cd /tmp", True]]:
        sys.stderr = sys.__stderr__
        sys.stderr.write = sys.__stderr__.write
        sys.stderr.write(u"{user_command_mark}{command}{end}".format(
            user_command_mark=const.USER_COMMAND_MARK,
            command=corrected_command[0],
            end=u' (+side effect)' if corrected_command[1] else ''))
    return

# Generated at 2022-06-14 09:12:47.373313
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    import StringIO
    out = StringIO.StringIO()
    sys.stderr = out
    how_to_configure_alias(None)

    result = (u"Seems like " + \
              color(colorama.Style.BRIGHT) + \
              u"fuck" + \
              color(colorama.Style.RESET_ALL) + \
              u" alias isn't configured!\n"
              u"More details - https://github.com/nvbn/thefuck#manual-installation\n")
    assert result in out.getvalue()


# Generated at 2022-06-14 09:12:50.268859
# Unit test for function confirm_text
def test_confirm_text():
    import colorama
    colorama.init()
    confirm_text('')


if __name__ == '__main__':
    test_confirm_text()

# Generated at 2022-06-14 09:12:53.458028
# Unit test for function color
def test_color():  # pragma: no branch
    assert color(colorama.Fore.RED) == colorama.Fore.RED
    assert color(colorama.Fore.RED) == ''

# Generated at 2022-06-14 09:12:55.536504
# Unit test for function color
def test_color():
    assert color('foo') == 'foo'
    settings.no_colors = True
    assert color('foo') == ''

# Generated at 2022-06-14 09:13:19.225346
# Unit test for function debug
def test_debug():
    from .conf import settings
    from io import StringIO
    output = StringIO()

    settings.debug = True

    debug_print = __import__('functools').partial(print, file=output)
    with __import__('contextlib').redirect_stdout(output):
        debug('Hello world!')
        debug_print()

    output.seek(0)
    output_lines = output.readlines()
    output_lines = [line.rstrip() for line in output_lines]

    assert output_lines == [
        u'\x1b[34m\x1b[1mDEBUG:\x1b[0m Hello world!', '']

    # Disable debug output
    settings.debug = False
    output = StringIO()

# Generated at 2022-06-14 09:13:28.746317
# Unit test for function confirm_text
def test_confirm_text():
    script = u'ls -a'
    corrected_command = Command(script, corrected=True)
    confirm_text(corrected_command)
    assert sys.stderr.getvalue() == u'{}ls -a [enter/↑/↓/ctrl+c]'.format(const.USER_COMMAND_MARK)
    sys.stderr.truncate(0)
    corrected_command = Command(script, side_effect=True, corrected=True)
    confirm_text(corrected_command)
    assert sys.stderr.getvalue() == u'{}ls -a (+side effect) [enter/↑/↓/ctrl+c]'.format(const.USER_COMMAND_MARK)

# Generated at 2022-06-14 09:13:35.666228
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)
    how_to_configure_alias(const.ConfigurationDetails(
        path='/home/user/.zshrc',
        content='eval $(fuck --alias)',
        reload='exec $SHELL -l',
        can_configure_automatically=True))
    how_to_configure_alias(const.ConfigurationDetails(
        path='/home/user/.zshrc',
        content='eval $(fuck --alias)',
        reload='exec $SHELL -l',
        can_configure_automatically=False))



# Generated at 2022-06-14 09:13:37.516803
# Unit test for function debug_time
def test_debug_time():
    import time
    with debug_time('test'):
        time.sleep(1)

# Generated at 2022-06-14 09:13:40.096698
# Unit test for function color
def test_color():
    assert color('bold') == colorama.Style.BRIGHT



# Generated at 2022-06-14 09:13:47.033666
# Unit test for function debug_time
def test_debug_time():
    from contextlib import contextmanager
    from datetime import datetime
    from StringIO import StringIO

    @contextmanager
    def debug_time(msg):
        started = datetime.now()
        try:
            yield
        finally:
            print(u'{} took: {}'.format(msg, datetime.now() - started))

    with StringIO() as log, debug_time('msg'):
        pass

    assert u'msg took: ' in log.getvalue()

