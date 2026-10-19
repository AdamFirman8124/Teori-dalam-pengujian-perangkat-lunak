

# Generated at 2022-06-14 09:03:59.282681
# Unit test for function confirm_text
def test_confirm_text():
    from pytest import raises
    from .testcase import TestCase
    from .utils import suppress_stderr

    with TestCase() as case:
        case.os_system.return_value = 1
        case.os_environ.__getitem__.return_value = '0'
        case.os_path.lexists.return_value = True

        with raises(SystemExit) as result:
            with suppress_stderr():
                confirm_text(corrected_command=None)

        assert result.value.code == 1



# Generated at 2022-06-14 09:04:11.071719
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from .shells import Shell
    import pytest
    from .types import ConfigurationDetails


# Generated at 2022-06-14 09:04:13.382675
# Unit test for function debug_time
def test_debug_time():
    l = []
    with debug_time('test'):
        l.append(1)
    assert l == [1]

# Generated at 2022-06-14 09:04:16.407715
# Unit test for function show_corrected_command
def test_show_corrected_command():
    sys.stderr.write = lambda x: x  # monkeypatch
    show_corrected_command(object())

# Generated at 2022-06-14 09:04:17.168378
# Unit test for function debug
def test_debug():
    debug('Hello World')

# Generated at 2022-06-14 09:04:22.498504
# Unit test for function color
def test_color():
    assert color(colorama.Back.RED + colorama.Fore.WHITE + colorama.Style.BRIGHT) == ''
    settings.no_colors = False
    assert color(colorama.Fore.RED + colorama.Style.BRIGHT) == colorama.Fore.RED + colorama.Style.BRIGHT

# Generated at 2022-06-14 09:04:26.357928
# Unit test for function show_corrected_command
def test_show_corrected_command():
    corrected_command = corrected_command_instance()
    corrected_message = const.USER_COMMAND_MARK + 'python'
    assert show_corrected_command(corrected_command)==corrected_message


# Generated at 2022-06-14 09:04:32.395046
# Unit test for function debug
def test_debug():
    sys.stderr = open('file', 'w')
    settings.debug = True
    debug('Hello!')
    sys.stderr.close()
    assert open('file').read() == u'\x1b[94m\x1b[1mDEBUG:\x1b[0m Hello!\n'
    open('file', 'w').close()

# Generated at 2022-06-14 09:04:35.735232
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import sys
    sys.stdout.write('')
    sys.stdout.write = lambda x: sys.stdout
    show_corrected_command(sys.stdout)

# Generated at 2022-06-14 09:04:46.357022
# Unit test for function confirm_text
def test_confirm_text():
    def assert_confirm_text(script, side_effect, output):
        corrected_command = MockCorrectedCommand(script, side_effect)
        confirm_text(corrected_command)
        assert sys.stderr.getvalue() == output

    from .utils import MockSysStderr

    sys.stderr = MockSysStderr()

    class MockCorrectedCommand(object):
        def __init__(self, script, side_effect):
            self.script = script
            self.side_effect = side_effect

    assert_confirm_text(u'foo', False,
                        u'{}foo []\033[1K\r'.format(const.USER_COMMAND_MARK))

# Generated at 2022-06-14 09:04:51.120568
# Unit test for function debug_time
def test_debug_time():
    with debug_time(u"hello"):
        pass



# Generated at 2022-06-14 09:05:01.059436
# Unit test for function debug
def test_debug():
    output = []

    def mockwrite(string):
        output.extend(string.split('\n'))

    settings.debug = True
    try:
        saved = sys.stderr.write
        sys.stderr.write = mockwrite
        debug(u'ёжик')
        assert output == [u'\x1b[34m\x1b[1mDEBUG:\x1b[0m \xd1\x91\xd0\xb6\xd0\xb8\xd0\xba']
    finally:
        sys.stderr.write = saved
        settings.debug = False

# Generated at 2022-06-14 09:05:06.889656
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text('ls -l') == u'ls -l [Ввод/↑/↓/ctrl+c]'

# Generated at 2022-06-14 09:05:08.749227
# Unit test for function debug_time
def test_debug_time():
    with debug_time(u'Test'):
        pass



# Generated at 2022-06-14 09:05:18.041308
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import subprocess
    import tempfile
    import os
    temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False)
    temp_file.write('import os\n')
    temp_file.close()
    temp_file_name = temp_file.name
    try:
        subprocess.call(['python', temp_file_name])
        show_corrected_command(['python', temp_file_name])
    finally:
        os.remove(temp_file_name)


# Generated at 2022-06-14 09:05:22.061058
# Unit test for function confirm_text
def test_confirm_text():
    from .const import DEFAULT_CACHE_TIMEOUT
    from .conf import settings
    settings.cache_timeout = DEFAULT_CACHE_TIMEOUT
    confirm_text(const.CorrectedCommand('ls', True))
    confirm_text(const.CorrectedCommand('ls -alh', False))

# Generated at 2022-06-14 09:05:22.925103
# Unit test for function show_corrected_command
def test_show_corrected_command():
    pass

# Generated at 2022-06-14 09:05:25.247618
# Unit test for function debug_time
def test_debug_time():
    import time
    with debug_time('foo'):
        time.sleep(0.1)

# Generated at 2022-06-14 09:05:26.530566
# Unit test for function debug_time
def test_debug_time():
    debug_time('test')

# Generated at 2022-06-14 09:05:27.854121
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text('')

# Generated at 2022-06-14 09:05:35.008218
# Unit test for function debug
def test_debug():
    from StringIO import StringIO
    out = StringIO()
    sys.stderr = out
    debug(u'msg')
    assert u'msg' in out.bu

# Generated at 2022-06-14 09:05:38.709455
# Unit test for function debug
def test_debug():
    assert debug(u'test') == sys.stderr.write(u'\x1b[34m\x1b[1mDEBUG:\x1b[0m test\n')


# Generated at 2022-06-14 09:05:52.760500
# Unit test for function confirm_text
def test_confirm_text():
    try:
        test_confirm_text.last_output
    except AttributeError:
        test_confirm_text.last_output = None

    def fake_stdout(data):
        test_confirm_text.last_output = data

    def test(command):
        corrected_command = Command(script=command)
        confirm_text(corrected_command)
        assert command in test_confirm_text.last_output
    prev_stdout = sys.stdout
    sys.stdout = fake_stdout
    test('git comit -am "Correct commit"')
    test('git commit -am "Correct commit"')
    test('git comit -am "Correct commit"')
    test('git commit -am "Correct commit"')
    sys.stdout = prev_stdout

# Generated at 2022-06-14 09:06:04.619542
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    import re
    import subprocess
    configuration_details = subprocess.check_output(
        ['python', 'setup.py', 'configuration_details'])
    configuration_details = configuration_details.decode(sys.stdout.encoding)
    configuration_details = re.search(
        r"shell_template=\((.*?), .*\)", configuration_details).groups()[0]
    configuration_details = configuration_details.replace("'", "")
    configuration_details = configuration_details.replace("\\n", "\n")
    configuration_details = configuration_details.replace("\\t", "\t")
    configuration_details = configuration_details.replace("\\r", "\r")
    configuration_details = configuration_details.replace("\\f", "\f")

# Generated at 2022-06-14 09:06:11.522250
# Unit test for function debug
def test_debug():
    from StringIO import StringIO
    import sys, os
    debug_io = StringIO()
    stdout_save = sys.stdout
    sys.stdout = debug_io
    debug("test debug")
    sys.stdout = stdout_save
    debug_io.seek(0)
    result = debug_io.readline()
    result = result.strip()
    assert result == "DEBUG: test debug"

# Generated at 2022-06-14 09:06:24.900486
# Unit test for function debug
def test_debug():
    # Clear all printed text
    sys.stdout.seek(0)
    sys.stdout.truncate()
    # Run function
    debug('Function debug() works fine')
    # Get what function printed on stdout
    output = sys.stdout.getvalue().strip()
    # Check that output equals to the string
    assert output == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m Function debug() works fine', 'Debug message is incorect'

# Generated at 2022-06-14 09:06:27.602227
# Unit test for function debug_time
def test_debug_time():
    time = datetime.now()
    with debug_time(u'foo'):
        assert datetime.now() - time > datetime.now() - time

# Generated at 2022-06-14 09:06:33.749330
# Unit test for function confirm_text
def test_confirm_text():
    import functools
    from mock import Mock
    from thefuck.shells.base import Command
    command = Command('ls', 'l', '')
    _input = Mock(side_effect=functools.partial(raw_input, 'y'))
    _print = Mock()
    with Mock(raw_input=_input, print=_print):
        assert confirm_text(command) is True
        assert confirm_text(command) is False
        assert 'ls' in _print.call_args[0][0]
    _input.assert_called_with()



# Generated at 2022-06-14 09:06:40.080219
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    configuration_details = const.ConfigurationDetails(
        can_configure_automatically=True,
        reload='test_reload',
        path='test_path',
        content='test_content')
    how_to_configure_alias(configuration_details)


if __name__ == '__main__':
    test_how_to_configure_alias()

# Generated at 2022-06-14 09:06:42.559695
# Unit test for function confirm_text
def test_confirm_text():
    text = confirm_text()
    assert (text == 'The Fuck {} using Python {} and {}n')

# Generated at 2022-06-14 09:06:50.913879
# Unit test for function debug_time
def test_debug_time():
    import time
    import mock

    with mock.patch('sys.stderr') as mock_stderr:
        with debug_time('debug'):
            time.sleep(0.3)
        mock_stderr.write.assert_called_once_with(
            '\x1b[34m\x1b[1mDEBUG:\x1b[0m debug took: 0:00:00.300000\n')

# Generated at 2022-06-14 09:06:54.053056
# Unit test for function debug_time
def test_debug_time():
    from datetime import timedelta
    with debug_time('sdfsdf'):
        assert 1==1
        pass

# Generated at 2022-06-14 09:06:56.598679
# Unit test for function debug_time
def test_debug_time():
    assert debug_time('test {}'.format(1)) == 'test 1 took: 0:00:00.000'


# Generated at 2022-06-14 09:07:04.789179
# Unit test for function confirm_text
def test_confirm_text():
    from .utils import memoize
    mocked_confirm_text = memoize(confirm_text)
    try:
        import io
        import sys
        from .conf import load_settings, _get_settings_path
        load_settings(_get_settings_path())
        sys.stdout = io.BytesIO()
        mocked_confirm_text(None)
        assert b"\033[1K" in sys.stdout.getvalue()
    finally:
        sys.stdout = sys.__stdout__

# Generated at 2022-06-14 09:07:10.705559
# Unit test for function show_corrected_command
def test_show_corrected_command():
    class CorrectedCommand(object):
        def __init__(self, script, side_effect):
            self.script = script
            self.side_effect = side_effect

    assert '$ fuck b' == show_corrected_command(CorrectedCommand('b', False))
    assert '$ fuck b (+side effect)' == show_corrected_command(CorrectedCommand('b', True))

# Generated at 2022-06-14 09:07:13.948548
# Unit test for function color
def test_color():
    if settings.no_colors:
        assert color(colorama.Fore.RED) == ''
    else:
        assert color(colorama.Fore.RED) == colorama.Fore.RED

# Generated at 2022-06-14 09:07:18.633614
# Unit test for function debug_time
def test_debug_time():
    from mock import patch
    from io import StringIO

    file_obj = StringIO()
    with patch('sys.stderr', file_obj):
        with debug_time('test'):
            pass
    assert u'test took: 0:00:00.000' in file_obj.getvalue()

# Generated at 2022-06-14 09:07:29.914800
# Unit test for function show_corrected_command
def test_show_corrected_command():
    import mock
    import StringIO

    corrected_command = mock.Mock()
    corrected_command.script = 'commnad'
    corrected_command.side_effect = 'some side effect'

    io = StringIO.StringIO()
    io.name = '<stderr>'
    sys.stderr = io
    show_corrected_command(corrected_command)
    assert io.getvalue() == '$ commnad (+side effect)\n'

    corrected_command.side_effect = None
    io = StringIO.StringIO()
    io.name = '<stderr>'
    sys.stderr = io
    show_corrected_command(corrected_command)
    assert io.getvalue() == '$ commnad\n'



# Generated at 2022-06-14 09:07:38.292947
# Unit test for function debug
def test_debug():
    import StringIO
    stream = StringIO.StringIO()
    settings.set_debug(True)
    sys.stderr = stream
    debug('debug messsage')
    assert u'DEBUG: debug messsage' in stream.getvalue()

    settings.set_debug(False)
    stream = StringIO.StringIO()
    sys.stderr = stream
    debug('debug messsage')
    assert u'DEBUG: debug messsage' not in stream.getvalue()

# Generated at 2022-06-14 09:07:50.186913
# Unit test for function debug
def test_debug():
    from mock import patch
    from thefuck.types import Result

    with patch('sys.stderr') as stderr:
        results = [Result(script='foo', side_effect=True),
                   Result(script='bar', side_effect=False)]
        expected = [(u'{0:%Y-%m-%d %H:%M:%S.%f}'.format(datetime.now()),
                     u'foo +side effect\n'),
                    (u'{0:%Y-%m-%d %H:%M:%S.%f}'.format(datetime.now()),
                     u'bar\n')]
        debug(results)
        assert stderr.write.call_args_list == expected



# Generated at 2022-06-14 09:07:57.472886
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .command import Command
    show_corrected_command(Command('git push origin master', None))
    show_corrected_command(Command('git push origin master', 'git push'))

# Generated at 2022-06-14 09:08:03.934786
# Unit test for function show_corrected_command
def test_show_corrected_command():
    class CorrectedCommand:
        def __init__(self, script=None, side_effect=None):
            self.script = script
            self.side_effect = side_effect
    show_corrected_command(CorrectedCommand('ls'))
    show_corrected_command(CorrectedCommand('git push ...', True))

# Generated at 2022-06-14 09:08:11.677419
# Unit test for function debug_time
def test_debug_time():
    import time

    @contextmanager
    def noop_context_manager():
        yield

    start = datetime.now()
    with debug_time(u'test'):
        time.sleep(0.1)
        assert datetime.now() - start < datetime.now()
        start = datetime.now()
        with noop_context_manager():
            time.sleep(0.1)
            assert datetime.now() - start < datetime.now()

# Generated at 2022-06-14 09:08:17.309084
# Unit test for function debug
def test_debug():
    from tests.utils import capture_stderr

    settings.debug = True
    out = capture_stderr(debug, 'msg')
    assert out == u'\x1b[34m\x1b[1mDEBUG:\x1b[0m msg\n'

    settings.debug = False
    out = capture_stderr(debug, 'msg')
    assert out == ''



# Generated at 2022-06-14 09:08:23.089186
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    config_details = SettingsAttrs(
        can_configure_automatically=True,
        reload='reload',
        path='~/.profile',
        content="eval $(thefuck --alias)"
    )
    assert how_to_configure_alias(config_details) == '\n'

# Generated at 2022-06-14 09:08:35.490463
# Unit test for function confirm_text

# Generated at 2022-06-14 09:08:36.717069
# Unit test for function color
def test_color():
    assert color('') == ''


# Generated at 2022-06-14 09:08:43.665879
# Unit test for function debug_time
def test_debug_time():
    from timeit import Timer
    with debug_time('test'):
        a = Timer('a = [1]*(10**2)', 'gc.enable()').timeit()
        b = Timer('b = [1]*(10**3)', 'gc.enable()').timeit()
        c = Timer('c = [1]*(10**4)', 'gc.enable()').timeit()
        d = Timer('d = [1]*(10**5)', 'gc.enable()').timeit()

# Generated at 2022-06-14 09:08:51.817138
# Unit test for function debug
def test_debug():
    class TestShell(object):
        def __init__(self):
            self.assert_equals_test = TestEquals()
            self.assert_equals_test.debug_log = ['test']

    class TestEquals(object):
        def assertEquals(self, one, two):
            if one != two:
                raise AssertionError('Error')

    test = TestShell()
    test.assert_equals_test.assertEquals('test', debug('test'))

# Generated at 2022-06-14 09:08:57.802636
# Unit test for function confirm_text
def test_confirm_text():
    mocked_stderr = StringIO()
    with patch("sys.stderr", mocked_stderr):
        confirm_text(CorrectedCommand("ls", "ls -G"))

# Generated at 2022-06-14 09:09:10.718283
# Unit test for function confirm_text
def test_confirm_text():
    from commands import CorrectedCommand
    assert confirm_text(CorrectedCommand('ls', side_effect=True)) == None
    assert confirm_text(CorrectedCommand('ls', side_effect=False)) == None
    assert confirm_text(CorrectedCommand('pwd', side_effect=False)) == None
    assert confirm_text(CorrectedCommand('pwd', side_effect=True)) == None
    assert confirm_text(CorrectedCommand('python --help', side_effect=False)) == None
    assert confirm_text(CorrectedCommand('python --help', side_effect=True)) == None

# Generated at 2022-06-14 09:09:13.379825
# Unit test for function color
def test_color():
    assert color('test') == 'test'

    settings.no_colors = True

    assert color('test') == ''



# Generated at 2022-06-14 09:09:16.765752
# Unit test for function debug
def test_debug():
    import pytest
    with pytest.raises(AssertionError):
        debug(u'1')



# Generated at 2022-06-14 09:09:27.966725
# Unit test for function show_corrected_command
def test_show_corrected_command():
    script = 'git push -f'
    from .command import Command
    show_corrected_command(Command(script, False))
    assert '\033[1K\r$ git push -f' == sys.stderr.getvalue()[:-1]
    sys.stderr.reset()

    show_corrected_command(Command(script, True))
    assert '\033[1K\r$ git push -f (+side effect)' == sys.stderr.getvalue()[:-1]
    sys.stderr.reset()

    script = 'pygmentize -g'
    show_corrected_command(Command(script, False))
    assert '\033[1K\r$ pygmentize -g' == sys.stderr.getvalue()[:-1]
    sys.stderr.reset()

# Generated at 2022-06-14 09:09:29.667327
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    assert how_to_configure_alias(None)

# Generated at 2022-06-14 09:09:31.843523
# Unit test for function debug_time
def test_debug_time():
    def test():
        import time
        time.sleep(1)
        return

    with debug_time('test'):
        test()



# Generated at 2022-06-14 09:09:36.278636
# Unit test for function color
def test_color():
    assert not settings.no_colors
    settings.no_colors = True
    assert color('XXX') == ''
    settings.no_colors = False
    assert color('XXX') == 'XXX'



# Generated at 2022-06-14 09:09:40.204797
# Unit test for function debug_time
def test_debug_time():
    # Case 1: with debug True
    settings.debug = True
    with debug_time('test'):
        pass
    # Case 2: with debug False
    settings.debug = False
    with debug_time('test'):
        pass

# Generated at 2022-06-14 09:09:41.398091
# Unit test for function confirm_text
def test_confirm_text():
    corrected_command = 'cd ..'
    confirm_text(corrected_command)


# Generated at 2022-06-14 09:09:42.999524
# Unit test for function confirm_text
def test_confirm_text():
    confirm_text(u'test')
    print('testing')

# Generated at 2022-06-14 09:09:58.133841
# Unit test for function debug
def test_debug():
    from thefuck.conf import settings
    from thefuck.utils import debug
    from thefuck.utils import colored_result_len
    from thefuck.types import Result

    settings.debug = True

    # to restore stdout
    stdout = sys.stdout
    sys.stdout = sys.stderr

    # temporary fix: now Result class has `result` field (shuld be `script`)
    r_1 = Result(script=u'test')
    assert debug(r_1) is None

    # checking if `script` field is colored red
    r_2 = Result(script=u'test')
    assert debug(r_2) is None
    sys.stdout = stdout



# Generated at 2022-06-14 09:10:00.789626
# Unit test for function debug_time
def test_debug_time():

    import sys
    test_start = "test_start"
    test_end = "test_end"
    with debug_time(test_start):
        sys.stderr.write(test_end)

# Generated at 2022-06-14 09:10:03.006404
# Unit test for function color
def test_color():
    assert color('text') == 'text'
    settings.no_colors = True
    assert color('text') == ''

# Generated at 2022-06-14 09:10:05.967086
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    # TODO: improve test. Currently it just checks that function
    # doesn't throw an exception
    how_to_configure_alias(None)



# Generated at 2022-06-14 09:10:08.541879
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    class arg:
        def _asdict(self):
            return {}
    how_to_configure_alias(arg())


# Generated at 2022-06-14 09:10:12.165446
# Unit test for function show_corrected_command
def test_show_corrected_command():
    _input = ('grep refs/tag/v1.0.0 HEAD | grep -v "^-" | cut -c42-', True)
    show_corrected_command(_input)
    assert _input

# Generated at 2022-06-14 09:10:16.341573
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from thefuck.conf import ConfigurationDetails

    configuration_details = ConfigurationDetails(
            can_configure_automatically=False,
            path='path',
            content='content',
            reload='reload')

    how_to_configure_alias(configuration_details)

# Generated at 2022-06-14 09:10:20.335836
# Unit test for function confirm_text
def test_confirm_text():
    from tests.utils import Mock
    correct_command = Mock()
    correct_command.side_effect = False
    correct_command.script = 'ls'
    confirm_text(correct_command)

# Generated at 2022-06-14 09:10:21.762540
# Unit test for function debug
def test_debug():
    assert debug('debug') == None


# Generated at 2022-06-14 09:10:23.529817
# Unit test for function show_corrected_command
def test_show_corrected_command():
    assert 'fuck' in show_corrected_command('fuck')

# Generated at 2022-06-14 09:10:29.197497
# Unit test for function debug_time
def test_debug_time():
    from time import sleep
    with debug_time('test'):
        sleep(0.1)


# Generated at 2022-06-14 09:10:31.201689
# Unit test for function debug
def test_debug():
    from mock import patch, Mock
    debug(u'hello world')
    with patch('thefuck.utils.settings', Mock(debug=False)):
        debug(u'hello world')



# Generated at 2022-06-14 09:10:38.441394
# Unit test for function debug_time
def test_debug_time():

    import os
    import re

    with open(os.devnull, 'w') as devnull:
        sys.stderr = devnull
        with debug_time('test'):
            pass

    sys.stderr = sys.__stderr__
    with debug_time('test'):
        pass
    assert re.match(r'DEBUG: test took: \d+\.\d* s', sys.stderr.getvalue())

# Generated at 2022-06-14 09:10:49.794715
# Unit test for function confirm_text
def test_confirm_text():
    from mock import patch
    from datetime import date as test_date
    sys.stderr = open('/dev/null', 'w')
    sys.stdout = open('/dev/null', 'w')
    with patch('thefuck.shells.and_', False),\
         patch('thefuck.shells.or_', False),\
         patch('thefuck.shells.to_', False),\
         patch('thefuck.shells.get_aliases', lambda: []),\
         patch('thefuck.settings.no_colors', False),\
         patch('thefuck.settings.require_confirmation', True),\
         patch('thefuck.settings.slow_commands', ['somecommand']),\
         patch('thefuck.utils.date', test_date(2005, 11, 4)):
        confirm

# Generated at 2022-06-14 09:10:54.465721
# Unit test for function color
def test_color():
    assert settings.no_colors == True
    assert color(colorama.Fore.RED) == ""
    settings.no_colors = False
    assert color(colorama.Fore.RED) == colorama.Fore.RED


# Generated at 2022-06-14 09:11:06.362375
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    global settings
    settings.debug = True
    settings.no_colors = True
    original_print = print

    from . import alias
    from .types import ConfigurationDetails


    def print(*args, **kwargs):
        original_print(*args, **kwargs)

    def debug_cf(msg):
        print(msg)

    setattr(alias, 'debug', debug_cf)

    how_to_configure_alias(
        ConfigurationDetails(
            path=u'~/.bashrc',
            content='\n'.join(alias.get_alias(shell='bash')),
            reload=u'exec bash',
            can_configure_automatically=False))

    how_to_configure_alias(None)


# Generated at 2022-06-14 09:11:17.159916
# Unit test for function confirm_text
def test_confirm_text():
    import StringIO
    output = StringIO.StringIO()
    sys.stderr = output
    class test_cmd(object):
        def __init__(self):
            self.script = 'ls 1'
            self.side_effect = True
    confirm_text(test_cmd())
    sys.stderr = sys.__stderr__

# Generated at 2022-06-14 09:11:21.816886
# Unit test for function confirm_text
def test_confirm_text():
    import sys
    import StringIO
    buf = StringIO.StringIO()
    sys.stdout = buf
    confirm_text('')
    assert buf.getvalue() == const.USER_COMMAND_MARK+'[\033[1K\r\x1b[1m\x1b[1m\x1b[32menter\x1b[0m/\x1b[34m↑\x1b[0m/\x1b[34m↓\x1b[0m/\x1b[31mctrl+c\x1b[0m]'

# Generated at 2022-06-14 09:11:29.663334
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .models import CorrectedCommand
    from .conf import settings
    from . import const
    settings.no_colors = False
    settings.debug = False
    settings.command = ''
    settings.script = ''
    settings.wait = ''
    show_corrected_command(CorrectedCommand(script='ls'))
    show_corrected_command(CorrectedCommand(script='ls', side_effect=True))
    settings.no_colors = True
    settings.debug = True
    settings.command = 'ls'
    settings.script = 'ls'
    settings.wait = '1'
    confirm_text(CorrectedCommand(script='ls'))
    confirm_text(CorrectedCommand(script='ls', side_effect=True))
    debug('debug message')
    how_to_configure_alias(None)

# Generated at 2022-06-14 09:11:42.395171
# Unit test for function confirm_text
def test_confirm_text():
    from mock import Mock
    from thefuck.shells import Bash

    assert confirm_text(Mock(Script=lambda: u'ls', side_effect=False)) == \
        (u'{prefix}{clear}{bold}ls{reset} [{green}enter{reset}/{blue}↑{reset}'
         u'/{blue}↓{reset}/{red}ctrl+c{reset}]'.format(
            prefix=const.USER_COMMAND_MARK,
            clear='\033[1K\r',
            bold=color(colorama.Style.BRIGHT),
            green=color(colorama.Fore.GREEN),
            red=color(colorama.Fore.RED),
            reset=color(colorama.Style.RESET_ALL),
            blue=color(colorama.Fore.BLUE)))
   

# Generated at 2022-06-14 09:11:50.769148
# Unit test for function debug_time
def test_debug_time():
    from time import sleep
    with debug_time('test'):
        sleep(1)



# Generated at 2022-06-14 09:12:00.519249
# Unit test for function debug
def test_debug():
    class StdError(object):
        messages = []

        def write(self, *messages):
            self.messages.extend(messages)

    original_std_err = sys.stderr
    stderr = StdError()
    sys.stderr = stderr

    try:
        debug(u'привет мир!')
        assert u'привет мир!' in stderr.messages[0]

        debug(u'foo bar')
        assert u'foo bar' in stderr.messages[1]

        debug(u'я тут')
        assert u'я тут' in stderr.messages[2]

    finally:
        sys.stderr = original_std_err

# Generated at 2022-06-14 09:12:09.905381
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from thefuck.shells import Shell
    content = 'fuck = /thefuck/thefuck --alias && fuck'
    profile_path = '/home/user/.bashrc'
    reload_command = 'source ~/.bashrc'
    can_configure_automatically = True
    shell = Shell(content, profile_path, reload_command, can_configure_automatically)  # NOQA
    how_to_configure_alias(shell)
    assert True

# Generated at 2022-06-14 09:12:19.933630
# Unit test for function debug
def test_debug():
    message = 'test_message'
    with settings.override(debug=True):
        debug(message) is None
        assert sys.stderr.getvalue() == (u'\x1b[34m\x1b[1mDEBUG:\x1b[0m '
                                         u'test_message\n')
    with settings.override(debug=False):
        debug(message) is None
        assert sys.stderr.getvalue() == (u'\x1b[34m\x1b[1mDEBUG:\x1b[0m '
                                         u'test_message\n')

# Generated at 2022-06-14 09:12:23.590447
# Unit test for function confirm_text
def test_confirm_text():
    # TODO: add test for side_effect
    corrected_command = 'fuck echo "hello"'
    confirm_text(corrected_command)

# Generated at 2022-06-14 09:12:26.716659
# Unit test for function debug
def test_debug():
    from mock import patch

    with patch('fuck.log.sys.stderr') as sys_stderr:
        debug('test')
    assert sys_stderr.write.called

# Generated at 2022-06-14 09:12:37.983857
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    import StringIO
    import sys

    output = StringIO.StringIO()
    sys.stdout = output
    how_to_configure_alias(None)

    expected = """Seems like \x1b[1mfuck\x1b[0m alias isn't configured!\n""" \
               """More details - https://github.com/nvbn/thefuck#manual-installation\n"""
    assert output.getvalue() == expected

    output = StringIO.StringIO()
    sys.stdout = output
    configuration_details = 'configuration details'
    how_to_configure_alias(configuration_details)


# Generated at 2022-06-14 09:12:50.421864
# Unit test for function show_corrected_command
def test_show_corrected_command():
    from .utils import NamedCommand
    from . import shell
    import tempfile
    import os

    def mock_print(text):
        print(text)

    def run_function_with_mock_print(function, *args, **kwargs):
        old_print = __builtins__['print']
        __builtins__['print'] = mock_print
        try:
            function(*args, **kwargs)
        finally:
            __builtins__['print'] = old_print

    with tempfile.NamedTemporaryFile() as temp:
        temp.write("print('abc');\n")
        temp.flush()

        # without side effect
        command = shell.and_('python', temp.name)
        corrected_command = NamedCommand('python', temp.name, '', '', '', '', '')
       

# Generated at 2022-06-14 09:12:54.131928
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    import mock
    import sys
    with mock.patch('sys.stderr.write') as write:
        how_to_configure_alias(None)
        assert write.called


# Generated at 2022-06-14 09:12:58.461302
# Unit test for function debug
def test_debug():
    from tests.utils import support_stdin

    with support_stdin('false\n') as stdin:
        # `stdin.buffer` is needed on Python 3
        with debug_time('test'):
            stdin.buffer.read()



# Generated at 2022-06-14 09:13:07.085123
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text(
        thefuck.shells.andromeda.AndromedaCommand(
            script='git commit',
            side_effect=False
        )) == const.USER_COMMAND_MARK + 'git commit ' + '[enter/↑/↓/ctrl+c]'



# Generated at 2022-06-14 09:13:09.379695
# Unit test for function debug
def test_debug():
    with debug_time('test'):
        pass



# Generated at 2022-06-14 09:13:11.940147
# Unit test for function show_corrected_command
def test_show_corrected_command():
    try:
        sys.stdout = open('test_file', 'w')
        show_corrected_command('test')
        assert open('test_file').read() == 'git status\n'
    finally:
        sys.stdout = sys.__stdout__
        remove('test_file')

# Generated at 2022-06-14 09:13:17.692915
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    configuration_details = mock.MagicMock(spec=['content'])
    configuration_details.content = "some content"
    configuration_details.can_configure_automatically = True
    configuration_details.path = 'some path'
    configuration_details.reload = 'reload command'
    how_to_configure_alias(configuration_details)



# Generated at 2022-06-14 09:13:22.555298
# Unit test for function debug_time
def test_debug_time():
    import mock
    import time
    time.sleep = mock.MagicMock()

    with debug_time('msg'):
        time.sleep(1)


if __name__ == '__main__':
    test_debug_time()

# Generated at 2022-06-14 09:13:28.912625
# Unit test for function how_to_configure_alias
def test_how_to_configure_alias():
    from . import shell
    from .utils import get_shell
    shell_info = get_shell()

    class ConfigurationDetails(shell.ConfigurationDetails):
        def __init__(self, can_configure_automatically, **kwargs):
            super(ConfigurationDetails, self).__init__(
                can_configure_automatically=can_configure_automatically,
                **kwargs)

    contents = u'eval $(thefuck --alias)'
    show_configuration_details = ConfigurationDetails(
        can_configure_automatically=True,
        path=u'/test/testpath',
        content=contents,
        reload=u'reload')

    how_to_configure_alias(show_configuration_details)

# Generated at 2022-06-14 09:13:31.142396
# Unit test for function color
def test_color():
    assert color(u'foo') == u'foo'
    settings.no_colors = True
    assert color(u'foo') == u''

# Generated at 2022-06-14 09:13:34.324016
# Unit test for function confirm_text
def test_confirm_text():
    import sys

    original_stderr = sys.stderr
    sys.stderr = sys.stdout

    import colorama
    colorama.init()
    confirm_text('test')

    sys.stderr = original_stderr

# Generated at 2022-06-14 09:13:38.216815
# Unit test for function color
def test_color():
    assert color(colorama.Fore.BLUE) == ''
    settings.no_colors = False
    assert color(colorama.Fore.BLUE) == colorama.Fore.BLUE

# Generated at 2022-06-14 09:13:45.901922
# Unit test for function confirm_text
def test_confirm_text():
    assert confirm_text(
        Command('ls -al', 'ls -al', '')) == '\033[1K\rls -al'
    assert confirm_text(Command('rmdir some_folder',
                                'rmdir some_folder', ''),
                        side_effect_on=True) == \
        '\033[1K\rrmdir some_folder (+side effect)'