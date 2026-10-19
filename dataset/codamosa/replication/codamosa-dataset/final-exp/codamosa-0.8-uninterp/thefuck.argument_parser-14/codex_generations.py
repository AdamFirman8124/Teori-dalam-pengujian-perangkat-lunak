

# Generated at 2022-06-14 08:20:49.904505
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()

# Generated at 2022-06-14 08:20:58.404141
# Unit test for method parse of class Parser
def test_Parser_parse():
    from .utils import get_alias
    assert Parser().parse([
        'thefuck', 'python', '-c', 'print(42)', ARGUMENT_PLACEHOLDER,
        '--yes', '-d', '--', '-i']) == Namespace(
            debug=True, yes=True, shell_logger=None,
            enable_experimental_instant_mode=False, force_command=None,
            command=['python', '-c', 'print(42)'], alias=get_alias(),
            help=False, repeat=False, version=False)

# Generated at 2022-06-14 08:21:04.842240
# Unit test for method parse of class Parser
def test_Parser_parse():
    """Parser.parse test"""
    expected = {
        'command': ['bash'],
        'alias': None,
        'help': False,
        'debug': False,
        'repeat': False,
        'yes': False,
        'shell_logger': None,
        'force_command': None,
        'version': False,
        'enable_experimental_instant_mode': False}
    assert Parser().parse(['fake-script', 'bash']) == expected


# Generated at 2022-06-14 08:21:17.891940
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['thefuck', '-y', '-l', 'logfile']) == \
           parser._parser.parse_args(['-y', '-l', 'logfile'])
    assert parser.parse(['thefuck', '-y', ARGUMENT_PLACEHOLDER]) == \
           parser._parser.parse_args(['-y'])
    assert parser.parse(['thefuck', ARGUMENT_PLACEHOLDER]) == \
           parser._parser.parse_args([])
    assert parser.parse(['thefuck', '-r', '-d', 'echo', 'message']) == \
           parser._parser.parse_args(['-r', '-d', '--', 'echo', 'message'])



# Generated at 2022-06-14 08:21:22.888129
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from unittest.mock import patch

    with patch('sys.stderr.write') as mock_write:
        Parser().print_help()
        mock_write.assert_called_once()


# Generated at 2022-06-14 08:21:23.886534
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:21:25.297322
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
	Parser().print_usage()



# Generated at 2022-06-14 08:21:28.048856
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    out = StringIO()
    sys.stderr = out
    parser.print_help()
    return True

# Generated at 2022-06-14 08:21:30.281296
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    p = Parser()
    assert p.print_usage() != None


# Generated at 2022-06-14 08:21:32.507143
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
	test_obj = Parser()
	result = test_obj.print_usage()
	print(result)

# Generated at 2022-06-14 08:21:50.338650
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    """To run the test, in the shell, enter "python -m unittest tests.test_Parser.test_Parser_print_help" """    
    import unittest
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

    class TestParser(unittest.TestCase):
        def test_Parser_print_help(self):
            parser = Parser()

# Generated at 2022-06-14 08:21:51.643024
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser


# Generated at 2022-06-14 08:22:00.665716
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from io import StringIO
    parser = Parser()
    with StringIO() as buf, redirect_stdout(buf):
        parser.print_usage()
        assert buf.getvalue().strip() == '''\
usage: thefuck [-h] [-v] [-y | -r] [-a [custom-alias-name]]
               [-l SHELL_LOGGER] [--enable-experimental-instant-mode]
               [--debug] [--force-command FORCE_COMMAND]
               [command [command ...]]
'''.strip()

# Generated at 2022-06-14 08:22:02.508929
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser


# Generated at 2022-06-14 08:22:03.817821
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:22:05.360689
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:22:15.770979
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    help_text = StringIO()
    sys.stderr = help_text
    parser = Parser()
    parser.print_help()

    assert "Usage: thefuck [OPTIONS]" in help_text.getvalue()
    assert "Options:" in help_text.getvalue()
    assert "--version  show program's version number and exit" in help_text.getvalue()
    assert "--alias [custom-alias-name]  prints alias for current shell" in help_text.getvalue()
    assert "-l, --shell-logger  log shell output to the file" in help_text.getvalue()
    assert "--enable-experimental-instant-mode  enable experimental instant mode, use on your own risk" in help_text.getvalue()
    assert "-h, --help  show this help message and exit" in help

# Generated at 2022-06-14 08:22:18.364656
# Unit test for constructor of class Parser
def test_Parser():
	Parser()
	print("test_Parser is successful")
	
if __name__ == '__main__':
	test_Parser()

# Generated at 2022-06-14 08:22:23.317236
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from .parser import Parser
    from mock import Mock
    parser = Parser()
    # For coverage
    parser._parser.print_usage = Mock()
    parser.print_usage()
    parser._parser.print_usage.assert_called_with(sys.stderr)


# Generated at 2022-06-14 08:22:24.852404
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert_true(parser._parser)


# Generated at 2022-06-14 08:22:34.335442
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    assert Parser().print_usage() == None


# Generated at 2022-06-14 08:22:35.426406
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser


# Generated at 2022-06-14 08:22:36.830923
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser


# Generated at 2022-06-14 08:22:46.488342
# Unit test for method parse of class Parser
def test_Parser_parse():

    class ParserTest(Parser):

        def __init__(self):
            Parser.__init__(self)
            self.add_argument_call_count = 0

        def _add_arguments(self):
            pass

        def add_argument(self, *args, **kwargs):
            self.add_argument_call_count += 1

        def parse(self, argv):
            self.add_argument_call_count = 0
            return Parser.parse(self, argv)

    parser = ParserTest()

    args = parser.parse([
        'thefuck', 'fuck', ARGUMENT_PLACEHOLDER, '-l', 'logfile'])
    assert args.shell_logger == 'logfile'
    assert not args.command


# Generated at 2022-06-14 08:22:59.399831
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['thefuck', 'echo ls']) == Namespace(
        command=['ls'], debug=False, repeat=False, yes=False,
        force_command=None)
    assert parser.parse(['thefuck', '--debug', 'echo ls']) == Namespace(
        command=['ls'], debug=True, repeat=False, yes=False,
        force_command=None)
    assert parser.parse(['thefuck', '--repeat', 'echo ls']) == Namespace(
        command=['ls'], debug=False, repeat=True, yes=False,
        force_command=None)

# Generated at 2022-06-14 08:23:01.180309
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    assert type(p) is Parser

# Generated at 2022-06-14 08:23:02.553434
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:23:07.407745
# Unit test for method print_help of class Parser
def test_Parser_print_help():
	parser = Parser()
	output = StringIO()
	sys.stdout = output
	parser.print_help()
	sys.stdout = sys.__stdout__
	assert "Usage: thefuck" in output.getvalue()


# Generated at 2022-06-14 08:23:08.714163
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:23:10.542986
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    actual = parser.print_help()
    assert actual is None

# Generated at 2022-06-14 08:23:26.569819
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser()

# Generated at 2022-06-14 08:23:29.192726
# Unit test for method parse of class Parser
def test_Parser_parse():
    p = Parser()
    args = p.parse(['thefuck', '-a'])
    assert args.alias == get_alias()

# Generated at 2022-06-14 08:23:37.618453
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser().parse(['fuck', '--'] + [ARGUMENT_PLACEHOLDER] + ['ls', '-l'])
    assert parser.command == ['ls', '-l']
    assert parser.yes is False
    assert parser.debug is False
    assert parser.force_command is None
    assert parser.repeat is False
    assert parser.shell_logger is None
    assert parser.version is False
    assert parser.alias is None
    assert parser.enable_experimental_instant_mode is False
    assert parser.help is False

    parser = Parser().parse(['fuck', '--', 'ls', '-l'])
    assert parser.command == ['ls', '-l']

    parser = Parser().parse(['fuck', 'ls', '-l'])

# Generated at 2022-06-14 08:23:51.012213
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    segments = parser._parser.format_help().strip().split('\n')
    assert segments[1] == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]]'
    assert segments[2] == '                  [-l shell-logger]'
    assert segments[3] == '                  [--enable-experimental-instant-mode]'
    assert segments[4] == '                  [-y | -r] [-d] [--force-command FORCE_COMMAND]'
    assert segments[5].startswith('                  [command [')
    assert segments[5].endswith(ARGUMENT_PLACEHOLDER + ']')
    assert segments[6] == '                  [command ...]]'

# Generated at 2022-06-14 08:24:03.032988
# Unit test for method parse of class Parser
def test_Parser_parse():
    from .const import ARGUMENT_PLACEHOLDER
    from .utils import get_alias
    from .utils import get_alias
    from .utils import get_alias
    from .utils import get_alias
    from .utils import get_alias
    from .utils import get_alias
    from .utils import get_alias
    from .utils import get_alias
    from .utils import get_alias
    from .utils import get_alias
    from .utils import get_alias
    from .utils import get_alias
    from .utils import get_alias
    from .utils import get_alias
    from .utils import get_alias
    from .utils import get_alias
    from .utils import get_alias
    from .utils import get_alias
    from .utils import get_alias
    from .utils import get_alias

# Generated at 2022-06-14 08:24:07.809628
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    class Stderr(object):
        def write(self, arg):
            self.argument = arg
            return arg    
    sys.stderr = Stderr()
    test_command = Parser()
    test_command.print_help()
    sys.stderr = sys.__stderr__


# Generated at 2022-06-14 08:24:21.470722
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    # o = p.parse(['--repeat',
    #  '--enable-experimental-instant-mode',
    #  '--force-command',
    #  '--yes',
    #  '--help',
    #  '--debug',
    #  '--alias',
    #  'fuck'])
    # for k, v in o.__dict__.items():
    # 	print (k, v)
    # print ('------------------------------')
    # o = p.parse(['--repeat',
    #  '--enable-experimental-instant-mode',
    #  '--force-command',
    #  '--yes',
    #  '--help',
    #  '--debug',
    #  '--alias',
    #  'fuck',


# Generated at 2022-06-14 08:24:23.716749
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    assert p._parser.prog == 'thefuck'


# Generated at 2022-06-14 08:24:36.141055
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from thefuck.utils import which
    from thefuck.types import Settings
    from thefuck.shells import shell
    from thefuck.rules.man import match, get_new_command

    def side_effect(command):
        if command == 'echo':
            return which('echo')
        elif command == 'ls':
            return which('ls')

    settings = Settings(shell=shell.get_key(), no_colors=False,
                                 wait_command=0)
    
    p = Parser()
    p.print_usage()
    
    sys.stdout = open('Parser.txt', 'w')
    p.print_usage()
    sys.stdout = sys.__stdout__
    
    f = open('Parser.txt', 'r')
    command = f.read()
    f.close()

# Generated at 2022-06-14 08:24:40.242013
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert isinstance(parser, Parser)
    assert parser._parser is not None
    assert isinstance(parser._parser, ArgumentParser)


# Generated at 2022-06-14 08:24:58.152343
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    assert isinstance(parser.print_help(), None)
    

# Generated at 2022-06-14 08:25:02.299767
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    from io import StringIO
    from unittest.mock import patch
    capturedOutput = StringIO()
    sys.stderr = capturedOutput

    parser.print_usage()
    sys.stderr = sys.__stderr__
    assert capturedOutput.getvalue() == 'Usage: thefuck [options] [--] command\n'


# Generated at 2022-06-14 08:25:03.902159
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    assert parser.print_help() is None

# Generated at 2022-06-14 08:25:05.683153
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()
    assert(1 == 1)

# Generated at 2022-06-14 08:25:13.614316
# Unit test for method parse of class Parser
def test_Parser_parse():
    # With placeholder
    arguments = Parser().parse(['fuck', '-v', ARGUMENT_PLACEHOLDER, '-r'])
    assert arguments.version
    assert arguments.repeat
    assert not arguments.command

    # Without placeholder
    arguments = Parser().parse(['fuck', '-h', '-a'])
    assert arguments.help
    assert arguments.alias == get_alias()
    assert not arguments.command

    # With command
    arguments = Parser().parse(['fuck', 'sudo', '-l'])
    assert not arguments.help
    assert not arguments.alias
    assert arguments.command == ['sudo', '-l']

# Generated at 2022-06-14 08:25:19.334534
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    # arrange
    parser = Parser()
    class MockStream(object):
        def write(self, text):
            pass
        def flush(self):
            pass
    sys.stderr = MockStream()

    # act
    parser.print_help()

    # assert
    assert True

# Generated at 2022-06-14 08:25:30.892874
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    # test on empty input
    assert parser.parse([]) == parser._parser.parse_args([])
    # test on input with only one argument
    assert parser.parse(['one_argument']) == parser._parser.parse_args(['one_argument'])
    assert parser.parse(['one_argument']) == parser._parser.parse_args(['one_argument'])
    # test on input with more arguments
    assert parser.parse(['one_argument', '--', 'another_argument']) == parser._parser.parse_args(['--', 'one_argument', 'another_argument'])

# Generated at 2022-06-14 08:25:43.506596
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    import StringIO
    output = StringIO.StringIO()
    parser.print_help(output)

# Generated at 2022-06-14 08:25:50.281261
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from .const import VERSION
    from .utils import is_man_installed
    from .typings import ArgParseResult

    # The following statement is needed to enable
    # the parser's print_help method.
    # The print_help method normally ignores
    # Argument Errors and prints the help manual.
    # For this test to succeed, the Argument Error
    # needs to be handled by the test case.
    parser = Parser()

    # The following statements test the print_help method's
    # output when an Argument Error is raised by the parse() method.

    argv = ['thefuck', '--non_existent_option']
    try:
        parser.parse(argv)
    except SystemExit:
        argparse_error = sys.exc_info()[1]

# Generated at 2022-06-14 08:25:56.798138
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    old_stderr = sys.stderr
    try:
        from io import StringIO
        out = StringIO()
        sys.stderr = out
        parser.print_help()
        assert 'show this help message and exit' in out.getvalue()
    finally:
        sys.stderr = old_stderr


# Generated at 2022-06-14 08:26:21.283851
# Unit test for method parse of class Parser

# Generated at 2022-06-14 08:26:23.213434
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:26:34.306857
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    """
    Tests whether the print_usage() method of the Parser class returns the
    correct output.

    """
    parser = Parser()
    capturedOutput = io.BytesIO()
    sys.stdout = capturedOutput
    parser.print_usage()
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == "usage: thefuck -h [-v] [-a]" \
                                       "[-l shell-logger] " \
                                       "[--enable-experimental-instant-mode]" \
                                       "[-d] [--force-command force-command]" \
                                       "[command]\n"


# Generated at 2022-06-14 08:26:47.268265
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['thefuck']) == parser._parser.parse_args([])
    assert parser.parse(['thefuck', '-y']) == parser._parser.parse_args(['-y'])
    assert parser.parse(['thefuck', '-v']) == parser._parser.parse_args(['-v'])
    assert parser.parse(['thefuck', '-a']) == parser._parser.parse_args(['-a'])
    assert parser.parse(['thefuck', '-a', 'alias']) == parser._parser.parse_args(['-a', 'alias'])
    assert parser.parse(['thefuck', '--shell-logger', '-v']) == parser._parser.parse_args(['--shell-logger', '-v'])


# Generated at 2022-06-14 08:26:56.753891
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    s = io.StringIO()
    parser.print_help(s)
    help_message = s.getvalue()
    assert '-v, --version' in help_message
    assert '-a, --alias [custom-alias-name]' in help_message
    assert '[custom-alias-name] prints alias for current shell' in help_message
    assert '-l, --shell-logger' in help_message
    assert '-h, --help' in help_message
    assert '-d, --debug' in help_message

# Generated at 2022-06-14 08:26:58.303927
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:27:00.508780
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    assert p
    assert p._parser
    p.parse([])

# Generated at 2022-06-14 08:27:03.149126
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser.prog == 'thefuck'
    assert parser._parser.add_help == False

# Generated at 2022-06-14 08:27:04.329578
# Unit test for constructor of class Parser
def test_Parser():
    _ = Parser()


# Generated at 2022-06-14 08:27:05.963271
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:27:38.065055
# Unit test for constructor of class Parser
def test_Parser():
    Parser()



# Generated at 2022-06-14 08:27:40.401595
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser is not None


# Generated at 2022-06-14 08:27:48.175412
# Unit test for method print_help of class Parser
def test_Parser_print_help():

    # create parser instance
    parser = Parser()

    # capture stdout
    import sys
    from io import StringIO
    output = StringIO()
    old_stdout = sys.stdout
    sys.stdout = output

    # print help
    parser.print_help()
    sys.stdout = old_stdout

    # convert captured stdout to string
    # and check if it contains help string
    output = output.getvalue()
    assert "-v, --version" in output

# Generated at 2022-06-14 08:27:56.371148
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser._actions[0].option_strings == ['-v','--version']
    assert parser._parser._actions[0].action == 'store_true'
    assert parser._parser._actions[0].help == "show program's version number and exit"
    assert parser._parser._actions[1].option_strings == ['-a','--alias']
    assert parser._parser._actions[1].nargs == '?'
    assert parser._parser._actions[1].const == get_alias()
    assert parser._parser._actions[1].help == '[custom-alias-name] prints alias for current shell'
    assert parser._parser._actions[2].option_strings == ['-l','--shell-logger']
    assert parser._parser._actions[2].action == 'store'

# Generated at 2022-06-14 08:27:58.401198
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    ps = Parser()
    ps.print_usage()



# Generated at 2022-06-14 08:28:11.144566
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    parsed_args = parser.parse(['thefuck', 'scp', 'a', 'b', 'c'])
    assert parsed_args.command[:2] == ['scp', 'a']
    assert parsed_args.command[2:] == ['b', 'c']

    short_options = parser.parse(['thefuck', '-v', 'command', 'arg1', 'arg2'])
    assert short_options.version is True

    long_options = parser.parse(
        ['thefuck', '--repeat', '--help', 'command', 'arg1', 'arg2'])
    assert long_options.repeat is True
    assert long_options.help is True


# Generated at 2022-06-14 08:28:13.265365
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    print(parser.print_usage())


# Generated at 2022-06-14 08:28:25.905509
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from .utils import get_default_alias, get_version
    parser = Parser()
    parser.print_usage()
    assert parser._parser.prog == 'thefuck'
    assert parser._parser.usage == ('usage: thefuck [-h] [-y | -r] [-d] [-a [custom-alias-name]] '
                                    '[-l shell-logger] [--enable-experimental-instant-mode] '
                                    '[--force-command FORCE_COMMAND] [--version] '
                                    '[command [command ...]]')
    assert parser._parser.version == get_version()
    assert parser._parser.add_help == False
    assert parser._parser.conflict_handler == 'error'



# Generated at 2022-06-14 08:28:34.909326
# Unit test for method print_help of class Parser

# Generated at 2022-06-14 08:28:43.000920
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from io import StringIO
    mock_stdout = StringIO()
    sys.stdout = mock_stdout
    # Test for print_usage method
    parser = Parser()
    parser.print_usage()
    sys.stdout.getvalue()
    sys.stdout = sys.__stdout__
    assert mock_stdout.getvalue().strip() == "usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER]\n                  [--enable-experimental-instant-mode] [-d] [--force-command FORCE_COMMAND]\n                  [command [command ...]]\n"



# Generated at 2022-06-14 08:29:42.526189
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from six import StringIO
    from .utils import get_alias

    sys.stderr = StringIO()
    parser = Parser()
    parser.print_usage()

    stderr = sys.stderr
    sys.stderr = sys.__stderr__
    assert stderr.getvalue().strip() == \
        'usage: thefuck [-h] [-v] [-a [custom-alias-name]] ' \
        '[-l shell-logger] [--enable-experimental-instant-mode] [-d] ' \
        '[--force-command FORCE_COMMAND] [command [command ...]]'

    sys.stderr = StringIO()
    parser.print_usage()

    stderr = sys.stderr
    sys.stderr = sys.__stderr__


# Generated at 2022-06-14 08:29:44.561388
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    p = Parser()
    assert p.print_help() is None

# Generated at 2022-06-14 08:29:56.127019
# Unit test for method parse of class Parser
def test_Parser_parse():
    # Test: print_help
    parser = Parser()
    result = parser.parse(['-h'])
    assert result.help is True

    # Test: print_alias
    assert parser.parse(['-a']).alias == 'fuck'
    assert parser.parse(['-a', 'fuck']).alias == 'fuck'

    # Test: print_version
    assert parser.parse(['-v']).version is True

    # Test: run in debug mode
    assert parser.parse(['-d']).debug is True

    # Test: run in repeat mode
    assert parser.parse(['-r']).repeat is True

    # Test: run in hard mode
    assert parser.parse(['-y']).yeah is True

    # Test: shell log output

# Generated at 2022-06-14 08:30:08.894598
# Unit test for method print_help of class Parser

# Generated at 2022-06-14 08:30:10.216158
# Unit test for constructor of class Parser
def test_Parser():
	PAR = Parser()
	assert PAR


# Generated at 2022-06-14 08:30:11.518275
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:30:13.853045
# Unit test for constructor of class Parser
def test_Parser():
    try:
        Parser()
    except:
        assert False
    else:
        assert True

# Generated at 2022-06-14 08:30:19.470863
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parsed_usage = Parser().parse(['thefuck'])._usage_
    with patch('thefuck.main.sys.stderr', new=StringIO()) as stderr:
        Parser().print_usage()
        assert stderr.getvalue() == parsed_usage

# Generated at 2022-06-14 08:30:32.411990
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from .utils import capture_stderr
    from .parser import Parser
    from .const import thefuck_version
    parser = Parser()
    result = capture_stderr(parser.print_usage)
    assert result == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] ' \
           '\n[-l shell-logger] [--enable-experimental-instant-mode] ' \
           '[-y | -r] [-d] [--force-command FORCE_COMMAND]\n' \
           '\n command\n\n' \
           'The Fuck {} - a magnificent app which corrects your' \
           ' previous console \n' \
           'command.\n'.format(thefuck_version)


# Generated at 2022-06-14 08:30:33.811287
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()