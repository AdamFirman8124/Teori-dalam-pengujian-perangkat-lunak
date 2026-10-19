

# Generated at 2022-06-13 20:53:54.970839
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # This function must be tested via "test_flutils".
    pass  # pragma: no cover

# Generated at 2022-06-13 20:54:00.552655
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import make_dirs_in_path
    from flutils.funcutils import make_singleton
    from os.path import dirname
    import tempfile
    tmp_dir = dirname(tempfile.mkdtemp())

    @make_singleton
    def reset_config_files():
        make_dirs_in_path(tmp_dir)

        setup_commands_cfg = os.environ.get('SETUP_COMMANDS_CONFIG')
        if setup_commands_cfg is not None:
            return

        setup_cfg = os.path.join(tmp_dir, 'setup.cfg')
        with open(setup_cfg, 'w') as fp:
            fp.write(
                '[metadata]\n'
                'name = flutils\n'
            )

       

# Generated at 2022-06-13 20:54:07.363627
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config"""
    from pathlib import Path
    from unittest.mock import Mock
    from unittest.mock import patch

    mock_parser = Mock()
    mock_parser.sections.return_value = [
        'metadata',
        'setup.command.build',
        'setup.command.test',
        'setup.command.rulez',
    ]

# Generated at 2022-06-13 20:54:16.131279
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    from flutils.scriptutils import each_sub_command_config

    path = os.path.join(
        os.environ.get('FLUTILS_TEST_DATA', '.'),
        'sub_commands'
    )
    path = os.path.abspath(path)

    for cfg in each_sub_command_config(path):
        assert cfg.name
        assert cfg.camel
        assert cfg.description
        assert cfg.commands

# Generated at 2022-06-13 20:54:30.203227
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from inspect import cleandoc
    from pathlib import Path
    from textwrap import dedent
    from tempfile import mkdtemp
    from unittest import TestCase
    from unittest.mock import patch, Mock
    from flutils.systemutils import ModuleNotFoundError

    class TestEachSubCommandConfig(TestCase):
        def setUp(self):
            self.setup_dir = mkdtemp()
            self.addon_file = Path(self.setup_dir, 'setup_commands.cfg')
            self.addCleanup(self.addon_file.unlink)
            self.setup_cfg_path = Path(self.setup_dir, 'setup.cfg')
            self.addCleanup(self.setup_cfg_path.unlink)

        def test_not_found(self):
            fs = extract_stack

# Generated at 2022-06-13 20:54:34.548718
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    print('Testing each_sub_command_config()...')
    for config in each_sub_command_config():
        print(config)

# Use python -m flutils.setupcfg to run unit test
if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:54:36.368424
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config():
        print(config)

# Generated at 2022-06-13 20:54:38.901686
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for command in each_sub_command_config('.'):
        print(command)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:54:52.141373
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from collections import Counter
    from os import chdir, getcwd, path

    def _test():
        output_path = path.join('tests', 'fixtures', 'config', 'output')
        setup_cfg_path = path.join('tests', 'fixtures', 'config')
        setup_cfg_path = path.join(setup_cfg_path, 'setup.cfg')
        setup_dir = path.dirname(setup_cfg_path)
        if not path.isdir(setup_dir):
            os.makedirs(setup_dir)
        if not path.isfile(setup_cfg_path):
            open(setup_cfg_path, 'w').close()
        config_path = path.join(output_path, 'setup_commands.cfg')
        if path.isfile(config_path):
            os

# Generated at 2022-06-13 20:54:59.251982
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for cfg in each_sub_command_config():
        if cfg.camel == 'Make':
            assert cfg.name == 'make'
            assert cfg.description == ''
            assert cfg.commands == ('build', )
        elif cfg.camel == 'MakeClean':
            assert cfg.name == 'make clean'
            assert cfg.description == ''
            assert cfg.commands == ('clean', )
        elif cfg.camel == 'MakeLint':
            assert cfg.name == 'make lint'
            assert cfg.description == ''
            assert cfg.commands == ('lint', )
        elif cfg.camel == 'MakeFix':
            assert cfg.name == 'make fix'
            assert cfg.description == ''
            assert cfg.comm

# Generated at 2022-06-13 20:55:23.054586
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    setup_dir = os.path.join(base_dir, 'examples', 'setup_dir')
    setup_dir = os.path.normpath(setup_dir)
    expected = [
        ("test.command", "TestCommand", "Test desc...",
         ("echo 'test_command'",)),
        ("test.command.other", "TestCommandOther", "Test desc...",
         ("echo 'test_command_other'",))
    ]
    for i, sub_command in enumerate(each_sub_command_config(setup_dir)):
        assert isinstance(sub_command.name, str)
        assert isinstance(sub_command.camel, str)

# Generated at 2022-06-13 20:55:30.790433
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from .util_test import make_and_remove_dir
    from .util_test import write_file

    from os import mkdir

    from shutil import copy

    with make_and_remove_dir() as setup_dir:
        setup_dir = cast(str, setup_dir)
        mkdir(os.path.join(setup_dir, 'src'))
        src_path = os.path.join(setup_dir, 'src', '__init__.py')
        write_file(src_path, '#')

        setup_py_path = os.path.join(setup_dir, 'setup.py')
        write_file(setup_py_path, '#')

        setup_cfg_path = os.path.join(setup_dir, 'setup.cfg')

# Generated at 2022-06-13 20:55:42.588485
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import get_path_to_env_file
    from flutils.testutils import capture_stdout, capture_stderr
    from flutils.testutils.files import FileBuilder
    from flutils.testutils.testcase import BaseTestCaseWithTempDir

    class BaseTestCase(BaseTestCaseWithTempDir):
        pass

    class TestEachSubCommandConfig(BaseTestCase):
        def setUp(self) -> None:
            super().setUp()
            self.addCleanup(self.assert_all_files_closed)

        def test_file_not_found_error(self):
            with self.assertRaises(FileNotFoundError):
                each_sub_command_config(self.temp_dir)


# Generated at 2022-06-13 20:55:50.813602
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import textwrap
    import shutil
    import unittest

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.test_dir = tempfile.TemporaryDirectory()
            self.setup_py = os.path.join(self.test_dir.name, 'setup.py')
            with open(self.setup_py, 'w') as fp:
                fp.write('')
            self.setup_cfg = os.path.join(self.test_dir.name, 'setup.cfg')

# Generated at 2022-06-13 20:56:02.465368
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    test_dir = os.path.dirname(__file__)
    path = os.path.join(test_dir, 'test_setup_commands.cfg')
    assert os.path.isfile(path) is True
    commands: List[SetupCfgCommandConfig] = list(
        each_sub_command_config(test_dir)
    )
    assert isinstance(commands, list)

    for command in commands:
        assert isinstance(command, SetupCfgCommandConfig)
        assert isinstance(command.name, str)
        cmd_name = command.name
        cmd_name = cmd_name.replace('.', '_')
        cmd_name = cmd_name.replace('-', '_')
        assert cmd_name.isidentifier() is True

# Generated at 2022-06-13 20:56:13.803397
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    import sys
    import flutils

    # Test running the function when we are not in the project's directory
    test_dir = os.path.dirname(__file__)
    setup_dir = os.path.dirname(flutils.__file__)
    os.chdir(test_dir)
    try:
        assert each_sub_command_config(setup_dir)
    except FileNotFoundError:
        assert False, "The FileNotFoundError exception was not expected."
    except AssertionError as err:
        assert False, "'%s'" % err

    try:
        assert each_sub_command_config()
    except FileNotFoundError:
        assert False, "The FileNotFoundError exception was not expected."

# Generated at 2022-06-13 20:56:25.604172
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import flask
    import requests
    import requests_toolbelt
    import requests_toolbelt.toolbelt
    import requests_toolbelt.toolbelt.cli
    import requests_toolbelt.toolbelt.toolbelt
    from . import setup_commands

    def get_parent_paths(path: Union[str, os.PathLike]) -> Generator[str, None, None]:
        path = str(path)
        for x in range(len(path.split('/')) - 2):
            path = path.rsplit('/', 1)[0]
            if path:
                yield path

    for path in get_parent_paths(__file__):
        if path in sys.path:
            sys.path.remove(path)
    sys.path.insert(0, '')


# Generated at 2022-06-13 20:56:36.640862
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from .testing import (
        unit_test_setup_cfg,
        unit_test_setup_commands_cfg,
        unit_test_setup_py,
    )
    import tempfile
    with tempfile.TemporaryDirectory() as test_dir:
        with open(
                os.path.join(test_dir, 'setup.py'), mode='w',
                encoding='utf-8'
        ) as out_fh:
            out_fh.write(unit_test_setup_py)
        with open(
                os.path.join(test_dir, 'setup.cfg'), mode='w',
                encoding='utf-8'
        ) as out_fh:
            out_fh.write(unit_test_setup_cfg)

# Generated at 2022-06-13 20:56:49.765855
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import THIS_DIR
    from types import SimpleNamespace

    class Config(SimpleNamespace):
        camel: str
        name: str
        description: str
        commands: Tuple[str, ...]

    here = os.path.dirname(THIS_DIR)
    expected: Dict[str, Config] = {}
    for config in each_sub_command_config(here):
        config = config._asdict()
        expected[config['name']] = Config(
            camel=config['camel'],
            name=config['name'],
            description=config['description'],
            commands=config['commands'],
        )

    assert expected['test'].camel == 'Test'
    assert expected['test'].name == 'test'

# Generated at 2022-06-13 20:57:01.803860
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Test the flutils.setup.each_sub_command_config function."""
    import argparse
    import pathlib

    def _args_get_setup_dir(args: argparse.Namespace) -> str:
        if args.setup_dir:
            if args.setup_dir.is_absolute():
                return str(args.setup_dir.resolve())
            else:
                return str(args.setup_dir.resolve().absolute())

        return str(pathlib.Path(
            __file__).parent.parent.joinpath('setup.py').resolve())

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--setup_dir',
        help="The path to the project's setup.py directory.",
        type=pathlib.Path
    )
    args = parser.parse_

# Generated at 2022-06-13 20:57:34.112864
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    out = list(each_sub_command_config(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), 'test_data'
        )
    ))
    assert len(out) is 3
    # check `test` section from setup_commands.cfg
    assert out[0].name == 'test'
    assert out[0].camel == 'Test'
    assert out[0].description == 'Run the unit tests.'
    assert out[0].commands == (
        'coverage run -m unittest',
        'coverage report',
    )
    # check `coverage` section from setup.cfg
    assert out[1].name == 'coverage'
    assert out[1].camel == 'Coverage'

# Generated at 2022-06-13 20:57:46.535536
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.dirname(__file__)
    configs = list(each_sub_command_config(setup_dir))
    assert len(configs) == 1
    assert configs[0].name == 'hello'
    assert configs[0].camel == 'Hello'
    assert configs[0].description == 'Hello World!'
    assert configs[0].commands[0] == 'echo "Hello World!"'


if __name__ == '__main__':
    from sys import stderr
    from traceback import print_exc


# Generated at 2022-06-13 20:57:58.974289
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.testutils import TestOutput
    from os import path

    test_output = TestOutput()
    setup_dir = path.dirname(path.dirname(path.abspath(__file__)))

    for config in each_sub_command_config(setup_dir):
        test_output.print(config)
    test_output.print()

    for config in each_sub_command_config():
        test_output.print(config)
    test_output.print()

    test_output.format_output({
        'python_version': '%s.%s.%s' % sys.version_info[:3],
        'sys_platform': sys.platform,
    })


if __name__ == '__main__':
    from flutils.testutils import run_doctest

    run_do

# Generated at 2022-06-13 20:58:04.911960
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config():
        assert len(config.commands) > 0
        assert isinstance(config.camel, str)
        assert isinstance(config.commands, tuple)
        assert isinstance(config.description, str)
        assert isinstance(config.name, str)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:58:09.971455
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    cwd = os.getcwd()
    os.chdir(os.path.dirname(__file__))
    os.chdir('..')
    cnt = 0
    for _ in each_sub_command_config():
        cnt += 1
    assert cnt == 2
    os.chdir(cwd)

# Generated at 2022-06-13 20:58:20.060327
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from os import (
        sep,
        pathsep,
    )
    from tempfile import TemporaryDirectory
    from contextlib import (
        contextmanager,
    )
    from subprocess import (
        PIPE,
        Popen,
        CalledProcessError,
    )
    from shutil import (
        which,
    )

    @contextmanager
    def cd(d):
        if not d:
            yield
            return
        curdir = os.getcwd()
        os.chdir(d)
        try:
            yield
        finally:
            os.chdir(curdir)

    def _detect_install_type(setup_dir) -> str:
        with cd(setup_dir):
            cmd = ['pip', 'install', '-U', '.']
            p = Popen

# Generated at 2022-06-13 20:58:28.445312
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for sc in each_sub_command_config('test'):
        assert type(sc) == SetupCfgCommandConfig
    for sc in each_sub_command_config('test/test_setup_cfg_commands'):
        assert type(sc) == SetupCfgCommandConfig
        assert sc.name != ''
        assert sc.camel != ''
        assert sc.description != ''
        assert len(sc.commands) > 0
        for x in sc.commands:
            assert x != ''

# Generated at 2022-06-13 20:58:39.955424
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config"""
    import flutils.envutils
    import cleo.application
    from .. import __version__

    def _out(
            msg: str,
            color: cleo.application.OutputFormatterStyle = None
    ) -> None:
        if color is not None:
            color = color.apply
        else:
            color = lambda x: x
        if msg:
            msg = msg.strip()
        if msg:
            msg = msg.replace('\r\n', ' ')
            msg = msg.replace('\n', ' ')
            if msg.endswith('.'):
                msg = msg[:-1]
            msg = color(msg)
            print(msg)


# Generated at 2022-06-13 20:58:50.075393
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Tests :func:`flutils.setuputils.each_sub_command_config`."""
    from . import osutils
    from .testutils import unittest_reporter
    from .typingutils import TYPE_CHECKING

    if TYPE_CHECKING:
        from flutils.setuputils import test_each_sub_command_config as dut

    caller = osutils.get_caller_module(0)

    with unittest_reporter(caller=caller):
        import os
        import shutil
        from .strutils import to_str

        # Test 1: normal case.
        this_dir = os.path.dirname(os.path.realpath(__file__))

# Generated at 2022-06-13 20:59:00.848509
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import pprint
    import sys
    cur_dir = os.path.dirname(__file__)
    setup_dir = os.path.realpath(os.path.join(cur_dir, '..', '..'))
    for cmd in each_sub_command_config(setup_dir):
        pprint.pprint(cmd)
        sys.stdout.flush()


if __name__ == '__main__':
    import sys
    print(sys.path)
    test_each_sub_command_config()

# Generated at 2022-06-13 20:59:53.413585
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile

    with tempfile.TemporaryDirectory() as temp_dir:
        path = os.path.join(temp_dir, 'setup_commands.cfg')
        with open(path, 'wt') as fh:
            fh.write(
                '''[setup.command.test]\nname = test\ncommand = foo {home}'''
            )
        for x in each_sub_command_config(temp_dir):
            assert x.name == 'test'
            assert x.commands == ('foo %s' % os.path.expanduser('~'),)

# Generated at 2022-06-13 21:00:03.797185
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Tests the ``each_sub_command_config`` function."""
    import flutils.sysutils
    import sh

    this = flutils.sysutils.this_file(__file__)
    root_dir = os.path.dirname(this)
    setup_py_path = os.path.join(root_dir, 'setup.py')
    setup_cfg_path = os.path.join(root_dir, 'setup.cfg')
    setup_commands_cfg_path = os.path.join(root_dir, 'setup_commands.cfg')

    sh.rm('-f', setup_py_path)
    sh.rm('-f', setup_cfg_path)
    sh.rm('-f', setup_commands_cfg_path)


# Generated at 2022-06-13 21:00:16.133263
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from pprint import pprint
    from tempfile import mkdtemp

    from flutils.pathutils import (
        ensure_parent_exists,
        mk_temp_py_file,
    )

    def _write_setup(
            setup_dir: str
    ) -> str:
        path = os.path.join(setup_dir, 'setup.py')
        with open(path, 'wt') as f:
            f.write('pass\n')
        return path

    def _write_setup_cfg(
            setup_dir: str,
            commands: List[Dict[str, str]]
    ) -> str:
        path = os.path.join(setup_dir, 'setup.cfg')

# Generated at 2022-06-13 21:00:20.068515
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # from flutils.configutils import each_sub_command_config
    for command in each_sub_command_config(setup_dir='.'):
        print(command)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:00:31.377857
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit-test the function each_sub_command_config"""
    # pylint: disable=protected-access
    import unittest.mock

    mck_get_name = unittest.mock.MagicMock()
    mck_get_name.return_value = 'test-name'

    mck_each_setup_cfg_command = unittest.mock.MagicMock()
    mck_each_setup_cfg_command.return_value = iter([
        SetupCfgCommandConfig(
            'test_command_name', 'TestCommand', 'Test command description', ()
        )
    ])


# Generated at 2022-06-13 21:00:33.702268
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config():
        print(config)

# Generated at 2022-06-13 21:00:44.581620
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import recur_chdir

    def assert_sub_command(
            sub_command: SetupCfgCommandConfig
    ) -> None:
        assert isinstance(sub_command.name, str)
        assert isinstance(sub_command.camel, str)
        assert isinstance(sub_command.description, str)
        assert isinstance(sub_command.commands, tuple)
        assert all(
            isinstance(cmd, str)
            for cmd in sub_command.commands
        )

    def assert_sub_command_list(
            sub_commands: List[SetupCfgCommandConfig]
    ) -> None:
        assert isinstance(sub_commands, list)

# Generated at 2022-06-13 21:00:53.145154
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from pathlib import Path
    import sys

    setup_dir = None
    for fs in extract_stack():
        fs = cast(FrameSummary, fs)
        basename = os.path.basename(fs.filename)
        if basename == 'setup.py':
            setup_dir = str(os.path.dirname(fs.filename))
            break
    if setup_dir:
        setup_dir = Path(setup_dir)
        setup_commands_cfg = setup_dir / 'setup_commands.cfg'
        setup_cfg = setup_dir / 'setup.cfg'
        found = False
        for fs in extract_stack():
            fs = cast(FrameSummary, fs)
            basename = os.path.basename(fs.filename)
            if basename == 'setup.py':
                found = True


# Generated at 2022-06-13 21:01:01.576558
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    config = list(each_sub_command_config())

    for i in config:
        if 'highlight' in i.description:
            assert(i.commands ==
                   ('python -m flutils --highlight',)
                   )
        elif 'help' in i.description:
            assert(i.commands == ('python -m flutils --help',))
        elif 'run' in i.description:
            assert(i.commands == ('python run.py',))

if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:01:12.203559
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from pathlib import Path
    from tempfile import TemporaryDirectory

    # Assume this file is in the tests directory of the project
    path = Path(__file__)
    while path and path.name != 'tests':
        path = cast(Path, path.parent)
    path = path.absolute()

    with TemporaryDirectory() as tmpdir:
        tmpdir = cast(str, tmpdir)
        filepath = Path(tmpdir, 'setup.cfg')
        filepath.write_text(
            """
            [metadata]
            name = flutils_test
            
            [setup.command.sub-command]
            name = sub-command
            description = Run the sub command.
            commands = 
                echo "sub-command"
            """,
            encoding='utf8',
            errors='ignore'
        )

# Generated at 2022-06-13 21:01:50.327267
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config"""
    for scc in each_sub_command_config('/tmp'):
        print(scc)


if __name__ == "__main__":
    # Unit test for function each_sub_command_config
    test_each_sub_command_config()

# Generated at 2022-06-13 21:01:59.011274
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil

    def verify_commands(
            commands: List[SetupCfgCommandConfig],
            expected_commands: List[SetupCfgCommandConfig]
    ) -> None:
        assert len(commands) == len(expected_commands)
        for i, cmd in enumerate(commands):
            assert cmd.name == expected_commands[i].name
            assert cmd.camel == expected_commands[i].camel
            assert cmd.description == expected_commands[i].description
            assert cmd.commands == expected_commands[i].commands

    tmpdir = tempfile.mkdtemp()

# Generated at 2022-06-13 21:02:11.992568
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def test_func(
            setup_dir: Optional[Union[os.PathLike, str]] = None
    ) -> Generator[SetupCfgCommandConfig, None, None]:
        return each_sub_command_config(setup_dir)

    setup_dir = os.path.dirname(__file__)
    out = list(test_func(setup_dir))
    assert len(out) == 1
    assert out[0].name == 'flutils.setup_command.__main__'
    assert out[0].camel == 'FlutilsSetupCommandMain'
    assert out[0].description.startswith('$ setup.py') is True
    assert len(out[0].commands) == 1
    assert out[0].commands[0].startswith('setup.py') is True

# Generated at 2022-06-13 21:02:14.642749
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config(os.path.dirname(__file__)):
        print(config)

# Generated at 2022-06-13 21:02:26.224893
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import tempfile


# Generated at 2022-06-13 21:02:38.309641
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config."""
    #
    # Basic test
    #
    with tempfile.TemporaryDirectory() as tempdir:
        setup_dir = os.path.join(tempdir, 'setup')
        os.makedirs(setup_dir)
        setup_py_path = os.path.join(setup_dir, 'setup.py')
        with open(setup_py_path, 'w') as f:
            f.write('# setup.py')
        setup_cfg_path = os.path.join(setup_dir, 'setup.cfg')
        with open(setup_cfg_path, 'w') as f:
            f.write('[metadata]\nname = abc')

# Generated at 2022-06-13 21:02:39.757692
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    pass



# Generated at 2022-06-13 21:02:44.843393
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for scc in each_sub_command_config(setup_dir='./test/pkg'):
        print(scc)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:02:53.876655
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.testutils import TempDirTestCase
    import os.path

    class TestSubCommand(TempDirTestCase):
        def setUp(self):
            super().setUp()
            with open(os.path.join(self.tempdir, 'setup.cfg'), 'w') as fh:
                fh.write(
                    "[metadata]\n"
                    "name = flutils\n"
                    "[setup.command.test]\n"
                    "test = {name}\n"
                    "test2 = #\n"
                    "test3 = \n"
                    "test4 =  \n"
                    "test5 = a\n"
                    "test6 = a   \n"
                )

        def test_basic(self):
            from contextlib import redirect_stdout
            from io import StringIO

# Generated at 2022-06-13 21:03:07.120378
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    d = os.path.dirname(__file__)
    path = os.path.join(d, 'data')
    config = list(each_sub_command_config(path))
    assert len(config) > 0
    for config in each_sub_command_config(path):
        assert config.camel.istitle()
        assert config.camel.isidentifier()
        assert config.description.strip()
        assert config.name.istitle()
        assert config.name.isidentifier()
        for cmd in config.commands:
            cmd = cmd.strip()
            assert cmd

if __name__ == '__main__':
    import sys
    import logging
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)