

# Generated at 2022-06-14 09:03:59.351040
# Unit test for function confirm_text
def test_confirm_text():
    from .shells import Shell
    shell = Shell()
    from .types import Command
    shell.from_shell = Command("ls", "ls")
    confirm_text(shell.from_shell)

# Generated at 2022-06-14 09:04:03.155020
# Unit test for function color
def test_color():
    assert color('\033[42;97m') == '\033[42;97m'
    settings.no_colors = True
    assert color('\033[42;97m') == ''

# Generated at 2022-06-14 09:04:11.213783
# Unit test for function confirm_text
def test_confirm_text():
    from six import StringIO
    # mocking stdout
    sys.stderr = StringIO()
    # call
    confirm_text(['ls'])
    # assert the output matches what we want
    assert sys.stderr.getvalue() == (
        "\033[1K\r[fuck]ls [\033[32menter\033[0m/\033[34m↑\033[0m/\033[34m↓"
        "\033[0m/\033[31mctrl+c\033[0m]")

# Generated at 2022-06-14 09:04:24.952207
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    from mock import patch


# Generated at 2022-06-14 09:04:37.029379
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .shells import Shell
    from .configuration import Configuration
    import mock
    import os
    import platform
    import string
    import random

    def rand_path():
        return os.path.join(*(random.choice(string.ascii_letters)
                              for _ in range(random.randrange(10))))


# Generated at 2022-06-14 09:04:39.361063
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)
    how_to_configure_alias(True)


# Generated at 2022-06-14 09:04:43.968496
# Unit test for function color
def test_color():
    assert color(colorama.Fore.RED) == colorama.Fore.RED
    assert color('red') == ''
    settings.no_colors = True
    assert color('red') == ''
    assert color(colorama.Fore.RED) == ''
    settings.no_colors = False

# Generated at 2022-06-14 09:04:44.701432
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:04:51.424592
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    import sys
    sys.stdout = open('test.txt', 'w')
    how_to_configure_alias('test')
    sys.stdout.close()
    with open('test.txt', 'r') as f:
        lines = f.readlines()
        assert lines[0].startswith('Seems like fuck alias isn\'t configured!')
        assert lines[1].startswith('Please put fuck =')


# Generated at 2022-06-14 09:04:55.444548
# Unit test for function debug
def test_debug():
    from mock import patch

    with patch('sys.stderr') as stderr_mock:
        debug('test log')

    stderr_mock.write.assert_called_with('test log\n')



# Generated at 2022-06-14 09:05:05.682609
# Unit test for function debug
def test_debug():
    from io import StringIO
    debug_out = StringIO()
    old_stderr = sys.stderr
    sys.stderr = debug_out
    debug('Hello world')
    assert debug_out.getvalue() == ''
    settings.debug = True
    debug('Hello world')
    assert debug_out.getvalue().endswith('Hello world\n')
    sys.stderr = old_stderr

# Generated at 2022-06-14 09:05:13.606305
# Unit test for function confirm_text
def test_confirm_text():
    from mock import patch
    with patch('sys.stderr') as syserr:
        confirm_text(const.CorrectedCommand('git', '', '', None))
        syserr.write.assert_called_with(
            u'$ git [\x1b[32menter\x1b[0m/\x1b[34m↑\x1b[0m/\x1b[34m↓\x1b[0m/\x1b[31mctrl+c\x1b[0m]')

# Generated at 2022-06-14 09:05:19.443946
# Unit test for function show_corrected_command
def test_show_corrected_command():
    assert show_corrected_command(corrected_command=const.CorrectedCommand(
        script='ls -lha', side_effect=False)) == 'ls -lha'
    assert show_corrected_command(corrected_command=const.CorrectedCommand(
        script='ls -la', side_effect=True)) == 'ls -la (+side effect)'


# Generated at 2022-06-14 09:05:20.674616
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = "fuck a"
    confirm_text(corrected_command)
    #test if the output is correct
    assert corrected_command == "fuck a"


# Generated at 2022-06-14 09:05:25.434054
# Unit test for function color
def test_color():
    assert color(colorama.Fore.RED + 'foo' + colorama.Fore.RESET) == ''
    assert color(colorama.Fore.RED + 'foo' + colorama.Fore.RESET) == ''

# Generated at 2022-06-14 09:05:27.809037
# Unit test for function color
def test_color():
    assert(color('') == '')
    settings.no_colors = True
    assert(color('x') == '')

# Generated at 2022-06-14 09:05:31.680788
# Unit test for function confirm_text
def test_confirm_text():
    from thefuck.shells.bash import Bash

    show_corrected_command(
        Bash.from_shell(script='brew update && brew upgrade && brew cask',
                        side_effect=True))

# Generated at 2022-06-14 09:05:34.740777
# Unit test for function debug
def test_debug():
    assert debug('aaa') == sys.stderr.write('\x1b[34m\x1b[1mDEBUG:\x1b[0m aaa\n')



# Generated at 2022-06-14 09:05:38.910330
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    with debug_time('test'):
        pass
    from mock import call
    from thefuck.utils import debug
    debug.assert_called_with(u'test took: 0:00:00.000')

# Generated at 2022-06-14 09:05:52.827409
# Unit test for function confirm_text
def test_confirm_text():
    from StringIO import StringIO
    import sys
    import re
    stdout = sys.stderr
    sys.stderr = StringIO()
    confirm_text('ls -al')
    res = sys.stderr.getvalue()
    sys.stderr = stdout

# Generated at 2022-06-14 09:06:01.821104
# Unit test for function debug
def test_debug():
    from tests.utils import create_mock, captured_output

    with captured_output() as (_, _, s_err):
        debug(u'foo')
    assert u'foo' not in s_err.getvalue()
    settings.debug = True
    with captured_output() as (_, _, s_err):
        debug(u'bar')

    assert u'bar' in s_err.getvalue()
    settings.debug = False



# Generated at 2022-06-14 09:06:02.305992
# Unit test for function debug
def test_debug():
    debug('message')

# Generated at 2022-06-14 09:06:04.298841
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)
    how_to_configure_alias(None)



# Generated at 2022-06-14 09:06:12.259110
# Unit test for function debug
def test_debug():
    import StringIO

    buf = StringIO.StringIO()
    debug = lambda msg: buf.write(msg + '\n')
    debug('Foo')
    assert buf.getvalue() == 'Foo\n'

    buf = StringIO.StringIO()
    settings.debug = True
    debug('Bar')
    assert buf.getvalue() == ''

    buf = StringIO.StringIO()
    debug('Baz')
    assert buf.getvalue() == 'Baz\n'

# Generated at 2022-06-14 09:06:15.211912
# Unit test for function debug
def test_debug():
    # Test with settings.debug = True
    settings.debug = True
    debug('test')
    settings.debug = False
    debug('test')



# Generated at 2022-06-14 09:06:28.420465
# Unit test for function debug
def test_debug():
    import mock
    import sys
    import thefuck
    from contextlib import contextmanager

    def get_settings(key, default=None):
        return True

    def reset_settings(*_):
        pass

    @contextmanager
    def mocked_no_debug():
        with mock.patch('thefuck.settings.no_debug', True),\
                mock.patch('thefuck.settings.get_settings',
                           side_effect=get_settings),\
                mock.patch.object(thefuck.settings.Singleton, 'reset',
                                  side_effect=reset_settings):
            yield

    with mock.patch('sys.stderr') as se:
        debug("test_debug")
        assert se.write.call_count == 1
        se.write.assert_called_with("test_debug\n")


# Generated at 2022-06-14 09:06:29.555472
# Unit test for function confirm_text
def test_confirm_text():
    show_corrected_command('git commit -m "My commit"')

# Generated at 2022-06-14 09:06:30.451566
# Unit test for function debug_time
def test_debug_time():
    with debug_time(u'my-msg'):
        pass

# Generated at 2022-06-14 09:06:38.453335
# Unit test for function debug_time
def test_debug_time():
    from datetime import datetime, timedelta
    from contextlib import contextmanager
    @contextmanager
    def debug_time(msg):
        started = datetime.now()
        try:
            yield
        finally:
            debug(u'{} took: {}'.format(msg, datetime.now() - started))
    with debug_time('test_debug_time'):
        l=0
        for i in range(10):
            l=l+i
    assert l==45

# Generated at 2022-06-14 09:06:43.220688
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from thefuck.types import Command
    assert show_corrected_command(Command('ls', 'ls')) == None
    assert show_corrected_command(Command('ls', 'ls', side_effect=True)) == None


# Generated at 2022-06-14 09:06:52.053213
# Unit test for function color
def test_color():
    assert color('test') == ''
    assert color('test') == ''
    settings.no_colors = False
    assert color('test') == 'test'

# Generated at 2022-06-14 09:07:04.872697
# Unit test for function confirm_text
def test_confirm_text():
    from thefuck.conf import Config
    from thefuck.rules.command import Command
    from thefuck.shells import Bash
    config = Config()
    config.env = {'LANG': 'en_US'}
    config.no_colors = False
    cmd = Command(script='cd ..', side_effect=False)
    assert confirm_text(cmd) == '{prefix}cd .. [enter/↑/↓/ctrl+c]'.format(
                                   prefix=const.USER_COMMAND_MARK)
    config.no_colors = True
    assert confirm_text(cmd) == '{prefix}cd .. [enter/↑/↓/ctrl+c]'.format(
                                   prefix=const.USER_COMMAND_MARK)

# Generated at 2022-06-14 09:07:06.955826
# Unit test for function debug_time
def test_debug_time():
    import time
    with debug_time('test'):
        time.sleep(0.5)

# Generated at 2022-06-14 09:07:10.735684
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    print('test_how_to_configure_alias')
    how_to_configure_alias(None)


# Generated at 2022-06-14 09:07:18.349923
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .shells import Shell
    from .command import Command
    from .corrected_command import CorrectedCommand

    correct_command_list = [
        "git commit",
        "git commit -am 'add changes'",
        "git commit -am 'add changes' --allow-empty"]

    for command in correct_command_list:
        corrected_command = CorrectedCommand(Shell('', ''), Command(command), '')
        show_corrected_command(corrected_command)

# Generated at 2022-06-14 09:07:29.593527
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    import StringIO
    from .config import ConfigurationDetails

    configuration_details = ConfigurationDetails(user_dir=None,
                                                 can_configure_automatically=True,
                                                 reload='source ~/.bashrc',
                                                 path='.bashrc',
                                                 content='alias fuck=\'fuck\'')
    sys.stdout = output = StringIO.StringIO()
    how_to_configure_alias(configuration_details)

# Generated at 2022-06-14 09:07:30.886695
# Unit test for function debug_time
def test_debug_time():
    with debug_time('Testing'):
        pass

# Generated at 2022-06-14 09:07:34.802937
# Unit test for function show_corrected_command
def test_show_corrected_command():
    class Command:
        def __init__(self, script, side_effect=False):
            self.script = script
            self.side_effect = side_effect

    show_corrected_command(Command(u'git push origin master'))
    show_corrected_command(Command(u'git push origin master', True))
    show_corrected_command(Command(u'echo "Hello world"'))

# Generated at 2022-06-14 09:07:35.460582
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:07:39.921794
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from tempfile import mkstemp
    import os

    corrected_command = "ls -a"
    fd, fname = mkstemp()
    try:
        with open(fname, 'w') as f:
            show_corrected_command(corrected_command)
    finally:
        os.close(fd)
        os.remove(fname)

# Generated at 2022-06-14 09:07:58.927190
# Unit test for function debug
def test_debug():
    from mock import patch, Mock
    from textwrap import dedent
    from .main import _prepare_debug

    _, _, exc_info = sys.exc_info()
    with patch('sys.stdout') as stdout:
        debug('test')
        assert stdout.write.called
        stdout.write.assert_called_once_with(dedent(u'''
            {blue}{bold}DEBUG:{reset} test\n''').format(
                blue=color(colorama.Fore.BLUE),
                bold=color(colorama.Style.BRIGHT),
                reset=color(colorama.Style.RESET_ALL)))
    with patch('sys.stderr') as stderr:
        warn('test')
        assert stderr.write.called
        stderr.write.assert_called_once

# Generated at 2022-06-14 09:08:01.874514
# Unit test for function debug_time
def test_debug_time():
    from .conf import load_settings
    from .output import debug_time

    settings = load_settings(False)
    with debug_time('Name'):
        pass

# Generated at 2022-06-14 09:08:08.644162
# Unit test for function confirm_text
def test_confirm_text():
    from mock import patch
    from time import time
    confirm_text(corrected_command='corrected_command')
    with patch('time.time') as time_mock:
        time_mock.return_value = time() + 1
        confirm_text(corrected_command='corrected_command')

if __name__ == '__main__':
    test_confirm_text()

# Generated at 2022-06-14 09:08:19.207827
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import thefuck.shells.bash
    test = thefuck.shells.bash.Bash()
    test.is_alias_set = True
    test.script = 'ls -l'
    test.side_effect = ('alias fuck="eval $(thefuck $(fc -ln -1)); fc -R"'
                        ' && fuck')
    corrected_command = thefuck.shells.bash.Command(test.script, test)
    import io
    output = io.StringIO()
    show_corrected_command(corrected_command)
    out = output.getvalue()

# Generated at 2022-06-14 09:08:20.179488
# Unit test for function confirm_text
def test_confirm_text():
    show_corrected_command('git diff')
    confirm_text('git diff')

# Generated at 2022-06-14 09:08:21.217151
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)

# Generated at 2022-06-14 09:08:27.838706
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import sys
    import StringIO
    stdout = sys.stdout
    sys.stdout = StringIO.StringIO()
    class corrected_command:
        def __init__(self):
            self.script = "nano"
            self.side_effect = False
    show_corrected_command(corrected_command())
    assert sys.stdout.getvalue() == '> nano\n'



# Generated at 2022-06-14 09:08:29.338339
# Unit test for function confirm_text
def test_confirm_text():
    test_string = 'print("Hello World")'
    confirm_text(test_string)

# Generated at 2022-06-14 09:08:30.450915
# Unit test for function debug_time
def test_debug_time():
    with debug_time('Test'):
        assert True

# Generated at 2022-06-14 09:08:37.081381
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import io
    import sys
    output = io.StringIO()
    sys.stderr = output
    corrected_command = 'git plu'
    show_corrected_command(corrected_command)
    expected_output = 'git plu\n'
    assert output.getvalue() == expected_output
    sys.stderr = sys.__stderr__



# Generated at 2022-06-14 09:08:52.230924
# Unit test for function debug_time
def test_debug_time():
    from contextlib import contextmanager

    @contextmanager
    def debug_time(msg):
        started = datetime.now()
        try:
            yield
        finally:
            sys.stderr.write(u'{} took: {}'.format(msg, datetime.now() - started))

    with debug_time('test'):
        import time
        time.sleep(1)

# Generated at 2022-06-14 09:08:53.837733
# Unit test for function show_corrected_command
def test_show_corrected_command():
    assert show_corrected_command('Fuck you') == 'Fuck you'


# Generated at 2022-06-14 09:09:06.666212
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    cases = [
        '~/.bashrc',
        '~/.bash_profile',
        '~/.zsh',
        '~/.config/fish/config.fish',
        '~/.config/fish/config.fish\n',
        '',
        '\n',
        None
    ]

    for path in cases:
        for reload in cases:
            for can_configure_automatically in (True, False):
                class ConfigurationDetails:
                    @property
                    def path(self):
                        return path

                    @property
                    def reload(self):
                        return reload

                    @property
                    def can_configure_automatically(self):
                        return can_configure_automatically

                    def _asdict(self):
                        return {'path': path, 'reload': reload}

                how_to_

# Generated at 2022-06-14 09:09:13.233461
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .command import Command

    assert (show_corrected_command(Command('git ci', 'git commit')) ==
            const.USER_COMMAND_MARK+'git ci'+'\n')
    assert (show_corrected_command(Command('git ci', 'git commit', True)) ==
            const.USER_COMMAND_MARK+'git ci'+' (+side effect)'+'\n')

# Generated at 2022-06-14 09:09:17.800772
# Unit test for function confirm_text
def test_confirm_text():
    # generate fake corrected_command
    corrected_command = type('Command', (), {})
    corrected_command.script = 'git push'
    corrected_command.side_effect = True
    confirm_text(corrected_command)

# Generated at 2022-06-14 09:09:25.176751
# Unit test for function debug_time
def test_debug_time():
    from mock import patch
    from datetime import timedelta
    with patch('sys.stderr') as sys_stderr:
        with debug_time('test'):
            pass
        sys_stderr.write.assert_called_once_with(
            u'test took: {}\n'.format(timedelta()))



# Generated at 2022-06-14 09:09:27.433299
# Unit test for function debug_time
def test_debug_time():
    import time
    with debug_time(u'test_debug_time'):
        time.sleep(0.001)

# Generated at 2022-06-14 09:09:40.018718
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import mock
    import sys
    sample = sys.modules[__name__]
    sample.sys = mock.Mock()
    sample.const = mock.Mock()
    command = mock.Mock()
    command.script = "ls"
    command.side_effect = True
    sample.show_corrected_command(command)
    sample.sys.stderr.write.assert_called_once_with(u'f>ls (+side effect)\n')
    sample.sys.stderr.write.reset_mock()
    command.side_effect = False
    sample.show_corrected_command(command)
    sample.sys.stderr.write.assert_called_once_with(u'f>ls \n')

# Generated at 2022-06-14 09:09:42.534687
# Unit test for function color
def test_color():
    assert color('RED') == 'RED'
    settings.no_colors = True
    assert color('RED') == ''



# Generated at 2022-06-14 09:09:44.923151
# Unit test for function debug
def test_debug():
    from . import debug
    debug('a debug message')
    try:
        1/0
    except:
        debug(1/0)



# Generated at 2022-06-14 09:10:07.859423
# Unit test for function debug_time
def test_debug_time():
    import time
    import re
    import threading

    with debug_time('Test'):
        time.sleep(0.1)
    output = []
    def output_listener(out, output):
        while True:
            output.append(out.readline())

    thread = threading.Thread(target=output_listener, args=(sys.stderr, output))
    thread.start()
    with debug_time('Test'):
        time.sleep(0.1)
    thread.join()
    assert len(output) == 1
    match = re.search(r'DEBUG:\s*Test\s*took:\s*([\d.]+)\s*sec', output[0])
    assert match
    time_taken = float(match.group(1))
    assert time_taken > 0.1

# Generated at 2022-06-14 09:10:09.770382
# Unit test for function debug
def test_debug():
    with settings.override(debug=False):
        debug('test message')
    with settings.override(debug=True):
        debug('test message')

# Generated at 2022-06-14 09:10:12.461438
# Unit test for function debug
def test_debug():
    from mock import patch
    with patch('sys.stderr') as stderr:
        debug('debug')
        assert stderr.write.called

# Generated at 2022-06-14 09:10:13.215367
# Unit test for function color
def test_color():
    assert color('color') == 'color'



# Generated at 2022-06-14 09:10:18.262208
# Unit test for function confirm_text
def test_confirm_text():
    for script, side_effect in [("test script", True), ("test script", False)]:
        corrected_command = type("test", (object,),
                                 dict(script=script, side_effect=side_effect))
        sys.stderr.write("\033[1K\r")
        confirm_text(corrected_command)

# Generated at 2022-06-14 09:10:19.285926
# Unit test for function debug_time
def test_debug_time():
    # TODO: fix it
    return
    with debug_time(u'Lorem Ipsum'):
        pass

# Generated at 2022-06-14 09:10:22.738360
# Unit test for function color
def test_color():
    assert color('') == ''
    assert color('\x1b[32m') == ''
    settings.no_colors = False
    assert color('\x1b[32m') == '\x1b[32m'

# Generated at 2022-06-14 09:10:26.976006
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import thefuck.conf
    from thefuck.types import Command
    from thefuck.utils import styled

    thefuck.conf.settings.no_colors = True
    assert '$ ' == const.USER_COMMAND_MARK



# Generated at 2022-06-14 09:10:29.519698
# Unit test for function debug_time
def test_debug_time():
    from time import sleep
    for sec in range(4):
        with debug_time(u'Sleeping {} sec'.format(sec)):
            sleep(sec)


# Generated at 2022-06-14 09:10:31.736584
# Unit test for function debug
def test_debug():
    sys.stderr = sys.stdout
    debug(u'test')



# Generated at 2022-06-14 09:10:47.961340
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    import colorama
    colorama.init()
    print("\nTesting how_to_configure_alias")
    print("--------------------------")
    how_to_configure_alias(None)
    print("--------------------------")


# Unit tests for function already_configured

# Generated at 2022-06-14 09:11:00.528654
# Unit test for function confirm_text
def test_confirm_text():
    from ..utils import which
    from ..shells import shell
    from ..main import get_alias

    from pytest import raises

    SHELL_INFO = 'Shell: Command not found\n'

    with raises(SystemExit):
        version('TheFuck version', 'Python version', SHELL_INFO)

    shell('bash')

    with raises(SystemExit):
        version('TheFuck version', 'Python version', SHELL_INFO)

    SHELL_INFO = 'Shell: {0}\n'.format(which('bash'))

    with raises(SystemExit):
        version('The Fuck version', 'Python version', SHELL_INFO)

    get_alias()

    with raises(SystemExit):
        version('The Fuck version', 'Python version', SHELL_INFO)

# Generated at 2022-06-14 09:11:03.917435
# Unit test for function debug
def test_debug():
    try:
        with open('/dev/null') as f:
            with debug_time('test'):
                pass
    except IOError as e:
        debug(str(e))

# Generated at 2022-06-14 09:11:06.980522
# Unit test for function debug_time
def test_debug_time():
    # It's hard to test the duration of an operation.
    # This test is just to make sure it doesn't crash.
    with debug_time('something'):
        pass

# Generated at 2022-06-14 09:11:09.241360
# Unit test for function color
def test_color():
    assert color(colorama.Fore.BLUE + 'blue') == '\x1b[34mblue'



# Generated at 2022-06-14 09:11:12.168171
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    configuration_details = ('hello', 'world')
    how_to_configure_alias(configuration_details)



# Generated at 2022-06-14 09:11:25.268338
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .types import CorrectedCommand
    from . import rules
    rule1 = rules.Rule(
        name='fuck',
        match=lambda c: None,
        get_new_command=lambda c: 'fuck')
    rule2 = rules.Rule(
        name='fuck',
        match=lambda c: True,
        get_new_command=lambda c: 'fuck')
    corrected_command = CorrectedCommand('fuck', '', rule1)
    show_corrected_command(corrected_command)
    corrected_command = CorrectedCommand('fuck', '', rule2)
    show_corrected_command(corrected_command)

# Generated at 2022-06-14 09:11:38.009013
# Unit test for function debug
def test_debug():
    from contextlib import contextmanager
    from StringIO import StringIO
    from . import debug, const

    @contextmanager
    def captured_output():
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err

    with captured_output() as (out, err):
        debug('Some debug msg')
    assert 'DEBUG: Some debug msg\n' == err.getvalue()

    with captured_output() as (out, err):
        debug('Some debug msg')

# Generated at 2022-06-14 09:11:39.091323
# Unit test for function show_corrected_command
def test_show_corrected_command():
    pass


# Generated at 2022-06-14 09:11:46.396973
# Unit test for function confirm_text
def test_confirm_text():
    const.USER_COMMAND_MARK = '> '
    const.USER_COMMAND_MARK = '> '
    class Command(object):
        def __init__(self, script, side_effect=False):
            self.script = script
            self.side_effect = side_effect

    class CommandTestCase(object):

        def __init__(self, name, input_command, output_command):
            self.name = name
            self.input_command = input_command
            self.output_command = output_command


# Generated at 2022-06-14 09:11:58.483151
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)

# Generated at 2022-06-14 09:12:12.673882
# Unit test for function confirm_text
def test_confirm_text():
    from contextlib import contextmanager
    from StringIO import StringIO

    @contextmanager
    def captured_output():
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err

    class CorrectedCommand:
        script = ''
        side_effect = False

    corrected_command = CorrectedCommand()
    with captured_output() as (out, err):
        confirm_text(corrected_command)
    output = out.getvalue().strip()


# Generated at 2022-06-14 09:12:14.651984
# Unit test for function debug_time
def test_debug_time():
    import time
    with debug_time('Test debug_time()'):
        time.sleep(1)

# Generated at 2022-06-14 09:12:17.214940
# Unit test for function color
def test_color():
    assert color(colorama.Back.RED) == ''
    assert color(colorama.Back.RED) == ''



# Generated at 2022-06-14 09:12:26.831387
# Unit test for function debug_time
def test_debug_time():
    chrono, started = [], datetime.now()
    with debug_time('foo'):
        chrono.append(datetime.now() - started)
        chrono.append(datetime.now() - started)
        raise ValueError('foo')
    chrono.append(datetime.now() - started)
    assert chrono[0].microseconds > 0

# Generated at 2022-06-14 09:12:35.992893
# Unit test for function debug
def test_debug():
    with open('/dev/null', 'wb') as devnull:
        stderr = sys.stderr
        settings.debug = False
        debug('123')
        assert stderr.write.called is False

        settings.debug = True
        sys.stderr = devnull
        debug('123')
        assert stderr.write.called is False
        sys.stderr = stderr

        settings.debug = True
        debug('123')
        stderr.write.assert_called_with('\x1b[34m\x1b[1mDEBUG:\x1b[0m 123\n')

# Generated at 2022-06-14 09:12:49.579955
# Unit test for function confirm_text
def test_confirm_text():
    import io
    stdout = io.BytesIO()
    sys.stdout = stdout

    import thefuck.shells.bash as bash
    import thefuck.utils as utils
    corrected_command = utils.CorrectedCommand('ls', True)
    import thefuck.shells.base as base
    confirm_text(corrected_command)
    sys.stdout = sys.__stdout__

# Generated at 2022-06-14 09:12:51.054458
# Unit test for function confirm_text
def test_confirm_text():
    answer= 'ls -lha'
    confirm_text(answer)

# Generated at 2022-06-14 09:12:53.802073
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text(const.Command('git commit', False)) == \
        u'fuckshit git commit [enter/↑/↓/ctrl+c]'

# Generated at 2022-06-14 09:13:06.507594
# Unit test for function debug
def test_debug():
    def test_output(msg):
        assert sys.stderr.write.called is True
        assert sys.stderr.write.call_args_list[0][0][0].startswith('\x1b['
                                                                  '1K\r\x1b[34'
                                                                  ';1mDEBUG'
                                                                  ':\x1b[0m '
                                                                  + str(msg))

    from mock import patch, call

    with patch('sys.stderr') as sys_stderr:
        sys_stderr.write = call
        debug(const.TEST_STR)
        test_output(const.TEST_STR)

    with patch('sys.stderr') as sys_stderr:
        sys_stderr.write = call
        settings

# Generated at 2022-06-14 09:13:19.706881
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text('ls')

# Generated at 2022-06-14 09:13:29.621035
# Unit test for function debug_time
def test_debug_time():
    import os
    from .conf import Config
    from . import utils
    from .rules.python import match, get_new_command
    from .shells import Bash
    from .application import Application
    import time
    time.sleep(0.1)
    start_time = datetime.now()
    app = Application(
        Config(rules=[utils.import_object(
                'thefuck.rules.python.python_re_match')]),
        Bash(),
        False)
    app.run_rule(
        match(u"ping 8.8.8.8", ["ping 8.8.8.8"], "ping 8.8.8.8", "ping 8.8.8.8", None),
        get_new_command)
    # The difference is less than 1 ms since sleep(0.1) and time to execute

# Generated at 2022-06-14 09:13:30.447903
# Unit test for function confirm_text
def test_confirm_text():
    show_corrected_command('echo hello')
    confirm_text('test command')

# Generated at 2022-06-14 09:13:31.097480
# Unit test for function debug_time
def test_debug_time():
    debug_time("")

# Generated at 2022-06-14 09:13:35.902034
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    from .conf import Config
    from .utils import get_closest

    # Get closest timestamp for test
    timestamp = get_closest("timestamp")
    timestamp.return_value = datetime.now()
    timestamp.return_value += timedelta(milliseconds=1)

    with debug_time('test msg') as result:
        pass
    assert result is None, 'debug_time should return None'

# Generated at 2022-06-14 09:13:40.067309
# Unit test for function color
def test_color():
    assert color(u'\033[31m') == u'\033[31m'
    assert settings.no_colors is False
    settings.no_colors = True
    assert color(u'\033[31m') == u''

# Generated at 2022-06-14 09:13:41.962533
# Unit test for function debug_time
def test_debug_time():
    @debug_time("test")
    def foo():
        import time
        time.sleep(1)

    foo()

# Generated at 2022-06-14 09:13:45.661101
# Unit test for function color
def test_color():
    assert '\033[1m' == color(colorama.Style.BRIGHT)
    assert '' == color(colorama.Style.BRIGHT, True)



# Generated at 2022-06-14 09:13:50.767457
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug('debug message')
    settings.debug = False
    debug('debug message')
    settings.debug = True
    with debug_time('debug time message'):
        pass
    settings.debug = False
    with debug_time('debug time message'):
        pass