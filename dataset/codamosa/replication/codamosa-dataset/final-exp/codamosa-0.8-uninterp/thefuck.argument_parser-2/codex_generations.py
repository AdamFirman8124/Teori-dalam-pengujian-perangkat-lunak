

# Generated at 2022-06-14 08:20:47.859955
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    return p

# Generated at 2022-06-14 08:20:59.581760
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    """Test method print_usage of class Parser"""
    # To test the method print_usage we need to check the output of the
    # method print_usage when called
    # For this we need to create a class instance and then call it's print_usage method
    parser = Parser()
    # We need to capture the standard output
    # By default standard output is the console(sys.stdout)
    # We can redirect it to some stream
    # Here we will use StringIO
    # StringIO is used to operate on string as a file
    # Here we will capture the output of print_usage method in the out
    from contextlib import contextmanager
    import sys
    from io import StringIO

    @contextmanager
    def captured_output():
        new_out, new_err = StringIO(), StringIO()
        old_out, old_err

# Generated at 2022-06-14 08:21:03.467500
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    error_msg = '--test_parser_method_print_help error'
    try:
        parser = Parser()
        parser.print_help()
        print('test_Parser_print_help passed')
    except:
        print(error_msg)


# Generated at 2022-06-14 08:21:16.685407
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    """
    Unit test for method print_help of class Parser.
    """
    # Following code is copied from https://stackoverflow.com/a/241015/8492355
    # and https://stackoverflow.com/a/4417822/8492355
    import StringIO
    out = StringIO.StringIO()
    sys.stdout.write = out.write  #redirect stdout to out
    Parser().print_help()
    assert isinstance(out.getvalue(), str)  #check if it is a string
    assert "Usage:" in out.getvalue()  #check it outputs usage
    assert "thefuck" in out.getvalue()  #check it outputs "thefuck"
    assert "--version" in out.getvalue()  #check it outputs --version

# Generated at 2022-06-14 08:21:21.392787
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(['thefuck', '-a'])
    assert args.alias == get_alias()
    args = parser.parse(['thefuck', '-l', 'helloworld'])
    assert args.shell_logger == 'helloworld'
    args = parser.parse(['thefuck', '-d'])
    assert args.debug


# Generated at 2022-06-14 08:21:22.850515
# Unit test for constructor of class Parser
def test_Parser():
    parser=Parser()
    # print(parser)



# Generated at 2022-06-14 08:21:35.306986
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    import sys
    import io
    import re
    result = io.StringIO()
    sys.stderr = result
    parser.print_help()
    actual = result.getvalue()

    assert re.search(r'usage: thefuck \[(.*)\] command', actual) is not None, \
        'Parser.print_help should contain usage'
    assert re.search(r'\[-h\]', actual) is not None, \
        'Parser.print_help should contain option [-h]'
    assert re.search(r'\[-v\]', actual) is not None, \
        'Parser.print_help should contain option [-v]'

# Generated at 2022-06-14 08:21:49.090115
# Unit test for method parse of class Parser
def test_Parser_parse():
    """Test method parse of class Parser
    """
    parser = Parser()
    arguments = parser.parse(['fuck'])
    assert not arguments.version
    assert not arguments.alias
    assert not arguments.debug
    assert not arguments.yes
    assert not arguments.repeat
    assert not arguments.help
    assert not arguments.shell_logger
    assert not arguments.command
    assert not arguments.force_command
    assert not arguments.enable_experimental_instant_mode

    arguments = parser.parse(['fuck', '-v'])
    assert arguments.version
    assert not arguments.alias
    assert not arguments.debug
    assert not arguments.yes
    assert not arguments.repeat
    assert not arguments.help
    assert not arguments.shell_logger
    assert not arguments.command
    assert not arguments.force_command
   

# Generated at 2022-06-14 08:21:51.291395
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert hasattr(parser, '_parser')

# Generated at 2022-06-14 08:22:03.924640
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    import unittest
    import io
    from .utils import get_alias
    from .parser import Parser

    class fakestd(object):

        def __init__(self):
            self.data = []

        def write(self, msg):
            self.data.append(msg)

        def flush(self):
            pass

    class TestParser(unittest.TestCase):

        def setUp(self):
            self.stderr = fakestd()
            self.stream = io.StringIO(newline='')
            self.parser = Parser()
           # sys.stderr = self.stream
            sys.stderr = self.stderr


# Generated at 2022-06-14 08:22:09.619203
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    help_message = parser.print_help()
    assert help_message is None

    help_message = parser.print_usage()
    assert help_message is None

# Generated at 2022-06-14 08:22:12.069225
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    my_parser = Parser()
    my_parser.print_help()

# Generated at 2022-06-14 08:22:17.355067
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    captured_output = StringIO()
    sys.stderr = captured_output
    parser.print_usage()
    sys.stderr = sys.__stderr__
    assert 'usage: thefuck' in captured_output.getvalue()


# Generated at 2022-06-14 08:22:26.119052
# Unit test for method parse of class Parser
def test_Parser_parse():
    print("running test for method parse of class Parser")
    parser = Parser()
    sys.argv = ['thefuck', '--force-command', 'pwd']
    assert parser.parse(sys.argv) == parser._parser.parse_args(['--force-command', 'pwd'])
    sys.argv = ['thefuck', '-l', '~/log']
    assert parser.parse(sys.argv) == parser._parser.parse_args(['-l', '~/log'])
    sys.argv = ['thefuck', 'echo', 'test', ARGUMENT_PLACEHOLDER, '-l', '~/log', '-v']

# Generated at 2022-06-14 08:22:29.409957
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    help = parser.print_help()
    assert isinstance(help, None)


# Generated at 2022-06-14 08:22:30.466145
# Unit test for constructor of class Parser
def test_Parser():
    version = Parser()

# Generated at 2022-06-14 08:22:31.442682
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser()


# Generated at 2022-06-14 08:22:35.635414
# Unit test for method parse of class Parser
def test_Parser_parse():
    argv = ['thefuck', 'git', 'push', 'origin', 'master', ':q']
    args = Parser().parse(argv)
    assert args.command == 'git push origin master :q'


# Generated at 2022-06-14 08:22:46.063015
# Unit test for method parse of class Parser
def test_Parser_parse():
    p = Parser()
    args = p.parse(['thefuck', '-y', '-h', '@'])
    assert args.yes
    assert args.help
    assert not args.debug
    assert not args.command

    args = p.parse(['thefuck', '-r', '-d', '@'])
    assert args.repeat
    assert args.debug
    assert not args.help
    assert not args.command

    args = p.parse(['thefuck', '-y', '-r', '-d'])
    assert not args.help
    assert not args.command
    assert not args.yes
    assert not args.repeat
    assert args.debug

    args = p.parse(['thefuck', '-y', '-r', '@', 'ls'])
    assert not args.help

# Generated at 2022-06-14 08:22:55.447934
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    s = StringIO()
    sys.stderr = s
    parser.print_usage()
    assert u'usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER]\n' in s.getvalue()
    assert u'[-y | -r] [-d] [--force-command FORCE_COMMAND] [--]\n' in s.getvalue()
    assert u'[command [command ...]]' in s.getvalue()


# Generated at 2022-06-14 08:23:07.259871
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    with patch('sys.stderr'):
        parser.print_usage()
        sys.stderr.write.assert_called_with(
            'usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER]\n'
            '[--enable-experimental-instant-mode] [-y|-r] [-d]\n'
            '[--force-command FORCE_COMMAND] [command [command ...]]\n')

# Generated at 2022-06-14 08:23:11.604935
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    stderr = StringIO()
    sys.stderr = stderr
    parser.print_usage()
    sys.stderr = sys.__stderr__
    assert 'usage' in stderr.getvalue()

# Generated at 2022-06-14 08:23:21.351144
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    with NamedTemporaryFile() as stdout:
        stdout.seek(0)
        stdout.close()
        with open(stdout.name, 'r') as fp:
            real_out = fp.read()

    with NamedTemporaryFile() as stderr:
        stderr.seek(0)
        stderr.close()
        with open(stderr.name, 'r') as fp:
            real_err = fp.read()

    stdout = sys.stdout
    stderr = sys.stderr
    sys.stdout = open(stdout.name, 'w')
    sys.stderr = open(stderr.name, 'w')
    parser = Parser()
    parser.print_usage()
    sys.stdout = stdout

# Generated at 2022-06-14 08:23:22.543725
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:23:26.217532
# Unit test for constructor of class Parser
def test_Parser():
    args = Parser().parse([None, '--alias', 'fuck', 'echo', 'foo'])
    assert args.alias == 'fuck'
    assert args.command == ['echo', 'foo']



# Generated at 2022-06-14 08:23:36.318872
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['fuck']) == parser._parser.parse_args([])
    assert parser.parse(['fuck', 'command']) == parser._parser.parse_args(['--', 'command'])
    assert parser.parse(['fuck', 'command', ARGUMENT_PLACEHOLDER, 'argument']) == parser._parser.parse_args(['argument', '--', 'command'])
    assert parser.parse(['fuck', 'command1', 'command2', ARGUMENT_PLACEHOLDER, 'argument']) == parser._parser.parse_args(['argument', '--', 'command1', 'command2'])
    assert parser.parse(['fuck', ARGUMENT_PLACEHOLDER, 'argument']) == parser._parser.parse_args([])

# Generated at 2022-06-14 08:23:39.154228
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    """
    >>> Parser().print_usage() # doctest: +ELLIPSIS
    usage: ...
    """


# Generated at 2022-06-14 08:23:51.378534
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    # mock stdout for test print usage
    temp_stdout = sys.stdout
    stream = io.StringIO()
    sys.stdout = stream
    parser = Parser()
    parser.print_usage()
    sys.stdout = temp_stdout

    stream.seek(0)
    actual = stream.read()
    expected = """\
usage: thefuck [-h] [-d] [-y] [-r] [-v] [-a [custom-alias-name]]
               [-l SHELL_LOGGER] [--enable-experimental-instant-mode]
               [--force-command FORCE_COMMAND] [--help]
               [command [command ...]]

positional arguments:
  command               command that should be fixed
"""
    assert actual == expected

# Generated at 2022-06-14 08:23:59.671943
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from StringIO import StringIO
    from .utils import get_alias
    stream = StringIO()
    sys.stderr = stream
    parser = Parser()
    parser.print_help()
    assert 'usage: thefuck' in stream.getvalue()
    assert '--shell-logger' in stream.getvalue()
    assert '-a' in stream.getvalue()
    assert '--alias' in stream.getvalue()
    assert '-l' in stream.getvalue()
    assert get_alias() + ']' in stream.getvalue()
    assert '-h' in stream.getvalue()

# Generated at 2022-06-14 08:24:01.220841
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:24:15.588754
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    assert "usage: thefuck" in unicode(Parser().print_usage())


# Generated at 2022-06-14 08:24:25.265504
# Unit test for method parse of class Parser
def test_Parser_parse():
    # test case 1
    # command with 1 argument
    parser = Parser()
    args = parser.parse(['thefuck', 'ls', '-la', '/'])
    assert args.command == ['ls', '-la', '/']
    # test case 2
    # command with 2 arguments
    parser = Parser()
    args = parser.parse(['thefuck', 'git', '--version'])
    assert args.command == ['git', '--version']
    # test case 3
    # command with 3 arguments
    parser = Parser()
    args = parser.parse(['thefuck', 'git', 'status', 'show'])
    assert args.command == ['git', 'status', 'show']
    # test case 4
    # command with 1 argument with --
    parser = Parser()

# Generated at 2022-06-14 08:24:28.307834
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    print(p._parser.prog)
    print(p._parser.add_help)

#test_Parser()

# Generated at 2022-06-14 08:24:30.830060
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    assert parser.print_usage() == parser._parser.print_usage(sys.stderr)


# Generated at 2022-06-14 08:24:34.226859
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    # We cannot test print_usage() of Parser()._parser directly,
    # becase it will not show in coverage report
    parser = Parser()
    parser.print_usage()

# Generated at 2022-06-14 08:24:41.583399
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['thefuck', 'ls']) == argparse.Namespace(debug=False, force_command=None, shell_logger=None, yeah=False, repeat=False, enable_experimental_instant_mode=False, help=False, alias=None, command=['ls'])
    assert parser.parse(['thefuck', 'ls', '-a', 'fuck']) == argparse.Namespace(debug=False, force_command=None, shell_logger=None, yeah=False, repeat=False, enable_experimental_instant_mode=False, help=False, alias='fuck', command=['ls'])

# Generated at 2022-06-14 08:24:44.465056
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    # Parser._parser.print_help()
    testparser = Parser()
    testparser.print_help()
    assert True

# Generated at 2022-06-14 08:24:47.295196
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    return parser


# Generated at 2022-06-14 08:24:55.827676
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from .utils import get_alias
    from .compat import text_type
    alias = get_alias()
    parser = Parser()
    parser.parse(['-h'])
    help_str = 'usage: thefuck [-h] [-v | -a [custom-alias-name] | -l SHELL_LOGGER | ' \
               '--enable-experimental-instant-mode] [-y | -r] [--force-command FORCE_COMMAND] ' \
               '[command [command ...]]'
    assert help_str == text_type(parser._parser.format_usage())

# Generated at 2022-06-14 08:25:08.912605
# Unit test for method parse of class Parser
def test_Parser_parse():
    p = Parser()
    res = p.parse(['thefuck',
                   'git branch | grep \'*\' | cut -c3-',
                   '--alias',
                   'fuck',
                   '--shell-logger',
                   '~/.shell_logger',
                   '--debug',
                   '--force-command',
                   'fuck',
                   '--',
                   '--test-arg',
                   ARGUMENT_PLACEHOLDER,
                   'arg1',
                   'arg2',
                   'arg3'])
    assert len(res) == 10
    assert res.alias == 'fuck'
    assert res.shell_logger == '~/.shell_logger'
    assert res.debug
    assert res.force_command == 'fuck'

# Generated at 2022-06-14 08:25:45.553135
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    # Test 1: a=b c d
    arguments = parser.parse(['thefuck', 'a=b', ARGUMENT_PLACEHOLDER, 'c', 'd'])
    assert 'a' in arguments
    assert 'b' in arguments
    assert 'c' in arguments
    assert 'd' in arguments
    assert '-y' not in arguments
    assert '-r' not in arguments
    # Test 2: thefuck -y a=b c d
    arguments = parser.parse(['thefuck', '-y', 'a=b', ARGUMENT_PLACEHOLDER, 'c', 'd'])
    assert 'a' in arguments
    assert 'b' in arguments
    assert 'c' in arguments
    assert 'd' in arguments
    assert '-y' in arguments

# Generated at 2022-06-14 08:25:57.404664
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse([
        'thefuck',
        'ls',
        '-alh',
        ARGUMENT_PLACEHOLDER,
        '-v',
        'command_with_args']) == parser.parse([
        'thefuck',
        '--',
        'ls',
        '-alh',
        '-v',
        'command_with_args'])
    assert parser.parse([
        'thefuck',
        '--alias',
        'fuck',
        ARGUMENT_PLACEHOLDER,
        'command_with_args']) == parser.parse([
        'thefuck',
        '--alias',
        'fuck',
        '--',
        'command_with_args'])

# Generated at 2022-06-14 08:25:59.085686
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()

# Generated at 2022-06-14 08:26:07.199899
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    import io
    import sys

    temp_stdout = sys.stdout
    try:
        out = io.StringIO()
        sys.stdout = out
        Parser().print_help()
        output = out.getvalue().strip()
    finally:
        sys.stdout = temp_stdout


# Generated at 2022-06-14 08:26:09.029279
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    assert parser.print_usage()

# Generated at 2022-06-14 08:26:10.841849
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()



# Generated at 2022-06-14 08:26:12.152499
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()

# Generated at 2022-06-14 08:26:16.991841
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from cStringIO import StringIO

    capturedOutput = StringIO()
    sys.stderr = capturedOutput

    parser = Parser()
    parser.print_help()

    sys.stderr = sys.__stderr__
    assert 'usage' in capturedOutput.getvalue()


# Generated at 2022-06-14 08:26:29.997758
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    stderr = sys.stderr = StringIO()
    parser = Parser()
    parser.print_usage()
    assert stderr.getvalue().startswith("usage: thefuck")
    assert stderr.getvalue().endswith("...\n")
    assert "show program's version number and exit" in stderr.getvalue()
    assert "[custom-alias-name] prints alias for current shell" in \
        stderr.getvalue()
    assert "log shell output to the file" in stderr.getvalue()
    assert "enable experimental instant mode, use on your own risk" in \
        stderr.getvalue()
    assert "[command that should be fixed]" in stderr.getvalue()


# Generated at 2022-06-14 08:26:32.243800
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    assert parser.print_help() == None


# Generated at 2022-06-14 08:27:18.170812
# Unit test for method print_help of class Parser
def test_Parser_print_help():
   parser = Parser()
   content = parser.print_help()

# Generated at 2022-06-14 08:27:19.530299
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()



# Generated at 2022-06-14 08:27:21.414618
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()
    assert parser != None


# Generated at 2022-06-14 08:27:23.464601
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser.prog == 'thefuck'

# Generated at 2022-06-14 08:27:24.773461
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser() is not None

# Generated at 2022-06-14 08:27:34.965498
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    from io import StringIO
    output = StringIO()

    old_stderr = sys.stderr
    sys.stderr = output

    parser.print_usage()

    sys.stderr = old_stderr
    assert output.getvalue() == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-d] [--force-command FORCE_COMMAND] [-y | -r] [--] [command ...]\n'


# Generated at 2022-06-14 08:27:37.466466
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from thefuck.types import Settings
    from thefuck.runner import Runner

    p = Parser()
    p.print_usage()


# Generated at 2022-06-14 08:27:41.434420
# Unit test for method parse of class Parser
def test_Parser_parse():
    argv = ['thefuck', 'ls', '-l']
    p = Parser()
    assert p.parse(argv).command == ['ls', '-l']

    argv = ['thefuck', ARGUMENT_PLACEHOLDER, '-l']
    assert p.parse(argv).command == ['-l']



# Generated at 2022-06-14 08:27:53.494732
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert vars(parser.parse(["thefuck", "echo hi && sleep 1 && echo bye" ])) == \
        {'debug': False, 'force_command': None, 'help': False, 'repeat': False, 'shell_logger': None, 'yes': False, 'version': False, 'command': ['echo', 'hi', '&&', 'sleep', '1', '&&', 'echo', 'bye']}
    assert vars(parser.parse(["thefuck", "echo hi && sleep 1 && echo bye", "`echo test`" ])) == \
        {'debug': False, 'force_command': None, 'help': False, 'repeat': False, 'shell_logger': None, 'yes': False, 'version': False, 'command': ['test']}

# Generated at 2022-06-14 08:27:55.382892
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    p = Parser()
    # Check if stderr is the right output
    assert getattr(sys.stderr, 'encoding') == True

# Generated at 2022-06-14 08:29:37.267311
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    """ Unit test for method print_help of class Parser"""
    test_parser = Parser()
    test_parser.print_help()

# Generated at 2022-06-14 08:29:38.912319
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser is not None


# Generated at 2022-06-14 08:29:42.509081
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['/bin/echo']) == \
           parser._parser.parse_args(['/bin/echo'])


# Generated at 2022-06-14 08:29:55.082430
# Unit test for method parse of class Parser
def test_Parser_parse():
    assert Parser().parse([
        'fuck', '--force-command', 'ls', '-la', '--',
        ARGUMENT_PLACEHOLDER, '&&', 'git', 'commit', '-am', '"change"']) == \
        argparse.Namespace(
            alias=None,
            command=['ls', '-la', '&&', 'git', 'commit', '-am', '"change"'],
            debug=False,
            enable_experimental_instant_mode=False,
            force_command='ls',
            help=False,
            repeat=False,
            shell_logger=None,
            version=False,
            yeah=False)


# Generated at 2022-06-14 08:29:56.838083
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:29:58.024252
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()

# Generated at 2022-06-14 08:30:02.933818
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from tempfile import NamedTemporaryFile
    from os import remove

    with NamedTemporaryFile() as file:
        Parser().print_help(file=file)
        file.flush()
        with open(file.name, 'r') as lines:
            assert len(lines) > 0

# Generated at 2022-06-14 08:30:05.700387
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    argv = ['./thefuck']
    arguments = parser.parse(argv)
    assert arguments.help



# Generated at 2022-06-14 08:30:07.793414
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser is not None

# Unit test to check the parse function

# Generated at 2022-06-14 08:30:10.817779
# Unit test for constructor of class Parser
def test_Parser():
    argparser = Parser()
    assert argparser._parser.prog == 'thefuck'
    assert argparser._parser.add_help == False