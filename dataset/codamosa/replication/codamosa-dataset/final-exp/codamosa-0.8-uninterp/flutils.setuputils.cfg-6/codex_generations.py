

# Generated at 2022-06-13 20:54:03.706007
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from pytest import raises

    def test(setup_dir: str) -> None:
        for i in each_sub_command_config(setup_dir):
            # print(i)
            assert isinstance(i.name, str)
            assert isinstance(i.camel, str)
            assert isinstance(i.description, str)
            assert isinstance(i.commands, tuple)
            for j in i.commands:
                assert isinstance(j, str)

    test('./flutils/setup_cfg')
    with raises(FileNotFoundError):
        test('examples')
    with raises(FileNotFoundError):
        test('/tmp/dummypath')
    with raises(FileNotFoundError):
        test()



# Generated at 2022-06-13 20:54:08.644669
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_config_directory = os.path.join(
        os.path.dirname(__file__), 'setup_config'
    )
    assert len(list(each_sub_command_config(setup_config_directory))) == 6

# Generated at 2022-06-13 20:54:22.219157
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Test for flutils.setuputils.each_sub_command_config"""

    from flutils.setuputils import each_sub_command_config as esc

    def _each_setup_cfg_command_config(
            setup_dir: Optional[str] = None
    ) -> Generator[Tuple[str, str, Tuple[str, ...]], None, None]:
        for config in esc(setup_dir):
            yield config.name, config.camel, config.commands

    out = list(_each_setup_cfg_command_config('tests/setup_test_proj'))

# Generated at 2022-06-13 20:54:27.740440
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config."""
    import unittest

    class TestSubCommandConfig(unittest.TestCase):

        def test_sub_command_config(self):
            import tempfile
            import os

            with tempfile.TemporaryDirectory() as tmpdirname:
                setup_dir = os.path.abspath(tmpdirname)
                with open(os.path.join(setup_dir, 'setup.py'), 'w') as f:
                    f.write("""
# -*- coding: utf-8 -*-

import os

from setuptools import setup

setup()
""")

# Generated at 2022-06-13 20:54:39.370771
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # pylint: disable=R0204
    gen = each_sub_command_config(os.path.dirname(__file__))
    result = list(gen)
    assert result is not None
    assert len(result) == 4
    assert result[0].name == 'setuptools.command.build_py'
    assert result[0].description == 'Build the project.'
    assert len(result[0].commands) == 1
    assert result[0].commands[0] == 'python setup.py build'

    assert result[1].name == 'setuptools.command.install'
    assert result[1].description == 'Install the project.'
    assert len(result[1].commands) == 1
    assert result[1].commands[0] == 'python setup.py install'


# Generated at 2022-06-13 20:54:42.215831
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config():
        print(config)



# Generated at 2022-06-13 20:54:45.289717
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config():
        assert config.name is not None
        assert config.camel is not None
        assert config.description is not None
        assert len(config.commands) > 0

# Generated at 2022-06-13 20:54:51.854804
# Unit test for function each_sub_command_config
def test_each_sub_command_config():  # noqa: D103
    result: List[SetupCfgCommandConfig] = list(each_sub_command_config())
    assert len(result) == 2
    assert result[0].name == 'sdist'
    assert result[0].commands == ('python setup.py sdist',)
    assert result[1].name == 'test.run.tox'
    assert result[1].commands == ('tox',)

# Generated at 2022-06-13 20:55:02.789007
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from contextlib import redirect_stderr, redirect_stdout
    from io import StringIO
    import pickle
    import json
    import sys

    with open(os.path.join(os.path.dirname(__file__), 'setup_cfg.pkl'),
              'rb') as fh:
        try:
            expected = pickle.load(fh)
        except ModuleNotFoundError:
            expected = json.load(fh)

    with open(os.path.join(os.path.dirname(__file__), 'setup.cfg'),
              'rb') as fh:
        try:
            setup_cfg = pickle.load(fh)
        except ModuleNotFoundError:
            setup_cfg = json.load(fh)


# Generated at 2022-06-13 20:55:07.210681
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.project.setuputils import each_sub_command_config
    for cfg in each_sub_command_config():
        print('{cfg.name} = {cfg.camel}'.format(cfg=cfg))



# Generated at 2022-06-13 20:55:25.645364
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    lst = list(each_sub_command_config('temp/test/test_setup_commands/test_project'))
    assert lst
    assert cast(SetupCfgCommandConfig, lst[0]).camel == 'BuildDocs'
    assert cast(SetupCfgCommandConfig, lst[1]).camel == 'Check'
    assert cast(SetupCfgCommandConfig, lst[2]).camel == 'Coverage'
    assert cast(SetupCfgCommandConfig, lst[3]).camel == 'Fail'
    assert cast(SetupCfgCommandConfig, lst[4]).camel == 'Install'
    assert cast(SetupCfgCommandConfig, lst[5]).camel == 'StartCoverage'
    assert cast(SetupCfgCommandConfig, lst[6]).camel == 'StopCoverage'

# Generated at 2022-06-13 20:55:34.957349
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from os.path import dirname
    from sys import path
    from typing import Tuple
    from configparser import ConfigParser

    def _test_commands(commands: Tuple[str, ...]):
        for command in commands:
            assert command.startswith('py .') is True

    path.insert(0, dirname(__file__))
    parser = ConfigParser()
    parser.read('setup_commands.cfg')
    format_kwargs = {
        'name': 'test_sub_command',
        'setup_dir': dirname(__file__),
        'home': os.path.expanduser('~')
    }

# Generated at 2022-06-13 20:55:37.924577
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config():
        print(config)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:55:48.134286
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    print(
        'Running function "%s"...'
        % test_each_sub_command_config.__name__
    )

    import flutils.setuputils as utils

    test = os.path.realpath(
        os.path.join(os.path.dirname(__file__), 'test_utils')
    )
    os.chdir(test)

    for cfg in utils.each_sub_command_config(test):
        print(cfg)

    os.chdir(os.path.dirname(test))
    print()



# Generated at 2022-06-13 20:56:01.116011
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import re

    base = os.path.join(tempfile.gettempdir(), 'setup_cfg_test')
    os.makedirs(base)
    setup_cfg = os.path.join(base, 'setup.cfg')
    setup_commands = os.path.join(base, 'setup_commands.cfg')
    with open(setup_cfg, 'w') as f:
        print(
            '[metadata]',
            'name = test-package',
            file=f
        )

# Generated at 2022-06-13 20:56:12.456580
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys

    from flutils.pyutils import get_func_name

    setup_dir = os.path.dirname(sys.executable)
    setup_dir = os.path.dirname(setup_dir)
    setup_dir = os.path.join(setup_dir, 'setup')
    print('\n%s' % get_func_name())
    for x in each_sub_command_config(setup_dir):
        print(f'{x.name}: {x.description}')
        print('-' * len(x.name))
        for y in x.commands:
            print(y)
        print()


if __name__ == "__main__":
    test_each_sub_command_config()

# Generated at 2022-06-13 20:56:13.680461
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for cfg in each_sub_command_config('./helpers/data'):
        print(cfg)



# Generated at 2022-06-13 20:56:18.296030
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    print('Test the function each_sub_command_config.')
    print()
    for config in each_sub_command_config():
        print(config)
        print()


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:56:27.352039
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os

    setup_cfg_path = os.path.join(
        os.path.dirname(__file__),
        '..', '..', 'tests', 'setup.cfg',
    )
    setup_dir = os.path.realpath(os.path.dirname(setup_cfg_path))
    parser = ConfigParser()
    parser.read(setup_cfg_path)
    format_kwargs = {
        'setup_dir': setup_dir,
        'name': _get_name(parser, setup_cfg_path),
        'home': os.path.expanduser('~')
    }
    for config in _each_setup_cfg_command(parser, format_kwargs):
        assert config.name
        assert config.camel
        assert config.description
        assert config.commands



# Generated at 2022-06-13 20:56:37.779342
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import logging
    import os
    import shutil
    import tempfile
    import time

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    def _create_setup_cfg(setup_dir):
        with open(os.path.join(setup_dir, 'setup.py'), 'w'):
            pass
        _cfg = ConfigParser()
        _cfg.add_section('metadata')
        _cfg['metadata']['name'] = 'test'
        with open(os.path.join(setup_dir, 'setup.cfg'), 'w') as _fh:
            _cfg.write(_fh)


# Generated at 2022-06-13 20:56:47.980418
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.objutils import pretty_format_object

    for scc in each_sub_command_config():
        print(pretty_format_object(scc))
    print()

    for scc in each_sub_command_config(setup_dir='/path/to/proj'):
        print(pretty_format_object(scc))

# Generated at 2022-06-13 20:57:00.144807
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from pprint import pprint
    from shutil import (
        rmtree,
        copytree,
    )
    from tempfile import mkdtemp

    from flutils.fileutils import (
        get_file_contents,
        write_file_contents,
    )

    def _setup_dir(
            setup_cfg: str = '',
            setup_commands_cfg: str = '',
            test_setup_cfg_data: List[Tuple[str, str]] = None
    ):
        tmpdir = mkdtemp()
        cfg_path = os.path.join(tmpdir, 'setup.cfg')
        setup_cfg_data = get_file_contents(cfg_path)

# Generated at 2022-06-13 20:57:09.621124
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import pathlib
    from flutils.testhelpers import mk_temp_dir

    setup_dir = str(pathlib.Path(__file__).parent.parent)

# Generated at 2022-06-13 20:57:23.793278
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def _test_each_sub_command_config() -> None:
        for cmd in each_sub_command_config():
            print(cmd)

    test_folder = os.path.join(
        os.path.dirname(__file__),
        '..',
        'test',
        'data',
        'test_setup_cmd_config',
        'project_a'
    )
    _test_each_sub_command_config()


# def each_sub_command_config(
#         parser: ConfigParser,
#         setup_dir: Optional[Union[os.PathLike, str]] = None
# ) -> Generator[SetupCfgCommandConfig, None, None]:
#     setup_dir = setup_dir or str(os.path.dirname(__file__))
#     setup_dir = os.path

# Generated at 2022-06-13 20:57:34.320120
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import flutils.tests.resources.setupcfg

    setup_cfg_path = os.path.join(
        flutils.tests.resources.setupcfg.__path__[0],
        'setup.cfg'
    )
    setup_commands_cfg_path = os.path.join(
        flutils.tests.resources.setupcfg.__path__[0],
        'setup_commands.cfg'
    )

    parser = ConfigParser()
    parser.read(setup_cfg_path)
    name = _get_name(parser, setup_cfg_path)

    parser = ConfigParser()
    parser.read(setup_commands_cfg_path)
    format_kwargs = {'name': name}

# Generated at 2022-06-13 20:57:44.173124
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from itertools import islice
    from flutils.miscutils import ensure_generator_state

    setup_dir = os.path.realpath(os.path.dirname(__file__))
    setup_dir = os.path.join(setup_dir, 'example_project')

    def no_gen():
        return each_sub_command_config(setup_dir)

    def gen0():
        return each_sub_command_config(setup_dir)

    def gen1():
        yield from gen0()

    def gen2():
        yield from gen1()

    def gen3():
        yield from gen2()

    def gen4():
        yield from gen3()

    def no_gen2():
        return gen1()

    def gen5():
        return gen1()

    def gen6():
        yield

# Generated at 2022-06-13 20:57:49.425712
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    results = list(each_sub_command_config())
    for result in results:
        print(result)
    assert len(results)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:57:50.995906
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for cfg in each_sub_command_config():
        assert cfg is not None

# Generated at 2022-06-13 20:58:02.406552
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import unittest.mock as mock


# Generated at 2022-06-13 20:58:13.716824
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import unittest
    import tempfile
    import shutil

    class TestSetupCfgFunctions(unittest.TestCase):

        def setUp(self):
            self.dir = tempfile.mkdtemp()
            self.setup_dir = os.path.join(self.dir, 'setup_dir')
            os.mkdir(self.setup_dir)
            with open(os.path.join(self.setup_dir, 'setup.py'), 'w')as setup:
                setup.write('"""Test setup file."""\n')

# Generated at 2022-06-13 20:58:27.676731
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for cmd in each_sub_command_config(os.path.dirname(__file__)):
        assert isinstance(cmd.name, str)
        assert isinstance(cmd.camel, str)
        assert isinstance(cmd.description, str)
        assert isinstance(cmd.commands, tuple)
        for command in cmd.commands:
            assert isinstance(command, str)



# Generated at 2022-06-13 20:58:38.229241
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import each_dir_chain
    cwd = os.getcwd()
    for path in each_dir_chain(cwd, 'setup_commands.cfg'):
        setup_dir = os.path.dirname(path)
        break
    else:
        raise RuntimeError("Unable to find any setup_commands.cfg files.")
    for config in each_sub_command_config(setup_dir):
        print(config)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:58:45.740757
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config."""

    # The commands are used to test the creation of the commands
    # using the given setup.cfg file.
    commands = [
        '-c',
        '"echo \'test\'"',
        '"echo \'test\'"',
        '-c',
        '"echo \'test\'"',
        '"echo \'test\'"',
        '-c',
        '"echo \'test\'"',
        '"echo \'test\'"',
    ]

    # Get where this test file is located
    setup_dir = os.path.dirname(os.path.realpath(__file__))

    # Read the setup.cfg file in the setup directory
    parser = ConfigParser()

# Generated at 2022-06-13 20:58:51.823222
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config('.'):
        assert isinstance(config, SetupCfgCommandConfig)
        assert isinstance(config.name, str)
        assert isinstance(config.camel, str)
        assert isinstance(config.description, str)
        assert isinstance(config.commands, tuple)

# Generated at 2022-06-13 20:59:03.361854
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for sub_cmd_cfg in each_sub_command_config():
        assert isinstance(sub_cmd_cfg, SetupCfgCommandConfig)
        assert isinstance(sub_cmd_cfg.name, str)
        assert isinstance(sub_cmd_cfg.camel, str)
        assert isinstance(sub_cmd_cfg.description, str)
        assert isinstance(sub_cmd_cfg.commands, tuple)
        for command in sub_cmd_cfg.commands:
            assert isinstance(command, str)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:59:14.796020
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_commands_path = os.path.realpath(__file__)
    while os.path.isdir(setup_commands_path) is False:
        setup_commands_path = os.path.dirname(setup_commands_path)
    setup_commands_path = os.path.join(setup_commands_path, 'setup_commands.cfg')
    if os.path.isfile(setup_commands_path) is False:
        raise FileNotFoundError(
            "Unable to find the 'setup_commands.cfg' file."
        )
    setup_dir = os.path.dirname(setup_commands_path)
    for config in each_sub_command_config(setup_dir):
        print(config)


if __name__ == '__main__':
    test

# Generated at 2022-06-13 20:59:26.931243
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.configutils.checkconfig import check_config
    from flutils.configutils.configs import FlaskConfig
    from flutils.configutils.loaders import setup_cfg_loader
    from pathlib import Path
    import pytest

    # This following import command is required to get pytest to actually
    # execute the function test code.
    import sys

    # The following optional import allows us to use the 'pytest.raises'
    # function in Python 2.
    import builtins
    try:
        builtins.BaseException
    except AttributeError:
        builtins.BaseException = Exception

    cwd = Path().cwd()
    path = cwd.joinpath('test_flutils', 'test_configutils')


# Generated at 2022-06-13 20:59:39.846095
# Unit test for function each_sub_command_config

# Generated at 2022-06-13 20:59:50.357661
# Unit test for function each_sub_command_config

# Generated at 2022-06-13 21:00:01.780749
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from .test_setup_cfg_parser import prep_test_files
    from shutil import rmtree
    from unittest import TestCase

    class TestEachSubCommandConfig(TestCase):
        def setUp(self):
            self.setup_dir = prep_test_files()
            self.teardown = False
            self.commands = tuple(
                each_sub_command_config(self.setup_dir)
            )

        def tearDown(self):
            if self.teardown and self.setup_dir:
                rmtree(self.setup_dir)

        def runTest(self):
            self.assertEqual(len(self.commands), 2)

# Generated at 2022-06-13 21:00:23.638392
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from sys import modules
    from pkgutil import walk_packages

    def is_package(module):
        """Checks if the given module is a package."""
        try:
            return module.__file__.endswith('.py') is False
        except AttributeError:
            return False

    def is_top_level(module):
        """Checks if the given module is located in the top level."""
        try:
            return module.__name__.count('.') == 0
        except AttributeError:
            return False

    def each_sub_package(
            package_name: str
    ) -> Generator[Tuple[str, ModuleType], None, None]:
        """Finds each sub-package in the given package."""

# Generated at 2022-06-13 21:00:30.829390
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import expand

    for config in each_sub_command_config(expand('t.flutils.test_configutils')):
        assert isinstance(config, SetupCfgCommandConfig)
        assert config.name or config.camel or config.description or config.commands


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:00:40.832093
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def _make_result(setup_dir: Optional[Union[os.PathLike, str]] = None):
        if setup_dir is None:
            setup_dir = os.path.abspath(os.path.dirname(__file__))
        return next(each_sub_command_config(setup_dir))

    assert _make_result().name == 'test'
    assert _make_result().camel == 'Test'
    assert _make_result().description == 'A very simple command.'
    assert _make_result().commands == ('echo "test"',)

# Generated at 2022-06-13 21:00:49.532063
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    test_dir = os.path.join(os.path.abspath(__file__), '..', '..', '..', '..')
    for config in each_sub_command_config(test_dir):
        assert isinstance(config, SetupCfgCommandConfig)
        assert isinstance(config.name, str)
        assert isinstance(config.camel, str)
        assert isinstance(config.description, str)
        assert isinstance(config.commands, tuple)
        for cmd in config.commands:
            assert isinstance(cmd, str)

# Generated at 2022-06-13 21:01:01.977188
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from inspect import getfile
    from os import path

    # Obtain the directory that contains this file.
    pkg_dir = path.dirname(path.abspath(getfile(test_each_sub_command_config)))

    # Traverse to the desired test directory
    test_dir = path.join(pkg_dir, 'tests', 'data', 'test_package')

    # Test
    out: List[SetupCfgCommandConfig] = list(each_sub_command_config(test_dir))
    assert len(out) == 1
    assert out[0].name == 'foo'
    assert out[0].camel == 'Foo'
    assert out[0].description == 'This is the Foo command.'

# Generated at 2022-06-13 21:01:13.073139
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import io
    import unittest
    TEST_CONFIG = """\
    [metadata]
    name = test-package

    [setup.command.test]
    name = test-1
    description = This is test 1.
    commands =
        ls -l
        echo $HOME
    [setup.command.test.2]
    name = test-2
    description = This is test 2.
    commands = echo $SETUP_DIR

    [setup.command.test.3]
    name = test-2
    description = echo $NAME
    command = echo $NAME
    [setup.command.test.4]
    name = test-3
    description = |
        This is test 3.
    commands =
        echo line 1
        echo line 2
    """

# Generated at 2022-06-13 21:01:22.196079
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from collections import OrderedDict
    from importlib import import_module
    from inspect import isgenerator
    from os import path
    from textwrap import dedent
    from unittest import TestCase

    from flutils.setuputils import each_sub_command_config

    this_dir = path.dirname(path.abspath(__file__))
    root_dir = path.dirname(this_dir)
    tester_dir = path.join(this_dir, 'data_sub_command_config')

    class TestEachSubCommandConfig(TestCase):

        def test_00(self):
            """verify function returns a generator"""
            out = each_sub_command_config(setup_dir=tester_dir)
            self.assertTrue(isgenerator(out))

# Generated at 2022-06-13 21:01:35.455044
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.setuputil import each_sub_command_config
    from flutils.testutils import make_test_dir
    from flutils.timeutils import Timer
    import shutil
    import tempfile

    temp_dir = tempfile.mkdtemp()
    setup_cfg = os.path.join(temp_dir, 'setup.cfg')
    setup_commands_cfg = os.path.join(temp_dir, 'setup_commands.cfg')
    setup_commands_py = os.path.join(temp_dir, 'setup_commands.py')

# Generated at 2022-06-13 21:01:40.588815
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    cfg = None
    for cfg in each_sub_command_config(os.path.join(
        os.path.dirname(__file__), '..'
    )):
        pass
    assert cfg is not None
    assert cfg.camel == 'SharedVars'

# Generated at 2022-06-13 21:01:53.963190
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import inspect
    import tempfile
    from io import StringIO

    setup_dir = os.path.dirname(inspect.getfile(each_sub_command_config))
    setup_dir = os.path.realpath(os.path.join(setup_dir, '..'))

    f = StringIO()
    f.write('[metadata]\n')
    f.write('name = flutils\n')
    f.write('[setup.command.foo]\n')
    f.write('description = Does stuff\n')
    f.write('command = echo foo\n')
    f.seek(0)

    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'setup.cfg')

# Generated at 2022-06-13 21:02:39.757000
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    pass



# Generated at 2022-06-13 21:02:46.525428
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import pathlib
    import pprint
    import sys

    setup_dir = str(pathlib.Path(__file__).parent.parent)
    print(setup_dir)
    print()
    for config in each_sub_command_config(setup_dir):
        print(config)
        print()
    print()
    for config in each_sub_command_config():
        print(config)
        print()
    print()
    for config in each_sub_command_config(sys.path[0]):
        print(config)
        print()

# Generated at 2022-06-13 21:02:56.808884
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.funcutils import get_func_name
    from flutils.sysutils import get_test_file_path

    def test_func():
        path = get_test_file_path('test_cmd_gen')
        for cmd_cfg in each_sub_command_config(setup_dir=path):
            assert cmd_cfg.camel == 'TestSubCommand'
            assert cmd_cfg.name == 'test.cmd.gen'
            assert cmd_cfg.description == ''
            assert cmd_cfg.commands == ('echo "hello"',)

    func_name = get_func_name(test_func)
    try:
        test_func()
    except Exception:
        import traceback
        msg = traceback.format_exc()

# Generated at 2022-06-13 21:03:10.093432
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from tests.fixtures.setup_commands import path
    import tempfile

    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = os.path.join(tmp_dir, 'setup_commands.cfg')
        with open(tmp_path, 'w') as fp:
            fp.write('''
[metadata]
name = {name}

[setup.command.pbr-test]
commands =
    echo hello world
''')
        with open(os.path.join(tmp_dir, 'setup.py'), 'w') as fp:
            fp.write("pass\n")

# Generated at 2022-06-13 21:03:18.841248
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config."""
    setup_dir = os.path.dirname(__file__)
    for config in each_sub_command_config(setup_dir):
        assert config.name == 'test'
        assert config.camel == 'Test'
        assert config.description == 'Run unit tests for this project.'
        commands = (
            'pytest -m "not integration" --cov-report html --cov-report term '
            '--cov-report xml --cov --cov-branch --cov-config={setup_dir}'
            '/coverage.cfg --cov-fail-under=0 --cov-report annotate {setup_dir}'
        )
        assert config.commands == (commands,)



# Generated at 2022-06-13 21:03:34.590280
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.systemutils import mkdtemp

    def _validate(setup_dir: str) -> None:
        for config in each_sub_command_config(setup_dir):
            assert isinstance(config.name, str)
            assert isinstance(config.camel, str)
            assert isinstance(config.description, str)
            assert isinstance(config.commands, tuple)
            if config.commands:
                for cmd in config.commands:
                    assert isinstance(cmd, str)
            assert config.name != ''

    def _write_setup_cfg(path: os.posix.PosixPath, name: str) -> None:
        # noinspection PyTypeChecker
        with open(path, 'w') as fd:
            print('[metadata]', file=fd)

# Generated at 2022-06-13 21:03:39.329364
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import pprint
    this_dir = os.path.dirname(__file__)
    setup_dir = os.path.dirname(this_dir)
    pprint.pprint(list(each_sub_command_config(setup_dir)))

