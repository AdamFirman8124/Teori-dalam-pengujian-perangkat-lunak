

# Generated at 2022-06-14 08:20:55.103158
# Unit test for constructor of class Parser
def test_Parser():
    Parser()


# Generated at 2022-06-14 08:20:58.405468
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    usage = 'usage: thefuck [-h] [-v] [-a [custom-alias-name]]\n'
    parser = Parser()
    assert parser.print_usage() == usage

# Generated at 2022-06-14 08:21:06.635448
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    # redirect stdout to a string buffer
    stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        parser.print_usage()
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = stdout
    assert output == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]]\n' \
                     '              [-l SHELL_LOGGER]\n' \
                     '              [--enable-experimental-instant-mode]\n' \
                     '              [-y | -r] [-d] [--force-command COMMAND]\n' \
                     '              [command [command ...]]\n'


# Generated at 2022-06-14 08:21:17.663575
# Unit test for method parse of class Parser
def test_Parser_parse():
    args = Parser().parse(['thefuck', '--help'])
    assert args.help

    args = Parser().parse(['thefuck', '--debug', '--help'])
    assert args.help
    assert args.debug

    args = Parser().parse(['thefuck', 'ls', '-al'])
    assert not args.help
    assert args.command == ['ls', '-al']

    args = Parser().parse(['thefuck', 'git', 'commmit', '-m', 'message',
                           '&lt;', 'THEFUCK_PLACEHOLDER', 'rm', 'a.file'])
    assert args.command == ['git', 'commmit', '-m', 'message', '&lt;']
    assert args.force_command == 'rm a.file'


# Generated at 2022-06-14 08:21:20.250859
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser()



# Generated at 2022-06-14 08:21:21.482283
# Unit test for constructor of class Parser
def test_Parser():
    Parser()

# Generated at 2022-06-14 08:21:29.032692
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    """check print_help() of Parser"""
    parser = Parser()
    # save sys.stdout
    save_stdout = sys.stdout
    # redirect sys.stdout to StringIO
    out = StringIO()
    sys.stdout = out
    parser.print_help()
    # restore sys.stdout
    sys.stdout = save_stdout
    # do we get right help string?
    assert out.getvalue().find("usage: thefuck") != -1

# Generated at 2022-06-14 08:21:32.337119
# Unit test for constructor of class Parser
def test_Parser():
    cmd = Parser()
    # this method is private so it's hard to test, it's just for the sake of coverage
    cmd._add_arguments()



# Generated at 2022-06-14 08:21:34.241502
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()
    assert True


# Generated at 2022-06-14 08:21:37.844227
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    args = parser.parse(['-v'])
    assert args.version == True
    args = parser.parse(['-l'])
    assert args.shell_logger == True

# Generated at 2022-06-14 08:21:41.477880
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser != None


# Generated at 2022-06-14 08:21:43.866937
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser

# Unit test of function _add_arguments()

# Generated at 2022-06-14 08:21:51.869437
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from io import BytesIO
    from sys import stderr
    stderr = BytesIO()
    parser = Parser()
    parser.print_usage()
    stderr.seek(0)
    assert 'usage: thefuck [-v] [-a [custom-alias-name]] [-l shell-logger]' \
           ' [-h] [-y] [-r]\n' == stderr.read()


# Generated at 2022-06-14 08:21:59.387751
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()
    assert(sys.stderr.getvalue() == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-y | -r] [-d] [--force-command FORCE_COMMAND] [command [command ...]]\n')


# Generated at 2022-06-14 08:22:02.312128
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    try:
        parser.print_usage()
    except SystemExit:
        pass
    assert True

# Generated at 2022-06-14 08:22:04.138175
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser


# Generated at 2022-06-14 08:22:05.424640
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    Parser().print_usage()


# Generated at 2022-06-14 08:22:11.411543
# Unit test for method print_help of class Parser
def test_Parser_print_help():

    parser = Parser()

    # Store the stderr of function print_help()
    old_stderr = sys.stderr
    out = StringIO()
    sys.stderr = out

    parser.print_help()
    output = out.getvalue()
    assert (output.startswith('usage: thefuck'))

# Generated at 2022-06-14 08:22:23.294756
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    # Arrange
    from io import StringIO
    from unittest import mock
    from unittest.mock import patch

    parser = Parser()
    parser_output = """\
usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l shell-logger] \
[--enable-experimental-instant-mode] [-y | -r] [-d] [--force-command FORCE_COMMAND] \
[--] [command [command ...]]
"""
    # Assume that stderr is sys.stderr
    expected_output = parser_output
    with patch.object(sys, 'stderr', new=StringIO()) as mock_stderr:
        # Act
        parser.print_usage()
        output = mock_stderr.getvalue()
    # Ass

# Generated at 2022-06-14 08:22:25.599815
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser.prog == 'thefuck'
    assert not parser._parser.add_help



# Generated at 2022-06-14 08:22:30.337283
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser


# Generated at 2022-06-14 08:22:32.734255
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    # Setup
    parser = Parser()
    # Exercise
    parser.print_help()
    # Verify
    assert True # It works when it runs to the end



# Generated at 2022-06-14 08:22:33.748883
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:22:35.160358
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser()._parser.prog == 'thefuck'

# Generated at 2022-06-14 08:22:37.710922
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()
    assert True


# Generated at 2022-06-14 08:22:43.677782
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(["thefuck"])
    assert args.command == []
    assert args.debug == False
    assert args.shell_logger == None
    assert args.help == False
    assert args.version == False
    assert args.alias == None
    assert args.force_command == None
    assert args.enable_experimental_instant_mode == False


# Generated at 2022-06-14 08:22:50.455407
# Unit test for method parse of class Parser
def test_Parser_parse():
    from .fuck import Fuck
    sys.argv = ['/usr/local/bin/thefuck', '--force_command', 'ls', '--', 'git', 'add']
    fuck = Fuck()
    assert(fuck.command.script == 'git')
    assert(fuck.command.script_parts == ['git', 'add'])

# Generated at 2022-06-14 08:22:53.884856
# Unit test for constructor of class Parser
def test_Parser():
    s = Parser()
    assert type(s) is Parser


"""
Loading Module
"""
if __name__ == '__main__':
    test_Parser()

# Generated at 2022-06-14 08:23:00.808451
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from StringIO import StringIO
    from contextlib import contextmanager

    @contextmanager
    def redirect_io():
        stdout, stderr = sys.stdout, sys.stderr
        sys.stdout, sys.stderr = StringIO(), StringIO()
        try:
            yield
        finally:
            sys.stdout, sys.stderr = stdout, stderr

    with redirect_io():
        parser = Parser()
        parser.print_usage()

    assert 'usage: thefuck' in sys.stdout.getvalue()


# Generated at 2022-06-14 08:23:14.877598
# Unit test for method parse of class Parser
def test_Parser_parse():
    def assert_parse(argv, expected_command, expected_args):
        assert_args = [expected_args.get(k, None) for k in [
            'alias', 'yes', 'repeat', 'command', 'debug', 'force_command']]
        assert_args.append(expected_args.get('shell_logger', None))
        assert_args.append(expected_args.get('enable_experimental_instant_m', None))
        assert_args.append(expected_args.get('help', None))
        assert_args.append(expected_command)

        arg_parser = Parser()
        args = arg_parser.parse(['thefuck'] + argv)
        assert args.command == expected_command, args.command

# Generated at 2022-06-14 08:23:24.039672
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from .utils import support_mock
    with support_mock.patch_stdout_isatty(sys.stdout):
        p = Parser()
        p.print_help()
        assert sys.stdout.getvalue().startswith('usage:')

# Generated at 2022-06-14 08:23:35.129340
# Unit test for method parse of class Parser
def test_Parser_parse():
    # When we pass argument that should be ignored by parser,
    # then we get them in return.
    parser = Parser()
    args = parser.parse(['script.py', '-vv'])
    assert args.debug is True
    assert args.command == []

    # When we pass argument that should be parsed,
    # then we get them in return.
    args = parser.parse(['script.py', '-l', 'log.txt', '-vv'])
    assert args.debug is True
    assert args.shell_logger == 'log.txt'
    assert args.command == []

    # When we pass argument that should be parsed,
    # and our special placeholder after it,
    # then we get arguments after placeholder in our command.

# Generated at 2022-06-14 08:23:41.633862
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    original_sys_argv = sys.argv
    sys.argv = original_sys_argv[:1] + list("foo bar 'baz'")
    args = parser.parse(sys.argv)
    assert args == parser._parser.parse_args("foo bar 'baz'".split(" "))
    sys.argv = original_sys_argv

# Generated at 2022-06-14 08:23:46.558798
# Unit test for method parse of class Parser
def test_Parser_parse():
    args = ['', '-v']
    parser = Parser()
    real_args = parser.parse(args)
    expected_args = parser._prepare_arguments(args[1:])
    assert real_args == parser._parser.parse_args(expected_args)

# Generated at 2022-06-14 08:23:55.143240
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from .utils import capture_stderr, which
    from .tests.utils import make_invocation, which

    invocation = make_invocation()

    with capture_stderr() as stderr:
        Parser().print_help()
    assert 'thefuck [OPTIONS] [COMMAND]' in stderr.getvalue()
    assert '--version' in stderr.getvalue()

    with capture_stderr() as stderr:
        Parser().print_usage()
    assert 'usage: thefuck [OPTIONS] [COMMAND]' in stderr.getvalue()
    assert '--version' in stderr.getvalue()



# Generated at 2022-06-14 08:24:07.049478
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from tempfile import NamedTemporaryFile
    from .utils import read_output

    parser = Parser()

    with NamedTemporaryFile() as f:
        parser.print_help(file=f)
        f.seek(0)

# Generated at 2022-06-14 08:24:14.446506
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from io import StringIO
    message = StringIO()
    parser = Parser()
    parser.print_usage(file=message)
    assert message.getvalue() == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-d] [--force-command FORCE_COMMAND] [--] [command [command ...]]\n'  # noqa: E501


# Generated at 2022-06-14 08:24:20.484291
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from io import StringIO
    from sys import stderr
    try_and_print = lambda x: Parser().print_usage()
    # test for: Parser._parser.print_usage(sys.stderr)
    stderr = StringIO()
    try_and_print()
    print(stderr.getvalue(),'\n')


# Generated at 2022-06-14 08:24:27.907023
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['_', '-l', '--force-command', 'echo', ARGUMENT_PLACEHOLDER]) == \
        Namespace(alias=None, command=[], debug=False, enable_experimental_instant_mode=False,
                  force_command='echo', help=False, shell_logger='-l', yes=False, repeat=False,
                  version=False)



# Generated at 2022-06-14 08:24:30.057080
# Unit test for constructor of class Parser
def test_Parser():
	_parser = ArgumentParser(prog='thefuck', add_help=False)
	assert(_parser is not None)

# Generated at 2022-06-14 08:24:51.262404
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    """Testing method print_help of class Parser"""
    parser = Parser()
    sys.stderr = StringIO()
    parser.print_help()
    assert(sys.stderr.getvalue().startswith('usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-d] [--force-command FORCE_COMMAND] [command [command ...]]\n'))
    sys.stderr = StringIO()
    parser.print_usage()

# Generated at 2022-06-14 08:24:54.514298
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    assert("usage: thefuck [-h] [-v] [-a [CUSTOM-ALIAS-NAME]]" in str(parser.print_help()))

# Generated at 2022-06-14 08:25:07.558561
# Unit test for method parse of class Parser
def test_Parser_parse():

    # Test 1
    parser1 = Parser()
    arguments1 = parser1.parse(['test', 'python', 'manage.py', 'runserver'])
    assert arguments1.command == ['manage.py', 'runserver'], \
        "failed to handle normal argument"

    # Test 2
    parser2 = Parser()
    arguments2 = parser2.parse(['test', 'python', 'manage.py', 'runserver', ARGUMENT_PLACEHOLDER])
    assert arguments2.command == ['python', 'manage.py', 'runserver'], \
        "failed to handle argument with placeholder"

    # Test 3
    parser3 = Parser()

# Generated at 2022-06-14 08:25:17.711599
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser._prepare_arguments(['fuck', 'ls', '-la']) == ['ls', '-la', '--', 'fuck']
    assert parser._prepare_arguments(['fuck', 'ls', ARGUMENT_PLACEHOLDER, '-la']) == ['-la', '--', 'ls']
    assert parser._prepare_arguments(['fuck', 'ls', 'fuck', ARGUMENT_PLACEHOLDER, '-la']) == ['-la', '--', 'ls', 'fuck']
    assert parser._prepare_arguments(['fuck', 'ls', ARGUMENT_PLACEHOLDER, '-la', '-la']) == ['-la', '-la', '--', 'ls']

# Generated at 2022-06-14 08:25:19.437995
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    _parser = Parser()
    _parser.print_usage()


# Generated at 2022-06-14 08:25:30.919506
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    # Basic and place holder are not exists
    assert parser.parse(['-v']) == parser._parser.parse_args(['-v'])
    assert parser.parse(['--version']) == parser._parser.parse_args(['--version'])

    # Place holder
    assert parser.parse(['--', '-v']) == parser._parser.parse_args(['--', '-v'])
    assert parser.parse(['--', '--version']) == parser._parser.parse_args(['--', '--version'])
    assert parser.parse(['--', '--', '-v']) == parser._parser.parse_args(['--', '--', '-v'])
    assert parser.parse(['--', '--', '--version']) == parser._parser.parse

# Generated at 2022-06-14 08:25:32.640407
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    Parser().print_usage()

# Generated at 2022-06-14 08:25:35.121870
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    assert parser.print_help().startswith("usage: thefuck")


# Generated at 2022-06-14 08:25:38.705422
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    with patch('sys.stderr') as mock_stderr:
        Parser().print_usage()

    assert mock_stderr.write.call_count == 1


# Generated at 2022-06-14 08:25:40.744231
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert isinstance(parser, Parser)


# Generated at 2022-06-14 08:26:02.200379
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    capture = io.StringIO()
    parser.print_help(file=capture)
    assert "usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l shell-logger] [--enable-experimental-instant-mode] [-y | -r]" in capture.getvalue() and "optional arguments:" in capture.getvalue()

# Generated at 2022-06-14 08:26:05.017288
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    assert p is not None

parser = Parser()



# Generated at 2022-06-14 08:26:06.876169
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()
    assert True

# Generated at 2022-06-14 08:26:09.751154
# Unit test for constructor of class Parser
def test_Parser():
    assert_equal(Parser()._parser.prog, 'thefuck')
    assert_equal(Parser()._parser.add_help, False)


# Generated at 2022-06-14 08:26:10.932046
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser().print_help()

# Generated at 2022-06-14 08:26:12.217493
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    assert p != None

# Generated at 2022-06-14 08:26:14.832898
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser_usage = parser.parse(['thefuck', '--help']).help
    assert parser_usage is True
test_Parser_print_usage()

# Generated at 2022-06-14 08:26:23.773350
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from unittest.mock import patch
    from sys import stderr

    test = Parser()
    with patch('textwrap.dedent', lambda x: x) as mocked_method:
        with patch('sys.stderr', stderr) as mocked_stderr:
            test.print_help()
            assert 'usage: thefuck' in mocked_stderr.getvalue()
            assert 'optional arguments:' in mocked_stderr.getvalue()

# Generated at 2022-06-14 08:26:35.902256
# Unit test for method parse of class Parser
def test_Parser_parse():
    p = Parser()
    args = p.parse(['fuck'])
    assert not args.enable_experimental_instant_mode
    assert not args.debug
    assert not args.help
    assert not args.repeat
    assert not args.shell_logger
    assert not args.version
    assert not args.yes
    assert not args.alias
    assert not args.force_command

    args = p.parse(['fuck', '--debug'])
    assert args.debug
    assert not args.help
    assert not args.repeat
    assert not args.shell_logger
    assert not args.version
    assert not args.yes
    assert not args.alias
    assert not args.force_command

    args = p.parse(['fuck', '--help'])
    assert args.help
    assert not args.debug

# Generated at 2022-06-14 08:26:48.596707
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(
        ['./thefuck', 'git', 'brnch', ARGUMENT_PLACEHOLDER, '-l']) == \
        Namespace(alias='fuck',
                  command=['git', 'brnch'],
                  debug=False,
                  enable_experimental_instant_mode=False,
                  force_command=None,
                  help=False,
                  repeat=False,
                  shell_logger='-l',
                  version=False,
                  yeah=False)

# Generated at 2022-06-14 08:27:27.077902
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    """Unit test for method print_help of class Parser.

    """
    import sys
    import StringIO
    import thefuck.main
    sys.argv = ['thefuck', '--debug', '--help']
    output = StringIO.StringIO()
    old_stdout = sys.stdout
    sys.stdout = output
    thefuck.main.main()
    sys.stdout = old_stdout
    assert '--debug' in output.getvalue()

# Generated at 2022-06-14 08:27:28.247439
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser is not None

# Generated at 2022-06-14 08:27:38.829699
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from .output import print_usage
    from .main import fuck
    from .const import ALIAS

    parser = Parser()
    parser.print_help()
    assert "argument to -l which does not start with '-'" in caplog.text

    fuck('echo test')
    parser.print_help()
    assert "argument to -l which does not start with '-'" not in caplog.text
    assert "`{} something`".format(ALIAS) in caplog.text

    fuck('echo test')
    print_usage()
    assert "argument to -l which does not start with '-'" not in caplog.text
    assert "`{} something`".format(ALIAS) in caplog.text

    # check that print_help can be called without active logger
    parser.print_help()


# Generated at 2022-06-14 08:27:44.445398
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    out = StringIO()
    sys.stderr = out
    parser.print_usage()
    output = out.getvalue()
    sys.stderr = sys.__stderr__
    assert 'usage: thefuck [-h] [-v] [-a [custom-alias-name]]' in output


# Generated at 2022-06-14 08:27:47.339493
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    try:
        parser.print_usage()
        return True
    except:
        return False


# Generated at 2022-06-14 08:27:53.122913
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(['', '--alias', 'test'])
    assert args.alias == 'test'
    args = parser.parse(['', 'fuck', 'ls', '/tmp'])
    assert args.command == ['fuck', 'ls', '/tmp']
    args = parser.parse(['', 'fuck', 'ls'])
    assert args.command == ['fuck', 'ls']
    args = parser.parse(['', 'fuck'])
    assert args.command == ['fuck']
    args = parser.parse(['', 'fuck', ARGUMENT_PLACEHOLDER, 'ls', '/tmp'])
    assert args.command == ['ls', '/tmp']
    args = parser.parse(['', 'fuck', ARGUMENT_PLACEHOLDER, 'ls'])

# Generated at 2022-06-14 08:27:54.614672
# Unit test for constructor of class Parser
def test_Parser():
    Parser()


# Generated at 2022-06-14 08:27:59.377796
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(['thefuck','--help','--','git','add','test'])

    assert(args.help == True)
    assert(args.command == ['git','add','test'])

# Generated at 2022-06-14 08:28:00.609957
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:28:03.812985
# Unit test for constructor of class Parser
def test_Parser():
	p = Parser()
	p._prepare_arguments('')
	p.parse('')
	p.print_usage()
	p.print_help()

# Generated at 2022-06-14 08:29:27.790063
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser != None

# Generated at 2022-06-14 08:29:35.054030
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()
    assert sys.stderr.getvalue() == (
        'usage: thefuck [-h] [-v] [-a [custom-alias-name]] '
        '[-l shell-logger]\n'
        '               [--enable-experimental-instant-mode]\n'
        '               [-y | -r] [-d] [--force-command force-command]\n'
        '               [command [command ...]]\n')


# Generated at 2022-06-14 08:29:36.805817
# Unit test for constructor of class Parser
def test_Parser():
    a = Parser()
    assert a


# Generated at 2022-06-14 08:29:39.428812
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from mock import patch
    from thefuck.shells import Shell

    with patch.object(Parser,
                      '__init__',
                      return_value=None):
        assert Parser().print_usage()



# Generated at 2022-06-14 08:29:52.642989
# Unit test for method parse of class Parser
def test_Parser_parse(): 
    import sys
    import io
    sys.stdout = io.StringIO()
    sys.stderr = io.StringIO()
    parser = Parser()
    parser.parse(['', '--enable-experimental-instant-mode'])
    result = sys.stdout.getvalue()
    assert result == ''
    parser.print_usage()
    result = sys.stderr.getvalue()
    assert result == 'usage: thefuck [-h] [-v] [-a [CUSTOM-ALIAS-NAME]] [-l SHELL-LOGGER]\n                  [--enable-experimental-instant-mode] [-d]\n                  [--force-command FORCE-COMMAND]\n                  [command [command ...]]\n'
    parser.print_help()

# Generated at 2022-06-14 08:29:54.889364
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    usage = parser.print_usage()
    assert usage == parser.print_usage()



# Generated at 2022-06-14 08:29:56.296320
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser is not None


# Generated at 2022-06-14 08:30:07.393778
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    cmd1 = ['fuck', 'bash', '-l', '-c', 'ls']
    cmd2 = ['fuck', 'bash', '-l', '-c', 'ls', ARGUMENT_PLACEHOLDER, '-h']
    parse1 = parser.parse(cmd1)
    print(parse1)
    assert parse1.command == ['bash', '-l', '-c', 'ls']
    parse2 = parser.parse(cmd2)
    print(parse2)
    assert parse2.command == ['ls']
    assert parse2.help == True
    return True

test_Parser_parse()

# Generated at 2022-06-14 08:30:18.939296
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    args = parser.parse(['thefuck', 'command', 'arg1', 'arg2'])
    stdout = sys.stdout
    try:
        sys.stdout = stderr = StringIO()
        parser.print_usage()
        assert_equals(
            stderr.getvalue(),
            'usage: thefuck [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER]\n'
            '               [--enable-experimental-instant-mode] [-h] [-d]\n'
            '               [--force-command FORCE_COMMAND] COMMAND [COMMAND ...]\n')
    except:
        raise
    finally:
        sys.stdout = stdout


# Generated at 2022-06-14 08:30:30.063470
# Unit test for method parse of class Parser
def test_Parser_parse():
    args_01 = ["--debug"]
    args_02 = ["tail"]
    args_03 = ["tail", "-n", "10", "--", ARGUMENT_PLACEHOLDER, "-d", "--force-command", "tail", "--debug"]
    args_04 = ["tail", "-n", "10", "--", ARGUMENT_PLACEHOLDER, "--yes"]
    args_05 = ["tail", "-n", "10", "--", ARGUMENT_PLACEHOLDER, "--repeat"]
    parser = Parser()

    result_01 = parser.parse(args_01)
    assert(result_01.debug == True)
    assert(result_01.force_command == None)
    assert(result_01.command == [])
