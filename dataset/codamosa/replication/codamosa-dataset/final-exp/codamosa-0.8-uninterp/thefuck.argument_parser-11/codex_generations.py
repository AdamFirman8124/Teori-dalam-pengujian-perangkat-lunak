

# Generated at 2022-06-14 08:20:58.251938
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert len(parser._parser._actions) == 11
    assert len(parser._parser._actions[0].option_strings) == 2
    assert len(parser._parser._actions[1].option_strings) == 2
    assert len(parser._parser._actions[2].option_strings) == 1
    assert len(parser._parser._actions[3].option_strings) == 2
    assert len(parser._parser._actions[4].option_strings) == 1
    assert len(parser._parser._actions[5].option_strings) == 2


# Generated at 2022-06-14 08:20:59.872179
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    Parser().print_help()
    Parser().print_usage()

# Generated at 2022-06-14 08:21:02.496990
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse([''])
    assert parser.parse([''])
    assert parser.parse(['', '--force-command', 'echo 123'])
    assert parser.parse(['', 'echo', 'which'])

# Generated at 2022-06-14 08:21:15.723042
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()

# Generated at 2022-06-14 08:21:20.455414
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    stderr = sys.stderr
    sys.stderr = StringIO.StringIO()
    Parser().print_help()
    help_text = sys.stderr.getvalue()
    sys.stderr = stderr
    assert help_text.startswith("usage: thefuck")
    assert "show this help message and exit" in help_text

# Generated at 2022-06-14 08:21:22.696586
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
  parser = Parser()
  assert parser._parser.print_usage(sys.stderr) == None


# Generated at 2022-06-14 08:21:35.238229
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    """Unit test for method print_usage of class Parser"""
    f_sys_stderr_write = StringIO.StringIO()
    sys.stderr.write = f_sys_stderr_write
    parser = Parser()
    parser.print_usage()
    sys.stderr.write = sys.__stderr__

# Generated at 2022-06-14 08:21:37.709468
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    ret = Parser().print_help
    if(ret is not None):
        return True
    else:
        return False

# Generated at 2022-06-14 08:21:39.923410
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    print_help_output = Parser().print_help()
    assert print_help_output == None


# Generated at 2022-06-14 08:21:44.924967
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    # Setup
    from StringIO import StringIO
    import sys
    out = StringIO()
    sys.stderr = out

    # Test
    p = Parser()
    p.print_usage()

    # Verify
    assert out.getvalue() == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] [--enable-experimental-instant-mode] [-l SHELL_LOGGER] [-y | -r] [-d] [--force-command FORCE_COMMAND] [command [command ...]]\n'



# Generated at 2022-06-14 08:21:49.843870
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    arguments = Parser()
    arguments.print_usage()
test_Parser_print_usage()


# Generated at 2022-06-14 08:21:51.552298
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    parser.args = parser.parse(argv)



# Generated at 2022-06-14 08:22:04.705490
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    old_stderr = sys.stderr
    sys.stderr = StringIO()

    from .const import VERSION
    from thefuck.rules.git_add_missing_comma import match, get_new_command
    from thefuck.rules.git_add_missing_comma import get_new_command
    from thefuck.rules.git_add_missing_comma import match

    parser = Parser()
    parser.print_help()


# Generated at 2022-06-14 08:22:09.513736
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    # Parser has an attribute called prog
    assert parser._parser.prog
    # Parser has an attribute called add_help
    assert parser._parser.add_help
    

# Generated at 2022-06-14 08:22:16.547675
# Unit test for method parse of class Parser
def test_Parser_parse():
    # Parser_parse() should return None if no arguments are passed to it
    assert Parser().parse(['thefuck']) == None
    assert Parser().parse([]) == None
    # Parser_parse() should return an argparse.Namespace object if arguments are passed to it 
    assert isinstance(Parser().parse(['thefuck', 'echo']),argparse.Namespace) == True

# Generated at 2022-06-14 08:22:20.504748
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    import tempfile

    parser = Parser()
    parser.print_help()
    parser.print_usage()

    f = tempfile.NamedTemporaryFile()
    parser.parse([f.name, '--debug'])

# Generated at 2022-06-14 08:22:22.194973
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()

# Generated at 2022-06-14 08:22:23.704680
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser
    assert parser._parser


# Generated at 2022-06-14 08:22:24.750344
# Unit test for constructor of class Parser
def test_Parser():
    a = Parser()
    assert a._parser

# Generated at 2022-06-14 08:22:30.884265
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    argv = ['-y', 'ls', '-la', ARGUMENT_PLACEHOLDER, 'error']
    parser = Parser()
    parser.parse(argv)
    assert parser.print_usage() == parser._parser.print_usage(sys.stderr)


# Generated at 2022-06-14 08:22:46.345451
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from .const import VERSION
    from .utils import which
    from .utils import get_alias

    # Which programs are available
    is_fortune_available = which('fortune')
    is_sh_available = which('sh')

    real_argv = sys.argv
    real_which = which
    real_get_alias = get_alias

    output = StringIO()
    sys.stderr = output

# Generated at 2022-06-14 08:22:48.165816
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:22:49.985771
# Unit test for constructor of class Parser
def test_Parser():
    parser=Parser()
    assert parser._parser


# Generated at 2022-06-14 08:23:00.614015
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()

    # Test for function parse for the case that there is no placeholder
    arguments = parser.parse(['thefuck'])
    assert arguments.version == False
    assert arguments.alias == None
    assert arguments.help == False
    assert arguments.debug == False
    assert arguments.force_command == None
    assert arguments.command == ['thefuck']

    # Test for function parse for the case that there is placeholder
    arguments = parser.parse(['thefuck', '--help', ARGUMENT_PLACEHOLDER])
    assert arguments.version == False
    assert arguments.alias == None
    assert arguments.help == True
    assert arguments.debug == False
    assert arguments.force_command == None
    assert arguments.command == ['thefuck', '--help']

# Generated at 2022-06-14 08:23:03.095080
# Unit test for constructor of class Parser
def test_Parser():
    if __name__ == '__main__':
        Parser()
        print("It works!")


# Generated at 2022-06-14 08:23:05.652940
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    assert p
    assert isinstance(p, Parser)


# Generated at 2022-06-14 08:23:08.596608
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    command = ['thefuck', '--version']
    parser = Parser()
    parser.parse(command)
    return parser.print_usage()


# Generated at 2022-06-14 08:23:11.556772
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from thefuck import main
    parser = Parser()
    parser.print_help()
    #assert main.test_print_help() == parser.print_help()



# Generated at 2022-06-14 08:23:12.886839
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    assert parser.print_help() == None

# Generated at 2022-06-14 08:23:17.107314
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    # Test for print usage
    parser = Parser()
    sys.stderr = open('/dev/null', 'w')
    parser.print_usage()
    sys.stderr.close()


# Generated at 2022-06-14 08:23:33.742027
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['./thefuck', 'git', 'branch']) == parser._parser.parse_args(['git', 'branch'])
    assert parser.parse(['./thefuck', 'git branch']) == parser._parser.parse_args(['git branch'])
    assert parser.parse(['./thefuck', 'git branch', '-v']) == parser._parser.parse_args(['--', 'git branch', '-v'])
    assert parser.parse(['./thefuck', '--yeah', 'git branch']) == parser._parser.parse_args(['--yeah', 'git branch'])

# Generated at 2022-06-14 08:23:45.484591
# Unit test for method parse of class Parser
def test_Parser_parse():
    class FakeArgumentParser(object):
        def __init__(self):
            self.args = None
        def parse_args(self, args):
            self.args = args
            return args

    parser = Parser()
    parser._parser = FakeArgumentParser()
    args = parser.parse(['thefuck', 'ls', 'asd', ARGUMENT_PLACEHOLDER, '-l', '--help'])
    assert(args == ['ls', 'asd', '-l', '--help'])
    assert(parser._parser.args == ['-l', '--help', '--', 'ls', 'asd'])

    args = parser.parse(['thefuck', 'ls', 'asd', ARGUMENT_PLACEHOLDER])
    assert(args == ['ls', 'asd'])

# Generated at 2022-06-14 08:23:47.317038
# Unit test for constructor of class Parser
def test_Parser():
     parser = Parser()
     print(parser)
# test_Parser()

# Generated at 2022-06-14 08:23:56.041108
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    """Test the method print_usage of class Parser"""
    import sys
    import io

    old_stderr = sys.stderr
    result = io.StringIO()
    sys.stderr = result

    parser = Parser()
    parser.print_usage()

    sys.stderr = old_stderr
    output = result.getvalue()

    assert output=="""usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER]
                     [--enable-experimental-instant-mode] [-d] [-y] [-r]
                     [--force-command FORCE_COMMAND]
                     [command [command ...]]"""


# Generated at 2022-06-14 08:23:57.182104
# Unit test for constructor of class Parser
def test_Parser():

    pr = Parser()



# Generated at 2022-06-14 08:23:58.733990
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser()._parser.prog == 'thefuck'



# Generated at 2022-06-14 08:24:06.673216
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    arguments = parser.parse(['thefuck',
                              'git',
                              'commit',
                              '-m',
                              'fix',
                              ARGUMENT_PLACEHOLDER,
                              '--debug'])
    assert arguments.debug
    assert len(arguments.command) is 6
    assert arguments.command[0] == 'git'
    assert arguments.command[5] == '--debug'


# Generated at 2022-06-14 08:24:08.483786
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    p = Parser()
    p.print_help()


# Generated at 2022-06-14 08:24:09.890345
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser
    assert parser.parse(['thefuck'])



# Generated at 2022-06-14 08:24:15.656298
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(['-h'])
    assert args.help
    args = parser.parse(['--help'])
    assert args.help
    args = parser.parse(['--help', '--version'])
    assert args.help
    assert args.version

# Generated at 2022-06-14 08:24:30.568168
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert str(parser).startswith('usage: ')


# Generated at 2022-06-14 08:24:34.523236
# Unit test for method parse of class Parser
def test_Parser_parse():
    import sys
    sys.argv = ["thefuck", "--version"]
    parser = Parser()
    args = parser.parse(sys.argv)
    assert args.version == True


# Generated at 2022-06-14 08:24:36.313242
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()
    assert True


# Generated at 2022-06-14 08:24:44.445168
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._add_arguments()
    assert parser._prepare_arguments(['fuck']) == ['fuck']
    assert parser._prepare_arguments(['fuck', 'fuck', 'fuck']) == ['fuck', 'fuck', 'fuck']
    assert parser.parse(['fuck']) is not None
    assert parser.print_usage() is not None
    assert parser.print_help() is not None

# Generated at 2022-06-14 08:24:52.138649
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    def test_help():
        parser = Parser()
        parser.print_help()
    try:
        sys.stderr = StringIO()
        test_help()
    except SystemExit:
        help = sys.stderr.getvalue()
    assert 'Usage: thefuck' in help
    assert '--help' in help
    assert '--version' in help
    assert '[custom-alias-name]' in help

# Generated at 2022-06-14 08:24:53.528133
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    p = Parser()
    p.print_help()

# Generated at 2022-06-14 08:25:02.015156
# Unit test for method parse of class Parser
def test_Parser_parse():
    """Unit test for method parse of class Parser."""
    parser = Parser()
    argv = ['thefuck', 'vim', '-h']
    assert parser.parse(argv) == parser._parser.parse_args(argv[1:])
    argv = ['thefuck', 'vim', ARGUMENT_PLACEHOLDER, '-d']
    assert parser.parse(argv) == parser._parser.parse_args(
        ['vim', '-d', '--'])

# Generated at 2022-06-14 08:25:08.714880
# Unit test for method parse of class Parser
def test_Parser_parse():
    """ Test method parse of class Parser."""
    test_list = ['--alias', 'fuck', '-v', '-a', 'fuck', '-h', '-d', 
    '-l', 'fuck.log', '-y', 'fuck ls', '-r', 'fuck ls', 'fuck', 'fuck ls']
    ans = ['-v', '-h', '-d', '-y', '--', 'fuck', 'fuck']
    for x in test_list:
        argv = ['thefuck'] + x.split()
        parser = Parser()
        print(ans)
        assert(str(parser.parse(argv)) == ans)

# Generated at 2022-06-14 08:25:12.035866
# Unit test for constructor of class Parser
def test_Parser():
    from .const import ARGUMENT_PLACEHOLDER
    from .utils import get_alias
    assert ARGUMENT_PLACEHOLDER in str(Parser())
    assert get_alias() in str(Parser())

# Generated at 2022-06-14 08:25:18.475212
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from .utils import get_script_path
    from .config import Config, load_config
    from .application import Application
    load_config(Config('/dev/null'))
    Application(Parser(), argv=[get_script_path()]).run()

if __name__ == '__main__':
    test_Parser_print_usage()

# Generated at 2022-06-14 08:25:58.355516
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    parsed_arguments = parser.parse(['', '--version'])
    assert parsed_arguments.version
    parsed_arguments = parser.parse(['', '-d', 'ls', '-lah'])
    assert parsed_arguments.debug
    assert parsed_arguments.command == ['ls', '-lah']
    parsed_arguments = parser.parse(['', '--force-command', 'ls', '-lah'])
    assert parsed_arguments.force_command == 'ls'
    assert parsed_arguments.command == ['-lah']
    parsed_arguments = parser.parse(['', '--force-command', 'ls'])
    assert parsed_arguments.force_command == 'ls'
    assert parsed_arguments.command == []

# Generated at 2022-06-14 08:26:06.892194
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    import sys
    import io
    from unittest.mock import patch

    parser = Parser()
    parser.parse(['fuck', 'ls', '-a'])
    with patch('sys.stdout', new=io.StringIO()) as fake_out:
        parser.print_usage()
        assert fake_out.getvalue() == 'usage: fuck [-h] [-v] [-a [custom-alias-name]] ' \
                                      '[-l SHELL_LOGGER] [--enable-experimental-instant-mode] ' \
                                      '-y | -r [-d] [--force-command FORCE_COMMAND] command ...\n'

# Generated at 2022-06-14 08:26:08.698925
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser != None


# Generated at 2022-06-14 08:26:10.520746
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    p=Parser()
    p.print_help()
    print('completed')

# Generated at 2022-06-14 08:26:19.362760
# Unit test for constructor of class Parser
def test_Parser():
    Parser().parse([ARGUMENT_PLACEHOLDER, 'ls', '-a'])
    Parser().parse([ARGUMENT_PLACEHOLDER, 'ls', '-a', '--', '-l'])
    Parser().parse([ARGUMENT_PLACEHOLDER, 'ls', '-a', '-l'])
    Parser().parse(['ls', '-a', '--', '-l'])
    Parser().parse(['ls', '-a', ARGUMENT_PLACEHOLDER, '-l'])
    Parser().parse(['ls', '-a', ARGUMENT_PLACEHOLDER])
    Parser().parse(['ls', '-a'])
    Parser().parse([ARGUMENT_PLACEHOLDER])


# Generated at 2022-06-14 08:26:25.615498
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from io import StringIO
    from .parser import Parser
    old_stderr = sys.stderr
    sys.stderr = try_stderr = StringIO()
    Parser().print_help()
    sys.stderr = old_stderr
    assert try_stderr.getvalue()



# Generated at 2022-06-14 08:26:36.592869
# Unit test for method parse of class Parser
def test_Parser_parse():
    p = Parser()
    assert p.parse(['/bin/thefuck']) == p._parser.parse_args([])
    assert p.parse(['/bin/thefuck', '-y']) == p._parser.parse_args(['-y'])
    assert p.parse(['/bin/thefuck', 'ls -la']) == p._parser.parse_args(['--', 'ls -la'])
    assert p.parse(['/bin/thefuck', ARGUMENT_PLACEHOLDER, 'ls', '-la']) == p._parser.parse_args(['ls', '-la'])
    assert p.parse(['/bin/thefuck', ARGUMENT_PLACEHOLDER, 'ls', '-la', '--', '-x']) == p._parser.parse_

# Generated at 2022-06-14 08:26:45.241141
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    """
    Unit test for method print_help of class Parser.
    """
    import io
    from unittest.mock import patch
    from thefuck.parser import Parser
    with patch('sys.stderr', new_callable=io.StringIO) as mock_err:
        Parser().print_help()
        assert mock_err.getvalue().startswith('usage: thefuck')


# Generated at 2022-06-14 08:26:52.150346
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()
    parser.parse(['the_fuck', 'haha', '-v'])
    parser.print_usage()
    parser.parse(['the_fuck', '-a'])
    parser.print_usage()
    parser.parse(['the_fuck', '-ha'])
    parser.parse(['the_fuck', '-ha', 'no_need'])
    parser.parse(['the_fuck', '-y'])
    parser.parse(['the_fuck', '-r'])


# Generated at 2022-06-14 08:27:05.751765
# Unit test for method parse of class Parser
def test_Parser_parse():
    sys.argv = ['thefuck']
    parser = Parser()
    parser.parse(['thefuck', 'ls', '-la'])
    assert parser.parse(['thefuck', 'ls', '-la']) == parser._parser.parse_args(['--', 'ls', '-la'])
    assert parser.parse(['thefuck', 'ls', '-la', ';', 'cd', '~']) == parser._parser.parse_args(['--', 'cd', '~'])
    assert parser.parse(['thefuck', '--enable-experimental-instant-mode', 'ls', '-la']) == parser._parser.parse_args(['--enable-experimental-instant-mode', '--', 'ls', '-la'])

# Generated at 2022-06-14 08:27:56.474063
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    p = Parser()
    assert(p.print_help() == None)

# Generated at 2022-06-14 08:28:02.313034
# Unit test for method parse of class Parser
def test_Parser_parse():
    argv = ['thefuck', '-d', 'command', '-x', ARGUMENT_PLACEHOLDER, '-y']
    result_argv = ['command', '-x', '-y', '--']
    parser = Parser()
    assert result_argv == parser._prepare_arguments(argv)


# Generated at 2022-06-14 08:28:13.309542
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['thefuck', 'git']).command == ['git']
    assert parser.parse(['thefuck', '-y', 'git']).command == ['git']
    assert parser.parse(['thefuck', '-v']).version
    assert parser.parse(['thefuck', '-a']).alias == get_alias()
    assert parser.parse(['thefuck', '-h']).help
    assert parser.parse(['thefuck', '--alias', 'f']).alias == 'f'
    assert parser.parse(['thefuck', '--alias', '%']).alias == '%'

# Generated at 2022-06-14 08:28:14.742211
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    # test explicitly
    Parser().print_usage()

# Generated at 2022-06-14 08:28:15.771637
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()

# Generated at 2022-06-14 08:28:25.702022
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    import StringIO
    saved_stdout = sys.stdout
    try:
        out = StringIO.StringIO()
        sys.stdout = out
        parser.print_usage()
        output = out.getvalue().strip()
        assert output == "usage: thefuck [-h] [-v] [-a [custom-alias-name]]" +\
        " [-y] [-r] [-l SHELL_LOGGER] [-d] [--enable-experimental-instant-mode]" +\
        " [command [command ...]]"
    finally:
        sys.stdout = saved_stdout


# Generated at 2022-06-14 08:28:27.879055
# Unit test for constructor of class Parser
def test_Parser():
    assert isinstance(Parser(), Parser)


# Generated at 2022-06-14 08:28:33.346390
# Unit test for method parse of class Parser
def test_Parser_parse():
    """
    :return: None
    """

    parser = Parser()
    parser.parse(['thefuck', 'ls', '~', ARGUMENT_PLACEHOLDER, '-y', '-d'])
    parser.parse(['thefuck', 'ls', '~'])
    parser.parse(['thefuck', 'ls', '~', ARGUMENT_PLACEHOLDER, '--'] +
                 ['ls', '-la', '-y'])



# Generated at 2022-06-14 08:28:34.908528
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    assert parser.print_help() == parser._parser.print_help(sys.stderr)


# Generated at 2022-06-14 08:28:35.978364
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:30:21.331889
# Unit test for constructor of class Parser
def test_Parser():
    with pytest.raises(TypeError):
        Parser(1)
    with pytest.raises(TypeError):
        Parser(None)


# Generated at 2022-06-14 08:30:27.544713
# Unit test for method parse of class Parser
def test_Parser_parse():
	parser = Parser()
	output = parser.parse(['/bin/ls', '-l'])
	print(output)
	output = parser.parse(['/bin/ls', '-l', ARGUMENT_PLACEHOLDER, '---yes', '--debug'])
	print(output)

# Generated at 2022-06-14 08:30:29.394455
# Unit test for constructor of class Parser
def test_Parser():
    with raises(ValueError):
        parser = Parser(123)


# Generated at 2022-06-14 08:30:31.600662
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert isinstance(parser, Parser)



# Generated at 2022-06-14 08:30:33.205002
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:30:36.552201
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    """
    Unit test for method print_help of class Parser
    """
    parser = Parser()
    parser.print_usage()
    parser.print_help()

# Generated at 2022-06-14 08:30:49.698001
# Unit test for method parse of class Parser
def test_Parser_parse():

    parser = Parser()
    args = parser.parse(['/home/user/program', 'command', ARGUMENT_PLACEHOLDER, '-d'])
    assert args.command == ['command']
    assert args.debug == True

    args = parser.parse(['/home/user/program', '?', '-l', 'haha'])
    assert args.command == ['?']
    assert args.shell_logger == 'haha'

    args = parser.parse(['/home/user/program', '--', 'command'])
    assert args.command == ['command']

    args = parser.parse(['/home/user/program', 'command', 'arg1', 'arg2'])
    assert args.command == ['command', 'arg1', 'arg2']
