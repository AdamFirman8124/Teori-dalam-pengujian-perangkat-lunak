

# Generated at 2022-06-14 08:20:56.441621
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    args = parser.parse(['fuck', '--alias'])
    assert args.alias == get_alias()

# Generated at 2022-06-14 08:20:58.640859
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    p = Parser()
    #print p.print_help()
    p.parse(['fuck', '--help'])

# Generated at 2022-06-14 08:20:59.907482
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert isinstance(parser, Parser)


# Generated at 2022-06-14 08:21:01.495712
# Unit test for constructor of class Parser
def test_Parser():
    P = Parser()
    assert(isinstance(P, Parser))
    assert(isinstance(P._parser, ArgumentParser))


# Generated at 2022-06-14 08:21:03.358539
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser


# Generated at 2022-06-14 08:21:04.604783
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser()


# Generated at 2022-06-14 08:21:08.484868
# Unit test for method parse of class Parser
def test_Parser_parse():
    class_name = Parser()
    result = class_name.parse(['thefuck', 'git', '--hard'])
    assert(result.command == ['git', '--hard'])



# Generated at 2022-06-14 08:21:17.567909
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    import io
    import sys
    f = io.StringIO()
    sys.stderr = f
    parser = Parser()
    parser.print_usage()
    assert f.getvalue() == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]]\
 [-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-d] [-y] [-r] [--] \
[COMMAND [COMMAND ...]]\n'
    f.close()


# Generated at 2022-06-14 08:21:23.614246
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    stderr = sys.stderr
    try:
        from StringIO import StringIO
        sys.stderr = StringIO()
        parser.print_usage()
    finally:
        sys.stderr = stderr



# Generated at 2022-06-14 08:21:25.047965
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()

# Generated at 2022-06-14 08:21:41.051830
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    # Test if parser returns correct value.
    assert parser.parse(['thefuck', 'echo']) == parser._parser.parse_args(['--', 'echo'])
    assert parser.parse(['thefuck', '-v']) == parser._parser.parse_args(['-v'])
    assert parser.parse(['thefuck', 'echo', 'arg1', 'arg2']) == parser._parser.parse_args(['--', 'echo', 'arg1', 'arg2'])
    assert parser.parse(['thefuck', 'echo', ARGUMENT_PLACEHOLDER, 'arg1', 'arg2']) == parser._parser.parse_args(['arg1', 'arg2', '--', 'echo'])

# Generated at 2022-06-14 08:21:52.178092
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['thefuck', 'ech0']) == parser._parser.parse_args(['ech0'])
    assert parser.parse(['thefuck', '--repeat', 'ech0']) == parser._parser.parse_args(['--repeat', 'ech0'])
    # assert parser.parse(['thefuck', '--repeat', 'ech0', 'hello', '1']) == parser._parser.parse_args(['--repeat', 'ech0', 'hello', '1'])
    assert parser.parse(['thefuck', '--repeat', 'ech0', ARGUMENT_PLACEHOLDER, 'hello', '1']) == parser._parser.parse_args(['hello', '1', '--', '--repeat', 'ech0'])



# Generated at 2022-06-14 08:21:57.140860
# Unit test for method parse of class Parser
def test_Parser_parse():
    # Given
    argv = 'thefuck -v test'.split(' ')
    parser = Parser()
    # When
    args = parser.parse(argv)
    # Then
    assert(args.version == True)
    assert(args.command == ['test'])


# Generated at 2022-06-14 08:21:59.762413
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()
    assert True


# Generated at 2022-06-14 08:22:10.306953
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    class Stderr(object):
        def __init__(self):
            self.content = StringIO()
            self.old_stderr = sys.stderr
            sys.stderr = self

        def write(self, s):
            self.content.write(s)

        def __del__(self):
            sys.stderr = self.old_stderr

    parser = Parser()
    stderr = Stderr()
    parser.print_usage()
    assert 'usage: thefuck' in stderr.content.getvalue()



# Generated at 2022-06-14 08:22:20.861134
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from .const import VERSION
    from io import StringIO

    output = StringIO()
    sys.stderr = output
    Parser().print_usage()
    output.seek(0)
    assert "usage: thefuck [--version] [-h] [-v] [-a [custom-alias-name]]" \
        "[-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-d] [-y] [-r] " \
        "[--force-command FORCE_COMMAND] [command [command ...]]\n" == \
        output.read()
    sys.stderr = sys.__stderr__


# Generated at 2022-06-14 08:22:25.251284
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from .utils import capture_output
    from .main import print_usage
    parser = Parser()
    with capture_output() as (out, err):
        parser.print_usage()
    assert out.getvalue().strip() == print_usage().strip()
    assert err.getvalue() == ''


# Generated at 2022-06-14 08:22:28.328263
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()
    assert True


# Generated at 2022-06-14 08:22:42.540694
# Unit test for method parse of class Parser
def test_Parser_parse():
    with mock.patch.object(Parser, '_add_arguments'):
        parser = Parser()

        # test with argument placeholder
        with mock.patch.object(Parser, '_prepare_arguments') as \
                prepare:
            prepare.return_value = None
            with mock.patch('sys.argv', new=['fuck', '-v', 'dir',
                                             ARGUMENT_PLACEHOLDER, '-h']):
                parser.parse(sys.argv)
            prepare.assert_called_once_with(['fuck', '-v', 'dir',
                                             ARGUMENT_PLACEHOLDER, '-h'])
            parse = parser._parser.parse_args
            parse.assert_called_once_with([])

        # test without argument placeholder

# Generated at 2022-06-14 08:22:44.034400
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    parser.parse()


# Generated at 2022-06-14 08:23:16.916492
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    assert p
    assert p._parser
    assert p._parser._actions[0].dest == 'version'
    assert p._parser._actions[0].option_strings == ['-v', '--version']
    assert p._parser._actions[1].dest == 'alias'
    assert p._parser._actions[1].option_strings == ['-a', '--alias']
    assert p._parser._actions[1].const == get_alias()
    assert p._parser._actions[1].help == '[custom-alias-name] prints alias for current shell'
    assert p._parser._actions[2].dest == 'shell_logger'
    assert p._parser._actions[2].option_strings == ['--shell-logger', '-l']

# Generated at 2022-06-14 08:23:17.898863
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    assert p is not None

# Generated at 2022-06-14 08:23:30.921344
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    temp_stdout = StringIO()
    old_stdout = sys.stdout
    sys.stdout = temp_stdout

# Generated at 2022-06-14 08:23:32.048176
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser() is not None


# Generated at 2022-06-14 08:23:38.646078
# Unit test for method parse of class Parser
def test_Parser_parse():
    args_parser = Parser()
    # Test command without "thefuck"
    arguments = args_parser.parse(['ls'])
    assert arguments.command == ['ls']
    # Test command with "thefuck"
    arguments = args_parser.parse(['thefuck', 'ls'])
    assert arguments.command == ['ls']
    # Test command with "thefuck", its argument and it argument's value
    arguments = args_parser.parse(['thefuck', '-a', 'fuck'])
    assert arguments.alias == 'fuck'
    # Test command with "thefuck", its argument and "--"
    arguments = args_parser.parse(['thefuck', '--alias', '--'])
    assert arguments.alias == get_alias()
    # Test command with "thefuck", it's argument and another after "--"
   

# Generated at 2022-06-14 08:23:51.459412
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    import os
    import argparse
    import mock
    import pytest

    class Parser(object):
        def __init__(self):
            self.parser = argparse.ArgumentParser(prog='thefuck', add_help=False)

        def print_usage(self):
            self.parser.print_usage(sys.stderr)

    p = Parser()
    with mock.patch.object(sys, 'stderr') as stderr_mock:
        p.print_usage()

# Generated at 2022-06-14 08:23:58.843917
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()

    parser.print_usage()
    result = sys.stderr.read()
    output = 'usage: thefuck [-h] [-v] [-a [custom-alias-name]]\n'
    output += '                [-l shell-logger] [--enable-experimental-instant-mode]\n'
    output += '                [-y | -r] [-d] [--force-command FORCE-COMMAND]\n'
    output += '                command [command ...]\n'
    assert output == result

# Generated at 2022-06-14 08:23:59.956597
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:24:09.140799
# Unit test for constructor of class Parser
def test_Parser():
    from .const import ARGUMENT_PLACEHOLDER
    from .utils import get_alias
    from .settings import parse_alias
    import sys
    import os

    parser = Parser()
    os.environ['SHELL'] = 'zsh'
    args = parser.parse([
        'thefuck', 'fuck', '--enable-experimental-instant-mode', '-a', 'test',
        ARGUMENT_PLACEHOLDER, '-e', '/tmp/alias.py'])
    parse_alias(args.alias)

    print(args.enable_experimental_instant_mode)
    print(args.alias)

# Generated at 2022-06-14 08:24:10.641026
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:24:41.623618
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    Parser().print_usage()

# Generated at 2022-06-14 08:24:54.950841
# Unit test for method parse of class Parser
def test_Parser_parse():
    sys.argv = ['thefuck', '-y', 'some', ARGUMENT_PLACEHOLDER, 'command']
    assert Parser().parse(sys.argv).yes == True
    assert Parser().parse(sys.argv).command == ['command']
    sys.argv = ['thefuck', 'command', 'some', ARGUMENT_PLACEHOLDER, '--help']
    assert Parser().parse(sys.argv).help == True
    assert Parser().parse(sys.argv).command == ['command', 'some']
    sys.argv = ['thefuck', '--', '--help', 'command']
    assert Parser().parse(sys.argv).help == False
    assert Parser().parse(sys.argv).command == ['--help', 'command']

# Generated at 2022-06-14 08:25:04.340017
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    import sys
    import io
    sys.stderr = io.StringIO()
    Parser().print_usage()
    assert sys.stderr.getvalue().strip() == "usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-d] [--force-command FORCE_COMMAND] [-y] [-r] [--] [command [command ...]]"  # noqa: E501
    sys.stderr = sys.__stderr__


# Generated at 2022-06-14 08:25:07.018852
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:25:13.144509
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from io import StringIO
    from unittest.mock import patch

    args = ['-d']

    with patch('sys.stderr', new=StringIO()) as mock_stderr:
        parser = Parser()
        parser.parse(args)
        parser.print_usage()
        mock_stderr.seek(0)
        assert mock_stderr.readline() == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]]\n'



# Generated at 2022-06-14 08:25:27.306323
# Unit test for method parse of class Parser
def test_Parser_parse():
    obj = Parser()
    assert obj._prepare_arguments([]) == []
    assert obj._prepare_arguments(['ls']) == ['--', 'ls']
    assert obj._prepare_arguments(['ls', '-l']) == ['--', 'ls', '-l']
    assert obj._prepare_arguments(['ls', ARGUMENT_PLACEHOLDER]) == []
    assert obj._prepare_arguments(['ls', ARGUMENT_PLACEHOLDER, '-l']) == ['-l']
    assert obj._prepare_arguments(['ls', ARGUMENT_PLACEHOLDER, '-l', '-a']) == ['-l', '-a']

# Generated at 2022-06-14 08:25:37.352239
# Unit test for method parse of class Parser
def test_Parser_parse():
    argv = [" program", "--", "command", "arg1", ARGUMENT_PLACEHOLDER, "-arg2", "-arg3", "arg4"]
    parser = Parser()
    args = parser.parse(argv)
    assert args.alias == False
    assert args.debug == False
    assert args.help == False
    assert args.repeat == False
    assert args.shell_logger == None
    assert args.version == False
    assert args.yes == False
    assert args.force_command == None
    assert args.command == ["-arg2", "-arg3", "arg4"]

# Generated at 2022-06-14 08:25:46.480947
# Unit test for constructor of class Parser
def test_Parser():
    fuck = Parser()
    # test parse
    args = fuck.parse(['fuck', '-d', '-h', '-v'])
    assert args.debug
    assert args.help
    assert args.version

    args = fuck.parse(['fuck','-h'])
    assert args.help

    args = fuck.parse(['fuck', '-d', '--version', '-h'])
    assert args.debug
    assert args.help
    assert args.version

    args = fuck.parse(['fuck','-l','logfile'])
    assert args.shell_logger == 'logfile'

    args = fuck.parse(['fuck','-a'])
    assert args.alias is None

    args = fuck.parse(['fuck','-a','alias'])
    assert args.alias == 'alias'



# Generated at 2022-06-14 08:25:59.285913
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from six import StringIO
    from contextlib import redirect_stderr

    f = StringIO()
    with redirect_stderr(f):
        parser = Parser()
        parser.print_usage()
        output = f.getvalue().strip()

    assert 'usage: thefuck [-h] [-v] [-a [custom-alias-name]]' in output
    assert 'thefuck [-h] [-v] [-a [custom-alias-name]]' in output
    assert 'thefuck [-h] [-v] [-a [custom-alias-name]] [-r] [-y]' in output
    assert 'thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER]' in output

# Generated at 2022-06-14 08:26:06.252514
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser().parse(['thefuck', '--version']).version
    assert Parser().parse(['thefuck', '--help']).help
    assert Parser().parse(['thefuck', '-v']).version
    assert Parser().parse(['thefuck', '-h']).help
    assert Parser().parse(['thefuck', '--alias']).alias
    assert Parser().parse(['thefuck', '--alias', 'fuck']).alias == 'fuck'
    assert Parser().parse(['thefuck']).command is None
    assert Parser().parse(['thefuck', 'git', 'log']).command == ['git', 'log']


# Generated at 2022-06-14 08:26:54.073834
# Unit test for method parse of class Parser
def test_Parser_parse():
    class Args:
        alias = 'fuck'
        command = ['git', 'add', '.']

    parser = Parser()
    assert parser.parse(['thefuck', 'git', 'add', '.']) == Args()

    class Args:
        command = ['git', 'add', '.']

    assert parser.parse(['thefuck', '--', 'git', 'add', '.']) == Args()

# Generated at 2022-06-14 08:26:59.222177
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    out = StringIO()
    save_stderr = sys.stderr
    sys.stderr = out
    parser.print_help()
    assert 'usage: thefuck [-h]' in out.getvalue()
    sys.stderr = save_stderr

# Generated at 2022-06-14 08:27:00.855779
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser
    assert parser._parser


# Generated at 2022-06-14 08:27:02.475981
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    assert parser.print_usage() is None


# Generated at 2022-06-14 08:27:09.938954
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    # Placeholder, nothing after
    assert parser.parse(["--", ARGUMENT_PLACEHOLDER]) == parser._parser.parse_args([])
    # Placeholder, something after
    assert parser.parse(['cmd', 'arg1', 'arg2', '--', ARGUMENT_PLACEHOLDER, 'arg3', 'arg4']) == parser._parser.parse_args(['arg3', 'arg4', '--', 'cmd', 'arg1', 'arg2'])
    # Not placeholder, something after
    assert parser.parse(['cmd', 'arg1', 'arg2']) == parser._parser.parse_args(['--', 'cmd', 'arg1', 'arg2'])

# Generated at 2022-06-14 08:27:21.224323
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    """
    A trivial test of the function print_help of class Parser
    """
    import io
    import sys
    import os

    stdout_ = sys.stdout

    try:
        # To test output, we need to redirect the output to a string,
        # which we can then compare to the expected value.
        strio = io.StringIO()
        sys.stdout = strio

        parser = Parser()
        parser.print_help()
        strio.seek(0)
        actual = strio.read()
        assert actual

        # The output should include the word 'usage'
        expected = "usage"
        assert expected in actual

        # The output should include the word 'command'
        expected = 'command'
        assert expected in actual

    finally:
        #We have to reset the old output
        sys

# Generated at 2022-06-14 08:27:34.783984
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()

    # Adds arguments to parser.
    args = parser.parse([''])
    assert args.version is False

    # Adds arguments to parser.
    args = parser.parse([''])
    assert args.alias is None 

    # Adds arguments to parser.
    args = parser.parse([''])
    assert args.shell_logger is None

    # Adds arguments to parser.
    args = parser.parse([''])
    assert args.enable_experimental_instant_mode is False

    # Adds arguments to parser.
    args = parser.parse([''])
    assert args.help is False

    # _add_conflicting_arguments
    args = parser.parse([''])
    assert args.yes is False

    # _add_conflicting_arguments

# Generated at 2022-06-14 08:27:42.683678
# Unit test for method parse of class Parser
def test_Parser_parse():
    arguments = ['--debug',
                 '--force-command', 'crm -s',
                 '--',
                 'cd',
                 '/home/home/ome',
                 'cd',
                 '/root/root/oot',
                 'cd',
                 '/usr/usr/usr/usr',
                 'cd',
                 '/opt/opt/opt',
                 'cd',
                 ARGUMENT_PLACEHOLDER,
                 '/bin/bin/bin']
    assert Parser().parse(arguments) == \
        Parser()._parser.parse_args(Parser()._prepare_arguments(arguments[1:]))

# Generated at 2022-06-14 08:27:44.384818
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
   parser = Parser()
   parser.print_usage()


# Generated at 2022-06-14 08:27:47.288439
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    result = parser.parse([sys.argv[0], '-d'])
    assert result.debug is True


# Generated at 2022-06-14 08:29:28.008306
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    old_stderr = sys.stderr
    sys.stderr = stderr = StringIO()
    p = Parser()
    p.print_usage()
    sys.stderr = old_stderr
    assert 'usage: thefuck' == stderr.getvalue()[:16]


# Generated at 2022-06-14 08:29:36.900035
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse([
        'thefuck', 'git', 'remote', 'add', 'origin', 'git@github:nvbn/'
        'thefuck.git', ARGUMENT_PLACEHOLDER, 'sudo', '-v']) == \
        parser.parse([
            'sudo', '-v', 'thefuck', 'git', 'remote', 'add', 'origin',
            'git@github:nvbn/thefuck.git'])



# Generated at 2022-06-14 08:29:38.574156
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    assert p == p


# Generated at 2022-06-14 08:29:45.402422
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    with open("tests/help.txt") as help_file:
        parser.print_help()
        help_file.seek(0)
        assert help_file.read() == sys.stderr.getvalue()
        sys.stderr.truncate(0)
        sys.stderr.seek(0)

# Generated at 2022-06-14 08:29:50.301545
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    import sys
    import io
    buffer = io.StringIO()
    sys.stderr = buffer
    parser = Parser()
    parser.print_help()
    print(buffer.getvalue())
    return

if __name__ == '__main__':
    test_Parser_print_help()

# Generated at 2022-06-14 08:29:56.745747
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser=Parser()

# Generated at 2022-06-14 08:30:09.949891
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser.parse('fuck -v')
    assert parser.parse('fuck -a')
    assert parser.parse('fuck -l')
    assert parser.parse('fuck --enable-experimental-instant-mode')
    assert parser.parse('fuck -h')
    assert parser.parse('fuck -y')
    assert parser.parse('fuck -r')
    assert parser.parse('fuck -d')
    assert parser.parse('fuck --force-command')
    assert parser.parse('fuck')
    assert parser.parse('fuck -v -a -l --enable-experimental-instant-mode -h -y -r -d --force-command')


if __name__ == '__main__':
    parser = Parser()
    parser.parse('fuck -v -a')

# Generated at 2022-06-14 08:30:13.852745
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    """docstring for test_Parser_print_usage"""
    parser = Parser()
    parser.parse(['','-h'])
    # parser.print_usage()
    parser.print_help()

# Generated at 2022-06-14 08:30:17.485790
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser is not None

if __name__=="__main__":
    test_Parser()

# Generated at 2022-06-14 08:30:18.727722
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()