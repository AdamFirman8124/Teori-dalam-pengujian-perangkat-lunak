

# Generated at 2022-06-14 08:20:52.663580
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:20:55.522455
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    assert parser.print_help() == parser._parser.print_help(sys.stderr)


# Generated at 2022-06-14 08:21:05.725282
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(["thefuck", "git br -v"]) == parser._parser.parse_args(["git", "br", "-v"])
    assert parser.parse(["thefuck", "git br -v", "--"]) == parser._parser.parse_args(["--", "git", "br", "-v"])
    assert parser.parse(["thefuck", "--", "--help"]) == parser._parser.parse_args(["--", "--help"])
    assert parser.parse(["thefuck", "git br -v", ARGUMENT_PLACEHOLDER, "--placeholderargs"]) == parser._parser.parse_args(["--placeholderargs", "git", "br", "-v"])

# Generated at 2022-06-14 08:21:06.983371
# Unit test for constructor of class Parser
def test_Parser():
    Parser()

# Generated at 2022-06-14 08:21:19.191845
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser._prepare_arguments(['-v', '-h', '-a', 'fuck'])
    assert args == ['-v', '-h', '-a', 'fuck']
    args = parser._prepare_arguments(['-v', '-h', 'fuck', ARGUMENT_PLACEHOLDER, '-a', 'fuck'])
    assert args == ['-a', 'fuck', '--','-v', '-h', 'fuck']
    args = parser._prepare_arguments(['fuck', ARGUMENT_PLACEHOLDER, '-a', 'fuck'])
    assert args == ['-a', 'fuck', '--', 'fuck']

# Generated at 2022-06-14 08:21:31.741541
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from io import StringIO
    from .const import USAGE
    
    # Ensure the expect usage is correct
    assert USAGE == "usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-d] [--force-command FORCE_COMMAND] [-y] [-r] [command [command ...]]"
    
    # Ensure the print_usage output is correct
    #
    # Create a StringIO object to capture the stdout
    capturedOutput = StringIO()
    sys.stdout = capturedOutput

    parser = Parser()
    parser.print_usage()
    sys.stdout = sys.__stdout__
    
    assert capturedOutput.getvalue() == USAGE + "\n"
    

# Generated at 2022-06-14 08:21:35.445465
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    #A very simple test.
    assert parser.parse(argv=['thefuck', 'ls', '-l']) == parser._parser.parse_args(['ls', '-l'])

# Generated at 2022-06-14 08:21:45.495583
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    p.parse(['thefuck', 'echo', 'Fuck'])
    p.parse(['thefuck', '-a'])
    p.parse(['thefuck', '--shell-logger'])
    p.parse(['thefuck', '--help'])
    p.parse(['thefuck', '--yes'])
    p.parse(['thefuck', '--repeat'])
    p.parse(['thefuck', '--debug'])
    p.parse(['thefuck', '--force-command'])



# Generated at 2022-06-14 08:21:48.596924
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    parser.parse(['thefuck', '--alias'])
    parser.parse(['thefuck', '--no-alias'])

# Generated at 2022-06-14 08:21:53.625345
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from tests.output_tester import OutputTester
    parser = Parser()
    tester = OutputTester(parser.print_usage)
    tester.assertIn('[options]')
    tester.assertIn('[command]')


# Generated at 2022-06-14 08:21:59.726070
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    help_argparser = ArgumentParser(add_help=False)
    assert parser._parser.format_help() == help_argparser.format_help()


# Generated at 2022-06-14 08:22:02.857384
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['thefuck', '--alias', 'fuck']) == \
        parser.parse(['thefuck', '-a', 'fuck'])

# Generated at 2022-06-14 08:22:12.974595
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    from StringIO import StringIO
    orig = sys.stderr
    sys.stderr = StringIO()
    parser.print_usage()
    result = sys.stderr.getvalue()
    sys.stderr.close()
    sys.stderr = orig
    assert result == "usage: thefuck [-h] [-v] [-a [custom-alias-name]]\n            [-l SHELL_LOGGER]\n            [--enable-experimental-instant-mode]\n            [-d] [--force-command COMMAND] [--]\n            [command [command ...]]\n"


# Generated at 2022-06-14 08:22:21.737508
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    try:
        stdout = sys.stdout
        sys.stdout = StringIO()
        parser.print_usage()
        assert sys.stdout.getvalue() == "usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l shell-logger] [--enable-experimental-instant-mode] [-y | -r] [-d] [--force-command force-command] [--] [command [command ...]]\n"
    finally:
        sys.stdout = stdout



# Generated at 2022-06-14 08:22:32.953834
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from io import BytesIO
    import sys
    from thefuck.parser import Parser
    parser = Parser()
    orig_stderr = sys.stderr
    sys.stderr = BytesIO()
    parser.print_usage()
    orig_stderr.write(sys.stderr.getvalue())

# Generated at 2022-06-14 08:22:36.151865
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    parser._parser = ArgumentParser(prog='thefuck', add_help=False)
    parser._add_arguments()
    args = parser.parse(['-l'])
    assert args.shell_logger
    assert args.command == []

# Generated at 2022-06-14 08:22:38.686008
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    assert parser.parse(['-h'])


# Generated at 2022-06-14 08:22:40.348420
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser


# Generated at 2022-06-14 08:22:46.517198
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    expected = Namespace(alias=get_alias(), command=['git', 'h'], debug=None,
                         enable_experimental_instant_mode=False,
                         force_command=None, help=None,
                         repeat=None, shell_logger=None, version=False,
                         yes=False)
    result = parser.parse(['-l', '--debug', '--alias', 'fuck', 'git', 'h'])
    assert result == expected



# Generated at 2022-06-14 08:22:59.428611
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    argv = ['thefuck', 'ls', ARGUMENT_PLACEHOLDER, '-a']
    args = parser.parse(argv)
    assert args.alias == get_alias()
    assert args.command == ['ls']
    argv = ['thefuck', 'ls', '-a', ARGUMENT_PLACEHOLDER]
    args = parser.parse(argv)
    assert args.command == ['ls', '-a']
    argv = ['thefuck', '--alias']
    args = parser.parse(argv)
    assert args.alias == get_alias()
    argv = ['thefuck', '-l', '/tmp/error.log']
    args = parser.parse(argv)

# Generated at 2022-06-14 08:23:04.402217
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser()

# Unit test to check if command of class Parser is displayed

# Generated at 2022-06-14 08:23:08.262093
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from .command import parser
    from .test_utils import capture_stderr
    with capture_stderr() as stderr:
        parser.print_usage()
    assert stderr.getvalue() == ''


# Generated at 2022-06-14 08:23:10.445319
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert repr(parser) == '<Parser>'


# Generated at 2022-06-14 08:23:20.745541
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    # Pass the arguments of the command that should be fixed
    # argv = ['fuck', 'wrong_command', '--arg1', 'value', '--arg2', 'value']
    argv = ['fuck', 'wrong_command', '--arg1', 'value', '--arg2', 'value', 
        '-y', '-h']
    result = parser.prepare_arguments(argv)
    assert result == ['wrong_command', '--arg1', 'value', '--arg2', 'value', 
        '-y', '-h', '--']
    argv = ["fuck"]
    result = parser.prepare_arguments(argv)
    assert result == ['--']

    # Call method parse after run method prepare_arguments
    result = parser.parse(argv)

# Generated at 2022-06-14 08:23:23.861546
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    sys.stderr = open('output.txt', 'w')
    parser = Parser()
    parser.print_help()
    sys.stderr.close()


# Generated at 2022-06-14 08:23:34.263838
# Unit test for method parse of class Parser
def test_Parser_parse():
    # Test the placeholder 'fuck'
    parser = Parser()
    assert parser.parse(['fuck', '-v']) == parser._parser.parse_args(['-v'])
    assert parser.parse(['fuck', '-h']) == parser._parser.parse_args(['-h'])
    assert parser.parse(['fuck', '-a']) == parser._parser.parse_args(['-a'])
    assert parser.parse(['fuck', '-a', 'alias']) == parser._parser.parse_args(['-a', 'alias'])
    assert parser.parse(['fuck', '-d']) == parser._parser.parse_args(['-d'])
    assert parser.parse(['fuck', '-y']) == parser._parser.parse_args(['-y'])
    assert parser

# Generated at 2022-06-14 08:23:45.089518
# Unit test for method parse of class Parser
def test_Parser_parse():
    """Test for method parse of class Parser"""
    parser = Parser()
    cmd = ['/usr/bin/fuck', 'command', 'hello', 'world', ARGUMENT_PLACEHOLDER, '-d', '-y', '--debug', '--yes', 'arg1', 'arg2']
    args = parser.parse(cmd)
    assert args.command == ['hello', 'world']
    assert args.debug == True
    assert args.yes == True
    assert args.repeat == False
    assert args.alias == False
    assert args.version == False
    assert args.help == False
    assert args.shell_logger == False
    assert args.enable_experimental_instant_mode == False
    assert args.force_command == False

# Generated at 2022-06-14 08:23:53.377317
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    import io
    import sys
    # This will redirect anything printed in the method print_help() to our
    # own stream
    saved_stdout = sys.stdout
    try:
        out = io.StringIO()
        sys.stdout = out
        parser.print_help()
        # sys.stdout.getvalue() will get the value written in our buffer (out)
        output = sys.stdout.getvalue().strip()
    finally:
        sys.stdout = saved_stdout

    assert output


# Generated at 2022-06-14 08:23:58.679198
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()

    saved_std_err = sys.stderr
    sys.stderr = io.StringIO()
    parser.print_usage()
    output = sys.stderr.getvalue()
    sys.stderr = saved_std_err

    assert output.find('usage: thefuck') == 0


# Generated at 2022-06-14 08:24:00.233603
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    assert Parser().print_help() == None

parser = Parser()

# Generated at 2022-06-14 08:24:21.019412
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()

# Generated at 2022-06-14 08:24:24.815104
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    """
    Method test_Parse_print_usage of class Parser.
    """
    parser = Parser()
    try:
        parser.print_usage()
    except:
        assert True


# Generated at 2022-06-14 08:24:27.834618
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    argv = ['parsertest']
    p = Parser()
    p.print_usage()
    assert True


# Generated at 2022-06-14 08:24:38.654696
# Unit test for method parse of class Parser
def test_Parser_parse():
    argument_parser = Parser()
    argument_parser_1 = Parser()
    argument_parser_2 = Parser()
    argument_parser_3 = Parser()
    arguments = argument_parser.parse(['thefuck', '--debug',
                                       'command', '--not-a-fuck-argument'])
    assert arguments.debug
    assert arguments.command == ['command', '--not-a-fuck-argument']
    assert not arguments.shell_logger
    assert not arguments.force_command
    assert not arguments.repeat
    assert not arguments.yes
    assert not arguments.alias
    assert not arguments.version

# Generated at 2022-06-14 08:24:41.517528
# Unit test for constructor of class Parser
def test_Parser():
    # gvim(settings)
    parser = Parser()
    assert parser._parser._prog == 'thefuck'


# Generated at 2022-06-14 08:24:43.822629
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    print(parser.parse(['thefuck', '-v']))

# Generated at 2022-06-14 08:24:52.914468
# Unit test for method parse of class Parser
def test_Parser_parse():
    # when
    output = Parser().parse('thefuck'.split())

    # then
    assert vars(output) == {
        'command': [],
        'alias': 'fuck',
        'debug': None,
        'enable_experimental_instant_mode': None,
        'force_command': None,
        'help': None,
        'repeat': None,
        'shell_logger': None,
        'version': None,
        'yes': None}


# Generated at 2022-06-14 08:24:54.595751
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    assert parser.print_usage() == ''

# Generated at 2022-06-14 08:25:06.321387
# Unit test for method parse of class Parser
def test_Parser_parse():
    p = Parser()
    assert p.parse(['']) == Namespace(debug=False,
                                      repeat=False,
                                      yes=False,
                                      force_command=None,
                                      help=False,
                                      shell_logger=None,
                                      alias=None,
                                      version=False,
                                      command=[])
    assert p.parse(['--debug']) == Namespace(debug=True,
                                             repeat=False,
                                             yes=False,
                                             force_command=None,
                                             help=False,
                                             shell_logger=None,
                                             alias=None,
                                             version=False,
                                             command=[])

# Generated at 2022-06-14 08:25:07.431896
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:25:26.200442
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    sys.argv = ["thefuck", "apt-get", "clean"]
    parser = Parser()
    fp = io.StringIO()
    with redirect_stdout(fp):
        parser.print_usage()
    output = fp.getvalue().strip()
    assert output == "usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-d] [--force-command FORCE_COMMAND] [-y | -r] [command [command ...]]"


# Generated at 2022-06-14 08:25:29.450150
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser.prog == 'thefuck'
    assert parser._parser.description == 'The Fuck - a magnificent app which corrects your previous console command.'
    assert parser._parser.formatter_class.__name__ == 'HelpFormatter'
    assert parser._parser.usage == '%(prog)s [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-h] [-d] [--force-command FORCE_COMMAND] command [command ...]'


# Generated at 2022-06-14 08:25:34.214946
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    assert Parser().print_usage() == \
        ArgumentParser(prog='thefuck', add_help=False).print_usage(sys.stderr)


# Generated at 2022-06-14 08:25:36.023723
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:25:41.439316
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from unittest import mock
    from io import StringIO

    parser = Parser()
    with mock.patch('sys.stderr', new_callable=StringIO, create=True) as mock_stderr:
        parser.print_help()

    assert "usage: thefuck [-h] [-v]" in mock_stderr.getvalue()

# Generated at 2022-06-14 08:25:45.481023
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    _stdout =  sys.stdout
    sys.stdout = _stderr = StringIO()
    parser.print_help()
    sys.stdout = _stdout
    assert "usage:" in _stderr.getvalue()

# Generated at 2022-06-14 08:25:58.620759
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    import io
    import sys
    import unittest

    class TestOutput(unittest.TestCase):
        def setUp(self):
            self.held, sys.stderr = sys.stderr, io.StringIO()

        def tearDown(self):
            sys.stderr = self.held

        def output(self):
            return sys.stderr.getvalue().strip()

    class Test(TestOutput):
        def test_Parser_print_help(self):
            parser = Parser()
            parser.print_help()

            returned = parser.output().split('\n')

# Generated at 2022-06-14 08:26:03.331809
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    import io
    import sys

    to_catch = io.StringIO()
    sys.stderr = to_catch

    parser = Parser()
    parser.print_help()

    sys.stderr = sys.__stderr__

    assert 'usage: thefuck' in to_catch.getvalue()

parser = Parser()

# Generated at 2022-06-14 08:26:05.120260
# Unit test for constructor of class Parser
def test_Parser():
    Parser()


# Generated at 2022-06-14 08:26:17.448907
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    # no placeholder
    assert parser.parse(['thefuck']) == parser._parser.parse_args([])
    assert parser.parse(['thefuck', '-v']) == parser._parser.parse_args(['-v'])
    assert parser.parse(['thefuck', '-a']) == parser._parser.parse_args(['-a'])
    assert parser.parse(['thefuck', 'echo']) == parser._parser.parse_args(['--', 'echo'])
    assert parser.parse(['thefuck', 'echo', '-h']) == parser._parser.parse_args(['--', 'echo', '-h'])

    # with placeholder

# Generated at 2022-06-14 08:26:35.242923
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:26:42.317527
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    parser._add_arguments = MagicMock()
    parser._parser = Mock()
    parser._parser.parse_args = MagicMock()
    parser.parse(['', '-v'])
    parser._add_arguments.assert_called_once_with()
    parser._parser.parse_args.assert_called_once_with(['-v'])



# Generated at 2022-06-14 08:26:45.630470
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    for arg in parser._parser._option_string_actions.values():
        assert arg.dest is not None or arg.option_strings == ['--help']

# Generated at 2022-06-14 08:26:53.560851
# Unit test for method parse of class Parser
def test_Parser_parse():
    p = Parser()
    parsed_args = p.parse(['thefuck'])
    assert parsed_args.alias is None
    assert parsed_args.verbose is None
    assert parsed_args.confirm is None
    assert parsed_args.shell_logger is None
    assert parsed_args.debug is None
    assert parsed_args.force_command is None
    assert parsed_args.command is None

    parsed_args = p.parse(['thefuck', 'ls'])
    assert parsed_args.alias is None
    assert parsed_args.verbose is None
    assert parsed_args.confirm is None
    assert parsed_args.shell_logger is None
    assert parsed_args.debug is None
    assert parsed_args.force_command is None
    assert parsed_args.command == []


# Generated at 2022-06-14 08:26:54.812982
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:27:06.203987
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    arg_parser = Parser()

# Generated at 2022-06-14 08:27:10.066533
# Unit test for method print_usage of class Parser

# Generated at 2022-06-14 08:27:10.794290
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser()

# Generated at 2022-06-14 08:27:12.972343
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()
    pass
    

# Generated at 2022-06-14 08:27:16.024768
# Unit test for constructor of class Parser
def test_Parser():
    p2 = Parser()
    #print('\nParsing arguments of class Parser')
    p2.parse(sys.argv)


# Generated at 2022-06-14 08:27:58.459398
# Unit test for method parse of class Parser
def test_Parser_parse():
    test = Parser()
    assert test.parse(['/usr/bin/python', '-d']) == (
    Namespace(command=[], debug=True, force_command=None, help=False, shell_logger=None, yes=False, alias=None))
    assert test.parse(['/usr/bin/python', 'fuck', '-d']) == (
    Namespace(command=['fuck'], debug=True, force_command=None, help=False, shell_logger=None, yes=False, alias=None))
    assert test.parse(['/usr/bin/python', 'fuck', '--']) == (
    Namespace(command=['fuck'], debug=False, force_command=None, help=False, shell_logger=None, yes=False, alias=None))

# Generated at 2022-06-14 08:28:09.458348
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from io import StringIO
    _stdout = sys.stdout
    sys.stdout = StringIO()
    help_print = Parser()
    help_print.print_usage()
    help_out = sys.stdout.getvalue()
    sys.stdout.close()
    sys.stdout = _stdout
    assert help_out == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-d] [--force-command FORCE_COMMAND] [-y | -r] [command [command ...]]\n'


# Generated at 2022-06-14 08:28:10.619152
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:28:12.550454
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    assert parser.print_usage() == None

# Generated at 2022-06-14 08:28:18.132058
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    args = parser._prepare_arguments(['--config'])
    parser.parse(args)
    s = cStringIO.StringIO()
    parser.print_help(file=s)
    assert 'thefuck' in s.getvalue()



# Generated at 2022-06-14 08:28:29.986374
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    p = Parser()
    output = p.help()

# Generated at 2022-06-14 08:28:41.311012
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert len(parser._parser._actions) == 13
    assert parser._parser._actions[0].option_strings == ['-v', '--version']

    for i in range(1, 11):
        if i == 1:
            assert parser._parser._actions[i].option_strings == ['-a', '--alias']
        elif i == 2:
            assert parser._parser._actions[i].option_strings == ['-h', '--help']
        else:
            assert parser._parser._actions[i].option_strings == ['-d', '--debug']


# Generated at 2022-06-14 08:28:43.485056
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    return p


# Generated at 2022-06-14 08:28:48.595370
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    old_stderr = sys.stderr
    sys.stderr = StringIO()
    parser.print_help()
    help_text = sys.stderr.getvalue()
    sys.stderr = old_stderr
    assert help_text != ""

# Generated at 2022-06-14 08:28:58.066427
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    import StringIO
    out = StringIO.StringIO()
    sys.stderr = out
    parser.print_usage()
    assert out.getvalue() == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-d] [--force-command FORCE_COMMAND] [-y] [-r] [--] [command [command ...]]\n'
    out.close()


# Generated at 2022-06-14 08:30:29.462819
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():    
    expected_output = "usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-d] [--force-command FORCE_COMMAND] [-y | -r] [--] [command [command ...]]\n"
    parser = Parser()
    parser.print_usage()
    assert expected_output == sys.stderr.getvalue()
    sys.stderr.truncate(0)
    sys.stderr.seek(0)


# Generated at 2022-06-14 08:30:38.723661
# Unit test for method parse of class Parser
def test_Parser_parse():
    result1 = Parser().parse(['thefuck', 'ls', '-a', '-l'])
    result2 = Parser().parse(['thefuck', '-h'])
    result3 = Parser().parse(['thefuck', '-l', 'logfile.txt', 'ls', '-a', '-l'])
    result4 = Parser().parse(['thefuck', '--shell-logger', 'logfile.txt', 'ls', '-a', '-l'])
    assert result1 == result2
    assert result3 == result4

# Generated at 2022-06-14 08:30:40.285654
# Unit test for constructor of class Parser
def test_Parser():
    Parser()


# Generated at 2022-06-14 08:30:50.862760
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert (parser.parse(['thefuck', 'git', 'branch', 'lalal']) ==
            parser._parser.parse_args(['git', 'branch', 'lalal']))
    assert (parser.parse(['thefuck', ARGUMENT_PLACEHOLDER, 'a', 'b', 'c',
                          'git', 'branch', 'lalal']) ==
            parser._parser.parse_args(['c', 'git', 'branch', 'lalal']))