

# Generated at 2022-06-13 20:53:59.327200
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # pylint: disable=unused-variable
    from pathlib import Path
    from unittest.mock import patch

    with patch('{}._prep_setup_dir'.format(__name__),
               new=lambda: str(Path(__file__).parent)):
        # print(Path(__file__).parent)
        for cmd in each_sub_command_config():
            print(cmd)
            # print()
            # print(cmd.camel)
            # print(cmd.description)
            # print(cmd.commands)

# Generated at 2022-06-13 20:54:07.053208
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    output = list(each_sub_command_config(setup_dir))
    assert output
    base_cmd = '{setup_dir}/setup.py'
    for config in output:
        cmd_name = config.name
        camel_name = config.camel
        description = config.description
        commands = config.commands
        assert isinstance(cmd_name, str)
        assert cmd_name
        assert isinstance(camel_name, str)
        assert camel_name
        assert camel_name == underscore_to_camel(cmd_name.replace('.', '_'))
        assert isinstance(description, str)
        assert description

# Generated at 2022-06-13 20:54:16.963449
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    generator = each_sub_command_config()
    config = next(generator)
    assert config.name == 'run_tests'
    assert config.camel == 'RunTests'
    assert config.description == 'Run the test suite'
    assert config.commands == ('pytest -vv', )

    config = next(generator)
    assert config.name == 'my_sub_command'
    assert config.camel == 'MySubCommand'
    assert config.description == 'My Sub Command'
    assert config.commands == ('echo Sub Command', )

# Generated at 2022-06-13 20:54:29.252664
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    this_file = os.path.realpath(__file__)
    this_dir = os.path.dirname(this_file)
    root_dir = os.path.realpath(os.path.join(this_dir, '..', '..'))
    this_name = os.path.basename(__file__)
    try:
        out = list(each_sub_command_config(root_dir))
    except:
        print('[%s] Problem with function each_sub_command_config.' % this_name)
        raise
    else:
        assert out


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:54:39.570278
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import unittest

    class TestEachSubCommandConfig(unittest.TestCase):

        def test_each(self):
            here = os.path.dirname(os.path.abspath(__file__))
            testdir = os.path.join(here, '.tests')
            for config in each_sub_command_config(testdir):
                self.assertIsInstance(config, SetupCfgCommandConfig)
                self.assertIsInstance(config.name, str)
                if config.camel:
                    self.assertTrue(config.camel.isidentifier())
                if config.description:
                    self.assertIsInstance(config.description, str)
                self.assertIsInstance(config.commands, tuple)
                for cmd in config.commands:
                    self.assertIsInstance(cmd, str)
                   

# Generated at 2022-06-13 20:54:47.138864
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.realpath(os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        '..'
    ))
    out = list(each_sub_command_config(setup_dir))
    assert len(out) > 0

if __name__ == "__main__":
    test_each_sub_command_config()

# Generated at 2022-06-13 20:54:51.066906
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    project_dir = os.path.join(os.path.dirname(__file__), 'fixtures', 'test_project')
    for cfg in each_sub_command_config(project_dir):
        print('cfg: %s' % cfg)



# Generated at 2022-06-13 20:54:56.807031
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from pathlib import Path

    from testfixtures import compare

    setup_dir = Path('~/code/flutils').expanduser()
    out = list(each_sub_command_config(setup_dir))
    compare(out, [
        SetupCfgCommandConfig(
            'test_test.test.test',
            'TestTestTest',
            'Runs tests',
            ('cd {setup_dir} && py.test --cov flutils {setup_dir} '
             '--cov-report term-missing',)
        ),
    ])

# Generated at 2022-06-13 20:55:05.021549
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import tempfile
    from pathlib import Path

    def get_setup_cfg_file(
            parent_dir: Union[os.PathLike, str],
            name: str = 'setup.cfg',
    ) -> Path:
        return Path(parent_dir) / name

    def get_setup_commands_file(
            parent_dir: Union[os.PathLike, str],
            name: str = 'setup_commands.cfg',
    ) -> Path:
        return Path(parent_dir) / name


# Generated at 2022-06-13 20:55:16.223165
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile

# Generated at 2022-06-13 20:55:30.072560
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for cmd in each_sub_command_config('tests/fixtures/wheel-dir'):
        assert cmd.name == 'spam-eggs'
        assert cmd.camel == 'SpamEggs'
        assert cmd.description == 'SPAM and EGGs'
        assert cmd.commands == ('echo "SPAM"', 'echo "EGGs"')



# Generated at 2022-06-13 20:55:40.561718
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # pylint: disable=import-outside-toplevel
    from flutils.setuputils.commands import each_sub_command_config
    # pylint: enable=import-outside-toplevel

    out = list(each_sub_command_config(setup_dir='../tests'))
    assert len(out) == 1
    assert out[0].camel == 'TestCommand'
    assert out[0].name == 'test'
    assert out[0].description ==\
        'This is for the testing of this module.'
    assert out[0].commands == (
        'echo Hello World',
    )

# Generated at 2022-06-13 20:55:46.667328
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from .testing_utils import change_cwd

    setup_cfg_commands = list(each_sub_command_config())
    assert(len(setup_cfg_commands) >= 10)

    with change_cwd(__file__):
        setup_cfg_commands = list(each_sub_command_config())
        assert(len(setup_cfg_commands) == 0)
        setup_cfg_commands = list(each_sub_command_config('.'))
        assert(len(setup_cfg_commands) == 0)

# Generated at 2022-06-13 20:55:58.636744
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from unittest import TestCase, main
    from flutils.pathutils import this_repo_dir

    setup_dir = os.path.join(this_repo_dir(), 'tests', 'setup')
    for cfg in each_sub_command_config(setup_dir):
        assert isinstance(cfg, SetupCfgCommandConfig)

    class SetupCfgCommandConfigTest(TestCase):
        def test_each_sub_command_config(self):
            self.assertEqual('flutils_dummy_package',
                             _get_name(ConfigParser(),
                                       os.path.join(setup_dir, 'setup.cfg')))

    main()



# Generated at 2022-06-13 20:56:12.104237
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.testingutils.mock import patch

    from flutils.setuputils import each_sub_command_config

    # None setup_dir
    with patch(
        'flutils.setuputils._prep_setup_dir', return_value='/tmp/'
    ) as mock_prep, patch(
        'flutils.setuputils.each_sub_command',
        return_value=[
            SetupCfgCommandConfig(
                name='clean',
                camel='Clean',
                description='Clean the project files.',
                commands=('rm -rfv',)
            )
        ]
    ) as mock_each_sub_cmd, patch(
        'flutils.setuputils._get_name', return_value='name'
    ):
        path = os.path.join('/tmp/', 'setup.cfg')

# Generated at 2022-06-13 20:56:18.814417
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def _test(
            setup_dir: Optional[Union[os.PathLike, str]] = None
    ) -> None:
        print('each_sub_command_config(setup_dir=%r)' % setup_dir)
        try:
            for cmd_cfg in each_sub_command_config(setup_dir):
                print('  %r' % cmd_cfg)
        except Exception as err:
            print(repr(err))
            raise

    def _test_each_sub_command_config():
        _test(None)
        _test(os.path.abspath(os.path.join(__file__, '..', '..', '..')))

# Generated at 2022-06-13 20:56:23.931108
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config."""
    from pprint import pformat
    from flutils.pathutils import get_script_dir
    from flutils.testutils import capture_stderr, capture_stdout
    dname = get_script_dir(__file__)
    with capture_stdout() as stdout, capture_stderr() as stderr:
        for i, config in enumerate(
                each_sub_command_config(os.path.join(dname, 'test_project'))
        ):
            assert isinstance(config, SetupCfgCommandConfig), \
                stdout.getvalue() + stderr.getvalue()
            commands = list(config.commands)

# Generated at 2022-06-13 20:56:28.319688
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    assert isinstance(each_sub_command_config, types.GeneratorType)
    assert isinstance(next(each_sub_command_config()), SetupCfgCommandConfig)

if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:56:34.717333
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    out = list(each_sub_command_config(os.path.dirname(__file__)))
    assert len(out) == 1
    item = out[0]
    assert item.name == 'hello_there'
    assert item.camel == 'HelloThere'
    assert item.description == 'Hello There!'
    assert len(item.commands) == 1

# Generated at 2022-06-13 20:56:45.911343
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import argparse
    import shutil
    import tempfile

    def test_setup_cfg_file(
            setup_cfg_path: str,
            expected_commands: Tuple[Tuple[str, str, ...], ...]
    ):
        parser = argparse.ArgumentParser()
        parser.add_argument('--setup-dir', default=None)
        args = parser.parse_args()
        for command in each_sub_command_config(args.setup_dir):
            command = cast(SetupCfgCommandConfig, command)
            assert command.name
            assert command.camel
            assert command.description
            assert command.commands
            for cmd in command.commands:
                assert ' ' not in cmd

# Generated at 2022-06-13 20:57:01.787953
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import flutils.tests.testutils
    import flutils.tests.testutils.env as env
    each_sub_cmd = each_sub_command_config(env.fixture_path('setup_dir'))
    fixture_path = env.fixture_path('setup_dir')
    fixture_path = os.path.normpath(fixture_path)
    setup_cfg_path = os.path.join(fixture_path, 'setup.cfg')
    name = _get_name(ConfigParser(), setup_cfg_path)

    actual = list(each_sub_cmd)


# Generated at 2022-06-13 20:57:11.936929
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import inspect
    import unittest.mock as mock
    # Find the "tests" directory
    test_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
    test_dir = os.path.abspath(test_dir)
    # Find the directory that contains the "tests" directory
    pkg_dir = os.path.dirname(test_dir)
    setup_dir = os.path.join(pkg_dir, 'setup.py')
    setup_cfg_path = os.path.join(pkg_dir, 'setup.cfg')
    setup_commands_cfg_path = os.path.join(pkg_dir, 'setup_commands.cfg')
    assert os.path.isfile(setup_dir) is True
    assert os.path.isf

# Generated at 2022-06-13 20:57:25.894454
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from pathlib import Path
    from tempfile import TemporaryDirectory
    from typing import Generator

    dir_path: Path = Path(__file__).parent.parent
    assert Path(
        dir_path.joinpath('setup.py')
    ).is_file() is True
    assert Path(
        dir_path.joinpath('setup_commands.cfg')
    ).is_file() is True

    def create_setup_cfg(setup_cfg_path: str, **kwargs) -> None:
        import textwrap

        parser = ConfigParser()
        parser.read(setup_cfg_path)
        metadata = parser.add_section('metadata')
        metadata.add_option('name', kwargs.get('name', 'my_name'))

        section = parser.add_section('setup.command.my_command')
        section

# Generated at 2022-06-13 20:57:36.209905
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import realpath

    setup_cfg_file: str = realpath(
        './tests/test_setup_cfg/setup.cfg',
        __file__
    )
    setup_cfg_dir: str = os.path.dirname(setup_cfg_file)
    commands = list(each_sub_command_config(setup_cfg_dir))
    assert len(commands) == 2

    # Test the first result.
    assert len(commands[0].commands) == 1
    actual = commands[0].commands[0]
    expected = '$HOME/bin/sphinx-build -b html -a ' \
               '-d $HOME/projects/python-flutils/docs/build/doctrees ' \
               '$HOME/projects/python-flutils/docs/source '

# Generated at 2022-06-13 20:57:44.966732
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil
    import textwrap

    cfg_template = textwrap.dedent("""\
        [metadata]
        name = {name}

        [setup.command.foo]
        Name = Foo
        description = Run Foo
        commands =
            echo foo
            echo {name}

        [setup.command.bar]
        # Name = Bar
        description = Run Bar
        commands =
            echo bar
            echo {name}

        [setup.command.baz]
        description = Run Baz
        commands =
            echo baz
            echo {name}
        """)

    dir_path = tempfile.mkdtemp()

# Generated at 2022-06-13 20:57:57.732522
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import os

    current_file_path = os.path.realpath(sys.argv[0])
    current_dir_path = os.path.dirname(current_file_path)
    project_dir_path = os.path.join(current_dir_path, os.pardir)

    sub_commands = tuple(each_sub_command_config(project_dir_path))
    assert len(sub_commands) == 3

    sub_cmd = sub_commands[0]
    assert sub_cmd.name == 'test'
    assert sub_cmd.camel == 'Test'
    assert sub_cmd.description == 'Test for setup_config.py'

# Generated at 2022-06-13 20:58:01.002393
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    path = os.path.dirname(__file__)
    for config in each_sub_command_config(path):
        assert isinstance(config, SetupCfgCommandConfig)

# Generated at 2022-06-13 20:58:10.221375
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import unittest

    class TestEachSubCommandConfig(unittest.TestCase):
        def test_each_sub_command_config(self):
            import pprint

            for config in each_sub_command_config(__file__):
                print()
                pprint.pprint(config)

    test_cases = (
        TestEachSubCommandConfig,
    )

    suite = unittest.TestSuite()
    for case in test_cases:
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(case))

    runner = unittest.TextTestRunner()
    runner.run(suite)

# Generated at 2022-06-13 20:58:18.571182
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.testutils import TempDirTestCase
    from .utilities import (
        capture_output,
    )

    class TestEachSubCommandConfig(TempDirTestCase):
        def test_no_setup_py(self):
            with self.assertRaises(SystemExit):
                with capture_output() as (out, err):
                    list(each_sub_command_config(self.path))
            self.assertEqual(out.getvalue(), '')
            self.assertTrue(err.getvalue().startswith('ERROR: '))
            self.assertTrue(
                'Unable to find the directory that contains the '
                "'setup.py' file."
                in err.getvalue()
            )


# Generated at 2022-06-13 20:58:31.248251
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config."""
    import unittest
    import os
    import tempfile

    class Test_each_sub_command_config(unittest.TestCase):
        """Unit test class for function each_sub_command_config."""

        def setUp(self: 'Test_each_sub_command_config'):
            self.tempdir = tempfile.TemporaryDirectory()
            tempdir = self.tempdir.name
            self.curdir = os.getcwd()
            os.chdir(tempdir)

        def tearDown(self: 'Test_each_sub_command_config'):
            os.chdir(self.curdir)
            self.tempdir.cleanup()


# Generated at 2022-06-13 20:58:56.335195
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.systemutils import get_temp_dir
    from pathlib import (
        Path,
    )
    from shutil import (
        copy,
    )
    from tempfile import (
        gettempdir,
    )
    import PySimpleGUI as sg
    sg.ChangeLookAndFeel('DarkAmber')
    sg.SetOptions(element_padding=(0, 0))
    tmpdir = get_temp_dir()
    srcdir = Path(__file__).parent
    srcdir = srcdir.joinpath('setup.cfg')
    dstdir = Path(tmpdir).joinpath('setup.cfg')
    copy(str(srcdir), str(dstdir))
    srcdir = Path(__file__).parent
    srcdir = srcdir.joinpath('setup_commands.cfg')
    dst

# Generated at 2022-06-13 20:59:07.286153
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from pathlib import Path
    from sys import modules

    import flutils.setup_utils

    # noinspection PyProtectedMember
    def _test(
            setup_dir: Union[os.PathLike, str],
            expected: List[SetupCfgCommandConfig]
    ) -> List[SetupCfgCommandConfig]:
        actual: List[SetupCfgCommandConfig] = []
        mods = list(modules.values())
        for config in flutils.setup_utils.each_sub_command_config(setup_dir):
            actual.append(config)
        assert actual == expected
        mods = list(modules.values())
        assert sorted(mods) == sorted(modules.values())
        return actual

    # Empty
    setup_dir = str(Path('tests/data/setup_empty_setup_dir'))
    out = _test

# Generated at 2022-06-13 20:59:15.574953
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config('/Applications/Google Chrome.app'):
        assert config.name == 'unittest_test'
        assert config.camel == 'UnittestTest'
        assert config.description == (
            'Executes the unit tests within the ``src/unittest_test'
            '`` directory.'
        )
        assert config.commands[0] == 'pip install -r dev-requirements.txt'
        assert config.commands[1] == (
            'python -m unittest discover --start-directory src/'
            'unittest_test --pattern "*_test.py" --verbose'
        )

# Generated at 2022-06-13 20:59:27.346392
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import unittest
    import os.path as osp
    import tempfile

    class TestEachSubCommandConfig(unittest.TestCase):
        def setUp(self):
            self.temp_dir = tempfile.mkdtemp()

        def tearDown(self):
            import shutil
            shutil.rmtree(self.temp_dir)

        def _create_setup_cfg(self, data=None):
            import os

# Generated at 2022-06-13 20:59:36.731947
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.dirname(os.path.abspath(__file__))
    setup_dir = os.path.dirname(setup_dir)
    setup_dir = os.path.dirname(setup_dir)
    setup_dir = os.path.dirname(setup_dir)
    setup_dir = os.path.dirname(setup_dir)
    for cmd in each_sub_command_config(setup_dir):
        print(cmd)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:59:47.664511
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import unittest

    class TestEachCommand(unittest.TestCase):
        def test(self):
            import tempfile
            import pathlib
            import shutil
            import subprocess

            tmp = tempfile.mkdtemp()
            tmp = pathlib.Path(tmp)

# Generated at 2022-06-13 21:00:00.456493
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.testutils import _prep_test_dir
    _prep_test_dir()
    from . import (
        _test_setup_commands_cfg,
        _test_setup_cfg
    )
    from pkg_resources import resource_string
    from io import StringIO
    from os.path import realpath

    for _ in range(2):
        test_dir = Resource(
            path=_prep_test_dir(),
            name='test_dir',
            mode='wb'
        )
        with test_dir:
            test_dir.write_resource_string(
                _test_setup_commands_cfg,
                'setup_commands.cfg'
            )
            test_dir.write_resource_string(_test_setup_cfg, 'setup.cfg')

        # First time, ``setup

# Generated at 2022-06-13 21:00:12.571743
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with open('build/setup_commands.cfg', 'w+t') as f:
        f.write("""\
[setup.command.test.unit]
name = {name}
command = python setup.py test

[setup.command.test.pylint]
name = test-pylint
commands =
    python -m pip install --upgrade  pylint
    python -m pylint "{setup_dir}"
""")
    for cfg in each_sub_command_config('build'):
        print(cfg)
        assert len(cfg.commands) != 0

if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:00:25.987497
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # noinspection PyProtectedMember
    import sys
    import os
    import site
    import shutil
    import tempfile
    # noinspection PyProtectedMember
    from flutils import pathutils

    # Create a temporary directory
    tmp = tempfile.gettempdir()
    output_path = os.path.join(tmp, 'test_setup_cfg')
    if os.path.exists(output_path):
        if os.path.isdir(output_path):
            shutil.rmtree(output_path)
        else:
            os.remove(output_path)
    pathutils.create_dirs(output_path)

    # Create setup.cfg
    path = os.path.abspath(os.path.join(output_path, 'setup.cfg'))

# Generated at 2022-06-13 21:00:37.811496
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import unittest

    @classmethod
    def get_suite(cls):
        class SetupCommandFinderTest(unittest.TestCase):
            def test_each_sub_command_config(self):
                configs: List[SetupCfgCommandConfig] = []
                for config in each_sub_command_config():
                    configs.append(config)

                cmds = [
                    'test', 'upload', 'register', 'sdist', 'install',
                    'bdist_wheel', 'uninstall', 'tag',
                    'test_manifest', 'test_pep8', 'test_flake8',
                    'test_pydocstyle', 'test_isort', 'test_mypy',
                    'test_unittest', 'test_pylint'
                ]

# Generated at 2022-06-13 21:01:12.581960
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import shutil
    from tempfile import TemporaryDirectory

    from conftest import TestConfig

    tmpdir = TemporaryDirectory()
    tmpdir.cleanup()
    tmpdir = tmpdir.name

# Generated at 2022-06-13 21:01:15.572765
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    config = list(each_sub_command_config())
    assert len(config) > 0
    assert isinstance(config, list)
    assert isinstance(config[0], SetupCfgCommandConfig)

# Generated at 2022-06-13 21:01:23.047135
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.realpath(
        os.path.join(os.path.dirname(__file__), '..', '..')
    )
    # print(setup_dir)

    _validate_setup_dir(setup_dir)

    setup_cfg_path = os.path.join(setup_dir, 'setup.cfg')
    parser = ConfigParser()
    parser.read(setup_cfg_path)

    name = _get_name(parser, setup_cfg_path)
    # print(name)

    format_kwargs = {
        'setup_dir': '.'.join(setup_cfg_path.split('.')[:-1]),
        'home': os.path.expanduser('~'),
        'name': name,
    }

# Generated at 2022-06-13 21:01:35.789003
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # pylint: disable=unused-variable
    from unittest.mock import Mock
    from pkg_resources import Requirement
    from importlib import import_module
    from unittest import TestCase
    from os.path import join
    from shutil import rmtree
    from tempfile import mkdtemp
    from typing import List

    class TestConfig(NamedTuple):
        dirname: str
        installed_reqs: List[str]
        test_commands: List[str]


# Generated at 2022-06-13 21:01:41.860172
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # _prep_setup_dir

    # _get_name

    # _each_setup_cfg_command

    # each_sub_command_config
    for cmd in each_sub_command_config():
        print(cmd.__dict__)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:01:54.648587
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.testutils import (
        dot_testing_path,
        make_setup_cfg,
        make_setup_py,
    )
    from subprocess import (
        check_output,
        DEVNULL,
        STDOUT,
    )

    setup_py_contents = """\
"""

    setup_cfg_contents = """[metadata]
name = flutils.testutils
version = 0.1.0

[options]
packages = find:

[files]
extra_files = 1
    """


# Generated at 2022-06-13 21:02:06.253765
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.system import in_directory  # noqa
    with in_directory(__file__):
        assert tuple(each_sub_command_config()) == (
            SetupCfgCommandConfig(
                name='test.commands',
                camel='TestCommands',
                description='Test commands.',
                commands=(
                    'test_command_one',
                    'test_command_two',
                    'test_command_three'
                )
            ),
            SetupCfgCommandConfig(
                name='test.commands.two',
                camel='TestCommandsTwo',
                description='Test commands 2.',
                commands=(
                    'test_command_2_one',
                    'test_command_2_two',
                    'test_command_2_three'
                )
            )
        )
    #

# Generated at 2022-06-13 21:02:15.069913
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from pprint import pprint
    from flutils.custom_types import PathLike

    def each_setup_cfg_command_config(
            setup_dir: Optional[Union[PathLike, str]] = None
    ) -> Generator[SetupCfgCommandConfig, None, None]:
        for config in each_sub_command_config(setup_dir):
            yield config

    setup_dir = os.path.join(
        os.path.dirname(__file__),
        'setup_cfg_files'
    )


# Generated at 2022-06-13 21:02:26.409934
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import subprocess
    import pytest

    with subprocess.Popen(
            ['git', 'init', 'test_repo'],
            stdout=subprocess.PIPE,
            universal_newlines=True
    ) as proc:
        stdout, stderr = proc.communicate()
        p = pytest.approx(0, abs=1.0)
        assert proc.returncode == p

# Generated at 2022-06-13 21:02:38.465902
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    configs = list(each_sub_command_config('build/flutils/'))
    assert len(configs) == 3
    assert configs[0].name == 'test'
    assert configs[0].camel == 'Test'
    assert configs[0].description == 'Runs the unit tests.'
    assert configs[0].commands == (
        'python -m unittest discover',
        'python -m unittest discover -s tests -p "*_test.py"',
    )
    assert configs[1].name == 'clean'
    assert configs[1].camel == 'Clean'
    assert configs[1].description == 'Cleans the project.'
    assert configs[1].commands == ('python setup.py clean',)
    assert configs[2].name == 'build'

# Generated at 2022-06-13 21:03:13.009188
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import inspect
    import itertools
    import sys

    def _get_this_dir(
            file: str
    ) -> str:
        this_dir = os.path.dirname(os.path.abspath(file))
        assert os.path.isdir(this_dir)
        return this_dir

    from flutils.pathutils import cwd_in_path

    this_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, this_dir)
    this_dir = _get_this_dir(__file__)
    assert cwd_in_path(this_dir) is True


# Generated at 2022-06-13 21:03:20.731319
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # pylint: disable=protected-access
    dir_path = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )
    dir_path = os.path.join(dir_path, 'examples')
    for out in each_sub_command_config(dir_path):
        print(out)


if __name__ == "__main__":  # pragma: no cover
    test_each_sub_command_config()

# Generated at 2022-06-13 21:03:35.161168
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import pathlib

    # For some reason, mypy doesn't recognize
    # flutils.setuputils.each_sub_command_config() when called within
    # a test function.  Even when the test function is within this
    # module.  So the following line is needed to tell mypy the
    # expression is a generator.
    each_sub_command_config()

    for config in each_sub_command_config():
        print(config, file=sys.stderr)

    # Test a path that does NOT exist
    with pytest.raises(FileNotFoundError):
        print(
            list(each_sub_command_config(setup_dir='/foo/bar/baz')),
            file=sys.stderr
        )

    # Test a path that is not a directory

# Generated at 2022-06-13 21:03:39.845917
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    try:
        list(each_sub_command_config())
        assert False
    except FileNotFoundError:
        assert True
    if os.path.isdir('test/test_project'):
        list(each_sub_command_config('test/test_project'))

