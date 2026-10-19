

# Generated at 2022-06-14 08:20:57.250489
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['/usr/bin/fuck', 'ls', '-la']) == \
           parser._parser.parse_args(['--', 'ls', '-la'])
    assert parser.parse(['/usr/bin/fuck', 'ls', '-la', ARGUMENT_PLACEHOLDER, '-l', '-a']) == \
           parser._parser.parse_args(['-l', '-a', '--', 'ls', '-la'])

# Generated at 2022-06-14 08:20:59.871483
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    assert p._parser.prog == 'thefuck'
    assert not p._parser.add_help
        

# Generated at 2022-06-14 08:21:07.872399
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    import sys
    import io
    import unittest

    sys.stderr = io.StringIO()
    Parser().print_help()

# Generated at 2022-06-14 08:21:18.274955
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    """Test for method print_help of class Parser"""
    parser = Parser()
    help_lines = parser.print_help().split('\n')
    assert help_lines[-6] == 'optional arguments:'
    assert help_lines[-5] == '  -l, --shell-logger LOGFILE'
    assert help_lines[-4] == '                        log shell output to the file'
    assert help_lines[-3] == '  --enable-experimental-instant-mode'
    assert help_lines[-2] == '                        enable experimental instant mode, use on your own risk'
    assert help_lines[-1] == '  -h, --help            show this help message and exit'

# Generated at 2022-06-14 08:21:25.110308
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert hasattr(parser._parser, 'add_argument')
    assert hasattr(parser._parser, 'print_usage')
    assert hasattr(parser._parser, 'print_help')
    assert hasattr(parser, 'print_help')
    assert hasattr(parser, 'print_usage')


# Generated at 2022-06-14 08:21:30.517299
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    import sys
    from os import devnull
    oput = sys.stderr
    sys.stderr = open(devnull, 'w')
    args = Parser().parse([])
    assert args.help == True
    sys.stderr.close()
    sys.stderr = oput


# Generated at 2022-06-14 08:21:39.492179
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    output_file = open('output_file.txt', 'w')
    parser = Parser()
    parser.print_help()
    output_file.write(sys.stderr.getvalue())
    output_file.close()
    output_file = open('output_file.txt', 'r')

# Generated at 2022-06-14 08:21:44.516469
# Unit test for method parse of class Parser
def test_Parser_parse():
    parsed_args = Parser().parse(['fuck', '-d', '--', 'test', 'command', 'with', 'args', ARGUMENT_PLACEHOLDER, '--', '--fuck-me'])
    assert parsed_args.debug == True
    assert parsed_args.command == ['test', 'command', 'with', 'args', '--fuck-me']
    assert ARGUMENT_PLACEHOLDER not in parsed_args.command
    assert len(parsed_args.command) == 5



# Generated at 2022-06-14 08:21:45.888955
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser is not None

# Generated at 2022-06-14 08:21:47.318131
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser is not None

# Generated at 2022-06-14 08:22:03.968061
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    class args_namespace(object):
        def __init__(self, args):
            for k, v in args.iteritems():
                setattr(self, k, v)
    # argv = ['']
    result = args_namespace(parser.parse([]))
    assert result.help == False
    # argv = ['-h']
    result = args_namespace(parser.parse(['-h']))
    assert result.help == True
    # argv = ['--help']
    result = args_namespace(parser.parse(['--help']))
    assert result.help == True
    # argv = ['command']
    result = args_namespace(parser.parse(['command']))
    assert result.command == ['command']
    # argv = ['command1

# Generated at 2022-06-14 08:22:05.288690
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser

# Generated at 2022-06-14 08:22:14.657151
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from .utils import get_alias

    parser = Parser()
    parser._parser.prog = 'thefuck'
    parser._parser.add_argument('-a', '--alias', nargs='?', const=get_alias(), help='[custom-alias-name] prints alias for current shell')
    parser._parser.add_argument('-h', '--help', action='store_true', help='show this help message and exit')
    parser._parser.add_argument('command', nargs='*', help='command that should be fixed')
    f = sys.stderr

    parser.print_usage()
    output = f.getvalue().strip()
    assert output == 'usage: thefuck [-a [custom-alias-name]] [-h] [command ...]'


# Generated at 2022-06-14 08:22:16.274347
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:22:26.274236
# Unit test for method parse of class Parser
def test_Parser_parse():
    test_input = ['-l', '-t', 'test', '--force-command']
    res = Parser()._prepare_arguments(test_input)
    assert res == ['--', '-t', 'test']
    res = Parser()._prepare_arguments(['-t', 'test'])
    assert res == ['--', '-t', 'test']
    res = Parser().parse(['/usr/bin/fuck', '-v'])
    assert res.version is True
    res = Parser().parse(['/usr/bin/fuck', '-l', '--force-command'])
    assert res.shell_logger is None

if __name__ == '__main__':
    test_Parser_parse()

# Generated at 2022-06-14 08:22:34.387547
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert '-v, --version' in parser.print_usage()
    assert '-a, --alias' in parser.print_usage()
    assert '-l, --shell-logger' in parser.print_usage()
    assert '--enable-experimental-instant-mode' in parser.print_usage()
    assert '-h, --help' in parser.print_usage()
    assert '-d, --debug' in parser.print_usage()
    assert 'command' in parser.print_usage()


# Generated at 2022-06-14 08:22:35.046696
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    Parser().print_help()

# Generated at 2022-06-14 08:22:36.665997
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:22:47.103542
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(['thefuck', 'echo', 'hello', 'world', '--alias', 'fuck'])
    assert args.command == ['echo', 'hello', 'world']
    assert args.alias == 'fuck'
    assert not args.debug
    assert not args.enable_experimental_instant_mode
    assert not args.help
    assert not args.shell_logger
    assert not args.version
    assert not args.yes
    assert not args.repeat

    args = parser.parse(
        ['thefuck', '-a', 'fuck', 'echo', 'hello', 'world'])
    assert args.alias == 'fuck'

    args = parser.parse(
        ['thefuck', '--alias', 'fuck', 'echo', 'hello', 'world'])
    assert args.alias

# Generated at 2022-06-14 08:22:54.308318
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
        
    # Method should print to stderr
    old_stderr = sys.stderr
    try:
        from cStringIO import StringIO
        sys.stderr = StringIO()
        parser.print_usage()
        assert 'usage: thefuck' in sys.stderr.getvalue()
    finally:
        sys.stderr = old_stderr


# Generated at 2022-06-14 08:23:17.250573
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()

    assert parser.parse(sys.argv).command == []
    assert parser.parse(sys.argv + ['ls']).command == ['ls']
    assert parser.parse(sys.argv + ['ls', '-la']).command == ['ls', '-la']
    assert parser.parse(sys.argv + [ARGUMENT_PLACEHOLDER, 'ls', '-la']).command == ['ls', '-la']
    assert parser.parse(sys.argv + ['ls', ARGUMENT_PLACEHOLDER, '-la']).command == ['-la']

# Generated at 2022-06-14 08:23:19.067763
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser is not None


# Generated at 2022-06-14 08:23:21.882043
# Unit test for constructor of class Parser
def test_Parser():
    print ("Running test_Parser...")
    assert type(Parser()) == Parser


# Generated at 2022-06-14 08:23:22.607706
# Unit test for constructor of class Parser
def test_Parser():
    Parser()

# Generated at 2022-06-14 08:23:32.615781
# Unit test for method parse of class Parser
def test_Parser_parse():
    # Setup
    parser = Parser()
    argv1 = ['/path/to/binary', 'echo', 'X', 'Y']
    argv2 = ['/path/to/binary', 'echo', ARGUMENT_PLACEHOLDER, 'X', 'Y']

    # Test
    result1 = parser.parse(Parser()._prepare_arguments(argv1))
    result2 = parser.parse(Parser()._prepare_arguments(argv2))

    # Assert
    assert result1.command == ['echo', 'X', 'Y']
    assert result2.command == ['X', 'Y']


# Generated at 2022-06-14 08:23:34.608323
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    p = Parser()
    p.print_usage()


# Generated at 2022-06-14 08:23:38.288750
# Unit test for method parse of class Parser
def test_Parser_parse():
    args = Parser().parse(['prog', 'edit', 'file', '--opt', 'arg'])
    assert args.command == ['edit', 'file', '--opt', 'arg']



# Generated at 2022-06-14 08:23:51.300413
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from .output import print_usage, print_alias, print_empty_line
    from .utils import print_error
    from .const import NOTHING_TO_FIX, FAILED_CMD_MSG, ALIAS_MANUAL

    class _parser(Parser):
        def _add_arguments(self):
            self._parser.add_argument(
                '-a', '--alias',
                nargs='?',
                const=get_alias(),
                help='[custom-alias-name] prints alias for current shell')
            self._parser.add_argument(
                '-h', '--help',
                action='store_true',
                help='show this help message and exit')

    class _output(object):
        @staticmethod
        def __instancecheck__(inst):
            return True


# Generated at 2022-06-14 08:24:03.291559
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    """
    Test print_help method of class Parser()
    """
    # first, get the argument parser
    parser = Parser()
    # the _add_arguments method of the Parser class has been tested before
    # so we can skip this step
    # check if the print_help method prints the help for the program to stdout
    # the stderr is saved, because later we want to check if the help is printed
    # to stderr
    #
    # also, the stderr is saved in a variable sys_stderr
    sys_stderr = sys.stderr
    # save the stderr
    sys.stderr = StringIO()
    # call the print_help method
    parser.print_help()
    # get the output of the print_help method

# Generated at 2022-06-14 08:24:07.961943
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    """Unit test for Parser.print_help, it should print the help message to STDOUT"""
    result_file   = 'result_file.txt'
    sys.stdout    = open(result_file, 'w')
    parser        = Parser()
    parser.print_help()
    assert open(result_file, 'r').read()

# Generated at 2022-06-14 08:24:27.168143
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    args = Parser()
    output = args.print_help()
    assert output == None

# Generated at 2022-06-14 08:24:38.726238
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    # Unit test for _add_arguments
    from .utils import get_alias
    test_alias = get_alias() if get_alias() is not None else '[custom-alias-name]'
    assert parser._parser.parse_args('-a'.split())
    assert parser._parser.parse_args(('-a ' + test_alias).split())
    # Unit test for _add_conflicting_arguments
    assert not parser._parser.parse_args('-y'.split()).repeat
    assert not parser._parser.parse_args('-r'.split()).yes
    assert not parser._parser.parse_args('-y'.split()).debug
    # Unit test for _prepare_arguments
    arguments = '-h'.split()

# Generated at 2022-06-14 08:24:40.505155
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()


# Generated at 2022-06-14 08:24:41.837043
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser
    return parser

# Generated at 2022-06-14 08:24:53.791254
# Unit test for method parse of class Parser
def test_Parser_parse():
    from .. import main
    args = main.Parser().parse(['thefuck', '--', 'ls', '-al'])
    assert args.command == ['ls', '-al']
    args = main.Parser().parse(['thefuck', '--', 'ls', '-al', ARGUMENT_PLACEHOLDER, '--force-command'])
    assert args.command == ['ls', '-al']
    assert args.force_command == '--force-command'
    args = main.Parser().parse(['thefuck', ARGUMENT_PLACEHOLDER, '--force-command'])
    assert args.command == []
    assert args.force_command == '--force-command'

# Generated at 2022-06-14 08:24:55.512211
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()



# Generated at 2022-06-14 08:24:58.145564
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from .parser import Parser
    parser = Parser()
    parser.print_usage()
    assert True


# Generated at 2022-06-14 08:25:11.418343
# Unit test for method parse of class Parser
def test_Parser_parse():
    from .utils import prepare_arguments
    p = Parser()
    assert p.parse(['thefuck', 'git', 'satus', '--porcelain']) == \
        prepare_arguments(['git', 'satus', '--porcelain'])
    assert p.parse(['thefuck', 'git', 'satus', '--porcelain', ARGUMENT_PLACEHOLDER, '--all']) == \
        prepare_arguments(['--all', 'git', 'satus', '--porcelain'])

# Generated at 2022-06-14 08:25:12.899204
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:25:16.006374
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert 'prog=\'thefuck\', add_help=False' in str(parser._parser)


# Generated at 2022-06-14 08:25:36.810727
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    assert Parser().print_usage() == None


# Generated at 2022-06-14 08:25:41.005767
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    my_parser = Parser()
    target = sys.stderr
    my_parser.print_help()
    target.write(my_parser._parser.format_help())


# Generated at 2022-06-14 08:25:48.550783
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(['thefuck', '-v', '--no-color'])
    assert args.version
    assert not args.shell_logger
    assert not args.help
    assert not args.yes
    assert not args.repeat
    assert not args.debug
    assert not args.force_command

    args = parser.parse(['thefuck', 'some_command', '--no-color'])
    assert not args.version
    assert not args.shell_logger
    assert not args.help
    assert not args.yes
    assert not args.repeat
    assert not args.debug
    assert not args.force_command
    assert args.command == ['some_command']


# Generated at 2022-06-14 08:25:49.897064
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
	Parser().print_usage()

# Generated at 2022-06-14 08:25:54.649230
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()._parser
    stream = StringIO()
    parser.print_help(stream)
    assert "usage: thefuck" in stream.getvalue()
    assert "help\n   --enable-experimental-instant-mode" in stream.getvalue()



# Generated at 2022-06-14 08:25:56.287863
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    # p = Parser()
    # p.print_usage()
    pass

# Generated at 2022-06-14 08:26:05.919351
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from .import utils
    from .utils import replace_argument
    from .shells import get_aliases
    from .main import print_usage

    parser = Parser()
    out = utils.get_output(parser.print_usage)
    usages = out.strip().split('\n')
    assert len(usages) == 2
    assert usages[1].endswith('[-h] [-v] [-a [custom-alias-name]]'
                              ' [-l SHELL_LOGGER] [-y] [-r] [-d] [--] '
                              'command [command ...]')

    assert replace_argument(usages[0], 'thefuck') in get_aliases()

    with utils.mock.patch('thefuck.utils.get_alias', return_value='fuck'):
        out

# Generated at 2022-06-14 08:26:08.303356
# Unit test for constructor of class Parser
def test_Parser():
    parser_obj = Parser()
    assert isinstance(parser_obj, Parser)


# Generated at 2022-06-14 08:26:18.663350
# Unit test for method parse of class Parser
def test_Parser_parse():

    from .utils import which, is_alias

    parser = Parser()

    assert parser.parse(['thefuck']) == parser._parser.parse_args([])

    # Test for case:
    # - execute command without arguments
    # - no placeholder
    assert parser.parse(['thefuck', 'ls']) \
           == parser._parser.parse_args(['--', 'ls'])

    # Test for case:
    # - execute command without arguments
    # - placeholder at the end
    assert parser.parse(['thefuck', 'git', 'comm', 're', 'ARGUMENT_PLACEHOLDER']) \
           == parser._parser.parse_args(['--', 'git', 'comm', 're'])

    # Test for case:
    # - execute command without arguments
    # - placeholder in the middle


# Generated at 2022-06-14 08:26:25.898765
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    argv = [r'C:\Users\Bhuvnesh\Anaconda3\Scripts\thefuck.exe', r'C:\Users\Bhuvnesh\Anaconda3\Scripts\conda.exe', r'list']
    parser.parse(argv)
    parser.print_help()
    assert parser.print_help() == parser.print_help()

# Generated at 2022-06-14 08:26:38.409459
# Unit test for constructor of class Parser
def test_Parser():
    Parser()


# Generated at 2022-06-14 08:26:49.809702
# Unit test for method parse of class Parser
def test_Parser_parse():
    """Unit test for method parse of class Parser."""
    parser = Parser()
    sys.argv = ['thefuck']
    assert parser.parse(sys.argv) == parser._parser.parse_args([])

    sys.argv = ['thefuck', '-h']
    assert parser.parse(sys.argv) == parser._parser.parse_args(['-h'])

    sys.argv = ['thefuck', '-a']
    assert parser.parse(sys.argv) == parser._parser.parse_args(['-a'])

    sys.argv = ['thefuck', '-a', 'fuck']
    assert parser.parse(sys.argv) == parser._parser.parse_args(['-a', 'fuck'])

    sys.argv = ['thefuck', '-v']
   

# Generated at 2022-06-14 08:26:55.564492
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    import mock
    from .parser import Parser

    parser = Parser()

    with mock.patch.object(parser._parser, 'print_usage') as mock_print_usage:
        parser.print_usage()
        mock_print_usage.assert_called_once_with(sys.stderr)


# Generated at 2022-06-14 08:27:05.120933
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser
    argv = ['thefuck', '-v']
    args = parser.parse(argv)
    assert args.version == True
    assert args.alias == None
    assert args.shell_logger == None
    assert args.enable_experimental_instant_mode == None
    assert args.help == None
    assert args.debug == None
    assert args.force_command == None
    assert args.command == []
    assert args.yes == None
    assert args.repeat == None


# Generated at 2022-06-14 08:27:18.168885
# Unit test for method print_help of class Parser

# Generated at 2022-06-14 08:27:19.529182
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser


# Generated at 2022-06-14 08:27:20.651055
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    pass



# Generated at 2022-06-14 08:27:32.284156
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from .utils import get_alias, get_loader
    from .config import Config
    from unittest.mock import patch
    p = Parser()
    assert p.parse(['fuck'])
    assert p.parse(['fuck', '-v'])
    assert p.parse(['fuck', '-a'])
    assert p.parse(['fuck', '-a', 'dry-run'])
    assert p.parse(['fuck', '-l', 'shell_logger'])
    assert p.parse(['fuck', '--enable-experimental-instant-mode'])
    assert p.parse(['fuck', '-h'])
    assert p.parse(['fuck', '-d'])
    assert p.parse(['fuck', '--force-command', 'python'])

# Generated at 2022-06-14 08:27:34.034664
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser is not None


# Generated at 2022-06-14 08:27:41.416298
# Unit test for method parse of class Parser
def test_Parser_parse():
    argv = ['thefuck', '--yes', 'git']
    args = Parser().parse(argv)
    assert args.yes == True
    assert args.command == ['git']
    argv = ['thefuck', 'git', 'commit']
    args = Parser().parse(argv)
    assert args.command == ['git', 'commit']
    argv = ['thefuck', 'git', 'commit', '--', '-v']
    args = Parser().parse(argv)
    assert args.command == ['git', 'commit', '-v']
    argv = ['thefuck', 'ls', ARGUMENT_PLACEHOLDER, '-l']
    args = Parser().parse(argv)
    assert args.command == ['ls', '-l']

# Generated at 2022-06-14 08:28:16.872243
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from .tests.utils import capture_stderr
    with capture_stderr() as stderr:
        Parser().print_help()
    assert "usage: thefuck [-h] [-v] [-a [custom-alias-name]]\n" in stderr
    assert "[-d] [-y | -r] [--force-command FORCE_COMMAND]\n" in stderr
    assert "command ...\n" in stderr
    assert "\n" in stderr
    assert "optional arguments:\n" in stderr
    assert "-h, --help            show this help message and exit\n" in stderr
    assert "-v, --version         show program's version number and exit\n" in stderr
    assert "-a, --alias [custom-alias-name]\n" in stder

# Generated at 2022-06-14 08:28:22.718376
# Unit test for method parse of class Parser
def test_Parser_parse():
    p = Parser()

    argument = "thefuck root {} --add-some-flag ./some/script.py".format(ARGUMENT_PLACEHOLDER)
    argument = argument.split()
    result = p.parse(argument)
    result.instant = False

    assert 'root' in result.command



# Generated at 2022-06-14 08:28:33.341517
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse([''])
    assert not args.version
    assert not args.alias
    assert not args.shell_logger
    assert not args.enable_experimental_instant_mode
    assert not args.help
    assert not args.yes
    assert not args.repeat
    assert not args.debug
    assert not args.force_command
    assert not args.command
    args = parser.parse(['', '-v'])
    assert args.version
    assert not args.alias
    assert not args.shell_logger
    assert not args.enable_experimental_instant_mode
    assert not args.help
    assert not args.yes
    assert not args.repeat
    assert not args.debug
    assert not args.force_command
    assert not args.command
    args

# Generated at 2022-06-14 08:28:35.217421
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:28:36.322845
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    parser.parse(["thefuck", "hello"])

# Generated at 2022-06-14 08:28:46.245504
# Unit test for method parse of class Parser
def test_Parser_parse():
    import unittest
    import io
    import sys
    # Assume parser is Parser
    parser = Parser()
    # Assume sys.stderr.getvalue() is equivalent of
    # getvalue of io.StringIO which has been used
    # as substitute for sys.stderr
    stderr = io.StringIO()
    sys.stderr = stderr
    # Assume argv is the argument input
    argv = ['-v']
    # Assume parseObj is the parse_args result
    parseObj = parser.parse(argv)
    # Assume that the result of parse_args is stored
    # in namespace
    assert parseObj.version
    # Assume that expected output is defined in a string

# Generated at 2022-06-14 08:28:51.022895
# Unit test for method parse of class Parser
def test_Parser_parse():
    args = Parser().parse(['thefuck', 'echo', 'haha', '--force-command'])
    assert (args.command == ['echo', 'haha'] and
            args.debug == False and
            args.force_command == None and
            args.alias == None and
            args.debug == args.debug and
            args.help == False and
            args.repeat == False and
            args.shell_logger == None and
            args.version == False and
            args.yeah == False)


# Generated at 2022-06-14 08:28:52.153408
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser

# Generated at 2022-06-14 08:28:54.258579
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    try:
        parser.print_usage()
    except IOError:
        assert True
    else:
        assert False

# Generated at 2022-06-14 08:28:59.008810
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from .main import get_parser
    parser = get_parser()
    usage_text = parser.print_usage()
    assert usage_text == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l shell_logger] [--enable-experimental-instant-mode] [-d] [--force-command force_command] [-y | -r] [--] [command [command ...]]', 'test_Parser_print_usage failed'



# Generated at 2022-06-14 08:30:01.826010
# Unit test for method parse of class Parser
def test_Parser_parse():
	"""
	Node for testing for Unit test for method parse of class Parser
	"""
	p = Parser()
	argv = ['thefuck', '--version']
	assert p.parse(argv).version == True
	argv = ['thefuck', '-v']
	assert p.parse(argv).version == True
	argv = ['thefuck', '--version', '--alias']
	assert p.parse(argv).version == True
	assert p.parse(argv).alias == get_alias()
	argv = ['thefuck', '--version', '--alias', 'fuck']
	assert p.parse(argv).version == True
	assert p.parse(argv).alias == 'fuck'

# Generated at 2022-06-14 08:30:12.045128
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from .utils import capture_secho, capture_output
    from .parser import Parser
    with capture_output() as (out, _):
        Parser().print_usage()
    msg = str(out)

    assert(msg == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]]\n              [-l SHELL_LOGGER]\n              [--enable-experimental-instant-mode] [-d] [--force-command FORCE_COMMAND]\n              [--] [command [command ...]]\n')


# Generated at 2022-06-14 08:30:17.014938
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    import io 
    import sys
    
    try:
        sys.stderr = io.StringIO()
        parser = Parser()
        parser.print_usage()
    finally:
        sys.stderr = sys.__stderr__
    


# Generated at 2022-06-14 08:30:27.294239
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    test_argv = [
        '/home/miraculix/.pyenv/shims/thefuck',
        'git lg',
        '--',
        '-d'
    ]
    arguments = parser._prepare_arguments(test_argv[1:])
    assert arguments == ['--', '-d']

    arguments = parser._prepare_arguments([
        '/home/miraculix/.pyenv/shims/thefuck',
        'git',
        '--',
        'lg',
        '-d'
    ])
    assert arguments == ['--', 'lg', '-d']

# Generated at 2022-06-14 08:30:37.149185
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(['thefuck', 'ls', '-la', ARGUMENT_PLACEHOLDER, '-d'])
    assert args.debug
    assert args.command == ['ls', '-la']

    args = parser.parse(['thefuck', 'ls', '-la', '-d'])
    assert args.debug
    assert args.command == ['ls', '-la']

    args = parser.parse(['thefuck', '-d', 'ls', '-la'])
    assert args.debug
    assert args.command == []

    args = parser.parse(['thefuck', '-d'])
    assert args.debug
    assert args.command == []

# Generated at 2022-06-14 08:30:40.837906
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['thefuck', ARGUMENT_PLACEHOLDER]) == \
        parser.parse(['thefuck'])

# Generated at 2022-06-14 08:30:43.178826
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    assert isinstance(p, Parser)



# Generated at 2022-06-14 08:30:45.294152
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_help()
    assert True
