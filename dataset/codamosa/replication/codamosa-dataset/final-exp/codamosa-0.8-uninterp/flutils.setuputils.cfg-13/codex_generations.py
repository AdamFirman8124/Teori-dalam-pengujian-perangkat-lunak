

# Generated at 2022-06-13 20:53:58.689350
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    root_dir = os.path.dirname(os.path.dirname(__file__))
    root_dir = os.path.join(root_dir, 'example')
    for config in each_sub_command_config(root_dir):
        assert config.name is not None
        assert config.camel is not None
        assert config.description is not None
        assert config.commands is not None
        assert len(config.commands) > 0

# Generated at 2022-06-13 20:54:06.871888
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from shutil import (
        copyfileobj,
        move,
        rmtree,
    )
    from tempfile import NamedTemporaryFile
    from flutils.testutils import TempDirTestCase

    test_dir_name = '__setuptools-setup-commands__'
    setup_cfg_name = 'setup.cfg'
    setup_py_name = 'setup.py'

    class TestSetupCmd(TempDirTestCase):
        def setUp(self):
            super(TestSetupCmd, self).setUp()
            self.setup_dir = os.path.join(self.temp_dir, test_dir_name)
            os.mkdir(self.setup_dir)

# Generated at 2022-06-13 20:54:21.287855
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.join(os.path.dirname(__file__), 'scratch', 'test_setup_command')
    out = set(each_sub_command_config(setup_dir))

# Generated at 2022-06-13 20:54:32.560997
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil
    import textwrap
    setup_dir = tempfile.TemporaryDirectory()

# Generated at 2022-06-13 20:54:43.747791
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    from io import StringIO

    with tempfile.TemporaryDirectory() as td:
        td = os.path.realpath(td)
        setup_py = os.path.join(td, 'setup.py')
        setup_cfg = os.path.join(td, 'setup.cfg')
        setup_commands_cfg = os.path.join(td, 'setup_commands.cfg')
        print(td)
        print(setup_py)

        with open(setup_py, 'w') as f:
            f.write('')

        # Test invalid setup directory
        try:
            list(each_sub_command_config(td))
        except (FileNotFoundError, NotADirectoryError) as ex:
            assert 'does NOT contain a setup.cfg' in str(ex)

       

# Generated at 2022-06-13 20:54:54.818994
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import pytest
    from flutils.helpers.setup_utils import (
        each_sub_command_config,
        test_each_sub_command_config,
        SetupCfgCommandConfig,
    )
    from flutils.helpers.setup_kwargs import get_setup_kwargs
    for setup_dir in ('.', '../..'):
        for config in each_sub_command_config(setup_dir):
            config = cast(SetupCfgCommandConfig, config)
            yield config
    with pytest.raises(FileNotFoundError):
        each_sub_command_config('foo')
    with pytest.raises(FileNotFoundError):
        each_sub_command_config(None)

# Generated at 2022-06-13 20:55:00.211421
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.dirname(__file__)
    # setup_dir = os.path.dirname(os.path.dirname(__file__))
    for sccc in each_sub_command_config(setup_dir):
        print(sccc)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:55:03.496532
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    print(list(each_sub_command_config()))


test_each_sub_command_config.unittest = ['.path', 'setup_cfg']


if __name__ == '__main__':
    raise SystemExit(__import__('doctest').testmod()[0])

# Generated at 2022-06-13 20:55:15.243216
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.testutils import TempDirTestCase

    class TestEachSubCommandConfig(TempDirTestCase):

        def test_each_sub_command_config(self):
            path = os.path.join(self.temp_dir, 'setup.py')
            with open(path, 'w') as f:
                f.write('#!/usr/bin/env python3\n')

            path = os.path.join(self.temp_dir, 'setup.cfg')
            with open(path, 'w') as f:
                f.write('''\
[metadata]
name = foo-bar
version = 2.3.4

[options]
packages = find:

[options.package_data]
* = *.txt, *.rst
                ''')


# Generated at 2022-06-13 20:55:26.353941
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import get_bin_dirpath
    import sysconfig
    from pathlib import Path

    exe_dir = get_bin_dirpath(sysconfig.get_path('scripts'))
    setup_dir = sysconfig.get_path('data')
    test_cmd_cfgs = os.path.join(setup_dir, 'setup_commands.cfg')

    # Test with an existing package
    out = []
    for cfg in each_sub_command_config():
        out.append(cfg)
    assert out[0].camel == 'Test'
    assert out[0].name == 'test'
    assert out[0].commands == ('pytest', )

    # Test with a local project that contains a setup_commands.cfg file

# Generated at 2022-06-13 20:55:43.618982
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    cfg_path = os.path.join(os.getcwd(), 'tests', 'data', 'setup_commands.cfg')
    parser = ConfigParser()
    parser.read(cfg_path)

    format_kwargs: Dict[str, str] = {
        'setup_dir': os.path.dirname(cfg_path),
        'home': os.path.expanduser('~'),
        'name': 'example-project',
    }
    name_title_description_cmds = tuple(
        (cfg.name, cfg.camel, cfg.description)
        for cfg in _each_setup_cfg_command(parser, format_kwargs)
    )

# Generated at 2022-06-13 20:55:58.506479
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.envutils import get_temp_path
    from flutils.pathutils import each_file
    from flutils.timeutils import UTCTime
    from os import path
    from pathlib import Path
    from shutil import rmtree
    from tempfile import mkdtemp
    from textwrap import dedent

    from pytest import raises
    from typing import Generator

    TEMP_DIR = mkdtemp()
    SETUP_DIR = path.join(TEMP_DIR, 'setup')
    Path(SETUP_DIR).mkdir()
    SETUP_CFG_PATH = path.join(SETUP_DIR, 'setup.cfg')
    SETUP_PY_PATH = path.join(SETUP_DIR, 'setup.py')


# Generated at 2022-06-13 20:56:12.114326
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile

    # Create the contents of a setup.py file
    setup_py_contents = """
from distutils.core import setup
setup(
    name='flutils',
    version='1.2.3',
    py_modules=['flutils'],
    scripts=['sum.py'],
    zip_safe=False,
)
"""
    # Create the contents of a setup.cfg file
    setup_cfg_contents = """
[metadata]
name = flutils
version = 1.2.3

[options]
test_suite = tests.tests
install_requires = 
    flutils = 1.2.3
"""
    # Create the contents of a setup_commands.cfg file

# Generated at 2022-06-13 20:56:18.824502
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import shutil
    import tempfile

    def _run_test(
            setup_dir: Optional[Union[os.PathLike, str]] = None
    ) -> None:
        setup_dir = _prep_setup_dir(setup_dir=setup_dir)
        setup_cfg_path = os.path.join(setup_dir, 'setup.cfg')
        with open(setup_cfg_path, 'a') as f:
            f.write('\n[metadata]\nname = flutils')
        import flutils
        sys.path.insert(0, setup_dir)
        try:
            for sc in each_sub_command_config(setup_dir=setup_dir):
                print(sc)
        finally:
            sys.path.remove(setup_dir)

# Generated at 2022-06-13 20:56:24.001508
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from sys import path
    from os import getcwd
    path.insert(0, getcwd())

    from flutils.setuputils import each_sub_command_config


    from typing import Generator
    from configparser import ConfigParser

    from flutils.setuputils import each_sub_command_config
    from flutils.setuputils import SetupCfgCommandConfig

    def _each_sub_command_config(
            parser: ConfigParser
    ) -> Generator[
        SetupCfgCommandConfig, None, None
    ]:
        for sc in each_sub_command_config():
            assert isinstance(sc, SetupCfgCommandConfig)
            yield sc

    parser = ConfigParser()
    parser.read('setup.cfg')
    scs = list(_each_sub_command_config(parser))

    assert scs


# Unit

# Generated at 2022-06-13 20:56:35.350185
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os

    def _each_sub_command_config(setup_dir: str,
                                 expected_name: str,
                                 expected_sub_cmd_count: int,
                                 expected_sub_cmd: Tuple[str, ...]):

        name = None
        count = 0
        sub_cmds: List[str] = []
        for config in each_sub_command_config(setup_dir):
            name = config.name
            sub_cmds.append(config.commands[0])
            count += 1

        assert count == expected_sub_cmd_count
        assert expected_sub_cmd == tuple(sub_cmds)
        assert expected_name == name

    test_dir = os.path.dirname(__file__)

# Generated at 2022-06-13 20:56:43.844714
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    path = os.path.join(
        os.path.dirname(__file__),
        'example_project'
    )
    name = 'example_project'
    for cmd in each_sub_command_config(path):
        assert name in cmd.name
        assert cmd.camel.endswith('Command')
        assert len(cmd.commands) == 1
        assert 'man' in cmd.commands[0]



# Generated at 2022-06-13 20:56:47.702986
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import relpath_to_file
    from pprint import pprint

    print()
    pprint(tuple(each_sub_command_config(relpath_to_file())))
    print()


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:56:52.823374
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    actual = list(each_sub_command_config('.'))
    expected = [
        SetupCfgCommandConfig(
            'fixme',
            'Fixme',
            'Fixme - Destroys all the things',
            ('echo \'Destroys all the things\'',)
        )
    ]
    assert actual == expected


# Generated at 2022-06-13 20:56:57.015425
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from sys import stdout
    from textwrap import dedent as dd
    for config in each_sub_command_config():
        commands = dd('\n'.join(config.commands))
        stdout.write(f'{config.name}:\n{commands}\n')

# Generated at 2022-06-13 20:57:09.272923
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    this_path = os.path.realpath(os.path.dirname(__file__))
    _calls, _results = 0, 0
    for sc in each_sub_command_config(this_path):
        _calls += 1
        if '_tests' not in sc.name:
            _results += 1
    assert _calls == 1, _calls
    assert _results == 1, _results


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:57:23.663036
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from tests.unit.setup_commands import test_config_file
    from tests.unit import (
        setup_commands_1,
        setup_commands_2,
        setup_commands_3,
        setup_commands_4,
        setup_commands_5,
        setup_commands_6,
        setup_commands_7,
        setup_commands_8,
        setup_commands_9,
        setup_commands_10,
    )
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        name = 'flutils-test-project'
        setup_dir = os.path.join(tmpdir, name)
        os.mkdir(setup_dir)

# Generated at 2022-06-13 20:57:25.414356
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for setup_cfg_command_config in each_sub_command_config():
        pass
    assert True

# Generated at 2022-06-13 20:57:28.173998
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for cfg in each_sub_command_config(setup_dir='.'):
        print(cfg)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:57:39.622932
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import os
    import tempfile
    import unittest
    from contextlib import (
        redirect_stderr,
        redirect_stdout,
    )
    from io import StringIO
    from subprocess import Popen, PIPE
    from typing import (
        Dict,
        Iterable,
        Iterator,
        Optional,
        Tuple,
    )
    from unittest.mock import patch

    from flutils.systemutils import (
        create_process,
        platform_is,
    )

    from .func_utils import (
        each_sub_command_config as each_sub_command_config_func,
        get_test_config,
    )

    # pylint: disable=missing-docstring

# Generated at 2022-06-13 20:57:44.039287
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for command_config in each_sub_command_config():
        assert command_config.name.isidentifier() is True
        assert command_config.camel.isidentifier() is True
        assert command_config.commands



# Generated at 2022-06-13 20:57:56.592418
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Tests the function
    :func:`~flutils.projutils.each_sub_command_config`.
    """
    from flutils.projutils import (
        each_sub_command_config,
        setup_dir,
    )
    from flutils.testutils import get_caller
    path = get_caller('test', 3)
    for config in each_sub_command_config(path):
        assert config is not None
        assert config.camel
        assert config.name
        assert config.commands
        assert config.description
    setup_cfg_path = os.path.join(path, 'setup.cfg')
    with open(setup_cfg_path, 'w') as w_fp:
        w_fp.write('[metadata]\n')

# Generated at 2022-06-13 20:58:08.082170
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import textwrap

    OUT = [
        SetupCfgCommandConfig(
            name='myfunc',
            camel='MyFunc',
            description='This is my func.',
            commands=(
                'echo hi',
                'echo there'
            )
        )
    ]

    with open('setup.py', 'w') as f:
        f.write('import setuptools\n')

    with open('setup.cfg', 'w') as f:
        f.write('[metadata]\n')
        f.write("name = my_package\n")
        f.write("\n")
        f.write("[setup.command.xyz]\n")
        f.write('name = myfunc\n')
        f.write('description = This is my func.\n')

# Generated at 2022-06-13 20:58:14.068625
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # Test with a PathLike
    for _ in each_sub_command_config(Path(__file__).parent):
        pass
    # Test with a string
    for _ in each_sub_command_config(str(Path(__file__).parent)):
        pass
    # Test without specifying the setup_dir
    for _ in each_sub_command_config():
        pass

# Generated at 2022-06-13 20:58:27.246463
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def _test_each_sub_command_config(
        parser: ConfigParser,
        path: str,
        setup_dir: str,
        expected: List[SetupCfgCommandConfig],
    ):
        setup_dir = os.path.realpath(setup_dir)
        actual = list(each_sub_command_config(setup_dir=setup_dir))
        assert expected == actual

    # Tests using a simple setup.cfg file
    parser = ConfigParser()
    path = os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        'data',
        'simple',
        'setup.cfg'
    )
    parser.read(path)
    # Get the test path

# Generated at 2022-06-13 20:58:50.234320
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    configs = list(each_sub_command_config('./tests/data/setup-python'))
    configs = sorted(configs, key=lambda x: x.name)
    assert len(configs) == 2
    assert configs[0].name == 'app.sub.subsub'
    assert configs[0].camel == 'SubSubsub'
    assert configs[0].description == ''

# Generated at 2022-06-13 20:58:52.718754
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config():
        print(config)

# Generated at 2022-06-13 20:59:00.579580
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    cmds = []
    def go():
        for cmd in each_sub_command_config():
            cmds.append(cmd)
    go()
    if cmds:
        cmds = sorted(cmds, key=lambda c: c.name)
        for cmd in cmds:
            print(cmd)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:59:03.830788
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for cfg in each_sub_command_config():
        print(cfg)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:59:07.481756
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.dirname(__file__)
    for config in each_sub_command_config(setup_dir):
        print(config)

# Generated at 2022-06-13 20:59:15.952394
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import re
    import pathlib
    root = pathlib.Path(__file__).parent
    project_files = root.joinpath('project_files')
    os.chdir(project_files)
    from flutils.pathutils import ensure_dir
    ensure_dir(root.joinpath('gen'))
    sys.path.append(str(root))
    for i, each in enumerate(each_sub_command_config('project_files')):
        with open('gen/setup.cfg', 'w', encoding='UTF-8') as fout:
            fout.write(each.description)
        os.system('cat gen/setup.cfg')
        assert i == 0



# Generated at 2022-06-13 20:59:26.226534
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from sys import exc_info, modules
    from pprint import pprint
    for item in each_sub_command_config():
        pprint(item)
    assert exc_info() == (None, None, None), \
        'each_sub_command_config must not throw an exception'
    assert modules['__main__'].__file__ == 'tests/test_setup_cfg.py', \
        'each_sub_command_config must run in the correct file'
    del modules['__main__']

if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:59:39.167497
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config."""
    import sys
    import unittest
    from pathlib import Path

    class TestEachSubCommandConfig(unittest.TestCase):
        def test_each_sub_command_config(self):
            """Unit test for function each_sub_command_config."""
            root_dir = Path(__file__).parent
            if sys.version_info.minor == 8:
                root_dir = root_dir / 'script_setup_cfg'
            else:
                root_dir = root_dir / 'script_setup_cfg_py3_9'
            with self.assertRaises(FileNotFoundError):
                each_sub_command_config(root_dir / 'bin')
            with self.assertRaises(NotADirectoryError):
                each_

# Generated at 2022-06-13 20:59:49.741241
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    data = list(each_sub_command_config(
        setup_dir='tests/data/scaffold'
    ))

# Generated at 2022-06-13 21:00:01.541877
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    print('Testing %r' % each_sub_command_config)

    def contents(p) -> List[str]:
        return list(sorted(map(cast(str, os.path.basename), os.listdir(p))))

    orig_cwd = os.getcwd()

# Generated at 2022-06-13 21:00:31.267880
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.dirname(__file__)
    for scc in each_sub_command_config(setup_dir):
        print(scc.commands)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:00:43.500349
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import pytest
    import sys
    import pathlib
    import os

    here = pathlib.Path(__file__).parent
    root = here.parent.parent
    root = str(root)
    sys.path.insert(0, root)
    from flutils.fileutils import (
        copy_files,
        move_files,
        rm_files,
    )
    from flutils.miscutils import (
        make_temp_dir,
        read_file,
    )

    setup_cfg_path = os.path.join(root, 'setup.cfg')
    setup_py_path = os.path.join(root, 'setup.py')
    setup_commands_cfg_path = os.path.join(root, 'setup_commands.cfg')

# Generated at 2022-06-13 21:00:55.282241
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    import os.path
    import shutil
    import tempfile

    def _create_setup_cfg_file(path: str, cmd_count: int = 0) -> None:
        with open(path, 'w') as out:
            out.write(
                "[metadata]\n"
                "name = test_pkg\n"
            )
        if cmd_count:
            with open(path, 'a') as out:
                for i in range(cmd_count):
                    out.write(f"\n[setup.command.test.cmd-{i}]\n")
                    out.write(f"    name = test_cmd-{i}\n")
                    out.write(f"    description = Test command {i}!\n")


# Generated at 2022-06-13 21:01:09.672299
# Unit test for function each_sub_command_config
def test_each_sub_command_config():  # noqa: D103
    from structlog._config import _CONFIG
    from structlog._frames import _find_first_app_frame_and_name
    import structlog
    from structlog.threadlocal import wrap_dict
    _CONFIG.clear()
    _find_first_app_frame_and_name.cache_clear()
    structlog.reset_defaults()
    structlog.configure(
        processors=[
            wrap_dict(lambda d: d.update({'test': 'unit'}))
        ]
    )
    from sys import stderr
    from structlog import get_logger
    from flutils.setuputils import each_sub_command_config
    logger = get_logger()

# Generated at 2022-06-13 21:01:16.933401
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from os.path import abspath, dirname, join
    setup_dir = join(dirname(abspath(__file__)), 'setup_dir')
    for conf in each_sub_command_config(setup_dir):
        print(conf)
        assert conf.name is not None
        assert conf.camel is not None
        assert conf.description is not None
        assert conf.commands is not None

# Generated at 2022-06-13 21:01:21.449386
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    try:
        cast(Generator, each_sub_command_config())
    except Exception as err:
        raise AssertionError(
            'Function each_sub_command_config raised: %r.' % err
        )

# Generated at 2022-06-13 21:01:33.665399
# Unit test for function each_sub_command_config
def test_each_sub_command_config():

    def _validate(
            config: Tuple[str, ...],
            setup_cfg_command: SetupCfgCommandConfig
    ) -> None:
        name, camel, description, commands = config
        assert setup_cfg_command.name == name, (
                config, setup_cfg_command
        )
        assert setup_cfg_command.camel == camel, (
                config, setup_cfg_command
        )
        assert setup_cfg_command.description == description, (
                config, setup_cfg_command
        )
        assert setup_cfg_command.commands == commands, (
                config, setup_cfg_command
        )

    test_dir = os.path.dirname(os.path.abspath(__file__))

# Generated at 2022-06-13 21:01:38.783950
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.expanduser('~/src/flutils.py')
    for config in each_sub_command_config(setup_dir):
        assert config.commands
        break
    else:
        raise AssertionError("Nothing returned !")

# Generated at 2022-06-13 21:01:51.694468
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    import sys

    import six
    from flutils.configutils import (
        _each_setup_cfg_command_section,
        _each_setup_cfg_command,
    )

    setup_dir = os.path.dirname(__file__)
    parser = ConfigParser()
    parser.read(os.path.join(setup_dir, 'setup.cfg'))
    format_kwargs = {
        'setup_dir': setup_dir,
        'home': os.path.expanduser('~')
    }
    for section, command_name in _each_setup_cfg_command_section(parser):
        commands: List[str] = []
        options: List[str] = parser.options(section)

# Generated at 2022-06-13 21:01:59.622682
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.testutils import TempDir

    with TempDir() as tmpdir:
        with open(os.path.join(tmpdir, 'setup.cfg'), 'w') as fp:
            fp.write(
                '[metadata]\n'
                'name=flutils'
            )
        with open(os.path.join(tmpdir, 'setup_commands.cfg'), 'w') as fp:
            fp.write(
                '[setup.command.install]\n'
                "name={name} install\n"
                "description=Installing {name}\n"
                "command=echo Installing {name} to '{setup_dir}'"
            )

# Generated at 2022-06-13 21:02:57.994612
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import get_file_dir

    # Testcase 1
    with pytest.raises(FileNotFoundError):
        each_sub_command_config('/does/not/exist')

    # Testcase 2
    with pytest.raises(NotADirectoryError):
        each_sub_command_config('/tmp/doesnotexist')

    # Testcase 3
    with pytest.raises(FileNotFoundError):
        each_sub_command_config('/etc')

    # Testcase 4
    with pytest.raises(FileNotFoundError):
        each_sub_command_config(os.path.abspath(__file__))

    # Testcase 5
    setup_dir = get_file_dir(__file__)

# Generated at 2022-06-13 21:03:07.560922
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    found = False
    for config in each_sub_command_config(
            os.path.dirname(os.path.dirname(__file__))
    ):
        found = True
        assert config.name == 'setup_commands'
        assert config.camel == 'SetupCommands'
        assert config.description == (
            "Configures 'flutils.django.setup' sub-commands."
        )
        assert config.commands == (
            "python -m flutils.django.setup_commands",
        )
    assert found is True


if __name__ == "__main__":
    test_each_sub_command_config()

# Generated at 2022-06-13 21:03:17.890513
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from .__main__ import each_sub_command_config as func

    def _test(
            in_setup_dir: str,
            exp_config: List[SetupCfgCommandConfig]
    ) -> None:
        gen_config = list(func(in_setup_dir))
        assert exp_config == gen_config

    _test(
        in_setup_dir='tests/data/simple',
        exp_config=[
            SetupCfgCommandConfig(
                'cmd',
                'Cmd',
                'This is the command.',
                (
                    'echo "This is the command."',
                ),
            )
        ],
    )

# Generated at 2022-06-13 21:03:24.388612
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    cmd_configs = tuple(each_sub_command_config())
    assert isinstance(cmd_configs, tuple)
    assert len(cmd_configs) == 2

    expected_camel = [
        'UnicodeTest',
        'UnicodeTestWithDocker'
    ]
    expected_list = [
        'unicodetest',
        'unicodetest_with_docker'
    ]

    for cmd_config in cmd_configs:
        assert isinstance(cmd_config, SetupCfgCommandConfig)
        assert cmd_config.camel in expected_camel
        expected_camel.remove(cmd_config.camel)
        assert isinstance(cmd_config.name, str)
        assert cmd_config.name in expected_list
        expected_list.remove(cmd_config.name)

# Generated at 2022-06-13 21:03:33.120877
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    cfg: List[SetupCfgCommandConfig] = []
    for config in each_sub_command_config(os.path.expanduser('~/Code/flutils')):
        cfg.append(config)
    assert cfg.__len__() >= 2
    for config in cfg:
        for attr in ('description', 'camel', 'name', 'commands'):
            assert hasattr(config, attr)
    assert 'tests' in cfg[0].commands[0]
    assert 'python' in cfg[0].commands[0]