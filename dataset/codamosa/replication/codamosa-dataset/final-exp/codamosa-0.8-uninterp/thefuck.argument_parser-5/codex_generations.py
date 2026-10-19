

# Generated at 2022-06-14 08:21:00.570202
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()

    # with ARGUMENT_PLACEHOLDER
    args = parser.parse(['fuck'])
    assert args.enable_experimental_instant_mode == False

    args = parser.parse(['fuck', '-v'])
    assert args.enable_experimental_instant_mode == False
    assert args.version == True

    args = parser.parse(['fuck', '-a'])
    assert args.enable_experimental_instant_mode == False
    assert args.alias == get_alias()

    args = parser.parse(['fuck', '-h'])
    assert args.enable_experimental_instant_mode == False
    assert args.help == True

    args = parser.parse(['fuck', '-y'])
    assert args.enable_experimental_instant

# Generated at 2022-06-14 08:21:12.472552
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    """Test that method print_usage prints usage of parser."""
    parser = Parser()
    with patch('sys.stderr', StringIO()) as stderr:
        parser.print_usage()
    stderr.seek(0)
    assert stderr.readlines() == [
        'usage: thefuck [-h] [-v] [-a [custom-alias-name]]\n',
        '               [-l SHELL_LOGGER] [--enable-experimental-instant-mode]\n',
        '               [-y | -r] [-d] [--force-command FORCE_COMMAND]\n',
        '               command [command ...]\n',
        '\n']

# Generated at 2022-06-14 08:21:16.004228
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    args = parser.parse(['some-command', ARGUMENT_PLACEHOLDER, 'some-arg'])
    assert args.command == ['some-command', 'some-arg']

# Generated at 2022-06-14 08:21:23.749434
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    # Arrange.
    from io import StringIO
    from .utils import capture_output

    # Act.
    with capture_output() as (out, err):
        Parser().print_help()

    # Assert.
    actual = StringIO(err.getvalue())

# Generated at 2022-06-14 08:21:33.200516
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from io import StringIO
    from .utils import captured_stderr

    parser = Parser()
    with captured_stderr() as stderr:
        parser.print_usage()
    output = stderr.getvalue().strip()
    assert output == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l shell_logger] [--enable-experimental-instant-mode] [-y | -r] [-d] [--force-command force_command] [command [command ...]]'

#Unit test for method parse of class Parser

# Generated at 2022-06-14 08:21:38.067740
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    output = StdOutStub()
    parser.print_usage()
    assert output == "usage: thefuck [-h] [-v] [-a [CUSTOM-ALIAS-NAME]] [-l SHELL-LOGGER] [--enable-experimental-instant-mode] [-y] [-r] [-d] [--force-command FORCE-COMMAND] [command [command ...]]\n"



# Generated at 2022-06-14 08:21:39.915808
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    return parser


# Generated at 2022-06-14 08:21:41.344990
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser().__class__.__name__ == "Parser"


# Generated at 2022-06-14 08:21:52.417822
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    import StringIO
    saved_stderr = sys.stderr
    try:
        out = StringIO.StringIO()
        sys.stderr = out
        Parser().print_usage()
        output = out.getvalue().strip()
    finally:
        sys.stderr = saved_stderr

    assert output == '''usage: thefuck [-h] [-v] [-a custom-alias-name]
                 [-l shell-logger] [--enable-experimental-instant-mode]
                 [-y | -r] [-d] [--force-command]
                 [--] [command [command ...]]'''


# Generated at 2022-06-14 08:21:54.852607
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    command, *argv = ['--help']
    assert Parser().parse(argv) == True


# Generated at 2022-06-14 08:22:00.032327
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    assert parser.print_usage() is None


# Generated at 2022-06-14 08:22:04.811766
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['thefuck', 'ls', '../']) == argparse.Namespace(alias=None,
                                                                        command=['ls', '../'],
                                                                        debug=False,
                                                                        enable_experimental_instant_mode=False,
                                                                        force_command=None,
                                                                        help=False,
                                                                        repeat=False,
                                                                        shell_logger=None,
                                                                        version=False,
                                                                        yeah=False)


# Generated at 2022-06-14 08:22:06.485749
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser

# Generated at 2022-06-14 08:22:09.750453
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    dummyArgv = ['foo.py', '--help']
    dummy = Parser()
    dummy.parse(dummyArgv)
    assert True

# Generated at 2022-06-14 08:22:12.597812
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser_output = parser.print_usage()



# Generated at 2022-06-14 08:22:14.375317
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser


# Generated at 2022-06-14 08:22:15.653252
# Unit test for constructor of class Parser
def test_Parser():
    Parser()

# Generated at 2022-06-14 08:22:26.257738
# Unit test for method parse of class Parser
def test_Parser_parse():
    p = Parser()
    args = p.parse(['thefuck','some','command','some','more','args', '-y'])

    assert args.command[0] == 'some'
    assert args.command[1] == 'command'
    assert args.command[2] == 'some'
    assert args.command[3] == 'more'
    assert args.command[4] == 'args'
    assert args.yes is True
    assert args.repeat is None
    assert args.force_command is None
    assert args.debug is None
    assert args.shell_logger is None
    assert args.enable_experimental_instant_mode is None
    assert args.alias is None
    assert args.version is None
    assert args.help is None


# Generated at 2022-06-14 08:22:33.172363
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    import sys
    import io
    import unittest

    stderr = sys.stderr
    try:
        sys.stderr = io.StringIO()
        Parser().print_help()
        assert "show this help message and exit" in sys.stderr.getvalue()
    finally:
        sys.stderr = stderr

# Generated at 2022-06-14 08:22:35.116727
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:22:46.913860
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    class UnitTestParser(ArgumentParser):
        def __init__(self, *args, **kwargs):
            self.written = ''
            super(UnitTestParser, self).__init__(prog='', *args, **kwargs)

        def print_help(self, file=None):
            self.written = 'help'

    parser = Parser()
    parser._parser = UnitTestParser(add_help=False)

    parser.print_help()

    assert parser._parser.written == 'help'

# Generated at 2022-06-14 08:22:48.781235
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.parse(["--help"])

# Generated at 2022-06-14 08:22:50.120228
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()

    assert parser

# Generated at 2022-06-14 08:22:57.725339
# Unit test for constructor of class Parser
def test_Parser():
    """
    Unit test for constructor of class Parser
    """
    p = Parser()
    try:
        assert p != None
    except:
        print("test_Parser fails: Parser instance is null.")
        return False
    try:
        assert p._parser != None
    except:
        print("test_Parser fails: _parser instance is null.")
        return False

    print("test_Parser succeed.")
    return True


# Generated at 2022-06-14 08:22:59.687219
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    assert parser.print_usage() == None


# Generated at 2022-06-14 08:23:13.653771
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    # _prepare_arguments()
    assert parser.parse(['thefuck', 'vim', 'dir', 'dir']) == \
        parser._parser.parse_args(['vim', 'dir', 'dir'])
    assert parser.parse(['thefuck', 'vim', ARGUMENT_PLACEHOLDER, 'dir', 'dir']) == \
        parser._parser.parse_args(['dir', 'dir', '--', 'vim'])
    assert parser.parse(['thefuck', '--alias', 'vim', 'dir']) == \
        parser._parser.parse_args(['--alias', 'vim', 'dir'])
    assert parser.parse(['thefuck', 'vim', ARGUMENT_PLACEHOLDER, '--alias', 'dir']) == \
        parser

# Generated at 2022-06-14 08:23:15.702178
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    if (parser._parser.prog == "thefuck"):
        print("Unit test passed")
    else:
        print("Unit test failed")


# Generated at 2022-06-14 08:23:20.661344
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    args = parser.parse(['/path/to/python/bin/fuck', '-v', 'python'])
    assert args.version is True
    assert args.debug is False
    assert args.command == ['python']
    args = parser.parse(['/path/to/python/bin/fuck', '-a'])
    assert args.alias == get_alias()
    assert args.command == []



# Generated at 2022-06-14 08:23:26.748617
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    import argparse
    def mock_print_help(*args):
        assert args == (sys.stderr,)
    try:
        p = Parser()
        argparse.ArgumentParser.print_help = mock_print_help
        p.print_help()
    finally:
        argparse.ArgumentParser.print_help = argparse.ArgumentParser.print_help

# Generated at 2022-06-14 08:23:28.401262
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert isinstance(parser, Parser)

# Generated at 2022-06-14 08:23:51.974071
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()

# Generated at 2022-06-14 08:23:53.779962
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser is not None


# Generated at 2022-06-14 08:23:58.623180
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    argv = ['-d', 'command', ARGUMENT_PLACEHOLDER, '--', '-a', '-b']
    args = parser.parse(argv)
    assert args.debug == True
    assert args.command == ['command', '-a', '-b']

# Generated at 2022-06-14 08:24:06.483573
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()

    assert parser.parse(['thefuck']) == parser._parser.parse_args([])

    assert parser.parse(['thefuck', '--yes']) == parser._parser.parse_args(['--yes'])
    assert parser.parse(['thefuck', '--yes', '--debug']) == parser._parser.parse_args(['--yes', '--debug'])
    assert parser.parse(['thefuck', '--debug', '--yes']) == parser._parser.parse_args(['--debug', '--yes'])
    assert parser.parse(['thefuck', '--debug', '--force-command', '--yes']) == parser._parser.parse_args(['--debug', '--force-command', '--yes'])


# Generated at 2022-06-14 08:24:08.816663
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()
    # TODO assert text written to stdout

# Generated at 2022-06-14 08:24:11.403505
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:24:23.190853
# Unit test for method parse of class Parser
def test_Parser_parse():
    Parser().parse(['thefuck', 'git']) == Namespace(force_command=None, yes=False, repeat=False, debug=False, alias=get_alias(), command=[])
    Parser().parse(['thefuck', 'git', 'commit', '--amend', '-m', '"new commit"']) == Namespace(alias=get_alias(), force_command=None, yes=False, repeat=False, debug=False, command=['commit', '--amend', '-m', '"new commit"'])

# Generated at 2022-06-14 08:24:24.372327
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:24:33.733889
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    first_parse = parser.parse(['thefuck', 'foo', 'bar'])
    second_parse = parser.parse(['thefuck', '--', 'foo', 'bar'])
    third_parse = parser.parse(['thefuck', '--force-command', 'foobar', 'foo', 'bar'])
    assert first_parse.command == ['foo', 'bar']
    assert second_parse.command == ['foo', 'bar']
    assert third_parse.command == []
    assert third_parse.force_command == 'foobar'

# Generated at 2022-06-14 08:24:38.152948
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    parser.parse(["-a"])
    parser.parse(["-v"])
    parser.parse(["-l", "test"])
    parser.parse(["-h"])
    parser.parse(["-y"])
    parser.parse(["-r"])
    parser.parse(["--debug"])
    parser.parse(["--force-command", "test"])
    parser.parse(["test"])
    parser.parse(["--help"])
    parser.parse(["--enable-experimental-instant-mode"])
    parser.parse(["-p", "test"])



# Generated at 2022-06-14 08:25:13.160602
# Unit test for method parse of class Parser
def test_Parser_parse():
    import StringIO
    out = StringIO.StringIO()
    sys.stderr = out
    cmd = u'thefuck --force-command \'echo fuck\' --debug'
    p = Parser()
    args = p.parse(cmd.split())
    assert args.shell_logger is None
    assert args.enable_experimental_instant_mode is False
    assert args.force_command == u'echo fuck'
    assert args.help is False
    assert args.debug is True
    assert args.command == []

    cmd = u'thefuck --shell-logger /tmp/fuck.log --debug --'
    sys.stderr = out
    p = Parser()
    args = p.parse(cmd.split())
    assert args.force_command is None

# Generated at 2022-06-14 08:25:15.638127
# Unit test for method parse of class Parser
def test_Parser_parse():
    args = Parser().parse(['--force-command', 'echo'])
    assert args.force_command == 'echo'

if __name__ == '__main__':
    test_Parser_parse()

# Generated at 2022-06-14 08:25:26.408818
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(['fuck', 'push', 'origin', 'master', ARGUMENT_PLACEHOLDER, '-c', 'core.askpass=true'])
    assert args.command == ['push', 'origin', 'master']
    assert args.core_askpass == 'true'

    args = parser.parse(['fuck', 'push', 'origin', 'master', '-c', 'core.askpass=true'])
    assert args.command == ['push', 'origin', 'master']
    assert args.core_askpass == 'true'


# Generated at 2022-06-14 08:25:37.462812
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    """Parser.print_usage() prints usage of thefuck in case of empty arguments"""
    parser = Parser()
    captor = StringIO()
    sys.stderr = captor
    parser.print_usage()
    sys.stderr = sys.__stderr__
    assert captor.getvalue() == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]]\n            [-l SHELL_LOGGER]\n            [--enable-experimental-instant-mode]\n            [-y | -r] [-d] [--force-command COMMAND]\n            [command [command ...]]\n\n'


# Generated at 2022-06-14 08:25:39.187993
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    return parser.print_help()


# Generated at 2022-06-14 08:25:41.188102
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    assert Parser().print_usage() is None  # This purpose of the test is just to run print usage


# Generated at 2022-06-14 08:25:43.465317
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    assert parser.print_usage() == parser._parser.print_usage(sys.stderr)


# Generated at 2022-06-14 08:25:50.262644
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse([
        'thefuck', '--alias', 'fuck', 'echo', '-n', 'foo']) == \
        parser.parse(['thefuck', '--alias', 'fuck', 'echo', '-n', 'foo'])
    assert parser.parse([
        'thefuck', 'ls', '-lh', '/usr/bin', ARGUMENT_PLACEHOLDER,
        '-y', '-r']) == \
        parser.parse([
            'thefuck', '-y', '-r', 'ls', '-lh', '/usr/bin'])

# Generated at 2022-06-14 08:26:01.251977
# Unit test for constructor of class Parser
def test_Parser():
    from .const import ARGUMENT_PLACEHOLDER, DEFAULT_ALIAS
    from .utils import get_alias
    
    # test for command
    test_argv = ['fuck', '-v', '-a', 'chuck', '-l', 'foo.log', 
                 '--enable-experimental-instant-mode', '-h', '-d', '-y']
    assert Parser()._prepare_arguments(test_argv) == \
        ['-v', '-a', 'chuck', '-l', 'foo.log', '--enable-experimental-instant-mode', 
         '-h', '-d', '-y']

    # test for command with ARGUMENT_PLACEHOLDER

# Generated at 2022-06-14 08:26:02.459878
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    p = Parser()
    p.print_usage()

# Generated at 2022-06-14 08:26:54.262082
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    parser.parse()
    parser.print_usage()
    parser.print_help()
    parser._add_arguments()
    parser._add_conflicting_arguments()
    parser._prepare_arguments()

# Generated at 2022-06-14 08:26:56.696398
# Unit test for constructor of class Parser
def test_Parser():
    testParser = Parser()
    assert(type(testParser) == Parser)


# Generated at 2022-06-14 08:26:59.786988
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()

    options = ['thefuck', 'fuck', '-h']
    assert parser.parse(options).help is True

# Generated at 2022-06-14 08:27:09.186104
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['', '--enable-experimental-instant-mode'])
    assert parser.parse(['', '-a'])
    assert parser.parse(['', '-a', 'fuck'])
    assert parser.parse(['', '-l', 'fuck_logger'])
    assert parser.parse(['', '-h'])
    assert parser.parse(['', '--help'])
    assert parser.parse(['', '-v'])
    assert parser.parse(['', '--version'])
    assert parser.parse(['', '-y'])
    assert parser.parse(['', '-r'])
    assert parser.parse(['', '-d'])
    assert parser.parse(['', '--', 'ls', '-la'])
   

# Generated at 2022-06-14 08:27:12.280328
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.parse(['./bin/fuck', '--enable-experimental-instant-mode', '--shell-logger', 'log'])


# Generated at 2022-06-14 08:27:14.845365
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    # creating instance of class Parser
    parser = Parser()
    # calling method print_usage
    parser.print_usage()

# Generated at 2022-06-14 08:27:26.189049
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    # import sys
    # sys.stderr = open("test_unit_test.txt", "w")
    # parser.print_usage()
    # sys.stderr = open("test_parser_python_2.txt", "w")
    # parser.print_usage()
    # sys.stderr = open("test_parser_python_3.txt", "w")
    # parser.print_usage()
    # sys.stderr = open("test_parser_from_pytest_test_command.txt", "w")
    # parser.print_usage()
    # sys.stderr = open("test_parser_from_pytest_test_command_2.txt", "w")
    # parser.print_usage()
    # sys.stderr = open("test_

# Generated at 2022-06-14 08:27:32.541148
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    # The command
    assert parser.parse(['fuck']) == parser.parse(['fuck'])

    # The alias
    assert parser.parse(['fuck', '-a']) == parser.parse(['fuck', '-a'])

    # The alias and the command
    assert parser.parse(['fuck', '-a', 'ls']) == parser.parse(['fuck', '-a', 'ls'])

# Generated at 2022-06-14 08:27:40.958757
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    #Given
    parser = Parser()
    #When
    parser.print_help()
    #Then
    _contains_version_help = 'show program\'s version number and exit'
    _contains_alias_help = 'prints alias for current shell'
    _contains_logger_help = 'log shell output to the file'
    _contains_enable_instant_mode = 'enable experimental instant mode'
    _contains_help_help = 'show this help message and exit'
    _contains_yes_help = 'execute fixed command without confirmation'
    _contains_repeat_help = 'repeat on failure'
    _contains_debug_help = 'enable debug output'
    _contains_command_help = 'command that should be fixed'


# Generated at 2022-06-14 08:27:43.596619
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.parse(['--force-command', 'ls', '.'])
    assert parser.print_usage() != None

# Generated at 2022-06-14 08:30:06.780740
# Unit test for method parse of class Parser
def test_Parser_parse():
    """Unit test for method parse for class Parser"""
    instances = [
        # list of arguments,
        # expected list of arguments after running _prepare_arguments
        (['-h'], ['-h']),
        (['-y', 'cd', '--', '-l'], ['-l', '--', '-y', 'cd']),
        (['-r', 'cd', '--', '-l'], ['-l', '--', '-r', 'cd']),
        (['cd', '--', '-l'], ['-l', '--', 'cd']),
        (['cd', 'some', '--', '-l'], ['-l', '--', 'cd', 'some'])
    ]
    for arguments, expected_arguments in instances:
        parser = Parser()
        result

# Generated at 2022-06-14 08:30:09.647758
# Unit test for constructor of class Parser
def test_Parser():
	p = Parser()
	assert p._parser.prog == 'thefuck' and p._parser.add_help == False
	

# Generated at 2022-06-14 08:30:20.394053
# Unit test for method parse of class Parser
def test_Parser_parse():
    from .utils import get_shell
    from .const import ALIAS
    parser = Parser()

# Generated at 2022-06-14 08:30:23.486775
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    """Test for method print_help of class Parser"""
    parser = Parser()
    parser.print_help()
    assert parser.print_help()



# Generated at 2022-06-14 08:30:25.939680
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:30:37.309933
# Unit test for method parse of class Parser
def test_Parser_parse():
    # Scenario 1: the placeholder is in the command, the arguments are in the
    #             command
    parser1 = Parser()
    # the following command has the placeholder and the arguments
    command1 = ['thefuck', ARGUMENT_PLACEHOLDER, '-d', '-v', 'ls']
    parser1.parse(command1)
    # this command is the same as the above one in the --command
    command2 = ['thefuck', '-d', '-v', 'ls']
    with pytest.raises(SystemExit):
        parser1.parse(command2)
    # the following command has the known arguments
    command3 = ['thefuck', '-d', '-v']
    with pytest.raises(SystemExit):
        parser1.parse(command3)
    # the following command has the

# Generated at 2022-06-14 08:30:39.021611
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():

    parser = Parser()
    assert (parser.print_usage() == None)

# Generated at 2022-06-14 08:30:50.562870
# Unit test for method print_help of class Parser
def test_Parser_print_help():

    # First, create an instance of class Parser
    parser = Parser()

    # We need to store in a temporary file the output of method print_help
    # (we use a context manager to close the opened file)
    with open('test_Parser_print_help', 'w') as f:
        sys.stderr = f

        # Launch the method to be tested
        parser.print_help()

    # We reopen the file
    with open('test_Parser_print_help', 'r') as f:
        # Read its content
        content = f.read()
        # Check that the expected string is in the content
        assert('optional arguments' in content)
        assert('usage: thefuck' in content)
        assert('positional arguments' in content)
        assert('-v, --version' in content)