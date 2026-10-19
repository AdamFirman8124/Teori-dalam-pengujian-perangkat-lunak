

# Generated at 2022-06-14 08:21:02.985558
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    # Test with only argument "command"
    assert parser.parse(['fuck', 'foo', 'bar']) == parser._parser.parse_args(['foo', 'bar'])
    # Test with only argument "--help"
    assert parser.parse(['fuck', '--help']) == parser._parser.parse_args(['--help'])
    # Test with only argument "--version"
    assert parser.parse(['fuck', '--version']) == parser._parser.parse_args(['--version'])
    # Test with both "command" and "--help"
    assert parser.parse(['fuck', 'foo', 'bar', '--help']) == parser._parser.parse_args(['foo', 'bar', '--help'])
    # Test with one argument and one argument prefixed with "--

# Generated at 2022-06-14 08:21:04.232470
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()

# Generated at 2022-06-14 08:21:08.553021
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from contextlib import contextmanager
    from io import StringIO
    from thefuck.utils import capture
    from thefuck.parser import Parser

    p = Parser()
    p.parse(['hell'])
    with capture() as (out, _):
        p.print_usage()

    assert 'usage: thefuck' in out.getvalue()


# Generated at 2022-06-14 08:21:09.651308
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    assert callable(Parser.print_help.__func__)

# Generated at 2022-06-14 08:21:11.999414
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    p = Parser()
    p.print_help()


# Generated at 2022-06-14 08:21:13.111422
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert True

# Generated at 2022-06-14 08:21:15.808482
# Unit test for method parse of class Parser
def test_Parser_parse():
  args = Parser().parse(['thefuck', 'python', '-v'])
  assert args.command == ['python', '-v']

# Generated at 2022-06-14 08:21:22.555964
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    """
    This is a unit test for class Parser.
    """
    o_stdout = StringIO()
    o_stderr = StringIO()
    sys.stdout = o_stdout
    sys.stderr = o_stderr
    p = Parser()
    p.print_help()
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    help_string = o_stderr.getvalue()
    o_stdout.close()
    o_stderr.close()
    assert help_string.find('Usage:') >= 0

# Generated at 2022-06-14 08:21:35.131740
# Unit test for method parse of class Parser
def test_Parser_parse():
    # 1.1.
    parser = Parser()
    args = parser.parse(['program', 'arg'])
    assert args.command == ['arg']

    # 1.2
    args = parser.parse(['program', 'arg', 'lol'])
    assert args.command == ['arg', 'lol']

    # 2.1.
    args = parser.parse(['program', ARGUMENT_PLACEHOLDER, 'arg'])
    assert args.command == ['arg']

    # 2.2.
    args = parser.parse(['program', '-a', ARGUMENT_PLACEHOLDER, 'arg'])
    assert args.alias == True

    # 2.3.

# Generated at 2022-06-14 08:21:37.639959
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    try:
        parser.print_help()
    except SystemExit:
        pass

# Generated at 2022-06-14 08:21:47.396320
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert isinstance(parser, Parser)


# Generated at 2022-06-14 08:21:49.691492
# Unit test for method parse of class Parser
def test_Parser_parse():
    _Parser = Parser()
    _Parser.parse(["--enable-experimental-instant-mode"])


# Generated at 2022-06-14 08:21:56.230731
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser.prog == 'thefuck'
    assert parser._parser.add_help
    assert [arg.dest for arg in parser._parser._actions] == [
        'version', 'alias', 'shell_logger',
        'enable_experimental_instant_mode', 'help', 'yes', 'repeat', 'debug',
        'force_command', 'command']

# Generated at 2022-06-14 08:21:57.564149
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:22:11.301260
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    parser.parse(['-h']) == parser._parser.parse_args(['-h'])

    parser.parse(['-a', 'ls']) == parser._parser.parse_args(['-a', 'ls'])

    parser.parse(['-l', 'ls']) == parser._parser.parse_args(['-l', 'ls'])

    parser.parse(['-y', 'ls']) == parser._parser.parse_args(['-y', 'ls'])

    parser.parse(['-r', 'ls']) == parser._parser.parse_args(['-r', 'ls'])

    parser.parse(['ls']) == parser._parser.parse_args(['ls'])

    parser.parse(['-v', 'ls']) == parser._parser.parse_

# Generated at 2022-06-14 08:22:19.494806
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    mock_print_usage = mock.MagicMock()
    with mock.patch('sys.stderr', new=StringIO()) as mock_stderr:
        with mock.patch('argparse.ArgumentParser.print_usage',
                        new=mock_print_usage):
            parser = Parser()
            parser.print_usage()
            assert mock_print_usage.call_count == 1
            assert mock_print_usage.call_args[0] == (mock_stderr,)


# Generated at 2022-06-14 08:22:26.808488
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(['thefuck'])
    assert args == (
        parser._parser.parse_args(['--', 'thefuck']))
    args = parser.parse(['thefuck', 'ls'])
    assert args == (
        parser._parser.parse_args(['--', 'ls']))
    args = parser.parse(['thefuck', 'ls', '-l'])
    assert args == (
        parser._parser.parse_args(['--', 'ls', '-l']))
    args = parser.parse(['thefuck', 'ls', '-la', '-h'])
    assert args == (
        parser._parser.parse_args(['--', 'ls', '-la', '-h']))

# Generated at 2022-06-14 08:22:30.720244
# Unit test for constructor of class Parser
def test_Parser():
    # Given a Parser class
    parser = Parser()

    # When I call parse method with
    # Then I should get
    assert isinstance(parser.parse(['', '--debug']), argparse.Namespace)

# Generated at 2022-06-14 08:22:32.844188
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from io import StringIO
    output = StringIO()
    sys.stdout = output
    Parser().print_help()
    output.getvalue()

# Generated at 2022-06-14 08:22:33.844396
# Unit test for constructor of class Parser
def test_Parser():
    Parser()


# Generated at 2022-06-14 08:22:43.379686
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    asser

# Generated at 2022-06-14 08:22:50.658848
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    import io
    import sys

    sys.stdout = io.StringIO()
    parser = Parser()
    parser.print_help()
    string = sys.stdout.getvalue()
    sys.stdout.close()

    assert 'usage: thefuck' in string
    assert 'optional arguments:' in string
    assert '[custom-alias-name] prints alias for current shell' in string

# Generated at 2022-06-14 08:22:58.163190
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    p = Parser()
    ouptut = sys.stderr.getvalue()
    assert ouptut == "usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER]\n                 [--enable-experimental-instant-mode]\n                 [-y | -r] [-d] [--force-command FORCE_COMMAND] [--]\n                 [command [command ...]]\n"

# Generated at 2022-06-14 08:22:59.552700
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()


# Generated at 2022-06-14 08:23:11.396492
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from .utils import capture_output
    from .utils import patch_stdout
    from .utils import patch_stderr
    from sys import stderr
    with capture_output() as (stout_, sterr_):
        parser = Parser()
        parser.print_usage()
        assert sterr_.getvalue() == "usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l shell-logger]\n                  [--enable-experimental-instant-mode] [-y] [-r]\n                  [-d] [--force-command force-command]\n                  [command [command ...]]\n"


# Generated at 2022-06-14 08:23:19.434381
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()

    # 1. 'thefuck' should return default values.
    assert parser.parse(['thefuck']) == parser._parser.parse_args([])

    # 2. 'thefuck command' should return parsed 'command'.
    assert parser.parse(['thefuck', 'command']) == parser._parser.parse_args(['command'])

    # 3. 'thefuck command --custom-option' should return added '--' and
    #    parsed 'command'.
    assert parser.parse(
        ['thefuck', 'command', '--custom-option']) == parser._parser.parse_args(
        ['--', 'command', '--custom-option'])

    # 4. 'thefuck command --custom-option extra arguments' should return added
    #    '--' and parsed 'command' and '--custom-option

# Generated at 2022-06-14 08:23:21.278455
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser is not None

# Generated at 2022-06-14 08:23:22.966163
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:23:25.622384
# Unit test for constructor of class Parser
def test_Parser():
    # On instanciation, we should have a `ArgumentParser` object.
    assert isinstance(Parser(), ArgumentParser)


# Generated at 2022-06-14 08:23:27.324622
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    assert parser.print_usage() == None

# Generated at 2022-06-14 08:23:49.294240
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    import io
    import sys
    import re

    class Capturing(list):
        def __enter__(self):
            self._stdout = sys.stdout
            sys.stdout = self._stringio = io.StringIO()
            return self

        def __exit__(self, *args):
            self.extend(self._stringio.getvalue().splitlines())
            del self._stringio
            sys.stdout = self._stdout

    with Capturing() as output:
        Parser().print_help()
    # check for the usage
    assert re.search(r'usage: thefuck', output[0])
    # check for the positional arguments
    assert re.search(r'positional arguments:', output[2])

# Generated at 2022-06-14 08:23:50.632299
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()


# Generated at 2022-06-14 08:23:54.709883
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(['script', '-y', 'ls', '-l'])
    assert args.yes == True
    assert args.command == ['ls', '-l']

# Generated at 2022-06-14 08:23:57.235948
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    try:
        parser = Parser()
        helper = parser.print_help()
    except:
        assert False
    assert True

# Generated at 2022-06-14 08:23:58.344162
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser()



# Generated at 2022-06-14 08:24:06.384474
# Unit test for method parse of class Parser
def test_Parser_parse():
    from .const import ARGUMENT_PLACEHOLDER, DEFAULT_ALIAS

    # Case1: command should be fixed
    # Case1.1: alias is 'fuck'
    args = Parser().parse(['thefuck', 'echo fuck'])
    assert args.command == ['echo', 'fuck']
    assert not args.debug
    assert not args.yes
    assert not args.repeat
    assert args.alias is None
    assert args.version is None
    assert args.shell_logger is None

    assert Parser().parse(['thefuck', 'pwd']).command == ['pwd']
    assert Parser().parse(['thefuck', 'man', 'fuck']).command == [
        'man', 'fuck']

    # Case1.2: alias is 'fuck' and --yes flag is True

# Generated at 2022-06-14 08:24:09.257890
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()


# print_help is a function so it cannot be tested as a method

# Generated at 2022-06-14 08:24:17.305847
# Unit test for constructor of class Parser
def test_Parser():
    from .utils import get_alias
    parser = Parser()
    _add_arguments(parser)
    _add_conflicting_arguments(self)
    _prepare_arguments(self, argv=['-v', '-a', '-h', '-d'])
    parse(self, argv=['-v', '-a'])
    print_usage(self)
    print_help(self)


# Generated at 2022-06-14 08:24:19.826694
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser.prog == 'thefuck'
    assert parser._parser.add_help is False


# Generated at 2022-06-14 08:24:30.698127
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from .utils import is_func_called, reset_called_funcs
    import sys

    reset_called_funcs()

    parser = Parser()
    parser.print_usage()

    assert sys.stderr.getvalue() == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-d] [--force-command FORCE_COMMAND] [--] command ...\n'
    assert 'ArgumentParser.print_usage' in is_func_called()
    assert is_func_called().get('ArgumentParser.print_usage') == 1


# Generated at 2022-06-14 08:25:12.345127
# Unit test for method parse of class Parser
def test_Parser_parse():
    p = Parser()
    args = p.parse(['thefuck', '-y', 'ls'])
    assert args.yes
    assert args.command == ['ls']

    args = p.parse(['thefuck', '-r', 'ls', 'al'])
    assert args.repeat
    assert args.command == ['ls', 'al']

    args = p.parse(['thefuck', 'ls', 'al'])
    assert not args.repeat
    assert not args.yes
    assert args.command == ['ls', 'al']

    args = p.parse(['thefuck', 'ls', 'al', '-a'])
    assert not args.repeat
    assert not args.yes
    assert args.command == ['ls', 'al', '-a']


# Generated at 2022-06-14 08:25:14.190833
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.parse([])
    parser.print_help()

# Generated at 2022-06-14 08:25:18.817825
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()

    parser.parse([])
    parser.print_usage()
    sys.stderr.getvalue().strip().endswith('usage: thefuck [-h] [-v]\n')


# Generated at 2022-06-14 08:25:20.123533
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    assert p is not None

# Generated at 2022-06-14 08:25:27.243225
# Unit test for method parse of class Parser
def test_Parser_parse():
    assert Parser().parse(['thefuck']) == Namespace(
            alias=None,
            command=[],
            debug=False,
            enable_experimental_instant_mode=False,
            help=False,
            repeat=False,
            shell_logger=None,
            version=False,
            yes=False,
            force_command=None)


# Generated at 2022-06-14 08:25:28.891238
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()

# Generated at 2022-06-14 08:25:41.442425
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    assert parser.parse(['<script>', '-l', 'thefuck.log', 'cd']) == parser.parse(['<script>', 'cd'])
    assert parser.parse(['<script>', ARGUMENT_PLACEHOLDER, '-l', 'thefuck.log', 'cd']) == parser.parse(['<script>', 'cd', '-l', 'thefuck.log'])
    assert parser.parse(['<script>', '--alias', 'tgf', 'cd']) == parser.parse(['<script>', 'cd', '--alias', 'tgf'])

# Generated at 2022-06-14 08:25:49.485207
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    output = sys.stderr
    # outputs:
    # usage: thefuck [-h] [-v] [-l SHELL_LOGGER] [-d] [-y] [-r]
    #                [--enable-experimental-instant-mode]
    #                [--force-command FORCE_COMMAND] [--] [command [command ...]]
    #
    # optional arguments:
    #   -h, --help            show this help message and exit
    #   -v, --version         show program's version number and exit
    #   -l SHELL_LOGGER, --shell-logger SHELL_LOGGER
    #                         log shell output to the file
    #   -d, --debug           enable debug output
    #   -y, --yes, --yeah, --hard
    #                         execute fixed

# Generated at 2022-06-14 08:25:56.674292
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    sys.argv = []
    parser = Parser()
    parser.print_usage()
    assert sys.stderr.getvalue() == "usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l shell-logger] [--enable-experimental-instant-mode] [-y | -r] [--force-command force-command] [command [command ...]]\n"


# Generated at 2022-06-14 08:26:05.887317
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(['fuck', 'git', 'commit', '-a'])
    assert args.command == ['git', 'commit', '-a']
    args = parser.parse(['fuck', '^',
                         'git', 'commit', '-a'])
    assert args.command == ['git', 'commit', '-a']
    args = parser.parse(['fuck', 'fuck',
                         'git', 'commit', '-a'])
    assert args.command == ['fuck', 'git', 'commit', '-a']
    args = parser.parse(['fuck', 'fuck', '-d',
                         'git', 'commit', '-a'])
    assert args.command == ['fuck', 'git', 'commit', '-a']

# Generated at 2022-06-14 08:27:13.786267
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    p = Parser()
    p.print_help()

    assert True

# Generated at 2022-06-14 08:27:15.414323
# Unit test for method parse of class Parser
def test_Parser_parse():
        parser = Parser()
        parser.parse(['--yeah'])

# Generated at 2022-06-14 08:27:25.744219
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    with patch('sys.stderr') as stderr:
        parser.print_help()
        stderr.write.assert_any_call('')
        #stderr.write.assert_any_call('usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER]\n')
        #stderr.write.assert_any_call('              [-y] [-r] [-d] [--force-command FORCE_COMMAND]\n')
        #stderr.write.assert_any_call('              [command [command ...]]\n')
        #stderr.write.assert_any_call('')


# Generated at 2022-06-14 08:27:27.577077
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:27:32.648136
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from mock import patch

    with patch('sys.stderr.write') as stderr_write:
        Parser().print_usage()

    assert stderr_write.call_args[0][0].startswith('usage:')


# Generated at 2022-06-14 08:27:41.000790
# Unit test for method parse of class Parser
def test_Parser_parse():
  parser = Parser()
  def run_test(inp, exp):
    obs = parser.parse(inp)
    assert_equal(obs,exp)
  inps = [['fuck','--force-command','ls -la'],
          ['fuck','--shell-logger','--force-command','ls -la']]

# Generated at 2022-06-14 08:27:49.172070
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from six import StringIO
    import sys
    from .parser import Parser

    stdout = sys.stderr
    sys.stderr = StringIO()
    parser = Parser()
    parser.print_usage()
    sys.stderr.seek(0)
    out = sys.stderr.read()
    sys.stderr = stdout
    assert 'usage' in out
    assert 'prog' in out
    assert 'tf' in out
    assert '--' in out


# Generated at 2022-06-14 08:27:52.109802
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    with patch('sys.stderr') as stderr:
        Parser().print_help()
    assert stderr.write.called


# Generated at 2022-06-14 08:27:53.753192
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()


# Generated at 2022-06-14 08:27:55.182965
# Unit test for constructor of class Parser
def test_Parser():

    parser = Parser()

    assert parser._parser.prog == 'thefuck'


# Generated at 2022-06-14 08:30:35.673336
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()
    # TODO: test that parser.print_usage() prints to sys.stderr



# Generated at 2022-06-14 08:30:45.076488
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    buffer = StringIO()
    sys.stderr = buffer
    parser.print_usage()
    output = buffer.getvalue().strip()
    assert output == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]]' \
            ' [-l SHELL_LOGGER] [--enable-experimental-instant-mode]' \
            ' [-y | -r] [-d] [--force-command FORCE_COMMAND] command [command ...]'
