

# Generated at 2022-06-14 08:20:50.377146
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    help_text = parser.print_help()
    assert '-a [custom-alias-name], --alias' in help_text

# Generated at 2022-06-14 08:21:00.921864
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    """
    in the print_help function ,it will print the help message to the stderr.
    so in the test_Parser_print_help function, it will get the help message and check the help message with expected message.
    """

    test_parser = Parser()
    help_message = StringIO()
    sys.stderr = help_message
    test_parser.print_help()

# Generated at 2022-06-14 08:21:02.794769
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser


# Generated at 2022-06-14 08:21:16.047713
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    parser.parse([sys.executable, 'fuck'])
    parser.parse([sys.executable, 'fuck', '--alias'])
    parser.parse([sys.executable, 'fuck', '--help'])
    parser.parse([sys.executable, 'fuck', '--debug'])
    parser.parse([sys.executable, 'fuck','--force-command','ls'])
    parser.parse([sys.executable, 'fuck','--enable-experimental-instant-mode'])
    parser.parse([sys.executable, 'fuck','--shell-logger','file'])
    parser.parse([sys.executable, 'fuck','--repeat'])
    parser.parse([sys.executable, 'fuck','--yes'])

# Generated at 2022-06-14 08:21:23.762402
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    # Test command line options.
    assert parser.parse(['-d']).debug is True
    assert parser.parse(['--debug']).debug is True
    assert parser.parse(['-y']).yes is True
    assert parser.parse(['-r']).repeat is True
    assert parser.parse(['--shell-logger', 'log.txt']).shell_logger == 'log.txt'
    assert parser.parse(['-h']).help is True
    assert parser.parse(['-v']).version is True
    assert parser.parse(['-a']).alias is None
    assert parser.parse(['--alias', 'alias_name']).alias == 'alias_name'

# Generated at 2022-06-14 08:21:35.777042
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()

    assert parser.parse([]) == parser.parse(['--']) == \
           parser._parser.parse_args([])
    assert parser.parse(['1']) == parser.parse(['--', '1']) == parser.parse(['1', '--']) == \
           parser._parser.parse_args(['--', '1'])
    assert parser.parse(['1', '2', '3']) == parser.parse(['--', '1', '2', '3']) == parser.parse(['1', '2', '3', '--']) == \
           parser._parser.parse_args(['--', '1', '2', '3'])

# Generated at 2022-06-14 08:21:38.705971
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    # given
    parser = Parser()

    # when
    parser.print_help()

    # then
    assert True


# Generated at 2022-06-14 08:21:52.472401
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(['script_name', 'ls', '-a'])
    assert args.command == ['ls', '-a']
    assert args.alias is None

    args = parser.parse(['script_name', '-a', 'ls', '-a'])
    assert args.command == ['ls', '-a']
    assert args.alias is None

    args = parser.parse(['script_name', '--', '-a', 'ls', '-a'])
    assert args.command == ['-a', 'ls', '-a']
    assert args.alias is None

    args = parser.parse(['script_name', 'ls', '-a', ARGUMENT_PLACEHOLDER,
                         '-a'])

# Generated at 2022-06-14 08:21:54.386121
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    assert parser.print_help() is None

# Generated at 2022-06-14 08:22:08.385466
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    # Given a mock of stdout
    class MockStderr(object):
        def __init__(self):
            self.data = []

        def isatty(self):
            return True

        def write(self, data):
            self.data.append(data)

    mock_stdout = MockStderr()
    sys.stderr = mock_stdout

    parser = Parser()
    parser.print_help()

    # When I call print_help

# Generated at 2022-06-14 08:22:18.447494
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()
    # Output:
    #usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER]
    #               [--enable-experimental-instant-mode] [-d] [--force-command FORCE_COMMAND]
    #               [--yes | --repeat]
    #               [command [command ...]]
    #
    #Fixes your command

# Generated at 2022-06-14 08:22:20.682756
# Unit test for method parse of class Parser
def test_Parser_parse():
    args = Parser().parse(["some", "--arg"])
    assert args.command == ["some", "--arg"]

# Generated at 2022-06-14 08:22:23.486528
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    sys.argv = 'python3 ./thefuck/parser.py --help'.split(' ')
    p = Parser()
    p.print_help()


# Generated at 2022-06-14 08:22:27.015706
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(['fuck', 'command', ARGUMENT_PLACEHOLDER, '-a'])
    assert args.alias == get_alias()
    assert args.command == ['command']


# Generated at 2022-06-14 08:22:33.672423
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    sys.stderr = StringIO()
    Parser().print_usage()
    usage = sys.stderr.getvalue()
    assert 'usage: thefuck' in usage and '[-h] [-v] [-a [custom-alias-name]]' \
        '[-l shell-logger] [--enable-experimental-instant-mode] [-y] [-r] [-d] [--]' in usage


# Generated at 2022-06-14 08:22:35.125335
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()



# Generated at 2022-06-14 08:22:38.823326
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    """
    Create a Parser object
    Call print_usage
    """
    parser1 = Parser()
    parser1.print_usage()


# Generated at 2022-06-14 08:22:47.917451
# Unit test for method parse of class Parser
def test_Parser_parse():
    command_with_args = ['fuck', 
                         '-y', 
                         '--logger', 
                         'test.log', 
                         '-d', 
                         'pip', 
                         'install', 
                         'requests', 
                         ARGUMENT_PLACEHOLDER, 
                         '--no-cache-dir', 
                         'fuck', 
                         'new_args']
    command_without_args = ['fuck', 'ERROR:', '--logger', 'test.log', '-d']
    parser = Parser()
    
    #command without ARGUMENT_PLACEHOLDER
    result = parser.parse(command_without_args)
    assert result.command == ['ERROR:']
    assert result.debug == True

# Generated at 2022-06-14 08:23:00.028655
# Unit test for method parse of class Parser
def test_Parser_parse():
    assert (Parser().parse(['thefuck', '-l', 'shell.log']) ==
            Parser()._parser.parse_args(['-l', 'shell.log']))
    assert (Parser().parse(['thefuck', '-a', 'f', 'ls', '-l']) ==
            Parser()._parser.parse_args(['-a', 'f', '--', 'ls', '-l']))
    assert (Parser().parse(['thefuck', '-l', 'shell.log', 'ls', '-l', ARGUMENT_PLACEHOLDER, '-s']) ==
            Parser()._parser.parse_args(['-l', 'shell.log', '--', 'ls', '-l', ARGUMENT_PLACEHOLDER, '-s']))

# Generated at 2022-06-14 08:23:02.485275
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser_print_usage = Parser()
    parser_print_usage.print_usage()



# Generated at 2022-06-14 08:23:17.514595
# Unit test for method parse of class Parser
def test_Parser_parse():
    with pytest.raises(SystemExit):
        assert Parser().parse([])

    with pytest.raises(SystemExit):
        assert Parser().parse(['thefuck'])

    assert Parser().parse(['thefuck', 'ls']) == \
        argparse.Namespace(command=['ls'],
                           debug=False,
                           force_command=None,
                           repeat=False,
                           shell_logger=None,
                           yeah=False,
                           alias=None,
                           enable_experimental_instant_mode=False,
                           help=False,
                           version=False)

    assert Parser().parse(['thefuck', '-d', '--force-command', 'ls', '-r',
                           '--yes']) == \
        argparse.Namespace

# Generated at 2022-06-14 08:23:19.319120
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()



# Generated at 2022-06-14 08:23:26.981368
# Unit test for method parse of class Parser
def test_Parser_parse():

    parser = Parser()

    # Removing arguments containing placeholder
    result = parser.parse(['', 'toto', ARGUMENT_PLACEHOLDER, 'titi'])
    assert result.command == []

    # Adding a '--' before arguments of the command
    result = parser.parse(['', 'toto', 'titi'])
    assert result.command == ['toto', 'titi']



# Generated at 2022-06-14 08:23:30.078618
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    match = parser.parse(['fuck', 'git co -- '])

    assert match.command == ['git', 'co', '--']


# Generated at 2022-06-14 08:23:31.261111
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser


# Generated at 2022-06-14 08:23:32.412001
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser() != None



# Generated at 2022-06-14 08:23:39.242309
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    from thefuck.types import Arguments
    assert parser.parse(['some_command', ARGUMENT_PLACEHOLDER, '--yes']) == Arguments(alias=None, command='', debug=False, enable_experimental_instant_mode=False, force_command=None, help=False, repeat=False, shell_logger=None, version=False, yes=True)
    assert parser.parse(['some_command', ARGUMENT_PLACEHOLDER, '--debug']) == Arguments(alias=None, command='', debug=True, enable_experimental_instant_mode=False, force_command=None, help=False, repeat=False, shell_logger=None, version=False, yes=False)

# Generated at 2022-06-14 08:23:40.448472
# Unit test for constructor of class Parser
def test_Parser():
    Parser()

# Generated at 2022-06-14 08:23:42.179752
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser is not None


# Generated at 2022-06-14 08:23:45.584919
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.parse(['--','git','push','ov'])
    parser.print_usage()

# Unit test method print_help of class Parser

# Generated at 2022-06-14 08:23:49.613760
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser()


# Generated at 2022-06-14 08:23:55.311406
# Unit test for method parse of class Parser
def test_Parser_parse():
    try:
        parser = Parser()
        parser.parse(['thefuck','vim','--help','help','fuck','history',ARGUMENT_PLACEHOLDER,'a','b','c','d','e','f','1','2','3'])
    except Exception:
        assert False
    assert True

# Generated at 2022-06-14 08:23:57.576326
# Unit test for constructor of class Parser
def test_Parser():
    from .parser import Parser
    parser = Parser()
    assert parser._parser.prog == 'thefuck'
    assert parser._parser.add_help == False


# Generated at 2022-06-14 08:24:07.731114
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    stdout = sys.stdout
    stdout.truncate(0)
    sys.stdout = io.StringIO()
    try:
        Parser().print_usage()
        sys.stdout.seek(0)
        assert sys.stdout.read() == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-d] [--force-command FORCE_COMMAND] [--] [command [command ...]]\n'
    finally:
        sys.stdout.close()
        sys.stdout = stdout


# Generated at 2022-06-14 08:24:14.156513
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    with mock.patch.object(parser, '_parser') as mock_parser:
        parser.print_usage()
        mock_parser.print_usage.assert_called_with(sys.stderr)
        sys.stderr.flush()


# Generated at 2022-06-14 08:24:24.607938
# Unit test for constructor of class Parser

# Generated at 2022-06-14 08:24:26.061193
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:24:27.835046
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()
    assert True

# Generated at 2022-06-14 08:24:34.057159
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser.prog == 'thefuck'
    assert parser._parser.add_help == False
    assert parser._parser.version == None
    assert parser._parser.alias == None
    assert parser._parser.shell_logger == None
    assert parser._parser.debug == None
    assert parser._parser.force_command == None

# Generated at 2022-06-14 08:24:36.408701
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

test_Parser_print_help()

# Generated at 2022-06-14 08:24:41.329614
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    Parser().print_help()

# Generated at 2022-06-14 08:24:54.596701
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()

    def assert_argv(expected, argv):
        assert expected.command == parser.parse(argv).command

    assert_argv(
        argparse.Namespace(
            command=['git', 'push', 'origin', 'master', ':foo'],
            debug=False, alias=None, yes=False, repeat=False,
            shell_logger=False, force_command=None,
            help=False),
        sys.argv + ['git', 'push', 'origin', 'master', ':foo'])


# Generated at 2022-06-14 08:25:06.321504
# Unit test for method parse of class Parser
def test_Parser_parse():
    from .utils import get_alias

    parser = Parser()
    parsed_arguments = parser.parse(['thefuck', '-v'])
    assert parsed_arguments.version

    parsed_arguments = parser.parse(['thefuck', '--version'])
    assert parsed_arguments.version

    parsed_arguments = parser.parse(
        ['thefuck', '--alias', 'lefuck', '-v'])
    assert parsed_arguments.alias == 'lefuck'
    assert parsed_arguments.version

    parsed_arguments = parser.parse(['thefuck', '--alias', '-v'])
    assert parsed_arguments.alias == get_alias()
    assert parsed_arguments.version

    parsed_arguments = parser.parse(['thefuck', '-a', '-v'])
   

# Generated at 2022-06-14 08:25:13.811093
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    with patch('sys.stderr', new=StringIO()) as stderr:
        parser.print_usage()
    assert stderr.getvalue() == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]]\n' \
                                '              [-l SHELL_LOGGER]\n' \
                                '              [--enable-experimental-instant-mode]\n' \
                                '              [-y | -r] [-d] [--force-command FORCE_COMMAND]\n' \
                                '              [command [command ...]]\n'


# Generated at 2022-06-14 08:25:15.280221
# Unit test for constructor of class Parser
def test_Parser():
	parser = Parser()

# Generated at 2022-06-14 08:25:29.054209
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    output = StringIO()
    sys.stderr = output
    parser.print_help()
    sys.stderr = sys.__stderr__

# Generated at 2022-06-14 08:25:29.853119
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()  # no error raised



# Generated at 2022-06-14 08:25:34.592279
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    res = parser.print_help()
    assert res is None

if __name__ == '__main__':
    test_Parser_print_help()

# Generated at 2022-06-14 08:25:45.080061
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['fuck']) == parser.parse(['fuck', '--']) == parser.parse(['fuck', '--','--'])
    assert parser.parse(['fuck', '-v']) == parser.parse(['fuck', '-v', '--'])
    assert parser.parse(['fuck', 'ver']) == parser.parse(['fuck', '-a', 'ver', '--'])
    assert parser.parse(['fuck', 'ver']) != parser.parse(['fuck', '-r', 'ver', '--'])
    assert parser.parse(['fuck', 'ver']) != parser.parse(['fuck', '-y', 'ver', '--'])


# Generated at 2022-06-14 08:25:46.887976
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:26:02.392049
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()
    # assert sys.stderr.getvalue() == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER]\n            [--enable-experimental-instant-mode] [-d] [--force-command FORCE_COMMAND]\n            [command [command ...]]\n'


# Generated at 2022-06-14 08:26:04.147671
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    assert parser.print_help() == None

# Generated at 2022-06-14 08:26:17.279296
# Unit test for method print_help of class Parser

# Generated at 2022-06-14 08:26:18.991163
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    p = Parser()
    p.print_help()

# Generated at 2022-06-14 08:26:31.908238
# Unit test for method parse of class Parser
def test_Parser_parse():
    argv = ['thefuck', 'ls', '-l']
    parsed = Parser().parse(argv)
    assert not parsed.alias
    assert parsed.shell_logger is None
    assert parsed.command == ['ls', '-l']
    assert not parsed.debug
    assert not parsed.help
    assert not parsed.repeat
    assert not parsed.yes
    assert not parsed.version

    argv = ['thefuck', '--alias', 'fuck', 'ls', '-l']
    parsed = Parser().parse(argv)
    assert parsed.alias == 'fuck'
    assert parsed.shell_logger is None
    assert parsed.command == ['ls', '-l']
    assert not parsed.debug
    assert not parsed.help
    assert not parsed.repeat
    assert not parsed.yes
    assert not parsed.version

# Generated at 2022-06-14 08:26:37.520653
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser.prog == "thefuck"
    assert parser._parser.usage is None
    assert parser._parser.description is None
    assert parser._parser.epilog is None
    assert parser._parser.version is None


# Generated at 2022-06-14 08:26:50.742553
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    parser.parse(['thefuck', 'command']) \
        .should.equal(argparse.Namespace(
            alias=None,
            command=['command'],
            debug=False,
            enable_experimental_instant_mode=False,
            force_command=None,
            help=False,
            repeat=False,
            shell_logger=None,
            version=False,
            yes=False))


# Generated at 2022-06-14 08:26:52.459773
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:26:54.327254
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    assert isinstance(p, Parser)

# Generated at 2022-06-14 08:27:05.911138
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()

    assert parser._parser.prog == "thefuck"
    assert parser._parser.add_help == False
    assert parser._parser._actions[0].option_strings == ['-v', '--version']
    assert parser._parser._actions[0].help == "show program's version number and exit"
    assert parser._parser._actions[0].action == 'store_true'
    assert parser._parser._actions[1].option_strings == ['-a', '--alias']
    assert parser._parser._actions[1].const == get_alias()
    assert parser._parser._actions[1].help == '[custom-alias-name] prints alias for current shell'
    assert parser._parser._actions[2].option_strings == ['-l', '--shell-logger']
    assert parser._parser._actions[2].help

# Generated at 2022-06-14 08:27:37.781591
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['thefuck', 'ls', 'somewhere', ARGUMENT_PLACEHOLDER, '-l']) == parser.parse(['thefuck', '--', 'ls', 'somewhere', '-l'])
    assert parser.parse(['thefuck', 'ls', 'somewhere', ARGUMENT_PLACEHOLDER, '-l']) == parser.parse(['thefuck', 'ls', 'somewhere', '-l'])
    # TODO(https://github.com/nvbn/thefuck/issues/301)
    # assert parser.parse(['thefuck', 'ls', 'somewhere', ARGUMENT_PLACEHOLDER, '-l']) == parser.parse(['thefuck', '-l', 'ls', 's

# Generated at 2022-06-14 08:27:50.904622
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    argv = [
        sys.executable, 'some_script', '-v', '-d',
        '--debug', '--shell-logger=foo.log', '--force-command', 'cd',
        '-y', '--alias', 'fuck', '--',
        'git', 'push', ARGUMENT_PLACEHOLDER,
        '--verbose', '--force', '--rebase=interactive'
    ]
    command = [
        'git', 'push', '--verbose', '--force', '--rebase=interactive'
    ]
    args = parser.parse(argv)
    assert args.version
    assert args.debug
    assert args.shell_logger == 'foo.log'
    assert args.force_command == 'cd'


# Generated at 2022-06-14 08:27:58.400477
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(['fuck', '--alias'])
    assert args.alias == get_alias()

    args = parser.parse(['fuck', 'ssh', '-v'])
    assert args.command == ['ssh', '-v']

    args = parser.parse(['fuck', '-v', 'ssh', '-v'])
    assert args.command == ['ssh', '-v']

    args = parser.parse(['fuck', '--'])
    assert args.command == []

    args = parser.parse(['fuck', '--', 'ssh'])
    assert args.command == ['ssh']

    args = parser.parse(['fuck', 'no_such_command', '-v'])
    assert args.command == ['--', 'no_such_command', '-v']



# Generated at 2022-06-14 08:28:11.062796
# Unit test for method parse of class Parser
def test_Parser_parse():
    p = Parser()

# Generated at 2022-06-14 08:28:13.135506
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    arg_parser = Parser()
    assert arg_parser.print_usage() != None

# Generated at 2022-06-14 08:28:14.476707
# Unit test for constructor of class Parser
def test_Parser():
    # Check the class is instantiable
    Parser()

# Generated at 2022-06-14 08:28:15.867975
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser


# Generated at 2022-06-14 08:28:17.873434
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser
    assert isinstance(parser, Parser)


# Generated at 2022-06-14 08:28:19.127938
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:28:26.520866
# Unit test for method print_help of class Parser
def test_Parser_print_help():
	from unittest import mock
	#Redirecting stderr to stdout, because of different behaviour in py2 and py3
	with mock.patch("sys.stdout", new=sys.stderr):
		argv = ["thefuck", "tf"]
		parser = Parser()
		parser.print_help()
		assert argv[0] in sys.stderr.getvalue()

# Generated at 2022-06-14 08:29:18.314471
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    sys.stderr.write = MagicMock()
    obj = Parser()
    obj.print_usage()
    assert sys.stderr.write.call_count == 2


# Generated at 2022-06-14 08:29:20.059037
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    assert p.parse(['thefuck', 'fuck'])

# Generated at 2022-06-14 08:29:21.191697
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser.prog == 'thefuck'

# Generated at 2022-06-14 08:29:31.019887
# Unit test for method parse of class Parser
def test_Parser_parse():
    print("Start unit test for method parse of class Parser")
    parser = Parser()
    assert parser.parse(['thefuck',
                         '--shell-logger=log.txt',
                         'git',
                         'push',
                         'origin',
                         'master',
                         ARGUMENT_PLACEHOLDER]) == \
        parser.parse(['thefuck',
                      '--shell-logger=log.txt',
                      '--',
                      'push origin master'])
    print("End unit test for method parse of class Parser")

# Generated at 2022-06-14 08:29:40.872241
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['thefuck', '--force-command']).force_command is None
    assert parser.parse(['thefuck', '--debug', '--force-command', 'ls']).command == ['ls']
    assert parser.parse(['thefuck', '--debug', '-d']).command == []
    assert parser.parse(['thefuck']).force_command is None
    assert parser.parse(['thefuck']).debug is False
    assert parser.parse(['thefuck', '--debug']).debug is True
    assert parser.parse(['thefuck', 'error']).command == ['error']
    assert parser.parse(['thefuck', '-y', 'error']).command == ['error']

# Generated at 2022-06-14 08:29:53.548211
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    class FakeStderr(object):
        def __init__(self):
            self.messages = []

        def write(self, message):
            self.messages.append(message)

    fake_stderr = FakeStderr()
    with patch('sys.stderr', fake_stderr):
        Parser().print_usage()
    assert fake_stderr.messages == ['usage: thefuck [-h] [-v] [-a [custom-alias-name]] '
                                    '[-l SHELL_LOGGER] [--enable-experimental-instant-mode] '
                                    '[--force-command FORCE_COMMAND] [-y] [-r] '
                                    '[-d] [command [command ...]]\n']



# Generated at 2022-06-14 08:30:02.934470
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    result = ""
    with Capturing() as output:
        Parser().print_usage()
    for item in output:
        result += item
    assert result == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] ' \
                     '[-l shell-logger] [--enable-experimental-instant-mode] ' \
                     '[-y | -r] [-d] [--force-command FORCE_COMMAND] ' \
                     '[command [command ...]]\n'


# Generated at 2022-06-14 08:30:07.509364
# Unit test for method parse of class Parser
def test_Parser_parse():
    # Arrange
    p = Parser()
    # Act
    actual = p.parse(['', '--help'])
    # Assert
    assert actual.help is True


# Generated at 2022-06-14 08:30:11.913858
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(["thefuck", "git", "push", "--force"])
    assert args.command == ["git", "push", "--force"]
    assert args.debug is False


# Generated at 2022-06-14 08:30:17.333641
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    import sys
    from io import StringIO
    from thefuck.parser import Parser
    parser = Parser()
    print = StringIO()
    sys.stderr = print
    parser.print_usage()
    assert "usage: thefuck [-h] [-v]" in print.getvalue()
