

# Generated at 2022-06-14 08:20:53.397553
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    #Unit test returns false if Parser.print_usage() returns a string
    assert parser.print_usage() is None, "Parser.print_usage() is returning a string"


# Generated at 2022-06-14 08:21:00.696585
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    expected = 'usage: thefuck [-v] [-a [custom-alias-name]] ' + \
               '[-l shell-logger] [--enable-experimental-instant-mode] ' + \
               '[-h] [-d] [--force-command force-command] ' + \
               '[command [command ...]]\n'
    assert (parser.print_usage()) == (expected)


# Generated at 2022-06-14 08:21:03.670717
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    assert isinstance(p, object)
    assert isinstance(p._parser, ArgumentParser)


# Generated at 2022-06-14 08:21:12.732605
# Unit test for method parse of class Parser
def test_Parser_parse():
    inp = ['--debug', 'df -h', 'dfs -f']
    from argparse import Namespace
    assert Parser().parse(inp) == Namespace(cla=None, debug=True,
                                            enable_experimental_instant_mode=False, help=False,
                                            repeat=False, yes=False,
                                            command=['df', '-h'],
                                            shell_logger=None,
                                            force_command=None,
                                            alias=None,
                                            version=False)

# Generated at 2022-06-14 08:21:15.428121
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.parse(['thefuck'])
    result = parser.print_usage()
    assert result == None


# Generated at 2022-06-14 08:21:22.099834
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser=Parser()
    assert parser.parse(['thefuck', '--alias']) == {'alias': get_alias()}
    assert parser.parse(['thefuck', '--help']) == {'help': True}
    assert parser.parse(['thefuck', '--debug']) == {'debug': True}
    assert parser.parse(['thefuck', 'echo', 'hello']) == {'command': ['echo', 'hello']}
    assert parser.parse(['thefuck', 'echo',  ARGUMENT_PLACEHOLDER,'hello']) == {'command': ['echo', 'hello']}

# Generated at 2022-06-14 08:21:34.604035
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()

    args = parser.parse(['thefuck', 'command1', '-y'])
    assert args.yes
    assert not args.repeat

    args = parser.parse(['thefuck', 'command1', 'command2', '-r'])
    assert args.repeat
    assert not args.yes
    assert ['command1', 'command2'] == args.command

    args = parser.parse(['thefuck', 'command1', ARGUMENT_PLACEHOLDER, '--',
                         '-d', '--', 'command2'])
    assert args.debug
    assert ['command2'] == args.command
    assert ['command1', '-d'] == args.yes

    args = parser.parse(['thefuck', 'command1', 'command2'])

# Generated at 2022-06-14 08:21:48.078192
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['./thefuck', 'command']).command == ['command']
    assert parser.parse(['./thefuck', 'command', 'command_args']
                        ).command == ['command', 'command_args']
    assert parser.parse(['./thefuck', 'command', '--', 'command_args']
                        ).command == ['command']
    assert parser.parse(['./thefuck', 'command', '--', '--option',
                         'command_args']).command == ['command']
    assert parser.parse(['./thefuck', ARGUMENT_PLACEHOLDER,
                         'command_args', 'command']).command == ['command']

# Generated at 2022-06-14 08:21:56.354981
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from StringIO import StringIO
    output = StringIO()
    parser = Parser()
    parser.print_help()
    sys.stderr = output
    help_string = "usage: thefuck [-h] [-v] [-a [custom-alias-name]]\n" + \
                  "                [-l SHELL_LOGGER]\n" + \
                  "                [--enable-experimental-instant-mode]\n" + \
                  "                [-y | -r] [-d] [--force-command FORCE_COMMAND]\n" + \
                  "                [command [command ...]]\n"
    assert help_string in output.getvalue()
    help_string = "positional arguments:\n" + \
                  "  command               command that should be fixed\n\n"
    assert help_string

# Generated at 2022-06-14 08:22:08.809665
# Unit test for method parse of class Parser

# Generated at 2022-06-14 08:22:14.115570
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    assert parser.print_help()

# Generated at 2022-06-14 08:22:15.396502
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()

# Generated at 2022-06-14 08:22:17.661535
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    assert "optional arguments:" in parser.print_help()


# Generated at 2022-06-14 08:22:27.224918
# Unit test for method parse of class Parser
def test_Parser_parse():
    '''
    Unit test for method parse of class Parser
    '''
    args = ["some message",
            "--help",
            "--version",
            "--force-command",
            "--alias",
            "--shell-logger",
            "--debug",
            "--enable-experimental-instant-mode",
            "--repeat",
            "--yes",
            "-r",
            "-y",
            "-v",
            "-h",
            "-d",
            "-l",
            "--yeah",
            "--hard",
            "--",
            "-1",
            "-2",
            "error msg",
            "other msg"]
    parser = Parser()
    parsed = parser.parse(args)
    assert parsed.alias is None
    assert parsed.shell_logger is None


# Generated at 2022-06-14 08:22:41.593347
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    """
    The test for print_help method of class Parser

    """
    from .const import USAGE, VERSION
    import sys
    from .utils import create_argv
    from .utils import capture_stderr
    from thefuck import main
    parser = Parser()
    sys.argv = create_argv('-h',)
    with capture_stderr() as err:
        main()

# Generated at 2022-06-14 08:22:43.122416
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
	parser=Parser()
	parser.print_usage()
	

# Generated at 2022-06-14 08:22:44.341781
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:22:47.390441
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    print("Test for method print_help of class Parser")
    Parser().print_help()

# Generated at 2022-06-14 08:22:48.169951
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser()

# Generated at 2022-06-14 08:22:52.922152
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['--debug', 'echo', 'test']) == parser.parse(['echo', 'test', '--debug'])
    assert parser.parse(['echo', 'test', '--debug']) == parser.parse(['echo', 'test', '--debug'])

# Generated at 2022-06-14 08:23:06.020008
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    arguments = parser.parse(['', '-d'])
    assert arguments.debug
    arguments = parser.parse(['', '--debug'])
    assert arguments.debug


# Generated at 2022-06-14 08:23:07.406120
# Unit test for constructor of class Parser
def test_Parser():
    Parser()


# Generated at 2022-06-14 08:23:09.718969
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    str = parser.print_usage()
    assert str


# Generated at 2022-06-14 08:23:20.345857
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    # given:
    parser = Parser()
    # exercise:
    parser.print_help()
    # verify:

# Generated at 2022-06-14 08:23:24.090252
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    args = parser.parse(['thefuck', 'cd', '~'])
    assert args.command == ['cd', '~']

# Generated at 2022-06-14 08:23:28.468679
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    # Test if arguments have been added to self._parser
    assert any(self._parser._option_string_actions.keys()) == True
    # Test if parser has been created
    assert parser != None


# Generated at 2022-06-14 08:23:35.462813
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    try:
        sys.stderr = StringIO()
        Parser().print_usage()
        assert sys.stderr.getvalue() == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER]\n                  [--enable-experimental-instant-mode] [-d] [--force-command FORCE_COMMAND]\n                  [--] [command [command ...]]\n'
    finally:
        sys.stderr = sys.__stderr__


# Generated at 2022-06-14 08:23:42.359051
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse([])
    assert args.command == []
    assert args.yes is False
    assert args.repeat is False
    assert args.debug is False
    assert args.force_command is None
    assert args.enable_experimental_instant_mode is False
    assert args.shell_logger is None
    assert args.version is False
    assert args.alias is None
    assert args.help is False

# Generated at 2022-06-14 08:23:43.892516
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    Parser().print_help()

# Generated at 2022-06-14 08:23:48.502306
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    sys_stderr = StringIO()
    sys.stderr = sys_stderr
    parser = Parser()
    parser.print_usage()

    assert 'usage: thefuck' in sys_stderr.getvalue()


# Generated at 2022-06-14 08:24:05.150868
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser
    assert parser._parser

# Generated at 2022-06-14 08:24:09.422875
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()
    output = sys.stderr.getvalue()
    assert output == 'usage: thefuck [OPTIONS] [command [arguments...]]\n'


# Generated at 2022-06-14 08:24:16.346179
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    # Remove place holder and add '--' before 'command'
    assert parser.parse(['thefuck', '--debug', 'ls', ARGUMENT_PLACEHOLDER, '-l', '--help']) == \
        parser._parser.parse_args(['--debug', 'ls', '-l', '--help', '--'])


# Generated at 2022-06-14 08:24:25.129202
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(['thefuck', 'ls', ARGUMENT_PLACEHOLDER, '-l'])
    assert args.l
    assert args.command == ['ls']

    args = parser.parse(['thefuck', '--', 'ls', ARGUMENT_PLACEHOLDER, '-l'])
    assert args.l
    assert args.command == ['ls']

    args = parser.parse(['thefuck', 'ls', ARGUMENT_PLACEHOLDER])
    assert args.command == ['ls']

    args = parser.parse(['thefuck', 'ls', '--color'])
    assert args.command == ['ls', '--color']


# Generated at 2022-06-14 08:24:37.870740
# Unit test for method print_help of class Parser

# Generated at 2022-06-14 08:24:40.711170
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    assert parser.print_usage() == sys.stderr.write(parser._parser.format_usage())

# Generated at 2022-06-14 08:24:50.589379
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from io import StringIO
    from unittest.mock import patch

    parser = Parser()
    capturedOutput = StringIO()
    with patch('sys.stderr', capturedOutput):
        parser.print_usage()
    assert capturedOutput.getvalue() == 'usage: thefuck [-h] [--enable-experimental-instant-mode] [-a [custom-alias-name]] [-y | -r] [-l SHELL_LOGGER] [-d] [--force-command FORCE_COMMAND] [--] [command [command ...]]\n'


# Generated at 2022-06-14 08:24:56.586230
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():

    # Prepare the output
    out = StringIO()

    # Prepare the parser
    parser = Parser()

    # Check the control flow
    parser.print_usage()

    old_stdout = sys.stdout
    sys.stdout = out

    parser.print_usage()
    output = out.getvalue().strip()
    expected = Parser()._parser.format_usage().strip()
    assert output == expected

    sys.stdout = old_stdout

# Generated at 2022-06-14 08:24:58.152399
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:24:59.097271
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert isinstance(parser, Parser)

# Generated at 2022-06-14 08:25:34.215192
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser


# Generated at 2022-06-14 08:25:45.504966
# Unit test for method parse of class Parser
def test_Parser_parse():
    def check(expected, argv):
        assert argv
        parser = Parser()
        assert expected == parser.parse(argv)

    check(Namespace(
        alias=get_alias(),
        force_command=None,
        repeat=False,
        yes=False,
        debug=False,
        shell_logger=None,
        enable_experimental_instant_mode=False,
        help=False,
        version=False,
        command=[]), [])


# Generated at 2022-06-14 08:25:47.076411
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:25:49.273610
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser is not None


# Generated at 2022-06-14 08:25:55.007407
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from .utils import create_output

    with create_output() as output:
        Parser().print_usage()
    result = output.getvalue().strip()

    assert result == (
        "usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l "
        "shell-logger]")



# Generated at 2022-06-14 08:26:02.586653
# Unit test for method parse of class Parser
def test_Parser_parse():
    p = Parser()
    parse_dict = p.parse(["thefuck", "ls", ARGUMENT_PLACEHOLDER, "--"])
    parse_dict = parse_dict.__dict__
    assert parse_dict['command'] == ["ls", ARGUMENT_PLACEHOLDER]
    assert not parse_dict['version']
    assert not parse_dict['debug']
    assert not parse_dict['yes']
    assert not parse_dict['shell_logger']
    assert not parse_dict['help']
    assert not parse_dict['force_command']
    assert not parse_dict['repeat']


# Generated at 2022-06-14 08:26:07.581786
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(['thefuck', './wrong-cmd', ARGUMENT_PLACEHOLDER, 'cd', '-']) # noqa
    assert args.command == './wrong-cmd'



# Generated at 2022-06-14 08:26:13.056885
# Unit test for constructor of class Parser
def test_Parser():
	p = Parser()
	assert p._add_arguments is not None
	assert p._add_conflicting_arguments is not None
	assert p._prepare_arguments is not None
	assert p.parse is not None
	assert p.print_help is not None
	assert p.print_usage is not None

# Generated at 2022-06-14 08:26:16.010376
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    import thefuck.shells
    thefuck.shells.supported_shells = {}
    parser = Parser()
    parser.print_usage()
    pass

# Generated at 2022-06-14 08:26:18.874592
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    assert Parser()._parser.print_usage(sys.stderr) == None


# Generated at 2022-06-14 08:27:02.858906
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser.prog == 'thefuck'
    assert parser._parser.add_help == False
    assert parser.parse(['thefuck', '-v']) == \
        parser._parser.parse_args(['-v'])

# Generated at 2022-06-14 08:27:10.483197
# Unit test for constructor of class Parser
def test_Parser():
    a = Parser()
    assert a._parser.prog == 'thefuck'
    assert a._parser.add_help == False
    assert len(a._parser._positionals._group_actions) == 1
    assert len(a._parser._optionals._group_actions) == 10
    assert a._parser._positionals._group_actions[0].dest == 'command'
    assert a._parser._positionals._group_actions[0].nargs == '*'
    assert a._parser._optionals._group_actions[0].dest == 'version'
    assert a._parser._optionals._group_actions[0].action == 'store_true'
    assert a._parser._optionals._group_actions[1].dest == 'alias'
    assert a._parser._optionals._group_actions[1].nargs == '?'
   

# Generated at 2022-06-14 08:27:12.171890
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser is not None


# Generated at 2022-06-14 08:27:14.344549
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    with patch('sys.stderr'):
        Parser().print_usage()


# Generated at 2022-06-14 08:27:16.657156
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser.prog == 'thefuck'
    assert parser._parser.add_help == False


# Generated at 2022-06-14 08:27:27.855682
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    ### test case 1
    argvs = [ 'python','--alias','fuck','ls' ]
    parsed = parser.parse(argvs)
    assert parsed.command == ['ls'], 'command should be ls'
    assert not parsed.repeat, 'repeat should not be set'
    assert not parsed.yes, 'yes should not be set'
    assert not parsed.enable_experimental_instant_mode, 'enable_experimental_instant_mode should not be set'
    assert parsed.alias == 'fuck', 'alias should be set to fuck'
    assert not parsed.debug, 'debug should not be set'
    assert not parsed.force_command, 'force_command should not be set'
    ### test case 2
    argvs = [ 'python','-r','grep','abc' ]
    parsed = parser

# Generated at 2022-06-14 08:27:30.332565
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser.__dict__['_parser'].prog == 'thefuck'


# Generated at 2022-06-14 08:27:40.442269
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from io import StringIO
    import sys
    sys.stderr = StringIO()

# Generated at 2022-06-14 08:27:42.613201
# Unit test for constructor of class Parser
def test_Parser():
    test_parser = Parser()
    assert(test_parser)

# Test for function parse

# Generated at 2022-06-14 08:27:49.832475
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()
    assert sys.stderr.getvalue() == """usage: thefuck [-h] [-v] [-a [custom-alias-name]]
                  [-l shell-logger] [--enable-experimental-instant-mode] [-d]
                  [-y | -r] [--force-command FORCE_COMMAND] [--] [command]
"""


# Generated at 2022-06-14 08:29:22.128079
# Unit test for method parse of class Parser
def test_Parser_parse():
    from .main import main
    from .utils import get_closest, get_all_matches, get_command_from_history
    from .rules import get_rules
    from .parsers import get_parser
    from .shells import get_aliases
    from .exceptions import AppError
    import argparse
    argv = ['/usr/local/bin/thefuck', 'wiew', 'a', 'b', 'c', 'd', 'e', 'f', 'g']
    p = Parser()

# Generated at 2022-06-14 08:29:31.281907
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['thefuck', 'yes', 'ls', 'se']) == parser.parse(['thefuck', '--yes', 'ls', 'se'])
    assert parser.parse(['thefuck', 'ls', '--', '-a']) == parser.parse(['thefuck', 'ls', '-a'])
    assert parser.parse(['thefuck', 'yes', 'ls', 'se']) == parser.parse(['thefuck', '--yes', 'ls', 'se'])

# Generated at 2022-06-14 08:29:38.462157
# Unit test for constructor of class Parser
def test_Parser():
    a = Parser()
    assert argv==a.parse(argv)
    assert argv[1:]==a.parse(argv)[:-1] or argv==a.parse(argv[1:])
    assert ARGUMENT_PLACEHOLDER in argv==a._prepare_arguments(argv)
    assert '--'+argv[0] in a._prepare_arguments(argv)

# Generated at 2022-06-14 08:29:40.444534
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser._actions[0].dest == 'version'



# Generated at 2022-06-14 08:29:53.667357
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()

    # test parse with placeholder and command
    argv = ["./test.py", "blah", ARGUMENT_PLACEHOLDER, "command", "args"]
    assert parser.parse(argv) == parser._parser.parse_args(["command", "args"])

    # test parse with placeholder and no command
    argv = ["./test.py", "blah", ARGUMENT_PLACEHOLDER]
    assert parser.parse(argv) == parser._parser.parse_args([])

    # test parse without placeholder but command
    argv = ["./test.py", "blah", "command", "args"]
    assert parser.parse(argv) == parser._parser.parse_args(["--", "command", "args"])

# Generated at 2022-06-14 08:30:06.874571
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    # it prints to sys.stderr by default
    class StdErrMock(StringIO):
        def __init__(self):
            StringIO.__init__(self)
        def getvalue(self):
            return self.getvalue()
        def write(self, msg):
            # strip newlines
            self.write(msg.replace("\n", ""))
    stderrMock = StdErrMock()
    if sys.version_info < (3,):
        sys.stderr = stderrMock
    else:
        sys.stderr = io.TextIOWrapper(stderrMock, encoding='utf-8')
    parser.print_help()
    sys.stderr = sys.__stderr__
    # check if

# Generated at 2022-06-14 08:30:18.976194
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    print(parser._parser)

    # test for version
    parser._parser.print_usage(sys.stderr)
    parser._parser.print_help(sys.stderr)

    # test for alias
    parser.parse(['-a', get_alias()])
    parser.parse(['-a'])

    #test for shel-logger
    parser.parse(['-l','/tmp/thefuck.log'])

    #test for enable-experimental-instant-mode
    parser.parse(['--enable-experimental-instant-mode'])

    #test for help
    parser.parse(['-h'])

    # test for force-command
    parser.parse(['--force-command','ls -l'])

    parser.parse(['command'])




# Generated at 2022-06-14 08:30:30.089671
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['thefuck', 'ls', '-la']) == parser._parser.parse_args(['ls', '-la'])
    assert parser.parse(
        ['thefuck', 'git', '-la', '-b', 'master', ARGUMENT_PLACEHOLDER,  '-y', '-v']) == parser._parser.parse_args(
        ['-y', '-v', '--', 'git', '-la', '-b', 'master'])
    assert parser.parse(['thefuck', '-a', 'fuck']) == parser._parser.parse_args(['-a', 'fuck'])


# Generated at 2022-06-14 08:30:42.528854
# Unit test for method parse of class Parser
def test_Parser_parse():
    args = Parser().parse(['thefuck', 'echo', 'hello',
                           ARGUMENT_PLACEHOLDER, '--', '--version'])
    assert args.command == 'echo hello'
    assert args.version == True
    assert args.enabled_experimental_instant_mode == False
    assert args.alias == None
    assert args.debug == False
    assert args.help == False
    assert args.repeat == False
    assert args.yes == False

    args = Parser().parse(['thefuck', 'echo', 'hello',
                           ARGUMENT_PLACEHOLDER, '-a', 'tf'])
    assert args.command == 'echo hello'
    assert args.alias == 'tf'


# Generated at 2022-06-14 08:30:48.709288
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser.parse(['-v'])
    assert parser.parse(['-a'])
    assert parser.parse(['-l'])
    assert parser.parse(['--enable-experimental-instant-mode'])
    assert parser.parse(['-h'])
    assert parser.parse(['-y'])
    assert parser.parse(['-r'])
