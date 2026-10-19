

# Generated at 2022-06-14 09:03:56.223918
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = type(
        'CorrectedCommand',
        (object,),
        dict(script=u'less',
             side_effect=False))
    confirm_text(corrected_command)

# Generated at 2022-06-14 09:04:04.280290
# Unit test for function confirm_text
def test_confirm_text():
    class Fake(object):
        pass

    corrected_command = Fake()
    corrected_command.script = u'test'
    corrected_command.side_effect = False
    confirm_text(corrected_command)

    corrected_command = Fake()
    corrected_command.script = u'test'
    corrected_command.side_effect = True
    confirm_text(corrected_command)

if __name__ == '__main__':
    test_confirm_text()

# Generated at 2022-06-14 09:04:07.794879
# Unit test for function color
def test_color():
    assert color('red') == '\x1b[31m'
    assert color('reset') == '\x1b[0m'
    assert color('') == ''

# Generated at 2022-06-14 09:04:08.856706
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test1'):
        pass

# Generated at 2022-06-14 09:04:10.298680
# Unit test for function debug_time
def test_debug_time():
    from time import sleep

    with debug_time('t'):
        sleep(1)

# Generated at 2022-06-14 09:04:13.791901
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .main import CorrectedCommand
    show_corrected_command(CorrectedCommand(script='ls', side_effect=False))



# Generated at 2022-06-14 09:04:19.145715
# Unit test for function show_corrected_command
def test_show_corrected_command():
    # pylint: disable=E0602, W0612
    global sys
    import StringIO
    sys = StringIO.StringIO()
    show_corrected_command('git push origin master')
    assert sys.getvalue() == 'git push origin master\n'

# Generated at 2022-06-14 09:04:21.934679
# Unit test for function confirm_text
def test_confirm_text():
    import colorama
    colorama.init(autoreset=True)
    confirm_text(dict(script = 'script', side_effect = True))

# Generated at 2022-06-14 09:04:30.154787
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_command = corrected_

# Generated at 2022-06-14 09:04:34.032641
# Unit test for function debug
def test_debug():
    call_debug()
    assert sys.stderr.getvalue() == '\x1b[34m\x1b[1mDEBUG:\x1b[0m The message'

# Generated at 2022-06-14 09:04:46.721842
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import os

    # Change the user's HOME in order to make sure that no previously saved logs
    # will be found
    old_home = os.environ['HOME']
    os.environ['HOME'] = '/tmp'


# Generated at 2022-06-14 09:04:47.771710
# Unit test for function debug_time
def test_debug_time():
    with debug_time('msg'):
        pass

# Generated at 2022-06-14 09:04:50.811459
# Unit test for function debug_time
def test_debug_time():
    import mock
    mock_func = mock.Mock()

    with debug_time('test'):
        mock_func()

    assert mock_func.called



# Generated at 2022-06-14 09:04:55.661680
# Unit test for function debug_time
def test_debug_time():
    import time
    from . import log

    def sleep(sec):
        time.sleep(sec)
        return u'Success'

    log.settings.debug = True
    with log.debug_time(u'Sleep'):
        result = sleep(0.1)
    assert result == u'Success'

# Generated at 2022-06-14 09:05:03.439108
# Unit test for function confirm_text
def test_confirm_text():
    import re

    # The cleared line should start with `sudo `
    assert re.match(r'(\\033\[1K\\r)?{}sudo +'.format(const.USER_COMMAND_MARK),
                    confirm_text(CorrectedCommand(script='sudo ', side_effect=False)))

    # The cleared line should start with `sudo `
    assert re.match(
        r'(\\033\[1K\\r)?{}sudo +'.format(const.USER_COMMAND_MARK),
        confirm_text(CorrectedCommand(script='sudo ', side_effect=True)))

# Generated at 2022-06-14 09:05:05.891796
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text(corrected_command='thefuck --version')


# Generated at 2022-06-14 09:05:06.951360
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:05:12.420404
# Unit test for function debug
def test_debug():
    from StringIO import StringIO
    with settings(debug=False):
        assert not debug('foo')
        assert sys.stderr.getvalue() == ''
    with settings(debug=True):
        assert debug('foo')
        assert sys.stderr.getvalue().endswith('foo\n')



# Generated at 2022-06-14 09:05:14.185670
# Unit test for function debug
def test_debug():
    with debug_time('foo'):
        pass

# Generated at 2022-06-14 09:05:16.353014
# Unit test for function debug_time
def test_debug_time():
    import time

    with debug_time('A'):
        time.sleep(0.5)

    assert True

# Generated at 2022-06-14 09:05:23.759904
# Unit test for function show_corrected_command
def test_show_corrected_command():
	cmd = u'echo "test show corrected command"'
	corrected_command = unicode(cmd, sys.getfilesystemencoding())
	sys.stderr.write(u'{prefix}{bold}{script}{reset}{side_effect}\n'.format(
		prefix=const.USER_COMMAND_MARK,
		script=corrected_command.script,
		side_effect=u' (+side effect)' if corrected_command.side_effect else u'',
		bold=color(colorama.Style.BRIGHT),
		reset=color(colorama.Style.RESET_ALL)))

# Generated at 2022-06-14 09:05:28.698747
# Unit test for function debug
def test_debug():
    from StringIO import StringIO
    from .conf import settings
    settings.debug = True
    debug('test')
    assert StringIO.getvalue(sys.stderr) == '\x1b[34m\x1b[1mDEBUG:\x1b[0m test\n'

# Generated at 2022-06-14 09:05:33.417964
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = type(
        'FakeCorrectedCommand',
        (object,),
        {
            'script': 'echo "Hello world!'
        })
    confirm_text(corrected_command)



# Generated at 2022-06-14 09:05:43.978886
# Unit test for function debug_time
def test_debug_time():
    import StringIO
    from datetime import timedelta

    class FakeTime(object):
        def __init__(self):
            self.time = datetime.now()

        def __call__(self):
            self.time += timedelta(hours=1)
            return self.time

    with debug_time('message'):
        pass

    old_sys_stderr, sys.stderr = sys.stderr, StringIO.StringIO()

    with debug_time('message'):
        pass

    output = sys.stderr.getvalue()

    assert output.startswith('DEBUG: message took')

    sys.stderr = old_sys_stderr

    with debug_time('message'):
        raise Exception

    output = sys.stderr.getvalue()

    assert output.startswith

# Generated at 2022-06-14 09:05:56.690685
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import io
    import sys
    import re
    import tempfile
    from thefuck.utils import show_corrected_command

    # testing with sidebar effect
    with tempfile.TemporaryFile() as tmp:
        sys.stderr = io.TextIOWrapper(tmp)
        user_command = ('ls -lah')
        side_effect = ('sudo -s')
        corrected_command = user_command + ' && ' + side_effect
        show_corrected_command(corrected_command)
        tmp.seek(0)
        content = tmp.read().decode('UTF-8')
        assert content == '$ ls -lah && sudo -s (+side effect)\n'

    # testing without sidebar effect
    with tempfile.TemporaryFile() as tmp:
        sys.stderr = io.TextIOWrapper

# Generated at 2022-06-14 09:05:57.846558
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass
test_debug_time()

# Generated at 2022-06-14 09:06:00.719903
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)



# Generated at 2022-06-14 09:06:02.213469
# Unit test for function debug
def test_debug():
    debug('test')



# Generated at 2022-06-14 09:06:05.940711
# Unit test for function debug_time
def test_debug_time():
    debug_start = datetime.now()
    with debug_time('test_debug_time'):
        debug_end = datetime.now()
    assert debug_end - debug_start != datetime(1,1,1)

# Generated at 2022-06-14 09:06:12.703997
# Unit test for function show_corrected_command
def test_show_corrected_command():
    class CorrectedCommand(object):
        def __init__(self, script, side_effect=False):
            self.script = script
            self.side_effect = side_effect

    assert show_corrected_command(CorrectedCommand('ls')) == 'ls\n'
    assert show_corrected_command(CorrectedCommand('ls', True)) == \
        'ls (+side effect)\n'



# Generated at 2022-06-14 09:06:17.879849
# Unit test for function debug_time
def test_debug_time():
    from datetime import datetime

    with debug_time('test'):
        assert True



# Generated at 2022-06-14 09:06:28.481171
# Unit test for function debug
def test_debug():
    try:
        import StringIO
        StringIO = StringIO.StringIO
    except ImportError:
        import io
        StringIO = io.StringIO
    out = StringIO()
    err = StringIO()
    settings.debug = True
    try:
        with patch('sys.stdout', out):
            with patch('sys.stderr', err):
                debug('test')
        assert err.getvalue() == '\x1b[34m\x1b[1mDEBUG:\x1b[0m test\n'
    finally:
        settings.debug = False
    assert out.getvalue() == ''



# Generated at 2022-06-14 09:06:31.293937
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = corrected_command = const.CorrectedCommand('ls')
    confirm_text(corrected_command)
    assert True

# Generated at 2022-06-14 09:06:35.954855
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import mock
    from thefuck.types import CorrectedCommand
    with mock.patch('sys.stderr', new_callable=mock.PropertyMock) as stderr:
        show_corrected_command(CorrectedCommand('script', 'side effect'))
        assert stderr.write.call_args[0][0] == '\x1b[33m> script (+side effect)\x1b[0m'

# Generated at 2022-06-14 09:06:43.325953
# Unit test for function debug
def test_debug():
    from io import BytesIO
    stream = BytesIO()
    settings.debug = True
    sys.stderr = stream
    debug(u'TEST_MESSAGE')
    stream.seek(0)
    assert stream.read() == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m TEST_MESSAGE\n'.encode('utf-8')

# Generated at 2022-06-14 09:06:45.027396
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug(u"Test message")



# Generated at 2022-06-14 09:06:46.668632
# Unit test for function show_corrected_command
def test_show_corrected_command():
    assert show_corrected_command('ls') == 'ls'

# Generated at 2022-06-14 09:06:48.068171
# Unit test for function color
def test_color():
    assert color('foo') == 'foo'
    assert color(None) == ''



# Generated at 2022-06-14 09:06:57.635732
# Unit test for function show_corrected_command
def test_show_corrected_command():
    class Command():
        def __init__(self, script, side_effect):
            self.script = script
            self.side_effect = side_effect

    assert show_corrected_command(
        Command(script='git commit', side_effect=False)) == \
        const.USER_COMMAND_MARK + 'git commit'

    assert show_corrected_command(
        Command(script='cd', side_effect=True)) == \
        const.USER_COMMAND_MARK + 'cd (+side effect)'



# Generated at 2022-06-14 09:07:09.430561
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = type('', (), {'script': 'ls', 'side_effect': True})

# Generated at 2022-06-14 09:07:14.320031
# Unit test for function color
def test_color():
    assert color('test') == 'test'
    settings.no_colors = True
    assert color('test') == ''

# Generated at 2022-06-14 09:07:17.012553
# Unit test for function show_corrected_command
def test_show_corrected_command():
    class Command:
        script = 'script'
        side_effect = u'side effect'

    show_corrected_command(Command())



# Generated at 2022-06-14 09:07:22.444420
# Unit test for function color
def test_color():
    assert color(colorama.Fore.RED + 'foo' + colorama.Style.RESET_ALL) == ''
    settings.no_colors = False
    assert color(colorama.Fore.RED + 'foo' + colorama.Style.RESET_ALL) ==\
           colorama.Fore.RED + 'foo' + colorama.Style.RESET_ALL

# Generated at 2022-06-14 09:07:31.393745
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .shells import ShellInfo

    class ConfigurationDetails(object):
        reload = '. ~/.bashrc'

        class path(str):
            def __str__(self):
                return r'~/.bashrc'

        def can_configure_automatically(self):
            return True

    configuration_details = ConfigurationDetails()
    class Content(str):
        def __str__(self):
            return 'eval $(thefuck --alias)'

    configuration_details.content = Content()

    class ShellInfo(object):
        name = 'bash'

    how_to_configure_alias(configuration_details)
    how_to_configure_alias(None)

# Generated at 2022-06-14 09:07:35.198962
# Unit test for function debug_time
def test_debug_time():
    from unittest.mock import patch
    import os
    with patch('sys.stderr') as stderr:
        settings.debug = True
        with debug_time('test'):
            os.system('sleep 1')
        settings.debug = False
        assert stderr.write.call_count == 1
        assert 'test took' in stderr.write.call_args[0][0]



# Generated at 2022-06-14 09:07:36.001668
# Unit test for function debug
def test_debug():
    debug("Hello world")

# Generated at 2022-06-14 09:07:39.782330
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)
    how_to_configure_alias(('path','content','reload','can_configure_automatically'))

# Generated at 2022-06-14 09:07:41.812240
# Unit test for function debug
def test_debug():
    text = 'test'
    debug(text)


# Generated at 2022-06-14 09:07:44.504210
# Unit test for function debug_time
def test_debug_time():
    def test_func():
        print('asdf')
    with debug_time('test_func'):
        test_func()

# Generated at 2022-06-14 09:07:49.086269
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = type('CorrectedCommand',
                             (object,),
                             {'script': 'corrected',
                              'side_effect': None})
    confirm_text(corrected_command)

# Generated at 2022-06-14 09:07:56.930883
# Unit test for function color
def test_color():
    """It should add color escape sequences when colors are on."""
    settings.no_colors = False
    assert color('') == colorama.Back.RED + colorama.Fore.WHITE + colorama.Style.BRIGHT

    """It shouldn't add color escape sequences when colors are off."""
    settings.no_colors = True
    assert color('') == ''

# Generated at 2022-06-14 09:07:58.857387
# Unit test for function confirm_text

# Generated at 2022-06-14 09:08:01.933439
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    conf_details = {'answer': 'Hello world'}
    how_to_configure_alias(conf_details)



# Generated at 2022-06-14 09:08:11.298377
# Unit test for function show_corrected_command
def test_show_corrected_command():
    class CorrectedCommand(object):
        def __init__(self, script, side_effect):
            self.script = script
            self.side_effect = side_effect
    import StringIO
    old_stdout = sys.stdout
    sys.stdout = StringIO.StringIO()
    try:
        show_corrected_command(CorrectedCommand(script='ls', side_effect=True))
        assert sys.stdout.getvalue() == '> ls (+side effect)\n'
        show_corrected_command(CorrectedCommand(script='ls', side_effect=False))
        assert sys.stdout.getvalue() == '> ls (+side effect)\n> ls\n'
    finally:
        sys.stdout = old_stdout

# Generated at 2022-06-14 09:08:18.508199
# Unit test for function debug_time
def test_debug_time():
    from mock import patch
    from datetime import datetime, timedelta

    with patch('thefuck.shells.base.datetime') as mocked:
        mocked.now.return_value = datetime(2015, 1, 1)
        with debug_time('Command'):
            mocked.now.return_value = datetime(2015, 1, 1, 0, 0, 2)

        assert mocked.now.call_count == 2
        assert mocked.now.return_value - mocked.now.return_value == timedelta(seconds=2)

# Generated at 2022-06-14 09:08:23.958121
# Unit test for function confirm_text
def test_confirm_text():
    from .shells import Shell

    shell = Shell('bash')
    formatter = lambda c: shell.and_convert_commands(
        [c], require_confirmation=False)
    assert formatter('ls | grep test') == 'ls | grep test'

    formatter = lambda c: shell.and_convert_commands(
        [c], require_confirmation=True)
    assert formatter('ls | grep test') == 'ls | grep test'
    assert formatter('ls | rm test') == 'ls | rm test +side effect'

# Generated at 2022-06-14 09:08:27.842992
# Unit test for function debug
def test_debug():
    debug_output = StringIO()
    with patch('sys.stderr', debug_output):
        debug('foo')
        assert debug_output.getvalue() == 'foo\n'

# Generated at 2022-06-14 09:08:30.373619
# Unit test for function debug
def test_debug():
    settings.debug = True
    assert not debug('Test message')
    settings.debug = False
    assert not debug('Test message')



# Generated at 2022-06-14 09:08:39.559483
# Unit test for function debug
def test_debug():
    from StringIO import StringIO
    from contextlib import contextmanager

    @contextmanager
    def mock_setting(enable):
        orig = settings.debug
        settings.debug = enable
        yield
        settings.debug = orig

    with mock_setting(True), StringIO() as buf:
        debug(u'hello')
        assert buf.getvalue() == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m hello\n'

    with mock_setting(False), StringIO() as buf:
        debug(u'hello')
        assert buf.getvalue() == u''

# Generated at 2022-06-14 09:08:42.321049
# Unit test for function show_corrected_command
def test_show_corrected_command():
    assert show_corrected_command("git pus") == "git push"

# Generated at 2022-06-14 09:08:49.126737
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .corrector import CorrectedCommand
    corrected_command = CorrectedCommand('ls -la', 'ls -la', False)
    show_corrected_command(corrected_command)



# Generated at 2022-06-14 09:08:50.764998
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test_debug_time'):
        pass

# Generated at 2022-06-14 09:08:52.800229
# Unit test for function debug_time
def test_debug_time():
    pass
    # with debug_time(u'Message'):
    #     time.sleep(0.1)

# Generated at 2022-06-14 09:08:55.129323
# Unit test for function show_corrected_command
def test_show_corrected_command():
    a = Command('', '', False)
    show_corrected_command(a)

# Set up for unit test

# Generated at 2022-06-14 09:09:03.850147
# Unit test for function show_corrected_command
def test_show_corrected_command():
    # Module-level variables are used in these functions
    # so they need to be reset in each test
    colorama.reset_all()
    settings.reset_all()

    from .types import Command

    command = Command('git commit', 'git commit -v')
    show_corrected_command(command)
    assert command.script in sys.stderr.getvalue()

    settings.no_colors = True
    show_corrected_command(command)
    assert command.script in sys.stderr.getvalue()



# Generated at 2022-06-14 09:09:08.954301
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .configuration import ConfigurationDetails
    how_to_configure_alias(ConfigurationDetails(
        can_configure_automatically=True,
        path='~/.config.fish',
        reload='fuck --reload',
        content='status --is-interactive fish'))



# Generated at 2022-06-14 09:09:12.277834
# Unit test for function color
def test_color():
    assert not settings.no_colors
    assert color('test') == 'test'
    settings.no_colors = True
    assert color('test') == ''
    settings.no_colors = False

# Generated at 2022-06-14 09:09:19.807247
# Unit test for function debug
def test_debug():
    debug_data = []

    def _debug(msg):
        debug_data.append(msg)

    global debug
    debug = _debug
    debug(u'abc')
    debug(u'def')
    debug = lambda x: None
    assert debug_data == [u'abc', u'def']
    debug(u'abc')
    assert debug_data == [u'abc', u'def']

# Generated at 2022-06-14 09:09:32.341948
# Unit test for function debug
def test_debug():
    from thefuck.utils import get_closest, memoize, wrap_settings
    from thefuck.conf import settings
    from . import const
    from .shells import Shell
    from .shells.bash import Bash
    from .shells import get_aliases
    from .rules.git_dirty_worktree import match, get_new_command
    from .rules.python_no_module import match, get_new_command
    from .rules.pacman_dpkg_mismatch import match, get_new_command
    from .rules.git_no_command import match, get_new_command
    from .rules.git_stash import match, get_new_command
    from .rules.apt_get_dpkg_mismatch import match, get_new_command

# Generated at 2022-06-14 09:09:35.186583
# Unit test for function debug
def test_debug():
   #from thefuck.main import debug
   debug_msg = "This is debug message"
   debug(debug_msg)

# Generated at 2022-06-14 09:09:40.827298
# Unit test for function color
def test_color():
    assert color('red') == ''
    colorama.init()
    assert color('red') == '\x1b[31m'

# Generated at 2022-06-14 09:09:43.302889
# Unit test for function color
def test_color():
    assert color(colorama.Style.BRIGHT) == colorama.Style.BRIGHT
    assert color(colorama.Style.BRIGHT) != ''

# Generated at 2022-06-14 09:09:44.572608
# Unit test for function color
def test_color():
    assert color('red') == colorama.Fore.RED



# Generated at 2022-06-14 09:09:49.461483
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .shells import Bash
    from .command import Command

    shell = Bash()
    command = Command('command', 'script')
    show_corrected_command(command)



# Generated at 2022-06-14 09:10:02.586899
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import unittest
    class TestShowCorrectedCommand(unittest.TestCase):
        def setUp(self):
            import StringIO
            self.out = StringIO.StringIO()
            self.old_stderr = sys.stderr
            sys.stderr = self.out

        def tearDown(self):
            self.out.close()
            sys.stderr = self.old_stderr

        def test_show_corrected_command_without_side_effects(self):
            from thefuck.shells import Command
            show_corrected_command(Command(script='git commit -a', side_effect=False))
            self.assertEqual(self.out.getvalue(), u'$ git commit -a\n')


# Generated at 2022-06-14 09:10:07.894725
# Unit test for function debug_time
def test_debug_time():
    def test_function(iterations=3):
        for i in xrange(0, iterations):
            debug_time('iteration {}'.format(i))
    import cProfile, pstats
    cProfile.run('test_function()', 'stats')
    p = pstats.Stats('stats')
    p.sort_stats('cumulative').print_stats()

# Generated at 2022-06-14 09:10:10.619845
# Unit test for function debug
def test_debug():
    from contextlib import redirect_stderr

    from io import StringIO

    with redirect_stderr(StringIO()) as stderr:
        debug('test')

    assert stderr.getvalue().endswith('DEBUG: test\n')

# Generated at 2022-06-14 09:10:13.418833
# Unit test for function debug
def test_debug():
    from StringIO import StringIO

    captured_output = StringIO()
    sys.stderr = captured_output
    debug('test')
    sys.stderr = sys.__stderr__
    assert captured_output.getvalue() == '\x1b[34m\x1b[1mDEBUG:\x1b[0m test\n'

# Generated at 2022-06-14 09:10:23.023240
# Unit test for function confirm_text
def test_confirm_text():
    correct_text = u'Fuck Test Corrected Command'
    with open('/tmp/test_confirm_text.txt', 'w+') as file_:
        sys.stderr = file_
        original_sys_stderr = sys.stderr
        try:
            confirm_text(correct_text)
            file_.seek(0)
            assert file_.read() == u' [enter/↑/↓/ctrl+c]\n'
        finally:
            sys.stderr = original_sys_stderr

if __name__ == '__main__':
    test_confirm_text()

# Generated at 2022-06-14 09:10:31.501425
# Unit test for function confirm_text
def test_confirm_text():
    from .shells import Shell
    shell = Shell()
    import re

    def mock_read_line(self):
        tmp = self._read_line
        self._read_line = lambda: 'echo "Hello, World"'
        yield
        self._read_line = tmp

    with mock_read_line(shell):
        confirm_text(shell.from_shell('fuck'))
        assert re.search(r'\[enter/↑/↓/ctrl\+c\]', sys.stderr.getvalue())

# Generated at 2022-06-14 09:10:41.904580
# Unit test for function debug_time
def test_debug_time():
    import time
    import mock

    time.sleep = mock.Mock()
    with debug_time('Test debug time'):
        time.sleep(1)

    assert time.sleep.called
    assert time.sleep.call_args == (1, )

# Generated at 2022-06-14 09:10:50.364378
# Unit test for function confirm_text
def test_confirm_text():
    import sys
    sys.stderr.write = lambda x: x
    corrected_command = type('', (), {})
    corrected_command.side_effect = False
    corrected_command.script = 'git config --global user.email "you@example.com"'
    sys.stderr.write(confirm_text(corrected_command))
    assert sys.stderr.write == '\x1b[1K\rFuck: git config --global user.email "you@example.com" [enter/↑/↓/ctrl+c]\n'
    corrected_command.side_effect = True
    sys.stderr.write(confirm_text(corrected_command))

# Generated at 2022-06-14 09:10:53.947388
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text(const.CorrectedCommand('test','test')) == ">>>test [enter/↑/↓/ctrl+c]"
test_confirm_text()



# Generated at 2022-06-14 09:10:59.572833
# Unit test for function debug_time
def test_debug_time():
    import mock
    with mock.patch('sys.stderr') as stderr_mock:
        with debug_time('TEST'):
            pass

        stderr_mock.write.assert_called_with(u'TEST took: 0:00:00.000000\n')

# Generated at 2022-06-14 09:11:01.332017
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass


# Generated at 2022-06-14 09:11:04.646503
# Unit test for function debug_time
def test_debug_time():
    debug = debug_timer = ''

    with debug_time('test'):
        pass

    with debug_time('test'):
        debug_timer = debug

    assert debug == debug_timer

# Generated at 2022-06-14 09:11:07.963944
# Unit test for function debug
def test_debug():
    import io
    sys.stderr = io.StringIO()
    debug('test')
    sys.stderr.seek(0)
    assert 'test' in sys.stderr.readline(), 'debug work'

# Generated at 2022-06-14 09:11:11.189596
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = type('', (), {
        'script': 'ls -l',
        'side_effect': False
    })
    confirm_text(corrected_command)

# Generated at 2022-06-14 09:11:13.321717
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .command import Command
    print(show_corrected_command(Command('ls', 'ls -al')))

# Generated at 2022-06-14 09:11:25.482280
# Unit test for function confirm_text
def test_confirm_text():
    from .shells.bash import Bash
    from .shell import Shell
    assert confirm_text(Bash().from_shell(Shell('pwd', datetime(1, 1, 1)))) == u'[fuck]\033[1K\r\x1b[1mpwd\x1b[21m \x1b[32menter\x1b[0m/\x1b[34m↑\x1b[0m/\x1b[34m↓\x1b[0m/\x1b[31mctrl+c\x1b[0m]'

# Generated at 2022-06-14 09:11:32.392447
# Unit test for function debug_time
def test_debug_time():
    with debug_time('decorator'):
        pass
    with debug_time('decorator'):
        pass

# Generated at 2022-06-14 09:11:41.944950
# Unit test for function debug
def test_debug():
    import cStringIO
    import sys

    stdout = cStringIO.StringIO()
    sys.stderr = stdout

    debug("hello")
    assert(stdout.getvalue() == "")

    settings.debug = True
    debug("hello")
    assert(stdout.getvalue()
           == "\x1b[0;34;1mDEBUG:\x1b[0m hello\n")

    settings.no_colors = True
    debug("hello")
    assert(stdout.getvalue()
           == "DEBUG: hello\n")

# Generated at 2022-06-14 09:11:43.396744
# Unit test for function debug_time
def test_debug_time():
    import time

    with debug_time('test'):
        time.sleep(1)

# Generated at 2022-06-14 09:11:48.117564
# Unit test for function color
def test_color():
    assert color(colorama.Style.BRIGHT) == ''
    assert color(colorama.Style.BRIGHT) == ''
    settings.no_colors = False
    assert color(colorama.Style.BRIGHT) == colorama.Style.BRIGHT

# Generated at 2022-06-14 09:11:50.396939
# Unit test for function debug_time
def test_debug_time():
    import time
    with debug_time("test"):
        time.sleep(1)


# Generated at 2022-06-14 09:11:54.934245
# Unit test for function color
def test_color():
    assert color('%s' % colorama.Fore.RED) == '%s' % colorama.Fore.RED
    settings.no_colors = True
    assert color('%s' % colorama.Fore.RED) == ''

# Generated at 2022-06-14 09:11:56.732849
# Unit test for function show_corrected_command
def test_show_corrected_command():
    sys.stderr.write = lambda text: None
    assert show_corrected_command(None) is None

# Generated at 2022-06-14 09:11:57.590955
# Unit test for function show_corrected_command
def test_show_corrected_command():
    show_corrected_command(corrected_command)

# Generated at 2022-06-14 09:11:58.605623
# Unit test for function debug_time
def test_debug_time():
    debug_time("test")

# Generated at 2022-06-14 09:12:00.029966
# Unit test for function debug_time
def test_debug_time():
    with debug_time('time'):
        pass

# Generated at 2022-06-14 09:12:08.796112
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .shells import Shell
    configuration_details = Shell.from_shell('/bin/zsh')
    how_to_configure_alias(configuration_details)
# Result:
# Seems like fuck alias isn't configured!
# Please put
# eval $(thefuck --alias)
# in your
# ~/.zshrc
# and apply changes with
# source ~/.zshrc
# or restart your shell.
# More details - https://github.com/nvbn/thefuck#manual-installation

# Generated at 2022-06-14 09:12:16.597617
# Unit test for function debug
def test_debug():
    from StringIO import StringIO
    from .conf import settings
    from .utils import reset_settings
    import os

    settings.debug = True
    saved_environment = os.environ.copy()
    os.environ['PYTHONPATH'] = ''
    output = StringIO()
    debug_ = lambda x: sys.stderr.write(x)
    saved_stderr = sys.stderr
    sys.stderr = output
    try:
        debug('test')
    finally:
        sys.stderr = saved_stderr
        settings.debug = False
        reset_settings()
        os.environ = saved_environment
    assert 'test' in output.getvalue()

# Generated at 2022-06-14 09:12:27.844348
# Unit test for function debug_time
def test_debug_time():
    import time
    t = time.time()
    print
    with debug_time('test_debug_time'):
        time.sleep(1)
    assert (time.time() - t) > 1
    t = time.time()
    print
    with debug_time('test_debug_time'):
        pass
    assert (time.time() - t) < 1


if __name__ == '__main__':
    test_debug_time()

# Generated at 2022-06-14 09:12:34.862403
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    from contextlib import contextmanager

    @contextmanager
    def debug_time(msg):
        try:
            yield
        finally:
            debug(u'{} took: {}'.format(msg, timedelta(seconds=1)))

    def debug(msg):
        global result
        result = msg

    with debug_time('test'):
        pass

    assert u'test took: 0:00:01' == result



# Generated at 2022-06-14 09:12:48.494685
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from mock import patch
    from .rules.utils import ConfigurationDetails
    from .shells import shell
    from .utils import replace_argument
    from .types import Command

    with patch('sys.stderr') as stderr:
        how_to_configure_alias(ConfigurationDetails(replace_argument('fc -s'),
                                                    '~/.bashrc',
                                                    'source ~/.bashrc'))

        how_to_configure_alias(None)


# Generated at 2022-06-14 09:12:50.550395
# Unit test for function debug_time
def test_debug_time():
    def f():
        import time
        time.sleep(0.1)

    with debug_time(u'test'):
        f()

# Generated at 2022-06-14 09:12:54.210074
# Unit test for function debug_time
def test_debug_time():
    import datetime
    import time
    started = datetime.datetime.now()
    time.sleep(1)
    debug = datetime.datetime.now() - started
    assert debug == datetime.timedelta(0, 1)

# Generated at 2022-06-14 09:12:58.522095
# Unit test for function show_corrected_command
def test_show_corrected_command():
    # given
    corrected_command = 'ls'
    # when
    show_corrected_command(corrected_command)
    # then
    assert sys.stderr.getvalue().endswith('ls\n')



# Generated at 2022-06-14 09:13:00.885263
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)
    how_to_configure_alias('some')



# Generated at 2022-06-14 09:13:10.677900
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import sys
    import re
    from test.utils import prepare_mocked_settings, prepare_mocked_open

    with prepare_mocked_open() as (open_mock, resolve_mock):
        with prepare_mocked_settings({'no_colors': False}):
            show_corrected_command(('', None))
            assert not resolve_mock.called
            assert sys.stderr.getvalue() == u'$ []\n'

            sys.stderr.truncate(0)
            show_corrected_command(('fuck', None))
            assert not resolve_mock.called
            assert sys.stderr.getvalue() == u'$ fuck\n'

            sys.stderr.truncate(0)

# Generated at 2022-06-14 09:13:21.675595
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    from mock import patch

    with patch.object(sys.stderr, 'write') as mock_write, \
            patch.object(datetime, 'now') as mock_now:
        mock_now.return_value = datetime(2015, 10, 23, 5, 15)
        with debug_time('foo'):
            mock_now.return_value = datetime(2015, 10, 23, 5, 16)
        assert mock_write.call_args[0][0] == \
            '\x1b[34m\x1b[1mDEBUG:\x1b[0m foo took: 0:01:00'

# Generated at 2022-06-14 09:13:23.484038
# Unit test for function color
def test_color():
    assert color('red') == ''
    assert color(colorama.Fore.RED) != ''

# Generated at 2022-06-14 09:13:27.925286
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .shells.base import Shell

    settings.load()
    assert '$ fuck echo "test"' in show_corrected_command(
        Shell('', 'fuck echo "test"', 'user').get_history()[-1])



# Generated at 2022-06-14 09:13:29.100803
# Unit test for function show_corrected_command
def test_show_corrected_command():
    assert show_corrected_command('ls -la') == 'f ls -la \n'

# Generated at 2022-06-14 09:13:31.744133
# Unit test for function debug
def test_debug():
    try:
        with debug_time('test_debug'):
            1 + 'a'
    except Exception:
        pass
    print(format_exception(*sys.exc_info()))

# Generated at 2022-06-14 09:13:36.063940
# Unit test for function debug
def test_debug():
    from contextlib import contextmanager
    from StringIO import StringIO

    @contextmanager
    def debug_log():
        with settings.debug_on():
            debug_stream = StringIO()
            old_debug_file = sys.stderr
            sys.stderr = debug_stream
            try:
                yield debug_stream
            finally:
                debug_stream.seek(0)
                sys.stderr = old_debug_file

    def assert_debug_file(stream, expected_msg):
        stream.seek(0)
        msg = stream.read()
        assert msg == (u'\x1b[34m\x1b[1mDEBUG:\x1b[0m ' + expected_msg + u'\n')


# Generated at 2022-06-14 09:13:47.748235
# Unit test for function show_corrected_command
def test_show_corrected_command():

    class FakeCommand(object):

        def __init__(self, script, side_effect):
            self.script = script
            self.side_effect = side_effect

    corrected_command = FakeCommand(script='foo', side_effect=False)
    show_corrected_command(corrected_command)
    assert sys.stderr.getvalue() == '>: foo\n'

    corrected_command = FakeCommand(script='foo', side_effect=True)
    show_corrected_command(corrected_command)
    assert sys.stderr.getvalue() == '>: foo (+side effect)\n'

    corrected_command = FakeCommand(script='foo', side_effect=False)
    show_corrected_command(corrected_command)

# Generated at 2022-06-14 09:13:52.398152
# Unit test for function debug
def test_debug():
    import mock
    with mock.patch('sys.stderr') as stderr:
        debug('test')
        stderr.write.assert_called_with(u'\x1b[34m\x1b[1mDEBUG:\x1b[0m test\n')