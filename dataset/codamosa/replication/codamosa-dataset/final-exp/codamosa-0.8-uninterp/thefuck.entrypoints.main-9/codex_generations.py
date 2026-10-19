

# Generated at 2022-06-14 08:53:35.557741
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:53:37.016257
# Unit test for function main
def test_main():
    assert main() is None


# Generated at 2022-06-14 08:53:38.597359
# Unit test for function main
def test_main():
	if __name__ == '__main__':
		main()

# Generated at 2022-06-14 08:53:40.197291
# Unit test for function main
def test_main():
    main()
    assert True

# Generated at 2022-06-14 08:53:45.590141
# Unit test for function main
def test_main():
    sys.argv[1:] = "--help".split()
    main()

    sys.argv[1:] = "--alias bash".split()
    main()

    sys.argv[1:] = "fuck".split()
    main()

# Generated at 2022-06-14 08:53:52.646204
# Unit test for function main
def test_main():
    # known-args is an object, but when it is passed to the function fix_command()
    # we need it to be a string, so that the function will run properly.
    from .fix_command import fix_command
    class test_args:
        command = 'cd ~/Downloads'
    main_test_args = test_args()
    main_test_args.command = fix_command(main_test_args)
    assert main_test_args.command == 'cd ~/Downloads', 'main function test failed'

# Generated at 2022-06-14 08:53:54.201785
# Unit test for function main
def test_main():
    try:
        main()
    except SystemExit:
        pass

# Generated at 2022-06-14 08:53:56.774695
# Unit test for function main
def test_main():
	sys.argv.append('--help')
	test_main.test_func = main
	print(test_main.test_func)
	main()

# Generated at 2022-06-14 08:53:57.385595
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:53:58.003397
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:54:17.238049
# Unit test for function main
def test_main():
    test_arguments = ['thefuck', '--help']
    with patch.object(sys, 'argv', test_arguments):
        main()

# Generated at 2022-06-14 08:54:18.180369
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:54:19.823797
# Unit test for function main
def test_main():
    for arg in ["", "fuck", "fuck upgrade"]:
        main()

# Generated at 2022-06-14 08:54:21.342235
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:54:21.983278
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:54:28.182923
# Unit test for function main
def test_main():

    def run_main(main_args, parser_args=[]):
        with mock.patch('sys.argv', [sys.argv[0]] + main_args):
            with mock.patch('thefuck.argument_parser.Parser.parse') as parse:
                parse.return_value = parser_args
                try:
                    main()
                except SystemExit as sysexit:
                    return sysexit.code

    assert run_main(['--help']) is None
    assert run_main(['--version']) is None

    with mock.patch('thefuck.argument_parser.Parser') as Parser:
        assert run_main(['--alias', 'fuck']) is None
        Parser.assert_called_with().parse.assert_called_with(['fuck'])


# Generated at 2022-06-14 08:54:29.523827
# Unit test for function main
def test_main():  # noqa: E501
    main()

# Generated at 2022-06-14 08:54:31.395113
# Unit test for function main
def test_main():
    sys.argv = ['thefuck']
    main()


# Generated at 2022-06-14 08:54:32.871750
# Unit test for function main
def test_main():
    assert main() == None

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:54:34.165516
# Unit test for function main
def test_main():
    assert main() == Parser().parse()

# Generated at 2022-06-14 08:55:06.830725
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:55:08.027186
# Unit test for function main
def test_main():
    main()
    

# Generated at 2022-06-14 08:55:15.490009
# Unit test for function main
def test_main():
    from unittest.mock import patch, MagicMock
    from io import StringIO
    from ..system import init_output

    init_output()
    args = [sys.argv[0]]
    # Test help case
    with patch.object(sys, 'argv', args + ['--help']):
        main()
        out, err = capsys.readouterr()
        assert 'Usage: thefuck [OPTIONS]' in out

    # Test version case
    with patch.object(sys, 'argv', args + ['--version']):
        main()
        out, err = capsys.readouterr()
        assert 'The Fuck {}'.format(get_installation_info().version) in out

    # Test alias case
    with patch.object(sys, 'argv', args + ['--alias']):
        main

# Generated at 2022-06-14 08:55:16.698930
# Unit test for function main
def test_main():  # noqa: F811
    main()

# Generated at 2022-06-14 08:55:17.444509
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:55:18.156426
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:55:19.136913
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:55:20.153580
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-14 08:55:25.949102
# Unit test for function main
def test_main():
    main()
    try:
        assert (True)
    finally:
        print("test passed")

# Generated at 2022-06-14 08:55:29.559460
# Unit test for function main
def test_main():
    message = 'Usage: thefuck [OPTIONS] COMMAND [ARGS]...\nTry "thefuck --help" for help.'
    assert main() == message

# Generated at 2022-06-14 08:56:02.469763
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:56:03.351590
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-14 08:56:15.685541
# Unit test for function main
def test_main():
    from unittest.mock import patch
    from unittest.mock import MagicMock
    import sys


    def parse_return_mock():
        class MockReturn():
            def __init__(self):
                self.help = False
                self.version = False
                self.alias = False
                self.command = False
                self.shell_logger = False
        return MockReturn()

    # Original import code
    # from ..argument_parser import Parser
    # Replace by patch
    with patch('thefuck.argument_parser.Parser') as MockParser:
        # Get instance of mock thefuck.argument_parser.Parser
        parser_mock = MockParser()

        # Set return value of mock parser_mock.parse

# Generated at 2022-06-14 08:56:20.365890
# Unit test for function main
def test_main():
    assert main() == (
        None,
        None,
        None,
        None,
        None
    )



# Generated at 2022-06-14 08:56:21.836925
# Unit test for function main
def test_main():
    main()


# Generated at 2022-06-14 08:56:22.592485
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-14 08:56:31.414252
# Unit test for function main
def test_main():
    import sys

    # Search
    sys.argv = ['thefuck', 'cd']

    main()

    # Error
    sys.argv = ['thefuck', 'cd', '-e', '1']

    main()

    # Ignore
    sys.argv = ['thefuck', 'cd', '-i', '1']

    main()

    # Inverse
    sys.argv = ['thefuck', 'cd', '-I']

    main()

    # Debug
    sys.argv = ['thefuck', 'cd', '-D']

    main()

    # Slow
    sys.argv = ['thefuck', 'cd', '-s', '1']

    main()

    # Wait
    sys.argv = ['thefuck', 'cd', '-w', '1']

    main()

    # No wait

# Generated at 2022-06-14 08:56:32.449861
# Unit test for function main
def test_main():
	assert main() == None
	

# Generated at 2022-06-14 08:56:35.224525
# Unit test for function main
def test_main():
    from .alias import print_alias
    from .fix_command import fix_command
    main()
    assert callable(print_alias)
    assert callable(fix_command)

# Generated at 2022-06-14 08:56:48.342520
# Unit test for function main
def test_main():
    import os
    import sys
    from .alias import print_alias
    from .fix_command import fix_command
    from ..system import init_output
    from ..shells import shell
    from ..utils import get_installation_info

    installed_version = get_installation_info().version
    shell_name = shell.info()
    python_version = sys.version.split()[0]
    init_output()

    known_args = Parser().parse(sys.argv)
    known_args.help = True
    with pytest.raises(SystemExit):
        main()

    known_args = Parser().parse(sys.argv)
    known_args.version = True
    with pytest.raises(SystemExit):
        main()

    known_args = Parser().parse(sys.argv)

# Generated at 2022-06-14 08:57:54.865383
# Unit test for function main
def test_main():
    sys.argv = ['thefuck', '--version']
    assert main() == None

# Generated at 2022-06-14 08:57:58.632594
# Unit test for function main
def test_main():
    # Unit test for function main
    parser = Parser()
    known_args = parser.parse(["-v"])

    known_args.version = True
    known_args.help = False


main()

# Generated at 2022-06-14 08:58:00.165421
# Unit test for function main
def test_main():
    assert main() == None

test_main()

# Generated at 2022-06-14 08:58:05.867936
# Unit test for function main
def test_main():
    del os.environ['TF_HISTORY']
    assert not os.environ.get('TF_HISTORY', False)

    # set TF_HISTORY, such that it will be detected
    os.environ['TF_HISTORY'] = '12'
    assert os.environ.get('TF_HISTORY', False)

    main()
    assert not os.environ.get('TF_HISTORY', False)

# Generated at 2022-06-14 08:58:06.772919
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:58:07.565579
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:58:10.044385
# Unit test for function main
def test_main():
    assert main() == None

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:58:21.214769
# Unit test for function main
def test_main():
    class MockArgs(object):
        def __init__(self, command=None, help=None, version=None,
                     shell_logger=None, alias=None):
            self.command = command
            self.help = help
            self.version = version
            self.shell_logger = shell_logger
            self.alias = alias

    assert all(main() == None
               for arg in [MockArgs(command='git branch'),
                           MockArgs(command='cp', help=True),
                           MockArgs(version=True),
                           MockArgs(command='echo', alias='fuck'),
                           MockArgs(shell_logger='fish')])


if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:58:22.445883
# Unit test for function main
def test_main():
    assert(main() == None)

# Generated at 2022-06-14 08:58:23.895814
# Unit test for function main
def test_main():
    # TODO: test all branches
    pass

# Generated at 2022-06-14 09:00:48.369871
# Unit test for function main
def test_main():
    test_argv = ['python', '-W', 'ignore', 'main.py', '--help']
    with mock.patch.object(sys, 'argv', test_argv):
        try: 
            with mock.patch('thefuck.main.Parser') as mocked_parser:
                with mock.patch('sys.exit', side_effect=SystemExit) as mocked_exit:
                    main()
                    mocked_exit.assert_called_once_with(0)
                    mocked_parser.return_value.parse.assert_called_once_with(test_argv)
                    mocked_parser.return_value.print_usage.assert_called_once()
        except SystemExit:
            pass

# Generated at 2022-06-14 09:00:50.262852
# Unit test for function main
def test_main():
    sys.argv.append('--alias')
    main()
    assert sys.argv.pop() == '--alias'

# Generated at 2022-06-14 09:00:54.972441
# Unit test for function main
def test_main():
    with patch('thefuck.main.sys.argv', ['thefuck', '--version']), \
         patch('thefuck.main.logs.version') as version:
        main()
        version.assert_called_with(get_installation_info().version,
                                   sys.version.split()[0], shell.info())


# Generated at 2022-06-14 09:01:07.958334
# Unit test for function main
def test_main():
    import sys
    import mock


    from thefuck.main import _main
    from thefuck.argument_parser import Parser


    argv_original = sys.argv
    sys.argv = ['thefuck']
    parsed_args = Parser().parse(['thefuck'])
    sys.argv = argv_original
    

# Generated at 2022-06-14 09:01:18.630455
# Unit test for function main
def test_main():
    import sys
    import os

    class MyParser:
        def parse(self):
            pass

        def print_usage(self):
            pass

        def print_help(self):
            pass

    def mock_fix_command(args):
        print(args.debug)

    def mock_init_output():
        print('Init')

    def mock_parser():
        return MyParser()

    def mock_shell_logger(shell_logger):
        print(shell_logger)

    def mock_logs_warn(message):
        print(message)

    def mock_parser_print_version(version, python_version, shell):
        print(version, python_version, shell)

    def mock_get_installation_info():
        class MockInstallationInfo:
            version = '3.0'

        return Mock

# Generated at 2022-06-14 09:01:31.981639
# Unit test for function main
def test_main():
    import sys
    import os
    import json
    import argparse
    import unittest
    import subprocess
    from ..shells import shell
    from ..system import shell
    from ..utils import get_installation_info
    from ..utils import get_closest

    class TestMain(unittest.TestCase):
        def test_main(self):
            # testing --version
            with self.assertRaises(SystemExit) as version_check:
                main()
            version_check = version_check.exception.code
            self.assertEqual(version_check, None)

            # testing --help
            with self.assertRaises(SystemExit) as help_check:
                main(['thefuck', '--help'])
            help_check = help_check.exception.code
            self.assertEqual

# Generated at 2022-06-14 09:01:36.951898
# Unit test for function main
def test_main():
    class _Args:
        help = True
        def print_help(self):
            pass
        def print_usage(self):
            pass
    parser = Parser()
    def parse(argv):
        return _Args()
    parser.parse = parse
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-14 09:01:37.624296
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-14 09:01:38.344825
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 09:01:42.684644
# Unit test for function main
def test_main():
    sys.argv = [sys.argv[0], '--version']
    main()
    sys.argv = [sys.argv[0], '--help']
    main()

test_main()