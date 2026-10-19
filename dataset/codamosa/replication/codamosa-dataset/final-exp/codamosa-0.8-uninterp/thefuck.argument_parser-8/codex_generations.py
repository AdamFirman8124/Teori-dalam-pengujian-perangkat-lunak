

# Generated at 2022-06-14 08:20:47.754242
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser()._parser.prog == 'thefuck'

# Generated at 2022-06-14 08:20:59.444241
# Unit test for method parse of class Parser
def test_Parser_parse():
    settings = Parser()
    assert settings.parse(['thefuck', 'echo', '-v']) == \
        Namespace(alias=None, debug=False,
                  force_command=None, help=False,
                  repeat=None, repeat_command=None,
                  shell_logger=None, version=False,
                  yes=None, yeah=None, hard=None,
                  command=['echo', '-v'])

# Generated at 2022-06-14 08:21:07.682987
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    # When
    args = parser.parse(['fuck', 'git', 'push', ARGUMENT_PLACEHOLDER, '-v'])
    # Then
    assert '-v' in args.command
    assert 'git' in args.command
    assert 'push' in args.command
    # And
    args = parser.parse(['fuck', ARGUMENT_PLACEHOLDER, '-v'])
    # Then
    assert '-v' in args.command
    # And
    args = parser.parse(['fuck', ARGUMENT_PLACEHOLDER,
                         'git', 'push', '--', '-v'])
    # Then
    assert 'git' in args.command
    assert 'push' in args.command

# Generated at 2022-06-14 08:21:09.508787
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert vars(parser._parser).get('prog') is not None
    assert parser is not None


# Generated at 2022-06-14 08:21:13.653199
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from unittest.mock import Mock
    parser = Parser()
    parser.print_usage()
    parser._parser.print_usage.assert_called_once_with(sys.stderr)


# Generated at 2022-06-14 08:21:15.526160
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:21:16.971869
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()
    assert True

# Generated at 2022-06-14 08:21:18.149326
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()

# Generated at 2022-06-14 08:21:20.863695
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    parser.parse(["-v"])

# Generated at 2022-06-14 08:21:22.153838
# Unit test for constructor of class Parser
def test_Parser():
	parser = Parser()


# Generated at 2022-06-14 08:21:29.589489
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    p._prepare_arguments(['thefuck', '--version', '--', 'git commit'])

# Generated at 2022-06-14 08:21:33.385762
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():

    """Unit test for method print_usage of class Parser"""

    test_parser = Parser()
    result = test_parser.print_usage()

    # Should return none
    assert result == None

# Generated at 2022-06-14 08:21:34.982317
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:21:36.372724
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()


# Generated at 2022-06-14 08:21:42.475297
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from contextlib import redirect_stderr
    from io import StringIO
    from .const import USAGE, HELP

    f = StringIO()
    with redirect_stderr(f):
        Parser().print_help()
    output = f.getvalue()
    assert USAGE in output
    assert HELP in output


# Generated at 2022-06-14 08:21:48.508305
# Unit test for constructor of class Parser
def test_Parser():
    #create a instance, Parser
    app = Parser()
    args = app._parser
    #add argument
    args = app.parse(['fuck','-v','--debug','echo'])
    assert args.version == True
    assert args.debug == True
    assert args.command == ['echo']

if __name__ == '__main__':
    test_Parser()

# Generated at 2022-06-14 08:22:01.737414
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse('thefuck --debug --alias fuck foo') == \
        Namespace(command=None, alias='fuck', debug=True)
    assert parser.parse('thefuck --debug --alias fuck'.split()) == \
        Namespace(command=None, alias='fuck', debug=True)
    assert parser.parse('thefuck foo --debug'.split()) == \
        Namespace(command='foo', alias=None, debug=True)
    assert parser.parse('thefuck --debug foo'.split()) == \
        Namespace(command='foo', alias=None, debug=True)
    assert parser.parse('thefuck --debug --alias fuck foo'.split()) == \
        Namespace(command='foo', alias='fuck', debug=True)

# Generated at 2022-06-14 08:22:09.195298
# Unit test for method parse of class Parser
def test_Parser_parse():
    argv = ['thefuck', 'ps', '-ef', ARGUMENT_PLACEHOLDER, '--version']
    parser = Parser()
    arguments = parser.parse(argv)
    assert not arguments.help
    assert not arguments.version
    assert not arguments.yes
    assert not arguments.repeat
    assert not arguments.debug
    assert not arguments.alias
    assert not arguments.shell_logger
    assert not arguments.force_command
    assert arguments.command == ['ps', '-ef']

# Generated at 2022-06-14 08:22:17.169272
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from io import StringIO
    from unittest.mock import patch
    from thefuck.main import get_parser
    with patch('sys.stderr', StringIO()) as fake_stderr, \
         patch('thefuck.main.load_settings') as load_settings:
        get_parser().print_usage()
    assert 'usage: thefuck [--version]' in fake_stderr.getvalue()


# Generated at 2022-06-14 08:22:27.041498
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser.prog == "thefuck"
    assert parser._parser._actions[0].option_strings == ['-v', '--version']
    assert parser._parser._actions[1].option_strings == ['-a', '--alias']
    assert parser._parser._actions[2].option_strings == ['-l', '--shell-logger']
    assert parser._parser._actions[3].option_strings == [
        '--enable-experimental-instant-mode']
    assert parser._parser._actions[4].option_strings == ['-h', '--help']
    assert parser._parser._actions[5].option_strings == ['-y', '--yes',
                                                         '--yeah', '--hard']

# Generated at 2022-06-14 08:22:44.325436
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    import io
    import sys
    import unittest
    from unittest.mock import patch

    original_stdout = sys.stdout

    class OutputTests(unittest.TestCase):
        def setUp(self):
            sys.stdout = io.StringIO()

        def tearDown(self):
            sys.stdout = original_stdout

        @patch('thefuck.parser.get_alias')
        def test_Parser_print_help(self, get_alias):
            get_alias.return_value = 'fuck'
            parser = Parser()
            parser.print_help()

# Generated at 2022-06-14 08:22:57.376782
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    """
    Args:
       None
    Returns:
       True if test is OK
    Raises:
    """
    # given
    class YourParser(Parser):
        def _add_arguments(self):
            self._parser.add_argument(
                '-v', '--version',
                action='store_true',
                help="show program's version number and exit")
            self._parser.add_argument(
                '-a', '--alias',
                nargs='?',
                const=get_alias(),
                help='[custom-alias-name] prints alias for current shell')
    your_parser = YourParser()
    # when
    your_parser.print_usage()
    # then
    return True


# Generated at 2022-06-14 08:23:07.324475
# Unit test for method parse of class Parser
def test_Parser_parse():
    import unittest

    class Args(object):
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                self.__setattr__(key, value)

    class Test_Parser_parse(unittest.TestCase):
        def test_arguments_with_our_placeholder_in_the_middle(self):
            arguments = Parser().parse(['thefuck', 'cmd', '--opt', ARGUMENT_PLACEHOLDER, 'arg1', 'arg2'])

# Generated at 2022-06-14 08:23:08.551593
# Unit test for constructor of class Parser
def test_Parser():
    Parser()


# Generated at 2022-06-14 08:23:11.555491
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    '''
    print_usage should print usage of thefuck to sys.stderr

    '''
    parser = Parser()
    parser.print_usage()

# Generated at 2022-06-14 08:23:16.439212
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    # @todo: replace assert_called with specific classes
    parser = mock.Mock(spec=Parser())
    parser.print_usage()
    parser.get_parser().print_usage.assert_called_with(sys.stderr)



# Generated at 2022-06-14 08:23:22.124017
# Unit test for method parse of class Parser
def test_Parser_parse():
    from thefuck.parser import Parser  # Import the Class Parser(object)
    parser = Parser()                  # create an instance of Parser
    argv = ["-y","--","ls","-l"]
    args = parser.parse(argv)
    print(args)


# Generated at 2022-06-14 08:23:23.322629
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:23:24.531193
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    p = Parser()
    p.print_help()

# Generated at 2022-06-14 08:23:35.425728
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from .const import DESCRIPTION, VERSION
    from thefuck.repl import Repl
    from unittest.mock import patch

    _orig_Repl = Repl
    _patch_output = 'thefuck {}\n\n{}\n\n'.format(VERSION, DESCRIPTION)


# Generated at 2022-06-14 08:23:39.828880
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    p = Parser()
    p.print_help()

# Generated at 2022-06-14 08:23:52.176792
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from .utils import capture_output

    parser = Parser()

    with capture_output() as (stdout, stderr):
        parser.print_help()

    assert stderr == ""

# Generated at 2022-06-14 08:23:58.121769
# Unit test for method parse of class Parser
def test_Parser_parse():
    p = Parser()
    args = p.parse(['--force-command', 'echo', 'foo'])
    assert args.force_command == 'echo'
    assert args.debug is False
    assert args.command == ['foo']
    assert args.repeat is False
    assert args.yes is False
    assert args.shell_logger is None
    assert args.alias is False

# Generated at 2022-06-14 08:24:00.611851
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    assert parser.print_usage() == parser._parser.print_usage(sys.stderr)


# Generated at 2022-06-14 08:24:08.139329
# Unit test for method parse of class Parser
def test_Parser_parse():
    from .thefuck import TheFuck
    from .shells import AvailableShells
    from .types import Settings
    from .config import Config

    shell = AvailableShells().get('bash')

    parser = Parser()
    args = parser.parse(["./thefuck", "echo a"])
    assert TheFuck(Settings(args=args,
                            config=Config(shell, {'history_limit': None}),
                            shell=shell)).settings == Settings(args=args,
                                                               config=Config(shell, {'history_limit': None}),
                                                               shell=shell)

# Generated at 2022-06-14 08:24:21.827250
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()

    # without argument and without command
    assert parser.parse(['thefuck']) == parser._parser.parse_args(['thefuck'])
    # without argument and command
    assert parser.parse(['thefuck', 'ls', '-l']) == parser._parser.parse_args(['--', 'ls', '-l'])
    # argument and command
    assert parser.parse(['thefuck', 'ls', '-l', 'fuck', 'sudo']) == parser._parser.parse_args(['ls', '-l', '--', 'sudo'])
    # with argument and without command
    assert parser.parse(['thefuck', 'fuck']) == parser._parser.parse_args([])

    # with --alias
    assert parser.parse(['thefuck', '--alias']) == parser._parser

# Generated at 2022-06-14 08:24:22.583228
# Unit test for constructor of class Parser
def test_Parser():
    pass

# Generated at 2022-06-14 08:24:35.429948
# Unit test for method parse of class Parser
def test_Parser_parse():
    expected_output = 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l shell_logger] [--enable-experimental-instant-mode] [-d] [--force-command force_command] [-y | -r] [--] command [command ...]'
    class TestParser(Parser):
        def _prepare_arguments(self, argv):
            return []
    parser = TestParser()

    parser.parse(['thefuck'])
    stdout, stderr = capfd.readouterr()
    assert stdout == ''
    assert stderr.splitlines()[-1] == expected_output

    parser.parse(['thefuck', '-v'])
    stdout, stderr = capfd.readouterr()
    assert stdout == ''
    assert stder

# Generated at 2022-06-14 08:24:36.618671
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()

# Generated at 2022-06-14 08:24:46.993452
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    import sys
    import io
    from .const import VERSION

    output = io.StringIO()
    sys.stdout = output
    from .parser import Parser
    parser = Parser()
    parser.print_usage()
    assert output.getvalue().strip() == "usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-d] [--force-command FORCE_COMMAND] [--] [command [command ...]]"
    output.close()


# Generated at 2022-06-14 08:24:51.958144
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()



# Generated at 2022-06-14 08:24:59.787517
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from io import StringIO
    from thefuck.main import THEFUCK_SETTINGS_FILE
    from .utils import get_alias

    stdout = sys.stdout
    sys.stdout = io = StringIO()
    parser = Parser()
    parser.print_help()
    sys.stdout = stdout


# Generated at 2022-06-14 08:25:08.402144
# Unit test for method parse of class Parser
def test_Parser_parse():
    old_stdout = sys.stdout
    old_stdin = sys.stdin

    parser = Parser()
    sys.stdout = open('tmp', 'w')
    parser.parse(['thefuck', '-h'])
    sys.stdout.close()
    sys.stdout = old_stdout
    f = open('tmp')
    lines = f.readlines()
    expected_line = 'usage: thefuck [-h] [-v] [-a [custom-alias-name]]'
    f.close()
    unittest.TestCase().assertEqual(unittest.TestCase().assertTrue(expected_line in lines[0]), True)
    os.remove('tmp')

    # Test for version
    parser = Parser()
    sys.stdout = open('tmp', 'w')

# Generated at 2022-06-14 08:25:18.019825
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    parsed_args = parser.parse(['thefuck', '--shell-logger', 'log.txt', 'command', 'arg1', 'arg2'])
    assert parsed_args.shell_logger == 'log.txt'
    assert parsed_args.command == ['command', 'arg1', 'arg2']
    assert not parsed_args.version
    assert parsed_args.debug
    assert not parsed_args.repeat
    assert not parsed_args.yes
    assert not parsed_args.force_command
    assert not parsed_args.help

    parsed_args = parser.parse(['thefuck', 'command', 'arg1', 'arg2'])
    assert parsed_args.shell_logger is None
    assert parsed_args.command == ['command', 'arg1', 'arg2']

# Generated at 2022-06-14 08:25:19.334614
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_usage()

# Generated at 2022-06-14 08:25:25.915980
# Unit test for method parse of class Parser
def test_Parser_parse():
    test_args = ['--', 'ls', '-la']
    p = Parser()
    assert p.parse(test_args) ==  p._parser.parse_args(test_args)

    test_args = ['--', 'ls', '-la', '-d']
    assert p.parse(test_args) ==  p._parser.parse_args(test_args)

    test_args = ['--', 'ls', '-la', '-d']
    assert p.parse(test_args) ==  p._parser.parse_args(test_args)

    test_args = ['--', 'ls', '-la', '-d']
    assert p.parse(test_args) ==  p._parser.parse_args(test_args)


# Generated at 2022-06-14 08:25:26.898164
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser()._parser.description == 'Argument parser that can handle arguments with our special placeholder.'
#

# Generated at 2022-06-14 08:25:32.451062
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    out, err = capsys.readouterr()
    parser.print_usage()
    out, err = capsys.readouterr()
    assert err.startswith("usage: thefuck ")
    assert err.endswith("[options] [command]\n")


# Generated at 2022-06-14 08:25:44.374913
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    class FakeStderr(object):
        def __init__(self):
            self.data = []
        def write(self, value):
            self.data.append(value)
        def flush(self):
            pass
    stderr = FakeStderr()
    sys.stderr = stderr
    tmp = Parser()
    tmp.print_usage()

# Generated at 2022-06-14 08:25:57.779481
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from .parser import Parser
    from .utils import get_alias

    p = Parser()
    p.parse(['-h'])
    p.parse(['--help'])
    p.parse(['-a'])
    p.parse(['--alias'])
    p.parse(['-a', 'fuck'])
    p.parse(['--alias', 'fuck'])
    p.parse(['-v'])
    p.parse(['--version'])
    p.parse(['-d'])
    p.parse(['--debug'])
    p.parse(['-y'])
    p.parse(['--yes'])
    p.parse(['-l', '~/fuck-shell-output.log'])

# Generated at 2022-06-14 08:26:13.924830
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    f = StringIO()
    with redirect_stdout(f):
        Parser().parse(['thefuck', '--help'])
    assert f.getvalue() == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER]\n              [--enable-experimental-instant-mode] [-d] [--force-command FORCE_COMMAND]\n              [-y|-r] [--] [command [command ...]]\n\n'


# Generated at 2022-06-14 08:26:15.316098
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:26:17.010495
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    assert parser.print_usage() == None


# Generated at 2022-06-14 08:26:20.780368
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser=Parser()
    assert parser.print_usage() == parser._parser.print_usage(sys.stderr)


# Generated at 2022-06-14 08:26:22.201521
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    Parser().print_help()

# Generated at 2022-06-14 08:26:33.217669
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert 'a' in parser._parser._option_string_actions
    assert 'alias' in parser._parser._option_string_actions
    assert 'l' in parser._parser._option_string_actions
    assert 'shell-logger' in parser._parser._option_string_actions
    assert 'enable-experimental-instant-mode' in parser._parser._option_string_actions
    assert 'h' in parser._parser._option_string_actions
    assert 'help' in parser._parser._option_string_actions
    assert 'y' in parser._parser._option_string_actions
    assert 'yes' in parser._parser._option_string_actions
    #assert 'yeah' in parser._parser._option_string_actions
    assert 'hard' in parser._parser._option_string_actions

# Generated at 2022-06-14 08:26:46.246427
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    result = parser.parse(["/usr/local/bin/python2", "mycommand", '--foo', 'bar', '--', '--foo', 'baz'])
    assert result.command == ['--foo', 'baz']
    assert result.foo == 'bar'

    result = parser.parse(["/usr/local/bin/python2", "mycommand", 'cmd', '--', '--foo', 'bar'])
    assert result.command == ['--foo', 'bar']
    assert result.force_command == 'cmd'

    result = parser.parse(["/usr/local/bin/python2", "mycommand", '--', 'cmd', '--foo', 'bar'])
    assert result.command == ['cmd', '--foo', 'bar']
    assert not result.force_command

# Generated at 2022-06-14 08:26:47.824131
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser()



# Generated at 2022-06-14 08:26:54.127925
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    parser.parse(['thefuck', '-v'])
    parser.parse(['thefuck', '-a', 'alias_name'])
    parser.parse(['thefuck', '-a'])
    parser.parse(['thefuck', '-l'])
    parser.parse(['thefuck', '--enable-experimental-instant-mode'])
    parser.parse(['thefuck', '-h'])
    parser.parse(['thefuck', '-y'])
    parser.parse(['thefuck', '-r'])
    parser.parse(['thefuck', '-d'])
    parser.parse(['thefuck', '--force-command', 'command'])
    parser.parse(['thefuck', 'command'])

# Generated at 2022-06-14 08:27:02.127797
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    usage_str = "usage: thefuck [-h] [-v] [-a [custom-alias-name]]" \
                " [-l SHELL_LOGGER] [--enable-experimental-instant-mode]" \
                " [-d] [--force-command FORCE_COMMAND] [--yes] [--repeat]" \
                " [command [command ...]]"
    assert parser.print_usage() == sys.stderr.write(usage_str + "\n")


# Generated at 2022-06-14 08:27:20.457120
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from cStringIO import StringIO
    from .parser import Parser
    from .utils import get_alias
    alias_name = get_alias()

    old_stderr = sys.stderr
    sys.stderr = StringIO()
    try:
        Parser().print_usage()
    finally:
        sys.stderr = old_stderr



# Generated at 2022-06-14 08:27:21.414753
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    Parser().print_usage()

# Generated at 2022-06-14 08:27:31.348697
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    stdout = sys.stdout
    try:
        sys.stdout = StringIO()
        parser.print_usage()
        assert sys.stdout.getvalue() == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-d] [--force-command FORCE_COMMAND] [-y] [-r] [command [command ...]]\n'
    finally:
        sys.stdout = stdout


# Generated at 2022-06-14 08:27:32.586998
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()


# Generated at 2022-06-14 08:27:34.346871
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:27:40.511137
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from .utils import get_real_path
    from .conf import settings

    with settings(allow_system_commands=False):
        original_stderr = sys.stderr
        try:
            output = get_real_path('test/unexpected_output')
            sys.stderr = open(output, 'w')
            parser = Parser()
            parser.print_usage()
            sys.stderr.close()
            assert 'usage: thefuck' in open(output).read()
        finally:
            sys.stderr = original_stderr



# Generated at 2022-06-14 08:27:49.694658
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from io import StringIO
    from contextlib import redirect_stdout
    from .utils import get_alias
    from .main import PARSER as parser

    s = StringIO()
    with redirect_stdout(s):
        parser.print_help()
    assert 'Usage:' in s.getvalue()
    assert 'Show this help message and exit.' in s.getvalue()
    assert '[custom-alias-name] prints alias for current shell.' in s.getvalue()
    assert '-a, --alias [{0}]'.format(get_alias()) in s.getvalue()

# Generated at 2022-06-14 08:27:57.937481
# Unit test for constructor of class Parser
def test_Parser():
    actual = str(Parser()._parser)

# Generated at 2022-06-14 08:28:10.307775
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    import sys;
    old_stderr = sys.stderr;  # save old stderr

    parser = Parser()
    import io;
    sys.stderr = io.StringIO();
    parser.print_usage();
    #print( sys.stderr.getvalue() );
    assert( sys.stderr.getvalue().strip() == "usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-d] [--force-command FORCE_COMMAND] [-y | -r] [command [command ...]]") # stderr.getvalue is the captured output

    sys.stderr = old_stderr;  # restore old stderr

# Generated at 2022-06-14 08:28:16.509908
# Unit test for method parse of class Parser

# Generated at 2022-06-14 08:28:56.708281
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    result = parser.parse([
        'thefuck', '--alias', 'fuck', '--yeah', 'my_command', 'my_arg',
        ARGUMENT_PLACEHOLDER, 'fuck', '--', 'real_command', 'real_arg'])
    assert result.alias == 'fuck'
    assert result.yes
    assert result.command == ['my_command', 'my_arg']
    assert result.force_command == 'real_command real_arg'


# Generated at 2022-06-14 08:29:03.070833
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    arguments = parser.parse('thefuck git remote -rm origin')
    assert len(arguments.command) == 4

    arguments = parser.parse('thefuck git remote -rm origin')
    assert arguments.command[0] == 'git'
    assert arguments.command[1] == 'remote'
    assert arguments.command[2] == '-rm'
    assert arguments.command[3] == 'origin'

    arguments = parser.parse('thefuck git remote -rm origin'.split())
    assert arguments.command[0] == 'git'
    assert arguments.command[1] == 'remote'
    assert arguments.command[2] == '-rm'
    assert arguments.command[3] == 'origin'

    arguments = parser.parse('thefuck --debug git remote -rm origin'.split())

# Generated at 2022-06-14 08:29:04.168535
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser

# Generated at 2022-06-14 08:29:05.115522
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()

# Generated at 2022-06-14 08:29:10.923201
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse([
        'fuck',
        'was',
        'wrong',
        'command',
        ARGUMENT_PLACEHOLDER,
        'where',
        'the',
        'arguments',
        'are'])
    assert args.command == 'was wrong command'
    assert args.where == 'the'
    assert args.are == True



# Generated at 2022-06-14 08:29:19.878887
# Unit test for method parse of class Parser
def test_Parser_parse():
    sys_argv = ['', '-v', '-h', '--shell-logger', 'logger', '-l', '-h', '--shell-logger', 'logger1', '--force-command', 'force', '--', 'echo', 'hello']
    parser = Parser()
    result = parser.parse(sys_argv)
    assert result.shell_logger == 'logger1'
    assert result.enable_experimental_instant_mode is False
    assert result.command == ['echo', 'hello']
    assert result.force_command == 'force'

# Generated at 2022-06-14 08:29:21.312774
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    my_parser = Parser()
    my_parser.print_help()

# Generated at 2022-06-14 08:29:30.869736
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    """
    Test Parser with no options, output should be:
    usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER]
                   [--enable-experimental-instant-mode] [-d]
                   [--force-command FORCE_COMMAND]
                   [command [command ...]]
    """
    p = Parser()
    old_output = sys.stderr
    sys.stderr = StringIO()
    p.print_usage()
    sys.stderr = old_output

# Generated at 2022-06-14 08:29:38.163984
# Unit test for constructor of class Parser
def test_Parser():
    """
    test_Parser() perform Unit test for constructor of class Parser.
    If a bug is detected, the function will return False, otherwise
    it will return True.
    """
    p = Parser()
    if (not isinstance(p._parser, object)):
        raise ValueError("wrong object: Parser")
    if (not isinstance(p._parser, ArgumentParser)):
        raise ValueError("wrong parser with new Parser")
    return True


# Generated at 2022-06-14 08:29:43.060217
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    import io
    import sys

    sys.stderr = io.StringIO()

    parser = Parser()
    parser.print_help()

    assert "show this help message and exit" in sys.stderr.getvalue()

# Generated at 2022-06-14 08:30:21.594948
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse([])
    assert args.repeat is False
    assert args.yes is False
    assert args.version is False
    assert args.alias is None
    assert args.shell_logger is None
    assert args.shell_logger is None
    assert args.enable_experimental_instant_mode is False
    assert args.help is False
    assert args.debug is False
    assert args.force_command is None
    assert not args.command
    args = parser.parse([ 'thefuck', '-v' ])
    assert args.repeat is False
    assert args.yes is False
    assert args.version is True
    assert args.alias is None
    assert args.shell_logger is None
    assert args.enable_experimental_instant_mode is False

# Generated at 2022-06-14 08:30:29.389853
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    # mocks and stubs
    class MockFile:
        def __init__(self):
            self.content = ""
        def write(self, content):
            self.content = content
    mock_file = MockFile()
    parser = Parser()

    # test using mock
    parser.print_usage()

    # assert
    assert "usage: thefuck [--version]" in mock_file.content


# Generated at 2022-06-14 08:30:39.824992
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from io import StringIO
    import sys

    sys.stderr = StringIO()
    p = Parser()
    p.print_help()
    help_str = sys.stderr.getvalue()
    assert 'optional arguments' in help_str, help_str
    assert 'show program\'s version number and exit' in help_str, help_str
    assert '--debug' in help_str, help_str

    sys.stderr = StringIO()
    p = Parser()
    p.print_usage()
    usage_str = sys.stderr.getvalue()
    assert 'usage: thefuck' in usage_str, usage_str

# Generated at 2022-06-14 08:30:42.249676
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    assert p is not None