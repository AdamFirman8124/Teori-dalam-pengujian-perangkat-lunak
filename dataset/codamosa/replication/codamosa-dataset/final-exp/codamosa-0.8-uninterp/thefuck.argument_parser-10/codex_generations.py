

# Generated at 2022-06-14 08:20:50.072009
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    assert parser.print_usage() == None

# Generated at 2022-06-14 08:21:00.799005
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(['#!', 'ls', '-a', '-l'])
    assert args.command == ['ls', '-a', '-l']
    args2 = parser.parse(['#!', 'ls', ARGUMENT_PLACEHOLDER, '-a', '-l'])
    assert args2.command == ['-a', '-l', 'ls']
    args3 = parser.parse(['#!', '--help'])
    assert args3.help

    class Args(object):
        pass

    class Parser(object):
        def parse_args(self, argv):
            args = Args()
            args.command = argv
            return args

    parser = Parser()

# Generated at 2022-06-14 08:21:03.291799
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    if not parser:
        raise AssertionError("Parser is not initiated.")

# Generated at 2022-06-14 08:21:06.080172
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    code = parser.print_help(file=open(os.devnull, 'w'))
    assert code == None

# Generated at 2022-06-14 08:21:13.123332
# Unit test for method parse of class Parser
def test_Parser_parse():
    p = Parser()
    # When '{}' does not exist
    assert p._prepare_arguments(['-h']) == ['-h']
    # When '{}' exists
    assert p._prepare_arguments(['-h','aaa','{}','bbb','ccc']) == ['bbb','ccc','--','-h','aaa']
test_Parser_parse()


# Generated at 2022-06-14 08:21:16.215421
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    instance = Parser()
    instance.print_help()

if __name__ == '__main__':
    test_Parser_print_help()

# Generated at 2022-06-14 08:21:23.835172
# Unit test for method parse of class Parser
def test_Parser_parse():
    ParserResult = namedtuple('ParserResult', 'args command debug debug_logger enable_experimental_instant_mode force_command help help_arg repeat shell_logger version')
    args = ParserResult(args=[], command = [], debug = None, debug_logger = None, enable_experimental_instant_mode = None, force_command = None, help = None, help_arg = None, repeat = None, shell_logger = None, version = None)
    parser = Parser()

    assert parser.parse(['--help']) == args._replace(args = ['--help'], help = True)
    assert parser.parse(['--help-arg']) == args._replace(args = ['--help-arg'], help_arg = True)

# Generated at 2022-06-14 08:21:33.240628
# Unit test for method parse of class Parser
def test_Parser_parse():
    from .utils import get_alias
    from .const import ARGUMENT_PLACEHOLDER

    test_args = '-a --debug --force-command ls -h'.split(' ')

    fake_args = test_args[:]
    fake_args.append(ARGUMENT_PLACEHOLDER)
    args = Parser().parse(fake_args)

    assert args.alias == get_alias()
    assert args.debug
    assert args.force_command == 'ls'
    assert args.help
    assert not args.repeat
    assert not args.yes

# Generated at 2022-06-14 08:21:40.752055
# Unit test for constructor of class Parser
def test_Parser():
    """ Unit test for constructor of class Parser
    """
    parser = Parser()
    assert parser._parser.description == 'Argument parser that can handle arguments with our special placeholder.'
    assert parser._parser._prog == 'thefuck'
    assert parser._parser._actions[0].option_strings == ['-v', '--version']
    assert parser._parser._actions[0].type == 'store_true'
    assert parser._parser._actions[0].dest == 'version'
    assert parser._parser._actions[0].default == False
    assert parser._parser._actions[0].help == "show program's version number and exit"
    assert parser._parser._actions[1].option_strings == ['-a', '--alias']
    assert parser._parser._actions[1].type == 'store'

# Generated at 2022-06-14 08:21:50.436475
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    """Unit test for the method print_usage of class Parser"""
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    test_parser = Parser()
    test_parser.print_usage()
    assert capturedOutput.getvalue() == "usage: thefuck [-h] [-v] [-a [custom-alias-name]]\n              [-l SHELL_LOGGER] [--enable-experimental-instant-mode]\n              [-d] [--force-command FORCE_COMMAND]\n              [-- [command [command ...]]]\n"
    capturedOutput.close()
    sys.stdout = sys.__stdout__


# Generated at 2022-06-14 08:22:00.807474
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser != None

# Generated at 2022-06-14 08:22:13.009646
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(['thefuck', '--version'])
    assert args.version
    assert not args.debug
    assert not args.alias

    args = parser.parse(['thefuck', '--alias', 'fuck'])
    assert args.alias
    assert not args.version
    assert not args.debug
    assert args.alias == 'fuck'

    args = parser.parse(['thefuck', '--debug'])
    assert args.debug
    assert not args.version
    assert not args.alias

    args = parser.parse(['thefuck', '--help'])
    assert args.help
    assert not args.version
    assert not args.debug
    assert not args.alias

    args = parser.parse(['thefuck', 'pip3', 'install', 'requests'])

# Generated at 2022-06-14 08:22:16.490634
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    assert p is not None
    assert p._parser is not None
    assert p._parser.prog == 'thefuck'
    assert p._parser.add_help == False


# Generated at 2022-06-14 08:22:17.722779
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    Parser().print_usage()

# Generated at 2022-06-14 08:22:18.894388
# Unit test for constructor of class Parser
def test_Parser():
    Parser()


# Generated at 2022-06-14 08:22:31.625862
# Unit test for constructor of class Parser
def test_Parser():
    from thefuck.const import ARGUMENT_PLACEHOLDER
    from thefuck.utils import get_alias
    class TestParser(Parser):
        def test_init(self):
            parser = Parser()
            assert parser._parser.prog == 'thefuck'

        def test_add_arguments(self):
            args = [
                '-v', '--version',
                '-a', '--alias', 'a',
                '-l', '--shell-logger', 'logger',
                '--enable-experimental-instant-mode',
                '-h', '--help',
                '-y', '-r',
                '-d', '--debug',
                '--force-command', '-l',
                'a', '-a']
            parser = Parser()
            parser._

# Generated at 2022-06-14 08:22:34.386468
# Unit test for method parse of class Parser
def test_Parser_parse():
    _test_Parser_parse__test_prepare_arguments_with_placeholder()
    _test_Parser_parse__test_prepare_arguments_without_placeholder()


# Generated at 2022-06-14 08:22:38.330793
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from io import StringIO
    f = StringIO()
    parser = Parser()
    parser.print_usage(file=f)
    assert f.getvalue() == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-d] [--force-command FORCE_COMMAND] [-y] [-r] [--] [command [command ...]]\n'


# Generated at 2022-06-14 08:22:44.956550
# Unit test for constructor of class Parser
def test_Parser():
    def test_add_arguments(mocker):
        mocker.patch('argparse.ArgumentParser')
        mocker.patch.object(Parser, '_add_arguments')
        Parser()
        Parser._add_arguments.assert_called_once_with()
    # test whether we call _add_arguments in constructor
    test_add_arguments(mocker.patch('thefuck.shells.base.get_alias'))


# Generated at 2022-06-14 08:22:47.538256
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser is not None


# Generated at 2022-06-14 08:23:07.678163
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert(parser!=None)

# Generated at 2022-06-14 08:23:19.270985
# Unit test for method parse of class Parser
def test_Parser_parse():
    # get a new parser object
    parserObj = Parser()

    # this is a valid argument
    args = parserObj.parse(['-a'])
    assert args.alias == get_alias()

    # this is a valid argument
    args = parserObj.parse(['-a', 'fuck'])
    assert args.alias == 'fuck'

    # this is a valid argument
    args = parserObj.parse(['--alias=fuck'])
    assert args.alias == 'fuck'

    # this will trigger the default value
    args = parserObj.parse([])
    assert args.alias == get_alias()

    # this is a valid argument
    args = parserObj.parse(['-l', 'test.log'])
    assert args.shell_logger == 'test.log'

    # these are two valid argument
   

# Generated at 2022-06-14 08:23:24.470299
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    # Disable console output
    sys.stderr = open(os.devnull, 'w')
    parser.print_usage()
    # Enable console output
    sys.stderr = sys.__stderr__


# Generated at 2022-06-14 08:23:35.387560
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser.prog == 'thefuck' # Add arguments
    assert parser._parser.add_help == False
    assert isinstance(parser._parser._actions[0], argparse._VersionAction) # _add_arguments
    assert parser._parser._actions[1].nargs == '?'
    assert parser._parser._actions[2].action == 'store'
    assert parser._parser._actions[3].action == 'store_true'
    assert parser._parser._actions[4].action == 'store_true'
    assert parser._parser._actions[5].action == 'store_true'
    assert parser._parser._mutually_exclusive_groups[0]._group_actions[0].action == 'store_true'

# Generated at 2022-06-14 08:23:37.139338
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()
    assert isinstance(p, Parser)



# Generated at 2022-06-14 08:23:38.347311
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser()


# Generated at 2022-06-14 08:23:41.311572
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser.prog == 'thefuck'
    assert parser._parser.add_help == False



# Generated at 2022-06-14 08:23:45.212278
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(['command', 'arg1', 'arg2', '--', 'asd'])
    assert args.command == ['arg1', 'arg2']


# Generated at 2022-06-14 08:23:54.972125
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from . import utils
    with utils.mock.patch('sys.stderr') as sys_mock:
        Parser().print_usage()
    sys_mock.write.assert_has_calls([
        utils.mock.call('usage: thefuck [-h] [-v] [-a [custom-alias-name]]\n'
                        '               [-l shell-logger]\n'
                        '               [--enable-experimental-instant-mode]\n'
                        '               [-y] [-r] [-d] [--force-command FORCE_COMMAND]\n'
                        '               [command [command ...]]\n'),
        utils.mock.call('\n')])


# Generated at 2022-06-14 08:24:04.923593
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args_1 = parser.parse([])
    assert args_1.help == False
    assert args_1.shell_logger == None
    assert args_1.debug == False
    assert args_1.command == []
    assert args_1.repeat == False
    assert args_1.yes == False
    assert args_1.enable_experimental_instant_mode == False
    assert args_1.force_command == None
    assert args_1.alias == None
    assert args_1.version == False
    args_2 = parser.parse([parser.placeholder, 'fuck'])
    assert args_2.command == ['fuck']
    assert args_2.shell_logger == None
    assert args_2.debug == False
    assert args_2.repeat == False
    assert args_

# Generated at 2022-06-14 08:24:41.905697
# Unit test for constructor of class Parser
def test_Parser():
    p = Parser()

# Generated at 2022-06-14 08:24:47.294816
# Unit test for method parse of class Parser
def test_Parser_parse():
    p = Parser()
    args=p.parse(['thefuck',"-v"])
    assert args.version
    args=p.parse(['thefuck',"--force-command"])
    assert args.force_command is None

# Generated at 2022-06-14 08:24:49.022185
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser is not None


# Generated at 2022-06-14 08:24:58.262616
# Unit test for method parse of class Parser
def test_Parser_parse():
    p = Parser()
    sys.argv = ['thefuck', 'git', 'push']
    assert p.parse(sys.argv).command == ['git', 'push']
    sys.argv = ['thefuck', 'git', 'push', 'origin', 'master']
    assert p.parse(sys.argv).command == ['git', 'push', 'origin', 'master']
    sys.argv = ['thefuck', ARGUMENT_PLACEHOLDER, 'git', 'push']
    assert p.parse(sys.argv).command == ['git', 'push']
    sys.argv = ['thefuck', ARGUMENT_PLACEHOLDER, 'git', 'push', 'origin', 'master']

# Generated at 2022-06-14 08:24:58.969287
# Unit test for constructor of class Parser
def test_Parser():
    assert Parser().__class__ is Parser

# Generated at 2022-06-14 08:25:02.573570
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    stdout=sys.stdout
    sys.stdout = stdout_ = io.StringIO()
    try:
        parser = Parser()
        parser.print_help()
        sys.stdout.flush()
        stdout_.getvalue().find('show this help message and exit')>=0
    finally:
        sys.stdout = stdout

# Generated at 2022-06-14 08:25:09.174649
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    import io
    import sys
    help_str = io.StringIO()
    sys.stdout = help_str
    if sys.version_info[0] == 2:
        sys.stdout = io.BytesIO()
    parser = Parser()
    parser.print_usage()
    sys.stdout = sys.__stdout__
    assert help_str.getvalue().strip() == 'usage: thefuck [-h] [-v] [-a [custom-alias-name]] [-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-d] [--force-command FORCE_COMMAND] [-y | -r] [command [command ...]]'



# Generated at 2022-06-14 08:25:11.093286
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser is not None


# Generated at 2022-06-14 08:25:12.498436
# Unit test for constructor of class Parser
def test_Parser():
    test = Parser()
    assert test

# Generated at 2022-06-14 08:25:19.334728
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    test_args = ['--debug', 'command', '--', '--debug', '--force-command=ls', '--', '--debug']
    result_args = parser._prepare_arguments(test_args)
    cmd_args = parser._parser.parse_args(result_args)
    parser.print_help()

# Generated at 2022-06-14 08:26:11.488717
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:26:12.209662
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    parser.print_usage()

# Generated at 2022-06-14 08:26:13.576559
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:26:19.486954
# Unit test for method parse of class Parser
def test_Parser_parse():
    class ParserMock(Parser):
        def __init__(self):
            self._parser = mock.Mock(spec=ArgumentParser)
            self._parser.parse_args.return_value = 'parsed'

    assert ParserMock().parse(['thefuck', 'args', 'here']) == 'parsed'
    ParserMock()._parser.parse_args.assert_called_once_with(['args', 'here'])



# Generated at 2022-06-14 08:26:21.680323
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parser = Parser()
    parser.print_help()


# Generated at 2022-06-14 08:26:22.960688
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    parse = Parser()
    parse.print_help()

# Generated at 2022-06-14 08:26:24.985493
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser.__class__.__name__ == 'Parser'

# Generated at 2022-06-14 08:26:26.575469
# Unit test for constructor of class Parser
def test_Parser():
    Parser()


# Generated at 2022-06-14 08:26:31.422638
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    with patch('argparse.ArgumentParser.print_help') as mocked_print_help:
        parser = Parser()
        parser.print_help()
        mocked_print_help.assert_called_with(sys.stderr)


# Generated at 2022-06-14 08:26:43.265417
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from StringIO import StringIO
    from StringIO import StringIO
    from contextlib import contextmanager

    original_stderr = sys.stderr
    sys.stderr = StringIO()
    parser = Parser()

    try:
        parser.print_usage()
        assert sys.stderr.getvalue() == 'usage: thefuck [-v] [-a [custom-alias-name]] [-l shell-logger] [--enable-experimental-instant-mode] [-h] [-d] [-y | -r] [--force-command force-command] [--] [command ...]\n'
    finally:
        sys.stderr = original_stderr

# Generated at 2022-06-14 08:28:11.295202
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from StringIO import StringIO
    from .main import VERSION
    capture_stdout = StringIO()
    sys.stdout, old_stdout = capture_stdout, sys.stdout
    capture_stderr = StringIO()
    sys.stderr, old_stderr = capture_stderr, sys.stderr
    parser = Parser()
    parser.print_help()

# Generated at 2022-06-14 08:28:15.560285
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    result = Parser()
    if result.print_usage():
        print('test_Parser_print_usage succeed')
    else:
        print('test_Parser_print_usage failed')


# Generated at 2022-06-14 08:28:20.746673
# Unit test for constructor of class Parser
def test_Parser():
    parser = Parser()
    assert parser._parser.prog == 'thefuck'
    assert not parser._parser.add_help
    groups = [group for group in parser._parser._action_groups
              if group.title == 'optional arguments']
    assert len(groups) == 1
    assert parser._parser.description is None


# Generated at 2022-06-14 08:28:29.877394
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    from StringIO import StringIO
    import sys
    backup = sys.stderr
    try:
        out = StringIO()
        sys.stderr = out
        Parser().print_usage()
        output = out.getvalue().strip()
        assert output == ('usage: thefuck [-h] [-v] [-a [custom-alias-name]] '
                          '[-l SHELL_LOGGER] [--enable-experimental-instant-mode] [-d] [-y] [-r] [--force-command FORCE-COMMAND] [command [command ...]]')
    finally:
        sys.stde

# Generated at 2022-06-14 08:28:41.239843
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    from io import StringIO
    from unittest.mock import patch
    from thefuck.parser import Parser

    parser = Parser()

    stdout = StringIO()
    stderr = StringIO()
    with patch('sys.stderr', stderr):
        parser.print_help()
    assert u'usage: thefuck [-' in stderr.getvalue()

    stderr = StringIO()
    with patch('sys.stderr', stderr):
        parser.print_usage()
    assert u'usage: thefuck [-' in stderr.getvalue()

# Generated at 2022-06-14 08:28:43.989042
# Unit test for constructor of class Parser
def test_Parser():
  try:
    p = Parser()
  except Exception as e:
    print(e)

# Generated at 2022-06-14 08:28:45.538019
# Unit test for constructor of class Parser
def test_Parser():
    Parser()


# Generated at 2022-06-14 08:28:54.217302
# Unit test for method parse of class Parser
def test_Parser_parse():
    parser = Parser()
    args = parser.parse(['thefuck'])
    assert args.command == []
    assert args.debug is False
    assert args.enable_experimental_instant_mode is False
    assert args.repeat is False
    assert args.yes is False
    assert args.help is False

    args = parser.parse(['thefuck', 'ls', '-l'])
    assert args.command == ['ls', '-l']
    assert args.debug is False

    args = parser.parse(['thefuck', 'ls', '-l', ARGUMENT_PLACEHOLDER, '-la'])
    assert args.command == ['ls', '-l']
    assert args.debug is False


# Generated at 2022-06-14 08:29:05.487315
# Unit test for method print_help of class Parser
def test_Parser_print_help():
    # Arrange
    import sys
    from io import StringIO
    from unittest.mock import patch
    from thefuck.main import main
    from thefuck.const import VERSION

    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        # Act
        main(['--help'])
        output = mock_stdout.getvalue()
        # Assert

# Generated at 2022-06-14 08:29:07.587765
# Unit test for method print_usage of class Parser
def test_Parser_print_usage():
    parser = Parser()
    assert parser.print_usage() != None
