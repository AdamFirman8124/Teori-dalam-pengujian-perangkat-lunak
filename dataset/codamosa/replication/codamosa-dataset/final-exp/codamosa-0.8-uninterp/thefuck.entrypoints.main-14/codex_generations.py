

# Generated at 2022-06-14 08:53:36.947466
# Unit test for function main
def test_main():
    from unittest import mock
    from thefuck import settings
    from thefuck.settings import load_settings


# Generated at 2022-06-14 08:53:38.544107
# Unit test for function main
def test_main():
    assert main.__code__.co_argcount == 0


# Generated at 2022-06-14 08:53:41.503200
# Unit test for function main
def test_main():
    assert main()=="The Fuck is a magnificent app which corrects your previous console command."

# Generated at 2022-06-14 08:53:46.076642
# Unit test for function main
def test_main():
    try:
        assert main() == "Usage: thefuck [-h] [-v] [-d] [-a {bash,zsh,fish,man,all}] [--alias ALIAS]"
    except:
        print("There was an error!")

# Generated at 2022-06-14 08:53:46.915788
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:53:52.782884
# Unit test for function main
def test_main():
    global parser, known_args
    class mock_parser:
        def __init__(self):
            self.help = True
    parser = mock_parser()
    class mock_known_args:
        def __init__(self):
            self.version = True
            self.alias = True
            self.command = True
            self.shell_logger = True
    known_args = mock_known_args()
    main()

# Generated at 2022-06-14 08:53:56.226230
# Unit test for function main
def test_main():
    pass
    # We need to mock sys.argv to be able to run tests for main function.
    # argv = ['thefuck']
    # with patch('sys.argv', argv):
    #    main()

# Generated at 2022-06-14 08:54:10.077630
# Unit test for function main
def test_main():
    class mock_os_environ:
        def __init__(self):
            self.os_environ = {}
        def __getitem__(self, item):
            return self.os_environ[item]
        def __setitem__(self, key, value):
            self.os_environ[key] = value
        def __len__(self):
            return len(self.os_environ)
        def __iter__(self):
            self.os_environ_keys = list(self.os_environ.keys())
            self.current_iteration = 0
            return self
        def __next__(self):
            if self.current_iteration == len(self.os_environ_keys):
                raise StopIteration
            self.current_iteration += 1
            return self.os_en

# Generated at 2022-06-14 08:54:22.800513
# Unit test for function main
def test_main():
    assert main()
    sys.argv = ['thefuck', '--help']
    assert main()
    sys.argv = ['thefuck', '--version']
    assert main()
    sys.argv = ['thefuck', '--alias', 'fuck']
    assert main()
    sys.argv = ['thefuck', '-v']
    assert main()
    sys.argv = ['thefuck', '--settings=/dev/null',
                '--no-colors', '--require-confirmation', 'echo', '--help']
    assert main()
    sys.argv = ['thefuck', '--shell-logger', 'zsh']
    assert main()
    sys.argv = ['thefuck', 'fuck']
    assert main()

    os.environ['TF_HISTORY'] = 'fuck'

# Generated at 2022-06-14 08:54:24.822821
# Unit test for function main
def test_main():
    # If the error is not printed correctly, then the test will fail.
    main()

# Generated at 2022-06-14 08:54:33.830868
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-14 08:54:40.077241
# Unit test for function main
def test_main():
    parser = Parser()
    # check version
    logs.version(get_installation_info().version,
                 sys.version.split()[0], shell.info())

    # help
    parser.print_help()

    # alias
    print_alias()

    # check known_args
    fix_command()

    # shell_logger
    from .shell_logger import shell_logger
    shell_logger()

# Generated at 2022-06-14 08:54:40.787866
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:54:42.562921
# Unit test for function main
def test_main():
    sys.argv = ['thefuck']
    main()

# Generated at 2022-06-14 08:54:47.007724
# Unit test for function main
def test_main():
    import os
    from .shells.bash import Bash
    from .shells.zsh import Zsh
    from ..utils import MockArgumentParser, MockKnownArgs

    parser = MockArgumentParser()
    known_args = MockKnownArgs()
    os.environ = {'TF_HISTORY':'test'}
    if isinstance(shell, Bash):
        known_args.alias = 'fuck'
    elif isinstance(shell, Zsh):
        known_args.alias = 'f'
    else:
        known_args.alias = ''
    main()

# Generated at 2022-06-14 08:54:58.389002
# Unit test for function main
def test_main():
    # Test help message
    with logs.capture_output() as (out, err):
        main()
    assert out.getvalue().startswith('usage:')
    # Test version message
    with logs.capture_output() as (out, err):
        main(['--version'])
    assert out.getvalue().startswith('The Fuck version')
    assert err.getvalue() == ''
    # Test verbose message
    with logs.capture_output() as (out, err):
        main(['-v'])
    assert out.getvalue() == ''
    assert err.getvalue().startswith('DEBUG:')
    # Test error message if no command is passed
    with logs.capture_output() as (out, err):
        main([])
    assert out.getvalue() == ''

# Generated at 2022-06-14 08:55:11.650764
# Unit test for function main
def test_main():
    from unittest.mock import patch  # noqa: E402
    from io import StringIO  # noqa: E402
    from .. import utils  # noqa: E402
    from ..shells import get_aliases  # noqa: E402

    expected_exception = RuntimeError('Expected error')

    mock_fix_command = patch('thefuck.main.fix_command').start()
    mock_print_alias = patch('thefuck.main.print_alias').start()
    mock_print_usage = patch('thefuck.main.Parser.print_usage').start()
    mock_print_help = patch('thefuck.main.Parser.print_help').start()
    mock_version = patch('thefuck.main.logs.version').start()

# Generated at 2022-06-14 08:55:26.471786
# Unit test for function main
def test_main():
    from .alias import test_main as test_alias
    from .fix_command import test_main as test_fix_command

    from unittest.mock import patch

    with patch('thefuck.main.print_alias') as mock_print_alias, \
            patch('thefuck.main.fix_command') as mock_fix_command, \
            patch('thefuck.main.logs.version') as mock_logs_version, \
            patch('thefuck.main.logs.warn') as mock_logs_warn, \
            patch('thefuck.main.logs.write') as mock_logs_write:
        sys.argv = ['thefuck', '--alias']
        main()
        test_alias(mock_print_alias)


# Generated at 2022-06-14 08:55:30.978448
# Unit test for function main
def test_main():
    parser = Parser()
    known_args = parser.parse(sys.argv)
    assert known_args.help == True
    assert known_args.version == False
    assert known_args.alias == False
    assert known_args.command == False
    assert known_args.shell_logger == False

# Generated at 2022-06-14 08:55:31.601997
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-14 08:55:48.410824
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:55:48.973070
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:55:50.223266
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:55:56.068573
# Unit test for function main
def test_main():
    sys.argv = ['fuck']
    main()
    sys.argv = ['fuck', 'command']
    main()
    sys.argv = ['-v']
    main()
    sys.argv = ['-h']
    main()
    sys.argv = ['-a']
    main()
    sys.argv = ['--shell-logger=']
    main()

# Generated at 2022-06-14 08:55:56.791164
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:56:09.184177
# Unit test for function main

# Generated at 2022-06-14 08:56:10.237726
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-14 08:56:12.116768
# Unit test for function main
def test_main():
    sys.argv=['fuck', '--version']
    main()
    assert True

# Generated at 2022-06-14 08:56:15.431281
# Unit test for function main
def test_main():
    expected = Parser()
    known_args = expected.parse(sys.argv)

    assert Parser() == expected
    assert known_args == known_args

# Generated at 2022-06-14 08:56:17.181829
# Unit test for function main
def test_main():
    assert main()==None

# Generated at 2022-06-14 08:56:49.587199
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-14 08:56:50.364571
# Unit test for function main
def test_main():
    assert main()

# Generated at 2022-06-14 08:56:51.110101
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:57:01.894471
# Unit test for function main
def test_main():
    from unittest.mock import patch, MagicMock
    from .fix_command import FixCommand
    from .alias import print_alias
    from .shell_logger import shell_logger
    import sys
    import os

    # Check if parser.print_help() is called
    help_args = ['thefuck', '--help']
    with patch('thefuck.main.Parser') as parser_mock:
        main()
        parser_mock.assert_called_once_with()
        sys.argv = help_args
        parser_mock.return_value.parse.return_value = MagicMock(help=True)
        main()
        parser_mock.return_value.print_help.assert_called_once_with()

    # Check if logs.version is called

# Generated at 2022-06-14 08:57:02.594791
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-14 08:57:08.007418
# Unit test for function main
def test_main():
    if __name__ == '__main__':
        main()

# Generated at 2022-06-14 08:57:12.923506
# Unit test for function main
def test_main():
    args = ['echo', 'hoho', '--help', '--version', '--alias', '--shell-logger']
    main(args)

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:57:14.823894
# Unit test for function main
def test_main():
    if __name__ == '__main__':
        main()

# Generated at 2022-06-14 08:57:22.583180
# Unit test for function main
def test_main():
    sys.argv = ['./thefuck','--version']
    main()
    sys.argv = ['./thefuck','--help']
    main()
    sys.argv = ['./thefuck','--alias','bash']
    main()
    sys.argv = ['./thefuck','--command', 'ls -l']
    main()
    sys.argv = ['./thefuck','--shell_logger','bash']
    main()

# Generated at 2022-06-14 08:57:25.326114
# Unit test for function main
def test_main():
    if __name__ == '__main__':
        main()

# Generated at 2022-06-14 08:58:38.717843
# Unit test for function main
def test_main():
    with patch('sys.argv', ['thefuck', '--h']), \
            patch('logging.basicConfig') as mock_basic_config, \
            patch('thefuck.argument_parser.Parser.print_help') as mock_print_help, \
            patch('thefuck.argument_parser.Parser.print_usage') as mock_print_usage:
        main()
        assert mock_basic_config.call_args[0][0] == 2
        mock_print_help.assert_called()
        assert not mock_print_usage.called


# Generated at 2022-06-14 08:58:43.038305
# Unit test for function main
def test_main():
    class Args(object):
        pass
    args = Args()
    args.help = False
    args.version = True
    args.alias = True
    os.environ['TF_HISTORY'] = '100'

    main(args)
    assert 0

# Generated at 2022-06-14 08:58:45.726575
# Unit test for function main
def test_main():
    assert main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:58:46.396461
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-14 08:58:48.999337
# Unit test for function main
def test_main():
    try:
        main()
    except SystemExit:
        assert True
    else:
        assert False

# Generated at 2022-06-14 08:58:50.600081
# Unit test for function main
def test_main():
    assert main() == None
if __name__ == "__main__":
    main()

# Generated at 2022-06-14 08:58:55.063125
# Unit test for function main
def test_main():
    f = open('./testdata/alias_output.txt', 'r')
    sys.stdout = f
    main()
    f.close()

if  __name__ != '__main__':
    print('Run test cases: python3 -m unittest -v thefuck.main')

# Generated at 2022-06-14 08:59:06.959972
# Unit test for function main
def test_main():
    from . import __main__
    from unittest.mock import patch

    with patch.object(__main__, 'fix_command') as fix_command_mock, \
         patch.object(__main__, 'print_alias') as print_alias_mock:
        __main__.main()
        assert not fix_command_mock.called
        assert not print_alias_mock.called

        os.environ['TF_HISTORY'] = 'tf-history-value'
        __main__.main()
        assert fix_command_mock.called
        assert not print_alias_mock.called


# Generated at 2022-06-14 08:59:09.025828
# Unit test for function main
def test_main():
    parser = Parser()
    known_args = parser.parse(sys.argv)

# Generated at 2022-06-14 08:59:10.779447
# Unit test for function main
def test_main():
    # Test the main function
    main()

# Generated at 2022-06-14 09:01:30.553498
# Unit test for function main
def test_main():
    arg_list = ['-v']
    main()
    main(arg_list)

# Generated at 2022-06-14 09:01:42.940467
# Unit test for function main
def test_main():
    with patch('os.environ', {'TF_HISTORY': None}):
        with patch.object(Parser, 'parse') as mock_parse:
            with patch.object(Parser, 'print_usage') as mock_print_usage:
                with patch.object(Parser, 'print_help') as mock_print_help:
                    from ..utils import get_installation_info, logs
                    from ..shells import shell
                    from .alias import print_alias
                    from .fix_command import fix_command

                    mock_parse.return_value = MagicMock(version=False, help=False, alias=False, shell_logger=False, command=False)
                    main()
                    mock_print_usage.assert_called()


# Generated at 2022-06-14 09:01:43.638370
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 09:01:51.253066
# Unit test for function main
def test_main():
    import io
    import os
    import sys
    import unittest
    from unittest.mock import patch

    class MainTests(unittest.TestCase):
        def setUp(self):
            self._io = io.StringIO()
            sys.stdout = self._io
            self.save = os.environ.copy()

        def test_not_display_usage_and_help_and_version_and_alias_and_shell_logger(self):
            with patch('sys.argv', ['thefuck']):
                main()
            self._io.seek(0)
            self.assertEqual(self._io.read(), 'Usage: thefuck [OPTIONS]\nTry "thefuck --help" for help.\n')


# Generated at 2022-06-14 09:01:53.541703
# Unit test for function main
def test_main():
    main()
if __name__ == "__main__":
    main()

# Generated at 2022-06-14 09:02:04.230138
# Unit test for function main

# Generated at 2022-06-14 09:02:18.996513
# Unit test for function main
def test_main():
    import sys
    import io
    import contextlib
    sys.stdout = io.StringIO() # redirect stdout
    parser = Parser()
    args = parser.parse(['--help'])
    main()
    assert(sys.stdout.getvalue() == parser.format_help()+"\n")
    sys.stdout = io.StringIO()
    args = parser.parse(['--version'])
    main()
    assert(sys.stdout.getvalue() == "thefuck "+get_installation_info().version+"\n")
    sys.stdout = io.StringIO()
    args = parser.parse(['git','push'])
    main()
    

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 09:02:19.756350
# Unit test for function main
def test_main():
    assert callable(main)


# Generated at 2022-06-14 09:02:20.618848
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 09:02:22.313135
# Unit test for function main
def test_main():
    assert main() == None
if __name__ == '__main__':
    main()