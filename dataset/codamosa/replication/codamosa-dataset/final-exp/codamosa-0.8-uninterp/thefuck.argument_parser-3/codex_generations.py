

# Generated at 2022-06-14 08:20:55.666874
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    sys.stderr = open('tests/unittest_parse_usage.txt', 'w')
    parser.print_usage()
    sys.stderr.close()
    sys.stderr = sys.__stderr__
    assert open('tests/unittest_parse_usage.txt','r').read() == open('tests/unittest/unittest_parse_usage.txt','r').read()


# Generated at 2022-06-14 08:21:02.818995
# Unit test for constructor of class Parser
def test_Parser():
    parser_ = Parser()
    #  assert parser_._parser._prog == 'thefuck'
    #  assert parser_._parser._optionals._group_actions[0].dest == 'version'
    #  assert parser_._parser._optionals._group_actions[0].const == True
    #  assert parser_._parser._optionals._group_actions[0].default == False
    #  assert parser_._parser._optionals._group_actions[1].dest == 'alias'
    #  assert parser_._parser._optionals._group_actions[1].nargs == '?'
    #  assert parser_._parser._optionals._group_actions[1].const == get_alias()
    #  assert parser_._parser._optionals._group_actions[1].default == None
    #  assert parser_._parser._optionals

# Generated at 2022-06-14 08:21:11.356900
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    assert(p._parser.add_help is False)
    assert(p._parser._actions[0].option_strings == ['-v', '--version'])
    assert(p._parser._actions[0].help == "show program's version number and exit")
    assert(p._parser._actions[1].option_strings == ['-a', '--alias'])
    assert(p._parser._actions[1].help == '[custom-alias-name] prints alias for current shell')
    assert(p._parser._actions[2].option_strings == ['-l', '--shell-logger'])
    assert(p._parser._actions[2].help == 'log shell output to the file')
    assert(p._parser._actions[3].option_strings == ['--enable-experimental-instant-mode'])

# Generated at 2022-06-14 08:21:21.447910
# Unit test for method parse of class Parser
def test_Parser_parse():
    """
    Test for test_Parser_parse method of class Parser
    """
    def test_Parser_parse_case0():
        """
        Case 0 : parse("a","b",c")
        """
        argv = ['fuck', 'a', 'b', 'c']
        parser = Parser()
        assert parser.parse(argv) == parser._parser.parse_args(['--', 'a', 'b', 'c'])

    def test_Parser_parse_case1():
        """
        Case 1 : parse("a","b","P")
        """
        argv = ['fuck', 'a', 'b', ARGUMENT_PLACEHOLDER]
        parser = Parser()
        assert parser.parse(argv) == parser._parser.parse_args(['--', 'a', 'b'])



# Generated at 2022-06-14 08:21:22.218625
# Unit test for constructor of class Parser
def test_Parser():
    Parser()

# Generated at 2022-06-14 08:21:29.021598
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['command']) == parser.parse(['command', '--'])
    assert parser.parse(['command']) == parser.parse(
        ['command', ARGUMENT_PLACEHOLDER])
    assert parser.parse(['command']) == parser.parse(
        [ARGUMENT_PLACEHOLDER, 'command'])


# Generated at 2022-06-14 08:21:30.518472
# Unit test for constructor of class Parser
def test_Parser():
    Par = Parser()
    assert isinstance(Par, Parser)


# Generated at 2022-06-14 08:21:41.051350
# Unit test for method parse of class Parser
def test_Parser_parse():
    argv = ['thefuck', 'git', 'coomit']
    # test if ARGUMENT_PLACEHOLDER not found
    assert Parser().parse(argv).command == ['git', 'coomit']
    # test if it not command, just arguments
    argv = ['thefuck', '-d']
    assert Parser().parse(argv).command == []
    # test if ARGUMENT_PLACEHOLDER found
    argv = ['thefuck', 'git', ARGUMENT_PLACEHOLDER, '-c', 'git', 'coomit']
    assert Parser().parse(argv).command == ['-c', 'git', 'coomit']


# Generated at 2022-06-14 08:21:49.544470
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    p = Parser()
    import StringIO
    buf = StringIO.StringIO()
    sys.stderr = buf
    p.print_usage()
    sys.stderr = sys.__stderr__
    assert buf.getvalue() == "usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-d] [--force-command FORCE_COMMAND] [-y | -r] [--] [command [command ...]]\n"


# Generated at 2022-06-14 08:21:50.920972
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    assert p._parser is not None

# Generated at 2022-06-14 08:21:54.915085
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:21:56.749736
# Unit test for constructor of class Parser
def test_Parser():
    Parser()

# Demo of constructor of class Parser

# Generated at 2022-06-14 08:21:59.186769
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.parse([])
    parser.print_usage()


# Generated at 2022-06-14 08:22:03.690049
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['fuck', 'start']) == parser.parse(['fuck', 'start'])
    assert parser.parse(['fuck', 'start']) != parser.parse(['fuck', 'start', '--debug'])

# Generated at 2022-06-14 08:22:14.341801
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    '''
    This function is used to unit test method print_help of class Parser
    '''

    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        Parser().print_help()


# Generated at 2022-06-14 08:22:21.168645
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert (parser._parser.parse_args(['-d']).debug == True)
    assert (parser._parser.parse_args(['-l']).shell_logger == None)
    assert (parser._parser.parse_args(['-l','test.log']).shell_logger == 'test.log')
    assert (parser._parser.parse_args(['-v']).version == True)




# Generated at 2022-06-14 08:22:32.380883
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    sys.argv = ['./fuck.py', 'git']
    arguments = parser.parse(sys.argv)
    assert arguments.command == ['git']
    assert arguments.help == False
    sys.argv = ['./fuck.py', 'git', 'push']
    arguments = parser.parse(sys.argv)
    assert arguments.command == ['git', 'push']
    assert arguments.help == False
    sys.argv = ['./fuck.py', 'git', 'stash', 'list', ARGUMENT_PLACEHOLDER, '-q', 'push']
    arguments = parser.parse(sys.argv)
    assert arguments.command == ['git', 'stash', 'list']
    assert arguments.force_command == 'git stash list -q push'



# Generated at 2022-06-14 08:22:34.434741
# Unit test for constructor of class Parser
def test_Parser():
    obj = Parser()
    assert obj._add_arguments() == None


# Generated at 2022-06-14 08:22:45.465487
# Unit test for method parse of class Parser
def test_Parser_parse():
    args = ['thefuck','ls','blabla',ARGUMENT_PLACEHOLDER,'-v','-h']
    parser = Parser()
    result = parser.parse(args)

    assert result.command == ['ls']
    assert result.alias is None
    assert result.yes is False
    assert result.help is False
    assert result.version is True
    assert result.debug is False

    args = ['thefuck','ls',ARGUMENT_PLACEHOLDER,'-v','-h']
    parser = Parser()
    result = parser.parse(args)

    assert result.command == []
    assert result.alias is None
    assert result.yes is False
    assert result.help is False
    assert result.version is True
    assert result.debug is False


# Generated at 2022-06-14 08:22:50.858293
# Unit test for method parse of class Parser
def test_Parser_parse():
    arguments = Parser()._prepare_arguments(['fuck', 'command', '-a', 'fuck', 'with', '-y', '-r'])
    assert ['--', 'command', '-a', 'fuck', 'with', '-y', '-r'] == arguments

# Generated at 2022-06-14 08:23:07.034273
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['-v']) == parser.parse(['--version'])
    assert parser.parse(['-l', 'foo']) == parser.parse(['--shell-logger', 'foo'])
    assert parser.parse(['-d']) == parser.parse(['--debug'])
    assert parser.parse(['-l', 'foo', '-v', '-d', 'foo', 'bar']) == parser.parse(
        ['--debug', '--version', '--shell-logger', 'foo', 'foo', 'bar'])

# Generated at 2022-06-14 08:23:17.299575
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from . import main
    import sys
    from unittest.mock import patch
    with patch('sys.stderr') as mock_stderr:
        main.Parser().print_usage()
    mock_stderr.write.assert_called_once_with(
        sys.stderr,
        'usage: thefuck [-h] [-v] [-a [custom-alias-name]] '
        '[-l shell-logger]\n             [--enable-experimental-instant-mode] '
        '[-d] [--force-command force-command]\n             [--yes | '
        '--repeat] [command [command ...]]\n')


# Generated at 2022-06-14 08:23:27.503039
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from io import StringIO
    from .utils import capture_output

    parser = Parser()
    out, err = capture_output()

    parser.print_usage()
    expected = 'usage: {} [-h] [-v] [-a [custom-alias-name]] ' \
               '[-l shell-logger] [--enable-experimental-instant-mode]' \
               ' [-y | -r] [-d] [--force-command force-command] ' \
               'command ...\n'.format(get_alias())
    assert err.getvalue() == expected

    out, err = capture_output()

# Generated at 2022-06-14 08:23:36.947073
# Unit test for method parse of class Parser
def test_Parser_parse():
    assert Parser().parse(['']) == Namespace(
        _get_namespace_dict(
            command=[],
            debug=False,
            alias=get_alias(),
            version=False,
            force_command=None,
            help=False,
            repeat=False,
            yes=False,
            shell_logger=None,
            enable_experimental_instant_mode=False,
        ))

# Generated at 2022-06-14 08:23:50.534797
# Unit test for method parse of class Parser
def test_Parser_parse():
    Parser_parse_1 = Parser()
    sys.argv = ['thefuck', 'echo', 'a', 'b', 'c', '--', 'd', 'e', 'f']
    Parser_parse_1.parse(sys.argv) == ['echo', 'a', 'b', 'c', '--', 'd', 'e', 'f']
    sys.argv = ['thefuck', 'echo', 'a', 'b', 'c', 'd', 'e', 'f']
    Parser_parse_1.parse(sys.argv) == ['echo', 'a', 'b', 'c', 'd', 'e', 'f']
    sys.argv = ['thefuck', 'echo']
    Parser_parse_1.parse(sys.argv) == ['echo']

# Generated at 2022-06-14 08:23:52.170414
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:23:53.940149
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:23:56.574071
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    """
    prints the usage information for the command
    """
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:23:58.480745
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    # Call the method print_usage() from Parser class
    parser = Parser()
    parser.print_usage()

# Generated at 2022-06-14 08:24:04.234072
# Unit test for method parse of class Parser
def test_Parser_parse():
    # Initialize a instance of class Parser
    test_parser = Parser()

    # Check if the result of parse matches the given string
    assert(test_parser.parse('thefuck --debug -h') == 
    _parser.parse_args(['--debug', '-h']))



# Generated at 2022-06-14 08:24:15.132508
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.parse(["thefuck"])
    parser.print_usage()


# Generated at 2022-06-14 08:24:24.828561
# Unit test for method parse of class Parser
def test_Parser_parse():
    assert Parser().parse(['thefuck', 'echo', 'test']).command == ['echo', 'test']
    assert Parser().parse(['thefuck', 'echo', 'test', ARGUMENT_PLACEHOLDER, 'test!']).command == ['test!']
    assert Parser().parse(['thefuck', 'echo', 'test']).shell_logger is None
    assert Parser().parse(['thefuck', '--shell-logger', 'test', 'echo', 'test']).shell_logger == 'test'
    assert Parser().parse(['thefuck', 'echo', ARGUMENT_PLACEHOLDER, 'test', '--', '--shell-logger', 'test']).command == ['test', '--shell-logger', 'test']

# Generated at 2022-06-14 08:24:26.867363
# Unit test for method print_help of class Parser
def test_Parser_print_help():

    parser = Parser()

    parser.print_usage()
    parser.print_help()

# Generated at 2022-06-14 08:24:38.136805
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    with StringIO() as buf, redirect_stdout(buf):
        Parser().print_help()
        help_message = buf.getvalue()

# Generated at 2022-06-14 08:24:39.913520
# Unit test for constructor of class Parser
def test_Parser():
    assert isinstance(Parser(), Parser)




# Generated at 2022-06-14 08:24:51.828040
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from io import StringIO
    from unittest.mock import patch
    with patch('sys.stderr', new=StringIO()) as fake_stderr:
        Parser().print_usage()
        assert fake_stderr.getvalue() == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] ' \
                                         '[-l shell-logger] [--enable-experimental-instant-mode] ' \
                                         '[--shell-logger shell-logger] [-d] [-y] ' \
                                         '[-r] [--yes] [--yeah] [--hard] [--repeat] command [command ...]\n'


# Generated at 2022-06-14 08:24:58.684454
# Unit test for method parse of class Parser
def test_Parser_parse():
  # TODO: Arrange
  parser = Parser()
  input = [
    "thefuck",
    "python",
    "-v"
  ]
  expected = parser._parser.parse_args(["-v"])

  # Act
  result = parser.parse(input)

  # Assert
  assert result == expected

# Generated at 2022-06-14 08:25:02.979257
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    thefuck.parser.ArgumentParser = mock.MagicMock()

    parser = thefuck.parser.Parser()
    parser.print_usage()

    thefuck.parser.ArgumentParser.return_value.print_usage.assert_called_once_with(sys.stderr)


# Generated at 2022-06-14 08:25:04.188032
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser

# Generated at 2022-06-14 08:25:08.205711
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    sys.argv = ['thefuck', 'sudo', 'fuck']
    parser = Parser()
    actual = parser.print_usage()
    assert actual == None

# Generated at 2022-06-14 08:25:28.296232
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser


# Generated at 2022-06-14 08:25:30.021781
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['-h']) == \
        parser._parser.parse_args(['-h'])

# Generated at 2022-06-14 08:25:42.535594
# Unit test for method parse of class Parser
def test_Parser_parse():
    # Test the normal case
    argv = ['thefuck', 'thefuck', 'help', '-a', 'fuck', ARGUMENT_PLACEHOLDER, 'command', 'arg']
    result = Parser().parse(argv)
    assert result.alias == 'fuck'
    assert result.command == ['command', 'arg']
    assert result.help is False
    assert result.repeat is False
    assert result.version is False
    assert result.yes is False

    # Test the case when `--` is not needed to separate arguments
    argv = ['thefuck', 'command', 'arg']
    result = Parser().parse(argv)
    assert result.alias is None
    assert result.command == ['command', 'arg']
    assert result.help is False
    assert result.repeat is False
    assert result.version

# Generated at 2022-06-14 08:25:43.658847
# Unit test for constructor of class Parser
def test_Parser():
    Parser()



# Generated at 2022-06-14 08:25:47.499108
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    """Given: ArgumentParser object.
       When: I call method print_help.
       Then: Method must print help text, that looks like string
    """
    arg_parser = Parser()
    if arg_parser.print_help() == isinstance(str, arg_parser.print_help()):
        raise

# Generated at 2022-06-14 08:25:56.445873
# Unit test for method parse of class Parser
def test_Parser_parse():
    arguments = ['fuck', '-d', '--force-command', 'bash', 'cd', '-a']
    # ARGUMENT_PLACEHOLDER is the first element of arguments, so the command
    # and the arguments after it should be moved to the first place
    arguments.insert(0, ARGUMENT_PLACEHOLDER)

    parser = Parser()
    options = parser.parse(arguments)

    assert options.force_command == 'bash'
    assert options.command == ['--cd', '-a']

# Generated at 2022-06-14 08:25:58.075048
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser()


# Generated at 2022-06-14 08:25:59.538575
# Unit test for constructor of class Parser
def test_Parser():
    Parser()


# Generated at 2022-06-14 08:26:00.725500
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:26:03.653691
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()

if __name__ == '__main__':
    test_Parser_print_usage()

# Generated at 2022-06-14 08:26:40.468410
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser is not None


# Generated at 2022-06-14 08:26:51.621693
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    stderr_str = StringIO()
    sys.stderr = stderr_str

# Generated at 2022-06-14 08:27:02.496889
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from .utils import get_close_matches
    from .utils_os import system

    parser = Parser()

    # Short usage
    system('thefuck -h')
    assert parser.print_usage in get_close_matches(
        'usage: thefuck [-h]', system.stdout)

    try:
        # Long usage
        system('thefuck --help')
        assert parser.print_usage in get_close_matches(
            'usage: thefuck [-h]', system.stdout)
    except SystemExit:
        # Argument parser raises SystemExit with code 0
        pass


# Generated at 2022-06-14 08:27:08.909917
# Unit test for method parse of class Parser
def test_Parser_parse():
    from argparse import Namespace
    parser = Parser()
    result = parser.parse(['todo', 'todo', 'todo', '--script-debug', '--', 'todo', 'todo'])
    assert result == Namespace(command=['todo', 'todo'], alias=None, yes=False, repeat=False, shell_logger=None, enable_experimental_instant_mode=False, help=False, debug=True, force_command=None)



# Generated at 2022-06-14 08:27:10.608851
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser != None

# Generated at 2022-06-14 08:27:14.326337
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()

    # test with argument '--help'
    args = parser.parse(['thefuck', '--help'])
    assert args.help

    # test with argument '-h'
    args = parser.parse(['thefuck', '-h'])
    assert args.help

    # test with argument '--version'
    args = parser.parse(['thefuck', '--version'])
    assert args.version

    # test with argument '-v'
    args = parser.parse(['thefuck', '-v'])
    assert args.version

# Generated at 2022-06-14 08:27:22.073366
# Unit test for method parse of class Parser
def test_Parser_parse():
    test_parser = Parser()
    res = test_parser.parse(['/home/vagrant/.virtualenvs/lovelypig/bin/thefuck',
                             'git',
                             'add'])
    assert res.alias == False
    assert res.debug == False
    assert res.force_command == None
    assert res.shell_logger == None
    assert res.yes == False
    assert res.repeat == False
    assert res.enable_experimental_instant_mode == False
    assert res.help == False
    assert res.command == ['git', 'add']
    assert res.version == False

# Generated at 2022-06-14 08:27:31.349081
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    import StringIO
    import sys
    old_stderr, sys.stderr = sys.stderr, StringIO.StringIO()
    p = Parser()
    p.print_usage()
    assert sys.stderr.getvalue() == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-d] [command [command ...]]\n'
    sys.stderr = old_stderr


# Generated at 2022-06-14 08:27:33.921255
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    assert isinstance(parser, Parser)
    help_message = parser.print_help()
    assert isinstance(help_message, None)


# Generated at 2022-06-14 08:27:35.186508
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_usage()
    parser.print_help()

# Generated at 2022-06-14 08:28:53.324595
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser.prog == 'thefuck'

# Generated at 2022-06-14 08:28:57.215462
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    assert p
    assert callable(p.print_help)
    assert callable(p.print_usage)
    assert callable(p.parse)



# Generated at 2022-06-14 08:28:59.545425
# Unit test for method print_help of class Parser
def test_Parser_print_help():
	# Given
	#
	# When
	parser = Parser()
	# Then
	#
	assert parser

# Generated at 2022-06-14 08:29:05.692940
# Unit test for constructor of class Parser
def test_Parser():
    """Unit test for constructor of class Parser.

    Execute command:
    $ pytest tests/test_Parser.py -s
    """

    test_parser = Parser()
    assert test_parser._parser.prog == "thefuck"
    assert test_parser._parser.add_help == False

    test_parser.parse(['thefuck', '-v'])
    test_parser.print_usage()
    test_parser.print_help()
    print("\n----\nPass!")

# Generated at 2022-06-14 08:29:18.479882
# Unit test for method parse of class Parser
def test_Parser_parse():
    from .utils import get_parsed_arguments
    # without placeholder
    assert get_parsed_arguments(['--shell-logger', 'shell.log', 'foo']) == \
        Parser().parse(['', '--shell-logger', 'shell.log', 'foo'])
    # with placeholder
    assert get_parsed_arguments(
        ['--shell-logger', 'shell.log', 'ls', ARGUMENT_PLACEHOLDER,
         'bar', '-l']) == \
        Parser().parse(
            ['', '--shell-logger', 'shell.log', 'foo', ARGUMENT_PLACEHOLDER,
             'bar', '-l'])

# Generated at 2022-06-14 08:29:25.268287
# Unit test for method parse of class Parser
def test_Parser_parse():
    from .utils import is_shell
    class DummyArgv:
        def __init__(self, argv):
            self.argv = argv

        def __getitem__(self, index):
            return self.argv[index]

    class DummyArgumentParser:
        def __init__(self):
            pass

        def add_argument(self, *args, **kwargs):
            pass

        def add_mutually_exclusive_group(self):
            class DummyGroup:
                pass
            return DummyGroup()

        def parse_args(self, args):
            return args

        def print_usage(self, f=None):
            pass

        def print_help(self, f=None):
            pass


# Generated at 2022-06-14 08:29:35.868223
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser.prog == 'thefuck'
    assert parser._parser._actions[0].dest == 'alias'
    assert parser._parser._actions[1].dest == 'shell_logger'
    assert parser._parser._actions[2].dest == 'enable_experimental_instant_mode'
    assert parser._parser._actions[3].dest == 'help'
    assert parser._parser._actions[4].dest == 'debug'
    assert parser._parser._actions[5].dest == 'force_command'
    assert parser._parser._actions[6].dest == 'command'

# Generated at 2022-06-14 08:29:38.014286
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser != None
    assert parser._parser != None


# Generated at 2022-06-14 08:29:39.182302
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()

# Generated at 2022-06-14 08:29:40.862231
# Unit test for constructor of class Parser
def test_Parser():
    parser1 = Parser()
    assert parser1._parser.prog == 'thefuck'