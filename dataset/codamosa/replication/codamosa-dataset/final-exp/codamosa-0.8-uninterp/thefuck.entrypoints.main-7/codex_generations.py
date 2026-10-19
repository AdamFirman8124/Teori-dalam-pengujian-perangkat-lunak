

# Generated at 2022-06-14 08:53:35.258645
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:53:47.564642
# Unit test for function main
def test_main():
    from .fix_command import get_new_command
    import argparse
    import unittest
    import sys
    import os
    class TestMain(unittest.TestCase):
        def test_help(self):
            with self.assertRaises(SystemExit) as cm:
                main()
            self.assertEqual(cm.exception.code, 0)

        def test_version(self):
            sys.argv.append('--version')
            with self.assertRaises(SystemExit) as cm:
                main()
            self.assertEqual(cm.exception.code, 0)
            sys.argv.remove('--version')

        def test_alias(self):
            sys.argv.append('-a')
            with self.assertRaises(SystemExit) as cm:
                main()


# Generated at 2022-06-14 08:53:55.563032
# Unit test for function main
def test_main():
    # Test if the help message is displayed when '--help' is given as an argument
    from io import StringIO
    from unittest.mock import patch
    import thefuck
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    with patch.object(sys, 'argv', [thefuck.__file__, '--help']):
        main()
        sys.stdout = sys.__stdout__
        assert('usage: ' in capturedOutput.getvalue())

    # Test if the version is displayed when '--version' is given as an argument
    capturedOutput = StringIO()
    sys.stdout = capturedOutput
    with patch.object(sys, 'argv', [thefuck.__file__, '--version']):
        main()
        sys.stdout = sys.__stdout__

# Generated at 2022-06-14 08:53:56.701959
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:54:10.518860
# Unit test for function main
def test_main():
    from unittest.mock import MagicMock # noqa: E402

    # Unit test for case `known_args.help`
    parser = MagicMock()
    known_args = MagicMock()
    known_args.help = True
    known_args.version = False
    known_args.alias = False
    known_args.command = False
    globals()['parser'] = parser
    globals()['known_args'] = known_args
    main()
    parser.print_help.assert_called_once_with()

    # Unit test for case `known_args.version`
    parser = MagicMock()
    known_args = MagicMock()
    known_args.help = False
    known_args.version = True
    known_args.alias = False
    known_args.command = False


# Generated at 2022-06-14 08:54:11.750329
# Unit test for function main
def test_main():
    assert "Unknown command" in main()


# Generated at 2022-06-14 08:54:14.044281
# Unit test for function main
def test_main():
    parser = Parser()
    known_args = parser.parse(['fuck', '--help'])
    main()

# Generated at 2022-06-14 08:54:17.052405
# Unit test for function main
def test_main():
    with patch('sys.argv', ['thefuck', '    ']):
        main()
    assert True

test_main()

# Generated at 2022-06-14 08:54:18.916358
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:54:26.702345
# Unit test for function main
def test_main():
    from subprocess import check_output, call
    from unittest.mock import patch

    main()
    main()
    main()
    main()
    main()

    for _ in ['git config --global alias.doesnt-matter',
              'git config --global alias.fuck=!f() { TF_SHELL=fish thefuck $@; }; f',
              'fish -c "set -Ux TF_SHELL fish"',
              'fuck']:
        assert call(['bash', '-c', _]) == 0

    assert 'TF_SHELL=fish' in check_output(['bash', '-c', 'env'])
    assert 'TF_SHELL=fish' in check_output(['fish', '-c', 'env'])


# Generated at 2022-06-14 08:54:42.417635
# Unit test for function main
def test_main():
    # Setup
    import argparse

    argparse.ArgumentParser = MockArgumentParser
    MockArgumentParser.parse = MockParse
    MockParse.return_value = Namespace(help=False, version=False,
                                       alias=False, rule=None, \
                                       command=None, settings=None, \
                                       conf_file=None)

    # Mocks
    from unittest.mock import patch

    with patch('os.environ', {'TF_HISTORY': 'true'}):
        with patch('sys.argv', ['exe', '--help']):
            main()
            assert MockArgumentParser.args == ['exe', '--help']


# Generated at 2022-06-14 08:54:47.983473
# Unit test for function main
def test_main():
    error_count = 0
    print()
    logs.info('Testing main function')
    from .utils import make_arguments
    from .utils import clear_history
    from . import utils
    from .utils import get_history_id

    print()
    logs.info('Testing for help')
    args = make_arguments('fuck')
    try:
        main()
    except SystemExit as e:
        error_count += 1 if e.code != 0 else 0
    os.system('fuck --help')
    print()
    logs.info('Testing for clear_history')
    clear_history()
    history_id = get_history_id()
    print()
    logs.info('Testing for command')
    args = make_arguments('fuck cd', 'alias fuck="cd $1"')

# Generated at 2022-06-14 08:54:48.749712
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:54:59.331906
# Unit test for function main

# Generated at 2022-06-14 08:55:00.483395
# Unit test for function main
def test_main():
    assert sys.argv[0] == 'thefuck'

# Generated at 2022-06-14 08:55:01.129118
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:55:13.390598
# Unit test for function main
def test_main():
    from io import StringIO
    from unittest.mock import patch, MagicMock
    from . import main

    parser_mock = MagicMock()
    parser_mock.print_help.side_effect = SystemExit
    parser_mock.print_usage.side_effect = SystemExit

    with patch('thefuck.command_line.Parser', return_value=parser_mock):
        with patch.object(sys, 'argv', ['thefuck']):
            with self.assertRaises(SystemExit):
                main()
        with patch.object(sys, 'argv', ['thefuck', '--help']):
            with self.assertRaises(SystemExit):
                main()

# Generated at 2022-06-14 08:55:21.819298
# Unit test for function main
def test_main():
    import os

    environ = os.environ.copy()

    def clean():
        os.environ = environ

    def run_main(args):
        os.environ = environ
        os.environ['TF_HISTORY'] = 'this is a unit test'
        main(args)

    try:
        run_main(['--version'])
        run_main(['--help'])
        run_main(['--shell-logger'])
    finally:
        clean()

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:55:24.760163
# Unit test for function main
def test_main():
    assert main() == None


# Generated at 2022-06-14 08:55:37.266417
# Unit test for function main
def test_main():
    import os
    from .alias import print_alias
    from .fix_command import fix_command
    from .parser import Parser
    from .shell_logger import shell_logger
    from unittest import mock

    parser = mock.create_autospec(Parser)
    parser.parse.return_value = mock.MagicMock(
        help=False, version=False, alias=None, command=None,
        shell_logger=None,
    )

# Generated at 2022-06-14 08:56:00.879706
# Unit test for function main
def test_main():
    '''Unit test for main()'''
    # Mock output
    import io
    sys.stdout = io.StringIO()
    sys.stderr = io.StringIO()
    # Mock arguments
    sys.argv[1] = '--alias'
    main()
    # main() should print alias
    assert 'fuck = thefuck' in sys.stdout.getvalue()

# Generated at 2022-06-14 08:56:04.854077
# Unit test for function main
def test_main():
    import subprocess
    out = subprocess.check_output(
        ['python3', '-m', 'thefuck.cli.main'],
        stderr=subprocess.STDOUT
    ).decode('utf-8')  # type: bytes
    assert 'The Fuck 3.2' in out


if __name__ == "__main__":
    main()

# Generated at 2022-06-14 08:56:05.593175
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:56:06.231560
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:56:14.666986
# Unit test for function main
def test_main():
    print("Test case 1")
    print(main())
    print("Test case 2")
    print(main())
    print("Test case 3")
    print(main())
    print("Test case 4")
    print(main())
    print("Test case 5")
    print(main())

if __name__ == '__main__':
    # Unit test for function main
    test_main()
    
    main()

#if __name__ == '__main__':
#    main()

# Generated at 2022-06-14 08:56:21.291769
# Unit test for function main
def test_main():
    import subprocess
    proc = subprocess.Popen(["python3", "./thefuck/main.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    assert proc.returncode == 0

# Generated at 2022-06-14 08:56:28.550816
# Unit test for function main
def test_main():
    class FakeArgs():
        def __init__(self):
            self.help = False
            self.version = False
            self.alias = False         
    args = FakeArgs()
    #args.help = True
    #args.version = True
    #args.alias = True
    os.environ['TF_HISTORY'] = ''
    try:
        main()
    except:
        print('All tests are passed.')



# Generated at 2022-06-14 08:56:30.366918
# Unit test for function main
def test_main():
    assert main() == None

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:56:38.317510
# Unit test for function main
def test_main():
    with mock.patch.object(sys, 'argv', ['thefuck']):
        with mock.patch('thefuck.argument_parser.Parser.print_usage'):
            main()
    with mock.patch.object(sys, 'argv', ['thefuck', '--version']):
        with mock.patch('thefuck.logs.version'):
            main()
    with mock.patch.object(sys, 'argv', ['thefuck', '--help']):
        with mock.patch('thefuck.argument_parser.Parser.print_help'):
            main()
    with mock.patch.object(sys, 'argv', ['thefuck', '--alias', 'ls']):
        with mock.patch('thefuck.alias.print_alias'):
            main()

# Generated at 2022-06-14 08:56:53.681092
# Unit test for function main
def test_main():
    from click.testing import CliRunner
    from ..argument_parser import Parser
    from io import StringIO
    import os
    import re

    release_version = get_installation_info().version
    parser = Parser()
    runner = CliRunner()

    @runner.invoke(parser.parse, ['--help'])
    def test_help():
        assert result.exit_code == 0
        assert parser.print_help() in result.output

    @runner.invoke(parser.parse, ['--version'])
    def test_version():
        assert result.exit_code == 0
        assert release_version in result.output

    @runner.invoke(parser.parse, ['--alias'])
    def test_alias():
        assert result.exit_code == 0

# Generated at 2022-06-14 08:57:26.876511
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:57:27.654322
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:57:28.811354
# Unit test for function main
def test_main():
    main()
    assert True

# Generated at 2022-06-14 08:57:30.770015
# Unit test for function main
def test_main():
    parser = Parser()
    sys.argv = ['--help']
    main()

test_main()

# Generated at 2022-06-14 08:57:34.105343
# Unit test for function main
def test_main():
    os.environ['TF_HISTORY'] ='I like tests'
    main()
    assert os.environ.get('TF_HISTORY') == None

# Generated at 2022-06-14 08:57:40.766391
# Unit test for function main
def test_main():
    import sys
    import os
    import pytest
    # alias
    assert main() == print_alias(known_args)
    # version
    assert main() == logs.version(get_installation_info().version,
                     sys.version.split()[0], shell.info())
    # command
    assert main() == fix_command(known_args)
    # shell_logger
    assert main() == shell_logger(parser.shell_logger)

# Generated at 2022-06-14 08:57:45.051212
# Unit test for function main
def test_main():
    main()
if __name__ == "__main__":
    test_main()

# Generated at 2022-06-14 08:57:45.847128
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:58:01.339690
# Unit test for function main
def test_main():
    assert sys.argv[0] == "thefuck"
    sys.argv[1] = 'fuck'
    assert sys.argv[1] == 'fuck'
    sys.argv = ['thefuck', '--help']
    assert sys.argv[1] == '--help'
    sys.argv = ['thefuck', '--version']
    assert sys.argv[1] == '--version'
    sys.argv = ['thefuck', '--shell-logger']
    assert sys.argv[1] == '--shell-logger'
    sys.argv = ['thefuck', '--alias']
    assert sys.argv[1] == '--alias'
    sys.argv = ['thefuck', 'fuck']
    assert sys.argv[1] == 'fuck'

# Generated at 2022-06-14 08:58:01.983679
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-14 08:59:07.154943
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-14 08:59:11.889826
# Unit test for function main
def test_main():
    from unittest.mock import MagicMock
    from fuck import version
    main()
    logs.version.assert_called_with(version.__version__, '3.7.4', 'zsh')

# Generated at 2022-06-14 08:59:13.019851
# Unit test for function main
def test_main():
    assert (main()) == None

# Generated at 2022-06-14 08:59:22.430837
# Unit test for function main
def test_main():
    with patch('sys.exit') as sys_exit:
        with patch('thefuck.argument_parser.Parser') as parser_class:
            parser = MagicMock()
            parser_class.return_value = parser
            parser.parse.return_value.help = True
            parser.parse.return_value.version = False
            parser.parse.return_value.shell_logger = None
            parser.parse.return_value.alias = None
            parser.parse.return_value.command = None
            main()
        parser.print_help.assert_called_once_with()
        parser_class.assert_called_once_with()
        parser.parse.assert_called_once_with(sys.argv)
        assert not sys_exit.called

# Generated at 2022-06-14 08:59:34.848156
# Unit test for function main
def test_main():
    sys.argv = []
    main()
    assert logs.is_version_printed() is True
    assert logs.is_usage_printed() is True
    assert logs.is_help_printed() is False
    assert logs.is_alias_printed() is False
    assert logs.is_debug_enabled() is False

    sys.argv = ['-v']
    main()
    assert logs.is_version_printed() is True
    assert logs.is_usage_printed() is False
    assert logs.is_help_printed() is False
    assert logs.is_alias_printed() is False
    assert logs.is_debug_enabled() is False

    sys.argv = ['-h']
    main()
    assert logs.is_version_printed() is False
    assert logs.is_usage_printed() is False
   

# Generated at 2022-06-14 08:59:44.354541
# Unit test for function main
def test_main():
    from unittest.mock import patch

    main_str = main.__name__
    with patch(main_str + '.Parser') as mock_parser:
        mock_parser.return_value.parse.return_value.help = False
        mock_parser.return_value.parse.return_value.version = False
        mock_parser.return_value.parse.return_value.alias = False
        mock_parser.return_value.parse.return_value.shell_logger = False
        main()

        assert mock_parser.return_value.print_usage.call_count == 1
        assert mock_parser.return_value.print_help.call_count == 0

    with patch(main_str + '.Parser') as mock_parser:
        mock_parser.return_value.parse.return_value.help = True
       

# Generated at 2022-06-14 08:59:50.537530
# Unit test for function main
def test_main():
    import subprocess as sub
    import tempfile
    filename = tempfile.mktemp()

    sub.call("thefuck --version > " + filename, shell = True)

    file = open(filename, "r")
    test_version = file.read()
    file.close()

    assert "thefuck version" in test_version
    assert "Python version" in test_version
    assert "Shell version" in test_version

# Generated at 2022-06-14 08:59:58.082730
# Unit test for function main
def test_main():
    # Arrange
    parser = Parser()
    known_args = parser.parse(sys.argv)
    # Act
    main()
    # Assert
    # As there is no assert statement, the test will pass if main runs without
    # throwing an exception.
    # I would have tested the `known_args` but that would require changing the
    # input depending on the OS and I am not sure how to do that yet.
    # To test the `known_args` the `init_output()` function would also have to
    # be tested.

# Generated at 2022-06-14 09:00:08.846595
# Unit test for function main

# Generated at 2022-06-14 09:00:09.699016
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 09:02:35.405931
# Unit test for function main
def test_main():
    from unittest.mock import Mock, patch, mock_open, mock_open
    from unittest.mock import MagicMock
    from unittest import TestCase

    @patch('sys.argv', new=['thefuck', '-h'])
    def test_parser_print_help(capsys):
        main()
        captured = capsys.readouterr()
        assert 'Usage' in captured.out


# Generated at 2022-06-14 09:02:36.108438
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 09:02:38.377407
# Unit test for function main
def test_main():
    args = ['thefuck', '--version']
    main()

if __name__ == '__main__':  # pragma: no cover
    main()

# Generated at 2022-06-14 09:02:53.019464
# Unit test for function main
def test_main():
    # Print help and version
    sys.argv = ['tf', '-h']
    main()
    sys.argv = ['tf', '--help']
    main()
    sys.argv = ['tf', '-v']
    main()
    sys.argv = ['tf', '--version']
    main()

    # Print alias
    sys.argv = ['tf', 'alias', 'bash']
    main()

    # Only check if `TF_HISTORY` in `os.environ`.
    sys.argv = ['tf']
    os.environ['TF_HISTORY'] = '10'
    main()

    # Check if `-c` in `command`
    sys.argv = ['tf', '-c', 'echo']
    main()

    # Check `shell_logger`
    sys

# Generated at 2022-06-14 09:02:54.096469
# Unit test for function main
def test_main():
    assert main == main


# Generated at 2022-06-14 09:03:02.396444
# Unit test for function main
def test_main():
    from . import alias, fix_command
    temp = sys.argv
    sys.argv = [sys.argv[0], '--version']
    try:
        main()
    finally:
        sys.argv = temp
        logs.output.clear()

    temp = sys.argv
    sys.argv = [sys.argv[0], '--help']
    try:
        main()
    finally:
        sys.argv = temp
        logs.output.clear()


# Generated at 2022-06-14 09:03:07.071133
# Unit test for function main
def test_main():
    try:
        sys.argv = ['thefuck', '--version']
        assert main() is None
    except AssertionError:
        assert False

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 09:03:08.864839
# Unit test for function main
def test_main():

    parser = Parser()
    args = parser.parse(['-v'])
    assert args.version == True

# Generated at 2022-06-14 09:03:09.670792
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-14 09:03:10.305293
# Unit test for function main
def test_main():
    assert main() == None