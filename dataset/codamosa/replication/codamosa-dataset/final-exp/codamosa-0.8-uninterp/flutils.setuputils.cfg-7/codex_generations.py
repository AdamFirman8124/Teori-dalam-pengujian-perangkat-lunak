

# Generated at 2022-06-13 20:54:05.508757
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    tests = [
        {
            'name': 'Each Sub-Command Config',
            'setup_dir': '../../fl_setup_helper'
        },
        {
            'name': 'No Setup.py File',
            'setup_dir': '../../flutils'
        },
        {
            'name': 'No Setup.cfg File',
            'setup_dir': '../..'
        },
    ]
    for test in tests:
        if test['name'] == 'Each Sub-Command Config':
            try:
                list(each_sub_command_config(test['setup_dir']))
            except Exception as e:
                print(test['name'])
                raise e

# Generated at 2022-06-13 20:54:13.685543
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def _assert_each_sub_command_config(path: Union[os.PathLike, str]):
        # Call function to be tested
        configs = list(
            each_sub_command_config(setup_dir=path)
        )
        # Assert
        assert configs

    _assert_each_sub_command_config('/Users/mark/Projects/flutils')
    _assert_each_sub_command_config('/Users/mark/Projects/setup_tests')

# Generated at 2022-06-13 20:54:17.686702
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pytestutils import execute_doctest
    execute_doctest(each_sub_command_config.__module__)

# Run it through the test harness
test_each_sub_command_config()

# Generated at 2022-06-13 20:54:31.158958
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import unittest as ut
    import os

    @ut.skipUnless(
        os.path.exists('../tests/resources/git-repo'),
        'Test resources not found'
    )
    class TestEachSubCommandConfig(ut.TestCase):
        def test_normal(self):
            import pathlib as pl

            setup_dir = pl.Path('../tests/resources/git-repo')
            for sub_command in each_sub_command_config(setup_dir):
                print(sub_command)
                self.assertTrue(
                    sub_command.name.startswith('gitrepo'),
                    msg='The sub command\'s name should start with '
                        + '\'gitrepo\', not %r.' % sub_command.name
                )
                # self.assertTrue(
                #     sub

# Generated at 2022-06-13 20:54:40.436678
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_cfg_path = 'tests/files/setup_commands.cfg'
    parser = ConfigParser()
    parser.read(setup_cfg_path)
    format_kwargs = {
        'name': 'flutils_test',
        'setup_dir': os.path.abspath(os.path.dirname(setup_cfg_path)),
        'home': os.path.expanduser('~')
    }
    sub_commands = list(_each_setup_cfg_command(parser, format_kwargs))
    assert len(sub_commands) == 1
    setup_cfg_sub_command = sub_commands[0]
    assert setup_cfg_sub_command.name == 'sub_command_name'
    assert setup_cfg_sub_command.camel == 'SubCommandName'
    assert setup

# Generated at 2022-06-13 20:54:45.235956
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import flutils.setup_utils
    for config in each_sub_command_config(
        flutils.setup_utils.__path__[0]
    ):
        print(config)


if __name__ == '__main__':
    test_each_sub_command_config()
    sys.exit(0)

# Generated at 2022-06-13 20:54:50.454478
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import os.path

    basedir = os.path.dirname(os.path.dirname(os.path.dirname(
        sys.modules[__name__].__file__)
    ))
    assert each_sub_command_config(os.path.join(basedir, 'setup.py'))

# Generated at 2022-06-13 20:54:58.407425
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    tests = [
        ('flutils', 'commands'),
        ('minesweeper', 'commands'),
    ]
    for test in tests:
        project_dir = os.path.join(os.path.dirname(__file__), '..', '..',
                                   'flutils', test[0])
        dest_dir = os.path.join(project_dir, test[1])
        if os.path.exists(dest_dir):
            shutil.rmtree(dest_dir)
        os.makedirs(dest_dir)
        f = open(os.path.join(dest_dir, test[0] + "_commands.py"), 'w')

# Generated at 2022-06-13 20:55:13.354121
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    out = list(each_sub_command_config())
    assert out


if __name__ == '__main__':
    import sys
    import json
    import argparse
    from pathlib import Path
    from typing import TYPE_CHECKING
    if TYPE_CHECKING:
        from typing import Callable, Any
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--setup-dir',
        metavar='DIR',
        type=Path,
        help="The path to the directory that contains the project's "
        "'setup.py' file."
    )
    parser.add_argument(
        '-j', '--json',
        dest='json_out',
        action='store_true',
        help='Print the output as JSON.'
    )
    kwargs

# Generated at 2022-06-13 20:55:20.995312
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import get_parent_dir
    from flutils.objutils import dr_repr

    here = os.path.dirname(os.path.realpath(__file__))
    setup_dir = get_parent_dir(here)
    for scc in each_sub_command_config(setup_dir):
        print(dr_repr(scc))


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:55:35.840188
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    import random
    import string
    import tempfile

    def _generate_command_block(
            name: str,
            fp: TextIO
    ) -> None:
        command_idx = random.randint(1, 3)
        command_line_idx = random.randint(1, 3)
        fp.write('[setup.command.%s]\n' % name)

# Generated at 2022-06-13 20:55:44.339911
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def _find_setup_commands_cfg(setup_dir: str) -> None:
        """Finds the ``setup_commands.cfg`` file. """
        with argparse.ArgumentParser() as parser:
            parser.add_argument('setup_dir',
                                help='The directory that contains the '
                                     'setup.py file.')
            args = parser.parse_args()
            for config in each_sub_command_config(args.setup_dir):
                print('\n%r' % config)

    package_dir = Path(__file__).parent
    testdir = package_dir.joinpath('testdir')

    # Create a temporary working directory.
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)

        # Move the testdir to the temporary directory.


# Generated at 2022-06-13 20:55:59.038793
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    expected = (
        SetupCfgCommandConfig('command1', 'Command1', 'Description', ()),
        SetupCfgCommandConfig('command2', 'Command2', '', ()),
        SetupCfgCommandConfig('command3', '', '', ()),
        SetupCfgCommandConfig('command4', '', '', ()),
        SetupCfgCommandConfig('name4', 'Name4', '', ()),
    )

    with patch('os.path.isfile') as mock_isfile, \
            patch('os.path.expanduser') as mock_expanduser, \
            patch('os.path.join'), \
            patch('configparser.ConfigParser.read'):
        mock_isfile.return_value = True
        mock_expanduser.return_value = '/home/user'

# Generated at 2022-06-13 20:56:08.083163
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import logging

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger('test_each_sub_command_config')
    logger.info('started')

    setup_dir = os.path.realpath(
        os.path.join(
            os.path.dirname(__file__),
            '..',
            '..'
        )
    )

    for command in each_sub_command_config(setup_dir):
        logger.info(command)

    logger.info('finished')


# Generated at 2022-06-13 20:56:17.689327
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from unittest.mock import patch
    from pathlib import Path

    path = Path(__file__).parent / 'data' / 'setup_commands.cfg'
    with patch.object(ConfigParser, 'read', lambda self, path: self.read_file(open(path))):
        conf = list(each_sub_command_config(path.parent))

    assert len(conf) == 1
    c = conf[0]
    assert c.name == 'test'
    assert c.camel == 'Test'
    assert c.description == 'Test the application'
    assert c.commands == ('echo testing',)

# Generated at 2022-06-13 20:56:26.972725
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import re
    import unittest

    def get_pattern(s: str) -> str:
        return r'\b{0}\b'.format(s)

    class TestEachSubCommandConfig(unittest.TestCase):
        def test_finds_commands(self):
            commands = list(each_sub_command_config())
            commands.sort(key=lambda x: x.name)
            names = [_.name for _ in commands]
            names = '|'.join(names)
            self.assertRegex(names, get_pattern('command1'))
            self.assertRegex(names, get_pattern('command2'))

        def test_finds_commands_in_setup_commands_cfg(self):
            commands = list(each_sub_command_config())

# Generated at 2022-06-13 20:56:36.995188
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import unittest

    class EachSubCommandConfigTestCase(unittest.TestCase):
        def setUp(self):
            self.setup_dir = os.path.join(
                os.path.dirname(__file__),
                'resources',
                'test_each_sub_command_config'
            )

        def test_each_sub_command_config(self):
            configs = list(each_sub_command_config(self.setup_dir))
            self.assertEqual(len(configs), 5)
            for idx, config in enumerate(configs):
                self.assertEqual(config.name, config.camel)
                self.assertEqual(config.name, config.camel.lower())
                self.assertEqual(config.description, '-')


# Generated at 2022-06-13 20:56:45.852923
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Tests the function ``each_sub_command_config``."""
    this_dir = os.path.abspath(os.path.dirname(__file__))
    setup_dir = os.path.join(this_dir, 'data', 'setup_commands')
    for config in each_sub_command_config(setup_dir):
        print(config)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:56:57.636588
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import subprocess
    import tempfile
    import shutil
    import textwrap
    import contextlib

    command_count = 0
    expected_count = 0

    @contextlib.contextmanager
    def temp_dir():
        name = tempfile.mkdtemp()
        try:
            yield name
        finally:
            shutil.rmtree(name)

    def _write_file(
            path: str,
            contents: str,
            encoding='utf-8'
    ) -> None:
        with open(path, 'w', encoding=encoding) as fh:
            fh.write(contents)


# Generated at 2022-06-13 20:57:01.192692
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for cfg in each_sub_command_config():
        print(cfg)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:57:13.379441
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    os.environ['HOME'] = os.path.dirname(__file__)
    for cfg in each_sub_command_config():
        print(cfg)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:57:26.902664
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import unittest.mock
    import sys

    setup_dir = os.path.dirname(__file__)
    if not setup_dir:
        setup_dir = os.getcwd()
    expected = SetupCfgCommandConfig(
        name='setup.command.sub-command',
        camel='SetupCommandSubCommand',
        description='Foo.',
        commands=('echo',)
    )
    def sep(*args):
        return os.path.sep.join(args)
    with unittest.mock.patch.object(sys, 'argv', ['', '']):
        for cfg in each_sub_command_config(setup_dir):
            assert cfg == expected


if __name__ == '__main__':
    each_sub_command_config()

# Generated at 2022-06-13 20:57:35.546174
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import doctest
    file_path: str = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'test_each_sub_command_config.rst'
    )
    with open(file_path, 'r') as file:
        doctest.testmod(
            module=None,
            optionflags=doctest.ELLIPSIS,
            extraglobs={'lines': file.read()},
        )



# Generated at 2022-06-13 20:57:44.683684
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import inspect
    import pprint

    setup_dirs = (
        os.path.join(
            os.path.dirname(inspect.getfile(inspect.currentframe())),
            '..', '..', '..', '..', '..', 'docs', 'source', 'conf.py'
        ),
        os.path.join(
            os.path.dirname(inspect.getfile(inspect.currentframe())),
            '..', '..', '..', '..', '..', 'docs', 'source', 'conf.py'
        )
    )

    for setup_dir in setup_dirs:
        print('%r' % setup_dir)

# Generated at 2022-06-13 20:57:56.983835
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    tmp = tempfile.TemporaryDirectory()
    path = os.path.join(tmp.name, 'setup.py')
    with open(path, 'w') as fp:
        fp.write('\n')
    path = os.path.join(tmp.name, 'setup.cfg')

# Generated at 2022-06-13 20:58:08.472451
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    import tempfile

    def write_file(path: str, lines: List[str]) -> None:
        with open(path, 'w') as f:
            for line in lines:
                f.write('%s\n' % line)

    def get_configs(setup_dir: str) -> List[SetupCfgCommandConfig]:
        return [x for x in each_sub_command_config(setup_dir)]

    def check_configs(expected: List[SetupCfgCommandConfig], got: List[SetupCfgCommandConfig]) -> None:
        assert len(expected) == len(got)
        for expected, got in zip(expected, got):
            assert expected.camel == got.camel
            assert expected.name == got.name
            assert expected.description == got.description
            assert expected.comm

# Generated at 2022-06-13 20:58:13.703241
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # Test function
    next(each_sub_command_config(os.path.abspath('./sample')))
    # Test function w/o arguments
    next(each_sub_command_config())


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:58:27.099554
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # fmt: off
    # Testing against a "real" project
    commands = tuple(each_sub_command_config())
    assert commands[0] == SetupCfgCommandConfig(
        name='config.init',
        camel='ConfigInit',
        description='Initializes the config file.',
        commands=('../flcfg/entry.py init',)
    )
    assert commands[1] == SetupCfgCommandConfig(
        name='config.show',
        camel='ConfigShow',
        description='Shows the config file.',
        commands=('../flcfg/entry.py show',)
    )
    # Testing against a "fake" project
    d, fn = tempfile.mkstemp()
    os.close(d)

    def _cleanup():
        os.remove(fn)


# Generated at 2022-06-13 20:58:41.842404
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os.path
    import pathlib
    import tempfile

    setup_dir = tempfile.TemporaryDirectory()
    setup_dir.cleanup()
    setup_dir = setup_dir.name

    setup_py_path = os.path.join(setup_dir, 'setup.py')
    with open(setup_py_path, 'w') as setup_py_file:
        setup_py_file.write("""
import setuptools
setuptools.setup(
    name="my_proj",
    version="0.0.1",
    packages=setuptools.find_packages(),
)
""")

    setup_cfg_path = os.path.join(setup_dir, 'setup.cfg')
    with open(setup_cfg_path, 'w') as setup_cfg_file:
        setup_

# Generated at 2022-06-13 20:58:44.719908
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    os.environ['HOME'] = '/home/testuser'
    for command in each_sub_command_config('.'):
        assert True

# Generated at 2022-06-13 20:59:01.795356
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for cmd in each_sub_command_config(setup_dir=os.getcwd()):
        assert cmd
        assert cmd.name
        assert cmd.camel
        assert cmd.description
        assert cmd.commands


if __name__ == '__main__':
    for cmd in each_sub_command_config(setup_dir=os.getcwd()):
        print(cmd)

# Generated at 2022-06-13 20:59:14.414074
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from os.path import dirname, realpath, join
    import sys
    import unittest

    class TestCase(unittest.TestCase):

        def test_each_sub_command_config_no_sub_command_options(self):
            here = realpath(dirname(__file__))
            setup_dir = join(here, 'test_no_sub_command_options')
            sub_commands = list(each_sub_command_config(setup_dir))
            self.assertEqual(len(sub_commands), 0)

        def test_each_sub_command_config_sub_command_options(self):

            # Setup
            here = realpath(dirname(__file__))
            setup_dir = join(here, 'test_sub_command_options')
            # Exercise
            sub_comm

# Generated at 2022-06-13 20:59:26.616240
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Test function each_sub_command_config()."""
    _test_setup_dir = os.path.join(
        os.path.dirname(__file__),
        'data',
        'test_each_sub_command_config'
    )
    _test_setup_dir = os.path.realpath(_test_setup_dir)
    for sub_command_config in each_sub_command_config(_test_setup_dir):
        name = sub_command_config.name
        assert name in (
            'test_command',
            'test_command.one',
            'test_command.two',
            'test_command.three'
        )
        if name == 'test_command.one':
            assert sub_command_config.camel == 'TestCommandOne'

# Generated at 2022-06-13 20:59:27.708561
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    return

# Generated at 2022-06-13 20:59:33.094092
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    configs = list(each_sub_command_config(setup_dir='../..'))
    assert len(configs) == 7
    configs = list(each_sub_command_config(setup_dir=__file__))
    assert len(configs) == 0

# Generated at 2022-06-13 20:59:43.397215
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    path = os.path.realpath(
        os.path.join(
            os.path.dirname(__file__), '..', '..', '..', '..', '..', 'setup.py'
        )
    )
    path = os.path.dirname(path)
    out = list(each_sub_command_config(path))
    assert len(out) == 15
    assert out[0] == \
        SetupCfgCommandConfig(
            name='test',
            camel='Test',
            description='Runs tests.',
            commands=(
                'tox',
            )
        )

# Generated at 2022-06-13 20:59:53.681120
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from os import linesep
    from tempfile import TemporaryDirectory

    setup_dir: str
    msg: str
    with TemporaryDirectory() as tmpdir:
        setup_dir = str(tmpdir)

        # No setup.cfg file.
        msg = (
            "The given 'setup_dir' of %r does NOT contain a setup.cfg file."
            % setup_dir
        )
        with pytest.raises(FileNotFoundError) as exinfo:
            next(each_sub_command_config(setup_dir))
        assert msg == str(exinfo.value)

        # Empty setup.cfg file.
        with open(os.path.join(setup_dir, 'setup.cfg'), 'w') as fp:
            pass

# Generated at 2022-06-13 21:00:03.982785
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def _assert(
            expected: SetupCfgCommandConfig,
            found: SetupCfgCommandConfig
    ) -> None:
        if expected != found:
            msg = (
                "The expected data of %r\n"
                "does not match the actual data of %r"
            )
            raise AssertionError(msg % (expected, found))

    import inspect
    from flutils.pathutils import get_sub_path
    from flutils.strutils import dunder
    from flutils.sysutils import get_script_name

    this_path = os.path.abspath(inspect.getfile(inspect.currentframe()))
    setup_path = os.path.join(this_path, '..', 'setup.py')
    setup_dir = os.path.dirname(setup_path)
    cmd

# Generated at 2022-06-13 21:00:16.283090
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.realpath(
        os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            '..', '..', '..', '..', 'flutils'
        )
    )
    sc = None
    for sc in each_sub_command_config(setup_dir):
        pass
    assert sc is not None
    assert sc.name == 'fmt.validate'
    assert sc.camel == 'FmtValidate'
    assert sc.description == 'Validates Python files using black and the ' \
                             'pre-commit hooks.'
    assert sc.commands == (
        'pip install --quiet --upgrade -e .[fmt]',
        'fmt.validate --assert'
    )

# Generated at 2022-06-13 21:00:19.155286
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.join(
        os.path.expanduser('~'), '.flutils', 'flutils'
    )
    for _ in each_sub_command_config(setup_dir):
        pass

# Generated at 2022-06-13 21:00:26.875111
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    list(each_sub_command_config())

# Generated at 2022-06-13 21:00:29.857485
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    tasks = list(each_sub_command_config(setup_dir=os.path.dirname(__file__)))
    assert len(tasks) > 1

# Generated at 2022-06-13 21:00:41.668815
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from unittest.mock import patch
    from unittest.mock import Mock

    # Test the setup.cfg file
    config = ConfigParser()
    config.add_section('metadata')
    config.set('metadata', 'name', 'flutils')
    config.add_section('setup.command.flutils')
    config.set('setup.command.flutils', 'description',
               'A list of "setup.py" commands to run...')
    config.set('setup.command.flutils', 'commands',
               'python3 -m flutils.setup_commands.commands.run_tests '
               'python3 -m flutils.setup_commands.commands.run_black')
    out = []

# Generated at 2022-06-13 21:00:52.174821
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    configs = []
    for config in each_sub_command_config(
            os.path.expanduser('~/dev/git/flutils')
    ):
        configs.append(config)
    assert len(configs) == 9
    config = configs[0]
    assert config.name == 'example'
    assert config.camel == 'Example'
    assert config.description == 'Run the default example command.'
    assert config.commands == ('',)

    config = configs[1]
    assert config.name == 'example.hello'
    assert config.camel == 'Hello'
    assert config.description == 'Run the example hello command.'
    assert config.commands == ('python hello.py',)

    config = configs[2]
    assert config.name == 'example.world'

# Generated at 2022-06-13 21:01:03.750593
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import io
    import tempfile
    import shutil
    import unittest

    class TestEachSubCommandConfig(unittest.TestCase):

        def setUp(self):
            self.cwd = os.getcwd()
            self.tmpdir = tempfile.mkdtemp()
            os.chdir(self.tmpdir)

        def tearDown(self):
            os.chdir(self.cwd)
            shutil.rmtree(self.tmpdir)

        def test_each_sub_command_config(self):
            name = 'test_flutils_newproject'
            setup_dir = os.path.join(self.tmpdir, name)
            os.mkdir(setup_dir)

            setup_cfg = os.path.join(setup_dir, 'setup.cfg')

# Generated at 2022-06-13 21:01:14.205506
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from textwrap import dedent
    from subprocess import check_output as run

    from flutils.systemutils import (
        cleanup_dir,
        create_dir,
        create_file,
        rm_file,
        touch_file,
    )

    setup_dir_path = '/tmp/test-flutils-setupcfg'
    setup_dir_path = cleanup_dir(setup_dir_path)
    setup_dir_path = create_dir(setup_dir_path)

    setup_path = os.path.join(setup_dir_path, 'setup.py')
    touch_file(setup_path)

    setup_cfg_path = os.path.join(setup_dir_path, 'setup.cfg')

# Generated at 2022-06-13 21:01:19.204815
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for sub_command in each_sub_command_config(os.path.dirname(__file__)):
        assert sub_command.name
        assert sub_command.camel
        assert sub_command.description
        assert sub_command.commands

# Generated at 2022-06-13 21:01:31.768839
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    i = 0
    for command_cfg in each_sub_command_config():
        if i == 0:
            assert command_cfg.name == 'my-package'
            assert command_cfg.camel == 'MyPackage'
            assert command_cfg.description == 'The MyPackage package.'
            assert command_cfg.commands == (
                'python setup.py sdist bdist_wheel'
            )
        elif i == 1:
            assert command_cfg.name == 'my-package.register'
            assert command_cfg.camel == 'Register'
            assert command_cfg.description == 'Register MyPackage.'
            assert command_cfg.commands == ('python setup.py register',)
        elif i == 2:
            assert command_cfg.name == 'my-package.upload'
            assert command_cfg.camel

# Generated at 2022-06-13 21:01:41.257071
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Tests the ``each_sub_command_config`` function."""
    out = list(each_sub_command_config('flproject'))
    assert out == [
        SetupCfgCommandConfig(
            'test',
            'Test',
            'Run unit tests',
            (
                'flutils test --verbose',
                'py.test --verbose',
            )
        ),
        SetupCfgCommandConfig(
            'validate',
            'Validate',
            'Validate the code',
            (
                'flake8 flproject/ flutils/',
                'mypy --ignore-missing-imports flproject/ '
                'flutils/',
                'pydocstyle flproject/ flutils/',
            )
        ),
    ]



# Generated at 2022-06-13 21:01:50.275735
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Test: function each_sub_command_config."""
    import sys
    import logging
    sys.path.append('.')
    from flutils.get_user_info import each_sub_command_config as e

    msg = 'Unit test'
    logger = logging.getLogger(msg)
    try:
        count = 0
        for ee in e():
            count = count + 1
            logger.info(ee)
        logger.info(count)
    except BaseException:
        logger.exception(msg)
        raise

# Generated at 2022-06-13 21:02:11.501463
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from pprint import pprint
    import tempfile


# Generated at 2022-06-13 21:02:16.851111
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for sc in each_sub_command_config(setup_dir='~/Code/Python/flutils'):
        print(sc)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:02:22.312320
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config('./test/test_func'):
        assert config.name == 'test_func.test_sub_command'
        assert config.camel == 'TestFuncTestSubCommand'
        assert config.description == ''
        assert config.commands == ('echo test_sub_command',)

# Generated at 2022-06-13 21:02:29.556008
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    test_dir = os.path.dirname(__file__)
    for command in each_sub_command_config(test_dir):
        assert isinstance(command, SetupCfgCommandConfig)
        assert isinstance(command.name, str)
        assert isinstance(command.camel, str)
        assert isinstance(command.description, str)
        assert isinstance(command.commands, tuple)
        assert len(command.commands) > 0
        for cmd in command.commands:
            assert isinstance(cmd, str)



# Generated at 2022-06-13 21:02:39.433883
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Test the ``each_sub_command_config()`` function."""
    real_path = os.path.realpath(__file__)
    real_path = os.path.dirname(real_path)
    real_path = os.path.join(real_path, '__setup_commands__.cfg')
    if os.path.isfile(real_path):
        os.remove(real_path)

    def _real_path(filename: str) -> str:
        return os.path.realpath(os.path.join(real_path, filename))


# Generated at 2022-06-13 21:02:47.266516
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # See the root of this package for the setup.cfg file that is used
    # in this function.
    cnt = 0
    for config in each_sub_command_config():
        print(config)
        cnt += 1
    assert cnt > 0
    # The next two lines are a simple sanity test to ensure the generator
    # works as expected.
    cnt = 0
    for config in each_sub_command_config():
        cnt += 1
    assert cnt == 0

# Generated at 2022-06-13 21:02:57.118580
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from itertools import islice

    path = os.path.dirname(__file__)

    def each_sub_cmd_config(
            setup_dir: Optional[Union[os.PathLike, str]] = None
    ) -> Generator[SetupCfgCommandConfig, None, None]:
        return islice(each_sub_command_config(setup_dir), 1)

    assert next(each_sub_cmd_config(path)) == SetupCfgCommandConfig(
        'subcommand.subcmd',
        'SubCommandSubcmd',
        'My project sub-command',
        (
            'subcommand.subcmd --version',
        )
    )

# Generated at 2022-06-13 21:03:10.330018
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pytest import raise_if_not
    from flutils.envutils import set_up_env
    from flutils.commonutils import get_random_string

    temp_dir_path = set_up_env(
        script_name=get_random_string(inst=str),
        globals_=globals()
    ).temp_dir_path
    temp_dir_path = os.path.realpath(temp_dir_path)

    setup_py_path = os.path.join(temp_dir_path, 'setup.py')
    setup_cfg_path = os.path.join(temp_dir_path, 'setup.cfg')
    setup_commands_cfg_path = os.path.join(temp_dir_path, 'setup_commands.cfg')


# Generated at 2022-06-13 21:03:19.188306
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import os
    import shutil
    from tempfile import mkdtemp

    from flutils.pathutils import (
        get_abs_path,
    )
    from flutils.strutils import (
        rand_str,
    )

    sys.path.insert(0, str(get_abs_path('../..')))

    # Test the 'home' key replacement
    command_name = rand_str(6)
    description = rand_str(6)
    commands = 'echo "Hello world"'
    home = os.path.expanduser('~')
    working_dir = mkdtemp(prefix='flutils_test_')

# Generated at 2022-06-13 21:03:30.867016
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # pylint: disable=expression-not-assigned
    # pylint: disable=too-few-public-methods
    # pylint: disable=no-self-use
    class Test:
        def __init__(self, config: SetupCfgCommandConfig) -> None:
            self.config = config

        def test_config(self) -> None:
            config = self.config
            assert config.name
            assert config.camel
            assert config.description
            assert config.commands

    for config in each_sub_command_config(os.path.dirname(__file__)):
        Test(config).test_config()