

# Generated at 2022-06-14 08:20:54.118195
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    print(parser.parse(['-l','shell-logger','--','ls','|','fuck','grep']))


# Generated at 2022-06-14 08:21:05.084331
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    result = parser.parse(['thefuck', 'fuck', '-y'])
    assert result.command == ['fuck']
    assert result.yes

    result = parser.parse(['thefuck', 'fuck', '-a'])
    assert result.command == ['fuck']
    assert result.alias
    assert result.alias == get_alias()

    result = parser.parse(['thefuck', 'fuck', '-a', 'alias'])
    assert result.command == ['fuck']
    assert result.alias
    assert result.alias == 'alias'

    result = parser.parse(['thefuck', 'fuck', '--', '-a'])
    assert result.command == ['fuck', '-a']
    assert not result.alias


# Generated at 2022-06-14 08:21:18.081889
# Unit test for constructor of class Parser
def test_Parser():
    parser=Parser()
    assert parser._parser.prog == 'thefuck'
    assert parser._parser._actions[0].dest == 'version'
    assert parser._parser._actions[1].dest == 'alias'
    assert parser._parser._actions[2].dest == 'shell_logger'
    assert parser._parser._actions[3].dest == 'enable_experimental_instant_mode'
    assert parser._parser._actions[4].dest == 'help'
    assert parser._parser._actions[5].dest == 'yes'
    assert parser._parser._actions[6].dest == 'repeat'
    assert parser._parser._actions[7].dest == 'debug'
    assert parser._parser._actions[8].dest == 'force_command'
    assert parser._parser._actions[9].dest == 'command'


# Generated at 2022-06-14 08:21:29.414165
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    import sys
    from io import StringIO
    out = StringIO()
    sys.stderr = out
    parser.print_usage()
    assert out.getvalue() == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]]\n' \
                            '[-l SHELL_LOGGER] [--enable-experimental-instant-mode]\n' \
                            '[-d] [--force-command FORCE_COMMAND]\n' \
                            '[-y | -r] [command [command ...]]\n'
    out.close()


# Generated at 2022-06-14 08:21:30.222659
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()

# Generated at 2022-06-14 08:21:38.588179
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    try:
        # Create a ArgumentParser object by specifying argument keywords
        arguments = Parser()
        def in_file():
            # Test if print_help() will print into stderr as expected
            out = sys.stderr.getvalue()
            assert len(out) > 0, 'No data was output!'
            assert len(out) < 122, 'Too much data was output!'

        # Create a file like object
        sys.stderr = io.StringIO()
        # call print_help
        arguments.print_help()
        # call in_file() to test if print_help() will print into stderr
        in_file()
    finally:
        sys.stderr.close()


# Generated at 2022-06-14 08:21:40.460714
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser.parse(['fuck'])

# Generated at 2022-06-14 08:21:53.918724
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    '''
    Unit test for method print_usage of class Parser
    '''
    from thefuck.rules.git_no_command import enabled, match, get_new_command
    from thefuck.shells import Bash, Zsh, Fish
    from thefuck.types import Command, CorrectedCommand
    from thefuck import settings
    from thefuck.utils import cache, do_log
    from thefuck.main import Fuck, Rule

    fuck = Fuck(Rule(
        enabled, match, get_new_command,
        settings, cache, do_log))
    Fuck.__init__ = lambda self, x: None
    bash = Bash(fuck, [])
    zsh = Zsh(fuck, [])
    fish = Fish(fuck, [])

    assert bash.script('cd /tmp') == 'cd /tmp'
    assert z

# Generated at 2022-06-14 08:22:06.582509
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    class StdOut(object):
        """Fake stdout for unit test."""
        def __init__(self):
            self.stdout = ''

        def write(self, stdout):
            self.stdout += stdout

        def __str__(self):
            return self.stdout

    help_descriptions = ['thefuck: error: unrecognized arguments:',
                         '-h, --help show this help message and exit',
                         '--version show program\'s version number and exit',
                         '-a, --alias [custom-alias-name] prints alias',
                         '-y, --yes, --yeah, --hard execute fixed',
                         '   command without confirmation',
                         '-r, --repeat repeat on failure',
                         '-d, --debug enable debug output',
                         'command command that should be fixed']
    std

# Generated at 2022-06-14 08:22:07.888270
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    Parser()


# Generated at 2022-06-14 08:22:18.845802
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    assert isinstance(Parser().print_help(), None)



# Generated at 2022-06-14 08:22:20.624591
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    p = Parser()
    p.print_usage()



# Generated at 2022-06-14 08:22:32.041798
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    import io
    import sys
    stdout = io.StringIO()
    with redirect_stdout(stdout):
        Parser().print_help()
    assert stdout.getvalue()
    assert stdout.getvalue().startswith(
        'usage: thefuck [-h] [-a [custom-alias-name]] [-l SHELL_LOGGER]\n')
    assert stdout.getvalue().endswith(
        'optional arguments:' +
        '\n  -h, --help            show this help message and exit\n' +
        '  -d, --debug           enable debug output\n'
        '  --force-command FORCE-COMMAND\n' +
        '                        \n' +
        '  command [command ...]\n' +
        '                        command that should be fixed\n')


# Generated at 2022-06-14 08:22:33.056019
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    Parser().print_usage()


# Generated at 2022-06-14 08:22:35.233783
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    """
    Test print_help method of class Parser
    """

    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:22:37.209592
# Unit test for constructor of class Parser
def test_Parser():
    arg_parser = Parser()
    assert arg_parser is not None

# Generated at 2022-06-14 08:22:39.115692
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    assert parser.print_usage() is None

# Generated at 2022-06-14 08:22:42.977229
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    p = Parser()
    import io
    import sys
    sys.stderr = io.StringIO()
    p.print_help()
    sys.stderr.seek(0)
    assert sys.stderr.read()

# Generated at 2022-06-14 08:22:56.465364
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    command = "command"
    args = parser.parse([command])
    assert args.command == [command]

    command = "command one two"
    args = parser.parse([command])
    assert args.command == [command]

    command = "command --argument one"
    placeholder = "--"
    args = parser.parse([command, placeholder])
    assert args.command == [command]

    command = "command --argument one"
    placeholder = "--"
    args = parser.parse([placeholder, command])
    assert args.command == [command]

    command = ""
    args = parser.parse([command])
    assert args.command == []

    args = parser.parse(["--version"])
    assert args.version == True

# Generated at 2022-06-14 08:22:59.994348
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    parsed = parser.parse(['thefuck', 'ls', '-l'])
    assert parsed.command == ['ls', '-l']



# Generated at 2022-06-14 08:23:20.604748
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    out, err = capsys.readouterr()
    parser.print_usage()
    assert err == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-d]\n'


# Generated at 2022-06-14 08:23:23.279955
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.parse(['fuck', '--version'])
    assert parser._parser.print_usage() == True


# Generated at 2022-06-14 08:23:24.956156
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser != None



# Generated at 2022-06-14 08:23:35.673275
# Unit test for method parse of class Parser
def test_Parser_parse():
    class Parser_test(Parser):
        def __init__(self):
            super(Parser_test, self).__init__()

        def _add_arguments(self):
            self._parser.add_argument("-v", help="version", action="store_true")
            self._parser.add_argument("-t", help="test", action="store_true")

        def _add_conflicting_arguments(self):
            pass
        
    parser = Parser_test()
    assert parser.parse(["", "-v"]).v == True
    assert parser.parse(["", "--version"]).v == True
    assert parser.parse(["", "-t"]).t == True
    assert parser.parse(["", "--test"]).t == True


# Generated at 2022-06-14 08:23:37.399724
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()
    

# Generated at 2022-06-14 08:23:50.971801
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    # Command without arguments
    assert parser.parse(['./bin/fuck']) == parser._parser.parse_args([])
    # Command with one argument
    assert parser.parse(['./bin/fuck', 'python']) == \
        parser._parser.parse_args(['--', 'python'])
    # Command with two arguments
    assert parser.parse(['./bin/fuck', 'python', '--version']) == \
        parser._parser.parse_args(['--', 'python', '--version'])
    # Command with one argument, that is an option
    assert parser.parse(['./bin/fuck', '--help']) == \
        parser._parser.parse_args(['--help'])
    # Command with two arguments, the first one is an option

# Generated at 2022-06-14 08:23:52.429366
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser is not None

# Generated at 2022-06-14 08:23:54.174457
# Unit test for constructor of class Parser
def test_Parser():
    assert isinstance(Parser(), Parser)



# Generated at 2022-06-14 08:23:55.646147
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    p = Parser()
    p.print_usage()


# Generated at 2022-06-14 08:24:00.774538
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(['fuck', '-d', 'git', 'log', ARGUMENT_PLACEHOLDER, '--pretty', 'sh'])
    assert(args.debug == True)
    assert(args.command == ['git', 'log', '--pretty', 'sh'])


# Generated at 2022-06-14 08:24:41.238874
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    pass

# Generated at 2022-06-14 08:24:54.511404
# Unit test for method parse of class Parser
def test_Parser_parse():
    argv = ['thefuck', '-yy', '--shell-logger', 'shell.log', '-l', 'bash', '-h', 'cd', ARGUMENT_PLACEHOLDER, '/home']
    parser = Parser()
    # test parse
    args = parser.parse(argv)
    assert args.yes == True
    assert args.shell_logger == 'shell.log'
    assert args.enable_experimental_instant_mode == False
    assert args.help == False
    assert args.debug == False
    assert args.command == ['/home']
    # test parse_args
    args = parser.parse_args(argv)
    assert args.yes == True
    assert args.shell_logger == 'shell.log'

# Generated at 2022-06-14 08:24:55.990500
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()

# Generated at 2022-06-14 08:24:57.596877
# Unit test for constructor of class Parser
def test_Parser():
    a = Parser()
    assert_type(a, Parser)


# Generated at 2022-06-14 08:24:59.700938
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:25:00.955068
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    Parser().print_usage()

# Generated at 2022-06-14 08:25:02.241240
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:25:14.414013
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser.prog == 'thefuck'
    assert parser._parser.add_help

    assert parser._parser._actions[0].option_strings == ['-v']
    assert parser._parser._actions[0].dest == 'version'
    assert parser._parser._actions[1].option_strings == ['-a']
    assert parser._parser._actions[1].dest == 'alias'
    assert parser._parser._actions[2].option_strings == ['-l']
    assert parser._parser._actions[2].dest == 'shell_logger'
    assert parser._parser._actions[3].option_strings == ['-h']
    assert parser._parser._actions[3].dest == 'help'
    assert parser._parser._actions[4].option_strings == ['-y']
    assert parser._parser._

# Generated at 2022-06-14 08:25:15.598797
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()


parser = Parser()

# Generated at 2022-06-14 08:25:16.458710
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser()


# Generated at 2022-06-14 08:26:01.763266
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser

# Generated at 2022-06-14 08:26:15.327063
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from io import StringIO
    from .utils import get_aliases

    stderr = sys.stderr
    sys.stderr = StringIO()

    parser = Parser()
    parser.parse(['-h'])

# Generated at 2022-06-14 08:26:28.716964
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(
        ['fuck', 'django-admin.py', 'migrate', '--all-apps',
         '--noinput', ARGUMENT_PLACEHOLDER, '--traceback', '--verbosity', '2'])\
        == Namespace(alias=None,
                     command=['django-admin.py', 'migrate', '--all-apps',
                              '--noinput', '--traceback', '--verbosity', '2'],
                     debug=False,
                     enable_experimental_instant_mode=False,
                     force_command=None,
                     help=False,
                     repeat=False,
                     shell_logger=None,
                     version=False,
                     yes=False)



# Generated at 2022-06-14 08:26:32.788309
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser_ = Parser()
    assert parser_._parser._actions[0].option_strings == ['-v', '--version']
    parser_._parser.print_usage(sys.stderr)


# Generated at 2022-06-14 08:26:45.472054
# Unit test for method parse of class Parser
def test_Parser_parse():
    assert Parser().parse(['/bin/ls', '-lah']) == (
        Parser()._parser.parse_args(['-lah']))
    assert Parser().parse(['/bin/ls', '-lah', ARGUMENT_PLACEHOLDER, '-v']) == (
        Parser()._parser.parse_args(['-lah', '--', '-v']))
    assert Parser().parse(['/bin/ls', '-lah', ARGUMENT_PLACEHOLDER]) == (
        Parser()._parser.parse_args(['-lah', '--']))
    assert Parser().parse(['/bin/ls', '-v']) == (
        Parser()._parser.parse_args(['-v']))

# Generated at 2022-06-14 08:26:53.505536
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser.parse(['thefuck', '-v']) == parser.parse(['thefuck', '--version'])
    assert parser.parse(['thefuck', '-a']) == parser.parse(['thefuck', '--alias'])
    assert parser.parse(['thefuck', '-l']) == parser.parse(['thefuck', '--shell-logger'])
    assert parser.parse(['thefuck', '-h']) == parser.parse(['thefuck', '--help'])
    assert parser.parse(['thefuck', '-y']) == parser.parse(['thefuck', '--yes'])
    assert parser.parse(['thefuck', '-r']) == parser.parse(['thefuck', '--repeat'])

# Generated at 2022-06-14 08:27:06.751444
# Unit test for constructor of class Parser

# Generated at 2022-06-14 08:27:08.628942
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:27:20.336616
# Unit test for constructor of class Parser
def test_Parser():
    import mock
    import argparse

    parser = Parser()

    assert parser._parser
    assert parser._parser.prog == "thefuck"
    assert parser._parser.add_help == False

    assert parser._parser.actions[0].option_strings == ['-v', '--version']
    assert parser._parser.actions[0].dest == "version"
    assert parser._parser.actions[0].nargs == 0
    assert parser._parser.actions[0].const == None
    assert parser._parser.actions[0].default == False
    assert parser._parser.actions[0].type == None
    assert parser._parser.actions[0].choices == None
    assert parser._parser.actions[0].required == False
    assert parser._parser.actions[0].help == "show program's version number and exit"
    assert parser._

# Generated at 2022-06-14 08:27:21.669315
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    assert "usage: thefuck" in Parser().print_help()

# Generated at 2022-06-14 08:29:03.036566
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser() is not None

# Generated at 2022-06-14 08:29:04.595717
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()


# Generated at 2022-06-14 08:29:06.050784
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:29:19.776016
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from io import StringIO
    from .application import Application

    out = StringIO()
    parser = Parser()
    Application(lambda: None, lambda: None, out=out).print_help(parser)

# Generated at 2022-06-14 08:29:32.360300
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['thefuck', 'echo', 'test']) == \
        parser.parse(['thefuck', 'echo', 'test', ARGUMENT_PLACEHOLDER])

    assert parser.parse(['thefuck', 'echo', 'test', '--command', 'echo']) == \
        parser.parse(['thefuck', 'echo', 'test', '--command', 'echo', ARGUMENT_PLACEHOLDER])

    assert parser.parse(['thefuck', 'echo', 'test', '--command', 'echo']) == \
        parser.parse(['thefuck', 'echo', 'test', ARGUMENT_PLACEHOLDER, '--command', 'echo'])



# Generated at 2022-06-14 08:29:34.662416
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    p = Parser()
    p.print_help()

# Generated at 2022-06-14 08:29:36.810086
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser

if __name__ == '__main__':
    test_Parser()

# Generated at 2022-06-14 08:29:38.462608
# Unit test for constructor of class Parser
def test_Parser():
    args= Parser()
    assert args


# Generated at 2022-06-14 08:29:41.647235
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    import sys
    sys.argv = ["thefuck", "--help"]
    p = Parser()
    p.print_usage()
    assert True

# Generated at 2022-06-14 08:29:49.265616
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    test_args = '-v -h -d'.split()
    test_parser = Parser()
    # Test with multiple arguments
    test_parser.print_help(test_args)
    # Test with one argument
    test_args = '-v'.split()
    test_parser.print_help(test_args)
    # Test with no arguments
    test_args = ['']
    test_parser.print_help(test_args)