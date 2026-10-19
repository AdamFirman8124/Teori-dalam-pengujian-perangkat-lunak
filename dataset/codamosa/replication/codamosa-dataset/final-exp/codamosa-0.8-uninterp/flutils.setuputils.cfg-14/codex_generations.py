

# Generated at 2022-06-13 20:53:55.521125
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    pass

# Generated at 2022-06-13 20:54:04.315268
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.split(os.path.realpath(__file__))[0]
    for sub_cmd_config in each_sub_command_config(setup_dir):
        assert sub_cmd_config.name == 'i.am.a.sub-command'
        assert sub_cmd_config.camel == 'IAmASubCommand'
        assert (sub_cmd_config.description ==
                'A sub command for testing.')
        assert sub_cmd_config.commands == ('echo I am a sub command.',)
        break

# Generated at 2022-06-13 20:54:07.900544
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    source = 'source'

    class CommandConfig(NamedTuple):
        name: str
        camel: str
        commands: Tuple[str, ...]

    def add_to_source(name: str, commands: Tuple[str, ...]):
        nonlocal source

# Generated at 2022-06-13 20:54:21.805619
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    return
    # import tempfile
    # import textwrap
    # from flutils.configutils import TestConfig
    # from flutils.pathutils import get_absolute_path
    # from os.path import join
    # from typing import Dict, List, Tuple
    #
    # from flutils.funcutils import remove_func_attr
    # from flutils.tests.helpers import (
    #     assert_each_sub_command_config,
    # )
    # from typing_extensions import Annotated
    #
    #
    # def each_sub_command_config_tests(
    #         setup_dir: Union[os.PathLike, str],
    #         expect: Annotated[Dict[str, Tuple[str, ...]], TestConfig],
    #         setup_cfg_data: List[

# Generated at 2022-06-13 20:54:32.802972
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def _assert(
            setup_dir: os.PathLike,
            expected: Optional[List[SetupCfgCommandConfig]] = None
    ) -> None:
        if expected is None:
            expected = []
        actual = list(each_sub_command_config(setup_dir))
        assert actual == expected

    setup_dir = os.path.join(os.path.dirname(__file__), 'setup_dir')
    expected = [
        SetupCfgCommandConfig(
            '', '', '', ('pip install -r requirements_dev.txt',)
        ),
        SetupCfgCommandConfig(
            '', '', '', ('pip install -r requirements_run.txt',)
        ),
    ]
    _assert(setup_dir, expected)


# Generated at 2022-06-13 20:54:43.784676
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil
    import sys
    from unittest import mock

    with tempfile.TemporaryDirectory() as tmp_dir:
        name = 'my-package'

        def _write(filename, data):
            with open(os.path.join(tmp_dir, filename), 'w') as f:
                f.write(data)

        def _write_setup_cfg(content):
            _write('setup.cfg', content)

        _write_setup_cfg(
            '''
            [metadata]
            name = %s
            ''' % name
        )

        _write('setup.py', '''
        from setuptools import setup
        setup(name="{name}")
        '''.format(name=name))


# Generated at 2022-06-13 20:54:54.856100
# Unit test for function each_sub_command_config
def test_each_sub_command_config():

    # Note: We may want to use a temporary directory for the unit tests.
    # TODO: Is this the best way to run the unit tests from within the
    # package?
    setup_cfg_path = os.path.join(os.path.dirname(__file__), '..',
                                  'setup.cfg')
    setup_commands_cfg_path = os.path.join(os.path.dirname(__file__), '..',
                                           'setup_commands.cfg')

    # Test with the setup.cfg file
    parser = ConfigParser()
    parser.read(setup_cfg_path)
    name = _get_name(parser, setup_cfg_path)
    format_kwargs = {'name': name, 'setup_dir': os.path.dirname(__file__)}
    assert name

# Generated at 2022-06-13 20:55:04.121678
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # Test with the default setup_dir
    default_dir = None
    for sc in each_sub_command_config(default_dir):
        cmd_name = sc.name
        assert cmd_name, 'The command name should NOT be empty.'
        camel = sc.camel
        assert camel, 'The camel name should NOT be empty.'
        assert len(sc.commands), (
            'The command list should NOT be empty for the %r command.'
            % cmd_name
        )
        print(sc)

    # Test with the specific setup_dir
    setup_dir = os.path.join(os.path.dirname(__file__), '..', '..')
    for sc in each_sub_command_config(setup_dir):
        cmd_name = sc.name

# Generated at 2022-06-13 20:55:15.345724
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from unittest import TestCase

    class _TestCase(TestCase):
        def test(self):
            from os import path as os_path
            from os import sep as os_sep
            from tempfile import TemporaryDirectory

            def each_sub_command_config_test(
                    py_script: str,
                    cfg_script: str
            ) -> SetupCfgCommandConfig:
                with TemporaryDirectory() as temp_dir:
                    temp_dir = os_path.realpath(temp_dir)
                    setup_dir = os_path.join(temp_dir, 'project')
                    os.makedirs(setup_dir)
                    setup_py_path = os_path.join(setup_dir, 'setup.py')
                    with open(setup_py_path, 'wt') as fh:
                        fh.write

# Generated at 2022-06-13 20:55:26.434443
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    result = list(each_sub_command_config('tests'))
    # NOTE: Leaving the command names in their original case so the
    # unit test is less brittle with regards to case changes in the
    # future.

# Generated at 2022-06-13 20:55:47.055672
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config."""
    import sys
    import os
    from tempfile import mkdtemp
    from shutil import copyfile

    def _get_setup_py_path():
        for fs in extract_stack():
            fs = cast(FrameSummary, fs)
            if os.path.basename(fs.filename) == 'setup.py':
                return fs.filename

    setup_dir = mkdtemp()
    setup_py_path = os.path.join(setup_dir, 'setup.py')
    copyfile(_get_setup_py_path(), setup_py_path)

    config_file_path = os.path.join(setup_dir, 'setup.cfg')

# Generated at 2022-06-13 20:55:50.245747
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for sub_command in each_sub_command_config('./setup_dir'):
        print(sub_command)



# Generated at 2022-06-13 20:56:02.258367
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """A simple unit test to verify that each_sub_command_config() works
    with the flutils setup.py file that should be running this function.
    """
    def _is_ok(val: SetupCfgCommandConfig) -> bool:
        if val.name != 'flutils' and val.camel != 'Flutils':
            return False
        if val.description:
            if 'to run the tests' not in val.description:
                return False
        commands: List[str] = list(val.commands)
        if not commands:
            return False
        cmd = ' '.join(commands)
        if 'python setup.py test --test-suite=flutils' not in cmd:
            return False
        return True


# Generated at 2022-06-13 20:56:13.725049
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import shutil
    import tempfile
    temp_dir = tempfile.mkdtemp()


# Generated at 2022-06-13 20:56:24.679009
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.testing import UnitTest
    u = UnitTest(debug=True)

    def _each_setup_cfg_command_config(
            parser: ConfigParser,
            setup_dur: Optional[str] = None,
            setup_cfg: Optional[str] = None
    ) -> Generator[SetupCfgCommandConfig, None, None]:
        for scc in each_sub_command_config(setup_dir=setup_dur):
            yield scc

    # No setup.cfg
    u.test(
        method=_each_setup_cfg_command_config,
        setup_cfg='nope',
        setup_dur='tests/templates'
    )

    # No setup.py

# Generated at 2022-06-13 20:56:32.649610
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import inspect
    import pprint
    from pathlib import Path

    module_path = inspect.getfile(test_each_sub_command_config)
    module_path = Path(module_path)
    sub_cmds = list(each_sub_command_config(module_path.parent))
    assert sub_cmds
    assert sub_cmds[0].camel == 'DateFmt'
    assert sub_cmds[0].description == 'Generate a strftime() format string.'
    pprint.pprint(sub_cmds)

# Generated at 2022-06-13 20:56:39.991772
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pytestutils import (
        find_parent_dir,
        is_testing,
    )
    if is_testing():
        root = find_parent_dir('setup.py', curdir=os.curdir)
        print()
        for config in each_sub_command_config(root):
            print(config._asdict())


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:56:51.036278
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    path = os.path.join(
        os.path.dirname(__file__), 'data', 'test_setup_commands_cfg'
    )
    for i in each_sub_command_config(path):
        assert isinstance(i, SetupCfgCommandConfig)
        assert i.name
        assert i.camel
        assert i.description
        assert i.commands

        assert i.name in (
            'all',
            'bdist_wheel',
            'build_ext',
            'build',
            'clean',
            'install',
            'register',
            'sdist',
            'test',
            'test_bdist_wheel',
        )


# Generated at 2022-06-13 20:57:02.994743
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import pytest
    from flutils.pathutils import chdir_tm

    setup_dir = os.path.dirname(__file__)
    configs = list(each_sub_command_config(setup_dir))
    comma = ', '

# Generated at 2022-06-13 20:57:07.887802
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config('/home/user/flutils'):
        assert isinstance(config, SetupCfgCommandConfig)
        assert isinstance(config.name, str)
        assert isinstance(config.camel, str)
        assert isinstance(config.description, str)
        assert isinstance(config.commands, tuple)
        for cmd in config.commands:
            assert isinstance(cmd, str)



# Generated at 2022-06-13 20:57:29.892104
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    parent_dir = os.path.abspath(
        os.path.join(current_dir, os.path.pardir)
    )

# Generated at 2022-06-13 20:57:42.283100
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    from pathlib import Path

    from flutils.pathutils import temp_chdir

    from .conftest import _reset_sys_argv

    # setup.cfg
    with temp_chdir() as dir_path:
        with open('setup.cfg', 'w') as fp:
            fp.write('[metadata]\n')
            fp.write('name = foo\n')
        path = Path('.').resolve()
        sys.argv = ['python', 'setup.py', 'sub']
        with _reset_sys_argv(sys.argv) as reset:
            reset()
            assert sys.argv == ['python', 'setup.py', 'sub']
            assert each_sub_command_config(str(path)) is not None

    # setup.cfg, setup_commands

# Generated at 2022-06-13 20:57:52.797567
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    import sys
    import unittest

    basedir = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))
    sys.path.insert(0, basedir)
    import entrypoint_command_loader  # noqa isort:skip

    for _ in entrypoint_command_loader.each_sub_command_config(
            setup_dir=basedir
    ):
        pass

    class TestEachSubCommandConfig(unittest.TestCase):
        def test_command_with_template_variables(self):
            class TestConfig(NamedTuple):
                name: str
                camel: str
                description: str
                commands: Tuple[str, ...]


# Generated at 2022-06-13 20:58:04.941171
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    expected = frozenset((
        SetupCfgCommandConfig(
            'docs.build',
            'DocsBuild',
            'Build documentation using sphinx',
            (
                'cd docs',
                'make html',
                './upload-docs.sh',
            ),
        ),
        SetupCfgCommandConfig(
            'docs.spellcheck',
            'DocsSpellcheck',
            'Run spellcheck on documentation',
            (
                'bash -c '
                '"cd docs && make spelling"',
            ),
        ),
    ))

    this_dir = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(this_dir, 'test_data')
    result = frozenset(each_sub_command_config(test_dir))

# Generated at 2022-06-13 20:58:15.890157
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # Test case #0: A valid project
    case_0_setup_dir = os.path.join(
        os.path.dirname(__file__), '..', '..', '..'
    )
    case_0 = list(each_sub_command_config(case_0_setup_dir))
    assert len(case_0) > 0

    # Test case #1: An invalid project
    case_1_setup_dir = os.path.join(case_0_setup_dir, '..',)
    with pytest.raises(FileNotFoundError):
        list(each_sub_command_config(case_1_setup_dir))

    # Test case #2: Missing setup directory
    with pytest.raises(FileNotFoundError):
        list(each_sub_command_config())

    #

# Generated at 2022-06-13 20:58:20.071915
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.dirname(__file__)
    for config in each_sub_command_config(setup_dir):
        print(config)

# Generated at 2022-06-13 20:58:32.292099
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    import sys
    root = os.path.realpath(os.path.join(
        os.path.dirname(__file__),
        '..',
        '..',
        '..',
        '..',
        'src'
    ))
    flutils = os.path.join(root, 'flutils')
    if flutils not in sys.path:
        sys.path.append(flutils)
    import flutils
    flutils.console.LOGGER.debug(
        'Each sub command config for flutils:'
    )

# Generated at 2022-06-13 20:58:40.921914
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config."""
    dirs = (
        'tests/data/sample_1',
        'tests/data/sample_2',
        'tests/data/sample_3',
    )
    for dir_ in dirs:
        dir_ = os.path.realpath(dir_)
        print('Directory: %r' % dir_)
        for config in each_sub_command_config(dir_):
            print('', config)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:58:44.719893
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config(os.path.dirname(__file__)):
        assert config.name == 'pytest'
        assert len(config.commands) == 1
        print(config)

# Generated at 2022-06-13 20:58:52.015474
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # We need a real setup.py and setup.cfg to test this function.
    #   I'm going to use this project's.
    #   I'm going to use a python file that is a sibling of this one to
    #   determine the directory that contains this file.
    #   I'm going to use a sibling of this python file to determine the
    #   root of this project.
    #   I'll then use the root of this project to test the function.
    import os
    import sys
    import unittest
    from flutils.setuputils import (
        SetupCfgCommandConfig,
        each_sub_command_config
    )


# Generated at 2022-06-13 20:59:27.138675
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    import sys
    import tempfile

    # Create a test package
    with tempfile.TemporaryDirectory() as tmpdirname:
        os.mkdir(os.path.join(tmpdirname, sys.argv[1]))
        with open(os.path.join(tmpdirname, 'setup.py'), 'w') as f:
            f.write("""\
from setuptools import setup

setup()
""")
        with open(os.path.join(tmpdirname, 'setup.cfg'), 'w') as f:
            f.write("""\
[metadata]
name = My Proj
""")
        setup_dir = os.path.join(tmpdirname, sys.argv[1])

# Generated at 2022-06-13 20:59:39.893719
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import unittest
    import os.path

    class TestSetupCommands(unittest.TestCase):

        def test_each_sub_command_config(self):
            """Tests the function each_sub_command_config."""

            # Test empty setup.cfg file.
            setup_dir = os.path.join('tests', 'data', 'setup_empty')
            conf_gen = each_sub_command_config(setup_dir=setup_dir)
            with self.assertRaises(StopIteration):
                next(conf_gen)

            # Test basic setup.cfg file (i.e., no setup_commands.cfg).
            setup_dir = os.path.join('tests', 'data', 'setup_basic')
            conf_gen = each_sub_command_config(setup_dir=setup_dir)


# Generated at 2022-06-13 20:59:43.603035
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.projectutils import each_sub_command_config

    for config in each_sub_command_config():
        assert isinstance(config, SetupCfgCommandConfig)
        assert config.name
        assert config.camel
        assert config.description
        assert config.commands

# Generated at 2022-06-13 20:59:53.801903
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Verifies the CLI sub-commands are parsed correctly."""
    setup_dir = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        '..', '..', '..', '..', 'setuptools', 'project_template'
    )
    configs = list(each_sub_command_config(setup_dir))
    assert len(configs) == 6
    assert configs[0] == SetupCfgCommandConfig(
        name='docs.build',
        camel='DocsBuild',
        description='Build the docs',
        commands=(
            'python setup.py build_sphinx',
            'python setup.py check --restructuredtext',
            'python setup.py build_sphinx --warning-is-error',
        )
    )

# Generated at 2022-06-13 20:59:59.912864
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.configutils import find_config_file
    from flutils.pathutils import each_path_up

    for config_file in find_config_file('setup.cfg'):
        for setup_dir in each_path_up(config_file):
            for config in each_sub_command_config(setup_dir):
                print(config)



# Generated at 2022-06-13 21:00:09.349685
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for section, command_name in _each_setup_cfg_command_section(
            ConfigParser()
    ):
        assert section.startswith('setup.command.')
        assert command_name
    with pytest.raises(FileNotFoundError):
        each_sub_command_config('does_not_exist')
    with pytest.raises(FileNotFoundError):
        each_sub_command_config('/dev/null')
    with pytest.raises(FileNotFoundError):
        each_sub_command_config('/')
    with pytest.raises(NotADirectoryError):
        each_sub_command_config('/etc/passwd')
    with pytest.raises(FileNotFoundError):
        each_sub_command_config('/opt/python/')

# Generated at 2022-06-13 21:00:25.198038
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import unittest

    class TestEachSubCommandConfig(unittest.TestCase):
        def test_each_sub_command_config(self):
            import tempfile
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_dir = temp_dir.rstrip(os.sep)
                setup_dir = os.path.join(temp_dir, 'setup_dir')
                os.makedirs(setup_dir)
                setup_py_path = os.path.join(setup_dir, 'setup.py')


# Generated at 2022-06-13 21:00:37.469965
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def validate_each_command(
            iter_cmds: Generator[SetupCfgCommandConfig, None, None],
            expected_commands: Tuple[str, ...],
    ) -> None:
        commands = []
        for cmd in iter_cmds:
            commands += list(cmd.commands)
        assert sorted(commands) == sorted(expected_commands)

    with TemporaryDirectory() as tmpdirname:
        setup_cfg_fn = os.path.join(tmpdirname, 'setup.cfg')
        setup_cfg_cn = os.path.join(tmpdirname, 'setup_commands.cfg')

# Generated at 2022-06-13 21:00:49.323139
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.testingutils.fileutils import _file_exists

    kwargs: Dict[str, str] = {
        'setup_dir': os.path.realpath(
            os.path.join('tests', 'example_project')
        ),
        'home': os.path.expanduser('~')
    }
    setup_cfg_path = os.path.join(kwargs['setup_dir'], 'setup.cfg')
    parser = ConfigParser()
    parser.read(setup_cfg_path)
    kwargs['name'] = _get_name(parser, setup_cfg_path)
    path = os.path.join(kwargs['setup_dir'], 'setup_commands.cfg')
    if os.path.isfile(path):
        parser = ConfigParser()
        parser.read

# Generated at 2022-06-13 21:01:00.337568
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    #  Verify the 'home' keyword in config file.
    os.environ['HOME'] = '/tmp'
    try:
        home_value = None
        for command in each_sub_command_config('tests/fixtures/test_project1'):
            if command.name == 'test1':
                home_value = command.commands[0].split()[6]
                break
        assert home_value == '/tmp'  # type: ignore
    finally:
        del os.environ['HOME']

    # Verify the 'setup_dir' keyword in config file.
    for command in each_sub_command_config('tests/fixtures/test_project2'):
        if command.name == 'test1':
            setup_dir_value = command.commands[0].split()[6]
            break
    assert setup

# Generated at 2022-06-13 21:01:58.532087
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil
    import uuid
    tmp = tempfile.mkdtemp()

# Generated at 2022-06-13 21:02:05.918154
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    here = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(here, 'test_project')
    os.chdir(test_dir)
    import flutils.setup_commands  # NOQA

    for item in each_sub_command_config():
        print(item)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:02:08.103781
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for cfg in each_sub_command_config():
        print(cfg)

# Generated at 2022-06-13 21:02:11.299718
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for x in each_sub_command_config():
        print(x)

if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:02:24.872149
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile

    cfg_path = os.path.join(tempfile.gettempdir(), 'setup.cfg')

# Generated at 2022-06-13 21:02:30.849244
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    config = next(each_sub_command_config())
    print(config)


if __name__ == "__main__":
    test_each_sub_command_config()

__all__ = (
    'each_sub_command_config',
    'SetupCfgCommandConfig',
)

# Generated at 2022-06-13 21:02:36.844373
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    path = os.path.join(
        os.path.dirname(__file__), 'src', 'setuptools_populate_commands'
    )
    path = os.path.realpath(path)
    configs = list(each_sub_command_config(path))
    assert len(configs) == 2
    assert 'sample' in configs[0].name
    assert 'sample' in configs[1].name

# Generated at 2022-06-13 21:02:43.554850
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for n, c, d, cmds in each_sub_command_config():
        assert n
        assert c
        assert d
        assert cmds
    # TODO: add better, more robust, tests


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:02:53.432056
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # fmt: off
    actual = [x for x in each_sub_command_config(
        'tests/data/hello_world_pkg/src/hello_world_pkg',
    )
    ]

# Generated at 2022-06-13 21:03:06.794921
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import os.path
    import pkg_resources
    import flutils.cmdutils

    sys.path.append(os.path.dirname(__file__))

    try:
        flutils = pkg_resources.get_distribution('flutils')
    except pkg_resources.DistributionNotFound:
        flutils = pkg_resources.get_distribution('fl-utils')

    flutils_version = flutils.version
    assert flutils_version
    assert flutils.location == os.path.dirname(flutils.location)
    assert os.path.exists(flutils.location)
    assert os.path.isdir(flutils.location)
