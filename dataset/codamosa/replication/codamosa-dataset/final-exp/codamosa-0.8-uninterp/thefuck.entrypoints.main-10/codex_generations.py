

# Generated at 2022-06-14 08:53:48.432404
# Unit test for function main
def test_main():
    import os
    import sys
    import io
    from .alias import print_alias as mock_print_alias
    from .fix_command import fix_command as mock_fix_command
    from ..utils import get_installation_info as mock_get_installation_info
    from ..system import init_output
    from ..executors.git import Git
    from ..executors.fasd import Fasd
    from ..executors.mac_utils import MacUtils
    from ..executors.shell import Shell
    from ..executors.pip import Pip
    from ..executors.apt import Apt
    from ..executors.yarn import Yarn
    from ..executors.heroku import Heroku
    from ..executors.opsgenie import Opsgenie

# Generated at 2022-06-14 08:53:50.072818
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:53:53.718554
# Unit test for function main
def test_main():
    parser = Parser()
    known_args = parser.parse([])
    assert(isinstance(known_args, argparse.Namespace))

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:53:56.702209
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:53:57.279801
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:54:07.994217
# Unit test for function main
def test_main():
    import argparse

    def _test(args, expected):
        sys.argv = ['thefuck'] + args
        parser = Parser()
        known_args = parser.parse(sys.argv)

        if isinstance(expected, Exception):
            with pytest.raises(expected):
                main()
        else:
            main()
            assert known_args == expected

    _test(['--help'], argparse.ArgumentParser)
    _test(['--version'], None)
    _test(['--alias', 'fuck'], {'alias': ['fuck'],
                                'command': None,
                                'help': False,
                                'man': False,
                                'version': False})

# Generated at 2022-06-14 08:54:10.883306
# Unit test for function main
def test_main():
    assert main == "python3 main.py" or "python main.py"

# Generated at 2022-06-14 08:54:16.924864
# Unit test for function main
def test_main():
    import os
    os.environ['TF_HISTORY'] = 'true'
    known_args = Parser().parse(['', ''])
    assert fix_command(known_args) is not None
    os.environ['TF_HISTORY'] = ''


if __name__ == '__main__':
    sys.exit(main())

# Generated at 2022-06-14 08:54:17.874477
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-14 08:54:20.436196
# Unit test for function main
def test_main(): 
    sys.argv[1:] = ["--version","-v","--alias","--help","--shell-logger"]
    main()

# Generated at 2022-06-14 08:54:29.041421
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:54:40.619963
# Unit test for function main
def test_main():
    from unittest.mock import patch

    with patch('sys.argv', ['thefuck']):
        from .main import main
        from .parser import Parser
        from .alias import print_alias
        from .fix_command import fix_command

        with patch.object(Parser, 'parse') as mock_parse:
            with patch.object(Parser, 'print_help') as mock_print_help:
                with patch.object(Parser, 'print_usage') as mock_print_usage:
                    with patch.object(print_alias, 'print_alias') as mock_print_alias:
                        with patch.object(fix_command, 'fix_command') as mock_fix_command:
                            main()
                            # Checking the main function
                            mock_parse.assert_called_once()
                            mock_print_help

# Generated at 2022-06-14 08:54:41.893916
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-14 08:54:45.773271
# Unit test for function main
def test_main():
    try:
        main()
    except KeyboardInterrupt as e:
        print("Cannot test main function. KeyboardInterrupt exception thrown")
        print("Error: " + str(e))

# Generated at 2022-06-14 08:54:47.038944
# Unit test for function main
def test_main():
    from . import main
    assert main is not None

# Generated at 2022-06-14 08:54:58.388959
# Unit test for function main
def test_main():
    from test.shells import MockHistory, MockArgumentParser, MockLogs
    from test.utils import SuppressStdoutAndStderr

    with SuppressStdoutAndStderr():
        history = MockHistory()
        logs = MockLogs()
        parser = MockArgumentParser()
        sys.argv = ['thefuck']
        main()
        assert 'usage' in logs._out
        assert not history._out
        assert not parser._out
        history._out = ''
        logs._out = ''
        parser._out = ''

        sys.argv = ['thefuck', 'command']
        main()
        assert 'correct' in logs._out
        assert 'command' in history._out
        assert not parser._out
        history._out = ''
        logs._out = ''
        parser._out = ''

       

# Generated at 2022-06-14 08:55:01.971385
# Unit test for function main
def test_main():
    """
    Check if main function work correctly.
    """
    try:
        main()
    except SystemExit:
        pass
    except KeyboardInterrupt:
        pass

# Generated at 2022-06-14 08:55:04.126294
# Unit test for function main
def test_main():
    pass
# Test: python3 -m pytest test/unit/test_main.py

# Generated at 2022-06-14 08:55:14.293886
# Unit test for function main
def test_main():
    from io import StringIO
    from unittest.mock import patch
    # Patch fake output for unit test
    with patch('sys.stdout', new=StringIO()) as fake_output:
        with patch.object(sys, 'argv', ["thefuck", "--help"]):
            main()
            assert fake_output.getvalue() != ''
        with patch.object(sys, 'argv', ["thefuck", "--version"]):
            main()
            assert fake_output.getvalue() != ''
        with patch.object(sys, 'argv', ["thefuck", "--alias"]):
            main()
            assert fake_output.getvalue() != ''
        with patch.object(sys, 'argv', ["thefuck", "--shell-logger"]):
            main()
            assert fake_output.getvalue()

# Generated at 2022-06-14 08:55:34.879158
# Unit test for function main
def test_main():
    import thefuck.main as mn
    import argparse
    import sys
    mn.sys = sys
    mn.sys.argv = ['thefuck']
    mn.logs.version = 'version'
    mn.logs.warn = 'warn'
    mn.print_alias = 'print_alias'
    mn.fix_command = 'fix_command'
    mn.sys.argv = ['thefuck', '--help']
    mn.main()
    mn.sys.argv = ['thefuck', '--version']
    mn.main()
    mn.sys.argv = ['thefuck', '--alias']
    mn.main()
    mn.sys.argv = ['thefuck', '--shell-logger']
    mn.main()
   

# Generated at 2022-06-14 08:56:03.108651
# Unit test for function main
def test_main():
    parser = Parser()
    known_args, unknown_args = parser.parse_known_args(['-h'])
    assert known_args.help == True
    known_args, unknown_args = parser.parse_known_args(['--help'])
    assert known_args.help == True
    known_args, unknown_args = parser.parse_known_args(['-v'])
    assert known_args.version == True
    known_args, unknown_args = parser.parse_known_args(['--version'])
    assert known_args.version == True
    known_args, unknown_args = parser.parse_known_args(['--alias', 'debug'])
    assert known_args.alias == 'debug'

# Generated at 2022-06-14 08:56:03.733324
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:56:16.103938
# Unit test for function main
def test_main():

    try:
        from shell import Shell
    except ImportError:
        pass

    import os
    import sys
    import logging

    # check help
    sys.argv = ['thefuck', '--help']
    main()

    # check version
    sys.argv = ['thefuck', '--version']
    main()

    # check alias
    sys.argv = ['thefuck', '--alias']
    main()
    sys.argv = ['thefuck', '--alias', 'alias']
    main()

    # check fix command
    sys.argv = ['thefuck', '--command', 'command']
    main()

    os.environ['TF_HISTORY'] = 'history'
    main()

    # check shell logger
    sys.argv = ['thefuck', '--shell-logger']
    main

# Generated at 2022-06-14 08:56:28.667222
# Unit test for function main
def test_main():
    # import sys
    from unittest.mock import patch, Mock
    
    m_sys = Mock()
    m_sys.argv = ['thefuck','--help']
    with patch('thefuck.main.sys',m_sys):
        with patch('thefuck.main.Parser.parse'):
            with patch('thefuck.main.Parser.print_help') as m_print_help:
                with patch('thefuck.main.print_alias'):
                    with patch('thefuck.main.fix_command'):
                        with patch('thefuck.main.Parser.print_usage'):
                            main()
                            m_print_help.assert_called()

# Generated at 2022-06-14 08:56:29.468561
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-14 08:56:29.856497
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-14 08:56:31.315577
# Unit test for function main
def test_main():
    sys.argv = ['','-version']
    main()

# Generated at 2022-06-14 08:56:32.344904
# Unit test for function main
def test_main():
    pass


# Generated at 2022-06-14 08:56:34.243719
# Unit test for function main
def test_main():
    parser = Parser()
    kwargs = parser.parse(sys.argv)
    assert main() == None

# Generated at 2022-06-14 08:56:40.161115
# Unit test for function main
def test_main():
    with init_testing_logger(logs):
        # Call main
        main()

        # Call to version
        from ..utils import get_installation_info
        from .. import logs
        logs.version(get_installation_info().version,
                     sys.version.split()[0], shell.info())

# Generated at 2022-06-14 08:57:12.684508
# Unit test for function main
def test_main():
    try:
        main()
    except SystemExit:
        pass

# Generated at 2022-06-14 08:57:13.609940
# Unit test for function main
def test_main():
	assert main() == None

# Generated at 2022-06-14 08:57:14.292546
# Unit test for function main
def test_main():
    import thefuck.cmd

# Generated at 2022-06-14 08:57:26.286198
# Unit test for function main
def test_main():
    from io import StringIO
    from unittest.mock import patch
    from .shells import DEFAULT_SHELL

    with patch('sys.stdout', new=StringIO()) as fake_out:
        with patch('sys.argv', ['thefuck', '--version']):
            main()
            assert 'Python 3.6.1' in fake_out.getvalue()
            assert 'Bash 4.3.46' in fake_out.getvalue()

    with patch('sys.stdout', new=StringIO()) as fake_out:
        with patch('sys.argv', ['thefuck', '--shell-logger']):
            main()
            assert fake_out.getvalue().endswith(
                'thefuck -v --shell-logger {}\n'.format(DEFAULT_SHELL))


# Generated at 2022-06-14 08:57:36.499844
# Unit test for function main
def test_main():
    from ..system import init_output
    init_output()
    from .. import logs
    logger=logs.logger
    assert logger.level == 10
    #test for help
    from . import main
    try:
        sys.argv.append('--help')
        main()
    except SystemExit:
        assert True
    else:
        assert False
    #test for version
    from .. import get_installation_info
    from . import main
    from . import version
    try:
        sys.argv.append('--version')
        main()
    except SystemExit:
        assert True
    else:
        assert False
    #test for command or 'TF_HISTORY' in os.environ
    from . import main

# Generated at 2022-06-14 08:57:41.920601
# Unit test for function main
def test_main():
    # Test for parser
    assert Parser().parse(sys.argv) is not None

    # Test for main
    try:
        main()
    except:  # noqa: E722
        assert False

test_main()

# Generated at 2022-06-14 08:57:44.147285
# Unit test for function main
def test_main():
    assert main() != "help"
    assert main() != "version"

# Generated at 2022-06-14 08:57:45.670109
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:58:01.177584
# Unit test for function main
def test_main():
    from unittest.mock import patch, PropertyMock
    from ..arguments import Command, Options, Arguments
    from ..system import Shell, FakePath
    from ..types import CommandName

    sys.argv = ['thefuck']
    parser = Parser()
    arguments = parser.parse(sys.argv)

# Generated at 2022-06-14 08:58:02.661124
# Unit test for function main
def test_main():
    if __name__ == "__main__":
        main()

# Generated at 2022-06-14 08:59:17.001567
# Unit test for function main
def test_main():
    sys.argv[1:] = 'cmd --help'.split()
    main()
    sys.argv[1:] = '--version'.split()
    main()
    sys.argv[1:] = '-a zsh'.split()
    main()
    sys.argv[1:] = 'cmd --no-colors'.split()
    main()
    sys.argv[1:] = '--shell-logger'.split()
    main()
    # Error
    sys.argv[1:] = '-a non-existing-shell'.split()
    sys.exit = lambda arg: arg
    main()

# Generated at 2022-06-14 08:59:18.508369
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:59:19.545189
# Unit test for function main
def test_main():
    assert main == main

# Generated at 2022-06-14 08:59:27.101371
# Unit test for function main
def test_main():
    import sys
    import argparse
    argv = sys.argv
    sys.argv = ['thefuck']
    main()
    sys.argv = ['thefuck', '--help']
    main()
    sys.argv = ['thefuck', '--version']
    main()
    sys.argv = ['thefuck', '--alias']
    main()
    sys.argv = ['thefuck', '--shell-logger']
    main()
    sys.argv = ['thefuck', 'ls', '-al']
    main()
    sys.argv = argv

# Generated at 2022-06-14 08:59:36.889469
# Unit test for function main
def test_main():
    import unittest.mock as mock
    import unittest
    import sys
    from ..utils import get_installation_info
    from ..argument_parser import Parser
    from ..system import init_output
    from ..shells import shell
    from .alias import print_alias
    from .fix_command import fix_command
    from .shell_logger import shell_logger

    class TestMain(unittest.TestCase):
        def setUp(self):
            self.parser = mock.patch('thefuck.main.Parser').start()
            self.parser.return_value = self.parser
            self.parse = mock.patch.object(self.parser, 'parse').start()
            self.print_usage = mock.patch.object(self.parser, 'print_usage').start()

# Generated at 2022-06-14 08:59:37.891657
# Unit test for function main
def test_main():
    assert main(['fuck']) == None

# Generated at 2022-06-14 08:59:40.059819
# Unit test for function main
def test_main():
    try:
        sys.argv = ['thefuck']
        main()
    except SystemExit:
        pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:59:49.884977
# Unit test for function main
def test_main():
    import sys
    import thefuck
    sys.argv = ['thefuck', '--version']  # noqa: E402
    main()
    sys.argv = ['thefuck', '--shell']  # noqa: E402
    main()
    sys.argv = ['thefuck', '--alias', 'f']  # noqa: E402
    main()
    sys.argv = ['thefuck', 'cd', '~']  # noqa: E402
    main()
    sys.argv = ['thefuck']  # noqa: E402
    main()

# Generated at 2022-06-14 08:59:58.441890
# Unit test for function main
def test_main():

    # Testing help option
    sys.argv = ['thefuck','--help']
    main()

    # Testing alias option
    sys.argv = ['thefuck','--alias','fuck']
    main()

    # Testing shell_logger option
    sys.argv = ['thefuck','--shell-logger']
    main()

    # Testing version option
    sys.argv = ['thefuck','--version']
    main()

# Generated at 2022-06-14 08:59:59.200324
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 09:02:23.279230
# Unit test for function main
def test_main():
    for function_name in ['Parser', 'get_installation_info']:
        sys.modules['thefuck.argument_parser'].__dict__[function_name] = Mock(
            return_value=Mock(
                parse=Mock(return_value=Mock(help=False, version=False, alias=False, command=None, shell_logger=False)),
                print_help=Mock(),
                print_usage=Mock()))

    main()

    assert sys.modules['thefuck.argument_parser'].__dict__['Parser'].called
    assert sys.modules['thefuck.argument_parser'].__dict__['Parser'].return_value.parse.called
    assert sys.modules['thefuck.argument_parser'].__dict__['Parser'].return_value.print_usage.called


# Generated at 2022-06-14 09:02:34.816868
# Unit test for function main
def test_main():
    from unittest.mock import Mock

    from .alias import print_alias as _print_alias
    from .fix_command import fix_command as _fix_command
    from .shell_logger import shell_logger as _shell_logger

    old_print_alias = print_alias
    old_fix_command = fix_command
    old_shell_logger = shell_logger

    old_argv = sys.argv
    old_environ = os.environ.copy()
    old_parser_stdout = sys.stdout
    old_parser_stderr = sys.stderr
    old_args = Parser().parse


# Generated at 2022-06-14 09:02:38.328875
# Unit test for function main
def test_main():
    # Before anything else, initialize colorama.
    init_output()
    
    # Set up args
    sys.argv = ['ignore','-v']
    
    # Execute function
    main()


# Generated at 2022-06-14 09:02:45.080689
# Unit test for function main
def test_main():
    sys.argv = ["thefuck","--help"]
    main()
    parser = Parser()
    assert(parser.parse_args(["thefuck","--help"]).help==True)
    assert(parser.parse_args(["thefuck","--version"]).version==True)
    assert(parser.parse_args(["thefuck","--alias","fuck"]).alias=="fuck")

# Generated at 2022-06-14 09:02:57.142031
# Unit test for function main
def test_main():
    from .test_argument_parser import MockParser
    from .test_shells import MockShell

    def restore_shell():
        from ..shells import is_shell_supported, get_shell

        is_shell_supported.cache_clear()
        get_shell.cache_clear()

    restore_shell()
    parser = MockParser()
    known_args = parser.parse(sys.argv)
    shell._shell = MockShell()
    assert main.__code__.co_argcount == 0

    #if help:
    try:
        main()
    except SystemExit:
        assert parser.help == True

    #if version:
    known_args.version = True
    version = get_installation_info().version

# Generated at 2022-06-14 09:02:57.840291
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 09:03:00.011009
# Unit test for function main
def test_main():
    sys.argv.append('-v')
    main()
    sys.argv.remove('-v')

# Generated at 2022-06-14 09:03:00.753928
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 09:03:04.317873
# Unit test for function main
def test_main():
    logs.version = lambda x, y, z: x
    try:
        main()
    except SystemExit as e:
        return e.args[0]


# Generated at 2022-06-14 09:03:17.231063
# Unit test for function main
def test_main():
    from .... import system  # noqa: E402
    from .... import __version__  # noqa: E402
    from .alias import print_alias  # noqa: E402
    from .fix_command import fix_command  # noqa: E402
    from unittest.mock import MagicMock, patch  # noqa: E402

    sys.argv = ['thefuck']
    assert main() == None
    
    sys.argv = ['thefuck', '--help']
    with patch('thefuck.main.Parser') as mock_parser:
        mock_parser.return_value.parse.return_value = None

        main()
        mock_parser.return_value.print_help.assert_called_once()

    sys.argv = ['thefuck', '--version']