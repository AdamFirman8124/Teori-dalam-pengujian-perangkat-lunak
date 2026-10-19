

# Generated at 2022-06-14 08:53:40.322419
# Unit test for function main
def test_main():
    parser = Parser()
    assert type(parser) == Parser

# Generated at 2022-06-14 08:53:52.536705
# Unit test for function main
def test_main():
    # Filling the lists of alias
    nvbn_aliases = {"fuck": "fuck", "tf": "fuck --alias"}
    parser = Parser()
    known_args = parser.parse(sys.argv)
    assert (main() == None)
    assert (main() == parser.print_usage())
    assert (main() == parser.print_help())
    assert (main() == logs.version(get_installation_info().version,
                     sys.version.split()[0], shell.info()))
    assert (main() == print_alias(known_args))
    assert (main() == fix_command(known_args))
    assert (main() == logs.warn('Shell logger supports only Linux and macOS'))
    assert (main() == parser.parse(sys.argv))

# Generated at 2022-06-14 08:53:53.210541
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:54:06.520504
# Unit test for function main
def test_main():
    class args:
        # pylint: disable=too-many-instance-attributes
        def __init__(self, command, alias, help, version, shell_logger):
            self.command = command
            self.alias = alias
            self.help = help
            self.version = version
            self.shell_logger = shell_logger
            self.no_colors = False
            self.wait = False
            self.slow_commands = False
            self.settings_path = None

    # Check that the help is displayed
    class logs:
        def print_help():
            return True
        def print_usage():
            return True

    # Call main
    main(args(command=False, alias=False, help=True,
              version=False, shell_logger=False))

    # Check that a version

# Generated at 2022-06-14 08:54:07.626171
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:54:20.094181
# Unit test for function main
def test_main():
    import mock
    from thefuck.argument_parser import Parser

    mock_args = mock.Mock()
    mock_args.help = False
    mock_args.version = False
    mock_args.show_log = False
    mock_args.alias = False
    mock_args.shell = None
    mock_args.command = False
    mock_args.shell_logger = False

    sys.argv[1:] = []
    main()
    assert Parser().parse(sys.argv).help == False
    assert Parser().parse(sys.argv).version == False
    assert Parser().parse(sys.argv).alias == False
    assert Parser().parse(sys.argv).shell_logger == False

    mock_args.help = False
    mock_args.version = True
    mock_args

# Generated at 2022-06-14 08:54:27.162917
# Unit test for function main
def test_main():
    from argparse import ArgumentParser
    from thefuck.utils import get_root


# Generated at 2022-06-14 08:54:39.531414
# Unit test for function main
def test_main():
    from unittest.mock import patch
    import sys
    import pytest
    # with patch('sys.argv', ['thefuck', '--version']):
    #     with patch('thefuck.logs.version') as version_mock:
    #         main()
    #         assert version_mock.called
    with pytest.raises(SystemExit) as excinfo:
        with patch('sys.argv', ['thefuck', '--help']):
            sys.exit = Exception
            main()
    assert excinfo.type is SystemExit
    assert excinfo.value.code == 0
    with pytest.raises(SystemExit) as excinfo:
        with patch('sys.argv', ['thefuck', '--alias', 'fuck']):
            sys.exit = Exception
            main()

# Generated at 2022-06-14 08:54:40.206473
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:54:42.403421
# Unit test for function main
def test_main():
    assert main() == None
    assert sys.argv == ['fuck'] #noqa: WPS421

# Generated at 2022-06-14 08:54:59.929824
# Unit test for function main
def test_main():
    # When no arg is given, argparse will end with exit(2)
    sys.exit = lambda *x:x
    # When no arg is given, the help message should be printed
    with mock.patch("sys.stdout", new=io.StringIO()) as h:
        main()

# Generated at 2022-06-14 08:55:00.630403
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:55:01.449966
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:55:02.302066
# Unit test for function main
def test_main():
    assert main

# Generated at 2022-06-14 08:55:13.715296
# Unit test for function main
def test_main():
    import os
    import subprocess
    import tempfile

    temp_env = tempfile.mkdtemp()
    os.environ['TF_SHELL'] = 'ksh'
    os.environ['TF_DEBUG_MODE'] = '1'

    cmd = "thefuck --alias 'alias fuck='thefuck' --shell_logger --help"
    process = subprocess.Popen(cmd, env=os.environ, shell=True,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()

    assert 'Usage' in stdout
    assert 'Show error message' in stderr

    os.environ['TF_HISTORY'] = '1'
    cmd = "thefuck --version"
    process = subprocess.P

# Generated at 2022-06-14 08:55:18.943290
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:55:20.044466
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:55:36.310196
# Unit test for function main
def test_main():
    from .mocks.subprocess import Fuck
    from .mocks.subprocess import which
    from .mocks.subprocess import get_teminal_size
    fuck = Fuck()
    sys.argv = ['thefuck']
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()


# Generated at 2022-06-14 08:55:36.978213
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:55:38.348009
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:56:07.642347
# Unit test for function main
def test_main():
    import sys
    from unittest.mock import MagicMock
    from .alias import print_alias
    from .fix_command import fix_command
    from .shell_logger import shell_logger

    # Replace `sys.argv` to have a predictable input line.
    sys.argv = ['thefuck', '--version']

    # Mock exit function to avoid exiting the program.
    sys.exit = MagicMock()

    # Mock print function to use it as a spy.
    print_alias = MagicMock()
    fix_command = MagicMock()
    shell_logger = MagicMock()

    main()

    # Assert that `thefuck` was called with argument `--version`.
    print_alias.assert_not_called()
    fix_command.assert_not_called()
    shell_logger

# Generated at 2022-06-14 08:56:13.034130
# Unit test for function main
def test_main():
    logs.version('7.0.0', sys.version.split()[0], shell.info())
    fix_command(known_args)
    assert 'TF_HISTORY' in os.environ
    assert print_alias(known_args)
    assert parser.print_usage()
    assert parser.print_help()

# Generated at 2022-06-14 08:56:27.900371
# Unit test for function main
def test_main():
    from thefuck.utils import get_closest, get_history  # noqa: F401
    from thefuck.rules.fix_command import FixCommandRule # noqa: F401
    from thefuck.rules.pip import pip_support  # noqa: F401
    from thefuck.rules.cd_mkdir import cd_mkdir  # noqa: F401

    # mock function for unit test
    def mock_FixCommandRule(history):
        return MockRule(history)

    class MockRule:
        def __init__(self, history):
            self.history = history

        def get_new_command(self):
            return self.history[-1]

    parser = Parser()
    known_args1 = parser.parse(['-h'])
    sys.argv = ['thefuck', '-h']

# Generated at 2022-06-14 08:56:37.625403
# Unit test for function main
def test_main():
    #test for print_usage()
    import pytest
    from io import StringIO
    from unittest.mock import patch, mock_open
    class MockArgs:
        def __init__(self, version, help, alias, command, shell_logger):
            self.version = version
            self.help = help
            self.alias = alias
            self.command = command
            self.shell_logger = shell_logger
    #sys.argv[1:] = ['--help']
    mock_args = MockArgs(None, True, None, None, None)
    with patch("sys.stdout", new=StringIO()) as actual_stdout:
        main()
        actual_stdout.seek(0)
        actual_output = actual_stdout.read()

# Generated at 2022-06-14 08:56:46.443983
# Unit test for function main
def test_main():
    from unittest.mock import patch
    from io import StringIO
    with patch('sys.argv', ['-h']), \
        patch('sys.stdout', new=StringIO()) as fake_out:
        main()

# Generated at 2022-06-14 08:56:58.840498
# Unit test for function main
def test_main():
    def mock_parse(a):
        class Test:
            def __init__(self):
                self.help = False
                self.version = False
                self.alias = False
                self.command = False
                self.shell_logger = False
        return Test()

    class Parser:
        def __init__(self):
            pass

        def parse(self, a):
            return mock_parse(a)

        def print_help(self):
            pass

        def print_usage(self):
            pass

    class Shell:
        def info(self):
            return 'test'

    def mock_get_installation_info():
        class Test:
            version = 'test'
        return Test()

    logs.version = lambda a, b, c: None


# Generated at 2022-06-14 08:56:59.801271
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:57:00.485327
# Unit test for function main
def test_main():
    assert main() != ""

# Generated at 2022-06-14 08:57:17.893936
# Unit test for function main
def test_main():
    from .test_alias import test_print_alias
    from .test_fix_command import test_fix_command

    with mock.patch('sys.version', '3.4.5') as sys_version:
        with mock.patch('sys.argv', ['thefuck', 'ls', '--version']):
            args = Parser().parse(sys.argv)
            assert args.version
            main()
            assert sys_version.called

    with mock.patch('sys.argv', ['thefuck', 'ls', '--alias']):
        args = Parser().parse(sys.argv)
        assert args.alias
        test_print_alias(args)
        main()


# Generated at 2022-06-14 08:57:20.181895
# Unit test for function main
def test_main():
    main(test=True)

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:57:57.619382
# Unit test for function main
def test_main():
    # Sample input
    sys.argv = ['thefuck', '-c', 'ls']
    main()

    # Sample output
    assert sys.argv == ['thefuck', '-c', 'ls']


if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:58:08.065236
# Unit test for function main
def test_main():
    import io
    import sys
    import argparse

    # create an input stream
    string_input = io.StringIO()

    # create an output stream
    string_output = io.StringIO()

    # redirect the standard output to the stream
    sys.stdout = string_output

    # create an error stream
    string_error = io.StringIO()

    # redirect the standard error to the stream
    sys.stderr = string_error

    my_parser = Parser()
    # create known args with help set to true
    known_args = my_parser.parse(["thefuck", "--help"])
    # call main with known args
    main()

    # capture the output
    output = string_output.getvalue()
    assert 'thefuck [options] -- <your-command>' in output

# Generated at 2022-06-14 08:58:16.041125
# Unit test for function main
def test_main():
    sys.argv = ['thefuck', '--version']
    main()
    sys.argv = ['thefuck', '--help']
    main()
    sys.argv = ['thefuck', '--alias']
    main()
    sys.argv = ['thefuck', '--shell-logger', 'bash']
    main()
    sys.argv = ['thefuck', 'rm', '-rf']
    main()
    sys.argv = ['thefuck']
    main()

# Generated at 2022-06-14 08:58:25.130380
# Unit test for function main
def test_main():
    from .alias import print_alias
    from .fix_command import fix_command
    from .shell_logger import shell_logger
    from ..argument_parser import Parser
    from ..utils import get_installation_info

    main()

    c = Parser.parse.call_count
    assert Parser.parse.call_count == c+1

    c = logs.version.call_count
    assert logs.version.call_count == c+1

    c = get_installation_info.call_count
    assert get_installation_info.call_count == c+1

    c = print_alias.call_count
    assert print_alias.call_count == c+1

    c = fix_command.call_count
    assert fix_command.call_count == c+1

    c = shell_logger

# Generated at 2022-06-14 08:58:26.727407
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-14 08:58:27.463812
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:58:39.639427
# Unit test for function main
def test_main():
    from unittest import mock
    from .test_argument_parser import MockArgs

    with mock.patch('sys.argv', ['thefuck']):
        with mock.patch('thefuck.argument_parser.Parser.parse',
                        return_value=MockArgs(False, False, False, False,
                                              False, False)):
            with mock.patch('thefuck.argument_parser.Parser.print_usage'):
                main()
                thefuck.argument_parser.Parser.print_usage.assert_called_with()


# Generated at 2022-06-14 08:58:50.632547
# Unit test for function main
def test_main():
    from .alias import print_alias
    from .fix_command import fix_command
    import os # noqa: E402
    import sys # noqa: E402
    from ..system import init_output
    from ..utils import get_installation_info
    from ..shells import shell # noqa: E402
    class Parser():
        def parse(self,argv):
            self.help = False
            self.alias = False
            self.version = False
            self.command = False
            self.shell_logger = None
            return self
        def print_help(self):
            print('Print help message')
        def log_version(self,version,python_version,shell_info):
            print('version : '+version)
            print('python version : '+python_version)

# Generated at 2022-06-14 08:58:53.411952
# Unit test for function main
def test_main():
    # try to run main()
    try:
        main()
    except Exception as e:
        print("Something went wrong !\n\n{}".format(e))

# Generated at 2022-06-14 08:58:54.043987
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 09:00:04.326483
# Unit test for function main
def test_main():
    known_args = Parser.parse([])
    assert known_args.alias == False
    assert known_args.command == None
    assert known_args.help == False
    assert known_args.shell_logger == None
    assert known_args.version == False

# Generated at 2022-06-14 09:00:07.704118
# Unit test for function main
def test_main():
    class args:
        help = False
        version = False
        alias = False
        command = False
        shell_logger = False
    main(args)

# Generated at 2022-06-14 09:00:08.416754
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-14 09:00:15.228688
# Unit test for function main
def test_main():
    global default
    default = '\33[0m'
    parser = Parser()
    known_args = parser.parse(sys.argv)
    assert known_args.help == False
    assert known_args.version == False
    assert known_args.alias == False
    assert known_args.command == False
    assert known_args.shell_logger == False
    assert known_args.wait == False
    assert known_args.no_colors == False
    assert known_args.locale == None
    assert known_args.history_limit == 5000
    assert known_args.require_confirmation == True

# Generated at 2022-06-14 09:00:15.866002
# Unit test for function main
def test_main():
    assert main() == 4

# Generated at 2022-06-14 09:00:16.555618
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 09:00:25.833014
# Unit test for function main
def test_main():
    import unittest

    class MockedArgumentParser:
        def parse(self, args):
            return args

        def print_usage(self):
            return "usage"

    class MockedParser(Parser):
        def parse(self, args):
            return args

    class MockedUtils:
        def get_installation_info(self):
            return "installation info"

    class MockedLogs:
        def version(self, version, py_version, shell_info):
            return "version"

        def warn(self, msg):
            return "warn"

    class MockedShells:
        class MockedShell:
            def info(self):
                return "info"

        def MockedShells():
            return MockedShell()


# Generated at 2022-06-14 09:00:34.506843
# Unit test for function main
def test_main():
    import sys
    import io

    # No arguments
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    main()
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == "[tf]\n"

    # Version
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    main()
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() == "The Fuck 3.1 using Python 3.5.2\n"

# Generated at 2022-06-14 09:00:35.182841
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 09:00:35.931606
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 09:02:51.272505
# Unit test for function main
def test_main():
    sys.argv = ['./thefuck', '--help']
    assert main() == None

# Generated at 2022-06-14 09:03:03.574679
# Unit test for function main
def test_main():
    # testing the help option
    sys.argv = ['thefuck', '--help']
    main()
    # testing the version option
    sys.argv = ['thefuck', '--version']
    main()
    # testing the alias option
    sys.argv = ['thefuck', '--alias']
    main()
    # testing the command option
    sys.argv = ['thefuck', 'lsd']
    main()
    # testing the TF_HISTORY option
    os.environ['TF_HISTORY'] = 'lsd'
    sys.argv = ['thefuck']
    main()
    # testing the shell logger option
    sys.argv = ['thefuck', '--shell-logger']
    main()
    # testing the shell logger option with wrong option

# Generated at 2022-06-14 09:03:04.307508
# Unit test for function main
def test_main():
    assert isinstance(main(), object), "main() function is broken"

# Generated at 2022-06-14 09:03:17.231599
# Unit test for function main
def test_main():
    # testing the --help option
    with patch('sys.stdout', new=io.StringIO()) as fake_out:
        main()
    output = fake_out.getvalue()
    assert output.split('\n')[10] == "  -h, --help         show this help message and exit"
    # testing the --version option
    with patch('sys.stdout', new=io.StringIO()) as fake_out:
        main()
    output = fake_out.getvalue()
    assert output.split('\n')[13] == "  -V, --version      show program's version number and exit"
    # testing the --alias option
    with patch('sys.stdout', new=io.StringIO()) as fake_out:
        main()
    output = fake_out.getvalue()
    assert output.split

# Generated at 2022-06-14 09:03:17.948098
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-14 09:03:18.600594
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 09:03:25.690233
# Unit test for function main

# Generated at 2022-06-14 09:03:28.132353
# Unit test for function main
def test_main():
    #mock argv data
    sys.argv = ['thefuck', 'command']
    main()

# Generated at 2022-06-14 09:03:29.306681
# Unit test for function main
def test_main():
    assert callable(main)

# Generated at 2022-06-14 09:03:30.987089
# Unit test for function main
def test_main():
    # Test help
    main()
    # Test version
    main("--version")