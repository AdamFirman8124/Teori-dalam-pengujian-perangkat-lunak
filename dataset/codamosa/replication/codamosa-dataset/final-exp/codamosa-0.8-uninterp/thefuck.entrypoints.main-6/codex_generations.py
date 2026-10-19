

# Generated at 2022-06-14 08:53:28.282591
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:53:29.566909
# Unit test for function main
def test_main():
   main() 
   assert True

# Generated at 2022-06-14 08:53:30.735114
# Unit test for function main
def test_main():
    assert callable(main)

# Generated at 2022-06-14 08:53:35.466168
# Unit test for function main
def test_main():
    parser = Parser()
    known_args = parser.parse(sys.argv)
    assert known_args.help == False
    assert known_args.version == False
    assert known_args.alias == False
    assert 'TF_HISTORY' not in os.environ
    assert known_args.command == False
    assert known_args.shell_logger == "bash"

# Generated at 2022-06-14 08:53:36.224552
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-14 08:53:47.478920
# Unit test for function main
def test_main():
    old_argv = sys.argv
    sys.argv = ["thefuck", "--version"]
    main()
    assert sys.stderr.getvalue() == "The Fuck 3.11\nPython py3.7\n"
    sys.stderr.seek(0)
    sys.stderr.truncate()
    sys.argv = ["thefuck", "--help"]
    main()
    assert sys.stderr.getvalue().split("\n")[0] == "usage: The Fuck [-h] [--version] [--alias [ALIAS]]"
    sys.stderr.seek(0)
    sys.stderr.truncate()
    sys.argv = old_argv

# Generated at 2022-06-14 08:53:52.974249
# Unit test for function main
def test_main():
    sys.argv = ['thefuck']
    main()
    sys.argv = ['thefuck', '--version']
    main()
    sys.argv = ['thefuck', '--help']
    main()
    sys.argv = ['thefuck', '--alias', 'fuck']
    main()
    sys.argv = ['thefuck', 'ls']
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:53:57.721312
# Unit test for function main
def test_main():
    os.environ['TF_LOG'] = 'DEBUG'
    known_args = parser.parse(sys.argv)
    isinstance(known_args.log, str)
    isinstance(known_args.require_confirmation, bool)
    isinstance(known_args.history_limit, int)


# Generated at 2022-06-14 08:53:58.440961
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-14 08:53:59.351113
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-14 08:54:08.137963
# Unit test for function main
def test_main():
    return True;

# Generated at 2022-06-14 08:54:10.563204
# Unit test for function main
def test_main():
    sys.argv = ['thefuck', '--version']
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:54:11.318764
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:54:23.726109
# Unit test for function main
def test_main():
    import os
    import sys
    import unittest
    import thefuck.main as main

    class MockParser(object):
        def __init__(self):
            self.data = {}

        def parse(self, X):
            return self.data

        def print_help(self):
            return self.data

        def print_usage(self):
            return self.data

    class MockParser2(object):
        def parse(self, X):
            return {}

    class MockParser3(object):
        def parse(self, X):
            return {'shell_logger': 'fish'}

    class MockParser4(object):
        def parse(self, X):
            return {'alias': True}

    class MockParser5(object):
        def parse(self, X):
            return {'command': True}

# Generated at 2022-06-14 08:54:25.105477
# Unit test for function main
def test_main():
    main()
    assert True

# Generated at 2022-06-14 08:54:25.904434
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-14 08:54:37.520402
# Unit test for function main
def test_main():
    from unittest.mock import patch
    from .utils import mock_from_for
    from .utils import mock_input

    with patch('sys.argv', ['thefuck']):
        with mock_from_for(builtins):
            with mock_input('y'):
                with patch('thefuck.main.fix_command') as mock_fix_command:
                    main()
                    assert mock_fix_command.called is True

    with patch('sys.argv', ['thefuck']):
        with patch('thefuck.main.print_alias') as mock_print_alias:
            with mock_from_for(builtins):
                with mock_input('y'):
                    with patch('thefuck.main.fix_command') as mock_fix_command:
                        main()
                        assert mock_fix_command.called is True

# Generated at 2022-06-14 08:54:38.333565
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:54:46.557095
# Unit test for function main
def test_main():
    #Testing when help is true
    sys.argv = ['thefuck', '-h']
    test_main.main()
    #Testing when version is true
    sys.argv = ['thefuck', '-v']
    test_main.main()
    #Testing when alias is true
    sys.argv = ['thefuck', '-a']
    test_main.main()
    #Testing when command is true
    sys.argv = ['thefuck', '-c']
    test_main.main()
    #Testing when shell_logger is true
    sys.argv = ['thefuck', '-s']
    test_main.main()
    #Testing when nothing is true
    sys.argv = ['thefuck']
    test_main.main()

# Generated at 2022-06-14 08:54:58.059735
# Unit test for function main
def test_main():
    from .utils import version
    from .alias import print_alias
    from .shell_logger import shell_logger
    from .fix_command import fix_command
    from .argument_parser import Parser
    from ...utils import get_installation_info
    from ...system import init_output
    import sys
    import os
    import io

    old_version = version
    old_print_alias = print_alias
    old_shell_logger = shell_logger
    old_fix_command = fix_command
    old_Parser = Parser
    old_get_installation_info = get_installation_info
    old_init_output = init_output
    old_sys = sys
    old_os = os
    old_stdout = sys.stdout
    old_stderr = sys.stderr


# Generated at 2022-06-14 08:55:15.180339
# Unit test for function main
def test_main():
    import pytest
    1/0

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:55:18.735301
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-14 08:55:19.597945
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-14 08:55:20.434405
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:55:24.100870
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:55:25.065999
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-14 08:55:28.123705
# Unit test for function main
def test_main():
    try:
        main()
    except:
        assert False

# Generated at 2022-06-14 08:55:38.080150
# Unit test for function main
def test_main():
    from unittest.mock import patch, call
    from ..argument_parser import Parser
    from ..shells import shell
    from ..utils import get_installation_info
    from .alias import print_alias
    from .fix_command import fix_command

    arg_list = ['thefuck', '--help', '--version', '--alias', '--shell-logger', None]
    for arg in arg_list:
        os.environ.clear()

# Generated at 2022-06-14 08:55:48.484067
# Unit test for function main
def test_main():
    import sys
    from unittest.mock import Mock
    from . import alias
    from . import fix_command
    from . import shell_logger
    from .. import argument_parser
    from .. import logs
    from .. import utils
    from .. import version

    def print_usage(argv):
        sys.argv = argv
        main()

    logs.version = Mock()
    utils.get_installation_info = Mock(
        return_value=version.InstallationInfo('3.1.0'))
    version.python_version = '3.6.7'
    logs.warn = Mock()

# Generated at 2022-06-14 08:55:50.471025
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-14 08:56:24.163436
# Unit test for function main
def test_main():
    try:
        main()
    except SystemExit:
        pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:56:26.228255
# Unit test for function main
def test_main():
    with patch('sys.argv', ['thefuck']):
        assert main() == None

# Generated at 2022-06-14 08:56:37.163185
# Unit test for function main
def test_main():
    import argparse
    import subprocess  # noqa: E402
    import tempfile    # noqa: E402

    class FakeArgs:
        def __init__(self):
            self.help = None
            self.version = None
            self.alias = None
            self.command = None
            self.shell_logger = None

# Test for function main when help is given
    def test_not_help_and_version_and_alias_and_command():
        logs.error = lambda x: x
        subprocess.call = lambda x: 0
        os.environ = {}
        known_args = FakeArgs()
        parser = argparse.ArgumentParser()
        parser.print_usage = lambda : 'Helper'

        assert main() == parser.print_usage()


# Test for function main when no option is given

# Generated at 2022-06-14 08:56:37.821068
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:56:43.407710
# Unit test for function main
def test_main():
    old_argv = sys.argv
    try:
        sys.argv = ['thefuck', '--alias', 'fuck']
        main()
        sys.argv = ['thefuck', '--helper', 'tkf']
        main()
    finally:
        sys.argv = old_argv

# Generated at 2022-06-14 08:56:44.136090
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:56:57.416677
# Unit test for function main
def test_main():
    from unittest.mock import MagicMock, patch

    sys.argv[1:] = []
    main()
    with patch('thefuck.logs.version') as version_mock:
        main()
        assert version_mock.called

    with patch('thefuck.arguments.parser.Parser') as ArgumentParserMock:
        with patch.object(ArgumentParserMock, 'parse') as parse_mock:
            parse_mock.return_value = MagicMock()
            parse_mock.return_value.alias = False
            parse_mock.return_value.command = False

            with patch('thefuck.utils.get_installation_info') as get_installation_info_mock:
                get_installation_info_mock.return_value = MagicMock()
                get_

# Generated at 2022-06-14 08:56:59.276869
# Unit test for function main
def test_main():
    class KnownArgs():
        help = True
    main(KnownArgs)

# Generated at 2022-06-14 08:57:00.199080
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:57:01.630735
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-14 08:58:10.241356
# Unit test for function main
def test_main():
    """
    Unit test for function main in thefuck.main
    """
    assert callable(main)

    # Checking if function main performs as expected
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2

# Generated at 2022-06-14 08:58:10.979685
# Unit test for function main
def test_main():
    assert main() != None

# Generated at 2022-06-14 08:58:12.027962
# Unit test for function main
def test_main():
    assert main() == None


# Generated at 2022-06-14 08:58:12.747183
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:58:23.857815
# Unit test for function main
def test_main():
    import unittest.mock
    with unittest.mock.patch("thefuck.main.Parser") as mock_Parser, \
            unittest.mock.patch("thefuck.main.logs") as mock_logs, \
            unittest.mock.patch("thefuck.main.print_alias") as mock_print_alias, \
            unittest.mock.patch("thefuck.main.fix_command") as mock_fix_command:
        mock_Parser.parse.return_value.help = False
        mock_Parser.parse.return_value.version = False
        mock_Parser.parse.return_value.shell_logger = False
        main()
        assert mock_print_alias.called is False
        assert mock_fix_command.called is False
        assert mock_logs.version

# Generated at 2022-06-14 08:58:25.576372
# Unit test for function main
def test_main():
    try:
        main()
    except SystemExit:
        pass

# Generated at 2022-06-14 08:58:38.857507
# Unit test for function main
def test_main():
    # Ugly hack to mock input. Needed because the only argv is sys.argv.
    # In the future, we can use [Argv](https://pypi.org/project/argv/)
    # or [click](https://pypi.org/project/click/)
    old_argv = sys.argv
    old_exit = sys.exit
    old_print = print

    sys.argv = ['thefuck', '--help']
    sys.exit = lambda: None
    output = []
    print = output.append
    main()

    assert 'usage: thefuck' in '\n'.join(output)
    assert 'optional arguments:' in '\n'.join(output)

    sys.argv = ['thefuck', '--version']
    sys.exit = lambda: None
    output = []


# Generated at 2022-06-14 08:58:43.231078
# Unit test for function main
def test_main():
    from ..system import (
        init_logger,
        init_shell,
        init_logs,
        init_caches
    )
    init_logger()
    init_shell()
    init_logs()
    init_caches()

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:58:55.398627
# Unit test for function main
def test_main():
    from ..utils import replace_argument
    from ..config import Config
    from .shells import Shell, Bash, Zsh
    from .utils import (
        get_closest,
        get_all_matched_commands,
        get_shell_and_app_name,
        memoize,
        get_aliases_and_commands
    )
    assert main() == None
    assert Parser() != None
    assert replace_argument != None
    assert Config() != None
    assert Shell() != None
    assert Bash() != None
    assert Zsh() != None
    assert get_closest != None
    assert get_all_matched_commands != None
    assert get_shell_and_app_name != None
    assert memoize != None
    assert get_aliases_and_commands != None


# Generated at 2022-06-14 08:58:56.319848
# Unit test for function main
def test_main():
    assert callable(main)

# Generated at 2022-06-14 09:01:09.617184
# Unit test for function main
def test_main():
    args = ['-l']
    try:
        main()
    except SystemExit as e:
        return e.code == 2

# Generated at 2022-06-14 09:01:10.432157
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-14 09:01:19.258549
# Unit test for function main
def test_main():
    from .mock_objects import mock_open

    parser = Parser()

    # If there are no arguments return usage
    with mock_open([parser.prog, '']):
        main()

    # If help is requested return help
    with mock_open([parser.prog, '--help']):
        main()

    # If version is requested return version 
    with mock_open([parser.prog, '--version']):
        main()

    # If an alias is requested return alias
    with mock_open([parser.prog, '-a', 'zsh']):
        main()

    # If a command is given fix_command is called
    with mock_open([parser.prog, 'git branch']):
        main()


# Generated at 2022-06-14 09:01:20.014141
# Unit test for function main
def test_main():
    assert main

# Generated at 2022-06-14 09:01:32.824902
# Unit test for function main
def test_main():
    # Unit tests should be run as "python3 -m unittest"
    # Importing unit test module
    import unittest

    class TestMain(unittest.TestCase):
        """Tests for main"""

        def test_help(self):
            """Test printing help"""
            # Saving previous print value
            old_print = print
            # Mock print function
            print = lambda string: self.assertIn('Show help message', string)
            # Initializing arguments for function main
            sys.argv[1:] = ['--help']
            # Calling function main
            main()
            # Restoring print function
            print = old_print

        def test_version(self):
            """Test printing version"""
            # Saving previous print value
            old_print = print
            # Mock print function

# Generated at 2022-06-14 09:01:37.763297
# Unit test for function main
def test_main():
    import io
    import sys
    import thefuck

    out = io.StringIO()
    sys.stdout = out

    main()
    output = out.getvalue().strip()
    assert 'thefuck' in output
    assert thefuck.__version__ in output

    sys.stdout = sys.__stdout__


# Generated at 2022-06-14 09:01:38.693932
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 09:01:40.246317
# Unit test for function main
def test_main():
    try:
        main()
        assert True
    except Exception:
        assert False

# Generated at 2022-06-14 09:01:49.826362
# Unit test for function main
def test_main():
    from unittest.mock import patch
    from unittest.mock import Mock
    from .shell import Config
    from .shell import SupportedShell
    from .shell import bash
    from .shell import fish
    from .shell import zsh
    with patch('thefuck.main.parser.parse', return_value=Mock()) as mock_parser:
        with patch('thefuck.main.fix_command') as mock_fix_command:
            with patch('thefuck.main.print_alias') as mock_print_alias:
                mock_parser.return_value.command = True
                mock_parser.return_value.alias = False
                mock_parser.return_value.shell_logger = False
                mock_parser.return_value.help = False
                main()

# Generated at 2022-06-14 09:01:50.834755
# Unit test for function main
def test_main():
    assert main() is None