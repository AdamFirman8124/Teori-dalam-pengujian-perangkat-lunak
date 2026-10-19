

# Generated at 2022-06-14 09:03:56.638982
# Unit test for function debug
def test_debug():
    assert debug(u'Hello') == None

# Generated at 2022-06-14 09:03:59.661198
# Unit test for function confirm_text
def test_confirm_text():
    import StringIO
    sys.stderr = StringIO.StringIO()
    confirm_text(None)
    sys.stderr.close()

# Generated at 2022-06-14 09:04:04.386088
# Unit test for function confirm_text
def test_confirm_text():
    from .shells.expect import Expect

    expect = Expect(re.compile('^corrected:'))
    expect.sendline('corrected: command')
    assert expect.before == const.USER_COMMAND_MARK + 'corrected: command'



# Generated at 2022-06-14 09:04:07.390466
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text(
        CorrectedCommand('ls', 'll', False)) == confirm_text(
        CorrectedCommand('ls', 'll', False))

# Generated at 2022-06-14 09:04:13.154457
# Unit test for function debug_time
def test_debug_time():
    from contextlib import contextmanager
    import mock
    import time
    from thefuck.shells import _get_shell_info

    with mock.patch('thefuck.shells.subprocess') as subprocess:
        with contextmanager() as m:
            subprocess.check_output().decode.return_value = 'bash'
            with debug_time("{} initialized".format(_get_shell_info())):
                time.sleep(10)
            assert m.called

# Generated at 2022-06-14 09:04:25.256054
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .command import Command
    from .rule import Rule
    from .types import CorrectedCommand
    from .utils import wrap_colorama_streams
    from unittest import TestCase, main, mock
    from io import StringIO
    from tempfile import TemporaryDirectory

    class ShowCorrectedCommandTest(TestCase):
        def setUp(self):
            self.stderr = StringIO()
            wrap_colorama_streams(self.stderr, self.stderr, self.stderr)
            sys.stderr = self.stderr
            self.stdout = StringIO()
            sys.stdout = self.stdout


# Generated at 2022-06-14 09:04:31.195275
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from . import types
    from .shells import Bash
    from .utils import which
    import os

    # create a shell instance
    bash = Bash()

    # use bash to retrieve the current user's shell config
    configs = bash.shell_config()

    # set the user's shell config in the settings
    settings.which = which
    settings.shell = configs.shell
    settings.aliases = configs.aliases

    # give the function the command we want to show
    corrected_command = types.CorrectedCommand('ls', None, True)
    show_corrected_command(corrected_command)

    # get the terminal size and set it in settings so that the log can
    # dynamically adapt to different terminal sizes

# Generated at 2022-06-14 09:04:40.585308
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text('test_command') ==\
        u'{prefix}test_command [{green}enter{reset}/{blue}↑{reset}/{blue}↓{reset}/{red}ctrl+c{reset}]'.format(
            green=color(colorama.Fore.GREEN),
            red=color(colorama.Fore.RED),
            blue=color(colorama.Fore.BLUE),
            reset=color(colorama.Style.RESET_ALL),
            prefix=const.USER_COMMAND_MARK)

# Generated at 2022-06-14 09:04:43.962985
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = 'git push'
    show_corrected_command(corrected_command)

# Generated at 2022-06-14 09:04:59.702888
# Unit test for function debug
def test_debug():
    from unittest import TestCase
    from cStringIO import StringIO
    from contextlib import contextmanager
    from .conf import settings

    class DebugTestCase(TestCase):
        @contextmanager
        def assert_debug(self, expected):
            settings.debug = True
            log = StringIO()
            old_stderr = sys.stderr
            try:
                sys.stderr = log
                yield
                self.assertEqual(log.getvalue().strip(), expected)
            finally:
                settings.debug = False
                log.close()
                sys.stderr = old_stderr

        def test_debug(self):
            with self.assert_debug(u'debug'):
                debug(u'debug')

    return DebugTestCase



# Generated at 2022-06-14 09:05:05.011755
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from tests.mocks import Command

    show_corrected_command(Command('ls', ''))
    show_corrected_command(Command('ls', '', side_effect=True))

# Generated at 2022-06-14 09:05:06.098284
# Unit test for function debug
def test_debug():
    assert debug(__name__)

# Generated at 2022-06-14 09:05:09.477405
# Unit test for function show_corrected_command
def test_show_corrected_command():
    assert(show_corrected_command(u'test') == ' > test\n')


# Generated at 2022-06-14 09:05:21.651956
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from pytest import approx

    import thefuck
    from thefuck.shells.bash import Bash
    from thefuck.shells.zsh import Zsh
    from thefuck.shells.fish import Fish

    bash = Bash()
    zsh = Zsh()
    fish = Fish()

    # TODO:
    #     For applying changes run {bold}{reload}{reset} or restart your shell.".format(
    #         bold=color(colorama.Style.BRIGHT),
    #         reset=color(colorama.Style.RESET_ALL),
    #         reload=configuration_details.reload))
    #
    #     if configuration_details.can_configure_automatically:
    #         print(
    #             u"Or run {bold}fuck{reset} a second time to configure"
    #            

# Generated at 2022-06-14 09:05:34.687113
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    import sys
    import io
    from .conf import ConfigurationDetails


    configuration_details = ConfigurationDetails(path='test_path',
                                                 content='test_content',
                                                 can_configure_automatically=True,
                                                 reload='test_reload')

    sys.stdout = io.StringIO()

    how_to_configure_alias(configuration_details)

    lines = sys.stdout.getvalue().split('\n')
    assert lines[0] == 'Seems like \x1b[1mfuck\x1b[0m alias isn\'t configured!'

# Generated at 2022-06-14 09:05:43.071949
# Unit test for function debug
def test_debug():
    from mock import patch
    from thefuck.main import settings
    settings.debug = True
    with patch('sys.stderr') as stderr:
        debug('debug message')

    stderr.write.assert_called_with(
        u'{blue}{bold}DEBUG:{reset} debug message\n'.format(
            blue=color(colorama.Fore.BLUE),
            bold=color(colorama.Style.BRIGHT),
            reset=color(colorama.Style.RESET_ALL)))


# Generated at 2022-06-14 09:05:47.423205
# Unit test for function debug_time
def test_debug_time():
    start = datetime.now()
    with debug_time('Under timer') as timed_func:
        timed_func()
        assert datetime.now() - start < timed_func.__exit__()

# Generated at 2022-06-14 09:05:53.883883
# Unit test for function debug
def test_debug():
    import sys
    import StringIO
    sys.stderr = StringIO.StringIO()

    debug("test debug message")
    assert(sys.stderr.getvalue() == "test debug message\n")

    sys.stderr = sys.__stderr__



# Generated at 2022-06-14 09:05:56.417432
# Unit test for function color
def test_color():
    assert color('\33[31m') == '\33[31m'
    settings.no_colors = True
    assert color('\33[31m') == ''

# Generated at 2022-06-14 09:05:58.275018
# Unit test for function color
def test_color():
    assert color('colored') == 'colored'
    assert color('colored') == ''

# Generated at 2022-06-14 09:06:10.765929
# Unit test for function confirm_text
def test_confirm_text():
    # Magic for tests on Python 2.6
    if 'colorama' not in globals():
        import colorama
        sys.modules['colorama'] = colorama
    if 'color' not in globals():
        color = lambda color_: '' if settings.no_colors else color_
    from mock import Mock
    from .conf import Settings
    settings = Settings()
    settings.no_colors = False
    settings.confirm_enter = True
    settings.confirm_side_effect = True
    settings.confirm_all = True
    correct_command = Mock(
        script=u'pwd',
        side_effect=True)

# Generated at 2022-06-14 09:06:28.051219
# Unit test for function confirm_text
def test_confirm_text():
    import StringIO
    sys.stderr = StringIO.StringIO()

    corrected_cmd = corrected_command.CorrectedCommand(
        u'script', u'stderr', u'corrected', False)

    confirm_text(corrected_cmd)
    res = sys.stderr.getvalue()
    assert res == expected_result


# Generated at 2022-06-14 09:06:30.483023
# Unit test for function color
def test_color():
    colorama.init()
    assert color(colorama.Fore.CYAN + colorama.Style.BRIGHT) == \
        u'\x1b[36m\x1b[1m'



# Generated at 2022-06-14 09:06:32.356626
# Unit test for function debug_time
def test_debug_time():
    try:
        with debug_time('test'):
            pass
    except KeyboardInterrupt:
        pass

# Generated at 2022-06-14 09:06:34.840675
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .rule import CorrectedCommand
    from .test.utils import KeyValueStore
    settings.load(KeyValueStore())
    show_corrected_command(CorrectedCommand('rm /etc/hosts', False))

# Generated at 2022-06-14 09:06:47.854299
# Unit test for function debug
def test_debug():
    import io
    import sys

    stderr = sys.stderr

# Generated at 2022-06-14 09:06:49.208968
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text(None) is None



# Generated at 2022-06-14 09:06:53.807825
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .shells import Shell

    s = Shell()
    how_to_configure_alias(s.get_alias())
    already_configured(s.get_alias())
    configured_successfully(s.get_alias())

# Generated at 2022-06-14 09:06:54.899297
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text(1)

# Generated at 2022-06-14 09:06:55.692986
# Unit test for function debug
def test_debug():
    debug('test')

# Generated at 2022-06-14 09:06:59.672163
# Unit test for function debug_time
def test_debug_time():
    import time
    debug_time('hello')
    time.sleep(1)

# Generated at 2022-06-14 09:07:05.148414
# Unit test for function color
def test_color():
    assert color(colorama.Back.RED + colorama.Fore.WHITE
                 + colorama.Style.BRIGHT) == colorama.Back.RED \
        + colorama.Fore.WHITE + colorama.Style.BRIGHT



# Generated at 2022-06-14 09:07:12.729930
# Unit test for function show_corrected_command
def test_show_corrected_command():
    assert show_corrected_command(corrected_command) == const.COMMAND_MARK + corrected_command
    if corrected_command.has_side_effect:
        assert show_corrected_command(corrected_command) == const.COMMAND_MARK + corrected_command + ' (+side effect)'
    else:
        assert show_corrected_command(corrected_command) == const.COMMAND_MARK + corrected_command


# Generated at 2022-06-14 09:07:17.791001
# Unit test for function debug_time
def test_debug_time():
    # Testing in 1 second
    import time
    started = time.time()
    with debug_time('test'):
        time.sleep(1)
    time_taken = time.time() - started
    assert time_taken < 2, ('debug_time() should print debug message '
                            'about time taken')

# Generated at 2022-06-14 09:07:20.979706
# Unit test for function color
def test_color():
    assert color(colorama.Fore.RED + 'red') == colorama.Fore.RED + 'red'
    assert color(colorama.Fore.RED + 'red') != 'red'
    assert color(colorama.Fore.RED + 'red') == ''

# Generated at 2022-06-14 09:07:31.244226
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from tempfile import NamedTemporaryFile
    from types import GeneratorType
    from .shells import known_shells

    for shell in known_shells:
        # Test with /bin/bash
        tmp = NamedTemporaryFile(mode='w+t', suffix=shell)
        how_to_configure_alias(known_shells[shell](path=tmp.name))
        assert type(tmp.readlines()) == GeneratorType

        tmp.close()

        # Test with fish
        tmp = NamedTemporaryFile(mode='w+t', suffix=shell)
        how_to_configure_alias(known_shells[shell](path=tmp.name))
        assert type(tmp.readlines()) == GeneratorType

        tmp.close()

# Generated at 2022-06-14 09:07:33.777117
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .command import Command
    from .corrected_command import CorrectedCommand
    command = Command('pwd', '')
    corrected_command = CorrectedCommand(command, True)

    show_corrected_command(corrected_command)


# Generated at 2022-06-14 09:07:34.465571
# Unit test for function debug_time
def test_debug_time():
    pass


# Generated at 2022-06-14 09:07:37.912785
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .corrector import CorrectedCommand
    show_corrected_command(CorrectedCommand('git push origin master', False))
    show_corrected_command(CorrectedCommand('git push origin master', True))


# Generated at 2022-06-14 09:07:42.119586
# Unit test for function debug
def test_debug():
    from mock import patch

    with patch('sys.stderr.write') as sys_write:
        debug(u'test_msg')
    sys_write.assert_called_once()



# Generated at 2022-06-14 09:07:54.154316
# Unit test for function debug
def test_debug():
    import StringIO
    # Suppress output
    sys.stderr = StringIO.StringIO()
    settings.debug = True
    debug('test message')
    # sys.stderr should contain debug message
    assert sys.stderr.getvalue() == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m test message\n'
    settings.debug = False
    sys.stderr = sys.__stderr__


# Generated at 2022-06-14 09:08:07.542600
# Unit test for function confirm_text
def test_confirm_text():
    import io

    # Test when there is no side effect
    sys.stderr = capturedOutput = io.BytesIO()
    correct_command = 'grep --color=auto'
    confirm_text(correct_command)
    assert capturedOutput.getvalue() == "=> grep --color=auto [enter/↑/↓/ctrl+c]\n\033[2K\r"
    sys.stderr = sys.__stderr__

    # Test when there is a side effect
    sys.stderr = capturedOutput = io.BytesIO()
    correct_command = 'grep --color=auto +side effect'
    confirm_text(correct_command)

# Generated at 2022-06-14 09:08:12.454354
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    class ConfigurationDetails(object):
        def __init__(self, path, content, reload, can_configure_automatically):
            self.path = path
            self.content = content
            self.reload = reload
            self.can_configure_automatically = can_configure_automatically

    how_to_configure_alias(
        ConfigurationDetails('~/.bashrc', 'alias fuck=\'echo "The Fuck!"\'', 'source ~/.bashrc', False))
    how_to_configure_alias(None)


# Generated at 2022-06-14 09:08:18.370086
# Unit test for function debug
def test_debug():
    from contextlib2 import ExitStack
    from io import StringIO
    from .. import debug_tools

    with ExitStack() as stack:
        output = stack.enter_context(StringIO())
        stack.enter_context(debug_tools.debug_output(output))
        debug('test')

    assert output.getvalue() == '\x1b[34m\x1b[1mDEBUG:\x1b[0m test\n'

# Generated at 2022-06-14 09:08:30.346982
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    import io
    import os.path

    from .rules.python import match, get_new_command
    from .shells import Bash, Zsh
    from .utils import get_closest, replace_argument
    from .application import Application
    from .corrector import Corrector
    from .utils import get_all_executables
    from unittest.mock import patch
    import colorama
    colorama.init()
    import sys
    sys.stderr = io.StringIO()
    def getter(app):
        return app.alias
    def setter(app, val):
        app.alias = val

# Generated at 2022-06-14 09:08:38.299393
# Unit test for function confirm_text
def test_confirm_text():
    import StringIO
    from ..utils import get_closest
    from ..application import Application

    rule = get_closest('pss')
    app = Application([rule], u'git statut')
    app.correct_command(rule, u'git status')
    old_stdout = sys.stdout
    try:
        sys.stdout = StringIO.StringIO()
        confirm_text(app.running_command)
    finally:
        sys.stdout = old_stdout


# Generated at 2022-06-14 09:08:42.774804
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .types import CorrectedCommand
    show_corrected_command(CorrectedCommand(
        script='echo "Hello, world!"', side_effect='COPY_RESULT_TO_CLIPBOARD'))



# Generated at 2022-06-14 09:08:44.495369
# Unit test for function debug_time
def test_debug_time():
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:08:54.508802
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    u"""Тестирование корректности вывода информации на экран о том,
    как установить алиас для команды fuck, если он не задан в конфигурационном файле .bashrc или .zshrc"""
    from .conf import ConfigurationDetails


# Generated at 2022-06-14 09:09:01.861882
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = object()
    corrected_command.script = 'echo "Hello!"'
    corrected_command.side_effect = True
    assert show_corrected_command(corrected_command) == 'echo "Hello!" (+side effect)'
    corrected_command.side_effect = False
    assert show_corrected_command(corrected_command) == 'echo "Hello!"'



# Generated at 2022-06-14 09:09:15.386085
# Unit test for function confirm_text
def test_confirm_text():
    from thefuck.utils import get_shell_info
    from thefuck.rules.git_rebase import match, side_effect
    from mock import MagicMock
    from thefuck.shells import Bash, Fish

    env = MagicMock(get=lambda k: None, __setitem__=dict.__setitem__)
    assert match(Command(u'git rebase HEAD~3', env))
    side_effect(Command(u'git rebase HEAD~3', env))

    # Bash
    confirm_text(Command(u'git rebase HEAD~3', env))
    assert env['THEFUCK_CONFIRM_TEXT'] == (
        u'git rebase HEAD~3 '
        u'[enter/↑/↓/ctrl+c]')

    # Fish

# Generated at 2022-06-14 09:09:18.570967
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text('git push origin master') == 'git push origin master [enter/↑/↓/ctrl+c]'


# Generated at 2022-06-14 09:09:31.981183
# Unit test for function confirm_text
def test_confirm_text():
    import sys
    import os
    import errno

    TESTFN = "test-fuck-output.txt"

    try:
        fp = open(TESTFN, "w")
    except IOError as e:
        print("Error: %s" % e)
    else:
        # save stdout
        stdout = sys.stdout
        # save terminal settings
        attrs = list(termios.tcgetattr(sys.stdin))
        # temporarily redirect stdout
        sys.stdout = fp
        # capture output of confirm_text
        confirm_text('test')
        # restore stdout
        sys.stdout = stdout
        # close output file
        fp.close()
        # restore terminal settings
        termios.tcsetattr(sys.stdin, termios.TCSANOW, attrs)

# Generated at 2022-06-14 09:09:34.336948
# Unit test for function debug_time
def test_debug_time():
    with debug_time('title'):
        import time
        time.sleep(0.000001)


# Generated at 2022-06-14 09:09:38.113747
# Unit test for function debug
def test_debug():
    from cStringIO import StringIO
    from mock import patch
    from . import settings

    # Setup fake stderr
    stderr = StringIO()
    stdout = StringIO()
    with patch('sys.stderr', stderr):
        with patch('sys.stdout', stdout):
            settings.debug = True

            debug(u'test')
            assert stderr.getvalue().endswith('DEBUG: test\n')

            settings.debug = False
            debug(u'test')

# Generated at 2022-06-14 09:09:44.705942
# Unit test for function show_corrected_command
def test_show_corrected_command():
    sys.stdout = open("./tests/output.txt", "w")
    show_corrected_command(corrected_command)
    sys.stdout.close()
    WARNING    = '\033[1;31m'
    ENDC       = '\033[0m'
    expected_output = WARNING + '[WARN] ' + 'vim' + ENDC
    file = open("./tests/output.txt", "r") 
    output = file.readlines() 
    assert(output[0] == expected_output)


# Generated at 2022-06-14 09:09:51.830012
# Unit test for function color
def test_color():
    colorama.init()
    assert color(colorama.Fore.RED + colorama.Style.BRIGHT) == \
        colorama.Fore.RED + colorama.Style.BRIGHT
    settings.no_colors = True
    assert color(colorama.Fore.RED + colorama.Style.BRIGHT) == ''



# Generated at 2022-06-14 09:09:56.773210
# Unit test for function debug
def test_debug():
    # import StringIO
    # import sys
    # out = StringIO()
    # sys.stderr = out
    #
    # debug('test')
    # out.seek(0)
    # sys.stderr.write(out.read())
    pass

# Generated at 2022-06-14 09:09:59.521290
# Unit test for function debug_time
def test_debug_time():
    with debug_time('Test debug_time'):
        1+1

# Generated at 2022-06-14 09:10:06.341525
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    class ConfigurationDetails(object):
        def __init__(self, content, path, can_configure_automatically=True, reload='source ~/.bashrc'):
            self.content = content
            self.path = path
            self.can_configure_automatically = can_configure_automatically
            self.reload = reload

    how_to_configure_alias(ConfigurationDetails(content='content', path='path'))
    assert True

# Generated at 2022-06-14 09:10:17.012294
# Unit test for function confirm_text
def test_confirm_text():
    from unittest import TestCase
    from .command import Command
    from .rules.git import git_rule

    class TestConfirmText(TestCase):
        def setUp(self):
            self.confirm_text_input = []

        def confirm_text(self, corrected_command):
            self.confirm_text_input.append(corrected_command)

        def test_confirm_text(self):
            corrected_command = Command('test', 'git add')
            self.confirm_text(corrected_command)
            self.assertEqual(self.confirm_text_input, [corrected_command])

# Generated at 2022-06-14 09:10:18.322391
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    pass


# Generated at 2022-06-14 09:10:24.350240
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .shells import Zsh
    from .conf import ConfigurationDetails

    how_to_configure_alias(ConfigurationDetails(
        path=Zsh().alias_path,
        content=Zsh().fuck_alias(),
        can_configure_automatically=True,
        reload=u'type fuck again'))



# Generated at 2022-06-14 09:10:27.106059
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    configuration_details = configure()
    assert how_to_configure_alias(configuration_details) is None


# Generated at 2022-06-14 09:10:31.783635
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    import utils.colors as colors
    from utils.conf import ConfigurationDetails
    from .conf import ShellConfig
    from .const import SETTINGS_PATH, RELOAD_COMMAND

    # Terminal doesn't support colors and path doesn't exist
    colors.settings.no_colors = True
    assert not SETTINGS_PATH.exists()
    configuration_details = ConfigurationDetails(SETTINGS_PATH,
                                                 RELOAD_COMMAND, True)

# Generated at 2022-06-14 09:10:33.126972
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)



# Generated at 2022-06-14 09:10:34.707770
# Unit test for function debug
def test_debug():
    debug('test')



# Generated at 2022-06-14 09:10:38.819148
# Unit test for function color
def test_color():
    assert color('') == ''
    settings.no_colors = True
    assert color('') == ''
    settings.no_colors = False
    assert color('') == ''



# Generated at 2022-06-14 09:10:49.852786
# Unit test for function show_corrected_command
def test_show_corrected_command():
    class Command():
        def __init__(self, script='script', side_effect=False):
            self.script = script
            self.side_effect = side_effect
    command = Command()
    show_corrected_command(command)
    assert sys.stderr.getvalue() == (u'{prefix}{bold}{script}{reset}'
                                     u'\n'.format(
                                         prefix=const.USER_COMMAND_MARK,
                                         script=command.script,
                                         bold=color(colorama.Style.BRIGHT),
                                         reset=color(colorama.Style.RESET_ALL)))
    command = Command(side_effect=True)
    show_corrected_command(command)

# Generated at 2022-06-14 09:10:51.332949
# Unit test for function color
def test_color():
    assert color('red') == colorama.Fore.RED

# Generated at 2022-06-14 09:11:05.188297
# Unit test for function debug
def test_debug():
    from mock import patch, DEFAULT, MagicMock

    with patch.multiple(
            settings, debug=True,
            no_colors=False,
            universal_mode=False,
            wait_command=False,
            slow_commands=[]):
        with patch.multiple(
                'sys',
                stdout=DEFAULT,
                stderr=MagicMock()) as mocks:
            with debug_time(u'something'):
                pass
            mocks['stderr'].write.assert_called_with(
                '\x1b[34m\x1b[1mDEBUG:\x1b[0m something took: 0:00:00.000001\n')



# Generated at 2022-06-14 09:11:12.900908
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .utils import wrap_colorama_ansi

    def assert_corrected_command(command, corrected_command,
                                 side_effect=False):
        import StringIO
        buf = StringIO.StringIO()
        sys.stderr = buf
        show_corrected_command(corrected_command(command, side_effect))
        sys.stderr = sys.__stderr__
        assert wrap_colorama_ansi(buf.getvalue()) == (
            u'{}\033[1K\r\x1b[1m{}\x1b[0m{}\n'.format(
                const.USER_COMMAND_MARK, command,
                u' (+side effect)' if side_effect else u''))


# Generated at 2022-06-14 09:11:23.362632
# Unit test for function debug_time
def test_debug_time():
    def fn(debug):
        with debug_time('msg'):
            debug('test')
    import unittest
    import mock
    class TimeTestCase(unittest.TestCase):
        @mock.patch('thefuck.utils.debug')
        def test_debug(self, debug):
            fn(debug)
            debug.assert_called_with('msg took: 0:00:00')
    unittest.main()

# Generated at 2022-06-14 09:11:29.639086
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import StringIO
    save_stdout = sys.stdout
    try:
        out = StringIO.StringIO()
        sys.stdout = out
        sys.argv.append(u'test_show_corrected_command')
        try:
            import unittest.mock as mock
            from .correct import CorrectedCommand
            show_corrected_command(
                CorrectedCommand(u'echo "foo"', False))
            output = out.getvalue().strip()
            assert output == u'{}echo "foo"'.format(const.USER_COMMAND_MARK)
        finally:
            sys.argv.pop()
    finally:
        sys.stdout = save_stdout

# Generated at 2022-06-14 09:11:39.386816
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from datetime import datetime
    class configuration_details(object):
        def __init__(self):
            self.path = '~/.bashrc'
            self.reload = 'source ~/.bashrc'
            self.can_configure_automatically = True
            self.content = 'alias fuck='

        def _asdict(self):
            return self.__dict__

    # if configuration_details is not None
    configuration_details.reload = 'source ~/.bashrc'
    how_to_configure_alias(configuration_details)

    # if configuration_details is None
    how_to_configure_alias(None)


# Generated at 2022-06-14 09:11:46.398300
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import os
    import sys
    import unittest

    class TestShowCorrectedCommand(unittest.TestCase):
        def test_show_corrected_command(self):
            class CorrectedCommand(object):
                script = u'ls'
                side_effect = False

            saved_stdout = sys.stdout
            saved_stderr = sys.stderr
            try:
                out = open(os.devnull, 'w')
                sys.stdout = out
                sys.stderr = out

                show_corrected_command(CorrectedCommand())
            finally:
                sys.stdout = saved_stdout
                sys.stderr = saved_stderr

    unittest.main()

# Generated at 2022-06-14 09:11:47.632199
# Unit test for function debug_time
def test_debug_time():
    with debug_time('abc'):
        pass

# Generated at 2022-06-14 09:11:50.336544
# Unit test for function confirm_text
def test_confirm_text():
    import mock
    import sys
    for corrected_command in [
            mock.Mock(script=u'echo "fuck you!"')]:
        with mock.patch('sys.stderr') as stderr:
            confirm_text(corrected_command)
            assert stderr.write.call_count == 1



# Generated at 2022-06-14 09:11:56.706863
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .command import Command
    from .utils import clear_screen
    show_corrected_command(Command('ls', 'ls', False))
    assert clear_screen() + const.USER_COMMAND_MARK + 'ls' == sys.stderr.getvalue()
    sys.stderr.truncate(0)
    sys.stderr.seek(0)

# Generated at 2022-06-14 09:12:03.617193
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    
    def assert_contents(actual, expected):
        assert actual.strip() == expected.strip()

    with patch('sys.stdout', StringIO()) as out:
        how_to_configure_alias(None)
        assert_contents(out.getvalue(),
                        'Seems like \x1b[1mfuck\x1b[21m alias isn\'t configured!\n'
                        'More details - https://github.com/nvbn/thefuck#manual-installation\n')
    with patch('sys.stdout', StringIO()) as out:
        how_to_configure_alias(AttributeDict(path='~/.bashrc',
                                             reload='reload',
                                             content='. ~/.thefuck',
                                             can_configure_automatically=False))
        assert_

# Generated at 2022-06-14 09:12:10.196902
# Unit test for function debug
def test_debug():
    settings.debug = True
    debug('test_debug')
    output = sys.stderr.getvalue()
    assert 'DEBUG' in output
    assert 'test_debug' in output
    settings.debug = False



# Generated at 2022-06-14 09:12:13.269128
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = 'fuck'
    assert show_corrected_command(corrected_command) == '>>>> fuck'

# Generated at 2022-06-14 09:12:24.533574
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    class MetaConfigurationDetails(object):
        def __init__(self, can_configure_automatically, path, content, reload):
            self.can_configure_automatically = can_configure_automatically
            self.path = path
            self.content = content
            self.reload = reload

        def _asdict(self):
            return {
                'can_configure_automatically': self.can_configure_automatically,
                'path': self.path,
                'content': self.content,
                'reload': self.reload
            }

    configuration_details = MetaConfigurationDetails(False, 'bashrc',
                                                     'fuck=echo -n', 'source')
    import io
    import sys

    out_put_data = io.BytesIO()
    sys.stdout

# Generated at 2022-06-14 09:12:28.228160
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = "git status"
    message = const.USER_COMMAND_MARK + 'git status\n'
    assert message == show_corrected_command(corrected_command)


# Generated at 2022-06-14 09:12:39.210596
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .utils import wrap_streams
    from .history import History
    from .command import Command
    from .correct import CorrectedCommand
    from .shells import Fish, Bash

    fish = Fish()
    bash = Bash()

    streams = wrap_streams()
    history = History([])
    command = Command('ls', '', history)
    corrected = CorrectedCommand(command, 'ls *.py', True)

    show_corrected_command(corrected)
    output = streams.stdout.getvalue()
    assert output == ''
    output = streams.stderr.getvalue()
    assert output == u'{}ls *.py (+side effect)\n'.format(
        const.USER_COMMAND_MARK)

    history = History([(u'ls *.py', False)])

# Generated at 2022-06-14 09:12:42.816350
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(const.ConfigurationDetails('/Users/liuguangwei/.bashrc', 'source ~/.bashrc', False))


# Generated at 2022-06-14 09:12:46.911763
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .correct import CorrectedCommand
    from .rule import Rule
    rule = Rule('fuck', lambda x: x)
    r = CorrectedCommand(rule, [], '')
    show_corrected_command(r)


# Generated at 2022-06-14 09:12:49.913705
# Unit test for function color
def test_color():
    assert color(u'') == u''
    assert color(u'\033[1;31mRed\033[0m') == u'\033[1;31mRed\033[0m'

# Generated at 2022-06-14 09:12:56.621198
# Unit test for function debug
def test_debug():
    def my_run(debug_message):
        debug(debug_message)

    from mock import patch
    with patch('sys.stderr') as sys_stderr:
        my_run(u"Test debug")
        sys_stderr.write.assert_called_with(
            u'\x1b[34m\x1b[1mDEBUG:\x1b[0m Test debug\n')

# Generated at 2022-06-14 09:12:58.059024
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text(tuple()) == None



# Generated at 2022-06-14 09:13:05.930123
# Unit test for function debug
def test_debug():
    """Tests that debug writes to stderr"""
    import StringIO
    _stderr = sys.stderr
    try:
        out = StringIO.StringIO()
        sys.stderr = out
        debug('This is a test')
        output = out.getvalue().strip()
        assert 'This is a test' in output
    finally:
        sys.stderr = _stderr

# Generated at 2022-06-14 09:13:08.384194
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    how_to_configure_alias(None)

# Generated at 2022-06-14 09:13:09.591620
# Unit test for function debug
def test_debug():
    assert debug('text') == None


# Generated at 2022-06-14 09:13:21.317020
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .application import ConfigurationDetails
    from .utils import get_closest
    from .shells import Shell

    class FakeShell(Shell):
        alias_support = True
        can_configure_automatically = False
        prioritiy = 0

        def get_conf_filename(self):
            return '~/.bash'

        def get_relod_command(self):
            return 'source ~/.bash'

        @classmethod
        def from_shell(cls, shell_executable):
            return cls()

    Shell.aliases = [Shell, FakeShell]
    assert get_closest(FakeShell, 'bash') == FakeShell

# Generated at 2022-06-14 09:13:32.119216
# Unit test for function show_corrected_command
def test_show_corrected_command():
    sys.stderr = open('test_show_corrected_command.txt', 'w')
    corrected_command = Command('ls -l')
    corrected_command.side_effect = True
    show_corrected_command(corrected_command)
    corrected_command.side_effect = False
    show_corrected_command(corrected_command)
    sys.stderr.close()
    f = open('test_show_corrected_command.txt', 'r')
    text = f.readlines()
    f.close()
    assert text == ['ls -l (+side effect)\n', 'ls -l\n']

# Generated at 2022-06-14 09:13:36.182636
# Unit test for function debug
def test_debug():
    assert debug('foo bar') is None
    assert debug(u'foo bar') is None
    assert debug(u'утф-8!') is None
    assert debug(1) is None
    assert debug(1.0) is None
    assert debug([1, 2, 3]) is None
    assert debug({1: 2}) is None
    assert debug({u'утф-8': 1}) is None

# Generated at 2022-06-14 09:13:41.559858
# Unit test for function debug
def test_debug():
    from StringIO import StringIO

    with StringIO() as io:
        io_handler = io.__enter__()
        debug('Hello World!')
        io_handler.seek(0)
        assert io.read() == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m Hello World!\n'

# Generated at 2022-06-14 09:13:43.515994
# Unit test for function debug
def test_debug():
    assert '\033[1K\r' in confirm_text(None)

# Generated at 2022-06-14 09:13:49.539614
# Unit test for function debug
def test_debug():
    import StringIO
    captured_output = StringIO.StringIO()
    sys.stderr = captured_output
    debug(u'hello')
    sys.stderr = sys.__stderr__
    assert captured_output.getvalue() == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m hello\n'