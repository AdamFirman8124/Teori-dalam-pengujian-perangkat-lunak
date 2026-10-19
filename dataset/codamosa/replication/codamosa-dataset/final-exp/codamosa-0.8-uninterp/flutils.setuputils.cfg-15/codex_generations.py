

# Generated at 2022-06-13 20:54:03.652042
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.join(
        os.path.dirname(__file__), '..', '..', '..', 'flutils_pytest_example'
    )
    for config in each_sub_command_config(setup_dir):
        print(config.name)
        print(config.camel)
        print(config.description)
        print(config.commands)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:54:17.567405
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    cmds = [cmd for cmd in each_sub_command_config()]
    assert cmds[0] == SetupCfgCommandConfig(
        'docs.make_docs',
        'MakeDocs',
        'Make all documentation.',
        ('mkdocs build -d ../build/docs',)
    )
    assert cmds[1] == SetupCfgCommandConfig(
        'docs.serve_docs',
        'ServeDocs',
        'Serve all documentation.',
        ('mkdocs serve',)
    )
    assert cmds[2] == SetupCfgCommandConfig(
        'test',
        'Test',
        'Run tests.',
        ('pytest -vv --cov=flutils --ignore=build',)
    )
    assert len(cmds) == 3

# Generated at 2022-06-13 20:54:24.585506
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config():
        try:
            config.name
            config.camel
            config.description
            config.commands
        except AttributeError:
            raise AttributeError("each_sub_command_config does not "
                                 "produce SetupCfgCommandConfig")

# Generated at 2022-06-13 20:54:31.013629
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    c = next(each_sub_command_config(setup_dir='../..'))
    assert c.name == 'list_hooks'
    assert c.camel == 'ListHooks'
    assert c.description == ''
    assert c.commands == ('git submodule foreach --recursive '
                          'git config --list --show-origin --local '
                          '| sed -r "s/^/<repo>/g"',)

# Generated at 2022-06-13 20:54:40.347495
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    tests = (
        ('test_data', 'test_data'),
    )
    for test_data, expected in tests:
        actual = []
        for config in each_sub_command_config(test_data):
            actual.append(config.name)
        actual = ' '.join(actual)
        yield (
            assert_equal,
            expected,
            actual,
        )
    # Assert exception thrown
    try:
        next(each_sub_command_config())
    except Exception as e:
        yield assert_is_instance, e, FileNotFoundError
    # Assert exception thrown
    try:
        next(each_sub_command_config('/bogus/path'))
    except Exception as e:
        yield assert_is_instance, e, FileNotFoundError
    # Assert exception thrown


# Generated at 2022-06-13 20:54:42.354657
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    assert next(each_sub_command_config(setup_dir='.'))

# Generated at 2022-06-13 20:54:53.621602
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import unittest
    import shutil
    import tempfile

    class Test(unittest.TestCase):
        @staticmethod
        def _write_file(
                path: Union[os.PathLike, str],
                contents: str
        ) -> None:
            with open(path, 'w') as f:
                f.write(contents)

        def test_with_setup_cfg(self):
            empty_dir = tempfile.mkdtemp()
            setup_cfg = os.path.join(empty_dir, 'setup.cfg')
            self._write_file(setup_cfg, '[metadata]\nname=test')
            setup_dir = tempfile.mkdtemp()
            setup_py = os.path.join(setup_dir, 'setup.py')

# Generated at 2022-06-13 20:55:10.077651
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    args = sys.argv
    sys.argv = ['setup.py', 'build']

    base_dir = os.path.dirname(os.path.realpath(__file__))
    base_dir = os.path.join(base_dir, os.pardir)

    for sub_cmd_cfg in each_sub_command_config(base_dir):
        print(
            "name: %r\n"
            "camel: %r\n"
            "description: %r\n"
            "commands: %r\n"
            % (
                sub_cmd_cfg.name,
                sub_cmd_cfg.camel,
                sub_cmd_cfg.description,
                sub_cmd_cfg.commands
            )
        )

# Generated at 2022-06-13 20:55:16.766581
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    cwd = os.path.dirname(os.path.abspath(__file__))
    pkg_dir = os.path.join(cwd, 'pkg')
    config = next(each_sub_command_config(pkg_dir))
    assert config.name == 'pkg'
    assert config.camel == 'Pkg'
    assert config.description == 'pkg sub command!'
    assert config.commands == ('ls -la', )

# Generated at 2022-06-13 20:55:19.541342
# Unit test for function each_sub_command_config

# Generated at 2022-06-13 20:55:33.446540
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.testutils import unit_test_init
    unit_test_init()
    cmds = list(each_sub_command_config(os.path.realpath(__file__)))
    print(cmds)
    assert len(cmds) == 2
    assert cmds[0].name == 'build'
    assert cmds[0].camel == 'Build'
    assert cmds[0].description == 'Run build methods'
    assert cmds[0].commands == (
        'python setup.py clean sdist bdist_wheel',
        'twine upload dist/*'
    )

# Generated at 2022-06-13 20:55:38.872588
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def _test(setup_dir: str):
        for config in each_sub_command_config(setup_dir):
            print("Config:", str(config))

    _test('tests/custom_commands/sub1')
    _test('tests/custom_commands/sub2')


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:55:45.567227
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function, each_sub_command_config."""
    for section, cmd_name in _each_setup_cfg_command_section(
            ConfigParser()
    ):
        assert section.startswith('setup.command.')
        assert cmd_name
    format_kwargs = {
        'setup_dir': '/etc/passwd',
        'home': '/root',
    }
    var = list(_each_setup_cfg_command(ConfigParser(), format_kwargs))
    assert var == []


__all__ = ('each_sub_command_config',)

# Generated at 2022-06-13 20:55:51.650684
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    expected = (
        SetupCfgCommandConfig(
            'foo',
            'Foo',
            'A test',
            ('echo _a_',)),
    )
    out = list(each_sub_command_config('/home/peter/dev/flutils/tests/fixtures'))
    assert expected == out

# Generated at 2022-06-13 20:55:57.435575
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.objutils import __file__
    from flutils.pathutils import up_to_project_root

    setup_dir = up_to_project_root(__file__, level=2)
    for x in each_sub_command_config(setup_dir):
        print(x)



# Generated at 2022-06-13 20:56:10.594907
# Unit test for function each_sub_command_config

# Generated at 2022-06-13 20:56:22.389792
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    print('Test Name:', inspect.stack()[0][3])

    def _test(
            name: str,
            setup_dir: Union[os.PathLike, str],
            expected: Optional[SetupCfgCommandConfig],
            setup_cfg_path: Optional[Union[os.PathLike, str]] = None,
            setup_commands_cfg_path: Optional[Union[os.PathLike, str]] = None
    ) -> None:
        print('  Setup Dir:', setup_dir)
        print('  Expected Output:', expected)
        if setup_cfg_path:
            print('  Setup Config Path:', setup_cfg_path)
        if setup_commands_cfg_path:
            print('  Setup Commands Config Path:', setup_commands_cfg_path)

# Generated at 2022-06-13 20:56:24.786673
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for t in each_sub_command_config():
        assert isinstance(t, SetupCfgCommandConfig)

# Generated at 2022-06-13 20:56:30.157847
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.realpath(
        os.path.join(os.path.dirname(__file__), '..')
    )
    for config in each_sub_command_config(setup_dir):
        print(config)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:56:34.674296
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for sub_cmd_cfg in each_sub_command_config(
            setup_dir=os.path.join(os.path.dirname(__file__), 'test_data')):
        assert sub_cmd_cfg is not None


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:56:51.164664
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from os import environ, sep
    from os.path import dirname, join
    from unittest.mock import patch
    from pathlib import Path
    from tempfile import gettempdir
    from contextlib import contextmanager

    def _test_setup_commands_cfg(
            tmp_dir: str,
            *,
            setup_cfg_command_sections: Tuple[str, ...] = (),
            setup_cfg_command_options: Dict[str, Tuple[str, ...]] = {},
            setup_cfg_command_values: Dict[str, str] = {},
            setup_cfg_command_names: Dict[str, str] = {},
            setup_cfg_command_descriptions: Dict[str, str] = {}
    ) -> None:
        setup_cfg_command_sections

# Generated at 2022-06-13 20:56:54.191007
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    if __name__ == '__main__':
        for sub_command in each_sub_command_config():
            pass


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:56:59.467325
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for scc in each_sub_command_config(setup_dir=os.path.dirname(__file__)):
        assert isinstance(scc, SetupCfgCommandConfig)
        assert isinstance(scc.name, str)
        assert isinstance(scc.camel, str)
        assert isinstance(scc.description, str)
        assert isinstance(scc.commands, tuple)
        assert all([isinstance(c, str) for c in scc.commands])


__all__ = ('each_sub_command_config',)

# Generated at 2022-06-13 20:57:10.166786
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import unittest
    from unittest.mock import patch

    from flutils.setuputils import each_sub_command_config
    from flutils.setuputils.testing import (
        mock_ConfigParser,
        mock_ConfigParser_add_section,
        mock_ConfigParser_options,
        mock_ConfigParser_get,
    )


# Generated at 2022-06-13 20:57:13.311011
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    config = list(each_sub_command_config())
    #print('config: %r' % config)



# Generated at 2022-06-13 20:57:25.025143
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    cntr = 0
    for setup_cfg_command_config in each_sub_command_config():
        assert isinstance(setup_cfg_command_config, SetupCfgCommandConfig)
        assert isinstance(setup_cfg_command_config.name, str)
        assert isinstance(setup_cfg_command_config.camel, str)
        assert isinstance(setup_cfg_command_config.description, str)
        assert isinstance(setup_cfg_command_config.commands, tuple)
        for cmd in setup_cfg_command_config.commands:
            assert isinstance(cmd, str)
        cntr += 1
    assert cntr == 3

# Generated at 2022-06-13 20:57:28.298461
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for i in each_sub_command_config('tests/tests'):
        print(i)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:57:39.684309
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    test_setup_dir = os.path.join(
        os.path.dirname(os.path.abspath(os.path.expanduser(__file__))),
        'testdata'
    )
    for i, x in enumerate(each_sub_command_config(setup_dir=test_setup_dir)):
        if i == 0:
            assert x.name == 'initdb'
            assert x.camel == 'Initdb'
            assert x.description == (
                'Initializing the database.'
            )
            assert x.commands == (
                'python -m flutils.database.scripts.initdb',
            )
        else:
            assert x.name == 'update_db'
            assert x.camel == 'UpdateDB'

# Generated at 2022-06-13 20:57:46.136656
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    _setup_dir = os.path.abspath(os.path.dirname(__file__))
    _setup_dir = os.path.join(_setup_dir, '..', '..', '..', '..')
    for config in each_sub_command_config(_setup_dir):
        print(config)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:57:58.783791
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from unittest import TestCase

    class Test(TestCase):
        def test_basic(self):
            import os
            import functools
            import pathlib
            import tempfile

            def test_cmd_count(setup_dir, expected):
                """
                Helper function to test that the correct number of commands
                are returned by each_sub_command_config.
                """
                actual = list(each_sub_command_config(setup_dir))
                self.assertEqual(len(actual), expected)

            self.assertRaises(
                LookupError, each_sub_command_config, 'some_bad_path'
            )
            self.assertRaises(
                LookupError, each_sub_command_config, 'some_bad_path=123'
            )

# Generated at 2022-06-13 20:58:12.809532
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    data = list(each_sub_command_config())


if __name__ == '__main__':
    list(each_sub_command_config())

# Generated at 2022-06-13 20:58:26.431588
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    config = [
        (
            'test.command',
            'test.sub_name',
            'This is a test command.',
            'command_1',
            'command_2',
        ),
        (
            'test.command',
            'test.sub_name2.abc',
            'This is a test command 2.',
            'command_1',
            'command_2',
        ),
        (
            'test.command',
            'test.sub_name3.123',
            'This is a test command 3.',
            'command_1',
            'command_2',
        ),
    ]


# Generated at 2022-06-13 20:58:39.175240
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_cfg_path = os.path.abspath(
        os.path.join(
            os.path.realpath(os.path.dirname(__file__)),
            '../tests/pkgs/flutils_package/setup.cfg'
        )
    )
    setup_commands_cfg_path = os.path.abspath(
        os.path.join(
            os.path.realpath(os.path.dirname(__file__)),
            '../tests/pkgs/flutils_package/setup_commands.cfg'
        )
    )
    setup_dir = os.path.dirname(setup_cfg_path)

# Generated at 2022-06-13 20:58:49.488055
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from os import linesep

    from flutils.pathutils import each_file_recursive
    from flutils.pathutils import tmpdir

    with tmpdir() as tmp_dir:
        path = os.path.join(tmp_dir, 'setup.py')
        with open(path, 'w') as fp:
            fp.write('1')
        path = os.path.join(tmp_dir, 'setup.cfg')
        with open(path, 'w') as fp:
            fp.write("""[metadata]
name = foo_bar


[setup.command.foo.bar]
command = True
    """)

# Generated at 2022-06-13 20:59:04.160242
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    cmds = list(each_sub_command_config())
    assert len(cmds) == 4
    assert cmds[0] == SetupCfgCommandConfig(
        name='sdist',
        camel='Sdist',
        description='Build a source distribution.',
        commands=('/Users/david/Documents/Projects/Flutils/venv/bin/python '
                  'setup.py sdist',)
    )

# Generated at 2022-06-13 20:59:15.123542
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.testutils import UnitCase

    class Test(UnitCase):
        def setUp(self):
            package_dir = self.find_package_dir(__name__)
            self.setup_dir = os.path.join(package_dir, 'test_files')

        def test_no_setup_dir(self):
            self.assertIn(
                'setup_commands.cfg',
                self.format_exc_info(each_sub_command_config)
            )

        def test_bad_setup_dir(self):
            self.assertIn(
                "does NOT exist",
                self.format_exc_info(each_sub_command_config, '.')
            )


# Generated at 2022-06-13 20:59:27.436688
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config."""
    cdb = os.path.dirname(__file__)
    cdb = os.path.dirname(cdb)
    cdb = os.path.dirname(cdb)
    lines = []
    for cmd_config in each_sub_command_config(cdb):
        lines.append('Name: %s' % cmd_config.name)
        lines.append('Camel: %s' % cmd_config.camel)
        lines.append('Description: %s' % cmd_config.description)
        for cmd in cmd_config.commands:
            lines.append('- %s' % cmd)

# Generated at 2022-06-13 20:59:39.994955
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import pytest
    from tempfile import TemporaryDirectory
    from shutil import rmtree

    d = TemporaryDirectory()

# Generated at 2022-06-13 20:59:50.510590
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def _test(setup_dir: str, expected: List[Dict[str, str]]) -> None:
        out = list(each_sub_command_config(setup_dir))
        assert len(out) == len(expected)
        for i, e in enumerate(expected):
            assert out[i].name == e['name']
            assert out[i].camel == e['camel']
            assert out[i].description == e['description']
            assert out[i].commands == tuple(e['comand'])


# Generated at 2022-06-13 21:00:01.912607
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import os
    import tempfile

    from flutils.testutils import BaseTestCase

    from .encoding import ensure_text

    class TestEachSubCommandConfig(BaseTestCase):

        def setUp(self) -> None:
            self.test_dir = tempfile.TemporaryDirectory(prefix='test_')
            self.addCleanup(self.test_dir.cleanup)

            self.test_dir_path = ensure_text(self.test_dir.name)
            self._cd = os.getcwd()
            os.chdir(self.test_dir_path)

        def tearDown(self) -> None:
            os.chdir(self._cd)


# Generated at 2022-06-13 21:00:28.136569
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit testing for function ``each_sub_command_config``."""
    for subcommand in each_sub_command_config(__file__):
        assert isinstance(subcommand, SetupCfgCommandConfig)
        assert subcommand.name
        assert subcommand.camel
        assert subcommand.description
        assert subcommand.commands



# Generated at 2022-06-13 21:00:40.490006
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from .base import each_setup_cfg_command
    from .base import each_setup_cfg_command_description
    from .base import each_setup_cfg_command_name

    base_command_name = 'make'
    setup_dir = os.path.join(os.path.realpath(__file__), '..', '..')
    setup_dir = os.path.realpath(setup_dir)
    command_count = 0
    for command in each_setup_cfg_command_name(setup_dir):
        if base_command_name not in command:
            continue
        command_count += 1
        print(command)
    assert command_count == 2

    command_count = 0
    for description in each_setup_cfg_command_description(setup_dir):
        print(description)

# Generated at 2022-06-13 21:00:51.685247
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from os.path import isdir, isfile, join
    from shutil import copy2, rmtree
    from tempfile import mkdtemp
    from unittest import TestCase

    test_dir = mkdtemp()
    src_dir = os.path.dirname(os.path.abspath(__file__))

    test_setup_py_path = join(test_dir, 'setup.py')
    copy2(join(src_dir, 'setup.py'), test_setup_py_path)

    test_setup_cfg_path = join(test_dir, 'setup.cfg')
    copy2(join(src_dir, 'setup.cfg'), test_setup_cfg_path)

    for config in each_sub_command_config(test_dir):
        assert isinstance(config, SetupCfgCommandConfig)

# Generated at 2022-06-13 21:01:03.405866
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # noinspection PyUnresolvedReferences
    from pathlib import Path
    # noinspection PyUnresolvedReferences
    from pep517 import _build
    from flutils.which import which
    from flutils.testing import capture_out

    name = 'flutils'
    setup_dir = os.path.join(
        Path(__file__).parent.parent.parent.absolute(), 'src', name
    )

    def _test_setup_cfg_command_config(sc: SetupCfgCommandConfig) -> None:
        print(
            'name: %r\ncamel: %r\n'
            'description: %s\ncommands: %s\n'
            % (sc.name, sc.camel, sc.description, sc.commands)
        )
        assert sc.name
        assert sc.c

# Generated at 2022-06-13 21:01:13.503752
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    import shutil
    import tempfile
    import unittest
    import unittest.mock
    from io import StringIO
    from typing import Dict
    from uuid import uuid4

    from flutils.pythondevutils import each_sub_command_config

    real_open = open

    class TestCase(unittest.TestCase):
        def setUp(self: 'TestCase') -> None:
            self.long_str = 'abcdefghijklmnopqurstuvwxyz0123456789'
            self.root_dir = tempfile.mkdtemp(suffix='-test-%s' % uuid4())
            os.mkdir(os.path.join(self.root_dir, 'test_proj1'))

# Generated at 2022-06-13 21:01:15.529274
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for _ in each_sub_command_config():
        pass

# Generated at 2022-06-13 21:01:21.194134
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config(setup_dir=os.path.dirname(__file__)):
        assert config.name != ''
        assert config.camel != ''
        assert config.description != ''
        assert config.commands != ()



# Generated at 2022-06-13 21:01:28.184263
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    try:
        import setup_commands  # noqa: F401
        from . import each_sub_command_config
    except (ModuleNotFoundError, ImportError) as ex:
        if '' not in ex.msg:
            raise
        from .setup_commands import each_sub_command_config
    for sub_command_config in each_sub_command_config():
        print(sub_command_config)

# Generated at 2022-06-13 21:01:35.539491
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    _setup_dir = os.path.dirname(__file__)
    result: List[Tuple[str, str, str, Tuple[str, ...]]] = []
    for c in each_sub_command_config(_setup_dir):
        result.append((c.name, c.camel, c.description, c.commands))
    assert result == [
        ('run_tests', 'RunTests', 'Run tests', ('pytest',)),
    ]

# Generated at 2022-06-13 21:01:48.459988
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # Test the 'each_sub_command_config' function.
    setup_cfg_path = os.path.join(os.path.dirname(__file__), 'setup.cfg')
    parser = ConfigParser()
    parser.read(setup_cfg_path)
    format_kwargs: Dict[str, str] = {
        'name': _get_name(parser, setup_cfg_path),
        'setup_dir': os.path.dirname(__file__),
        'home': os.path.expanduser('~')
    }
    for c in _each_setup_cfg_command(parser, format_kwargs):
        print(c)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:02:39.754643
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.mkutils.setup_commands import each_sub_command_config

    import os
    import os.path
    import sys
    import tempfile

    import pytest


# Generated at 2022-06-13 21:02:49.555415
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import json
    import sys

    import pkg_resources

    expected_config = pkg_resources.resource_filename(
        __name__,
        'data/sub_commands_config.json'
    )
    with open(expected_config, "rt") as f:
        expected_config = json.load(f)

    setup_dir = expected_config['setup_dir']
    setup_cfg_path = os.path.join(setup_dir, 'setup.cfg')
    parser = ConfigParser()
    parser.read(setup_cfg_path)

    format_kwargs = {}
    format_kwargs['name'] = _get_name(parser, setup_cfg_path)
    format_kwargs['setup_dir'] = setup_dir

# Generated at 2022-06-13 21:03:03.894758
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    class Result(NamedTuple):
        name: str
        camel: str
        description: str
        commands: Tuple[str, ...]


# Generated at 2022-06-13 21:03:12.608861
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config():
        assert isinstance(config, SetupCfgCommandConfig)
        assert isinstance(config.description, str)
        assert isinstance(config.name, str)
        assert isinstance(config.camel, str)
        assert isinstance(config.commands, list)
        assert len(config.commands) >= 1
        print(config.name)
        print(config.camel)
        print(config.description)
        print(config.commands)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:03:22.805149
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    path = os.path.dirname(__file__)
    path = os.path.dirname(path)
    path = os.path.dirname(path)
    path = os.path.dirname(path)
    path = os.path.join(path, 'setup.cfg')
    parser = ConfigParser()
    parser.read(path)
    assert parser is not None
    assert len(list(parser.sections())) == 1
    assert parser.has_section('metadata')
    assert parser.has_option('metadata', 'name')
    assert parser.get('metadata', 'name') == 'it-project-commons'
    #
    path = os.path.dirname(__file__)
    path = os.path.dirname(path)
    path = os.path.dirname(path)
    path

# Generated at 2022-06-13 21:03:25.101582
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import pprint
    pprint.pprint(list(each_sub_command_config()))

# Generated at 2022-06-13 21:03:28.922505
# Unit test for function each_sub_command_config

# Generated at 2022-06-13 21:03:36.555242
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    class FakeFrame:
        f_code = None

        def __init__(
                self,
                filename: str = 'setup.py',
                lineno: int = 0
        ):
            self.f_lineno = lineno
            self.f_globals = {'__file__': filename}
