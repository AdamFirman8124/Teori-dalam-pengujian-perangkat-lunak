

# Generated at 2022-06-14 08:53:28.929407
# Unit test for function main
def test_main():    
    main()

# Generated at 2022-06-14 08:53:37.249164
# Unit test for function main
def test_main():
    from .core.config import RuntimeConfig
    from .core.shells import Zsh, Bash

    def fake_config(): return RuntimeConfig(set(), {})
    def fake_shell():
        class Shell:
            def __init__(self, name):
                self.name = name

        return Shell('zsh')

    import sys
    sys.argv = ['thefuck', '--help']
    main()

    sys.argv = ['thefuck', '--version']
    main()

    sys.argv = ['thefuck', '--shell']
    main()

    sys.argv = ['thefuck', '--shell-logger']
    main()

    sys.argv = ['thefuck', 'fuck']
    main()

    sys.argv = ['thefuck', '--alias']
    main()

# Generated at 2022-06-14 08:53:48.258695
# Unit test for function main
def test_main():
    from signal import SIG_DFL  # noqa: E402
    from signal import signal  # noqa: E402
    from io import StringIO
    from contextlib import redirect_stderr  # noqa: E402
    from contextlib import redirect_stdout  # noqa: E402
    from unittest.mock import patch  # noqa: E402
    from .test_utils import make_configured_env  # noqa: E402

    from .. import __version__  # noqa: E402
    from ..shells import Shell  # noqa: E402

    test_command = 'test'

# Generated at 2022-06-14 08:53:50.069248
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:53:51.915129
# Unit test for function main
def test_main():
    assert main() == None

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:54:02.826877
# Unit test for function main
def test_main():
    from unittest.mock import patch

    with patch('thefuck.main.ArgumentParser') as ArgumentParser:
        with patch('thefuck.main.print_alias') as print_alias:
            with patch('thefuck.main.fix_command') as fix_command:
                main()
                ArgumentParser.return_value.parse.assert_called_once_with(['thefuck'])
                ArgumentParser.return_value.print_help.assert_called_once_with()
                print_alias.assert_not_called()
                fix_command.assert_not_called()

    with patch('thefuck.main.ArgumentParser') as ArgumentParser:
        with patch('thefuck.main.print_alias') as print_alias:
            with patch('thefuck.main.fix_command') as fix_command:
                ArgumentParser

# Generated at 2022-06-14 08:54:03.807636
# Unit test for function main
def test_main():
    sys.argv = ["thefuck"]
    main()

# Generated at 2022-06-14 08:54:07.387079
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-14 08:54:08.306347
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-14 08:54:11.087321
# Unit test for function main
def test_main():
    os.environ['TF_HISTORY'] = './tests/comma'
    main()
    assert os.environ['TF_HISTORY'] == './tests/comma'

# Generated at 2022-06-14 08:54:26.769247
# Unit test for function main
def test_main():
    from .utils import set_env, get_env
    from .utils import get_temp_filename

    # set environment variable
    set_env('TF_HISTORY', get_temp_filename())
    # check if an alias is being requested
    assert known_args.alias == print_alias(known_args)

    # check if an otherwise is being requested
    assert known_args.command or 'TF_HISTORY' in os.environ == \
                                    fix_command(known_args)

    # check if a 'shell_logger' is being requested
    from .shell_logger import shell_logger
    assert known_args.shell_logger == shell_logger(known_args.shell_logger)
    # check if a 'parser.print_usage' is being requested

# Generated at 2022-06-14 08:54:39.333783
# Unit test for function main
def test_main():
    output = mock.Mock()

    argv = ['thefuck']
    with mock.patch('sys.argv', argv):
        with mock.patch('thefuck.argument_parser.Parser'):
            with mock.patch('thefuck.argument_parser.Parser.parse') as parse:
                with mock.patch('thefuck.argument_parser.Parser.print_usage') as print_usage:
                    print_usage.return_value = True
                    parse.return_value=mock.Mock()
                    parse.return_value.command= False
                    parse.return_value.shell_logger= False
                    parse.return_value.help = False
                    parse.return_value.version = False
                    parse.return_value.alias = False
                    main()
                    print_usage.assert_called_once()


# Generated at 2022-06-14 08:54:43.301993
# Unit test for function main
def test_main():
    assert main() is None
    # parser = Parser()
    # known_args = parser.parse(['--help'])
    # main(known_args)
    # contain_string_of_main_help(known_args)

# Generated at 2022-06-14 08:54:47.038945
# Unit test for function main
def test_main():
    argv = ['-v']
    with mock.patch.object(sys, 'argv', argv):
        with mock.patch.object(logs, 'version'):
            main()

# Generated at 2022-06-14 08:54:55.475102
# Unit test for function main
def test_main():
    def run(args):
        from .main import main
        from .alias import print_alias
        from .fix_command import fix_command
        from .shell_logger import shell_logger

        args = args.split()
        parser = Parser()
        args = parser.parse(args)
        main()

    assert run([]) == 'usage: main [-h] [--version] [--alias ALIAS] [--replace-command] [--no-wait] [--debug] command'

# Generated at 2022-06-14 08:55:08.726356
# Unit test for function main
def test_main():
    from .helpers import MockLogger, mock_load_config, mock_parse_call, mock_print_help, mock_print_usage, mock_print_version  # noqa: E501,F401

    with mock_load_config(), mock_parse_call() as (known_args, parser):
        main()
        known_args.help = True
        main()
        known_args.version = True
        main()
        known_args.alias = True
        main()
        known_args.command = True
        main()
        os.environ['TF_HISTORY'] = True
        main()
        known_args.shell_logger = True

        with MockLogger() as mock_logs:
            main()
            assert mock_logs.warn.called

    assert mock_print_help.called

# Generated at 2022-06-14 08:55:09.420754
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-14 08:55:22.249461
# Unit test for function main
def test_main():
    from .test_configuration import Configuration, get_logger
    from .shells import Shell
    from ..utils import get_installation_info
    from ..system import Runner
    from ..argument_parser import Parser
    os.environ['TF_HISTORY'] = 'echo $TF_HISTORY'
    runner = Runner(get_logger('test'), Shell(), Configuration(),
                    lambda _: sys.exit(-1))
    parser = Parser(runner, Configuration)
    known_args = parser.parse(sys.argv)
    known_args.__dict__['alias'] = True
    print_alias(known_args)
    known_args.__dict__['alias'] = False
    known_args.__dict__['command'] = "echo $TF_HISTORY"
    known_args.__dict__['pattern'] = None

# Generated at 2022-06-14 08:55:25.681920
# Unit test for function main
def test_main():
    assert 1 == 1

# Generated at 2022-06-14 08:55:26.550433
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:55:43.843720
# Unit test for function main
def test_main():
    import unittest

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:55:45.281369
# Unit test for function main
def test_main():
    try:
        main()
        assert True
    except:
        assert False

# Generated at 2022-06-14 08:55:46.736674
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:55:47.579965
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-14 08:55:48.224237
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:55:49.148806
# Unit test for function main
def test_main():
    # Call main function
    main()

# Generated at 2022-06-14 08:55:51.305511
# Unit test for function main
def test_main():
    sys.argv = ['thefuck']
    assert main() == None


# Generated at 2022-06-14 08:55:52.126867
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:55:57.437871
# Unit test for function main
def test_main():
    args = ['arg1', 'arg2']
    sys.argv = ['thefuck'] + args
    main()
    print('Congratulations on the unit test')

# Generated at 2022-06-14 08:55:58.342198
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:56:30.308187
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:56:42.346314
# Unit test for function main
def test_main():
    import os
    import pytest
    from .alias import print_alias # noqa: E402

    from click.testing import CliRunner
    from .fix_command import fix_command # noqa: E402

    from .shell_logger import shell_logger # noqa: E402

    from .argument_parser import Parser
    from .utils import get_installation_info
    from .system import init_output

    from ..utils import get_installation_info

    tf= sys.modules['tf']
    eq= pytest.approx
    os.environ.pop('TF_HISTORY', None)

    # Test to check if help is displayed
    parser = Parser()
    try:
        parser.parse(['--help'])
    except SystemExit:
        pass

# Generated at 2022-06-14 08:56:43.105257
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:56:43.894841
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:56:52.320350
# Unit test for function main
def test_main():
    from .help import test_main as help_test
    from .version import test_main as version_test
    from .alias import test_main as alias_test
    from .fix_command import test_main as fix_command_test
    from .shell_logger import test_main as shell_logger_test
    help_test()
    version_test()
    alias_test()
    fix_command_test()
    shell_logger_test()


# Generated at 2022-06-14 08:56:53.485422
# Unit test for function main
def test_main():
    assert main() == 0

# Generated at 2022-06-14 08:56:55.316919
# Unit test for function main
def test_main():
    from .test.test_main import test_main
    test_main()

# Generated at 2022-06-14 08:56:57.012230
# Unit test for function main
def test_main():
    # Nothing to test here.
    assert main()

# Generated at 2022-06-14 08:56:58.128913
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 08:56:58.818294
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:58:14.743947
# Unit test for function main
def test_main():
    assert fix_command.__name__ == 'fix_command'
    assert print_alias.__name__ == 'print_alias'
    assert logs.version.__name__ == 'version'
    assert get_installation_info.__name__ == 'get_installation_info'
    assert shell.info.__name__ == 'info'
    assert Parser.__name__ == 'Parser'
    assert Parser.parse.__name__ == 'parse'
    assert Parser.print_usage.__name__ == 'print_usage'
    assert Parser.print_help.__name__ == 'print_help'
    assert Parser.parse_known_args.__name__ == 'parse_known_args'
    assert os.environ.__name__ == 'environ'

# Generated at 2022-06-14 08:58:15.426418
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 08:58:16.159825
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:58:17.116996
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 08:58:19.944503
# Unit test for function main
def test_main():
    assert fix_command
    assert print_alias
    assert get_installation_info
    assert Parser
    assert init_output

# Generated at 2022-06-14 08:58:21.212832
# Unit test for function main
def test_main():
    assert main() is None


# Generated at 2022-06-14 08:58:25.239588
# Unit test for function main
def test_main():
    ll = [
        'python3',
        'main.py',
        'cd',
        '/usr'
    ]
    main(ll)


if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:58:30.732864
# Unit test for function main
def test_main():
    main()
    main(['-v'])
    main(['-h'])
    main(['--help'])
    main(['--version'])
    main(['--alias'])

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 08:58:41.018074
# Unit test for function main
def test_main():
    args_list = ['-h', '-v', '-a', 'fuck', '--no-color',
                 '-l', '-n2', '-t 1']
    result = []
    with patch('sys.argv', args_list):
        with patch('thefuck.__main__.Parser.parse') as mock_parse:
            mock_parse.return_value = None
            with patch('thefuck.__main__.Parser.print_help') as mock_help:
                with patch('thefuck.__main__.logs.version') as mock_version:
                    with patch('thefuck.__main__.print_alias') as mock_alias:
                        with patch('thefuck.__main__.fix_command') as mock_fix:
                            mock_help.return_value = None

# Generated at 2022-06-14 08:58:42.987133
# Unit test for function main
def test_main():
    main()
    assert True

if __name__ == '__main__':
    main()

# Generated at 2022-06-14 09:00:59.490510
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-14 09:01:01.765294
# Unit test for function main
def test_main():
    assert main() == None
#
if __name__ == '__main__':
    main()

# Generated at 2022-06-14 09:01:15.258522
# Unit test for function main
def test_main():
    from .shell_logger import shell_logger  # noqa: E402
    from .alias import print_alias  # noqa: E402
    from .fix_command import fix_command  # noqa: E402
    parser = Parser()
    known_args = parser.parse(sys.argv)
    assert main() == parser.print_usage()
    assert main() == parser.print_help()
    import subprocess  # noqa: E402
    subprocess.call([sys.executable, "python3 test_main.py", "shell_logger", "--debug"])
    subprocess.call([sys.executable, "python3 test_main.py",  "fix_command", "--debug"])

# Generated at 2022-06-14 09:01:15.972981
# Unit test for function main
def test_main():
    assert main()==0

# Generated at 2022-06-14 09:01:28.350992
# Unit test for function main
def test_main():
    def side_effect(argv):
        class KnownArgs:
            def __init__(self):
                self.help = True

        return KnownArgs()

    parser_parse_mock = Mock(side_effect=side_effect)
    parser_print_usage_mock = Mock()
    parser_print_help_mock = Mock()
    parser_mock = Mock()

    type(parser_mock).parse = parser_parse_mock
    type(parser_mock).print_help = parser_print_help_mock
    type(parser_mock).print_usage = parser_print_usage_mock

    parser_class_mock = Mock(return_value=parser_mock)

    with patch('thefuck.main.Parser', parser_class_mock):
        main()

    parser_class_

# Generated at 2022-06-14 09:01:29.076726
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-14 09:01:34.965128
# Unit test for function main
def test_main():
    parser = Parser()
    known_args = parser.parse(['-v'])

    if known_args.version:
        logs.version(get_installation_info().version,
                     sys.version.split()[0], shell.info())


if __name__ == '__main__':
    main()

# Generated at 2022-06-14 09:01:37.324908
# Unit test for function main
def test_main():
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-14 09:01:38.064176
# Unit test for function main
def test_main():
    assert main() == None

# Generated at 2022-06-14 09:01:38.721630
# Unit test for function main
def test_main():
    assert main()