

# Generated at 2022-06-14 08:20:53.579536
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    assert(parser.print_help())

test_Parser_print_help()

# Generated at 2022-06-14 08:20:58.022396
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    out = StringIO()
    parser = Parser()
    parser.print_usage(file=out)
    assert "Usage: thefuck [-h] [-v] [-a [custom-alias-name]]" in out.getvalue()


# Generated at 2022-06-14 08:21:06.465880
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    import StringIO
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')
    saved_stderr = sys.stderr
    try:
        out = StringIO.StringIO()
        sys.stderr = out
        parser = Parser()
        parser.print_help()
        output = out.getvalue().strip()
        assert output == "usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-d] [--force-command FORCE_COMMAND] [-y] [-r] [command [command ...]]"
    finally:
        sys.stderr = saved_stderr

# Generated at 2022-06-14 08:21:10.740002
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    sys.argv = ['thefuck']
    parser = Parser()
    parser.print_usage()
    assert sys.stdout.getvalue().strip() == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l shell-logger] [--enable-experimental-instant-mode] [-y] [-r] [-d] [--force-command force-command] [command [command ...]] '


# Generated at 2022-06-14 08:21:13.653334
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    sys.argv = [
        'thefuck', 'git'
    ]
    from .main import create_parser
    parser = create_parser()
    parser.print_help()

# Generated at 2022-06-14 08:21:25.187372
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(['thefuck',
                         'gco',
                         ARGUMENT_PLACEHOLDER,
                         'lol',
                         '--',
                         '--test'])
    assert args.command == ['gco', '--test']
    assert args.shell_logger is None
    assert args.repeat is False
    assert args.enable_experimental_instant_mode is False
    assert args.yes is False
    assert args.debug is False
    assert args.help is False

    args = parser.parse(['thefuck',
                         'git',
                         'push',
                         ARGUMENT_PLACEHOLDER])
    assert args.command == ['git', 'push']
    assert args.shell_logger is None
    assert args.repeat is False
    assert args

# Generated at 2022-06-14 08:21:37.322708
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()

    arguments = parser.parse(['script_name', 'git', 'push'])
    assert arguments.command == ['git', 'push']

    arguments = parser.parse(['script_name', '-l', 'logfile.log', 'git', 'push'])
    assert arguments.shell_logger == 'logfile.log'
    assert arguments.command == ['git', 'push']

    arguments = parser.parse(['script_name', '-y', 'git', 'push'])
    assert arguments.command == ['git', 'push']
    assert arguments.yes

    arguments = parser.parse(['script_name', '-r', 'git', 'push'])
    assert arguments.command == ['git', 'push']
    assert arguments.repeat


# Generated at 2022-06-14 08:21:49.357976
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from .parser import Parser
    from .utils import get_alias

    parser = Parser()

    from io import StringIO
    import sys

    old_stderr = sys.stderr
    redirected = StringIO()
    sys.stderr = redirected
    parser.print_help()
    sys.stderr = old_stderr

    assert 'option' in redirected.getvalue().split()
    assert '-a [custom-alias-name]' in redirected.getvalue().split()
    assert '-v' in redirected.getvalue().split()
    assert '-h' in redirected.getvalue().split()
    assert get_alias() in redirected.getvalue().split()

# Generated at 2022-06-14 08:21:53.293597
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    stderr = sys.stderr
    try:
        from StringIO import StringIO
        sys.stderr = StringIO()
        parser = Parser()
        parser.print_usage()
        assert sys.stderr.getvalue() == 'Usage: thefuck [OPTIONS] [COMMAND [ARG]...]\n'
    finally:
        sys.stderr = stderr

# Generated at 2022-06-14 08:21:55.625374
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    Parser().print_help()
    # We just want to check that it doesn't raise any exceptions.


# Generated at 2022-06-14 08:22:11.628426
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(["/usr/bin/env", "python"])
    assert args.command == ["python"]
    args = parser.parse(["/usr/bin/env", "python", "-y"])
    assert args.command == ["python"]
    assert args.yes
    args = parser.parse(["/usr/bin/env", "python", "-y", "-r"])
    assert args.command == ["python"]
    assert args.yes
    args = parser.parse(["/usr/bin/env", "python", "-r"])
    assert args.command == ["python"]
    assert args.repeat

# Unit Test for method parse of class Parser when there is a placeholder

# Generated at 2022-06-14 08:22:13.419904
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser.parse([""])



# Generated at 2022-06-14 08:22:20.027214
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from .utils import tmp_file
    from .const import PROJECT_NAME
    parser = Parser()
    with tmp_file('w') as fh:
        sys.stderr = fh
        parser.print_help()
        fh.flush()
        help_text = fh.read()
    assert PROJECT_NAME in help_text
    assert 'show this help message and exit' in help_text

# Generated at 2022-06-14 08:22:31.491014
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(['thefuck', 'ssh', '-t', 'x'])
    assert args.command == ['ssh', '-t', 'x']
    args = parser.parse(['thefuck', 'ssh', '-t', 'x', 're', 'execute'])
    assert args.command == ['ssh', '-t', 'x']
    assert args.repeat == True
    args = parser.parse(['thefuck', 'ssh', '-t', 'x', ARGUMENT_PLACEHOLDER, 're', 'execute'])
    assert args.command == ['re', 'execute']
    args = parser.parse(['thefuck', 're', 'execute'])
    assert args.command == ['re', 'execute']

# Generated at 2022-06-14 08:22:35.245958
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    expected = ['--force-command', 'git', 'push', 'origin', 'master']
    assert parser.parse(['thefuck', 'git', 'pu', '--force-command', 'git', 'push', 'origin', 'master']) == expected


# Generated at 2022-06-14 08:22:36.701659
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser is not None



# Generated at 2022-06-14 08:22:46.379137
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    import sys
    parser.print_usage()
    parser.print_help()
    parser.parse(['thefuck', '-v'])
    parser.parse(['thefuck', '-a'])
    parser.parse(['thefuck', '-l'])
    parser.parse(['thefuck', '--enable-experimental-instant-mode'])
    parser.parse(['thefuck', '-h'])
    parser.parse(['thefuck', '-d'])
    parser.parse(['thefuck', '--force-command'])
    parser.parse(['thefuck', '-y'])
    parser.parse(['thefuck', '-r'])

# Generated at 2022-06-14 08:22:48.231054
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:22:51.606925
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    status, output = getstatusoutput("python2 -m thefuck")
    assert parser.print_usage() == output

test_Parser_print_usage()


# Generated at 2022-06-14 08:22:52.909757
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser() is not None


# Generated at 2022-06-14 08:22:58.220588
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()



# Generated at 2022-06-14 08:23:03.175688
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    assert p._parser.prog == 'thefuck'
    assert p._parser.add_help == False
    assert p._parser._optionals
    assert p._parser._positionals
    assert p._parser._actions
    assert p._parser.formatter
    assert p._parser.usage

# Generated at 2022-06-14 08:23:08.736207
# Unit test for method parse of class Parser
def test_Parser_parse():
    # no exception for a good set of arguments
    Parser().parse(['echo', 'fuck'])
    try:
        Parser().parse(['-l'])
        assert False
    except SystemExit:
        pass
    try:
        Parser().parse(['--shell-logger'])
        assert False
    except SystemExit:
        pass
    try:
        Parser().parse(['-h'])
        assert False
    except SystemExit:
        pass
    try:
        Parser().parse(['--help'])
        assert False
    except SystemExit:
        pass

# Generated at 2022-06-14 08:23:10.083345
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser()


# Generated at 2022-06-14 08:23:11.120912
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:23:20.472432
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    class File(object):
        def __init__(self):
            self.output = []

        def write(self, chunk):
            self.output.append(chunk)

    file = File()
    parser = Parser()
    parser.print_usage(file)
    assert file.output[0].startswith(
        'usage: thefuck [-h] [-v] [-a [custom-alias-name]]\n'
        '               [-l SHELL_LOGGER] [--enable-experimental-instant-mode]\n'
        '               [-d] [--force-command FORCE_COMMAND]\n'
        '               [--] [command [command ...]]')


# Generated at 2022-06-14 08:23:30.424886
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    # Make sure that `usage` is printed when no arguments are provided.
    with patch.object(sys.stderr, 'write') as write_mock:
        parser = Parser()
        parser.print_usage()
        assert write_mock.call_args[0][0].startswith('usage')

    # Make sure that `usage` is not printed when arguments are provided.
    with patch.object(sys.stderr, 'write') as write_mock:
        parser = Parser()
        parser.parse(['thefuck', 'ls', '-la'])
        assert write_mock.call_args is None


# Generated at 2022-06-14 08:23:31.599341
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    assert p._parser

# Generated at 2022-06-14 08:23:38.490099
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    """Unit test for method print_usage of class Parser"""
    class Stderr:
        """Dummy class"""
        def __init__(self, test_case):
            self.test_case = test_case

        def write(self, message):
            self.test_case.assertEqual(message, 'usage: thefuck [-h] [-v] [-a [custom-alias-name]]')

    import unittest
    class TestParser(unittest.TestCase):
        """Test class for method print_usage of class Parser"""
        def test(self):
            parser = Parser()
            parser.print_usage()
            self.assertEqual(parser.print_usage(), None)
    class StderrTestCase(unittest.TestCase):
        @staticmethod
        def setUpClass():
            sys

# Generated at 2022-06-14 08:23:41.373424
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert hasattr(parser, '_parser')
    assert isinstance(parser, Parser)



# Generated at 2022-06-14 08:23:50.971744
# Unit test for constructor of class Parser
def test_Parser():
    main = Parser()
    assert main

# Generated at 2022-06-14 08:24:02.980741
# Unit test for method parse of class Parser
def test_Parser_parse():
    import unittest

    parser = Parser()
    args = parser.parse(['thefuck', '--yes', 'ls'])
    assert args.yes == True
    assert args.command == ['ls']

    args = parser.parse(['thefuck', '--repeat', 'ls'])
    assert args.repeat == True
    assert args.command == ['ls']

    args = parser.parse(['thefuck', 'ls'])
    assert args.repeat == False
    assert args.yes == False
    assert args.command == ['ls']

    args = parser.parse(['thefuck', '--yes', 'ls', ARGUMENT_PLACEHOLDER, '--force-command', 'cd', '~'])
    assert args.command == ['--force-command', 'cd', '~']

# Generated at 2022-06-14 08:24:11.379307
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    class Args:
        def __init__(self, aliases, command, debug, force_command,
                     shell_logger, yes, repeat):
            self.alias = aliases
            self.command = command
            self.debug = debug
            self.force_command = force_command
            self.shell_logger = shell_logger
            self.yes = yes
            self.repeat = repeat

# Generated at 2022-06-14 08:24:15.250030
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from StringIO import StringIO
    out = StringIO()
    Parser().print_usage(file=out)
    assert 'usage: thefuck' in out.getvalue()


# Generated at 2022-06-14 08:24:17.838657
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser.prog == 'thefuck'


# Generated at 2022-06-14 08:24:22.223959
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    parsed = parser.parse(['thefuck', 'git', 'status', '-a'])
    assert parsed.alias is None
    assert parsed.shell_logger is None
    assert parsed.enable_experimental_instant_mode is False
    assert parsed.help is False
    assert parsed.debug is False
    assert parsed.force_command is None
    assert parsed.command == ['git', 'status', '-a']


# Generated at 2022-06-14 08:24:34.993205
# Unit test for method parse of class Parser
def test_Parser_parse():
    # This test uses method parse of class Parser
    # First we need to create a Parser object
    parser = Parser()
    # This is the first argument test
    # Argument: thefuck --version
    args = parser.parse(['thefuck', '--version'])
    assert args.version == True
    assert args.alias == None
    assert args.debug == False
    assert args.force_command == None
    assert args.yes == False
    assert args.repeat == False
    assert args.help == False
    assert args.enable_experimental_instant_mode == False
    assert args.shell_logger == None
    assert args.command == []
    # This is the second argument test
    # Argument: thefuck --debug
    args = parser.parse(['thefuck', '--debug'])
    assert args.version

# Generated at 2022-06-14 08:24:41.587191
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    parser.parse(["a"])
    parser.parse(["a", "b"])
    parser.parse(["a", "b", "c"])
    parser.parse(["a", "b", "c", ARGUMENT_PLACEHOLDER, "d"])
    parser.parse(["a", "b", ARGUMENT_PLACEHOLDER, "d"])
    parser.parse(["a", "b", ARGUMENT_PLACEHOLDER, "d"])
    parser.parse(["a", "b", "c", ARGUMENT_PLACEHOLDER, "d", "e"])
    parser.parse(["a", "b", "c", ARGUMENT_PLACEHOLDER, "d", "e", "f"])


# Generated at 2022-06-14 08:24:52.891204
# Unit test for method parse of class Parser
def test_Parser_parse():
    args = Parser().parse(['fuck', 'x'])
    assert args.command == ['x']

    args = Parser().parse(['fuck', '--force-command', 'x'])
    assert args.command == []
    assert args.force_command == 'x'

    args = Parser().parse(['fuck', '--', 'x'])
    assert args.command == ['--', 'x']

    args = Parser().parse(['fuck', '-a', 'x'])
    assert args.alias == 'x'

    args = Parser().parse(['fuck', '--alias'])
    assert args.alias == get_alias


# Generated at 2022-06-14 08:24:55.446825
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    try:
        parser = Parser()
        parser.print_help()
    except SystemExit:
        assert True
    else:
        assert False

# Generated at 2022-06-14 08:25:09.560384
# Unit test for method print_help of class Parser
def test_Parser_print_help():
  parser = Parser()
  parser.print_help()

# Generated at 2022-06-14 08:25:11.000425
# Unit test for constructor of class Parser
def test_Parser():
    Parser()


# Generated at 2022-06-14 08:25:17.872227
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()

    argv = ['thefuck', ARGUMENT_PLACEHOLDER, '--ls']
    assert parser.parse(argv) == parser._parser.parse_args(['--ls'])

    argv = ['thefuck', '-h']
    assert parser.parse(argv) == parser._parser.parse_args(['-h'])

# Generated at 2022-06-14 08:25:28.160272
# Unit test for method parse of class Parser
def test_Parser_parse():
    import sys
    Parser = __import__('thefuck.shells', fromlist=['Parser']).Parser
    parser = Parser()
    argv = sys.argv
    sys.argv = ['thefuck', 'cd', '~/lll/ttt', ARGUMENT_PLACEHOLDER, '-l']
    assert parser.parse(sys.argv).command == ['cd', '~/lll/ttt']
    assert parser.parse(sys.argv).shell_logger == 'ttt'
    sys.argv = argv

# Generated at 2022-06-14 08:25:30.017856
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser


# Generated at 2022-06-14 08:25:39.677948
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    # make a parser object
    parser_obj = Parser()
    
    #make some arguments
    args = ['','-1','-2']
    
    #create a mock stderr
    stderr = io.StringIO()
    sys.stderr = stderr
    
    #run the method
    parser_obj.print_usage()
    
    #assertions
    assert len(stderr.getvalue().split('\n')) > 2
    

# Generated at 2022-06-14 08:25:42.648650
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    argv = ['thefuck', '--']
    parser.parse(argv)
    parser.print_usage()

# Generated at 2022-06-14 08:25:48.809297
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    old_stdout = sys.stdout
    sys.stdout = open('/tmp/t_out', 'w')
    parser.print_help()
    sys.stdout.close()
    sys.stdout = old_stdout

    with open('/tmp/t_out', 'r') as f:
        output = f.read()

    assert(len(output.split('usage: ')) == 2)
    assert(len(output.split('optional arguments:')) == 2)
    assert(len(output.split('positional arguments:')) == 2)

# Generated at 2022-06-14 08:25:50.265683
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:25:52.499823
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    return parser.print_help()


# Generated at 2022-06-14 08:26:09.871615
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()
    assert True

# Generated at 2022-06-14 08:26:19.200416
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    parsed_args = parser.parse(
        ['-v', '--alias', 'fuck', '--alias', 'fuck'])
    assert parsed_args.version
    assert parsed_args.alias == 'fuck'
    assert parsed_args.enable_experimental_instant_mode is False
    assert parsed_args.command == []

    parsed_args = parser.parse(
        ['--yes', '-d', 'ls', '-a'])
    assert parsed_args.debug
    assert parsed_args.command == ['-a']
    assert parsed_args.yes

    parsed_args = parser.parse(
        ['ls', '-l', ARGUMENT_PLACEHOLDER, '--color=auto'])
    assert parsed_args.command == ['--color=auto']



# Generated at 2022-06-14 08:26:27.403340
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    # match output of parse_args of argparse
    assert parser.parse([
        './bin/thefuck',
        '--debug',
        '--shell-logger',
        'shelllog.txt',
        'touch']) == parser._parser.parse_args([
            '--debug',
            '--shell-logger',
            'shelllog.txt',
            '--',
            'touch'])


# Generated at 2022-06-14 08:26:28.783420
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:26:35.604042
# Unit test for method print_help of class Parser
def test_Parser_print_help():
        # output = StringIO.StringIO()
        # sys.stdout = output
        parser = Parser()
        parser.print_help()

# Generated at 2022-06-14 08:26:44.040737
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    # Generate a fake file to store the stdout from print_help
    outfile = open('./testfile_print_help.txt', 'w')
    sys.stdout = outfile
    parser.print_help()
    outfile.close()
    infile = open('./testfile_print_help.txt')
    input_file = infile.read()
    print(input_file)
    assert input_file != ''
    infile.close()

# Generated at 2022-06-14 08:26:50.675241
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    p = Parser()
    s = StringIO()

    p.print_usage()
    # Call method print_usage
    sys.stderr.seek(0)
    r = sys.stderr.read()
    # Save the output to string
    sys.stderr = s
    # Restore stderr
    assert r.startswith('usage:')
    assert r.endswith('\n')


# Generated at 2022-06-14 08:26:53.458736
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()

test_Parser_print_usage()

# Generated at 2022-06-14 08:26:55.276336
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    p = Parser()
    p.print_usage()

# Generated at 2022-06-14 08:27:03.391719
# Unit test for method parse of class Parser
def test_Parser_parse():
    argv = ['/path/to/bin/thefuck', 'ls', '-l', ARGUMENT_PLACEHOLDER, '-y', '-d', '--debug']
    expected_args = ['-y', '-d', '--debug', '--', 'ls', '-l']
    args = Parser().parse(argv)
    assert vars(args) == vars(Parser().parse(expected_args))


# Generated at 2022-06-14 08:27:51.292403
# Unit test for method parse of class Parser
def test_Parser_parse():
    p = Parser()
    result = p.parse(['thefuck', '-y', 'ls', '-l', '-la'])
    assert result.yes == True
    assert result.command == ['ls', '-l', '-la']
    assert result.debug == False
    assert result.force_command == None
    assert result.help == False
    result = p.parse(['thefuck', '-y'])
    assert result.yes == True
    assert result.command == []
    result = p.parse(['thefuck', '-y', 'fuck'])
    assert result.yes == True
    assert result.command == []
    result = p.parse(['thefuck', 'fuck'])
    assert result.yes == False
    assert result.command == ['fuck']


# Generated at 2022-06-14 08:27:52.963855
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:27:54.187291
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:27:55.985490
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()

# Generated at 2022-06-14 08:28:03.204307
# Unit test for method parse of class Parser
def test_Parser_parse():
    import sys
    command = "get_my_error"
    expected = "get_my_error"

    # Prepare
    parser = Parser()
    sys.argv = ["thefuck", command]

    # Test
    arguments = parser.parse(sys.argv)
    command = arguments.command
    result = command[0]

    # Assert
    assert result == expected


# Generated at 2022-06-14 08:28:06.183956
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    try:
        parser.print_usage()
    except (TypeError, IOError):
        pass

# Generated at 2022-06-14 08:28:13.363166
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    usage = 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER]\n'
    usage += '               [--enable-experimental-instant-mode] [-y] [-r]\n'
    usage += '               [-d] [--force-command FORCE_COMMAND] [command [command ...]]\n'
    with patch('sys.stderr') as stderr:
        Parser().print_usage()
        stderr.write.assert_called_once_with(usage)



# Generated at 2022-06-14 08:28:15.134729
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser is not None


# Generated at 2022-06-14 08:28:23.291031
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    out = StringIO()
    sys.stderr = out
    parser.print_usage()
    output = out.getvalue().strip()
    assert output == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] '\
            '[-l SHELL_LOGGER] [--enable-experimental-instant-mode] '\
            '[-d] [-y | -r] [--force-command FORCE_COMMAND] '\
            '[command [command ...]]'



# Generated at 2022-06-14 08:28:33.653633
# Unit test for method print_help of class Parser

# Generated at 2022-06-14 08:30:17.104988
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:30:26.900158
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    old_stderr = sys.stderr

    class PseudoFile(object):

        def __init__(self, lines=[]):
            self.lines = lines

        def write(self, line):
            self.lines.append(line)

    output = PseudoFile()
    sys.stderr = output
    parser.print_usage()
    assert output.lines[0] == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]]\n'
    sys.stderr = old_stderr


# Generated at 2022-06-14 08:30:37.859029
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    # Arrange
    from StringIO import StringIO
    from mock import patch
    from .utils import import_by_path, which

    # Act
    parser = Parser()
    with patch('sys.stderr', new=StringIO()) as mock_stderr:
        parser.print_help()

    # Assert
    mock_stderr.seek(0)
    assert 'usage: thefuck' in mock_stderr.read()
    assert 'alias [custom-alias-name]' in mock_stderr.read()
    assert 'shell-logger log shell output to the file' in mock_stderr.read()
    assert '--help show this help message and exit' in mock_stderr.read()
    assert '--debug enable debug output' in mock_stderr.read()

# Unit test

# Generated at 2022-06-14 08:30:40.438758
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    print('Parser help:')
    parser.print_help()



# Generated at 2022-06-14 08:30:46.032373
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    class FakeFile(object):
        def write(self, _): pass
        def writelines(self, _): pass

    FakeSysStderr = FakeFile()
    with mock.patch('sys.stderr', FakeSysStderr):
        Parser().print_usage()
