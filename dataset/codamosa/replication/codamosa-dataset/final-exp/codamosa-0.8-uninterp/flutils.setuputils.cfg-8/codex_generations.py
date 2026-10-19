

# Generated at 2022-06-13 20:53:56.670854
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.dirname(__file__)
    setup_dir = os.path.join(setup_dir, os.pardir, os.pardir, os.pardir)
    setup_dir = os.path.abspath(setup_dir)
    configs = tuple(each_sub_command_config(setup_dir))
    assert configs
    assert len(configs) > 0

# Generated at 2022-06-13 20:54:06.389288
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.testutil import (
        TEST_ROOT,
        assert_each_line,
        assert_lstrip_line,
        assert_strip_line,
    )
    pkg_dir = os.path.join(TEST_ROOT, 'mock_pkgs')
    for pkg in ('setup_cfg_1', 'setup_cfg_2', 'setup_cfg_3'):
        pkg_path = os.path.join(pkg_dir, pkg)

# Generated at 2022-06-13 20:54:20.775785
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    first = next(each_sub_command_config(os.path.dirname(__file__)))
    assert first == SetupCfgCommandConfig("build", "Build", "", ())

    next(each_sub_command_config(os.path.dirname(__file__)))
    next(each_sub_command_config(os.path.dirname(__file__)))
    next(each_sub_command_config(os.path.dirname(__file__)))
    next(each_sub_command_config(os.path.dirname(__file__)))
    next(each_sub_command_config(os.path.dirname(__file__)))
    next(each_sub_command_config(os.path.dirname(__file__)))

# Generated at 2022-06-13 20:54:32.296747
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit tests for the each_sub_command_config function."""
    import pytest
    from flutils.setuputils import (
        each_sub_command_config,
        SetupCfgCommandConfig,
    )

    def _test_setup_cfg_file(
            setup_dir: Union[str, os.PathLike],
            expected: Tuple[SetupCfgCommandConfig, ...]
    ) -> None:
        assert isinstance(setup_dir, (str, os.PathLike))
        sub_commands = tuple(each_sub_command_config(setup_dir))
        assert sub_commands == expected

    with pytest.raises(FileNotFoundError):
        _test_setup_cfg_file('./', ())
    with pytest.raises(FileNotFoundError):
        _test_setup_cfg

# Generated at 2022-06-13 20:54:38.738416
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.dirname(__file__)

    out = list(each_sub_command_config(setup_dir))
    assert out
    t = out[0]
    assert t.camel == 'TravisCI'
    assert t.commands == ('travis setup releases',)

# Generated at 2022-06-13 20:54:52.140151
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def _assert() -> None:
        setup_cfg_path = os.path.join(os.getcwd(), 'setup.cfg')
        parser = ConfigParser()
        parser.read(setup_cfg_path)
        _get_name(parser, setup_cfg_path)

    try:
        os.chdir(os.path.dirname(__file__))
        for config in each_sub_command_config():
            pass
    finally:
        os.chdir(os.getcwd())

    try:
        os.chdir(os.path.dirname(__file__))
        for config in each_sub_command_config(os.path.dirname(__file__)):
            pass
    finally:
        os.chdir(os.getcwd())


# Generated at 2022-06-13 20:55:02.790166
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    #
    # Load the config
    #
    configs = tuple(each_sub_command_config())

    #
    # Check the names of the configs
    #
    names = tuple(set(map(lambda c: c.name, configs)))
    assert names == (
        'build', 'clean', 'clean_all', 'clean_manifest', 'coverage',
        'docs', 'dist', 'pypi', 'release', 'test', 'watch', 'watch_clean'
    )

    #
    # Check the names of the configs
    #
    camels = tuple(set(map(lambda c: c.camel, configs)))

# Generated at 2022-06-13 20:55:14.783451
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                             '../../..'))
    configs = tuple(each_sub_command_config(setup_dir))
    assert len(configs) > 0
    assert type(configs) is tuple
    assert type(configs[0]) is SetupCfgCommandConfig
    assert type(configs[0].name) is str
    assert type(configs[0].commands) is tuple
    assert type(configs[0].commands[0]) is str
    assert configs[0].name == 'clear-build'
    assert configs[0].camel == 'ClearBuild'
    assert configs[0].description == 'Remove the build directory.'

# Generated at 2022-06-13 20:55:19.587395
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.join(
        os.path.dirname(__file__), os.pardir, os.pardir
    )
    for config in each_sub_command_config(setup_dir):
        print(config)



# Generated at 2022-06-13 20:55:28.812448
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import argparse
    import io
    import sys
    from pprint import pprint
    from flutils.setuputils.command import each_sub_command_config

    # noinspection PyUnusedLocal
    def init_parser(parser: argparse.ArgumentParser) -> None:
        parser.add_argument(
            '--setup-dir',
            '-d',
            help="alternative setup directory location"
        )

    # noinspection PyUnusedLocal
    def run_command(args: argparse.Namespace) -> None:
        pprint(tuple(each_sub_command_config(args.setup_dir)))


# Generated at 2022-06-13 20:55:42.189910
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config(__file__):
        assert isinstance(config, SetupCfgCommandConfig)
        assert config.name
        assert config.camel
        assert config.description
        assert config.commands

# Generated at 2022-06-13 20:55:48.146838
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config():
        assert isinstance(config, SetupCfgCommandConfig)
        assert isinstance(config.name, str)
        assert isinstance(config.camel, str)
        assert isinstance(config.description, str)
        for cmd in config.commands:
            assert isinstance(cmd, str)


if __name__ == '__main__':

    each_sub_command_config(setup_dir=__file__)

    # Unit test
    test_each_sub_command_config()

# Generated at 2022-06-13 20:55:58.403806
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    here = os.path.dirname(__file__)
    tests_dir = os.path.dirname(here)
    pkg_dir = os.path.dirname(tests_dir)
    setup_dir = os.path.dirname(pkg_dir)
    gen = each_sub_command_config(setup_dir)
    assert tuple(gen) == (
        SetupCfgCommandConfig(
            'mypkg.commands.foo',
            'Foo',
            'Some command description.',
            ('command1', 'command2', 'command3')
        ),
    )

# Generated at 2022-06-13 20:56:12.114404
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import chdir
    from tempfile import TemporaryDirectory
    from . import init_cogs
    from .create_setup_command_package import test_create_setup_command_package

    #Create a project in a temporary workspace with the
    #'setup.command' config sections
    with TemporaryDirectory() as tmpdir:
        tmpdir = os.path.join(tmpdir, 'flutils_test_package')
        init_cogs(tmpdir, True)
        test_create_setup_command_package(tmpdir)

        #Create a 'setup_commands.cfg' file in the project's root directory
        #that contains the same 'setup.command' config sections as
        #the project's 'setup.cfg' file

# Generated at 2022-06-13 20:56:18.813084
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config."""
    it = each_sub_command_config(
        setup_dir=os.path.dirname(os.path.dirname(__file__))
    )

# Generated at 2022-06-13 20:56:31.296041
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import pytest

    with pytest.raises(FileNotFoundError):
        next(each_sub_command_config(setup_dir='/does/not/exist'))

    with pytest.raises(FileNotFoundError):
        next(each_sub_command_config(setup_dir='/lib'))

    with pytest.raises(FileNotFoundError):
        next(each_sub_command_config(setup_dir='/bin'))

    with pytest.raises(FileNotFoundError):
        next(each_sub_command_config(setup_dir='/'))

    with pytest.raises(FileNotFoundError):
        next(each_sub_command_config(setup_dir=__file__))


# Generated at 2022-06-13 20:56:43.837507
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import shutil
    import tempfile
    tempdir = tempfile.mkdtemp()

# Generated at 2022-06-13 20:56:54.047413
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    temp_dir = tempfile.TemporaryDirectory()
    setup_cfg_path = os.path.join(temp_dir.name, 'setup.cfg')
    setup_commands_cfg_path = os.path.join(temp_dir.name, 'setup_commands.cfg')
    with open(setup_cfg_path, 'w') as f:
        f.write(
            """\
[metadata]
name = hello-world
version = 1.2.3
"""
        )

# Generated at 2022-06-13 20:57:03.160637
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import re
    from flutils.testutils import temp_chdir
    from flutils.sysutils import (
        CmdResult,
        cmd_result,
    )

    cmd = 'python setup.py test --quiet'
    base_cmds = {
        'test_unit': cmd,
        'test_it': cmd + ' --only-integration-tests',
        'test_samples': cmd + ' --only-sample-tests',
        'test_system': cmd + ' --only-system-tests',
    }
    base_descs = {
        'test_unit': 'Runs the unit tests.',
        'test_it': 'Runs the integration tests.',
        'test_samples': 'Runs the sample tests.',
        'test_system': 'Runs the system tests.',
    }

# Generated at 2022-06-13 20:57:10.866803
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    config = next(each_sub_command_config())
    assert config.name == 'list'
    assert config.camel == 'List'
    assert config.description == 'List all setup commands.'
    assert config.commands == (
        'ls -l',
        'echo',
        'echo "foo"',
        'pwd',
    )
    config = next(each_sub_command_config())
    assert config.name == 'foo'
    assert config.camel == 'Foo'
    assert config.description == 'Foo option.'
    assert config.commands == ()

# Generated at 2022-06-13 20:57:23.338855
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config('tests'):
        assert config.name == 'test_project'
        assert config.camel == 'TestProject'
        assert config.description == 'The description for testing.'
        assert config.commands == ('test_test_project',)
        break
    else:
        raise RuntimeError(
            "Something unexpected happened while testing each_sub_command_config "
            "function."
        )

# Generated at 2022-06-13 20:57:33.862514
# Unit test for function each_sub_command_config
def test_each_sub_command_config():  # noqa: D102
    dirname = os.path.dirname(__file__)
    dirname = os.path.dirname(dirname)
    dirname = os.path.dirname(dirname)
    dirname = os.path.join(dirname, 'sample_project')
    actual = tuple(each_sub_command_config(dirname))

# Generated at 2022-06-13 20:57:40.846159
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import find_cur_dir_up

    cur_dir = find_cur_dir_up('setup.py')
    if cur_dir:
        for ccfg in each_sub_command_config(cur_dir):
            assert ccfg.name is not None
            assert ccfg.commands is not None
    else:
        print("WARNING: Unable to find the directory that contains the "
              "'setup.py' file.")



# Generated at 2022-06-13 20:57:42.687757
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    assert(len(list(each_sub_command_config())) > 0)

# Generated at 2022-06-13 20:57:47.428802
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def _test():
        for command in each_sub_command_config():
            assert 'setup.command' not in command.name
            assert 'setup.command' not in command.description
            assert 'setup.command' not in str(command.commands)
    _test()
    _test()
    _test()
    _test()



# Generated at 2022-06-13 20:57:58.195942
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    paths = [
        '~/Documents/Projects/flutils/setup.cfg',
    ]
    expected = [
        (('Description',), ('docs',), ('docs.build_docs',), ('docs.push_docs')),
        (('Description',), ('test',), ('test.test_the_test_environment')),
    ]
    got = []
    for path in paths:
        path = os.path.expanduser(path)
        setup_dir = os.path.dirname(path)
        for i in each_sub_command_config(setup_dir=setup_dir):
            got.append((i.description, i.commands))
    assert sorted(got) == sorted(expected)

# Generated at 2022-06-13 20:58:09.816138
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile

    setup_cfg_path = os.path.join(tempfile.gettempdir(), 'setup.cfg')
    setup_cfg_path2 = os.path.join(tempfile.gettempdir(), 'setup_commands.cfg')

    def cleanup():
        if os.path.isfile(setup_cfg_path):
            os.remove(setup_cfg_path)
        if os.path.isfile(setup_cfg_path2):
            os.remove(setup_cfg_path2)


# Generated at 2022-06-13 20:58:15.778873
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import pprint
    from inspect import (
        currentframe,
        getframeinfo,
    )

    pprint.pprint(list(each_sub_command_config()))

    info = getframeinfo(currentframe().f_back)
    setup_dir = os.path.dirname(info.filename)
    pprint.pprint(list(each_sub_command_config(setup_dir=setup_dir)))



# Generated at 2022-06-13 20:58:28.323811
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from random import randint
    from unittest.mock import patch
    from typing import Any
    from flutils.packageutils import (
        _Test_SetupCfgCommandConfig
    )
    import tempfile

    def get_setup_commands_cfg(
            commands: List[SetupCfgCommandConfig],
            setup_dir: str
    ) -> str:
        print('commands:', commands)
        lines = [
            '[metadata]',
            'name = some_package',
            '\n'
        ]

# Generated at 2022-06-13 20:58:39.979973
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config"""
    from unittest.mock import patch

    path = None
    with patch.object(os.path, 'realpath', return_value='/path/to/setup.py') \
            as mock_realpath, \
            patch.object(os.path, 'expanduser',
                         return_value='/path/to/home') as mock_expanduser, \
            patch.object(os.path, 'join', return_value=path) \
            as mock_join:
        each_sub_command_config()
        assert mock_realpath.call_count == 1
        assert mock_realpath.call_args[0][0] == '.'
        assert mock_expanduser.call_count == 1
        assert mock_expanduser.call_args

# Generated at 2022-06-13 20:58:59.820737
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.testutils.show_output import (
        print_str,
        print_sep
    )
    print_str('Running "each_sub_command_config" unit tests:')
    print_sep()

    sample_dir = os.path.join(
        os.path.dirname(__file__), '..', '..', 'sample', 'sample_cmd'
    )

    for config in each_sub_command_config(sample_dir):
        print_str(config)


if __name__ == '__main__':
    def main() -> int:
        import sys
        from flutils.testutils.show_output import (
            print_str,
            print_sep
        )
        print_str('Running "each_sub_command_config" unit tests:')
        print_

# Generated at 2022-06-13 20:59:09.132263
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.testutils import TemporaryDirectory
    from sys import path
    import tempfile
    from os import curdir, sep
    from os.path import expanduser, join, realpath
    from typing import Any
    from typing import Dict
    from typing import Generator as GeneratorType
    from typing import Optional
    from typing import Sequence
    from typing import TypeVar
    from typing import Union

    t = TypeVar('t')


# Generated at 2022-06-13 20:59:21.626693
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    assert os.path.isdir('tests') is True
    assert os.path.isdir('tests/files') is True
    tests_dir_path = os.path.dirname(os.path.realpath(__file__))
    assert os.path.basename(tests_dir_path) == 'tests'
    assert os.path.isdir(os.path.join(tests_dir_path, 'files')) is True
    path = os.path.join(tests_dir_path, 'files', 'pre_commit_config.yaml')
    assert os.path.isfile(path) is True
    assert os.path.realpath(path) == path

    setup_dir = os.path.dirname(path)
    assert os.path.basename(setup_dir) == 'files'

# Generated at 2022-06-13 20:59:31.187604
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile as tmp
    import json as jsonlib

# Generated at 2022-06-13 20:59:42.444932
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # noinspection PyUnresolvedReferences
    from flutils.testutils import test_path
    from flutils.setup import setup_utils
    from pathlib import Path
    from tempfile import TemporaryDirectory
    from textwrap import dedent

    # Test
    tmp_dir = str(test_path(setup_utils))
    with TemporaryDirectory() as tmp_dir:
        setup_dir = Path(os.path.join(tmp_dir, 'test-setup'))
        setup_dir.mkdir()

        # Test that a generic project directory is handled properly.

# Generated at 2022-06-13 20:59:54.521296
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # fmt: off
    expected = SetupCfgCommandConfig(
        'docs.build',
        'DocsBuild',
        'Build the documentation.',
        ('sphinx-build docs docs/_build',)
    )
    # fmt: on
    setup_dir = os.path.abspath(os.path.dirname(__file__))
    setup_dir = os.path.realpath(os.path.join(setup_dir, '..'))
    setup_dir = os.path.realpath(os.path.join(setup_dir, '..'))
    for out in each_sub_command_config(setup_dir):
        assert out == expected
        break

# Generated at 2022-06-13 21:00:04.593083
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pyutils import (
        each_key_value,
        each_key_value_str,
    )
    def verify_output(
            actual: SetupCfgCommandConfig,
            expected: SetupCfgCommandConfig,
            msg: str
    ) -> None:
        assert actual.name == expected.name, msg
        assert actual.camel == expected.camel, msg
        assert actual.description == expected.description, msg
        assert actual.commands == expected.commands, msg
    def _test() -> None:
        yield SetupCfgCommandConfig(
            'test.test',
            'Test_Test',
            'test the test command',
            ('echo "test test command"',)
        )

# Generated at 2022-06-13 21:00:16.609153
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.testutils import captured_output

    test_path = os.path.join(os.path.dirname(__file__), 'test')

    path = os.path.join(test_path, 'setup.cfg')
    parser = ConfigParser()
    parser.read(path)
    name = _get_name(parser, path)

    path1 = os.path.join(test_path, 'setup_commands.cfg')
    parser = ConfigParser()
    parser.read(path1)
    name1 = _get_name(parser, path)

    if name != name1:
        msg = "The name set in the 'setup.cfg' file and the "
        msg += "'setup_commands.cfg' files are different.  They "
        msg += "MUST be the same."
        raise ValueError

# Generated at 2022-06-13 21:00:24.679080
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    file_name = __file__
    if os.path.isfile(file_name):
        file_name = os.path.dirname(file_name)

    setup_dir = file_name.replace('flutils', 'flutils.test')
    setup_dir = os.path.join(setup_dir, 'data')

    for config in each_sub_command_config(setup_dir):
        commands = config.commands
        assert isinstance(commands, tuple)
        assert len(commands) > 0
        command = commands[0]
        command = command.replace('cd {setup_dir}', '')
        command = command.replace('export PYTHONPATH="{setup_dir}', '')
        command = command.replace('eval "export', '')
        command = command.replace('export', '')

# Generated at 2022-06-13 21:00:37.070644
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # The mocked module was put in the directory
    # <project_root>/tests/mocks/setup_commands.
    mock_setup_commands_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'mocks/setup_commands'
    )
    config: SetupCfgCommandConfig
    for config in each_sub_command_config(mock_setup_commands_path):
        pass
    assert config.camel == 'SubCommand'
    assert config.name == 'sub_command'
    assert config.description == (
        'For testing the `each_sub_command_config` function'
    )

# Generated at 2022-06-13 21:00:54.567606
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    print('Testing each_sub_command_config():')
    pyscript_dir: str = os.path.dirname(os.path.abspath(__file__))
    for sc in each_sub_command_config(pyscript_dir):
        print('\t', sc)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:01:01.689990
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import flutils.testutils
    import pathlib

    if not flutils.testutils.TESTING_ENABLE_COVERAGE:
        return

    assert each_sub_command_config() is not None, \
        "Test failed at line: %d" % flutils.testutils.lineno()

    path = pathlib.Path(__file__).parent
    path = pathlib.Path(path, 'testdata').as_posix()
    assert next(each_sub_command_config(path)) is not None, \
        "Test failed at line: %d" % flutils.testutils.lineno()

# Generated at 2022-06-13 21:01:03.552547
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    out = list(each_sub_command_config(__file__))
    assert len(out) == 0

# Generated at 2022-06-13 21:01:08.844848
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    THIS_DIR = os.path.dirname(__file__)
    path = os.path.join(THIS_DIR, '..', '..', 'tests', 'data', 'project1')
    print(path)
    for i in each_sub_command_config(path):
        print(i)

# Generated at 2022-06-13 21:01:11.304094
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    assert next(each_sub_command_config(), None) is not None



# Generated at 2022-06-13 21:01:17.550597
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from pprint import pformat
    from flutils.pathutils import get_file_name
    for command in each_sub_command_config():
        print(pformat(command))
    # Tests that it can find the 'setup.py' file when running as a unit test.
    this_file_path = get_file_name(os.path.abspath(__file__))
    for _ in each_sub_command_config(this_file_path):
        pass



# Generated at 2022-06-13 21:01:21.509896
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config():
        print(config)


all_sub_command_configs = tuple(each_sub_command_config())

# Generated at 2022-06-13 21:01:28.840496
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import local_path
    setup_dir = local_path('tests', 'test_project')
    for config in each_sub_command_config(setup_dir):
        pass


if __name__ == '__main__':
    from flutils.pathutils import local_path
    setup_dir = local_path('tests', 'test_project')
    for config in each_sub_command_config(setup_dir):
        print(config.commands)

# Generated at 2022-06-13 21:01:39.446942
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    cfg = list(each_sub_command_config())

# Generated at 2022-06-13 21:01:46.082778
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def _validate_config(config: SetupCfgCommandConfig) -> None:
        assert isinstance(config.name, str)
        assert isinstance(config.camel, str)
        assert isinstance(config.description, str)
        assert isinstance(config.commands, tuple)
        for command in config.commands:
            assert isinstance(command, str)

    for config in each_sub_command_config():
        _validate_config(config)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:02:23.473730
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from os import path
    from itertools import islice
    from sys import executable
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as td:
        td = str(td)
        _setup_py_path = path.join(td, 'setup.py')
        _setup_cfg_path = path.join(td, 'setup.cfg')
        _setup_commands_cfg_path = path.join(td, 'setup_commands.cfg')
        with open(_setup_py_path, 'w') as file:
            file.write('# This is a setup.py file')
        with open(_setup_cfg_path, 'w') as file:
            file.write(
                "[metadata]\n"
                "name =\n"
            )

# Generated at 2022-06-13 21:02:35.856350
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def f():
        pass

# Generated at 2022-06-13 21:02:43.068172
# Unit test for function each_sub_command_config
def test_each_sub_command_config():  # pylint: disable=unused-variable
    from tempfile import TemporaryDirectory
    from shutil import rmtree
    from os import environ, path, symlink
    from itertools import islice

    with TemporaryDirectory(prefix='setup__utils') as tmpdir:
        setup_dir = path.join(tmpdir, 'src', 'pypkg')
        os.makedirs(setup_dir)

# Generated at 2022-06-13 21:02:53.104655
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # pylint: disable=import-outside-toplevel
    from flutils.common.fileutils import each_dir_file_path
    from flutils.common.funcutils import onerror
    import sys

    import pytest

    try:
        sys.path.insert(0, os.path.dirname(__file__))
        import setup_commands
    finally:
        del sys.path[0]

    setup_dir = os.path.dirname(setup_commands.__file__)
    expected: List[Tuple[SetupCfgCommandConfig, ...]] = []
    if not os.environ.get('TRAVIS'):
        with open(os.path.join(setup_dir, 'setup_commands.cfg')) as file_obj:
            setup_cfg_str = file_obj.read

# Generated at 2022-06-13 21:02:58.856760
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.envutils import ensure_environment_is_clean

    ensure_environment_is_clean()
    for command in each_sub_command_config():
        print(command)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:03:11.619129
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import pytest

    def _load_all():
        """Loads all configs and returns a list of the names of each command."""
        out: List[str] = []
        for scc in each_sub_command_config():
            out.append(scc.name)
        return out

    # Basic test with the test and unit test commands already in the
    # config files
    sys.argv = [sys.argv[0], '--test', '--unit_test']
    expected = [
        'test',
        'unit_test',
    ]
    actual = _load_all()
    assert len(actual) == len(expected)
    for actual_item, expected_item in zip(sorted(actual), sorted(expected)):
        actual_item = actual_item
        assert actual_item

# Generated at 2022-06-13 21:03:22.414424
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.toolutils import each_sub_command_config
    from flutils.toolutils import SetupCfgCommandConfig

    # Return value tests
    exp = SetupCfgCommandConfig(
        'check',
        'Check',
        'Check git history and test files',
        (
            'python -m flake8 ./setup.py',
            'python -m flake8 src tests'
        )
    )
    results = list(each_sub_command_config())
    assert any(r.name == exp.name for r in results)

    # Test 'setup_dir' argument
    exp = SetupCfgCommandConfig(
        'parser.build',
        'ParserBuild',
        'Generate the parser code for the Python version',
        (
            'python tests/test_version.py'
        )
    )


# Generated at 2022-06-13 21:03:29.353342
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.filesystem import relative_to
    import inspect
    import pprint
    from pathlib import Path
    this_file = Path(inspect.getfile(inspect.currentframe())).resolve()
    setup_dir = relative_to(this_file, 'tests')
    configs = list(each_sub_command_config(setup_dir))
    pprint.pprint(configs)



# Generated at 2022-06-13 21:03:35.438542
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    out = list(each_sub_command_config())
    assert isinstance(out, list)
    for item in out:
        assert isinstance(item, SetupCfgCommandConfig)
        assert isinstance(item.name, str)
        assert isinstance(item.camel, str)
        assert isinstance(item.description, str)
        assert isinstance(item.commands, tuple)
        for command in item.commands:
            assert isinstance(command, str)
    if not out:
        raise SystemExit(1)

