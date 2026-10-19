

# Generated at 2022-06-14 08:53:36.717285
# Unit test for function main
def test_main():
    from .utils import mock_input_and_output
    from . import argument_parser_test  # noqa: E402
    from . import command_parser_test  # noqa: E402
    from . import matcher_test  # noqa: E402

# Generated at 2022-06-14 08:53:39.570324
# Unit test for function main
def test_main():
    test_args = ["./thefuck"]
    main()
    assert known_args.help == True

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:53:41.690896
# Unit test for function main
def test_main():
    assert repr(main()) == None


# Generated at 2022-06-14 08:53:53.129964
# Unit test for function main
def test_main():
    import sys
    import unittest
    from unittest.mock import patch

    class KnownArgs:
        def __init__(self, help_, version_, alias_, command_, shell_logger_):
            self.help = help_
            self.version = version_
            self.alias = alias_
            self.command = command_
            self.shell_logger = shell_logger_

    class MockParser:
        def parse(self, argv):
            return KnownArgs(argv[1] == '-h', argv[1] == '-v', argv[1] == 'alias',
                             argv[1] == 'command', argv[1] == 'shell-logger')

        def print_help(self):
            print('help')


# Generated at 2022-06-14 08:53:54.201532
# Unit test for function main
def test_main():
    main()
    assert True

# Generated at 2022-06-14 08:54:01.048078
# Unit test for function main
def test_main():
    import sys, os
    import thefuck.main as main
    sys.argv = ['python3', 'fuck']
    main.main()
    if main.parser.parse(sys.argv).help:
        print('tf_help_test_pass')
    sys.argv = ['python3', 'fuck', '--version']
    main.main()
    if main.known_args.version:
        print('tf_version_test_pass')


# Generated at 2022-06-14 08:54:07.909336
# Unit test for function main
def test_main():
    assert os.environ['TF_HISTORY']=='/home/thomas/.local/share/python-thefuck/history'
    assert os.environ['TF_IGNORE_DIAGNOSTICS']
    assert os.environ['TF_FUCK_INTERACTIVE']

    #assert os.environ['TF_HISTORY']=='/home/thomas/.local/share/python-thefuck/history'
    assert os.environ['TF_IGNORE_DIAGNOSTICS']
    assert os.environ['TF_FUCK_INTERACTIVE']

# Generated at 2022-06-14 08:54:08.712239
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:54:21.663480
# Unit test for function main
def test_main():
    try:
        import pytest  # noqa: F401
    except ImportError:
        return
    sys.argv = ['thefuck', '--help']
    logs.version = mock.Mock()
    main()
    logs.version.assert_not_called()
    sys.argv = ['thefuck', '--version']
    main()
    logs.version.assert_called()
    logs.warn = mock.Mock()
    sys.argv = ['thefuck', '--alias']
    main()
    logs.warn.assert_called()
    sys.argv = ['thefuck', '--command']
    main()
    sys.argv = ['thefuck', '--shell-logger']
    main()

# Generated at 2022-06-14 08:54:28.152050
# Unit test for function main
def test_main():
    from unittest.mock import patch
    from . import alias
    from . import fix_command
    from . import shell_logger
    import os
    import sys

    # test case 1: help
    with patch('sys.argv', ['thefuck','--help']):
        with patch.object(sys, 'stdout', new=io.StringIO()) as stdout:
            with patch.object(sys, 'stderr', new=io.StringIO()) as stderr:
                try:
                    main()
                except SystemExit as e:
                    assert e.code == 0
                    assert stdout.getvalue()
                    assert stderr.getvalue() == ''
        
    # test case 2: version

# Generated at 2022-06-14 08:54:37.691771
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:54:39.225400
# Unit test for function main
def test_main():
    assert eval(repr(main)) == main

# Generated at 2022-06-14 08:54:43.145959
# Unit test for function main
def test_main():
    os.environ['TF_HISTORY'] = 'test'
    sys.argv = ['thefuck', 'fuck']
    main()
    assert isinstance(known_args.command, str)
    assert known_args.command == 'fuck'

# Generated at 2022-06-14 08:54:46.849745
# Unit test for function main
def test_main():
    import sys, os # noqa: F401
    from .shells import shell # noqa: F401

    assert main() == None # noqa: F821


# Generated at 2022-06-14 08:54:58.009172
# Unit test for function main
def test_main():
    from unittest.mock import patch, Mock
    with patch('sys.argv', ['thefuck', '--alias', 'testalias']):
        with patch('thefuck.shells.which',
                   Mock(return_value='testcommand')) as mock_which:
            with patch('thefuck.main.print_alias',
                    Mock(return_value='testalias')) as mock_print_alias:
                main()
                mock_which.assert_called_once_with('testalias')

# Generated at 2022-06-14 08:55:09.350679
# Unit test for function main
def test_main():
    import imp
    from mock import patch

    from .alias import print_alias as mock_print_alias

    with patch.object(Parser, 'parse', autospec=True) as mock_parse:
        mock_parse.return_value = imp.new_module('args')
        mock_parse.return_value.help = False
        mock_parse.return_value.version = False
        mock_parse.return_value.shell_logger = False
        with patch.object(logs, 'version') as mock_logs:
            main()
            mock_logs.assert_called_once_with(get_installation_info().version, sys.version.split()[0], shell.info())

        mock_parse.return_value.version = True


# Generated at 2022-06-14 08:55:09.964941
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:55:12.734584
# Unit test for function main
def test_main():
    return

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:55:13.578493
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:55:20.420237
# Unit test for function main
def test_main():
    import argparse
    arg = argparse.Namespace(command = ['ls'])
    fix_command(arg)

# Generated at 2022-06-14 08:55:42.731097
# Unit test for function main
def test_main():
    assert main()
# Unit Tests for function test_main()
# def test_collect_comments():
#     assert get_installation_info()

# Unit Tests for function test_collect_comments()
# def test_collect_comments():
#     assert get_installation_info()
# Unit Tests for function test_collect_comments()
# def test_collect_comments():
#     assert get_installation_info()

# Generated at 2022-06-14 08:55:43.401062
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:55:43.978877
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:55:45.943139
# Unit test for function main
def test_main():
    assert main() == None

if __name__ == '__main__':
    test_main()

# Generated at 2022-06-14 08:55:52.512304
# Unit test for function main
def test_main():
    import sys
    from mock import patch

    from thefuck.shells.shell import fuck
    from thefuck.types import Command
    patch_argv = patch.object(sys, 'argv', ['thefuck', 'ls']).start()
    patch_fuck = patch('thefuck.main.fuck', return_value='blah').start()
    patch_log = patch('thefuck.main.logs.log', return_value='blah').start()

    main()
    patch_fuck.assert_called_once_with(Command('ls ', ''), None)
    patch_log.assert_called_once_with('blah')



# Generated at 2022-06-14 08:56:07.488584
# Unit test for function main
def test_main():  # noqa: F811
    import sys  # noqa: E402
    from .. import argument_parser  # noqa: E402
    from ..system import init_logging  # noqa: E402
    from ..system import init_settings  # noqa: E402
    from ..utils import get_installation_info  # noqa: E402
    from .alias import print_alias  # noqa: E402
    from .fix_command import fix_command  # noqa: E402
    from .shell_logger import shell_logger  # noqa: E402

    class FakeParser():
        def __init__(self):
            self.help = False
            self.version = False
            self.alias = False
            self.command = None
            self.shell_logger = None


# Generated at 2022-06-14 08:56:20.008222
# Unit test for function main
def test_main():
    # Test help option in function main
    try:
        main()
        assert False
    except SystemExit as e:
        assert e.code == 0
    # Test version option in function main
    try:
        main(['-v'])
        assert False
    except SystemExit as e:
        assert e.code == 0
    # Test alias option in function main
    try:
        main(['-a'])
        assert False
    except SystemExit as e:
        assert e.code == 0
    # Test shell_logger option in function main
    try:
        main(['-s', 'bash'])
        assert False
    except SystemExit as e:
        assert e.code == 0
    # Test no arguments in function main

# Generated at 2022-06-14 08:56:20.766239
# Unit test for function main
def test_main():
    assert main

# Generated at 2022-06-14 08:56:30.762622
# Unit test for function main
def test_main():

    import __main__ as main  # noqa: F401
    main.__package__ = 'thefuck'
    main.__file__ = 'thefuck'
    main.__name__ = 'thefuck'
    main.__doc__ = ''
    main.__spec__ = None
    """
    When we call main(), all the output is printed on stdout, so we substitute
    the original stdout with an object that will store all the information
    written to it.
    """
    out = []
    stdout_object = sys.stdout
    sys.stdout = out
    try:
        main()
    except SystemExit:
        pass
    sys.stdout = stdout_object

# Generated at 2022-06-14 08:56:32.624685
# Unit test for function main
def test_main():
    print("\n#### Running main unit tests ####\n")

# Generated at 2022-06-14 08:57:17.104416
# Unit test for function main
def test_main():
    parser = Parser()
    known_args = parser.parse(['-h'])
    assert known_args.help
    assert not known_args.verbose
    parser = Parser()
    known_args = parser.parse(['-v'])
    assert known_args.verbose
    assert not known_args.help
    parser = Parser()
    known_args = parser.parse(['-a'])
    assert known_args.alias
    assert not known_args.help
    assert not known_args.verbose


if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:57:20.300975
# Unit test for function main
def test_main():
    parser = Parser()
    known_args = parser.parse(sys.argv)
    assert known_args.command


if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:57:21.555788
# Unit test for function main
def test_main():
    assert main(1) == None

# Generated at 2022-06-14 08:57:34.185680
# Unit test for function main
def test_main():
    from .fix_command import mock_fix_command
    from .shell_logger import mock_shell_logger
    from .alias import mock_print_alias
    from . import logs

    parser = Parser()

    # For help
    with patch("thefuck.main.Parser.parse", return_value=argparse.Namespace(
      help=True, version=False, command="", script="")):
        with patch("thefuck.main.parser.print_help") as mock_print_help:
            main()
            assert mock_print_help.called

    # For version

# Generated at 2022-06-14 08:57:35.996811
# Unit test for function main
def test_main():
    sys.argv = ['thefuck', 'thefuck', 'ls']
    main()

# Generated at 2022-06-14 08:57:36.841411
# Unit test for function main
def test_main():

    # TODO: Add test
    return

# Generated at 2022-06-14 08:57:40.470683
# Unit test for function main
def test_main():
    #TODO: check how to test main()
    print("TBD")
    return True

# Generated at 2022-06-14 08:57:41.666907
# Unit test for function main
def test_main():
    print("Nothing to test")

# Generated at 2022-06-14 08:57:42.320521
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:57:55.458325
# Unit test for function main
def test_main():
    # Clearing the environment variables, in case set
    os.environ['TF_HISTORY'] = ''
    os.environ['TF_ALIAS'] = ''

    # Checking if 'help' gets printed
    sys.argv = ['thefuck', '--help']
    main()

    # Checking if version gets printed
    sys.argv = ['thefuck', '--version']
    main()

    # Checking if TF_ALIAS gets printed
    sys.argv = ['thefuck', '--alias']
    main()

    # Checking if TF_ALIAS gets printed with the shell type
    sys.argv = ['thefuck', '--alias', 'bash']
    main()

    # Checking if TF_ALIAS gets printed with the shell name
    sys.argv = ['thefuck', '--alias', 'fish']
    main()

# Generated at 2022-06-14 08:58:59.705124
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:59:01.679858
# Unit test for function main
def test_main():
    sys.argv=['thefuck']
    main()

main()

# Generated at 2022-06-14 08:59:03.240865
# Unit test for function main
def test_main():
    with pytest.raises(SystemExit):
        main()

# Generated at 2022-06-14 08:59:06.747801
# Unit test for function main
def test_main():
    test_command = ['python', '-m', 'thefuck']
    try:
        with open("test_main.txt", "w") as output:
            sys.stdout = output
            main()
    finally:
        sys.stdout = sys.__stdout__

# Generated at 2022-06-14 08:59:12.400176
# Unit test for function main
def test_main():
    from . import __main__
    from unittest import mock
    from ..system import init_output
    init_output()
    with mock.patch.object(__main__.sys, 'argv', ['thefuck']):

        assert __main__.main() is None


# Generated at 2022-06-14 08:59:22.154512
# Unit test for function main
def test_main():
    from ..utils import WrappedPopen, get_aliases_path, get_history_path
    parser = Parser()
    sys.argv = ['thefuck', '--version', '-v']
    main()
    assert sys.argv[1] == '--version'
    assert sys.argv[2] == '-v'
    logs.version(get_installation_info().version,
                 sys.version.split()[0], shell.info())
    sys.argv = ['thefuck', '--alias', 'python']
    main()
    assert sys.argv[1] == '--alias'
    assert sys.argv[2] == 'python'
    with open(get_aliases_path(), 'r') as f:
        lines = f.readlines()
    assert len(lines) == 1

# Generated at 2022-06-14 08:59:25.382978
# Unit test for function main
def test_main():
    test_args = ['fuck', 'ØØ', '-v']
    main(test_args)

# Generated at 2022-06-14 08:59:28.011507
# Unit test for function main
def test_main():
    passed = False
    try:
        main()
        passed = True
    except SystemExit:
        pass

    assert passed == True


# Generated at 2022-06-14 08:59:28.939236
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:59:30.019389
# Unit test for function main
def test_main():
    print("")

# Generated at 2022-06-14 09:01:51.761139
# Unit test for function main
def test_main():
    main()



# Generated at 2022-06-14 09:01:59.164564
# Unit test for function main
def test_main():
    # 0. Ignore all stdout.
    sys.stdout = os.devnull

    # 1. Test alias.
    sys.argv = ['thefuck', 'alias']
    main()

    # 2. Test version.
    sys.argv = ['thefuck', '--version']
    main()

    # 3. Test command with an unknown argument.
    sys.argv = ['thefuck', 'fuck']
    main()

# Generated at 2022-06-14 09:02:00.260013
# Unit test for function main

# Generated at 2022-06-14 09:02:04.912861
# Unit test for function main
def test_main():
    import mock
    import sys
    
    with mock.patch('sys.argv', ['thefuck','--version']):
        main()
        assert sys.argv[1] == '--version'

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 09:02:09.827593
# Unit test for function main
def test_main():
    sys.argv = ['thefuck', 'lol']
    main()

# Generated at 2022-06-14 09:02:12.588810
# Unit test for function main
def test_main():
    test_args = ['-h']
    with mock.patch('sys.argv', test_args):
        main()

test_main()

# Generated at 2022-06-14 09:02:13.776104
# Unit test for function main
def test_main():
    """Tests main function"""
    main()

# Generated at 2022-06-14 09:02:14.469074
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 09:02:23.516109
# Unit test for function main
def test_main():
    from io import StringIO
    import sys
    import os
    import unittest.mock as mock
    from .fix_command import fix_command
    from .alias import print_alias

    test_args = ['-r', '-v']
    tmp_stdout = sys.stdout
    try:
        out = StringIO()
        sys.stdout = out
        main()
        output = out.getvalue().strip()
    finally:
        sys.stdout = tmp_stdout
    assert output == 'thefuck 3.14.0 using Python 3.7.3'

    test_args = ['-h']
    tmp_stdout = sys.stdout

# Generated at 2022-06-14 09:02:34.927757
# Unit test for function main
def test_main():
    from unittest import mock
    from ..argument_parser import mock_arg_parser
    import sys

    with mock.patch.object(sys, 'argv', ['thefuck', '--help']):
        main()
        assert mock_arg_parser.called_print_help

    with mock.patch.object(sys, 'argv', ['thefuck', '--version']):
        main()
        assert mock_arg_parser.called_print_version

    with mock.patch.object(sys, 'argv', ['thefuck', '-h']):
        main()
        assert mock_arg_parser.called_print_help

    with mock.patch.object(sys, 'argv', ['thefuck', '-v']):
        main()
        assert mock_arg_parser.called_print_version
