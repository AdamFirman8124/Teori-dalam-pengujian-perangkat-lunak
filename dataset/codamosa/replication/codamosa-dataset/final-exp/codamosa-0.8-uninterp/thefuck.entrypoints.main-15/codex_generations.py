

# Generated at 2022-06-14 08:53:42.257447
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:53:53.339088
# Unit test for function main
def test_main():
    from .alias import print_alias  # noqa: E402
    from .fix_command import fix_command  # noqa: E402
    from ..system import init_output
    init_output()

    with patch('sys.argv', [__file__,'--help']):
        with patch('..argument_parser.Parser.parse', return_value=namedtuple('Args', 'help')):
            with patch('..argument_parser.Parser.print_help'):
                main()

    with patch('sys.argv', [__file__,'--version']):
        with patch('..argument_parser.Parser.parse', return_value=namedtuple('Args', 'version')):
            with patch('..logs.version'):
                main()


# Generated at 2022-06-14 08:54:06.569557
# Unit test for function main
def test_main():
    # Test for `parser.print_usage()`
    with patch('builtins.print') as print_mock:
        main()
        print_mock.assert_called_once_with('Usage: thefuck [OPTIONS] COMMAND\nTry "thefuck --help" for help.')

    # Test for `print_alias()`
    with patch('thefuck.main.print_alias') as mock_print_alias:
        with patch('thefuck.main.Parser') as mock_parser:
            mock_parser.return_value.parse.return_value = namedtuple(
                'args', 'command alias')(None, True)
            main()
            assert mock_print_alias.called

    # Test for `os.environ['TF_HISTORY']`

# Generated at 2022-06-14 08:54:09.655200
# Unit test for function main
def test_main():
    # No input, no output
    result = main()
    assert result == None

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:54:11.197893
# Unit test for function main
def test_main():
    # Test main function
    main()

# Generated at 2022-06-14 08:54:15.516078
# Unit test for function main
def test_main():
    """
    Test function for main function
    """
    assert main() == 'No command or alias is passed'
    assert main() == 'Usage: thefuck [OPTIONS] COMMAND'
    assert main() == 'shit: command not found'

# Generated at 2022-06-14 08:54:25.607812
# Unit test for function main
def test_main():
    parser = Parser()
    known_args = parser.parse(sys.argv)

    if known_args.help:
        parser.print_help()
    elif known_args.version:
        logs.version(get_installation_info().version,
                     sys.version.split()[0], shell.info())
    # It's important to check if an alias is being requested before checking if
    # `TF_HISTORY` is in `os.environ`, otherwise it might mess with subshells.
    # Check https://github.com/nvbn/thefuck/issues/921 for reference
    elif known_args.alias:
        print_alias(known_args)
    elif known_args.command or 'TF_HISTORY' in os.environ:
        fix_command(known_args)

# Generated at 2022-06-14 08:54:37.247294
# Unit test for function main
def test_main():
    os.environ.pop('TF_HISTORY')
    with patch('sys.argv', ['thefuck', '-v']):
        with patch('thefuck.logs.version') as version:
            main()
            version.assert_called_with(get_installation_info().version,
                                       sys.version.split()[0], shell.info())

    with patch('sys.argv', ['thefuck', '-h']):
        with patch('thefuck.argument_parser.Parser.print_help') as print_help:
            main()
            print_help.assert_called_with()

    with patch('sys.argv', ['thefuck', '--alias', 'fuck']):
        with patch('thefuck.logs.log') as log:
            main()

# Generated at 2022-06-14 08:54:43.066511
# Unit test for function main
def test_main():
    from .shell_logger import shell_logger
    from ..utils import test_output
    from ..system import reset_settings, init_settings
    from ..shells import get_shell

    def reset():
        reset_settings()
        init_settings()
        init_output()

    reset()
    
    def test_shell_logger(shell):
        with test_output() as (stdout, stderr):
            shell_logger(shell)
        assert stderr.getvalue() == 'Only work with linux now\n'

    test_shell_logger('csh')
    test_shell_logger('fish')
    reset()
    test_shell_logger('tcsh')
    reset()

    with test_output() as (stdout, stderr):
        main()

# Generated at 2022-06-14 08:54:43.803571
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:55:01.020892
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-14 08:55:02.062188
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-14 08:55:05.312904
# Unit test for function main
def test_main():
    # Mock sys.argv
    sys.argv = ['thefuck']
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:55:14.682345
# Unit test for function main
def test_main():
    from unittest.mock import patch
    from ..system import get_alias
    with patch('sys.argv', ['thefuck', '--alias']):
        main()
        get_alias()
    with patch('sys.argv', ['thefuck', '--alias', 'fuck']):
        main()
        get_alias(name='fuck')
    with patch('sys.argv', ['thefuck', '--version']):
        main()
    with patch('sys.argv', ['thefuck', '--shell', 'zsh']):
        main()
    with patch('sys.argv', ['thefuck', '--shell', 'fish']):
        main()
    with patch('sys.argv', ['thefuck', '--shell', 'bash']):
        main()

# Generated at 2022-06-14 08:55:20.519961
# Unit test for function main
def test_main():
    import argparse
    argparse.ArgumentParser.parse_args = lambda self: None
    assert main() == None

# Generated at 2022-06-14 08:55:25.474864
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:55:27.447541
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-14 08:55:29.297646
# Unit test for function main
def test_main():
    main()

if __name__ == "__main__":
    main()

# Generated at 2022-06-14 08:55:30.068164
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-14 08:55:43.147801
# Unit test for function main
def test_main():
    class MyParser(object):
        def parse(self, arguments):
            self.arguments = arguments
            return self

        def print_help(self):
            self.help_called = True

        def print_usage(self):
            self.usage_called = True

    parser = MyParser()

    original_print_alias = __builtins__['print']
    original_logs_version = logs.version

    alias_called = False

    def print_alias(known_args):
        nonlocal alias_called
        alias_called = True

    logs_version_called = False

    def logs_version(version, python_version, shell_info):
        nonlocal logs_version_called
        logs_version_called = True

    __builtins__['print'] = print_alias
    logs.version = logs_version

    known

# Generated at 2022-06-14 08:56:10.384603
# Unit test for function main
def test_main():
    get_installation_info().version = 'thefuck 3.11 dev'
    logs.version = lambda version, python, shell: (
        'thefuck 3.11 dev, Python 3.5.2, '
        'Bash 4.3.42(1)-release (x86_64-apple-darwin15.6.0)'
    )
    logs.warn = lambda msg: msg
    sys.argv = ['thefuck', '--version']
    main() == 'thefuck 3.11 dev, Python 3.5.2, '\
              'Bash 4.3.42(1)-release (x86_64-apple-darwin15.6.0)'
    sys.argv = ['thefuck']
    main() == None

# Generated at 2022-06-14 08:56:11.505671
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:56:12.118665
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:56:13.625739
# Unit test for function main
def test_main():
    assert main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:56:14.229114
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-14 08:56:28.198143
# Unit test for function main
def test_main():
    # Step 1: Test --version
    sys.argv = ['tf', '--version']
    main()
    assert '/Users/Amithash/anaconda3/bin/python3.5' in sys.stdout.getvalue()
    # Step 2: Test --help
    sys.stdout.truncate(0)
    sys.argv = ['tf', '--help']
    main()
    assert 'usage: tf [-h]' in sys.stdout.getvalue()
    # Step 3: Test --shell-logger
    sys.stdout.truncate(0)
    sys.argv = ['tf', '--shell-logger']
    main()
    assert 'usage: tf [-h]' in sys.stdout.getvalue()

# Generated at 2022-06-14 08:56:30.180799
# Unit test for function main
def test_main():
    assert main() == 'Usage: thefuck [OPTIONS] COMMAND'

# Generated at 2022-06-14 08:56:30.859486
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:56:38.417937
# Unit test for function main
def test_main():
    # The function `main` will print the help message if argument `--help` is specified
    def test_help():
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        assert 'Show this message and exit.' in captured_output.getvalue()
    
    # The function `main` will print the version information if argument `--version` is specified
    def test_version():
        captured_output = io.StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        assert 'The Fuck {}, Python {}'.format(__version__, sys.version.split()[0]) in captured_output.getvalue()
    
    # The function `main` will print the shell

# Generated at 2022-06-14 08:56:48.554068
# Unit test for function main
def test_main():
    from ..system import init_output
    assert callable(init_output)

    from os import environ
    assert callable(environ)

    from ..argument_parser import Parser
    assert callable(Parser)

    from ..utils import get_installation_info
    assert callable(get_installation_info)

    from ..shells import shell
    assert callable(shell)

    from .alias import print_alias
    assert callable(print_alias)

    from .fix_command import fix_command
    assert callable(fix_command)
    assert callable(main)
    #main()
    #print(main)

# Generated at 2022-06-14 08:57:21.152296
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:57:33.698193
# Unit test for function main
def test_main():
    import unittest  # noqa: E402
    def test_parser():
        import argparse  # noqa: E402
        class MockParser(argparse.ArgumentParser):
            def __init__(self, *args):
                self.called = False
                super(MockParser, self).__init__(*args)

            def parse_known_args(self, *args, **kwargs):
                self.called = True
                return [], []
        parser = MockParser()
        class MockLogs(object):  # noqa: E302
            def version(*args):
                pass
        class MockShell(object):  # noqa: E302
            @staticmethod
            def info():
                return 'bash'

# Generated at 2022-06-14 08:57:35.090954
# Unit test for function main
def test_main():
    assert main() == None


# Generated at 2022-06-14 08:57:35.774451
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:57:47.530042
# Unit test for function main

# Generated at 2022-06-14 08:57:48.251077
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:57:51.379497
# Unit test for function main
def test_main():
    sys.argv = ['thefuck-3.4', 'ls', 'git']
    main()
    assert 'usage: thefuck' in sys.stdout.getvalue()

# Generated at 2022-06-14 08:57:56.985611
# Unit test for function main
def test_main():
    # Mock the argument parser
    class mock_Parser:
        def parse(self, arguments):
            self.return_value = arguments[1]
            return self

    mock_parser = mock_Parser()
    arguments = ["thefuck", "-h"]
    expected = arguments[1]
    actual = mock_parser.parse(arguments)
    asser

# Generated at 2022-06-14 08:57:57.834357
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:57:58.632737
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:59:05.366262
# Unit test for function main
def test_main():
    sys.argv = ['thefuck', 'history']
    main()
    assert fix_command == fix_command

# Generated at 2022-06-14 08:59:18.173475
# Unit test for function main
def test_main():
    os.environ['TF_HISTORY'] = '1'
    sys.argv = [sys.argv[0], '--fuck', 'fuck']
    main()
    assert os.environ.get('TF_SHELL', None) is not None
    assert os.environ.get('TF_SHELL_FUCKED', None) is not None
    assert os.environ.get('TF_SHELL_COMMAND', None) is not None
    assert os.environ.get('TF_SHELL_HISTORY', None) is not None
    del os.environ['TF_HISTORY']
    del os.environ['TF_SHELL']
    del os.environ['TF_SHELL_FUCKED']
    del os.environ['TF_SHELL_COMMAND']
    del os.environ

# Generated at 2022-06-14 08:59:20.195288
# Unit test for function main
def test_main():
    return main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:59:25.073771
# Unit test for function main
def test_main():
    main.__globals__['parser'] = Parser()
    main.__globals__['known_args'] = main.__globals__['parser'].parse(['--version'])
    main()
    assert logs.version.__name__ == 'version'

# Generated at 2022-06-14 08:59:26.971194
# Unit test for function main
def test_main():
    sys.argv = ['thefuck', '--help']
    assert main()

# Generated at 2022-06-14 08:59:28.476831
# Unit test for function main
def test_main():
    # Unit test for function main
    
    # Function calls
    test_main()

# Generated at 2022-06-14 08:59:29.098984
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:59:33.346503
# Unit test for function main
def test_main():
    try:
        import thefuck.shells.shell  # noqa: E402
        shell.enabled = False
        sys.argv = sys.argv + ['--help']
        main()
    finally:
        shell.enabled = True

# Generated at 2022-06-14 08:59:36.991938
# Unit test for function main
def test_main():
    with mock.patch('sys.argv', ['thefuck', '--version']):
        main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:59:47.618696
# Unit test for function main
def test_main():
    import os
    from pathlib import Path
    from .mocking import MockingProgramTestCase
    from ..logs import logger
    
    # Define args for testing
    sys.argv = ['thefuck', '--shell=bash']
    # Quit the program if an error is raised
    main.quit = True


    # Test if the main program prints help text when called with help flag  ('--help')
    class TestHelp(MockingProgramTestCase):
        def setUp(self):
            # Define args for testing
            sys.argv = ['thefuck', '--help']
            # Quit the program if an error is raised
            main.quit = True
            # Clear mocking variables
            logger.mocking.clear()

        def test_help(self):
            main()

# Generated at 2022-06-14 09:02:11.420114
# Unit test for function main
def test_main():
    os.environ["TF_HISTORY"] = "history"
    sys.argv = ["", ""]
    from . import main as m
    assert m() == None

# Generated at 2022-06-14 09:02:16.920422
# Unit test for function main
def test_main():
    try:
        parser = Parser()
        sys.argv.append('--alias')
        known_args = parser.parse_known_args(sys.argv)
        main()
    except SystemExit as e:
        assert e.code == 0

# Generated at 2022-06-14 09:02:17.880190
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-14 09:02:19.383376
# Unit test for function main
def test_main():
    known_args = Parser().parse()
    assert(main() == None)

# Generated at 2022-06-14 09:02:20.843773
# Unit test for function main
def test_main():
    assert main() is not None

# Generated at 2022-06-14 09:02:25.725209
# Unit test for function main
def test_main():
    # Temp dir
    tempdir = tempfile.mkdtemp()
    # Temp file
    write_tempfile(tempdir, "tf_history", "last command")
    os.environ['TF_HISTORY'] = tempdir + "/tf_history"
    main()


# Generated at 2022-06-14 09:02:27.741905
# Unit test for function main
def test_main():
    main() == fix_command()


if __name__ == '__main__':
    main()

# Generated at 2022-06-14 09:02:36.573271
# Unit test for function main
def test_main():
    """
    Test that main() prints expected text.
    """
    import sys
    import unittest
    import contextlib
    import io
    import textwrap

    @contextlib.contextmanager
    def capture_output():
        new_out, new_err = io.StringIO(), io.StringIO()
        old_out, old_err = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = new_out, new_err
            yield sys.stdout, sys.stderr
        finally:
            sys.stdout, sys.stderr = old_out, old_err

    class FailingTestException(Exception):
        pass

    class MainTester(unittest.TestCase):
        def setUp(self):
            def fail():
                raise F

# Generated at 2022-06-14 09:02:37.242850
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 09:02:37.908269
# Unit test for function main
def test_main():
    assert main() is None