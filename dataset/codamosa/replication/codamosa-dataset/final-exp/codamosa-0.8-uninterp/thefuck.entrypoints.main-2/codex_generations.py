

# Generated at 2022-06-14 08:53:32.052977
# Unit test for function main
def test_main():
	observed_output_result = main()
	assert "fuck" in observed_output_result

# Generated at 2022-06-14 08:53:33.168896
# Unit test for function main
def test_main():
    assert main()==True

# Generated at 2022-06-14 08:53:45.854327
# Unit test for function main
def test_main():
    import unittest.mock
    from . import test_helpers
    mTest = unittest.mock.Mock()
    mTest.command = "fuck"
    mTest.history = ["fuck"]

# Generated at 2022-06-14 08:53:46.561271
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:53:47.614630
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:53:48.321045
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:53:50.073077
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:53:50.930629
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:53:51.695866
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-14 08:53:52.817855
# Unit test for function main
def test_main():
    print(main.__doc__)

# Generated at 2022-06-14 08:54:01.486113
# Unit test for function main
def test_main():
  main()

# Generated at 2022-06-14 08:54:15.746072
# Unit test for function main
def test_main():
    parser = Parser()
    known_args = parser.parse(sys.argv)
    print(known_args)
    if known_args.help:
        print("print_help")
    elif known_args.version:
        logs.version(get_installation_info().version, sys.version.split()[0], shell.info())
    # It's important to check if an alias is being requested before checking if
    # `TF_HISTORY` is in `os.environ`, otherwise it might mess with subshells.
    # Check https://github.com/nvbn/thefuck/issues/921 for reference
    elif known_args.alias:
        print_alias(known_args)

# Generated at 2022-06-14 08:54:18.241612
# Unit test for function main
def test_main():
    print ("main function testing starts")

    assert known_args.command == "pwd"

# Generated at 2022-06-14 08:54:19.452132
# Unit test for function main
def test_main():
    main()
    assert 1 == 1

# Generated at 2022-06-14 08:54:20.972871
# Unit test for function main
def test_main():
    os.environ['TF_HISTORY'] = "abc"
    main()

# Generated at 2022-06-14 08:54:22.481582
# Unit test for function main
def test_main():
    import thefuck
    assert_equal(thefuck.__main__.main(), 0)

# Generated at 2022-06-14 08:54:23.028118
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:54:29.140523
# Unit test for function main
def test_main():
    import unittest.mock as mock

    with mock.patch('thefuck.main.fix_command'), \
            mock.patch('thefuck.main.print_alias'), \
            mock.patch('thefuck.main.Parser', return_value=['parser']):
        main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:54:29.782609
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:54:31.143485
# Unit test for function main
def test_main():
    assert main() == main()

# Generated at 2022-06-14 08:54:58.094292
# Unit test for function main
def test_main():
    from unittest.mock import patch
    from .shell_logger import __name__ as shell_logger_name
    import io
    import sys

    args = [sys.argv[0], '--version']
    with patch.object(sys, 'argv', args):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            main()
            assert fake_stdout.getvalue() == ("The Fuck {} using Python {}\n"
                                              "Shell: {}\n").format(
                                                  get_installation_info().version,
                                                  sys.version.split()[0],
                                                  shell.info())

    args = [sys.argv[0], '--alias']

# Generated at 2022-06-14 08:55:01.920833
# Unit test for function main
def test_main():
    from .main import main
    from .argument_parser import Parser

    parser = Parser()
    known_args = parser.parse(sys.argv)

    main()

# Generated at 2022-06-14 08:55:03.232393
# Unit test for function main
def test_main():
    main()
    
test_main()

# Generated at 2022-06-14 08:55:14.074727
# Unit test for function main
def test_main():
    from .argument_parser import build_parser, print_help
    from .debug import debug_settings
    from .alias import print_alias
    args = build_parser().parse_args(['--version'])
    main  # force side effect: init_output
    main()
    args = build_parser().parse_args(['--help'])
    main  # force side effect: init_output
    main()
    args = build_parser().parse_args(['--alias', 'fuck'])
    main  # force side effect: init_output
    main()
    import os
    os.environ['TF_HISTORY'] = '''/var/folders/2y/5j5d9sf55vz8389f41jd1zc00000gn/T/tmpm8wxd4a4'''

# Generated at 2022-06-14 08:55:18.571943
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:55:27.186281
# Unit test for function main
def test_main():
    main()
    main_true_help()
    main_true_version()
    main_true_alias()
    main_true_command()
    main_true_shell_logger()


# Generated at 2022-06-14 08:55:28.042393
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:55:38.029891
# Unit test for function main
def test_main():
    import mock
    import unittest

    class TestMain(unittest.TestCase):
        @mock.patch('thefuck.main.Parser')
        def test_invalid_args(self, mock_parser):
            mock_parser.return_value.parse.return_value = 'invalid_args'
            mock_parser.return_value.print_usage.return_value = None
            main()
            mock_parser.return_value.parse.assert_called_once()
            mock_parser.return_value.print_usage.assert_called_once()

        @mock.patch('thefuck.main.Parser')
        def test_valid_args(self, mock_parser):
            mock_parser.return_value.parse.return_value = 'valid_args'
            mock_parser.return_value.print_

# Generated at 2022-06-14 08:55:38.763469
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:55:41.370264
# Unit test for function main
def test_main():
    os.environ['TF_HISTORY'] = 'true'
    known_args = Parser().parse(sys.argv)
    fix_command(known_args)

# Generated at 2022-06-14 08:56:27.901067
# Unit test for function main
def test_main():
    os.environ['TF_HISTORY'] = "cd"
    assert main() is None
    os.environ['TF_HISTORY'] = "cd.."
    assert main() is None
    os.environ['TF_HISTORY'] = "cd../"
    assert main() is None
    os.environ['TF_HISTORY'] = "cd ."
    assert main() is None
    os.environ['TF_HISTORY'] = "cd . "
    assert main() is None
    os.environ['TF_HISTORY'] = "cd ."
    assert main() is None
    os.environ['TF_HISTORY'] = "mkdir"
    assert main() is None
    os.environ['TF_HISTORY'] = "pip install"
    assert main() is None

# Generated at 2022-06-14 08:56:29.612652
# Unit test for function main
def test_main():
    assert callable(main)

# Generated at 2022-06-14 08:56:31.466813
# Unit test for function main
def test_main():
    assert main() is not None


if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:56:32.089754
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:56:33.558115
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:56:35.070037
# Unit test for function main
def test_main():
    try:
        main()
    except SystemExit:
        pass

# Generated at 2022-06-14 08:56:37.365655
# Unit test for function main
def test_main():
    if main=="":
        assert True
    else:
        assert False

# Generated at 2022-06-14 08:56:40.161149
# Unit test for function main
def test_main():
    try:
        repr(main())
    except:
        print("test for main function has something wrong")

test_main()

# Generated at 2022-06-14 08:56:43.225725
# Unit test for function main
def test_main():
    try:
        main()
    except Exception:
        raise AssertionError("Failed in main()")

# Test if the function is called

# Generated at 2022-06-14 08:56:55.724889
# Unit test for function main
def test_main():
    # Initialize output before importing any module, that can use colorama.
    from ..system import init_output

    init_output()

    from .alias import print_alias
    from .fix_command import fix_command

    print_alias_origin, fix_command_origin = print_alias, fix_command

    print_alias.side_effect = print_alias_origin
    fix_command.side_effect = fix_command_origin

    try:
        from .shell_logger import shell_logger
    except ImportError:
        shell_logger = None

    shell_logger_origin = shell_logger

    shell_logger_origin.side_effect = shell_logger

    main()

    # Test for alias
    sys.argv = ['thefuck', '--alias']
    main()

# Generated at 2022-06-14 08:58:02.890143
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-14 08:58:07.753183
# Unit test for function main
def test_main():
    import sys
    import os
    sys.argv = ["thefuck",  "git commit", "--no-color", "--debug"]
    main()
    assert "git commit" in os.environ["TF_HISTORY"]

# Generated at 2022-06-14 08:58:08.535767
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-14 08:58:09.560071
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:58:10.288024
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:58:10.926139
# Unit test for function main
def test_main():
    return True

# Generated at 2022-06-14 08:58:19.838186
# Unit test for function main
def test_main():
    mock_version = 'mock version'
    sys.argv = [
        sys.argv[0],
        '-v',
    ]
    with patch('..utils.get_installation_info') as mock_info:
        with patch('thefuck.logs.version') as mock_logs:
            mock_info.return_value = Mock(version=mock_version)
            main()
            mock_info.assert_called_with()
            mock_logs.assert_called_with(mock_version, ANY, ANY)

# Generated at 2022-06-14 08:58:21.531384
# Unit test for function main
def test_main():
    # TODO: Find out how to unit test function main
    pass

# Generated at 2022-06-14 08:58:29.829408
# Unit test for function main
def test_main():
    import sys
    sys.argv = ['tf']
    main()
    sys.argv = ['tf', '--version']
    main()
    sys.argv = ['tf', '--help']
    main()
    sys.argv = ['tf', '--shell', 'zsh']
    main()
    sys.argv = ['tf', '-l', 'zsh']
    main()
    sys.argv = ['tf', '--alias', 'alias']
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:58:40.755538
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

# Generated at 2022-06-14 09:01:01.650873
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 09:01:02.615256
# Unit test for function main
def test_main():
    assert main is not None

# Generated at 2022-06-14 09:01:03.659945
# Unit test for function main
def test_main():
    # Test for main function
    main()

# Generated at 2022-06-14 09:01:06.316269
# Unit test for function main
def test_main():
    from .. import main as main_function
    main_function()
    assert (1 + 1) == 2

# Generated at 2022-06-14 09:01:07.419285
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 09:01:08.756324
# Unit test for function main
def test_main():  # noqa: D103
    assert main() is None

# Generated at 2022-06-14 09:01:10.941659
# Unit test for function main
def test_main():
    sys.argv = ["thefuck", "--version"]
    main()


# Generated at 2022-06-14 09:01:11.883804
# Unit test for function main
def test_main():
    assert main() is not None

# Generated at 2022-06-14 09:01:14.619442
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 09:01:27.173355
# Unit test for function main
def test_main():

    # Mocks
    class ParserMock():
        def parse(self, argv):
            return argv
        def print_help(self):
            return
        def print_usage(self):
            return

    class SystemMock(object):
        class ModuleMock(object):
            @classmethod
            def version(cls, version_string, version_info, shell_info):
                return

    class ShellMock(object):
        @classmethod
        def fix_command(cls, shell_logger, _time=5):
            return

        @classmethod
        def info(cls):
            return

    class ArgparseMock(object):
        def __init__(self):
            self.help = False
            self.version = False
            self.alias = ''
            self.command = ''
           