

# Generated at 2022-06-13 20:54:02.353705
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import itertools
    import unittest

    class EachSubCommandConfigTestCase(unittest.TestCase):
        """Unit tests for function each_sub_command_config"""
        @staticmethod
        def _get_pkg_name(setup_dir: str) -> str:
            """Returns the package name from a setup_dir."""
            setup_command_configs = tuple(
                each_sub_command_config(setup_dir)
            )
            if not setup_command_configs:
                raise LookupError(
                    "The given 'setup_dir' of %r does NOT contain any "
                    "setup commands." % setup_dir
                )
            pkg_name = setup_command_configs[0].name
            pkg_name = pkg_name.partition('=')[0].strip()
           

# Generated at 2022-06-13 20:54:09.406299
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    ret = next(each_sub_command_config())
    assert SetupCfgCommandConfig(
        name='clean',
        camel='Clean',
        description='Clean up files.',
        commands=('find -name "*.pyc" -delete', 'find -name "__pycache__" -delete')
    ) == ret



# Generated at 2022-06-13 20:54:21.632685
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    expected = [
        SetupCfgCommandConfig(
            'my_project.my_sub_command',
            'MyProjectMySubCommand',
            'My sub command.',
            ('my_sub_command {name} {setup_dir}',)
        ),
        SetupCfgCommandConfig(
            'my_project.another_sub_command',
            'MyProjectAnotherSubCommand',
            'My another sub command.',
            ('another_sub_command {name} {home}',)
        ),
        SetupCfgCommandConfig(
            'my_project.yet_another_sub_command',
            'MyProjectYetAnotherSubCommand',
            'My yet another sub command.',
            ('yet_another_sub_command {name} {setup_dir}',)
        ),
    ]


# Generated at 2022-06-13 20:54:27.756043
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import here, parent_dirs
    for path in parent_dirs(here(), 'setup.py'):
        setup_dir = os.path.dirname(path)
        for config in each_sub_command_config(setup_dir):
            print("config: %s" % config)



# Generated at 2022-06-13 20:54:39.371223
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with TemporaryDirectory() as tmp_dir:
        tmp_dir = str(tmp_dir)
        setup_cfg_path = os.path.join(tmp_dir, 'setup.cfg')
        with open(setup_cfg_path, 'w', encoding='utf8') as f:
            f.write('[metadata]\n')
            f.write('name = flutils\n')
            f.write('\n')
            f.write('[setup.command.test]\n')
            f.write('name = Test for flutils\n')
            f.write('description = Runs the unit tests.\n')
            f.write('command = pytest --cov=flutils --cov-report=term-missing\n')
            f.write('\n')

# Generated at 2022-06-13 20:54:52.185372
# Unit test for function each_sub_command_config
def test_each_sub_command_config():

    with tempfile.TemporaryDirectory() as temp_dir:
        setup_cfg_contents = '''
[metadata]
name = {name}

[setup.command.foo]
commands =
    echo "foo command 1"
    echo "foo command 2"
    echo "foo command 3"

[setup.command.bar]
commands =
    echo "bar command 1"
    echo "bar command 2"
    echo "bar command 3"
'''  # noqa: E501
        name = 'tstpackage'
        setup_cfg_contents = setup_cfg_contents.format(name=name)
        with open(os.path.join(temp_dir, 'setup.cfg'), 'w') as f:
            f.write(setup_cfg_contents)

# Generated at 2022-06-13 20:55:02.789630
# Unit test for function each_sub_command_config
def test_each_sub_command_config():  # noqa
    """Unit test to test function each_sub_command_config."""
    import sys
    if sys.version_info < (3, 6):
        return
    from unittest import mock
    from flutils.pathutils import rm

    def mock_parser(contents: str) -> ConfigParser:
        return mock.Mock(
            spec=ConfigParser,
            **{'sections.return_value': ('setup.command.foo',
                                         'setup.command.bar')},
            **{'options.return_value': ('command', ),
               'get.return_value': contents,
               'get.side_effect': ConfigParser().get}
        )

    # Test empty parser
    cp = ConfigParser()
    with mock.patch('configparser.ConfigParser', return_value=cp):
        data = tuple

# Generated at 2022-06-13 20:55:10.444041
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_cfg_path = 'setup.cfg'
    parser = ConfigParser()
    parser.read(setup_cfg_path)
    format_kwargs = {
        'name': _get_name(parser, setup_cfg_path),
        'setup_dir': _prep_setup_dir()
    }
    yield from _each_setup_cfg_command(parser, format_kwargs)


if __name__ == '__main__':
    for command in each_sub_command_config():
        print(command)

# Generated at 2022-06-13 20:55:22.597401
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import unittest
    import tempfile
    import os
    import shutil

    class TestEachSubCommandConfig(unittest.TestCase):
        def test_sub_command_config(self):
            with tempfile.TemporaryDirectory() as dirpath:
                setup_cfg = os.path.join(dirpath, 'setup.cfg')
                os.makedirs(os.path.join(dirpath, 'src', 'flutils'),
                            exist_ok=True)
                with open(setup_cfg, 'w') as f:
                    f.write('[metadata]\nname = flutils\n')
                setup_commands_cfg = os.path.join(dirpath, 'setup_commands.cfg')

# Generated at 2022-06-13 20:55:28.682271
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(path, '..', '..')
    results = list(each_sub_command_config(path))
    assert len(results) == 1
    assert results[0].name == 'my-project.my_sub_command'
    assert results[0].commands == ('echo test',)


if __name__ == '__main__':
    import sys
    sys.exit(test_each_sub_command_config())

# Generated at 2022-06-13 20:55:47.515361
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import (
        is_empty_dir,
        remove_tree,
        temp_directory,
    )
    from flutils.shellutils import (
        chdir,
        cmd_exec,
    )
    from flutils.systemutils import (
        cls,
        get_cwd,
        set_cwd,
    )
    from flutils.textutils import (
        dedent,
        formatted_date_time,
    )

    # Basic template

# Generated at 2022-06-13 20:56:01.116651
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import shutil
    import tempfile
    from flutils.fileutils import safe_mkdir

    def _write_setup_cfg(name: str, commands: Dict[str, str]) -> str:
        parser = ConfigParser()
        parser.add_section('metadata')
        parser.set('metadata', 'name', name)
        for section, val in commands.items():
            parser.add_section(section)
            parser.set(section, 'commands', val)
        path = os.path.join(tmpdir, 'setup.cfg')
        with open(path, 'w') as f:
            parser.write(f)
            return path

    def _write_setup_commands_cfg(
            commands: Dict[str, str]
    ) -> Optional[str]:
        parser = ConfigParser()

# Generated at 2022-06-13 20:56:01.999991
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    pass



# Generated at 2022-06-13 20:56:13.276464
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    here = os.path.dirname(os.path.abspath(__file__))
    for setup_dir in ('', here, os.path.join(here, '..', '..')):
        if setup_dir:
            try:
                _validate_setup_dir(setup_dir)
            except (FileNotFoundError, NotADirectoryError):
                continue
            else:
                break
    else:
        raise FileNotFoundError(
            "Unable to find the directory that contains the 'setup.py' file."
        )
    format_kwargs: Dict[str, str] = {
        'setup_dir': _prep_setup_dir(setup_dir),
        'home': os.path.expanduser('~')
    }

# Generated at 2022-06-13 20:56:20.462640
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    this_file_path = os.path.abspath(__file__)
    parent_dir_path = os.path.dirname(this_file_path)
    parent_dir_path = os.path.dirname(parent_dir_path)
    parent_dir_path = os.path.dirname(parent_dir_path)
    for x in each_sub_command_config(parent_dir_path):
        print(x)

# Generated at 2022-06-13 20:56:32.337046
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from unittest.mock import patch
    from flutils.pathutils import touch

    with patch('os.path.dirname', return_value='/path/to/dir'):
        with patch('os.path.isfile', return_value=True):
            list(each_sub_command_config())

    with patch('os.path.dirname', return_value='/path/to/dir'):
        with patch('os.path.isfile', side_effect=[False, True, True]):
            list(each_sub_command_config())


# Generated at 2022-06-13 20:56:39.340724
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for cmd in each_sub_command_config():
        assert isinstance(cmd.name, str)
        assert isinstance(cmd.camel, str)
        assert isinstance(cmd.description, str)
        for cmd_str in cmd.commands:
            assert isinstance(cmd_str, str)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:56:50.804826
# Unit test for function each_sub_command_config

# Generated at 2022-06-13 20:57:02.766118
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import (
        get_abs_path,
    )
    from flutils.strutils import (
        random_str,
    )
    import shutil
    import tempfile
    setup_dir = tempfile.mkdtemp(prefix=random_str(6))
    setup_file = get_abs_path(
        os.path.join(setup_dir, 'setup.py')
    )
    setup_cfg_file = get_abs_path(
        os.path.join(setup_dir, 'setup.cfg')
    )
    setup_cmd_cfg_file = get_abs_path(
        os.path.join(setup_dir, 'setup_commands.cfg')
    )


# Generated at 2022-06-13 20:57:10.984320
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    import platform
    import subprocess
    import tempfile
    import shutil
    import flutils

    test_dir = os.path.dirname(os.path.abspath(__file__))
    setup_dir = os.path.join(test_dir, 'setup_commands')
    out_dir = os.path.join(test_dir, 'test_output')
    cfg_dir = os.path.join(test_dir, 'test_config')
    if not os.path.isdir(out_dir):
        os.mkdir(out_dir)
    out_file = os.path.join(out_dir, 'each_sub_command_config.txt')
    cwd = os.getcwd()


# Generated at 2022-06-13 20:57:21.773760
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # BUG: This needs to be run using pytest within the code dir
    from pprint import pprint
    pprint(list(each_sub_command_config()))



# Generated at 2022-06-13 20:57:26.806869
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for name, camel, description, commands in \
            each_sub_command_config(os.path.dirname(__file__)):
        print(name, camel, description, commands)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:57:39.443439
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..',
        '..'
    )
    command_configs = list(each_sub_command_config(setup_dir))
    assert len(command_configs) == 1
    command = command_configs[0]

    assert command.name == 'test'
    assert command.camel == 'Test'
    assert command.description == (
        'A sample command for unit testing.'
    ), command.description
    assert tuple(command.commands) == (
        'pytest -v -q test/',
    )


if __name__ == '__main__':
    import pytest
    pytest.main([__file__, '-s', '-v'])

# Generated at 2022-06-13 20:57:50.924225
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit tests for the function each_sub_command_config."""
    import sys
    import logging
    import contextlib
    import tempfile
    import shutil
    from io import StringIO
    cwd = os.getcwd()
    tmpdir = tempfile.mkdtemp(prefix='TestSetupCfg_')
    sys.path.append(tmpdir)

# Generated at 2022-06-13 20:58:02.355660
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with open('./setup_commands.cfg', 'w') as f:
        f.write('''
[setup.command.list_tasks]
name = {name} list-tasks sub-command
description = List all the tasks of the project
commands =
    flutils {name} list-tasks --help
''')

    for config in each_sub_command_config():
        assert config.name == 'tests.test_setup_command.test_each_sub_command_config list-tasks sub-command'
        assert config.camel == 'TestSetupCommandTestEachSubCommandConfigListTasksSubCommand'
        assert config.description == 'List all the tasks of the project'
        assert len(config.commands) == 1

# Generated at 2022-06-13 20:58:08.744727
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    os.chdir(os.path.dirname(__file__))
    for config in each_sub_command_config('tests/project'):
        assert isinstance(config.name, str)
        assert isinstance(config.camel, str)
        assert isinstance(config.description, str)
        assert isinstance(config.commands, (tuple, list))
        for command in config.commands:
            assert isinstance(command, str)

# Generated at 2022-06-13 20:58:11.797074
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    try:
        list(each_sub_command_config())
    except Exception as e:
        assert False, e

# Generated at 2022-06-13 20:58:18.921621
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from inspect import getsourcefile

    from flutils.pathutils import realpath_from_caller

    from ._test.test_utils import (
        capture,
        directory_path,
        get_python_module
    )

    from . import _test

    if 'setup.py' in get_python_module():

        def _test_sub_command(sub_command: SetupCfgCommandConfig) -> None:
            assert sub_command.commands
            with capture() as cap:
                _test.main(sub_command.name)
            assert cap.out

        with directory_path():
            modpath = (
                realpath_from_caller(
                    '_test_each_sub_command_config.py',
                    'flutils.sub_command.utils'
                )
            )
            _test_sub_

# Generated at 2022-06-13 20:58:31.519356
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os.path as osp
    from flutils.pathutils import make_relative_to_root
    import sys

    def each_config():
        yield from each_sub_command_config(setup_dir)

    # Make the path to the 'setup' directory relative to the project's root.
    setup_dir = make_relative_to_root(osp.abspath(__file__), 'setup')
    project_name = 'flutils'

    # Ensure that the project name is set in the config file.
    parsed_name = None
    for config in each_config():
        parsed_name = config.name

    assert parsed_name == project_name

    # Ensure that the setup path is set in the config file.
    parsed_path = None

# Generated at 2022-06-13 20:58:38.605225
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.dirname(__file__)
    out = list(each_sub_command_config(setup_dir))
    assert len(out) == 2
    assert out[0].name == 'sdist'
    assert out[0].commands == ('echo sdist', )
    assert out[1].name == 'bdist_wheel'
    assert out[1].commands == ('echo bdist_wheel', )

# Generated at 2022-06-13 20:59:05.483907
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from itertools import islice

    def _validate_cmds(
            generator: Generator[SetupCfgCommandConfig, None, None]
    ) -> None:
        assert all(map(
            lambda cmd: any(map(lambda cmd_: cmd_ == 'build', cmd.commands)),
            islice(generator, 0, 1),
        ))
        assert all(map(
            lambda cmd: any(map(lambda cmd_: cmd_ == 'build_sphinx', cmd.commands)),
            islice(generator, 1, 2),
        ))
        assert all(map(
            lambda cmd: any(map(lambda cmd_: cmd_ == 'setup.py', cmd.commands)),
            islice(generator, 2, 3),
        ))

# Generated at 2022-06-13 20:59:15.792639
# Unit test for function each_sub_command_config

# Generated at 2022-06-13 20:59:18.487142
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import flutils

    for scf in each_sub_command_config(flutils.FILE_DIR):
        print(scf)

# Generated at 2022-06-13 20:59:29.441847
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import re
    import sys
    from pathlib import Path
    from tempfile import (
        TemporaryDirectory,
        TemporaryFile,
    )
    from unittest import (
        main,
        TestCase,
    )

    class Test(TestCase):
        def test_setup_dir(self):
            with self.assertRaises(FileNotFoundError):
                list(each_sub_command_config('/does/not/exist'))

            with self.assertRaises(NotADirectoryError):
                list(each_sub_command_config(__file__))

            with self.assertRaises(FileNotFoundError):
                list(each_sub_command_config('/etc'))


# Generated at 2022-06-13 20:59:41.441287
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import in_temp_dir
    setup_dir = in_temp_dir(prefix='setup_dir', suffix='.d')
    setup_file = os.path.join(setup_dir, 'setup.py')
    setup_cfg = os.path.join(setup_dir, 'setup.cfg')
    setup_cmds_cfg = os.path.join(setup_dir, 'setup_commands.cfg')

    with open(setup_file, 'w') as f:
        f.write("""
from setuptools import setup

if __name__ == '__main__':
    setup()
""")

    with open(setup_cfg, 'w') as f:
        f.write("""
[metadata]
name = flutils
""")


# Generated at 2022-06-13 20:59:50.148793
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from pytest import raises

    with raises(FileNotFoundError):
        list(each_sub_command_config('./tests/bogus'))

    out = list(each_sub_command_config('./tests/data/setup_manager'))
    assert len(out) == 2

    out = list(each_sub_command_config('./tests/data/setup_commands'))
    assert len(out) == 2



# Generated at 2022-06-13 20:59:51.524903
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # TODO: Write unit tests.
    pass

# Generated at 2022-06-13 21:00:02.575997
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from os import makedirs

    from flutils.testing import temp_directory
    from flutils.testing import unittest

    class TestEachSubCommandConfig(unittest.TestCase):

        def test_each_sub_command_config(self):
            with temp_directory(prefix='test_each_sub_command_config') as td:
                td = os.path.join(td, 'setup_dir')
                os.makedirs(td)
                setup_cfg_path = os.path.join(td, 'setup.cfg')
                with open(setup_cfg_path, 'w') as fh:
                    fh.write('[metadata]\n')
                    fh.write('name = flutils.test.test\n')

# Generated at 2022-06-13 21:00:15.291518
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # Setup
    from collections import Counter
    from os import remove
    from os.path import isfile
    from tempfile import mkdtemp
    from unittest import TestCase

    from flutils.configutils import ConfigParser
    from flutils.configutils import IniFile
    from flutils.configutils import Section

    class TestClass(TestCase):

        @classmethod
        def setUpClass(cls) -> None:
            cls.setup_dir = mkdtemp(prefix='flutils-test-')

        def test_each_sub_command_config(self):

            def _test_func(
                    setup_dir: str,
                    expected: Counter,
                    cfg_path: os.PathLike,
                    cfg_text: str,
                    name: str = 'example-package'
            ):
                cfg

# Generated at 2022-06-13 21:00:24.168925
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import set_cwd_to_example_dir
    from flutils.envutils import export_to_envvar
    from flutils.testutils import quiet
    from flutils._vendor.jupyterlab_code_formatter._version import VERSION
    from flutils._vendor.jupyterlab_code_formatter.conda_kits.context.setup_commands \
        import (
            jupyter_pre_commit_check,
        )

# Generated at 2022-06-13 21:00:40.281422
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config('/Users/rjassal/Projects/flutils'):
        print(config)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:00:51.863962
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import setup_commands.cli

    def _each_setup_cfg_command_section(parser):
        return _each_setup_cfg_command_section(parser)

    def _each_setup_cfg_command(parser, format_kwargs):
        return _each_setup_cfg_command(parser, format_kwargs)

    def _get_name(parser, setup_cfg_path):
        return _get_name(parser, setup_cfg_path)

    def _prep_setup_dir(setup_dir=None):
        return _prep_setup_dir(setup_dir)

    def each_sub_command_config(setup_dir=None):
        return setup_commands.cli.each_sub_command_config(setup_dir)

    import os
    import tempfile
    import unittest

# Generated at 2022-06-13 21:01:03.552541
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    from pathlib import Path
    from tempfile import TemporaryDirectory
    from unittest import TestCase
    from unittest.mock import patch

    class EachSubCommandConfigUnitTest(TestCase):
        def test_each_sub_command_config(self):
            with TemporaryDirectory(prefix='temp_each_sub_command_config') \
                    as temp_dir:
                temp_dir = Path(temp_dir)
                temp_dir.joinpath('setup.py').touch()
                temp_dir.joinpath('setup.cfg').touch()
                path = temp_dir.joinpath('setup_commands.cfg')

# Generated at 2022-06-13 21:01:13.542564
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    tmp_setup_commands_cfg_path = None
    tmp_setup_py_path = None
    tmp_setup_cfg_path = None

# Generated at 2022-06-13 21:01:27.349846
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import pprint
    for cfg in each_sub_command_config('tests/data/pkg1'):
        print(cfg)
    #   SetupCfgCommandConfig(
    #       name='clean',
    #       camel='Clean',
    #       description='Clean out the stuff',
    #       commands=('rm -rf build', 'rm -rf dist')
    #   )
    #   SetupCfgCommandConfig(
    #       name='build',
    #       camel='Build',
    #       description='Build the distribution',
    #       commands=('python setup.py sdist bdist_wheel',)
    #   )
    #   SetupCfgCommandConfig(
    #       name='publish',
    #       camel='Publish',
    #       description='Publish the distribution',
    #       commands=('tw

# Generated at 2022-06-13 21:01:37.817647
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config."""
    setup_dir = os.path.realpath(
        os.path.expanduser(
            os.path.expandvars(
                os.path.join(
                    '~',
                    'git',
                    'flutils.py'
                )
            )
        )
    )
    sc = list(each_sub_command_config(setup_dir))
    assert sc[0].camel == 'Build'
    assert sc[0].commands == (
        'python setup.py sdist bdist_wheel',
        'twine upload dist/*',
    )


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:01:46.845044
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from unittest.mock import patch

    # Test that it raises FileNotFoundError when the source file cannot be
    # found.
    with patch('os.path.isfile') as mock_isfile:
        mock_isfile.return_value = False
        try:
            list(each_sub_command_config('/home'))
            assert False, 'FileNotFoundError not raised.'
        except FileNotFoundError:
            pass

    # Test that it raises FileNotFoundError when the ``setup.cfg`` file
    # cannot be found.
    with patch('os.path.isfile') as mock_isfile:
        mock_isfile.side_effect = (True,)

# Generated at 2022-06-13 21:01:53.362520
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.logutils import setup_test_logger
    from flutils.configutils import each_sub_command_config
    from pprint import pprint as pp
    from sys import stderr
    print('Testing each_sub_command_config()', file=stderr)
    setup_test_logger(name='flutils')
    pp(list(each_sub_command_config()))

# Generated at 2022-06-13 21:02:02.475170
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import (
        cd
    )
    for rt, ds, fs in os.walk(os.path.dirname(__file__)):
        for d in ds:
            if d == 'test_project':
                with cd(os.path.join(rt, d)):
                    for cfg in each_sub_command_config():
                        assert cfg
    with cd(os.path.dirname(__file__)):
        for cfg in each_sub_command_config():
            assert cfg

# Generated at 2022-06-13 21:02:13.183947
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def test(setup_dir: os.PathLike):
        out = list(each_sub_command_config(setup_dir))
        assert len(out) == 2
        assert out[0].name == 'build'
        assert out[0].camel == 'Build'
        assert out[0].description == 'Build the Sphinx documentation.'
        assert out[0].commands == ('clean', 'build -b html -d build')
        assert out[1].name == 'deploy'
        assert out[1].camel == 'Deploy'
        assert out[1].description == 'Deploy the Sphinx documentation.'
        assert out[1].commands == ('clean', 'build -b html -d build')

    test('tests/data/setup_commands')

# Generated at 2022-06-13 21:02:36.331052
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with patch('os.path.expanduser') as mock:
        mock.return_value = 'user_home'
        with patch('os.path.isfile') as mock:
            mock.return_value = False
            with patch('os.path.isdir') as mock:
                mock.return_value = True
                with patch('os.path.exists') as mock:
                    mock.return_value = True
                    with patch('os.path.realpath') as mock:
                        mock.return_value = 'dir'
                        with patch('configparser.ConfigParser.sections') as mock:
                            mock.return_value = ['section']
                            with patch('configparser.ConfigParser.options') as mock:
                                mock.return_value = ['option']

# Generated at 2022-06-13 21:02:45.240306
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import pprint
    from flutils.pkgutils import package_dir

    each = each_sub_command_config(setup_dir=package_dir())
    for i in each:
        print('Dictionary:')
        pprint.pprint(i._asdict())
        print('\n')
        print('Under`score:       ', i.name)
        print('CamelCase:         ', i.camel)
        print('Description:       ', i.description)
        print('Commands:')
        pprint.pprint(i.commands, indent=4)
        print('\n\n')


# Generated at 2022-06-13 21:02:54.135870
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    pwd = os.getcwd()
    print(pwd)
    print(os.path.dirname(pwd))
    print(os.path.dirname(os.path.dirname(pwd)))
    print(os.path.dirname(os.path.dirname(os.path.dirname(pwd))))
    for x in each_sub_command_config(setup_dir=os.path.dirname(os.path.dirname(pwd))):
        print(x)
        for c in x.commands:
            print(c)
    for x in each_sub_command_config(setup_dir=os.path.dirname(pwd)):
        print(x)
        for c in x.commands:
            print(c)


# Generated at 2022-06-13 21:03:07.503879
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.testhelpers import (
        mk_temp_dir,
        TempDir,
    )
    from flutils.config.tests._setup_cfg_example import (
        SETUP_CFG,
        SETUP_COMMANDS,
    )
    from dulwich import __version__ as dulwich_version
    from dulwich.tests.compat import StringIO
    from flutils.commands import (
        SETUP_FILE,
        WRITE_README_RST,
    )

    with TempDir(prefix='setup-cfg-') as td:
        td.write('setup.py', SETUP_FILE)
        td.write('setup.cfg', SETUP_CFG)
        td.write('setup_commands.cfg', SETUP_COMMANDS)

# Generated at 2022-06-13 21:03:17.851416
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # pylint: disable=C0103
    from flutils.envutils import get_project_root_dir

    def get_setup_commands(config: SetupCfgCommandConfig) -> List[str]:
        out = [config.name]
        out += list(config.commands)
        return out

    count = 0
    for dir_path in (
            get_project_root_dir(),
            os.path.join(get_project_root_dir(), os.pardir),
            os.path.join(get_project_root_dir(), os.pardir, os.pardir)
    ):
        dir_path = cast(str, dir_path)
        if os.path.isdir(dir_path) is False:
            continue

# Generated at 2022-06-13 21:03:33.160607
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def each_dir() -> Generator[str, None, None]:
        for fs in extract_stack():
            fs = cast(FrameSummary, fs)
            basename = os.path.basename(fs.filename)
            if basename == 'test_setupcfg.py':
                dirname = str(os.path.dirname(fs.filename))
                dirs = list(
                    filter(
                        lambda x: os.path.isdir(x),
                        map(lambda x: os.path.join(dirname, x), ('.', '..'))
                    )
                )
                yield from dirs

    for path in each_dir():
        for config in each_sub_command_config(path):
            print('config: %s' % config)