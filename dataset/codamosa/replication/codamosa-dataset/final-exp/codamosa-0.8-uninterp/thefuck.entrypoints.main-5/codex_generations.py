

# Generated at 2022-06-14 08:53:35.551710
# Unit test for function main
def test_main():
    from unittest.mock import patch
    from . import argument_parser as parser

    with patch('sys.argv', ['tf', '--version']):
        with patch.object(parser.Parser, 'parse') as mock_parse:
            with patch('thefuck.logs.version') as mock_version:
                with patch('thefuck.utils.get_installation_info') as mock_info:
                    with patch('thefuck.shells.shell.info'):
                        main()
                        assert mock_parse.called
                        assert mock_version.called
                        assert mock_info.called


# Generated at 2022-06-14 08:53:36.335781
# Unit test for function main
def test_main():
    ImportError
    pass

# Generated at 2022-06-14 08:53:38.115487
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:53:38.757869
# Unit test for function main
def test_main():
    assert main is not None

# Generated at 2022-06-14 08:53:41.755438
# Unit test for function main
def test_main():
    assert main() is None

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:53:42.621395
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-14 08:53:48.319628
# Unit test for function main
def test_main():
    parser = Parser()
    known_args = parser.parse(['--version'])
    logs.version("0.1.1", "0.1.1.dev", "shell")
    #known_args = parser.parse(['--help'])


if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:54:01.095003
# Unit test for function main
def test_main():
    def shell_logger_mock(shell_name):
        return True

    from ..shells import shell
    from .shell_logger import shell_logger
    from .alias import print_alias
    from .fix_command import fix_command

    import os

    original_shell_logger = shell_logger
    original_print_alias = print_alias
    original_fix_command = fix_command
    original_shell = shell.name
    original_environ = dict(os.environ)
    os.environ['TF_HISTORY'] = '1'


# Generated at 2022-06-14 08:54:02.412822
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:54:03.168349
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:54:12.072381
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-14 08:54:17.114860
# Unit test for function main
def test_main():
    try:
        main()
    except:
        assert False
    try:
        main()
    except:
        assert False
    try:
        main()
    except:
        assert False
    try:
        main()
    except:
        assert False

# Generated at 2022-06-14 08:54:19.506004
# Unit test for function main
def test_main():
   import sys
   sys.argv=['tf', 'ls', './test']
   assert main() == 0

# Generated at 2022-06-14 08:54:20.145799
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:54:21.349830
# Unit test for function main
def test_main():
    """
    Test for function main
    """
    assert main() == None

# Generated at 2022-06-14 08:54:23.065725
# Unit test for function main
def test_main():
	main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:54:23.865611
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:54:25.281765
# Unit test for function main
def test_main():
    assert main() == sys.exit(0)

# Generated at 2022-06-14 08:54:26.977213
# Unit test for function main
def test_main():
    main()
    assert True

# Generated at 2022-06-14 08:54:27.761524
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:54:44.585023
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:54:47.104979
# Unit test for function main
def test_main():
    assert init_output() == None
    
    
if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:54:58.424332
# Unit test for function main
def test_main():
    from unittest import mock

    with mock.patch('sys.argv', ['thefuck']),\
     mock.patch('thefuck.main.Parser.parse'),\
     mock.patch('thefuck.main.Parser.print_usage'):
        main()
        assert Parser.parse().print_usage.called
    with mock.patch('sys.argv', ['thefuck', '-h']),\
     mock.patch('thefuck.main.Parser.parse'),\
     mock.patch('thefuck.main.Parser.print_help'):
        main()
        assert Parser.parse().print_help.called

# Generated at 2022-06-14 08:55:01.615741
# Unit test for function main
def test_main():
    sys.argv = [sys.argv[0], '-v']
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:55:02.977120
# Unit test for function main
def test_main():
    sys.argv = ['-h']
    main()

# Generated at 2022-06-14 08:55:04.063798
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:55:11.993482
# Unit test for function main
def test_main():
    class mock_known_args():
        def __call__(self):
            self.alias = False
            self.command = False
            self.help = False
            self.version = False
            self.shell_logger = None
    known_args = mock_known_args()
    os.environ['TF_HISTORY'] = 'true'
    main()
    os.environ.pop('TF_HISTORY')

    known_args.alias = True
    main()
    main()

    main()

    main()

# Generated at 2022-06-14 08:55:26.316471
# Unit test for function main
def test_main():
    with mock.patch('thefuck.main.init_output') as p1:
        with mock.patch('thefuck.system.os') as p2:
            with mock.patch('thefuck.main.Parser') as p3:
                p3().parse.return_value = argparse.Namespace(
                    help=False,
                    version=False,
                    alias=False,
                    command=True,
                    shell_logger=False)
                p3().print_usage.return_value = 'default'
                p2.environ = {}
                main()
            assert p1.called
            assert p2.path.exists.called
            assert p2.path.isfile.called
            assert p3().parse.called
            assert p3().print_usage.called

# Generated at 2022-06-14 08:55:27.052985
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-14 08:55:28.050824
# Unit test for function main
def test_main():
    assert main() != None

# Generated at 2022-06-14 08:56:07.226895
# Unit test for function main
def test_main():

    with patch('thefuck.main.Parser'):
        with patch('thefuck.main.logs'):
            with patch('thefuck.main.print_alias'):
                with patch('thefuck.main.fix_command'):
                    with patch('thefuck.main.shell_logger'):
                        with patch('thefuck.main.os'):
                            import thefuck.main
                            thefuck.main.main()

# Generated at 2022-06-14 08:56:07.942195
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:56:08.678862
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:56:11.257104
# Unit test for function main
def test_main():
    sys.argv += ['--version']
    # import doctest
    # doctest.testmod()
    main()

# Generated at 2022-06-14 08:56:12.700443
# Unit test for function main
def test_main():
    import sys
    sys.argv = ["thefuck"]
    main()

# Generated at 2022-06-14 08:56:15.099021
# Unit test for function main
def test_main():
	try:
		if __name__ == "__main__":
			main()
	except Exception as e:
		return e

# Generated at 2022-06-14 08:56:17.385717
# Unit test for function main
def test_main():
    assert main() is None
main()

# Generated at 2022-06-14 08:56:29.623358
# Unit test for function main
def test_main():
    from . import main
    from . import fix_command
    from ..argument_parser import Parser
    from unittest.mock import patch
    main.sys.argv = ["thefuck"]
    with patch.object(main.argument_parser.Parser, 'parse', return_value=Parser().parse(["thefuck"])):
        with patch.object(main, 'print_alias', return_value=None) as mock_print_alias:
            with patch.object(main, 'fix_command', return_value=None) as mock_fix_command:
                main.main()
                mock_print_alias.assert_called_once()
                mock_fix_command.assert_called_once()
    main.sys.argv = ["thefuck", "--alias", "nonexistent"]

# Generated at 2022-06-14 08:56:30.220836
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:56:31.677449
# Unit test for function main
def test_main():
    # Test calling main with argument --help
    main(sys.argv)

# Generated at 2022-06-14 08:57:43.289634
# Unit test for function main
def test_main():
    from .shell_logger import main as shell_main # noqa: E402
    from .history import main as history_main # noqa: E402
    from test.shells import Shell   # noqa: E402
    from test.utils import support_dir_path   # noqa: E402
    logging.basicConfig(format='%(message)s', level=logging.INFO, stream=sys.stderr)
    _argv = [support_dir_path('commands/load_file'), '--settings', support_dir_path('settings/shell_logger.py')]
    _argv1 = [support_dir_path('commands/load_file'), '--settings', support_dir_path('settings/history_logger.py')]
    _argv_version = ['--version']

# Generated at 2022-06-14 08:57:58.818297
# Unit test for function main
def test_main():
	import pytest
	from tests.factories.pytest_factory import pytest_factory
	from unittest.mock import patch, MagicMock
	from sys import platform

	import thefuck

	with patch('thefuck.shells.is_posix', return_value=True):
		with patch('thefuck.logs.info') as mock_info:
			with patch('thefuck.logs.warn') as mock_warn:
				with patch('thefuck.main.print_alias'):
					known_args = MagicMock()
					known_args.help = False
					known_args.version = False
					known_args.alias = True
					known_args.command = True
				

# Generated at 2022-06-14 08:58:03.848694
# Unit test for function main
def test_main():
    from . import sys as _sys
    from . import os as _os
    from . import Parser, print_alias, fix_command
    from .utils import get_installation_info
    from .shells import shell
    from . import logs
    from unittest.mock import patch

# Generated at 2022-06-14 08:58:12.354799
# Unit test for function main
def test_main():
    from unittest.mock import patch
    import os
    from . import utils
    from .. import argument_parser as parser


# Generated at 2022-06-14 08:58:13.069954
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:58:14.766898
# Unit test for function main
def test_main():
    assert main() == None

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:58:16.430629
# Unit test for function main
def test_main():
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:58:17.476602
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:58:18.471013
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:58:24.672054
# Unit test for function main
def test_main():
    with patch('sys.argv', ['thefuck', '--alias=a']):
        with patch('thefuck.shells.get_shell') as shell_mock:
            main()
            shell_mock().app_alias.assert_called_once_with('a')


# Generated at 2022-06-14 09:00:39.249675
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 09:00:42.733794
# Unit test for function main
def test_main():
    """
    Check that standard flow works fine for `thefuck --help`
    """
    test_args = ['./bin/thefuck', '--help']
    main()
    assert sys.argv == test_args

# Generated at 2022-06-14 09:00:55.365211
# Unit test for function main
def test_main():
    from ..apps import Interpreter  # noqa: E402
    from ..utils import create_subshell_command  # noqa: E402
    from ..shells import get_shell  # noqa: E402
    from ..utils import wait_subprocess_running
    from ..utils import replace_argument
    from ..utils import split_command
    old_subshell = get_shell().subshell

    def subshell(new_environ):
        old_subshell(new_environ).stdin.write(b'echo 42\n')

    get_shell().subshell = subshell
    old_subprocess_popen = os.subprocess.Popen


# Generated at 2022-06-14 09:01:08.007155
# Unit test for function main
def test_main():

    # Mock sys.argv and os.environ to run the main() function
    sys.argv = ['thefuck', '--help']
    os.environ["TF_CLI_HISTORY_LENGTH"] = "2"
    os.environ["TF_CLI_PREVIEW_COMMAND"] = "1"
    os.environ["TF_SHELL_COMMAND_DELIMITER"] = ";"
    os.environ["TF_SHELL_COMMAND_DELIMITER_REQUIRED"] = "1"
    os.environ["TF_SHELL_COMMAND_DELIMITER_IGNORE_SPACE_AFTER_DELIMITER"] = "1"

# Generated at 2022-06-14 09:01:20.841709
# Unit test for function main
def test_main():
    from io import StringIO
    from ..utils import get_all_rules  # noqa: E402
    from .alias import _print_alias  # noqa: E402

    def test_version(version, python_version, shell_info):
        assert version == get_installation_info().version
        assert python_version == sys.version.split()[0]
        assert shell_info == shell.info()

    logs.version.side_effect = test_version
    logs.force_open_log = lambda: None
    _print_alias.side_effect = Exception
    f = StringIO()
    with patch('sys.stdout', f):
        main()
        main()
        main()
        main()
        main()
        main()
        main()

# Generated at 2022-06-14 09:01:33.371132
# Unit test for function main
def test_main():
    import sys  # noqa: E402
    import os  # noqa: E402
    parser = Parser()

    # Test help option is working
    sys.argv.append('-h')
    parser.parse(sys.argv)
    # Test shell option is working
    sys.argv.append('-l')
    parser.parse(sys.argv)
    # Test version option is working
    sys.argv.append('-V')
    parser.parse(sys.argv)
    # Test alias option is working
    sys.argv.append('-a')
    parser.parse(sys.argv)
    # Test command working with the given option
    sys.argv.append('-c')
    parser.parse(sys.argv)

    from .shell_logger import shell_logger 

# Generated at 2022-06-14 09:01:34.034677
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 09:01:37.376873
# Unit test for function main
def test_main():
    # This function has no tests. It's quite hard to mock argv.
    # You need to install pytest-mock to test this function
    pass

# Generated at 2022-06-14 09:01:38.126033
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-14 09:01:41.765781
# Unit test for function main
def test_main():
    from mock import patch, Mock

    with patch('sys.argv', [__file__]):
        with patch('sys.stdout', Mock()):
            main()


if __name__ == '__main__':
    main()