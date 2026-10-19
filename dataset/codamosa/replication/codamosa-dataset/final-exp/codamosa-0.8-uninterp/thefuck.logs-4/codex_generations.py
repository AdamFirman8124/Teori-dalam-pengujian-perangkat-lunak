

# Generated at 2022-06-14 09:03:57.677025
# Unit test for function debug
def test_debug():
    import mock
    import StringIO
    stderr = sys.stderr
    output = StringIO.StringIO()
    sys.stderr = output
    with mock.patch('thefuck.shells.get_shell_info') as get_shell_info:
        get_shell_info.return_value = 'sh'
        version('', '', '')
    sys.stderr = stderr
    assert output.getvalue() == '\n'

# Generated at 2022-06-14 09:04:01.512564
# Unit test for function debug
def test_debug():
    func = debug
    try:
        func('test')
    except Exception as error:
        raise AssertionError('{} has thrown exception {}'.format(func, error))



# Generated at 2022-06-14 09:04:03.819423
# Unit test for function debug
def test_debug():
    from .conf import Settings

    settings = Settings()
    settings.debug = True
    debug('foo')



# Generated at 2022-06-14 09:04:12.267389
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text({'script': 'a; b', 'side_effect': True}) == (u'{prefix}{clear}{bold}a; b{reset} (+side effect) [{green}enter{reset}/{blue}↑{reset}/{blue}↓{reset}/{red}ctrl+c{reset}]').format(prefix=const.USER_COMMAND_MARK, clear='\033[1K\r', bold=color(colorama.Style.BRIGHT), green=color(colorama.Fore.GREEN), red=color(colorama.Fore.RED), reset=color(colorama.Style.RESET_ALL), blue=color(colorama.Fore.BLUE))

# Generated at 2022-06-14 09:04:15.487238
# Unit test for function debug_time
def test_debug_time():
    import time
    with debug_time('test_sleep'):
        time.sleep(1)

# Generated at 2022-06-14 09:04:27.695585
# Unit test for function debug_time
def test_debug_time():
    """
    It should print debug message with time of execution on exit from
    context manager.
    """
    from datetime import timedelta
    from mock import patch
    from thefuck.shells import _get_script_path
    _get_script_path.cache_clear()
    with patch('thefuck.shells._get_script_path', return_value='fuck'):
        with debug_time('test'):
            pass
    _get_script_path.cache_clear()
    with patch('thefuck.shells._get_script_path', return_value='fuck'):
        with patch('thefuck.utils.datetime') as mock_datetime:
            mock_datetime.now.return_value = 0
            with debug_time('test'):
                pass

# Generated at 2022-06-14 09:04:40.584969
# Unit test for function confirm_text
def test_confirm_text():
    result = confirm_text({'script': 'hello',
                                'side_effect': False})
    assert result == (
        (u'`hello` [enter/↑/↓/ctrl+c]')), "incorrect string"

    result = confirm_text({'script': 'hello',
                                'side_effect': True})
    assert result == (
        (u'`hello` (+side effect) [enter/↑/↓/ctrl+c]')), "incorrect string"

    result = confirm_text({'script': 'hello',
                                'side_effect': True,
                                'colored_script': 'hello'})
    assert result == (
        (u'`hello` (+side effect) [enter/↑/↓/ctrl+c]')), "incorrect string"

# Generated at 2022-06-14 09:04:48.299199
# Unit test for function debug
def test_debug():
    import StringIO
    new_io = StringIO.StringIO()
    sys.stderr = new_io
    debug('test')
    sys.stderr.seek(0)
    assert sys.stderr.read() == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m test\n'
    sys.stderr = sys.__stderr__

# Generated at 2022-06-14 09:04:50.657892
# Unit test for function debug
def test_debug():
    with debug_time('Test'):
        pass

# Generated at 2022-06-14 09:04:52.705863
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text('ls') == 'ls [enter/↑/↓/ctrl+c] '

# Generated at 2022-06-14 09:05:00.353074
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)
    how_to_configure_alias(const.ConfigurationDetails(False, '', '', ''))
    how_to_configure_alias(const.ConfigurationDetails(True, 'content',
                            'path', 'reload'))



# Generated at 2022-06-14 09:05:11.403153
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    print('Test for function how_to_configure_alias')
    print('How to configure without details:')
    how_to_configure_alias(None)
    print('How to configure with details:')
    from .utils import ConfigurationDetails
    how_to_configure_alias(ConfigurationDetails(
        can_configure_automatically='can_configure_automatically',
        path='path',
        reload='reload',
        content='content'
    ))

# Generated at 2022-06-14 09:05:16.984764
# Unit test for function show_corrected_command
def test_show_corrected_command():
    command = 'git helloworld'
    corrected_command = 'git help world'
    assert show_corrected_command(corrected_command) == '{}git helloworld (+side effect)\n'.format(const.USER_COMMAND_MARK)

# Generated at 2022-06-14 09:05:18.488632
# Unit test for function debug
def test_debug():
    debug('This is debug message')
    debug('This is other debug message')

# Generated at 2022-06-14 09:05:21.394627
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .shells import Shell

    command = Shell('', '', '').from_raw_script('ls')
    show_corrected_command(command)
    assert 'ls' in sys.stderr.getvalue()

# Generated at 2022-06-14 09:05:31.343701
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .shells.bash import Bash
    from .shell import Setting
    import mock

    settings = mock.Mock()
    settings.no_colors = False

    bash = Bash('/usr/bin/bash', settings)
    show_corrected_command(bash.from_shell(Setting(script='ls', side_effect=True)))
    assert '\r' not in sys.stderr.getvalue()
    assert '\033[1K\r' not in sys.stderr.getvalue()
    sys.stderr.truncate(0)

# Generated at 2022-06-14 09:05:34.190761
# Unit test for function show_corrected_command
def test_show_corrected_command():
    show_corrected_command('ls -alh') == 'ls -alh'



# Generated at 2022-06-14 09:05:37.114291
# Unit test for function color
def test_color():
    assert color(colorama.Fore.BLUE) == ''
    assert color(colorama.Fore.RED) == '\x1b[31m'

# Generated at 2022-06-14 09:05:46.423468
# Unit test for function debug
def test_debug():
    from mock import patch

    with patch('sys.stderr') as stderr:
        debug('none')
        assert not stderr.write.called

        settings.debug = True
        debug('debug')
        stderr.write.assert_called_with('\x1b[34m\x1b[1mDEBUG:\x1b[0m debug\n')

        settings.no_colors = True
        debug('no colors')
        stderr.write.assert_called_with('DEBUG: no colors\n')

# Generated at 2022-06-14 09:05:49.292835
# Unit test for function color
def test_color():
    assert color('green') == 'green'
    settings.no_colors = True
    assert color('green') == ''

# Generated at 2022-06-14 09:05:56.652330
# Unit test for function confirm_text
def test_confirm_text():
    from .conf import settings
    settings.no_colors = False
    show_corrected_command('corrected_command')
    confirm_text('corrected_command')



# Generated at 2022-06-14 09:05:59.745486
# Unit test for function color
def test_color():
    assert color(colorama.Fore.RED) == '\033[31m'
    colorama.init()
    settings.no_colors = True
    assert color(colorama.Fore.RED) == ''

# Generated at 2022-06-14 09:06:07.904187
# Unit test for function debug_time
def test_debug_time():
    with debug_time("testing1"):
        a=1
        b=2
        c=a+b
    with debug_time("testing2"):
        a=1
        b=2
        c=a+b
    with debug_time("testing3"):
        a=1
        b=2
        c=a+b
    with debug_time("testing4"):
        a=1
        b=2
        c=a+b

# Generated at 2022-06-14 09:06:11.698144
# Unit test for function debug_time
def test_debug_time():
    with debug_time('first'):
        with debug_time('second'):
            with debug_time('third'):
                pass

# Generated at 2022-06-14 09:06:12.872701
# Unit test for function show_corrected_command
def test_show_corrected_command():
    pass


# Generated at 2022-06-14 09:06:20.869247
# Unit test for function confirm_text
def test_confirm_text():
    import os
    correct_command = u'fuck cd'
    correct_output = (u'[fuck] cd '
        '[\x1b[32menter\x1b[39m/\x1b[34m↑\x1b[39m/\x1b[34m↓\x1b[39m/\x1b[31mctrl+c\x1b[39m]')
    assert confirm_text(correct_command) == correct_output

# Generated at 2022-06-14 09:06:26.168640
# Unit test for function debug
def test_debug():
    debug('test')
    with debug_time('dummy_context_manager'):
        pass

# Generated at 2022-06-14 09:06:31.353360
# Unit test for function debug
def test_debug():
    import sys

    def get_debug_output():
        saved_stderr = sys.stderr
        try:
            from cStringIO import StringIO
            sys.stderr = StringIO()
            debug('test message')
            return sys.stderr.getvalue()
        finally:
            sys.stderr = saved_stderr

    debug_output = get_debug_output()

    assert 'test message' in debug_output

# Generated at 2022-06-14 09:06:35.493823
# Unit test for function debug
def test_debug():
    expected_text = u"DEBUG: test message\n"
    captured_output = io.StringIO()
    sys.stderr = captured_output
    debug(u"test message")
    actual_output = captured_output.getvalue()
    sys.stderr = sys.__stderr__
    assert actual_output == expected_text




# Generated at 2022-06-14 09:06:45.671793
# Unit test for function show_corrected_command
def test_show_corrected_command():
    mocked_stderr = mock.Mock()
    with mock.patch.object(sys, 'stderr', mocked_stderr):
        command = Command('foo', 'bar')
        show_corrected_command(command)
        mocked_stderr.write.assert_called_with(
            u'{}foo {b}{}{reset}\n'.format(const.USER_COMMAND_MARK,
                                           command.side_effect or '',
                                           b=color('\033[1m'),
                                           reset=color('\033[0m')))



# Generated at 2022-06-14 09:07:01.300355
# Unit test for function confirm_text
def test_confirm_text():
    sys.stderr.write(
        (u'{prefix}{clear}{bold}{script}{reset}{side_effect} '
         u'[{green}enter{reset}/{blue}↑{reset}/{blue}↓{reset}'
         u'/{red}ctrl+c{reset}]').format(
            prefix='$',
            script=u'ls',
            side_effect=' (+side effect)' if True else '',
            clear='\033[1K\r',
            bold=color(colorama.Style.BRIGHT),
            green=color(colorama.Fore.GREEN),
            red=color(colorama.Fore.RED),
            reset=color(colorama.Style.RESET_ALL),
            blue=color(colorama.Fore.BLUE)))
# End of confirm_text unit test

# Generated at 2022-06-14 09:07:03.190226
# Unit test for function debug_time
def test_debug_time():
    debug(u'test_debug_time')

# Generated at 2022-06-14 09:07:05.453804
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias()

# Generated at 2022-06-14 09:07:17.853735
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .correct import CorrectedCommand
    from StringIO import StringIO
    import sys
    old_stdout, sys.stdout = sys.stdout, StringIO()
    SHOW_CORRECTED_COMMAND = show_corrected_command(
        CorrectedCommand(u'git log', True))
    SHOW_CORRECTED_COMMAND
    assert sys.stdout.getvalue() == u'git log (+side effect)\n'
    SHOW_CORRECTED_COMMAND = show_corrected_command(
        CorrectedCommand(u'git log', False))
    SHOW_CORRECTED_COMMAND
    assert sys.stdout.getvalue() == u'git log\n'
    sys.stdout = old_stdout

# Generated at 2022-06-14 09:07:18.681191
# Unit test for function show_corrected_command
def test_show_corrected_command():
    show_corrected_command(corrected_command)

# Generated at 2022-06-14 09:07:20.936486
# Unit test for function show_corrected_command
def test_show_corrected_command():
    show_corrected_command('corrected_command.script')
    show_corrected_command('corrected_command.side_effect')

# Generated at 2022-06-14 09:07:26.913031
# Unit test for function show_corrected_command
def test_show_corrected_command():
    sys.stderr = open('test_show_corrected_command.log', 'w')
    settings.no_colors = True
    show_corrected_command('alskdfjas')
    show_corrected_command('ls -t')
    settings.no_colors = False
    show_corrected_command('ls -t')


# Generated at 2022-06-14 09:07:28.222738
# Unit test for function debug
def test_debug():
    debug('HERE')


# Generated at 2022-06-14 09:07:29.555784
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:07:34.605733
# Unit test for function debug_time
def test_debug_time():
    import mock
    with mock.patch('sys.stderr') as out:
        with debug_time('foo'):
            pass
        debug_time(None)
    assert out.write.call_args_list[0][0][0].endswith('DEBUG: foo')

# Generated at 2022-06-14 09:07:45.261409
# Unit test for function debug
def test_debug():
    # Method should do nothing if debug option is false.
    with debug_time('test'):
        settings.debug = False
        debug('test')
    assert True

    # Method should do nothing if debug option is false.
    settings.debug = True
    debug('test')
    assert True

# Generated at 2022-06-14 09:07:46.984243
# Unit test for function show_corrected_command
def test_show_corrected_command():
    show_corrected_command("echo asdf")


# Generated at 2022-06-14 09:07:55.135938
# Unit test for function debug
def test_debug():
    strings = []
    sys.stderr.write = strings.append

    settings.debug = True
    debug('test 1')
    assert len(strings) == 1
    assert u'\033[94m\033[1mDEBUG:\033[0m test 1\n' == strings[0]

    settings.debug = False
    strings.pop()
    debug('test 2')
    assert len(strings) == 0



# Generated at 2022-06-14 09:08:01.097571
# Unit test for function debug
def test_debug():
    from mock import mock_open, patch
    with patch('sys.stderr', mock_open()) as mock_obj:
        debug('bar')
    mock_obj.write.assert_called_with(u'\x1b[34m\x1b[1mDEBUG:\x1b[0m bar\n')


# Generated at 2022-06-14 09:08:13.309384
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from thefuck.types import Command
    import re

    origin_command = Command('ls', 'ls -l', '', '', '', 'ls -l')
    corrected_command = Command('ls', 'ls -la', 'ls -la', '', '', 'ls -a')
    show_corrected_command(corrected_command)

    expected_output = u'{prefix}{bold}{script}{reset}{side_effect}\n'.format(
        prefix=const.USER_COMMAND_MARK,
        script=corrected_command.script,
        side_effect=u' (+side effect)' if corrected_command.side_effect else u'',
        bold=color(colorama.Style.BRIGHT),
        reset=color(colorama.Style.RESET_ALL))


# Generated at 2022-06-14 09:08:18.112756
# Unit test for function debug
def test_debug():
    # Test default case
    sys.stderr = FakeStderr()
    debug('test')
    assert sys.stderr.called == u'DEBUG: test\n'
    # Test no_colors case
    settings.no_colors = True
    debug('test')
    assert sys.stderr.called == u'DEBUG: test\n'

# Generated at 2022-06-14 09:08:30.202970
# Unit test for function confirm_text
def test_confirm_text():
    from colorama import Fore
    from thefuck.utils import ConfirmedCommand

    script = 'sudo !!'
    side_effect=False

    confirmed_command = ConfirmedCommand(script, side_effect)


# Generated at 2022-06-14 09:08:33.789532
# Unit test for function debug
def test_debug():
    from mock import patch
    with patch('thefuck.shells.terminal.sys.stderr') as stderr:
        debug(u'foo')
        assert stderr.write.called

# Generated at 2022-06-14 09:08:39.144397
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)
    how_to_configure_alias(1)
    how_to_configure_alias("2")
    how_to_configure_alias({})
    how_to_configure_alias({'path': 'zshrc', 'content': 'zsh content'})
    configuration_list = {'path': 'zshrc', 'content': 'zsh content', 'reload': 'zsh'}
    how_to_configure_alias(configuration_list)

# Generated at 2022-06-14 09:08:41.844738
# Unit test for function debug
def test_debug():
    with debug_time('message'):
        pass



# Generated at 2022-06-14 09:08:50.829547
# Unit test for function show_corrected_command
def test_show_corrected_command():
    """
    input: show_corrected_command("1 + 1")
    output: ['!!! 1 + 1\n']
    """
    assert show_corrected_command("1 + 1") == ['!!! 1 + 1\n']


# Generated at 2022-06-14 09:08:55.571861
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from colorama import Fore
    config_details = {'bold': Fore.BLACK,
                      'reset': Fore.RESET,
                      'content': 'export alias fuck=\'eval $(thefuck $(fc -ln -1)); history -r\').',
                      'path': '~/.bashrc',
                      'reload': 'source ~/.bashrc'}
    configuration_details = namedtuple('config_details', '')
    how_to_configure_alias(configuration_details)



# Generated at 2022-06-14 09:08:59.826927
# Unit test for function debug_time
def test_debug_time():
    import mock
    mock = mock.Mock()

    def my_function():
        mock()

    with debug_time('my test'):
        my_function()

    assert mock.call_count == 1

# Generated at 2022-06-14 09:09:12.495248
# Unit test for function confirm_text
def test_confirm_text():
    from thefuck.utils import confirm_text
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

    with captured_output() as (out, err):
        confirm_text('command')

    assert out.getvalue() == '> command [enter/↑/↓/ctrl+c]> '



# Generated at 2022-06-14 09:09:26.195663
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from thefuck.shells import GnuShell
    from thefuck import conf
    from thefuck.conf import assert_conf, Settings
    conf.settings = Settings(no_colors=False, require_confirmation=False, priority=1000,
                             wait_command=0, slow_commands='', rules=[], exclude_rules=[],
                             wait_slow_command=15, history_limit=None,
                             alias='fuck', shell=GnuShell())


# Generated at 2022-06-14 09:09:40.117857
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from thefuck.rules.git import get_new_command
    assert u'git br' in get_new_command('git br', None)
    assert u'git branch' in get_new_command('git branch', None)
    assert u'git branch' in get_new_command('git branch 1', None)
    assert u'git branch -v' in get_new_command('git branch -v', None)
    assert u'git branch -v' in get_new_command('git branch -v 1', None)
    assert u'git branch -vv' in get_new_command('git branch -vv', None)
    assert u'git branch -vv' in get_new_command('git branch -vv 1', None)
    assert u'git branch --color' in get_new_command('git branch --color', None)
   

# Generated at 2022-06-14 09:09:43.524253
# Unit test for function show_corrected_command
def test_show_corrected_command():
    show_corrected_command({'script': 'test', 'side_effect': True})
    show_corrected_command({'script': 'test', 'side_effect': False})


# Generated at 2022-06-14 09:09:44.659023
# Unit test for function debug
def test_debug():
    assert debug('string') == None

# Generated at 2022-06-14 09:09:49.004203
# Unit test for function debug_time
def test_debug_time():
    logger = list()
    with debug_time('test'):
        for i in xrange(1000):
            logger.append(i)
    assert 'test took' in logger

# Generated at 2022-06-14 09:10:00.566330
# Unit test for function debug_time
def test_debug_time():
    from . import debug
    from datetime import datetime, timedelta
    from time import sleep
    from contextlib import contextmanager

    _debug = debug.debug
    _debug_time = debug.debug_time

    def debug(msg):
        print(msg)

    @contextmanager
    def debug_time(msg):
        started = datetime.now()
        try:
            yield
        finally:
            debug('{} took: {}'.format(msg, datetime.now() - started))

    try:
        debug('Debug 1!')
        with debug_time('Debug time 1'):
            sleep(1.1)
        debug('Debug 2!')
        with debug_time('Debug time 2'):
            sleep(0.9)
    finally:
        debug.debug = _debug

# Generated at 2022-06-14 09:10:16.342148
# Unit test for function confirm_text
def test_confirm_text():
    from StringIO import StringIO
    import sys
    import subprocess
    from thefuck.main import confirm_text

    #Backup sys.stdout and sys.stderr
    stdout_bak = sys.stdout
    stderr_bak = sys.stderr

    #Start test
    sys.stdout = StringIO()
    sys.stderr = StringIO()
    confirm_text('echo "Hello World!"')

# Generated at 2022-06-14 09:10:29.137470
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from thefuck.shells import Shell
    from thefuck.types import CorrectedCommand, Command

    command = Command(script='ls', stderr='abc')
    corrected_command = CorrectedCommand(script='ls -la', side_effect=False)
    shell = Shell(Command())

    sys.stderr = MagicMock()
    show_corrected_command(corrected_command)
    sys.stderr.write.assert_called_once_with(
        u'{prefix}{bold}{script}{reset}\n'.format(
            prefix=const.USER_COMMAND_MARK,
            script=corrected_command.script,
            bold=color(colorama.Style.BRIGHT),
            reset=color(colorama.Style.RESET_ALL)))



# Generated at 2022-06-14 09:10:31.010448
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text('ls') == 'ls'


# Generated at 2022-06-14 09:10:33.236961
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text(u'ls') == u'Fuck(ls) [enter/↑/↓/ctrl+c]'

# Generated at 2022-06-14 09:10:42.949211
# Unit test for function debug
def test_debug():
    import StringIO
    from mock import patch
    out = StringIO.StringIO()

    def reset():
        sys.stderr = out

    with patch(
            'sys.stderr', out):
        debug('test1')
        assert '\033[2m\033[34mDEBUG:\033[0m test1\n' == out.getvalue()
        out.truncate(0)
        settings.debug = False
        debug('test2')
        assert '' == out.getvalue()

# Generated at 2022-06-14 09:10:43.867284
# Unit test for function debug
def test_debug():
    debug('debug msg')

# Generated at 2022-06-14 09:10:53.840315
# Unit test for function debug_time
def test_debug_time():
    from test.utils import patch
    from test.lib import target

    with patch.object(sys.stderr, 'write') as write:
        with debug_time('foo'):
            pass
        assert write.call_count == 1
        assert 'foo took' in write.call_args[0][0]

    with patch.object(sys.stderr, 'write') as write:
        with debug_time('foo'):
            raise Exception('bar')
        assert write.call_count == 2
        # First call was from debug_time
        assert 'foo took' in write.call_args[0][0]
        # Second call was from exception
        assert 'bar' in write.call_args[0][0]

# Generated at 2022-06-14 09:10:59.968393
# Unit test for function show_corrected_command
def test_show_corrected_command():
    assert show_corrected_command(CorrectedCommand(script='echo "Hello"',
                                                   side_effect=False)) == \
        '{prefix}{script}{side_effect}\n'.format(
            prefix=const.USER_COMMAND_MARK,
            script='echo "Hello"',
            side_effect='')

# Generated at 2022-06-14 09:11:10.499168
# Unit test for function debug
def test_debug():
    from mock import patch, mock_open
    from six.moves import StringIO
    import sys

    with patch('thefuck.shells.enable_colors') as enable_colors:
        enable_colors.return_value = False
        with patch('thefuck.log.settings', debug=True):
            with patch('thefuck.log.open', mock_open(), create=True):
                debug(u'test-debug-msg')

    with patch('thefuck.shells.enable_colors') as enable_colors:
        enable_colors.return_value = True
        with patch('thefuck.log.settings', debug=True):
            with patch('thefuck.log.open', mock_open(), create=True):
                debug(u'test-debug-msg')

    # out_file should be opened only once


# Generated at 2022-06-14 09:11:12.803889
# Unit test for function confirm_text
def test_confirm_text():
    confirmed_command = 'thefuck --version'
    confirm_text(confirmed_command)



# Generated at 2022-06-14 09:11:22.902765
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from tempfile import NamedTemporaryFile
    from subprocess import Popen, PIPE
    with NamedTemporaryFile(mode='wt') as stdout:
        with NamedTemporaryFile(mode='wt') as stderr:
            p = Popen(['thefuck', '--shell', 'sh', '-l', 'python -c exit'],
                      stdout=stdout, stderr=stderr)
            p.wait()
            stdout.flush()
            stderr.flush()
            if p.returncode == 0:
                print('Error in test_show_corrected_command: return code is {}'
                      .format(p.returncode))
                return
            with open(stderr.name) as f:
                print(f.read())

# Generated at 2022-06-14 09:11:28.268926
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = Command('ls', side_effect=True)
    confirm_text(corrected_command)
    assert sys.stderr.read() == ('[ls (+side effect)]'
                                 '[\033[32;1menter\033[0m/\033[34;1m\u2191\033[0m/'
                                 '\033[34;1m\u2193\033[0m/\033[31;1mctrl+c\033[0m]')

# Generated at 2022-06-14 09:11:33.401382
# Unit test for function debug_time
def test_debug_time():
    import mock
    import time

    with mock.patch('thefuck.shells.base.debug') as debug:
        with debug_time('msg'):
            time.sleep(0.01)
            debug.assert_called_once_with('msg took: 0:00:00.010013')

# Generated at 2022-06-14 09:11:38.391958
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = const.Command('ls', 'ls -la', 'ls -la')
    show_corrected_command(corrected_command)


if __name__ == '__main__':
    test_show_corrected_command()

# Generated at 2022-06-14 09:11:43.787522
# Unit test for function debug
def test_debug():
    from StringIO import StringIO
    saved_stderr = sys.stderr
    try:
        out = StringIO()
        sys.stderr = out
        debug(u'Test message')
        assert out.getvalue() == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m Test message\n'
    finally:
        sys.stderr = saved_stderr

# Generated at 2022-06-14 09:11:47.381376
# Unit test for function confirm_text
def test_confirm_text():
    from .shells import Shell
    from .rule import CorrectedCommand

    corrected_command = CorrectedCommand('foo', '')
    confirm_text(corrected_command)

# Generated at 2022-06-14 09:11:49.842835
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text(corrected_command=object) == confirm_text(corrected_command=object)

# Generated at 2022-06-14 09:11:52.805468
# Unit test for function color
def test_color():
    assert color(u'foo') == u'foo'
    settings.no_colors = True
    assert color(u'foo') == u''

# Generated at 2022-06-14 09:11:54.571521
# Unit test for function debug
def test_debug():
    debug('test')
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:11:56.374281
# Unit test for function debug
def test_debug():
    assert not settings.debug
    debug('foo')


settings.debug = True



# Generated at 2022-06-14 09:12:06.204016
# Unit test for function confirm_text
def test_confirm_text():
    ans = confirm_text("mv 1.jpg 2.jpg")
    if ans is not None:
        assert ans == "mv 1.jpg 2.jpg"

# Generated at 2022-06-14 09:12:12.932054
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .command import Command
    from datetime import datetime
    correct_command = Command('ls', datetime(2015, 8, 21, 1, 38, 42))
    correct_command.side_effect = True
    show_corrected_command(correct_command)
    assert sys.stderr.getvalue() == 'Corrected:\n' \
                                    'ls (+side effect) \n' \
                                    '----------------------------\n'


# Generated at 2022-06-14 09:12:19.835779
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    for details in [None,
                    const.ConfigurationDetails('path', 'content', 'reload', True)]:

        def get_output_from_function(function):
            import StringIO
            old_stdout = sys.stdout
            sys.stdout = mystdout = StringIO.StringIO()
            function(details)
            sys.stdout = old_stdout
            return mystdout.getvalue().splitlines()

        output = get_output_from_function(how_to_configure_alias)
        assert output[0] == (
            "Seems like {bold}fuck{reset} alias isn't configured!".format(
                bold=color(colorama.Style.BRIGHT),
                reset=color(colorama.Style.RESET_ALL)))


# Generated at 2022-06-14 09:12:28.073735
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)
    how_to_configure_alias(object)
    how_to_configure_alias('')
    how_to_configure_alias(1)
    how_to_configure_alias(0)
    how_to_configure_alias(False)
    how_to_configure_alias([])
    how_to_configure_alias({})



# Generated at 2022-06-14 09:12:31.543753
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from thefuck.types import Command
    import colorama
    colorama.init()
    show_corrected_command(Command('pwd', 'cd /home/user', True))
    colorama.deinit()

# Generated at 2022-06-14 09:12:41.501222
# Unit test for function confirm_text
def test_confirm_text():
    from click.testing import CliRunner
    import os
    import subprocess
    from .main import main
    from .rules.python import match, get_new_command

    runner = CliRunner()
    ls = subprocess.check_output("which ls", shell=True).strip()
    with runner.isolated_filesystem():
        with open("data.txt", "w") as f:
            f.write("data")
        with open("test.txt", "w") as f:
            f.write("test")
        result = runner.invoke(main, ['ls data.txt', ls],
                               input='\n\n\n\n',
                               env={'LANG': 'C'})
        assert result.exit_code == 0
        assert match(Command('ls data.txt', ''), None)

# Generated at 2022-06-14 09:12:45.709696
# Unit test for function confirm_text
def test_confirm_text():
    # This use unicode character as up arrow.
    encoded_str = confirm_text(
        namedtuple('Command', ['script', 'side_effect'])(u'echo "test"', False)
    )
    assert '↑' in encoded_str

# Generated at 2022-06-14 09:12:57.326949
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .rules.utils import ConfigurationDetails
    from . import const
    import re
    import sys
    import os

    def should_contain(content, pattern):
        assert re.search(pattern, content)

    def should_be(content, pattern):
        assert re.search(pattern, content)
        assert len(re.findall(pattern, content)) == 1

    assert sys.stdout.isatty()

    config = ConfigurationDetails('.bashrc', 'stoit', 'waiting')

    assert const.ETC_DIR.mkdir()

    with open(const.ETC_DIR / 'fuck', 'w') as rc_file:
        rc_file.write('export SHELL=/bin/bash')

    assert os.path.exists(const.ETC_DIR / 'fuck')

    how_to_configure

# Generated at 2022-06-14 09:13:05.575596
# Unit test for function debug
def test_debug():
    with open(".debug.log", "w") as debug_file:
        debug_file_backup = sys.stderr
        sys.stderr = debug_file
        debug("TEST")
        sys.stderr = debug_file_backup
    with open(".debug.log", "r") as debug_file:
        content = debug_file.read()
    assert content == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m TEST\n'

# Generated at 2022-06-14 09:13:11.343916
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug(u'foo')
    assert sys.stderr.getvalue() == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m foo\n'

# Generated at 2022-06-14 09:13:20.352483
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass
    # Check output:
    assert sys.stderr.write.called

# Generated at 2022-06-14 09:13:31.452040
# Unit test for function debug
def test_debug():
    import mock
    import thefuck.utils

    with mock.patch.object(thefuck.utils.settings, 'debug', True):
        with mock.patch('sys.stderr') as stderr:
            thefuck.utils.debug('42')
            stderr.write.assert_called_with(u'\x1b[34m\x1b[1mDEBUG:\x1b[0m 42\n')

    with mock.patch.object(thefuck.utils.settings, 'debug', False):
        with mock.patch('sys.stderr') as stderr:
            thefuck.utils.debug('42')
            assert not stderr.write.called

# Generated at 2022-06-14 09:13:35.334538
# Unit test for function debug_time
def test_debug_time():
    try:
        import time
        with debug_time('Test'):
            time.sleep(0.5)
    except AssertionError:
        raise Exception('Please use --debug option to run this test.')

# Generated at 2022-06-14 09:13:45.347139
# Unit test for function show_corrected_command
def test_show_corrected_command():
    sys.stderr.write('\n\nTesting show_corrected_command function\n')
    sys.stderr.write('-----------------------------------------\n')
    sys.stderr.write('This is the expected output: \n')
    sys.stderr.write('$  ls -la \n')
    show_corrected_command('ls -la')
    sys.stderr.write('$  ls -la (+side effect) \n')
    show_corrected_command('ls -la', ' (+side effect)')
    sys.stderr.write('-----------------------------------------\n')
    sys.stderr.write('\n')
