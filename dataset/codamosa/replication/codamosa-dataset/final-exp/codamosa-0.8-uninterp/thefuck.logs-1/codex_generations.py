

# Generated at 2022-06-14 09:03:55.963163
# Unit test for function color
def test_color():
    assert color('red') == '\033[31m'
    settings.no_colors = True
    assert color('red') == ''
    settings.no_colors = False



# Generated at 2022-06-14 09:03:59.056545
# Unit test for function debug
def test_debug():
    """ Test with 2 usages of debug in the code."""
    with debug_time('Test debug_time'):
        debug('Test debug')

# Generated at 2022-06-14 09:04:10.603313
# Unit test for function debug
def test_debug():
    from StringIO import StringIO
    with settings.override(debug=False):
        output = StringIO()
        old_stderr = sys.stderr
        try:
            sys.stderr = output
            debug('test')
            assert output.getvalue() == ''

        finally:
            sys.stderr = old_stderr

        output = StringIO()
        old_stderr = sys.stderr
        try:
            sys.stderr = output
            with settings.override(debug=True):
                debug('test')
            assert output.getvalue() == '\x1b[34m\x1b[1mDEBUG:\x1b[0m test\n'

        finally:
            sys.stderr = old_stderr

# Generated at 2022-06-14 09:04:16.212900
# Unit test for function color
def test_color():
    assert color(colorama.Fore.RED) == colorama.Fore.RED
    assert color('') == ''
    settings.no_colors = True
    assert color(colorama.Fore.RED) == ''
    assert color('') == ''
    settings.no_colors = False



# Generated at 2022-06-14 09:04:24.526909
# Unit test for function confirm_text
def test_confirm_text():
    from .conf import Config
    config = Config('')
    from . import shell
    sh = shell.get_shell(config)
    from .command import Command
    history = ['ls']
    for i in range(10):
        history.append('git commit')
    corrected_command = Command(history[-1], [], side_effect=True)
    confirm_text(corrected_command)
    corrected_command = Command(history[-1], [], side_effect=False)
    confirm_text(corrected_command)

# Generated at 2022-06-14 09:04:25.213388
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text(const.CorrectedCommand)

# Generated at 2022-06-14 09:04:32.971748
# Unit test for function debug
def test_debug():
    from mock import patch, Mock
    settings.debug = True
    with patch('sys.stderr', Mock()) as stderr:
        debug('Debug message')
        assert stderr.write.called, 'stderr.write() not called'
    settings.debug = False
    with patch('sys.stderr', Mock()) as stderr:
        debug('Debug message')
        assert not stderr.write.called, 'stderr.write() called'

# Generated at 2022-06-14 09:04:38.039540
# Unit test for function debug_time
def test_debug_time():
    import time
    from datetime import timedelta

    debug_time('text')
    time.sleep(1)
    with debug_time('text') as t:
        time.sleep(0.5)
    assert t == timedelta(seconds=0.5)



# Generated at 2022-06-14 09:04:38.804181
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text(object())

# Generated at 2022-06-14 09:04:43.911967
# Unit test for function debug_time
def test_debug_time():
    import mock
    import thefuck.main
    with mock.patch('thefuck.main.debug') as mock_debug:
        with thefuck.main.debug_time('Foo'):
            pass
    mock_debug.assert_called_with(u'Foo took: 0:00:00')

# Generated at 2022-06-14 09:04:48.161496
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias()


# Generated at 2022-06-14 09:04:55.554040
# Unit test for function confirm_text
def test_confirm_text():
    from StringIO import StringIO
    stdout, sys.stderr = sys.stderr, StringIO()
    confirm_text(CorrectedCommand('echo', '', side_effect=True))
    assert sys.stderr.getvalue().endswith(' echo (+side effect) '
                                          '[enter/↑/↓/ctrl+c]')
    sys.stderr = stdout


# Generated at 2022-06-14 09:04:58.143557
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = 'command'
    confirm_text(corrected_command)
    print(corrected_command)

# Generated at 2022-06-14 09:05:00.663493
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass


# Generated at 2022-06-14 09:05:17.246928
# Unit test for function confirm_text
def test_confirm_text():
    import sys
    import mock
    from .terminal import confirm_text
    from .conf import Settings
    from . import const

    with mock.patch.object(sys, 'stderr') as stderr:
        settings = Settings(no_colors=True)
        with mock.patch.object(settings, 'no_colors', True):
            confirm_text(corrected_command=mock.Mock())

# Generated at 2022-06-14 09:05:22.732225
# Unit test for function debug
def test_debug():
    from StringIO import StringIO
    out = sys.stderr
    sys.stderr = StringIO()
    debug('foo'.format(33))
    sys.stderr.seek(0)
    try:
        assert sys.stderr.read() == '\x1b[34m\x1b[1mDEBUG:\x1b[0m foo\n'
    finally:
        sys.stderr = out

# Generated at 2022-06-14 09:05:30.124171
# Unit test for function debug
def test_debug():
    import io
    import sys

    stderr = sys.stderr
    try:
        sys.stderr = io.StringIO()
        debug(u'foo')
        captured_output = sys.stderr.getvalue()
        assert captured_output == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m foo\n'
    finally:
        sys.stderr = stderr

# Generated at 2022-06-14 09:05:42.639619
# Unit test for function confirm_text
def test_confirm_text():
    from .conf import Settings
    from . import types
    from .types import CorrectedCommand

    settings.no_colors = True
    settings.use_colors = False

    assert confirm_text(CorrectedCommand('sudo ls', 'ls')) == \
        u'$ sudo ls [enter/↑/↓/ctrl+c]'

    settings.no_colors = False
    settings.use_colors = True

    assert confirm_text(CorrectedCommand('sudo ls', 'ls')) == \
        u'$ sudo ls [enter/↑/↓/ctrl+c]'

    assert confirm_text(CorrectedCommand('sudo ls', 'ls', side_effect=True)) == \
        u'$ sudo ls (+side effect) [enter/↑/↓/ctrl+c]'

    settings.require_confirmation = False
   

# Generated at 2022-06-14 09:05:44.232109
# Unit test for function color
def test_color():
    assert color('color') == 'color'
    assert color('') == ''

# Generated at 2022-06-14 09:05:48.646708
# Unit test for function color
def test_color():
    assert color(u'foo') == u'foo'
    settings.no_colors = True
    assert color(u'foo') == u''
    settings.no_colors = False



# Generated at 2022-06-14 09:06:03.337943
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from contextlib import contextmanager
    from StringIO import StringIO
    import sys
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
        how_to_configure_alias(None)
    output = out.getvalue()

# Generated at 2022-06-14 09:06:11.327555
# Unit test for function debug
def test_debug():
    import StringIO
    fake_file = StringIO.StringIO()
    thefuck.log.settings.debug = True
    thefuck.log.debug(u'Debug message', _file=fake_file)
    fake_file.seek(0)
    assert (fake_file.readline() == u'\x1b[94m\x1b[1mDEBUG:\x1b[0m Debug message\n')
    fake_file.close()



# Generated at 2022-06-14 09:06:12.138951
# Unit test for function debug
def test_debug():
    debug('test')

# Generated at 2022-06-14 09:06:13.624773
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        assert True

# Generated at 2022-06-14 09:06:26.852206
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .utils import ConfigurationDetails
    from .shells import Shell
    from .const import THOSE_HAS_NO_AUTO_INSTALLATION_SUPPORT

    configuration_details = ConfigurationDetails('Powershell',
                                                 '.bash_profile',
                                                 'source .bash_profile')

    how_to_configure_alias(configuration_details)

    # Test if auto installation is supported by current shell
    configuration_details = ConfigurationDetails(Shell().name,
                                                 '',
                                                 '')
    how_to_configure_alias(configuration_details)

    # Test if auto installation is not supported by current shell
    configuration_details = ConfigurationDetails(
        Shell().name,
        '',
        '')
    how_to_configure_alias(configuration_details)

    # Test if how_

# Generated at 2022-06-14 09:06:34.563968
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    from cStringIO import StringIO
    with debug_time('foo'):
        sys.stderr = StringIO()
        bar() # it's a part of debug_time, so we need to call it

    output = sys.stderr.getvalue().strip()
    assert output.startswith('\x1b[34m\x1b[1mDEBUG:\x1b[0m foo took: ')
    delta = timedelta(*map(int, output[len('\x1b[34m\x1b[1mDEBUG:\x1b[0m foo took: '):-1].split(':')))
    assert delta.seconds >= 1 and delta.seconds <= 2

# Generated at 2022-06-14 09:06:37.444416
# Unit test for function debug_time
def test_debug_time():
    from . import utils
    with utils.debug_time('printing'):
        import time
        time.sleep(1)

# Generated at 2022-06-14 09:06:40.970208
# Unit test for function color
def test_color():
    assert color(colorama.Fore.BLACK + 'black') == '\x1b[30mblack\x1b[39m'
    assert color('') == ''

# Generated at 2022-06-14 09:06:41.775103
# Unit test for function debug
def test_debug():
    debug('debug')

# Generated at 2022-06-14 09:06:44.519792
# Unit test for function debug_time
def test_debug_time():
    with debug_time("test_debug_time"):
        time.sleep(0.01)

# Generated at 2022-06-14 09:06:53.206378
# Unit test for function debug
def test_debug():
    import io

    with io.StringIO() as debug_out:
        with settings.override(debug=True):
            debug(u'Message')
        assert debug_out.getvalue() == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m Message\n'

# Generated at 2022-06-14 09:07:00.261399
# Unit test for function debug
def test_debug():
    """Test that debug function makes expected output to stderr"""
    import StringIO

    # disable debug output to stderr
    settings.log_to_stderr = False

# Generated at 2022-06-14 09:07:06.648959
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    configuration_details = namedtuple('ConfigurationDetails', 'config_file,content,reload')
    how_to_configure_alias(configuration_details('.bashrc', 'alias fuck=\'eval $(thefuck $(fc -ln -1))\'', 'source ~/.bashrc'))



# Generated at 2022-06-14 09:07:11.324982
# Unit test for function color
def test_color():
    assert color(colorama.Fore.RESET) == ''
    assert color(colorama.Fore.RED) == colorama.Fore.RED
    assert color(colorama.Style.BRIGHT) == colorama.Style.BRIGHT

# Generated at 2022-06-14 09:07:13.505388
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from thefuck.commands import CorrectedCommand
    test_command = CorrectedCommand('ls -a', '')
    answer = 'ls -a'
    show_corrected_command(test_command)
    assert sys.stdout.getvalue() == answer



# Generated at 2022-06-14 09:07:17.396275
# Unit test for function show_corrected_command
def test_show_corrected_command():
    class CorrectedCommand(object):
        def __init__(self, script, side_effect):
            self.script = script
            self.side_effect = side_effect

    show_corrected_command(CorrectedCommand('ls', True))
    show_corrected_command(CorrectedCommand('ls', False))

# Generated at 2022-06-14 09:07:18.900788
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text('test') == '> test [enter/↑/↓/ctrl+c]'

# Generated at 2022-06-14 09:07:26.463136
# Unit test for function debug_time
def test_debug_time():
    print('Test debug_time')
    test_msg = 'Hello'
    with debug_time(test_msg) as nothing:
        pass # Тест не должен падать по семантике сборщика мусора
    if test_msg not in sys.stderr.getvalue():
        print('UNIT TEST FAILED')

# Generated at 2022-06-14 09:07:29.226477
# Unit test for function debug
def test_debug():
    debug_info = 'This is a test for debug message'
    debug(debug_info)

    assert debug_info in sys.stderr.getvalue()



# Generated at 2022-06-14 09:07:31.876615
# Unit test for function debug
def test_debug():
    from mock import patch

    with patch('thefuck.utils.sys.stderr') as stderr:
        debug('msg')
    stderr.write.assert_called_once_with('DEBUG: msg\n')

# Generated at 2022-06-14 09:07:36.610674
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from thefuck import shell
    corrected_command = shell.And('', 'echo "foo"', '')
    show_corrected_command(corrected_command)
    assert sys.stderr.readline() == "> echo \"foo\"\n"

# Generated at 2022-06-14 09:07:48.690234
# Unit test for function confirm_text
def test_confirm_text():
    from . import rules

    class MockCommand(object):
        def __init__(self, script, side_effect=False):
            self.script = script
            self.side_effect = side_effect

    class MockRule(object):
        def __init__(self, name):
            self.name = name

        def enabled_by_default(self):
            return True

        def get_new_command(self, *args, **kwargs):
            return MockCommand(self.name)

    rule_names = ['test1', 'test2', 'test3']
    rules._available_rules = set(MockRule(name) for name in rule_names)

    confirm_text(MockCommand(script='test command', side_effect=True))

# Generated at 2022-06-14 09:07:50.186554
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text(make_MockCommand('cd')) == 'cd'

# Generated at 2022-06-14 09:07:52.117782
# Unit test for function debug_time
def test_debug_time():
    def inner():
        pass
    debug_time('test')(inner)()
    assert True

# Generated at 2022-06-14 09:07:55.437295
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text(('fuck git remote add origin\n',)) == 'fuck git remote add origin\n [enter/↑/↓/ctrl+c]'

# Generated at 2022-06-14 09:07:58.591136
# Unit test for function debug
def test_debug():
    from collections import namedtuple
    from mock import patch

    with patch('sys.stderr') as stderr:
        debug(u'Test')
        assert stderr.write.called
        assert stderr.write.call_args[0][0] == \
            u'{blue}{bold}DEBUG:{reset} Test\n'.format(
                blue=color(colorama.Fore.BLUE),
                bold=color(colorama.Style.BRIGHT),
                reset=color(colorama.Style.RESET_ALL))

# Generated at 2022-06-14 09:08:02.146589
# Unit test for function show_corrected_command
def test_show_corrected_command():
    # If show_corrected_command run, it will always output a message, so
    # we need to capture the standard output to assert if it is the message
    # we expected

    from cStringIO import StringIO
    import sys

    output = StringIO()
    old_stdout, sys.stdout = sys.stdout, output
    show_corrected_command("git remote add origin https://github.com/nvbn/thefuck.git")
    sys.stdout = old_stdout

    assert output.getvalue() == '$ git remote add origin https://github.com/nvbn/thefuck.git \n'



# Generated at 2022-06-14 09:08:11.134047
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from StringIO import StringIO
    from .utils import captured_stderr

    with captured_stderr(StringIO()) as stderr:
        show_corrected_command(CorrectedCommand(
            "foo", False))
        assert stderr.getvalue() == u'$ foo\n'

    with captured_stderr(StringIO()) as stderr:
        show_corrected_command(CorrectedCommand(
            "bar", True))
        assert stderr.getvalue() == u'$ bar (+side effect)\n'



# Generated at 2022-06-14 09:08:12.242798
# Unit test for function debug
def test_debug():
    debug('test')

# Generated at 2022-06-14 09:08:17.377790
# Unit test for function show_corrected_command
def test_show_corrected_command():
    sys.stderr = open('output.txt', 'w')
    show_corrected_command("ls -alh")
    sys.stderr.close()
    sys.stderr = sys.__stderr__
    f = open("output.txt", "r")
    assert f.readline() == u'[ls -alh]\n'
    f.close()

# Generated at 2022-06-14 09:08:23.084478
# Unit test for function color
def test_color():
    assert color(colorama.Fore.RED) == colorama.Fore.RED
    settings.no_colors = True
    assert color(colorama.Fore.RED) == ''
    settings.no_colors = False

# Generated at 2022-06-14 09:08:26.951199
# Unit test for function debug_time
def test_debug_time():
    import time
    with debug_time('test'):
        time.sleep(0.1)
    with debug_time('test'):
        time.sleep(0.2)

# Generated at 2022-06-14 09:08:30.274286
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .corrected_command import CorrectedCommand
    show_corrected_command(CorrectedCommand('git commit -m message', True))
    show_corrected_command(CorrectedCommand('git commit -m message', False))



# Generated at 2022-06-14 09:08:32.420862
# Unit test for function debug_time
def test_debug_time():
    import time
    with debug_time(u'test'):
        time.sleep(0.5)

# Generated at 2022-06-14 09:08:33.604504
# Unit test for function debug_time
def test_debug_time():
    with debug_time('foo'):
        pass

# Generated at 2022-06-14 09:08:34.804819
# Unit test for function debug
def test_debug():
    assert debug('msg') is None

# Generated at 2022-06-14 09:08:35.857296
# Unit test for function debug
def test_debug():
    assert debug("test message") == None



# Generated at 2022-06-14 09:08:42.366186
# Unit test for function debug_time
def test_debug_time():
    import time
    import mock
    with mock.patch('sys.stderr.write') as sys_stderr_write:
        with debug_time('It') as r:
            time.sleep(1)
        assert r is None
    sys_stderr_write.assert_called_once_with(
        u'\x1b[34m\x1b[1mDEBUG:\x1b[0m It took: 0:00:01.001001\n')

# Generated at 2022-06-14 09:08:44.989328
# Unit test for function confirm_text
def test_confirm_text():
    from .shells import Namespace
    cmd = Namespace(script='ls', side_effect=True)
    confirm_text(cmd)

# Generated at 2022-06-14 09:08:47.274878
# Unit test for function color
def test_color():
    assert color(u'//') != '//'
    assert color(u'.*') == '.*'
    assert color(u'***') == '***'

# Generated at 2022-06-14 09:08:51.108931
# Unit test for function debug
def test_debug():
    debug('works')



# Generated at 2022-06-14 09:08:54.820887
# Unit test for function show_corrected_command
def test_show_corrected_command():
    assert show_corrected_command(corrected_command = ('thefuck')) == 'thefuck'
    assert show_corrected_command(corrected_command = ('thefuck')) != 'thefuk'
    assert show_corrected_command(corrected_command = ('thefuck')) != 'thefuc'



# Generated at 2022-06-14 09:08:59.293149
# Unit test for function debug_time
def test_debug_time():
    from .tests.utils import mock_popen, KeyValue

    settings.debug = True

    with mock_popen('sleep 1'):
        with debug_time('Test debug_time'):
            pass

# Generated at 2022-06-14 09:09:01.002996
# Unit test for function debug
def test_debug():
    from test.utils import assert_equal

    assert_equal(debug, u'debug')

# Generated at 2022-06-14 09:09:03.822385
# Unit test for function confirm_text
def test_confirm_text():
    show_corrected_command(['!echo "test"', False])


# Generated at 2022-06-14 09:09:05.126913
# Unit test for function color
def test_color():
    assert color(u'foo') == u''



# Generated at 2022-06-14 09:09:07.121957
# Unit test for function color
def test_color():
    assert color(u'foo') == colorama.Style.RESET_ALL + u'foo'



# Generated at 2022-06-14 09:09:08.406219
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:09:16.940160
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .utils import get_closest, get_all_executables
    from .application import Application
    from .shells import Shell
    from . import conf
    import sys
    import colorama
    from thefuck.shells import aliased, non_aliased

    conf.settings = conf.Config()
    conf.settings.no_colors = True
    conf.settings._clear_all = True

    colorama.init(strip=False)
    application = Application()

    shell = Shell()
    shell.path = '/usr/local/bin/bash'
    shell.version = '3.2.57(1)-release'

    closest = get_closest('bash', get_all_executables(shell))

    application.reload_alias = closest


# Generated at 2022-06-14 09:09:18.880573
# Unit test for function confirm_text
def test_confirm_text():
    from thefuck.utils import confirm_text
    confirm_text('command')

# Generated at 2022-06-14 09:09:28.399453
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = 'ls'
    confirm_text(corrected_command)
    corrected_command = 'ls + side effect'
    confirm_text(corrected_command)
    corrected_command = 'ls + side effect +more side effect'
    confirm_text(corrected_command)


if __name__ == '__main__':
    test_confirm_text()

# Generated at 2022-06-14 09:09:41.865565
# Unit test for function show_corrected_command
def test_show_corrected_command():
    output = sys.stderr.write('\033[1K\r{}'.format(const.USER_COMMAND_MARK))
    output = sys.stderr.write('\033[1K\r{}'.format(const.USER_COMMAND_MARK))
    output = sys.stderr.write('\033[1K\r{}'.format(const.USER_COMMAND_MARK))
    output = sys.stderr.write('\033[1K\r{}'.format(const.USER_COMMAND_MARK))
    output = sys.stderr.write('\033[1K\r{}'.format(const.USER_COMMAND_MARK))

# Generated at 2022-06-14 09:09:46.013117
# Unit test for function debug
def test_debug():
    settings.debug = True
    import io
    import sys
    stdout = io.BytesIO()
    stderr = io.BytesIO()
    sys.stdout = stdout
    sys.stderr = stderr
    try:
        debug('message')
        assert b'DEBUG: message\n' == stderr.getvalue()
        assert b'' == stdout.getvalue()
    finally:
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__


# Generated at 2022-06-14 09:09:48.183709
# Unit test for function debug
def test_debug():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:10:00.217047
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from . import shell
    import tempfile
    import subprocess
    import os

    configuration_details = shell.get_shell_configuration_details(
        shell.from_shell_name(shell.to_shell_name('bash')))

    with tempfile.NamedTemporaryFile() as f:
        how_to_configure_alias(configuration_details)
        f.flush()
        output = subprocess.check_output(['bash', '-c', 'cat {}'.format(f.name)])
        output = output.decode("utf-8")
        assert 'Seems like fuck alias isn\'t configured!' in output
        assert 'Or run fuck a second time to configure it automatically.' in output

        configuration_details.can_configure_automatically = False

# Generated at 2022-06-14 09:10:01.008848
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    pass

# Generated at 2022-06-14 09:10:04.994535
# Unit test for function debug
def test_debug():
    import StringIO
    output = StringIO.StringIO()
    sys.stderr = output
    debug('msg')
    sys.stderr = sys.__stderr__
    assert output.getvalue() == u'DEBUG: msg\n'

# Generated at 2022-06-14 09:10:09.417513
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    current_time = datetime.now()
    how_to_configure_alias(current_time)
    assert True
    # assert datetime.now() - current_time > 1


if __name__ == '__main__':
    test_how_to_configure_alias()

# Generated at 2022-06-14 09:10:18.167491
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import mock
    import getpass

    username = getpass.getuser()
    corrected_command = mock.Mock()
    corrected_command.script = 'git push --force'
    corrected_command.side_effect = 'cd ..'
    fake_stdout = mock.Mock()

    with mock.patch('sys.stdout', fake_stdout):
        show_corrected_command(corrected_command)

    expected = '{}[{}] {}git push --force (+side effect)\n'.format(
        const.USER_COMMAND_MARK, username, color(colorama.Style.BRIGHT))
    assert fake_stdout.write.called
    assert fake_stdout.write.call_args[0][0] == expected



# Generated at 2022-06-14 09:10:31.439690
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .shells import shell_info
    from .conf import ConfigurationDetails
    conf = ConfigurationDetails(
        '',
        '/tmp/fuck',
        '. /tmp/fuck',
        can_configure_automatically=True)
    how_to_configure_alias(conf)
    for outputline in sys.stdout.getvalue().split('\n'):
        assert outputline.startswith('Seems like ')
    conf = ConfigurationDetails(
        '',
        '/tmp/fuck',
        '. /tmp/fuck',
        can_configure_automatically=False)
    how_to_configure_alias(conf)
    for outputline in sys.stdout.getvalue().split('\n'):
        assert outputline.startswith('Seems like ')
    how_to_configure

# Generated at 2022-06-14 09:10:40.687335
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from collections import namedtuple
    Command = namedtuple('Command', 'script side_effect')
    show_corrected_command(Command('script', True))
    show_corrected_command(Command('script', False))



# Generated at 2022-06-14 09:10:44.210001
# Unit test for function color
def test_color():
    assert color(colorama.Fore.WHITE) == colorama.Fore.WHITE
    settings.no_colors = True
    assert color(colorama.Fore.WHITE) == ''

# Generated at 2022-06-14 09:10:51.057792
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = type(u'corrected_command', (object,),
                             {u'script': u'some scripts',
                              u'side_effect': True})
    print(u'#' * 30)
    print(u'Testing function show_corrected_command')
    print(u'#' * 30)
    show_corrected_command(corrected_command)


# Generated at 2022-06-14 09:10:53.499236
# Unit test for function show_corrected_command
def test_show_corrected_command():
    assert show_corrected_command(u'git push origin feature') == None



# Generated at 2022-06-14 09:10:54.776874
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias('')

# Generated at 2022-06-14 09:10:56.762680
# Unit test for function color
def test_color():
    assert color('red') == colorama.Fore.RED
    assert color('red') == ''

# Generated at 2022-06-14 09:11:07.195635
# Unit test for function confirm_text
def test_confirm_text():
    from .application import Application
    from .shells.bash import Bash
    from .shells.fish import Fish
    from .shells.zsh import Zsh
    from .utils import get_closest

    app = Application()
    app.shell = Bash()

    confirm_text(app._get_corrected_command(
        u'/bin/ls non_exist_file', {'ls': get_closest(app.collect_rules, 'ls')[-1]}))

    app.shell = Fish()

    confirm_text(app._get_corrected_command(
        u'ls non_exist_file', {'ls': get_closest(app.collect_rules, 'ls')[-1]}))

    app.shell = Zsh()


# Generated at 2022-06-14 09:11:11.932219
# Unit test for function debug
def test_debug():
    import mock
    from tests.utils import capture_stderr
    with capture_stderr() as captured:
        debug(u'foo')
        assert not captured.getvalue()
        settings.debug = True
        debug(u'foo')
    assert u'DEBUG: foo\n' == captured.getvalue()

# Generated at 2022-06-14 09:11:22.395636
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from thefuck.types import Command

    settings.no_colors = False
    show_corrected_command(Command('ls', 'ls'))
    show_corrected_command(Command('ls', 'ls', side_effect=True))

    settings.no_colors = True
    show_corrected_command(Command('ls', 'ls'))
    show_corrected_command(Command('ls', 'ls', side_effect=True))

# Generated at 2022-06-14 09:11:24.027669
# Unit test for function debug
def test_debug():
    def test_func(obj):
        debug('test_debug')
    settings.debug = True
    test_func(None)
    settings.debug = False
    test_func(None)

# Generated at 2022-06-14 09:11:29.702945
# Unit test for function debug_time
def test_debug_time():
    from pytest import raises
    from thefuck.utils import hidetraceback
    with raises(TypeError):
        with debug_time(2):
            pass

    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:11:31.322578
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)


# Generated at 2022-06-14 09:11:32.552080
# Unit test for function debug
def test_debug():
    assert debug('test') is None


# Generated at 2022-06-14 09:11:44.009597
# Unit test for function confirm_text
def test_confirm_text():
    #Set function confirm_text to be mockable
    global confirm_text
    original_confirm_text = confirm_text
    confirm_text = lambda x: None


# Generated at 2022-06-14 09:11:46.021979
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text('ls') == 'ls'


# Generated at 2022-06-14 09:11:48.445691
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text(12) == u'12 (+side effect) [enter/↑/↓/ctrl+c]'

# Generated at 2022-06-14 09:11:58.370729
# Unit test for function confirm_text
def test_confirm_text():
    def confirm_text_result(corrected_command):
        return (
            u'fuck {} [enter/↑/↓/ctrl+c]'.format(corrected_command.script))

    assert confirm_text_result(
        const.CorrectedCommand(u'ls', u'ls -l', False)) == confirm_text(
            const.CorrectedCommand(u'ls', u'ls -l', False))
    assert confirm_text_result(
        const.CorrectedCommand(u'ls', u'ls -l', True)) == confirm_text(
            const.CorrectedCommand(u'ls', u'ls -l', True))

# Generated at 2022-06-14 09:12:01.186620
# Unit test for function confirm_text
def test_confirm_text():
    class CorrectedCommand(object):
        script = u'ls'
        side_effect = False

    confirm_text(CorrectedCommand())

# Generated at 2022-06-14 09:12:05.430065
# Unit test for function show_corrected_command
def test_show_corrected_command():
    assert const.USER_COMMAND_MARK in show_corrected_command('\033[1K\r', './test_command.py', 0)

# Generated at 2022-06-14 09:12:07.431099
# Unit test for function debug_time
def test_debug_time():
    with debug_time('a'):
        pass

# Generated at 2022-06-14 09:12:22.650102
# Unit test for function debug_time
def test_debug_time():
    from .tests.utils import Mock, patch
    import datetime

    # The decorator @contextmanager is a generator. It returns a generator.
    # The generator it returns yields, then when the yield is returned,
    # it runs the block - the indented section after the yield keyword.
    # when the block completes, execution continues in the @contextmanager
    # decorator, which runs the block following the yield keyword.
    # The with statement handles the creation and destruction of context
    # managers.
    # The with statement calls the __enter__ method on the context manager
    # and assigns whatever __enter__ returns to the variable given by as.
    # It then executes the body of the with statement, finally
    # calling the __exit__ method on the context manager.
    # Here the __enter__ method is a generator. This is the reason why
    # while True is

# Generated at 2022-06-14 09:12:29.614921
# Unit test for function debug_time
def test_debug_time():
    def dummy_time(msg, start, end):
        assert msg == 'test'
        assert end > start

    with patch('datetime.datetime') as mock_datetime:
        mock_datetime.utcnow.side_effect = [42, 666]
        with patch('thefuck.shells.generic.debug') as mock_debug:
            mock_debug.side_effect = dummy_time
            with debug_time('test'):
                pass

# Generated at 2022-06-14 09:12:32.545554
# Unit test for function debug
def test_debug():
    from mock import patch

    with patch('sys.stderr') as stderr:
        debug('Foo')
        stderr.write.assert_called_once()

# Generated at 2022-06-14 09:12:39.322080
# Unit test for function confirm_text
def test_confirm_text():
    from StringIO import StringIO
    import sys
    out = StringIO()
    sys.stderr = out
    from thefuck.shells.bash import correct_command
    from thefuck.rules.sudo import match, get_new_command
    c = correct_command('pwd', ['pwd'], None)
    confirm_text(c)
    assert out.getvalue() == 'fuck pwd [enter/↑/↓/ctrl+c]\n'
# end test_confirm_text()

# Generated at 2022-06-14 09:12:43.834929
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = "git c"
    user_command_mark = const.USER_COMMAND_MARK
    assert show_corrected_command(corrected_command) == (user_command_mark + corrected_command)



# Generated at 2022-06-14 09:12:54.649905
# Unit test for function confirm_text

# Generated at 2022-06-14 09:12:56.956598
# Unit test for function color
def test_color():
    assert color('foo') == 'foo'
    settings.no_colors = True
    assert color('foo') == ''

# Generated at 2022-06-14 09:13:01.766355
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from thefuck.utils import NamedResult
    from .const import UserCommand

    show_corrected_command(
        NamedResult(UserCommand(command='git push origin master',
                                script='git push origin master --force',
                                side_effect=False), 'git'))

# Generated at 2022-06-14 09:13:03.477777
# Unit test for function debug_time
def test_debug_time():
    with debug_time('Say hello'):
        time.sleep(0.1)

# Generated at 2022-06-14 09:13:08.792526
# Unit test for function debug
def test_debug():
    from StringIO import StringIO
    buf = StringIO()
    sys.stderr = buf
    debug(u'Hello, world!')
    res = buf.getvalue()
    sys.stderr = sys.__stderr__
    assert res == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m Hello, world!\n'

# Generated at 2022-06-14 09:13:15.521177
# Unit test for function debug
def test_debug():
    from test import mock

    mock_stdout = mock.MagicMock()
    mock_stderr = mock.MagicMock()

    with mock.patch.object(sys, 'stderr', mock_stderr):
        debug('Test message')

    assert mock_stderr.write.call_count == 1
    (args, kwargs) = mock_stderr.write.call_args
    assert 'Test message' in args[0]

# Generated at 2022-06-14 09:13:16.659344
# Unit test for function debug_time
def test_debug_time():
    debug_time('test')

# Generated at 2022-06-14 09:13:24.908509
# Unit test for function show_corrected_command
def test_show_corrected_command():
    assert show_corrected_command(['ls']) == u'$ ls'
    assert show_corrected_command(['git', 'push', 'origin', 'master']) == \
        u'$ git push origin master'

if __name__ == '__main__':
    print(color('foo'))
    show_corrected_command(['ls'])
    show_corrected_command(['git', 'push', 'origin', 'master'])

# Generated at 2022-06-14 09:13:26.349299
# Unit test for function show_corrected_command
def test_show_corrected_command():
    show_corrected_command(CorrectedCommandMock())



# Generated at 2022-06-14 09:13:33.567200
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = u'git bad'
    show_corrected_command(corrected_command)
    sys.stderr.write(u'{prefix}{bold}{script}{reset}{side_effect}\n'.format(
        prefix=const.USER_COMMAND_MARK,
        script=corrected_command.script,
        side_effect=u' (+side effect)' if corrected_command.side_effect else u'',
        bold=color(colorama.Style.BRIGHT),
        reset=color(colorama.Style.RESET_ALL)))

    # Unit test for function confirm_text

# Generated at 2022-06-14 09:13:36.162109
# Unit test for function show_corrected_command
def test_show_corrected_command():
    show_corrected_command(corrected_command)

# Generated at 2022-06-14 09:13:38.403823
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)
    how_to_configure_alias(3)



# Generated at 2022-06-14 09:13:43.390834
# Unit test for function debug_time
def test_debug_time():
    """
    >>> try:
    ...     settings.debug = True
    ...     with debug_time('test'):
    ...         pass
    ... finally:
    ...     settings.debug = False
    """

# Generated at 2022-06-14 09:13:52.522486
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import tempfile
    from .command import Command

    fd, path = tempfile.mkstemp()
    stdout = sys.stdout

    sys.stdout = open(path, 'w')
    cmd = Command('/bin/ls')
    show_corrected_command(cmd)
    sys.stdout.close()

    sys.stdout = stdout
    with open(path, 'r') as fd:
        assert u'{}/bin/ls\n'.format(const.USER_COMMAND_MARK) == fd.read()

    import os
    os.remove(path)