

# Generated at 2022-06-14 09:03:56.934282
# Unit test for function debug_time
def test_debug_time():
    from thefuck.tests.utils import Mock

    output = Mock()
    with debug_time('foo'):
        pass

    assert output.write.called_once_with('foo took: 0:00:00\n')

# Generated at 2022-06-14 09:04:03.041120
# Unit test for function debug
def test_debug():
    from mock import patch
    with patch('sys.stderr') as mock_stderr:
        debug('test message')
        mock_stderr.write.assert_called_once_with(
            u'\x1b[94m\x1b[1mDEBUG:\x1b[0m test message\n')


# Generated at 2022-06-14 09:04:11.414304
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .command import Command
    from .types import CorrectedCommand
    from .types import MatchedRule
    from .utils import get_closest

    class DummyRule(object):
        name = 'Dummy Rule'

    corrected_command = CorrectedCommand(Command('emacs', ''), None)
    show_corrected_command(corrected_command)

    corrected_command = CorrectedCommand(Command('emacs', ''),
            MatchedRule(DummyRule(), get_closest('emacs', ['vim'])))
    show_corrected_command(corrected_command)

# Generated at 2022-06-14 09:04:14.654602
# Unit test for function debug
def test_debug():
    with settings as s:
        s.debug = True

        debug('debug message')



# Generated at 2022-06-14 09:04:16.470725
# Unit test for function debug_time
def test_debug_time():
    import time
    with debug_time('Test'):
        time.sleep(1)

# Generated at 2022-06-14 09:04:26.901556
# Unit test for function show_corrected_command
def test_show_corrected_command():
    assert show_corrected_command(Script(script='foo', side_effect=False)) == '{}foo\n'.format(const.USER_COMMAND_MARK)
    assert show_corrected_command(Script(script='foo', side_effect=True)) == '{}foo (+side effect)\n'.format(const.USER_COMMAND_MARK)
    assert show_corrected_command(Script(script='', side_effect=False)) == '{} \n'.format(const.USER_COMMAND_MARK)
    assert show_corrected_command(Script(script='', side_effect=True)) == '{}  (+side effect)\n'.format(const.USER_COMMAND_MARK)



# Generated at 2022-06-14 09:04:32.450168
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    configuration_details = {
        'path': u'~/.bashrc',
        'reload': 'source ~/.bashrc',
        'content': u'eval $(thefuck --alias)',
        'can_configure_automatically': True
    }

    how_to_configure_alias(configuration_details)
    assert True

# Generated at 2022-06-14 09:04:35.274226
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass


if __name__ == '__main__':
    test_debug_time()

# Generated at 2022-06-14 09:04:38.298196
# Unit test for function debug
def test_debug():
    from mock import patch
    stderr = patch('sys.stderr')
    debug(u'foo')
    assert stderr.write.called

# Generated at 2022-06-14 09:04:45.143689
# Unit test for function debug_time
def test_debug_time():
    from StringIO import StringIO
    from mock import patch, sentinel
    from . import log
    with patch.object(log, 'debug', return_value=None):
        with patch('sys.stderr', new_callable=StringIO) as err:
            with log.debug_time(sentinel.msg):
                pass
            assert (err.getvalue()
                    == 'DEBUG: {} took: 0:00:00.000000\n'.format(sentinel.msg))

# Generated at 2022-06-14 09:04:59.611283
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    import click
    import click.testing
    runner = click.testing.CliRunner()
    with runner.isolated_filesystem():
        import os
        import platform
        reload_cmd = '. ~/.profile' if platform.system() == 'Darwin' else 'builtin source ~/.bash_profile'
        how_to_configure_alias(const.ConfigurationDetails('~/.bash_profile', os.path.expanduser(b'~/.bash_profile'),
                                                  u'eval $(thefuck --alias)',
                                                  '(echo "eval $(thefuck --alias)") >> ~/.bash_profile',
                                                  reload_cmd, True))

# Generated at 2022-06-14 09:05:00.506660
# Unit test for function debug
def test_debug():
    debug('hello world')

# Generated at 2022-06-14 09:05:09.597641
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .types import CorrectedCommand
    from .conf import Settings
    from . import shells

    settings = Settings(no_color=True)
    shells.get_shell(settings)
    show_corrected_command(CorrectedCommand('ls', 'ls-alias'))
    show_corrected_command(CorrectedCommand('ls', 'ls-alias', True))

# Generated at 2022-06-14 09:05:18.929917
# Unit test for function debug_time
def test_debug_time():
    import time
    import contextlib
    @contextlib.contextmanager
    def fake_time():
        time.sleep(0.1)
        yield
    import io
    test_output = io.BytesIO()
    stdout = sys.stderr
    sys.stderr = test_output
    with debug_time(u'Test message'):
        with fake_time():
            with fake_time():
                pass
    assert 'Test message took: ' in test_output.getvalue()
    sys.stderr = stdout

# Generated at 2022-06-14 09:05:21.178588
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    assert 'Seems like thefuck alias isn\'t configured!' in how_to_configure_alias(None)


# Generated at 2022-06-14 09:05:22.802174
# Unit test for function debug
def test_debug():
    debug('test')



# Generated at 2022-06-14 09:05:24.124092
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias()

# Generated at 2022-06-14 09:05:29.006912
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = type('CorrectedCommand', (object,), {
        'script': 'foo',
        'side_effect': False})()

    assert confirm_text(corrected_command) == u'$ foo [enter/↑/↓/ctrl+c]'



# Generated at 2022-06-14 09:05:31.991577
# Unit test for function debug
def test_debug():
    print("Test debug() ...")
    debug("test debug")
    print("Test debug() OK")



# Generated at 2022-06-14 09:05:33.417523
# Unit test for function debug_time
def test_debug_time():
    with debug_time('Thinking'):
        pass

# Generated at 2022-06-14 09:05:37.578278
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text(['some', 'command']) == None



# Generated at 2022-06-14 09:05:45.191185
# Unit test for function debug
def test_debug():
    from test.utils import Mock
    mock = Mock()

    mock.debug = True
    settings.debug = mock.debug
    debug('some msg')
    assert mock.written() == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m some msg\n'

    mock.debug = False
    settings.debug = mock.debug
    debug('some msg')
    assert mock.written() == u''

# Generated at 2022-06-14 09:05:47.523808
# Unit test for function color
def test_color():
    assert color('abc') == 'abc'
    settings.no_colors = True
    assert color('abc') == ''

# Generated at 2022-06-14 09:05:49.215840
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text('python script.py')



# Generated at 2022-06-14 09:05:52.911322
# Unit test for function debug_time
def test_debug_time():
    _debug = []

    def debug(msg):
        _debug.append(msg)

    global debug
    with debug_time('message'):
        assert not _debug
    assert _debug
    debug('foo')

# Generated at 2022-06-14 09:06:02.110387
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    class Dummy:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    configuration_details = Dummy(
        content='Content',
        path='Path',
        reload='Reload')

    expected = (
        u"Seems like The Fuck isn't configured!\n"
        u"Please put Content in your Path and apply "
        u"changes with Reload or restart your shell.\n")
    assert how_to_configure_alias(configuration_details) == expected,\
        'how_to_configure_alias works wrong'

# Generated at 2022-06-14 09:06:13.590854
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from thefuck.types import ConfigurationDetails
    configuration_details = ConfigurationDetails(
        can_configure_automatically=True,
        path='~/.zshrc',
        py3='autofuck 3',
        py2='autofuck 2',
        reload='. ~/.zshrc')

    # format list of messages
    messages = []
    for line in how_to_configure_alias(configuration_details).split('\n'):
        line = line.replace(u'\r', '')
        messages.append(line)


# Generated at 2022-06-14 09:06:22.676225
# Unit test for function debug
def test_debug():
    from .conf import settings
    from . import const
    import colorama
    debug_msg = "Test debug message"
    settings.debug = True
    expected_output = u'{blue}{bold}DEBUG:{reset} {msg}\n'.format(
            msg=debug_msg,
            reset=color(colorama.Style.RESET_ALL),
            blue=color(colorama.Fore.BLUE),
            bold=color(colorama.Style.BRIGHT))
    assert debug(debug_msg) == expected_output


# Generated at 2022-06-14 09:06:24.689292
# Unit test for function show_corrected_command
def test_show_corrected_command():
    class Command:

        def __init__(self, script, side_effect):
            self.script = script
            self.side_effect = side_effect

    assert show_corrected_command(Command('pwd', False)) is None



# Generated at 2022-06-14 09:06:31.511074
# Unit test for function debug
def test_debug():
    from StringIO import StringIO
    from contextlib import contextmanager
    import sys

    @contextmanager
    def captured_output():
        old_out = sys.stderr
        old_colorama = sys.modules['colorama']
        del sys.modules['colorama']
        try:
            out = StringIO()
            sys.stderr = out
            yield out
        finally:
            sys.stderr = old_out
            sys.modules['colorama'] = old_colorama

    with captured_output() as output:
        debug(u'pizza')
        assert output.getvalue() == u'DEBUG: pizza\n'



# Generated at 2022-06-14 09:06:39.670945
# Unit test for function debug_time
def test_debug_time():
    with debug_time('name'):
        import time
        time.sleep(1)


# Generated at 2022-06-14 09:06:44.473429
# Unit test for function debug_time
def test_debug_time():
    import pytest
    from mock import Mock
    with debug_time('Test'):
        pass
    sys.stderr.write = Mock()
    settings.debug = True
    with debug_time('Test'):
        pass
    assert sys.stderr.write.called

# Generated at 2022-06-14 09:06:49.795833
# Unit test for function debug
def test_debug():
    fuu = "test"
    def side_effect(msg):
        global fuu
        fuu = msg
    settings.debug = True
    debug('foo bar')
    settings.debug = False
    sys.stderr.write = side_effect
    debug('foo bar')
    sys.stderr = sys.__stderr__
    assert fuu == 'foo bar'

# Generated at 2022-06-14 09:06:57.180624
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = u'ls -al'

# Generated at 2022-06-14 09:07:04.518458
# Unit test for function confirm_text
def test_confirm_text():
    sys.stderr.write.assert_any_call(
        (u'{prefix}{clear}{bold}{script}{reset}{side_effect} '
         u'[{green}enter{reset}/{blue}↑{reset}/{blue}↓{reset}'
         u'/{red}ctrl+c{reset}]').format(
            prefix=const.USER_COMMAND_MARK,
            script='cmd_script',
            side_effect=' (+side effect)',
            clear='\033[1K\r',
            bold=color(colorama.Style.BRIGHT),
            green=color(colorama.Fore.GREEN),
            red=color(colorama.Fore.RED),
            reset=color(colorama.Style.RESET_ALL),
            blue=color(colorama.Fore.BLUE)))

# Generated at 2022-06-14 09:07:06.013267
# Unit test for function show_corrected_command
def test_show_corrected_command():
    show_corrected_command('echo "yes"')

# Generated at 2022-06-14 09:07:08.278616
# Unit test for function debug_time
def test_debug_time():
    with debug_time(u'foo bar'):
        pass

# Generated at 2022-06-14 09:07:13.481023
# Unit test for function confirm_text
def test_confirm_text():
    from thefuck.utils import confirm_text
    import sys
    def mock_stderr(self):
        return 'hello world'
    sys.stderr = mock_stderr()
    confirm_text('hello')
    assert sys.stderr == 'hello world'

# Generated at 2022-06-14 09:07:17.445002
# Unit test for function color
def test_color():
    assert color(u'a') == u'a'
    assert color('a') == u'a'

    settings.no_colors = True
    assert color(u'a') == u''
    assert color('a') == u''

# Generated at 2022-06-14 09:07:22.205656
# Unit test for function show_corrected_command
def test_show_corrected_command():
    command = 'fuck'
    side_effect = True
    expected = '$ fuck (+side effect)\n'
    show_corrected_command(CorrectedCommand(command, side_effect))
    captured = sys.stderr.getvalue()
    assert captured == expected
    sys.stderr = sys.__stderr__


# Generated at 2022-06-14 09:07:30.338378
# Unit test for function confirm_text
def test_confirm_text():
    from .application import Application
    from .rules.git import git_rule

    app = Application()
    corrected_cmd = app.correct_command('git sa')
    confirm_text(corrected_cmd)

# Generated at 2022-06-14 09:07:34.112378
# Unit test for function show_corrected_command
def test_show_corrected_command():
    mock_command = type('MockCommand', (object,),
                        dict(script='mocked_script', side_effect=False))
    show_corrected_command(mock_command)

    mock_command = type('MockCommand', (object,),
                        dict(script='mocked_script', side_effect=True))
    show_corrected_command(mock_command)

# Generated at 2022-06-14 09:07:34.685710
# Unit test for function debug
def test_debug():
    debug('message', file=sys.stderr)

# Generated at 2022-06-14 09:07:36.011124
# Unit test for function color
def test_color():
    assert color(u'123') == u'123'
    assert color(u'123').__class__ == unicode



# Generated at 2022-06-14 09:07:49.059077
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from subprocess import check_output
    from .shells import get_shell_type
    from textwrap import dedent
    default_shell = get_shell_type().name
    expected_output = dedent(u"""\
        Seems like fuck alias isn't configured!
        Please put eval "$(thefuck --alias fuck)" in your ~/.{0}rc and apply changes with source ~/.{0}rc or restart your shell.
        Or run fuck a second time to configure it automatically.
        More details - https://github.com/nvbn/thefuck#manual-installation
        """.format(default_shell))

    how_to_configure_alias(None)

# Generated at 2022-06-14 09:07:54.784253
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from tempfile import NamedTemporaryFile
    from .command import Command
    with NamedTemporaryFile('w+b') as temp:
        temp.write('')
        temp.flush()

        assert sys.stderr.write(u'\033[1K\r{}ls\n'.format(const.USER_COMMAND_MARK))

        sys.stderr.write(u'')
        show_corrected_command(Command(u'clear', u'ls', temp.name, ''))

        temp.close()

# Generated at 2022-06-14 09:08:00.777796
# Unit test for function confirm_text
def test_confirm_text():
    # Corrected command
    # TODO: Use mock
    import io
    corrected_command = type('CorrectedCommand', (object,),
                             {'script': 'cat /dev/null', 'side_effect': False})
    sys.stderr = io.StringIO()
    confirm_text(corrected_command)
    result_string = sys.stderr.getvalue()
    sys.stderr = sys.__stderr__

# Generated at 2022-06-14 09:08:03.735686
# Unit test for function show_corrected_command
def test_show_corrected_command():
    print('Testing show_corrected_command.')
    show_corrected_command('ls')
    print('Test passed!')


# Generated at 2022-06-14 09:08:07.198080
# Unit test for function debug
def test_debug():
    _stderr = sys.stderr
    sys.stderr = None
    assert debug('test message') is None
    sys.stderr = _stderr

# Generated at 2022-06-14 09:08:09.453953
# Unit test for function confirm_text
def test_confirm_text():
    corrected_cmd = ("find . -name foo.bar"
                     "(display changed command with side effect)")

# Generated at 2022-06-14 09:08:18.684306
# Unit test for function color
def test_color():
    assert color(colorama.Fore.BLUE + 'blue') == '\x1b[34mblue\x1b[39m'
    assert color(colorama.Fore.BLUE + 'blue') == 'blue'

# Generated at 2022-06-14 09:08:19.472868
# Unit test for function debug_time
def test_debug_time():
    pass

# Generated at 2022-06-14 09:08:23.928914
# Unit test for function debug_time
def test_debug_time():
    from mock import patch
    with patch('thefuck.shells.common.debug') as debug:
        with debug_time('msg'):
            pass
        debug.assert_called_once_with(u'msg took: 0:00:00')

# Generated at 2022-06-14 09:08:29.265572
# Unit test for function confirm_text
def test_confirm_text():
    for i in range(len(const.USER_COMMAND_MARK)):
        confirm_text('')
        sys.stderr.write('.')
    confirm_text('')
    sys.stderr.write('\n')
    print("Test passed")

# Generated at 2022-06-14 09:08:30.355464
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias()


# Generated at 2022-06-14 09:08:32.937876
# Unit test for function debug_time
def test_debug_time():
    sys.stderr = lambda: ''
    sys.stderr.write = lambda: ''
    assert(debug_time('msg') is None)

# Generated at 2022-06-14 09:08:37.661635
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    colorama.init(autoreset=True)
    how_to_configure_alias(None)
    how_to_configure_alias({'content': 'content', 'path': 'path', 'reload': 'reload', 'can_configure_automatically': True})

# Generated at 2022-06-14 09:08:43.460656
# Unit test for function show_corrected_command
def test_show_corrected_command():
    f = open('/tmp/test', 'w')
    sys.stderr = f
    show_corrected_command('git')
    f.close()
    f = open('/tmp/test', 'r')
    assert f.read() == 'Corrected command: git\n'
    f.close()

# Generated at 2022-06-14 09:08:46.375123
# Unit test for function debug_time
def test_debug_time():
    started = datetime.now()
    debug_time('debug_time')
    assert debug_time('debug_time')
    end = datetime.now()
    assert started < end

# Generated at 2022-06-14 09:08:50.240804
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
   print('How to configure alias?')
   assert how_to_configure_alias([]) == []

# Generated at 2022-06-14 09:09:08.173642
# Unit test for function debug
def test_debug():
    from nose.tools import eq_, with_setup
    from StringIO import StringIO
    from .conf import settings
    from . import const

    test_message = 'test message'
    classic_debug_output = u'\033[94m\033[1mDEBUG:\033[0m {}\n'.format(test_message)

    def setup():
        settings.debug = True
        sys.stderr = StringIO()

    def teardown():
        settings.debug = False
        sys.stderr = sys.__stderr__

    @with_setup(setup, teardown)
    def test_output():
        debug(test_message)
        eq_(sys.stderr.getvalue(), classic_debug_output)


# Generated at 2022-06-14 09:09:10.661713
# Unit test for function debug_time
def test_debug_time():
    try:
        with debug_time("test"):
            pass
    except UnboundLocalError:
        raise Exception("'started' variable isn't set")

# Generated at 2022-06-14 09:09:24.550583
# Unit test for function confirm_text
def test_confirm_text():
    import unittest

    class TestConfirmText(unittest.TestCase):
        def setUp(self):
            import os
            import tempfile
            self.script = tempfile.mktemp()
            self.log = tempfile.mktemp()

            self.old_stderr = sys.stderr
            self.old_env = dict(os.environ)

            f = open(self.log, 'w')
            sys.stderr = f
            os.environ['TEST_CASE'] = 'test_confirm_text'

        def tearDown(self):
            import os
            import tempfile

            try:
                sys.stderr.close()
            finally:
                sys.stderr = self.old_stderr


# Generated at 2022-06-14 09:09:28.624071
# Unit test for function confirm_text
def test_confirm_text():
    sys.stderr.write('It is test_confirm_text\n')
    confirm_text('ls -la')
    sys.stderr.write('It is test_confirm_text\n')

# Generated at 2022-06-14 09:09:29.973577
# Unit test for function debug_time
def test_debug_time():
    with debug_time('abc'):
        pass

# Generated at 2022-06-14 09:09:43.265505
# Unit test for function confirm_text
def test_confirm_text():
    import io
    import sys
    from thefuck.conf import Command
    from thefuck.rules.nodejs import match, get_new_command

    test_io = io.StringIO()
    sys.stderr = test_io
    confirm_text(Command("npm install", "", "", "", "", "npm i"))

# Generated at 2022-06-14 09:09:47.918716
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    import StringIO
    output = StringIO.StringIO()
    saved_stdout = sys.stdout
    try:
        sys.stdout = output
        how_to_configure_alias()
        output_value = output.getvalue()
        assert output_value == u"Seems like \x1b[1mfuck\x1b[22m alias isn't configured!\nMore details - https://github.com/nvbn/thefuck#manual-installation\n"
    finally:
        sys.stdout = saved_stdout


# Generated at 2022-06-14 09:09:48.854004
# Unit test for function debug_time
def test_debug_time():
    with debug_time('Test'):
        pass

# Generated at 2022-06-14 09:09:50.846648
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = 'ls -la'
    confirm_text(corrected_command)

# Generated at 2022-06-14 09:09:52.095006
# Unit test for function debug
def test_debug():
    debug("test debug")



# Generated at 2022-06-14 09:10:02.065429
# Unit test for function show_corrected_command
def test_show_corrected_command():
    class CorrectedCommand(object):
        def __init__(self, script, side_effect=False):
            self.script = script
            self.side_effect = side_effect
    show_corrected_command(CorrectedCommand('ls -l'))
    show_corrected_command(CorrectedCommand('ls -l', True))



# Generated at 2022-06-14 09:10:08.127045
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    import six
    from .conf import Configuration
    from .conf import get_shell_info
    from . import __version__
    from . import get_python_version
    configuration_details = Configuration('-1', '-2', '-3', True)
    alias_name = 'fuck'
    how_to_configure_alias(configuration_details)
    assert alias_name in six.text_type(sys.stdout.getvalue())



# Generated at 2022-06-14 09:10:09.285393
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:10:11.482339
# Unit test for function debug_time
def test_debug_time():
    with debug_time('Testing'):
        import time
        time.sleep(0.1)

# Generated at 2022-06-14 09:10:19.245506
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from . import __version__
    how_to_configure_alias('Seems like fuck alias isn\'t configured!\n'
                           'Please put \'eval $(thefuck --alias)\' in your '
                           '~/.bashrc and apply changes with \'exec $SHELL\' '
                           'or restart your shell.\n'
                           'Or run fuck a second time to configure it '
                           'automatically.\n'
                           'More details - https://github.com/nvbn/thefuck#manual-installation')


# Generated at 2022-06-14 09:10:21.701250
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    assert how_to_configure_alias() == u'Seems like fuck alias isn\'t configured!'



# Generated at 2022-06-14 09:10:29.694751
# Unit test for function debug_time
def test_debug_time():
    from thefuck.utils import debug_time
    from datetime import datetime
    from thefuck import settings
    from contextlib import contextmanager
    settings.debug = True
    @contextmanager
    def wait(n):
        yield
    start = datetime.now()
    with debug_time('Test'):
        with wait(min(settings.check_time, 1)):
            pass
    wait_time = datetime.now() - start
    assert wait_time.seconds < 3

# Generated at 2022-06-14 09:10:30.442133
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)

# Generated at 2022-06-14 09:10:31.200853
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass


# Generated at 2022-06-14 09:10:40.366916
# Unit test for function debug
def test_debug():
    import pytest
    from thefuck.utils import debug
    from thefuck.utils import settings

    with pytest.raises(SystemExit) as excinfo:
        debug('')

    assert excinfo.value.code == 0

    with pytest.raises(SystemExit) as excinfo:
        debug('test debug message')

    assert excinfo.value.code == 0

    with pytest.raises(SystemExit) as excinfo:
        debug('test debug message')

    assert excinfo.value.code == 0



# Generated at 2022-06-14 09:10:49.925991
# Unit test for function debug_time
def test_debug_time():
    from mock import Mock, call
    debug = Mock()
    with debug_time('some message', debug=debug):
        pass
    debug.assert_called_with(any_str_with('some message took: '))



# Generated at 2022-06-14 09:10:51.591124
# Unit test for function debug_time
def test_debug_time():
    with debug_time("Debug time test"):
        print("Executed with debug time")

# Generated at 2022-06-14 09:10:53.498390
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text('test') == None



# Generated at 2022-06-14 09:10:59.636680
# Unit test for function debug
def test_debug():
    from _io import StringIO
    try:
        out = StringIO()
        sys.stderr = out
        debug(u'All your base are belong to us')
        assert u'DEBUG: All your base are belong to us\n' in out.getvalue()
    finally:
        sys.stderr = sys.__stderr__

# Generated at 2022-06-14 09:11:00.723070
# Unit test for function debug_time
def test_debug_time():
    print("test")

# Generated at 2022-06-14 09:11:08.050466
# Unit test for function confirm_text
def test_confirm_text():
    from .utils import TempHomeDirectory
    from .shells import Shell
    from . import const

    shell = Shell()

    with TempHomeDirectory() as temp_home_directory:
        if shell.app_alias:
            assert confirm_text(shell.app_alias) == const.USER_COMMAND_MARK + \
                                                    shell.app_alias.script + \
                                                    ' (+side effect)' + \
                                                    ' [enter/↑/↓/ctrl+c]'

# Generated at 2022-06-14 09:11:09.360568
# Unit test for function debug_time
def test_debug_time():

    debug_time('hello')

# Generated at 2022-06-14 09:11:25.215070
# Unit test for function debug
def test_debug():
    import sys
    from StringIO import StringIO
    out = StringIO()
    _stdout = sys.stdout
    try:
        sys.stdout = out
        debug('test')
        debug('1234567890' * 8)
        assert out.getvalue() == (
            u'\x1b[34m\x1b[1mDEBUG:\x1b[0m test\n'
            u'\x1b[34m\x1b[1mDEBUG:\x1b[0m 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890\n') # noqa
    finally:
        sys.stdout = _stdout
        out.close()

# Generated at 2022-06-14 09:11:30.551570
# Unit test for function confirm_text
def test_confirm_text():
    from .application import ConfirmedCommand, ConfirmRule
    from .rule import Command
    rule = ConfirmRule(lambda *_: True)
    corrected_command = ConfirmedCommand(
        Command('test', ''), 'Yes', rule)

    confirm_text(corrected_command)

# Generated at 2022-06-14 09:11:37.790254
# Unit test for function debug
def test_debug():
    from mock import Mock

    settings.debug = True
    sys.stderr = Mock()
    debug(u'foo')
    sys.stderr.write.assert_called_once_with(
        u'\033[34m\033[1mDEBUG:\033[0m foo\n')

    settings.debug = False
    sys.stderr = Mock()
    debug(u'bar')
    sys.stderr.write.assert_not_called()

# Generated at 2022-06-14 09:11:50.390462
# Unit test for function debug_time
def test_debug_time():
    msg = "Debug message"
    print("Testing debug_time()")
    debug_time(msg)
    assert debug(msg) == None

# Generated at 2022-06-14 09:11:52.867845
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        import time
        time.sleep(1)
        assert True

# Generated at 2022-06-14 09:11:57.780527
# Unit test for function debug
def test_debug():
    old_stderr = sys.stderr
    try:
        sys.stderr = sys.stdout
        settings.debug = True
        debug('Hello World')
        settings.no_colors = True
        debug('Hello World')
    finally:
        sys.stderr = old_stderr

# Generated at 2022-06-14 09:12:01.967323
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    from contextlib import contextmanager

    @contextmanager
    def time_delta(delta):
        started = datetime.now()
        try:
            yield
        finally:
            delta.append(datetime.now() - started)


# Generated at 2022-06-14 09:12:10.701891
# Unit test for function color
def test_color():
    colorama.init()
    assert color(colorama.Back.RED + colorama.Fore.WHITE +
                 colorama.Style.BRIGHT) == colorama.Back.RED + \
        colorama.Fore.WHITE + colorama.Style.BRIGHT
    settings.no_colors = True
    assert color(colorama.Back.RED + colorama.Fore.WHITE +
                 colorama.Style.BRIGHT) == ''

# Generated at 2022-06-14 09:12:19.819947
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    import mock

    with mock.patch('thefuck.log.datetime') as m_datetime:
        m_datetime.now = mock.MagicMock(return_value=timedelta(seconds=42))
        with debug_time('foo'):
            pass
        m_datetime.now = mock.MagicMock(return_value=timedelta(seconds=44))
    assert mock.call('foo took: 0:00:02') in m_datetime.mock_calls



# Generated at 2022-06-14 09:12:23.530755
# Unit test for function show_corrected_command
def test_show_corrected_command():
    assert(show_corrected_command("/bin/ls") == None)

# Unit test fot function confirm_text

# Generated at 2022-06-14 09:12:24.774571
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:12:31.768774
# Unit test for function debug_time
def test_debug_time():
    from mock import Mock
    from datetime import timedelta

    with Mock() as mock:
        with debug_time('msg'):
            pass

    assert mock.debug.call_count == 1
    assert 'msg' in mock.debug.call_args[0][0]
    assert 'took' in mock.debug.call_args[0][0]
    assert isinstance(mock.debug.call_args[0][0].split(' ')[3],
                      str)

# Generated at 2022-06-14 09:12:35.074018
# Unit test for function show_corrected_command
def test_show_corrected_command():
    command="git push origin master"
    corrected_command = Command(command, script="git pull")
    show_corrected_command(corrected_command)
    assert command == corrected_command.script


# Generated at 2022-06-14 09:12:47.224449
# Unit test for function color
def test_color():
    assert color('foo') == 'foo'
    assert color('foo') == ''

# Generated at 2022-06-14 09:12:48.490331
# Unit test for function show_corrected_command
def test_show_corrected_command():
    assert show_corrected_command() == None

# Generated at 2022-06-14 09:12:50.078287
# Unit test for function debug_time
def test_debug_time():
    msg = 'msg'
    with debug_time(msg) as time:
        time = time

# Generated at 2022-06-14 09:12:51.218418
# Unit test for function debug_time
def test_debug_time():
    with debug_time('Hello'):
        assert 1

# Generated at 2022-06-14 09:13:01.690630
# Unit test for function debug_time
def test_debug_time():
    from mock import patch

    with patch('datetime.datetime') as mock_datetime, \
            patch('thefuck.shells.base.sys') as mock_sys:
        mock_datetime.now.side_effect = [
            datetime(year=1970, month=1, day=1, hour=1),
            datetime(year=1970, month=1, day=1, hour=2)]
        with debug_time('test'):
            pass
        mock_sys.stderr.write.assert_called_once_with(
            '\033[34m\033[1mDEBUG:\033[0m test took: 1:00:00\n')

# Generated at 2022-06-14 09:13:11.021980
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    import tempfile
    from .conf import ConfigurationDetails
    from .shells.bash import Bash
    from .shells.zsh import Zsh
    from .shells.fish import Fish
    from .shells.powershell import Powershell
    bash = Bash()
    zsh = Zsh()
    fish = Fish()
    ps = Powershell()

    def test_for_shell(shell):
        with tempfile.NamedTemporaryFile() as temp_file:
            configuration_details = ConfigurationDetails(
                temp_file.name,
                shell.shell_config.format(temp_file.name),
                shell.reload_alias,
                True)
            how_to_configure_alias(configuration_details)

    for shell in (bash, zsh, fish):
        yield test_for_shell, shell

    configuration

# Generated at 2022-06-14 09:13:14.405316
# Unit test for function color
def test_color():
    assert color('\x1b[0;30;40m') == '\x1b[0;30;40m'
    colorama.init()
    assert color('\x1b[0;30;40m') == ''

# Generated at 2022-06-14 09:13:23.780479
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = const.CorrectedCommand(
        script='git commit -m "fix"',
        side_effect=False)
    show_corrected_command(corrected_command)
    assert sys.stderr.getvalue() == '{0}git commit -m "fix"\n'.format(
        const.USER_COMMAND_MARK)

    corrected_command_with_side_effect = const.CorrectedCommand(
        script='git commit -m "fix"',
        side_effect=True)
    show_corrected_command(corrected_command_with_side_effect)

# Generated at 2022-06-14 09:13:30.993864
# Unit test for function confirm_text
def test_confirm_text():

#   Enter confirmation
    sys.stdin.readline = lambda: '\n'

#   Down arrow
    sys.stdin.readline = lambda: '\x1b[B'

#   Up arrow
    sys.stdin.readline = lambda: '\x1b[A'

#   Ctrl+c
    sys.stdin.readline = lambda: '\x03'

# Generated at 2022-06-14 09:13:39.579965
# Unit test for function debug
def test_debug():
    # Setup
    assert not settings.debug
    line = u'foo'

    # Execute
    debug(line)

    # Assert
    assert settings.debug
    assert sys.stderr.getvalue() == ''

    # Setup
    settings.debug = True
    sys.stderr = StringIO()

    # Execute
    debug(line)

    # Assert
    expected = u'{blue}{bold}DEBUG:{reset} foo\n'.format(
        blue=color(colorama.Fore.BLUE),
        bold=color(colorama.Style.BRIGHT),
        reset=color(colorama.Style.RESET_ALL))
    actual = sys.stderr.getvalue()
    assert settings.debug
    assert expected == actual