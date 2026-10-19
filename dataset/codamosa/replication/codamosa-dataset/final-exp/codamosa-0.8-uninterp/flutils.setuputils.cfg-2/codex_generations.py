

# Generated at 2022-06-13 20:53:59.031601
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for cfg in each_sub_command_config('tests/template'):
        assert cfg.name == 'build_project'
        assert cfg.camel == 'BuildProject'
        assert cfg.description == ''
        assert cfg.commands == ('echo hi', 'echo bye')
        break
    else:
        assert False



# Generated at 2022-06-13 20:54:06.987194
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    current_dir = os.path.dirname(__file__)
    sub_command_config = list(
        each_sub_command_config(os.path.join(current_dir, 'data'))
    )
    assert sub_command_config[0] == \
        SetupCfgCommandConfig(
            'subcmd',
            'Subcmd',
            '',
            (
                'echo "This is a sub command."',
                'echo "This is another sub command."',
            )
        )

# Generated at 2022-06-13 20:54:21.353942
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    from io import StringIO

    def _prep_setup_cfg(*setup_cfg_texts: str) -> str:
        out = StringIO()
        for text in setup_cfg_texts:
            out.write(text)
        out.seek(0)
        return out.read()


# Generated at 2022-06-13 20:54:32.588692
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import TemporaryDirectory
    from tests import HERE

    with TemporaryDirectory(str(HERE)) as tmp_dir:
        setup_cfg = tmp_dir.join('setup.cfg')

# Generated at 2022-06-13 20:54:43.747816
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from tempfile import TemporaryDirectory
    from flutils.testutils import count_iter

    with TemporaryDirectory() as tmpdir:

        with open(os.path.join(tmpdir, 'setup.py'), 'w') as f:
            f.write('pass')

        with open(os.path.join(tmpdir, 'setup.cfg'), 'w') as f:
            f.write('''
[metadata]
name = mypkg
''')

        with open(os.path.join(tmpdir, 'setup_commands.cfg'), 'w') as f:
            f.write('''
[setup.command.setup_commands.cfg]
description = A test command.
commands = echo {name} >> {setup_dir}/__init__.py
''')


# Generated at 2022-06-13 20:54:54.818228
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    import tempfile
    this_filepath = os.path.realpath(__file__)
    this_dirpath = os.path.dirname(this_filepath)
    setup_dir = os.path.join(this_dirpath, 'setup_commands_test')

    this_module_path = os.path.realpath(__file__)
    this_module_dir = os.path.dirname(this_module_path)
    with tempfile.TemporaryDirectory() as tempdir:
        expected_setup_dir = os.path.join(tempdir, 'setup_commands_test')
        os.makedirs(expected_setup_dir)
        # setup_cfg

# Generated at 2022-06-13 20:55:02.202631
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Tests the function each_sub_command_config using the current directory
    that contains this test file.
    """
    def _test_sub_command(config: SetupCfgCommandConfig) -> None:
        assert config.name
        assert config.description
        assert config.camel
        assert config.commands
        print(config)

    for sub_command in each_sub_command_config(__file__):
        _test_sub_command(sub_command)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:55:14.012279
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def get_actual(setup_dir: str) -> Tuple[str, ...]:
        out = []
        for cfg in each_sub_command_config(setup_dir):
            out.append(cfg.name)
        return tuple(out)

    def assert_actual_expected(actual: Tuple[str, ...], expected: Tuple[str, ...]) -> None:
        assert len(actual) == len(expected), "The number of entries is different."
        for actual_entry, expected_entry in zip(sorted(actual), sorted(expected)):
            assert actual_entry == expected_entry

    # Test 1: no setup_dir
    # Test 1.1: setup_dir is None
    setup_dir: Optional[str] = None

# Generated at 2022-06-13 20:55:21.043883
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def _test(
            setup_dir: Union[os.PathLike, str],
            out: Optional[List[SetupCfgCommandConfig]] = None
    ) -> None:
        out = out if out else []
        assert list(each_sub_command_config(setup_dir)) == out

    _test(None)
    _test('/fake/path')
    _test(os.path.dirname(__file__))

# Generated at 2022-06-13 20:55:29.651352
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for ``each_sub_command_config``."""
    import unittest.mock as mock
    from importlib import invalidate_caches

    setup_dir = os.path.dirname(__file__)

    def check_path(path: str, value: str) -> None:
        assert os.path.exists(path) is True
        assert os.path.isfile(path) is True
        assert os.path.basename(path) == value

    # Default directory
    invalidate_caches()
    with mock.patch.object(__builtins__, 'open',
                           side_effect=RuntimeError, create=True):
        with pytest.raises(FileNotFoundError):
            list(each_sub_command_config())

# Generated at 2022-06-13 20:55:49.171867
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os

    from tempfile import TemporaryDirectory

    from shutil import copyfile

    from flutils.testutils import assert_each_equal

    from .testutils import EXAMPLE_CONFIG

    with TemporaryDirectory() as tmp_dir:
        setup_py_path = os.path.join(tmp_dir, 'setup.py')
        with open(setup_py_path, 'w') as infile:
            infile.write('# Auto-generated file.\n')

        setup_cfg_path = os.path.join(tmp_dir, 'setup.cfg')

        example_setup_commands_path = os.path.join(
            os.path.dirname(__file__),
            'example_setup_commands.cfg'
        )

# Generated at 2022-06-13 20:56:01.848228
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit testing for function each_sub_command_config."""
    import tempfile
    import shutil
    import os

    def _clean_tmpdir(tmpdir: str) -> None:
        if os.path.exists(tmpdir):
            shutil.rmtree(tmpdir)

    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = str(tmpdir)

# Generated at 2022-06-13 20:56:12.541582
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    config = {}
    for x in each_sub_command_config():
        config[x.name] = x
    expected = {
        'cmd1': SetupCfgCommandConfig(
            'cmd1',
            'Cmd1',
            'no description',
            ('echo [version]', 'echo [title]')
        ),
        'cmd2': SetupCfgCommandConfig(
            'cmd2',
            'Cmd2',
            'test',
            ('echo [name]', 'echo [title]')
        )
    }  # type: Dict[str, SetupCfgCommandConfig]
    for k, v in expected.items():
        assert config[k] == v, k

# Generated at 2022-06-13 20:56:16.204867
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for cfg in each_sub_command_config('setup_commands'):
        print(cfg)


if __name__ == '__main__':
    # from pathlib import Path
    import sys
    sys.exit(test_each_sub_command_config())

# Generated at 2022-06-13 20:56:28.319863
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from subprocess import Popen
    from uuid import uuid4
    from tempfile import TemporaryDirectory

    from flutils.env import cwd

    from .test_common import (
        BASE_SETUP_CFG,
        BASE_SETUP_PY,
        SETUP_DIR,
        SETUP_DIR_UNDER_CWD,
        SIMPLE_SETUP_COMMANDS_CFG,
        SIMPLE_SETUP_CFG,
    )

    # Test a bad setup_dir
    with pytest.raises(FileNotFoundError):
        list(each_sub_command_config(setup_dir='/tmp/does_not_exist'))

    # Test a bad setup_dir

# Generated at 2022-06-13 20:56:36.828307
# Unit test for function each_sub_command_config
def test_each_sub_command_config():

    def dump_sub_commands(command_configs):
        print("The following commands were found:")
        for cc in command_configs:
            print("\tCommand: %s" % cc.name)
            print("\t\tCamel Title: %s" % cc.camel)
            print("\t\tDescription: %s" % cc.description)
            for command in cc.commands:
                print("\t\tCommand Line: %s" % command)

    dump_sub_commands(each_sub_command_config())

if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:56:49.837662
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    here: str = os.path.dirname(__file__)
    here = os.path.join(here, 'test_files')
    here = os.path.realpath(here)


# Generated at 2022-06-13 20:57:01.903848
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil
    import sys

    def _make_temp_dir() -> str:
        out = tempfile.mkdtemp(
            prefix='test_each_sub_command_config_'
        )
        return out.replace(os.path.sep, '/')

    def _rm_temp_dir(temp_dir: str) -> None:
        shutil.rmtree(temp_dir, ignore_errors=True)

    temp_dir = _make_temp_dir()
    old_sys_path = sys.path

# Generated at 2022-06-13 20:57:05.148814
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    found = False
    for cfg in each_sub_command_config():
        found = True
        if not isinstance(cfg, SetupCfgCommandConfig):
            assert False

    assert found is True

# Generated at 2022-06-13 20:57:06.957753
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config():
        assert config.camel



# Generated at 2022-06-13 20:57:26.642429
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    import pathlib
    import shutil
    import tempfile

    def test_run(out: str, expected: str) -> None:
        assert out == expected

    def prep_files(src: str, dst: str, file_name: str) -> None:
        with open(os.path.join(src, file_name), 'w') as f:
            f.write(file_name)
        shutil.copy(os.path.join(src, file_name), dst)

    def create_temp_files(
            temp_dir: str,
            setup_cfg: str,
            setup_commands_cfg: str,
            setup_py: str
    ) -> None:
        prep_files(temp_dir, temp_dir, setup_cfg)

# Generated at 2022-06-13 20:57:37.225161
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # Only run as part of unit test
    import sys
    from os import remove
    from pathlib import Path
    from tempfile import TemporaryDirectory
    from unittest import TestCase

    from flutils.testutils.dicttestutils import (
        DictEquals,
        DictTestHelpersMixin,
        DictTestHelpersTestCaseMixin,
    )

    class TestCaseSetupCfgCommandConfig(TestCase, DictTestHelpersTestCaseMixin):
        def setUp(self) -> None:
            self.maxDiff = None

        def test_each_sub_command_config(self) -> None:
            """Tests the function each_sub_command_config in the module
            setup_commands_cfg."""

# Generated at 2022-06-13 20:57:43.257234
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config."""
    from pprint import pprint
    setup_dir = os.path.expanduser('~/python/flutils-x/flutils')
    for config in each_sub_command_config(setup_dir):
        pprint(config)


# Generated at 2022-06-13 20:57:53.558859
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import flutils.fldirs

    setup_dir = flutils.fldirs.get_dir(flutils.fldirs.Dir.DOCROOT)

    # noinspection PyTypeChecker
    commands: List[SetupCfgCommandConfig] = list(
        each_sub_command_config(setup_dir)
    )
    cmd = commands[0]
    assert isinstance(cmd.name, str)
    assert cmd.name == 'doctoken'
    assert isinstance(cmd.camel, str)
    assert cmd.camel == 'DocToken'
    assert isinstance(cmd.commands, (list, tuple))
    assert len(cmd.commands) == 1
    cmd = commands[1]
    assert isinstance(cmd.name, str)
    assert cmd.name == 'outdated'

# Generated at 2022-06-13 20:58:05.670880
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.project_tools import each_sub_command_config
    from string import printable
    from textwrap import dedent
    from pprint import pprint

    data: str = dedent("""
        [metadata]
        name = myproject

        [setup.command.my-command]
        name = my_command # the name of the command
        description = My command # the description of the command
        command = echo 'My command.' # the command to run
        command = echo 'My command again...' # another command to run
        commands =
            echo 'My command.'
            echo 'My command again...'

        [setup.command.another-command]
        name = another_command # the name of the command
        description = Another command # the description of the command
        commands =
            echo 'Another command.'
    """)
   

# Generated at 2022-06-13 20:58:16.320907
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with mock.patch('flutils.setuputils.os.path.expanduser') as mpathexp:
        mocked_home = '\\user\\home'
        mpathexp.return_value = mocked_home
        dir_name = __file__
        dir_name = os.path.dirname(dir_name)
        dir_name = os.path.dirname(dir_name)
        dir_name = os.path.dirname(dir_name)
        dir_name = os.path.dirname(dir_name)
        dir_name = os.path.dirname(dir_name)
        dir_name = os.path.join(dir_name, 'tests')
        dir_name = os.path.join(dir_name, 'setup_commands')

# Generated at 2022-06-13 20:58:28.350786
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import logging
    import sys

    from flutils.logutils.config import add_logging_config

    add_logging_config(
        default_level=logging.DEBUG,
        default_handler_level=logging.DEBUG,
        debug_fmt='%(levelname)7s: %(filename)s:%(lineno)d: %(message)s',
        info_fmt='%(levelname)7s: %(message)s'
    )

    # logger = logging.getLogger('test_each_sub_command_config')

    if __name__ == '__main__':
        print(sys.argv[0])
        setup_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    else:
        setup_dir = os

# Generated at 2022-06-13 20:58:34.968750
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config."""
    class SetupCfgCommandConfigConfig(NamedTuple):
        name: str
        camel: str
        description: str
        commands: Tuple[str, ...]
        setup_dir: str

    configs: List[SetupCfgCommandConfigConfig] = list()
    for cfg in each_sub_command_config('.'):
        configs.append(cfg)

    assert isinstance(configs, list)
    assert len(configs) > 0
    for config in configs:
        assert isinstance(config, SetupCfgCommandConfigConfig)
        assert isinstance(config.name, str)
        assert isinstance(config.camel, str)
        assert isinstance(config.description, str)
        assert isinstance(config.commands, tuple)

# Generated at 2022-06-13 20:58:39.539514
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.join(os.path.dirname(__file__), os.pardir)
    for cfg in each_sub_command_config(setup_dir):
        for command_name, command in cfg._asdict().items():
            print(command_name, command)

# Generated at 2022-06-13 20:58:49.750642
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdir:
        testdir = os.path.join(tmpdir, 'test_each_sub_command_config')
        os.mkdir(testdir)
        test_setup_cfg = os.path.join(testdir, 'setup.cfg')
        with open(test_setup_cfg, 'w') as fh:
            fh.write('''\
[metadata]
name = test
[console_scripts]
test = test.py:main
''')

# Generated at 2022-06-13 20:59:02.899935
# Unit test for function each_sub_command_config
def test_each_sub_command_config():

    for config in each_sub_command_config():
        # print(config)
        pass

# Generated at 2022-06-13 20:59:10.370634
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    config = list(each_sub_command_config())
    print(config)
    for c in config:
        print(c.name, c.camel, c.description, c.commands)


if __name__ == '__main__':
    from sys import argv
    if argv[0].lower().endswith('__main__.py'):
        test_each_sub_command_config()

# Generated at 2022-06-13 20:59:19.806124
# Unit test for function each_sub_command_config
def test_each_sub_command_config():

    # Test 1: Find each config file
    next(each_sub_command_config())

    # Test 2: No directory given
    with pytest.raises(FileNotFoundError):
        next(each_sub_command_config(None))

    # Test 3: No setup.py file
    with pytest.raises(FileNotFoundError):
        next(each_sub_command_config(''))

    # Test 4: No setup.cfg file
    with pytest.raises(FileNotFoundError):
        next(each_sub_command_config('.'))

# Generated at 2022-06-13 20:59:28.754242
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from pathlib import Path
    import sys

    cwd = os.path.dirname(sys.argv[0])
    cwd = Path(cwd)

    # Setup the test cwd
    cwd = cwd.resolve().parent  # Remove /tests
    cwd = cwd.resolve().parent  # Remove /flutils
    cwd = cwd.joinpath('tests').joinpath('setup_cfg_data')

    # The main
    for out in sorted(
            each_sub_command_config(setup_dir=cwd),
            key=lambda x: x.camel
    ):
        print(out)
# End unit test

# Generated at 2022-06-13 20:59:34.314013
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    this_dir = os.path.dirname(os.path.realpath(__file__))
    for scc in each_sub_command_config(setup_dir=this_dir):
        print(scc)


if __name__ == "__main__":
    test_each_sub_command_config()

# Generated at 2022-06-13 20:59:46.116785
# Unit test for function each_sub_command_config

# Generated at 2022-06-13 20:59:55.569215
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile

    PROJECT_NAME = 'flutils'

    dir_name = tempfile.mkdtemp()

    # Write setup.py file
    setup_py_path = os.path.join(dir_name, 'setup.py')
    assert os.path.isfile(setup_py_path) is False
    with open(setup_py_path, 'w') as f:
        f.write('# setup.py')

    # Write setup.cfg file
    setup_cfg_path = os.path.join(dir_name, 'setup.cfg')
    assert os.path.isfile(setup_cfg_path) is False
    with open(setup_cfg_path, 'w') as f:
        f.write('\n[metadata]\nname = %r\n' % PROJECT_NAME)

   

# Generated at 2022-06-13 21:00:05.313580
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os

    from pathlib import Path

    from flutils.pathutils import iterfiles

    from flutils.setuputils import (
        _each_setup_cfg_command,
        SetupCfgCommandConfig,
        each_sub_command_config
    )

    checks = [
        SetupCfgCommandConfig(
            'devtest', 'Devtest',
            'Runs a development test.',
            tuple(map(lambda x: str(x), iterfiles(
                Path(__file__).parent.parent.parent / 'devtest'
            )))
        )
    ]
    for cfg in each_sub_command_config(__file__):
        assert cfg in checks
        checks.remove(cfg)
    assert not checks


# Generated at 2022-06-13 21:00:07.455177
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    configs = list(each_sub_command_config())
    assert configs


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:00:18.756517
# Unit test for function each_sub_command_config

# Generated at 2022-06-13 21:00:51.931284
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import in_python_package_dir
    import os
    import shutil
    import tempfile
    import textwrap

    THIS_DIR = cast(str, os.path.dirname(os.path.realpath(__file__)))
    package_root = THIS_DIR
    while not in_python_package_dir(package_root) is True:
        package_root = os.path.dirname(package_root)
    package_root = os.path.realpath(package_root)

    with tempfile.TemporaryDirectory() as temp_dir:

        temp_dir = os.path.realpath(temp_dir)
        setup_dir = os.path.join(temp_dir, 'out')
        os.mkdir(setup_dir)


# Generated at 2022-06-13 21:01:03.605620
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.dirname(__file__)

    def test(expected: Tuple[str, ...], actual: Tuple[str, ...]) -> None:
        assert len(expected) == len(actual)
        for exp, act in zip(expected, actual):
            assert exp == cast(str, act)

    for config in each_sub_command_config(setup_dir):
        if config.name == 'lint':
            test(
                expected=(
                    'flake8 {setup_dir}',
                    'isort --check-only --recursive --quiet '
                    '{setup_dir}',
                ),
                actual=config.commands
            )

# Generated at 2022-06-13 21:01:14.123231
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.miscutils import run_cmd
    from pprint import pprint
    from tempfile import mkdtemp
    from shutil import rmtree
    from pathlib import Path
    import logging
    import sys

    setup_dir = mkdtemp()

# Generated at 2022-06-13 21:01:17.852871
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.dirname(__file__)
    for scc in each_sub_command_config(setup_dir):
        assert scc

# Generated at 2022-06-13 21:01:25.256133
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import each_sub_command_config
    from .testutils import (
        each_sub_command_config as _each_sub_command_config,
        get_setup_dir,
    )
    test_configs = tuple(each_sub_command_config(get_setup_dir()))
    assert test_configs == tuple(_each_sub_command_config(get_setup_dir()))

# Generated at 2022-06-13 21:01:30.168771
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    config = next(each_sub_command_config())
    assert config.name == 'myproject'
    assert config.camel == 'Myproject'
    assert config.description == ''
    assert config.commands == ('python -m flutils',
                               'python -m myproject',)

# Generated at 2022-06-13 21:01:34.019216
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config():
        print(config)
        assert config.name


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:01:47.777004
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    config = cast(
        SetupCfgCommandConfig,
        next(each_sub_command_config('../../../'))
    )
    assert config.name == 'help'
    assert config.camel == 'Help'
    assert config.description.startswith(
        'Command to help the user understand and get more information '
        'about how to use the program.'
    )
    expected = (
        'python -m flutils.utilities.autogen',
        'python -m flutils.program.autogen',
        'python -m flutils.program.autogen -h',
        'python -m flutils.program.autogen -d',
        'python -m flutils.program.autogen --debug',
    )
    assert expected == config.commands



# Generated at 2022-06-13 21:01:58.063752
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import io
    import tempfile

    def _write_setup_cfg(fp: io.TextIOBase):
        print("[metadata]", file=fp)
        print("name = 'Test Name'", file=fp)
        print("[setup.command.sub1.sub2]", file=fp)
        print("command = python", file=fp)
        print("         -m pip install", file=fp)
        print("         test-project", file=fp)
        print("     ", file=fp)
        print("     ", file=fp)
        print("     ", file=fp)
        print("[setup.command.sub3]", file=fp)
        print("commands = echo 'sub3'", file=fp)
        print("           echo 'sub3'", file=fp)

# Generated at 2022-06-13 21:02:09.633087
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, str(path))
    sys.path.insert(0, str(os.path.join(path, 'tests', 'usecases')))
    from setup_commands.usecases import (
        get_sub_commands,
        get_sub_commands_with_commands,
        get_sub_commands_with_name,
        get_sub_commands_with_name_commands,
    )
    setup_dir = os.path.join(path, 'tests', 'usecases')
    sc = list(each_sub_command_config(setup_dir))
    assert len(sc) == 4
    assert sc[0] == get_sub_commands()
   

# Generated at 2022-06-13 21:02:40.084468
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def _each_expected_setup_cfg_command_section(
            parser: ConfigParser
    ) -> Generator[Tuple[str, str], None, None]:
        """An expected each_setup_cfg_command_section() Generator."""
        for section in parser.sections():
            section = cast(str, section)
            section = section.strip()
            if section.startswith('setup.command.'):
                command_name = '.'.join(section.split('.')[2:])
                if command_name:
                    yield section, command_name

    def _each_expected_setup_cfg_command(
            parser: ConfigParser,
            format_kwargs: Dict[str, str]
    ) -> Generator[SetupCfgCommandConfig, None, None]:
        """An expected each_setup_cfg_command() Generator."""

# Generated at 2022-06-13 21:02:51.552629
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        file = os.path.join(temp_dir, 'setup.py')
        with open(file, 'w') as fp:
            pass
        file = os.path.join(temp_dir, 'setup.cfg')

# Generated at 2022-06-13 21:03:05.469876
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from unittest import mock

    setup_cfg_path = os.path.join('path', 'to', 'project', 'setup.cfg')
    setup_cfg_content = (
        '[metadata]\n'
        'name = Super Project\n'
        '\n'
        '[setup.command.foo]\n'
        'name = foo\n'
        'command = foo\n'
    )
    setup_commands_cfg_path = os.path.join('path', 'to', 'project',
                                           'setup_commands.cfg')
    setup_commands_cfg_content = (
        '[setup.command.bar]\n'
        'name = bar\n'
        'command = bar\n'
    )

# Generated at 2022-06-13 21:03:14.512569
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config."""
    from .__meta__ import __author__, __name__
    from .util import each_sub_command_config as main
    from .util import _each_setup_cfg_command_section as sub
    from .util import _each_setup_cfg_command as subsub
    from .util import _get_name as subsubsub
    from .util import _prep_setup_dir as subsubsubsub
    from .util import _validate_setup_dir as subsubsubsubsub

    a: List[SetupCfgCommandConfig] = list(each_sub_command_config())

# Generated at 2022-06-13 21:03:30.063836
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def run_test(setup_dir: str, exp_result: List[SetupCfgCommandConfig]):
        cnt = 0
        for res in each_sub_command_config(setup_dir):
            assert res == exp_result[cnt]
            cnt += 1
        assert cnt == len(exp_result)

    def run_test_exc(setup_dir: str, exp_exception: Exception):
        with pytest.raises(exp_exception):
            for _ in each_sub_command_config(setup_dir):
                pass

    setup_dir = os.path.join(
        os.path.dirname(__file__),
        '..',
        'flutils',
        'tests',
        'data',
        'setup_commands',
    )

# Generated at 2022-06-13 21:03:41.307310
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from pathlib import Path

    import os

    import flutils.mypyutils

    PROJECT_DIR = Path(os.path.dirname(__file__))
