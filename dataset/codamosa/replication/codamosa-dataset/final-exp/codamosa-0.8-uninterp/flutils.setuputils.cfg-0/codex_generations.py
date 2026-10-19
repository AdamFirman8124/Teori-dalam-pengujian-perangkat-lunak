

# Generated at 2022-06-13 20:53:56.064491
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    sys.path.insert(0, '.')
    from flutils.setup import each_sub_command_config
    for cmd in each_sub_command_config():
        print(cmd)

# Generated at 2022-06-13 20:54:05.028587
# Unit test for function each_sub_command_config
def test_each_sub_command_config():

    def print_each_sub_command_config(setup_dir: str) -> None:
        print("\n\n  With setup_dir=%r\n" % setup_dir)
        for scc in each_sub_command_config(setup_dir):
            print("   >>>> %s" % scc)
        print("\n")
        sys.stdout.flush()

    @contextmanager
    def test_dir(setup_dir: str) -> Generator[None, None, None]:
        """Creates a test directory that contains a setup.py and
        setup.cfg file, then changes to that directory.
        """

# Generated at 2022-06-13 20:54:18.593438
# Unit test for function each_sub_command_config
def test_each_sub_command_config():

    import tempfile

    with tempfile.TemporaryDirectory() as dp:
        with open(os.path.join(dp, 'setup.py'), 'w') as fp:
            fp.write('# namespace package\n')
        with open(os.path.join(dp, 'setup.cfg'), 'w') as fp:
            fp.write('[metadata]\nname=test_pkg\n')
        with open(os.path.join(dp, 'setup_commands.cfg'), 'w') as fp:
            fp.write('''[setup.command.test-cmd]
commands = echo %(name)s
''')
        gen = each_sub_command_config(dp)
        ctx = next(gen)
        assert ctx.name == 'test-cmd'

# Generated at 2022-06-13 20:54:26.653961
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.packages import create_package
    import tempfile
    import shutil
    import sys
    import importlib

    tmp_dir, pkg_name = tempfile.mkdtemp(), 'test_package'
    tmp_dir = os.path.realpath(tmp_dir)
    src_dir = os.path.join(tmp_dir, pkg_name)


# Generated at 2022-06-13 20:54:38.976923
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    class _TestConfig(NamedTuple):
        name: str
        camel: str
        description: str
        commands: Tuple[str, ...]

    test_cases: List[_TestConfig] = []

    config = _TestConfig(
        'test',
        'Test',
        '',
        (
            'echo test-command-1',
            'echo test-command-2',
        )
    )
    test_cases.append(config)

    config = _TestConfig(
        'test.sub',
        'TestSub',
        '',
        (
            'echo test-command-1',
            'echo test-command-2',
        )
    )
    test_cases.append(config)


# Generated at 2022-06-13 20:54:44.970068
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from logging import basicConfig, DEBUG, info
    import sys

    basicConfig(
        level=DEBUG,
        stream=sys.stdout,
        format='%(name)s: %(message)s'
    )

    for x in each_sub_command_config():
        info(x)

# Generated at 2022-06-13 20:54:55.650789
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config."""
    _, fn = tempfile.mkstemp(suffix='setup_commands.cfg')
    os.remove(fn)

    dirname, basename = os.path.split(fn)
    assert basename == 'setup_commands.cfg'


# Generated at 2022-06-13 20:55:04.442654
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import unittest

    class TestEachSubCommandConfig(unittest.TestCase):

        def test_each_sub_command_config(self):
            name = (
                "TestCase for "
                "flutils.setuputils.each_sub_command_config"
            )
            with tempfile.TemporaryDirectory() as tmpdir:
                meta_file = os.path.join(tmpdir, 'setup.py')
                with open(meta_file, 'w') as fout:
                    fout.write('name="%s"' % name)
                setup_cfg_file = os.path.join(tmpdir, 'setup.cfg')
                with open(setup_cfg_file, 'w') as fout:
                    fout.write('[metadata]\nname=%s' % name)


# Generated at 2022-06-13 20:55:15.605698
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    configs = tuple(each_sub_command_config())

    if len(configs) is 0:
        raise ValueError("No configs returned?")

    config = configs[0]
    if config.name != 'test_utils.test_project':
        raise RuntimeError(
            "Invalid config value for name. "
            "Expected 'test_utils.test_project', got %r."
            % config.name
        )
    if config.camel != 'TestUtilsTestProject':
        raise RuntimeError(
            "Invalid config value for camel. "
            "Expected 'TestUtilsTestProject', got %r."
            % config.camel
        )

# Generated at 2022-06-13 20:55:26.677629
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Verifies that the ``each_sub_command_config`` function works as
    expected.
    """
    import sys
    import os
    import unittest
    import tempfile

    class TestEachSubCommandConfig(unittest.TestCase):
        def setUp(self) -> None:
            self.temporary_dir = tempfile.TemporaryDirectory()

        def tearDown(self) -> None:
            self.temporary_dir.cleanup()

        def test_missing_setup_py(self):
            with self.assertRaises(FileNotFoundError):
                list(each_sub_command_config(self.temporary_dir.name))

        def test_missing_setup_cfg(self):
            setup_py_path = os.path.join(self.temporary_dir.name, 'setup.py')

# Generated at 2022-06-13 20:55:43.514761
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.testutils import (
        TEST_DATA,
        TempDir,
    )
    from flutils.shellutils import run_cmd
    from flutils.pathutils import mk_parent_dir

    with TempDir(prefix='test_setup_cfg') as tmpdir:
        path = os.path.join(tmpdir, 'setup.py')
        with open(path, 'w') as f:
            print('#!/usr/bin/env python', file=f)
        run_cmd(['chmod', '+x', path])
        path = os.path.join(tmpdir, 'setup.cfg')
        with open(path, 'w') as f:
            print("[metadata]", file=f)
            print("name = test-package", file=f)

# Generated at 2022-06-13 20:55:58.438637
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config"""
    from flutils.pfunc import (
        callable_to_function,
        cached_function_sub_call,
    )

    @cached_function_sub_call
    def each_sub_command_config_sub_call(
            setup_dir: str = None
    ) -> Generator[SetupCfgCommandConfig, None, None]:
        yield from each_sub_command_config(setup_dir)

    from flutils.testutils.pfunc import (
        check_function_sub_call_from_callable,
        check_function_sub_call_from_function,
    )


# Generated at 2022-06-13 20:56:12.102617
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from . import test_dir
    from . import test_file

    setup_dir = str(os.path.dirname(test_dir))
    setup_dir = os.path.realpath(setup_dir)
    setup_cfg_path = os.path.join(setup_dir, 'setup.cfg')
    parser = ConfigParser()
    parser.read(setup_cfg_path)
    name = _get_name(parser, setup_cfg_path)
    format_kwargs = {
        'name': name,
        'setup_dir': setup_dir,
        'home': os.path.expanduser('~')
    }
    path = os.path.join(setup_dir, 'setup.cfg')
    parser = ConfigParser()
    parser.read(path)

# Generated at 2022-06-13 20:56:18.812609
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.misctests import (
        each_sub_command_config as test_function,
        DATA_DIR,
    )
    from flutils.misctests.testapp.setup_commands import (
        each_sub_command_config as test_function_app,
    )
    from flutils.misctests.testapp.setup_commands.testapp.setup import (
        each_sub_command_config as test_function_app_testapp,
    )
    from flutils.misctests.testapp.setup_commands import (
        each_sub_command_config as test_function_app_setup_commands,
    )
    # These tests are commented out since they are failing in the current
    # implementation. When I figure out how to get the files found in
    # the ``flutils.

# Generated at 2022-06-13 20:56:27.563679
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import pytest
    from flutils.configutils import ConfigParser, each_sub_command_config

    data = '''[metadata]
name = test

[setup.command.test]
commands =
    echo "Test"
'''
    with pytest.raises(FileNotFoundError):
        each_sub_command_config('./test/file/does/not/exist')

    with tempfile.TemporaryDirectory() as td:
        path = os.path.join(td, 'setup.cfg')
        parser = ConfigParser()
        parser.read_string(data)
        parser.write(path)

        test = each_sub_command_config(td)

# Generated at 2022-06-13 20:56:37.780639
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    pkg_dir = os.path.abspath(os.path.dirname(__file__))
    pkg_dir = os.path.join(pkg_dir, '..')

    setup_dir = os.path.join(pkg_dir, 'setup_files', 'good')

# Generated at 2022-06-13 20:56:50.323350
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    this_module = sys.modules[__name__]
    this_file = os.path.realpath(this_module.__file__)
    setup_dir = os.path.realpath(os.path.join(
        os.path.dirname(this_file),
        '..',
    ))

    for out in each_sub_command_config(setup_dir):
        if out.name == 'install_sub.sub-sub':
            assert 'sub.sub-sub' == out.camel
            assert 'sub-sub install' == out.description

# Generated at 2022-06-13 20:56:52.320653
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def t():
        for conf in each_sub_command_config():
            print(conf)
    t()

# Generated at 2022-06-13 20:57:03.977669
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from os.path import join, dirname
    from flutils.pathutils import temp_dir
    from flutils.sysutils import create_file, save_file_text
    from tempfile import NamedTemporaryFile
    from textwrap import dedent

    with temp_dir() as td:
        path = join(td, 'setup.py')
        create_file(path)
        path = join(td, 'setup.cfg')
        with NamedTemporaryFile('w', dir=dirname(path), delete=False) as f:
            f.write(dedent("""
                [metadata]
                name = project
                """))
        _path = join(td, 'setup_commands.cfg')

# Generated at 2022-06-13 20:57:11.617830
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import unittest

    class EachSubCommandConfigTest(unittest.TestCase):
        def setUp(self):
            self.tmpdir = tempfile.TemporaryDirectory()
            self.addCleanup(self.tmpdir.cleanup)

            self.setup_cfg_path = os.path.join(self.tmpdir.name, 'setup.cfg')
            self.setup_py_path = os.path.join(self.tmpdir.name, 'setup.py')
            self.setup_commands_cfg_path = os.path.join(
                self.tmpdir.name, 'setup_commands.cfg'
            )

            with open(self.setup_cfg_path, 'w') as f:
                f.write(SETUP_CFG_FILE)


# Generated at 2022-06-13 20:57:29.667544
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import io
    import tempfile

    from flutils.subproc import run_subproc
    from flutils.files import each_file_line

    stdout = sys.stdout

# Generated at 2022-06-13 20:57:33.944532
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from . import _tempdir
    with _tempdir() as d:
        print("Test temp dir:", d)
        for sec in each_sub_command_config(d):
            print("    -", sec)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:57:44.005564
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import temp_dir
    from flutils.strings import secure_filename

    def _test_command(
            scfg: SetupCfgCommandConfig,
            name: str,
            description: str,
            commands: Tuple[str, ...],
            opath: Optional[str] = None
    ) -> None:
        assert scfg.name == name
        assert scfg.description == description
        assert scfg.commands == commands
        assert scfg.camel == secure_filename(
            ''.join(name.split('.')[1:]),
            include_symbols=False,
            replace_space='_'
        ).upper()
        if opath:
            assert os.path.isfile(opath) is False


# Generated at 2022-06-13 20:57:52.840088
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import re
    setup_dir = os.path.dirname(os.path.abspath(__file__))
    for sub_cmd in each_sub_command_config(setup_dir):
        assert re.search(
            r'^test_project\.((test|test_)plugin_\d+)\.[a-zA-Z0-9_-]+$',
            sub_cmd.name
        )
        if sys.version_info >= (3, 7):
            assert sub_cmd.camel
            assert sub_cmd.description
            assert isinstance(sub_cmd.commands, tuple)
            assert sub_cmd.commands


# Generated at 2022-06-13 20:58:04.991671
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for the module function each_sub_command_config."""
    # pylint: disable=R0201,W0613
    import sys
    import os
    import datetime as dt
    from pathlib import Path

    from flutils.logutils import logged_class

    import flutils.packutils as pu
    from flutils.sysutils import (
        is_main,
        is_ci_env,
        get_python_interpreter,
    )
    from flutils.timeutils import (
        now_tz_aware,
        get_utc_offset,
        get_tz_str,
    )
    from flutils.strutils import (
        camel_to_underscore,
        underscore_to_camel,
        underscore_to_title,
    )


# Generated at 2022-06-13 20:58:13.578602
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from unittest.mock import patch

    with patch('sys.argv', ['setup.py']):
        with patch('flutils.setup_utils.each_sub_command_config') as mock:
            from flutils.setup_utils import each_sub_command_config as func

            _ = func()
            mock.assert_called()

    with patch('sys.argv', ['setup.py', '--help']):
        with patch('flutils.setup_utils.each_sub_command_config') as mock:
            from flutils.setup_utils import each_sub_command_config as func

            _ = func()
            mock.assert_called()

# Generated at 2022-06-13 20:58:18.174017
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for cmd in each_sub_command_config():
        print(cmd)

if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:58:22.680576
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config(os.path.expanduser('~/dev/flutils')):
        print(config)
    assert True


# Generated at 2022-06-13 20:58:34.408548
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    cmd_configs = list(each_sub_command_config())
    assert len(cmd_configs) == 15
    assert cmd_configs[0] == SetupCfgCommandConfig(
        'test', 'Test', 'Runs the package tests.',
        ('flit install', 'pytest -v --cov=flutils')
    )
    assert cmd_configs[1] == SetupCfgCommandConfig(
        'docs.build', 'DocsBuild', 'Builds the project Sphinx documentation.',
        ('make docs',)
    )
    assert cmd_configs[2] == SetupCfgCommandConfig(
        'docs.serve', 'DocsServe', 'Serves the project documentation.',
        ('make docs.serve',)
    )
    assert cmd_configs[3] == SetupCfgCommand

# Generated at 2022-06-13 20:58:44.984831
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    test_dir = os.path.join(dir_path, 'data', 'setup_dir')
    assert os.path.isdir(test_dir)
    for item in each_sub_command_config(test_dir):
        assert isinstance(item, SetupCfgCommandConfig)
        assert isinstance(item.name, str)
        assert isinstance(item.camel, str)
        assert isinstance(item.description, str)
        assert isinstance(item.commands, tuple)
        assert all(isinstance(x, str) for x in item.commands)

# Generated at 2022-06-13 20:59:08.820017
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from click.testing import CliRunner
    import toml
    from flutils.configutils import (
        _ensure_dirs_and_files,
        _should_create_missing_configs,
    )
    from flutils.logutils import (
        CustomLogConfig,
        CustomLogger,
        _set_log_level_format,
    )
    from flutils.sysutils import (
        _is_wsl,
        _set_windows_env_vars,
    )
    from flutils.testutils import (
        _wsl_test_path,
        _windows_test_path,
    )
    from flutils.testutils import (
        _wsl_test_path,
        _windows_test_path,
    )

# Generated at 2022-06-13 20:59:17.157973
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # noinspection PyUnresolvedReferences
    from os import remove
    # noinspection PyUnresolvedReferences
    from os.path import exists, join
    # noinspection PyUnresolvedReferences
    from tempfile import mkdtemp
    import shutil

    test_dir = mkdtemp()

# Generated at 2022-06-13 20:59:29.119065
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config"""
    # invalid setup dir
    with pytest.raises(AssertionError):
        next(each_sub_command_config(''))

    # find_packages
    setup_dir = os.path.join(
        os.path.dirname(__file__), '..', '..', '..', 'tests', 'data'
    )
    next(each_sub_command_config(setup_dir))
    setup_cfg = os.path.join(setup_dir, 'setup.cfg')
    parser = ConfigParser()
    parser.read(setup_cfg)
    name = _get_name(parser, setup_cfg)
    setup_commands_cfg = os.path.join(setup_dir, 'setup_commands.cfg')
    parser = ConfigParser

# Generated at 2022-06-13 20:59:32.074081
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # type: () -> None
    """Unit test for function each_sub_command_config."""
    for cfg in each_sub_command_config():
        print(cfg)


if __name__ == "__main__":
    test_each_sub_command_config()

# Generated at 2022-06-13 20:59:42.976504
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.dirname(path)
    path = os.path.dirname(path)
    path = os.path.join(path, 'tests')
    path = os.path.join(path, 'data')

    test_paths = (
        os.path.join(path, 'setup_cmd'),
        os.path.join(path, 'setup_cmd_2'),
        os.path.join(path, 'setup_cmd_3'),
    )
    for i, setup_path in enumerate(test_paths):
        commands = tuple(each_sub_command_config(setup_path))

# Generated at 2022-06-13 20:59:47.409248
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    configs = list(each_sub_command_config())
    assert configs
    for config in configs:
        assert isinstance(config.name, str)
        assert isinstance(config.camel, str)
        assert isinstance(config.description, str)
        assert isinstance(config.commands, tuple)

# Generated at 2022-06-13 20:59:52.253833
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for sub_command_config in each_sub_command_config():
        assert sub_command_config.name
        assert sub_command_config.camel
        assert sub_command_config.description
        assert sub_command_config.commands



# Generated at 2022-06-13 21:00:03.037113
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import unittest


# Generated at 2022-06-13 21:00:15.582053
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import get_proj_dir
    from os.path import join as pjoin
    from pprint import pprint
    from configparser import ConfigParser

    proj_dir = get_proj_dir(__file__)
    if proj_dir is None:
        raise FileNotFoundError(
            "Unable to find the project directory. The returned value "
            "was %r." % proj_dir
        )
    setup_cfg_path = pjoin(proj_dir, 'setup.cfg')
    parser = ConfigParser()
    parser.read(setup_cfg_path)
    name = _get_name(parser, setup_cfg_path)
    assert name == 'flutils'

# Generated at 2022-06-13 21:00:26.391516
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    function_name = 'each_sub_command_config'
    docstring = globals()[function_name].__doc__
    assert docstring is not None

    # Test with the ``setup_dir`` argument NOT given.
    for sub_command in each_sub_command_config():
        assert sub_command


if __name__ == '__main__':
    """Run the unit tests for this module."""
    # Ensure the file is ran as a script.
    assert __package__ is None
    # Remove the directory of this file from the module search path.
    sys.path.pop(0)
    # Import the module to test.
    import setup_commands
    # Run the module's unit tests.
    setup_commands.test_all()

# Generated at 2022-06-13 21:00:58.823447
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import textwrap

# Generated at 2022-06-13 21:01:00.121816
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 21:01:12.693683
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from inspect import getfile
    from os import getcwd
    from os.path import dirname, join
    from unittest import TestCase
    from unittest.mock import patch

    from flutils.configutils import each_sub_command_config

    class Test_each_sub_command_config(TestCase):

        test_dir = dirname(getfile(lambda: None))
        # NOTE: Each test will be run in a different directory, therefore
        # no hardcoding of the relative paths.
        here = getcwd()

        def setUp(self):
            self.maxDiff = None
            self.res: List[SetupCfgCommandConfig] = []

        def tearDown(self):
            for item in self.res:
                print(item)
            self.res.clear()


# Generated at 2022-06-13 21:01:22.028917
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    here = os.path.abspath(os.path.dirname(__file__))

# Generated at 2022-06-13 21:01:34.118690
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    generators = []
    generators.append(each_sub_command_config())
    generators.append(each_sub_command_config(os.path.expanduser('~')))
    generators.append(each_sub_command_config(
        os.path.expanduser('~/Documents/GitHub')
    ))
    generators.append(each_sub_command_config(
        os.path.expanduser('~/Documents/GitHub/test_cl_commands')
    ))
    generators.append(each_sub_command_config(
        os.path.expanduser('~/Documents/GitHub/test_cl_commands/src')
    ))
    for gen in generators:
        cnt = 0
        for i in gen:
            cnt += 1
        assert cnt > 0

# Generated at 2022-06-13 21:01:47.896081
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    results = {sc.camel: sc.commands for sc in each_sub_command_config()}

# Generated at 2022-06-13 21:01:56.469873
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from types import FrameType

    class Frame(FrameType):
        pass
    fs = Frame(
        f_code=FrameType.f_code(each_sub_command_config),
        f_globals=FrameType.f_globals(each_sub_command_config),
        f_locals=FrameType.f_locals(each_sub_command_config),
        f_back=None
    )
    return each_sub_command_config(setup_dir=os.path.dirname(fs.f_code.co_filename))

# Generated at 2022-06-13 21:02:08.904335
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import os.path
    import shutil

    setup_cfg = """
[global]
quiet = 1

[metadata]
name = flutils

[files]
packages =
    flutils

[bdist_wheel]
universal = 1

[setup.commands]
description = Setup commands.

[setup.command.develop]
description = Install the project in 'development mode.'
commands =
    python setup.py develop
"""


# Generated at 2022-06-13 21:02:22.731527
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.testingutils import TempFileFactory


# Generated at 2022-06-13 21:02:35.667596
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Tests the function ``each_sub_command_config``."""
    pkg_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    assert 'tests' in pkg_dir
    pkg_dir = os.path.dirname(pkg_dir)
    assert 'flutils' in pkg_dir
    pkg_name = os.path.basename(pkg_dir)
    assert pkg_name == 'flutils'
    setup_dir = os.path.join(pkg_dir, 'tests', 'fixtures', 'setup')
    for item in each_sub_command_config(setup_dir):
        assert type(item) == SetupCfgCommandConfig

# Generated at 2022-06-13 21:02:53.424276
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import pathlib
    from typing import (
        Dict,
        Generator,
        List,
        Tuple,
    )

    from flutils.testutils import (
        compare_reprs,
        compares_equal,
    )

    def test_func(
            setup_dir: Optional[Union[pathlib.Path, str]] = None
    ) -> Generator[SetupCfgCommandConfig, None, None]:
        return each_sub_command_config(setup_dir)

    # each_sub_command_config()
    start_dir = pathlib.Path(__file__).parent.parent
    setup_dir = start_dir.joinpath('project_setup.cfg')
    out = list(test_func(setup_dir))
    # Ensure the .joinpath() dirs can be used as well
   

# Generated at 2022-06-13 21:03:04.282884
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config(os.path.abspath('.')):
        print('name', config.name)
        print('camel', config.camel)
        print('description', config.description)
        print('commands', config.commands)
        print('{')
        print('    name:', repr(config.name))
        print('    camel:', repr(config.camel))
        print('    description:', repr(config.description))
        print('    commands:', repr(config.commands))
        print('},')
test_each_sub_command_config()

# Generated at 2022-06-13 21:03:14.012237
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    with tempfile.TemporaryDirectory() as tmpdirname:
        setup_cfg_file = os.path.join(tmpdirname, 'setup.cfg')
        setup_commands_cfg_file = os.path.join(tmpdirname, 'setup_commands.cfg')
        with open(setup_cfg_file, 'w') as fp:
            fp.write(
                '[metadata]\n'
                'name = myproj\n'
            )

# Generated at 2022-06-13 21:03:18.193756
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for scfg in each_sub_command_config('/path/to/setup_dir'):
        assert scfg.name == 'cmd'
        assert scfg.commands[0] == 'echo "Do something very cool!"'



# Generated at 2022-06-13 21:03:34.337281
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    import operator
    import functools
    import tempfile
    import shutil

    setup_items = [
        ('setup.command.name', 'my_name'),
        ('setup.command.description', 'Describes my command.'),
        ('setup.command.command', 'echo "I am a command";'),
    ]
    extra_setup_items = [
        ('setup.command.extra.name', 'my_extra'),
        ('setup.command.extra.description', 'Describes my extra command.'),
        ('setup.command.extra.commands', '''
        echo "I am the first command";
        echo "I am the second command";
        '''),
    ]
