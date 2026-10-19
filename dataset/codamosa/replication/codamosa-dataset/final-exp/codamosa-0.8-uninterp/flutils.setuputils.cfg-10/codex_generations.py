

# Generated at 2022-06-13 20:54:00.519035
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    #
    # There is no setup.py.
    #
    with pytest.raises(FileNotFoundError):
        for config in each_sub_command_config():
            print(config)
    #
    # There is no setup.cfg.
    #
    with pytest.raises(FileNotFoundError):
        for config in each_sub_command_config(THIS_DIR):
            print(config)
    #
    # There is no setup_commands.cfg.
    #
    with pytest.raises(LookupError):
        for config in each_sub_command_config(THIS_DIR_NO_CMD_CFG):
            print(config)
    #
    # There is no 'name' in the setup.cfg's 'metadata' section.
    #

# Generated at 2022-06-13 20:54:07.340518
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    dirname, _ = os.path.split(os.path.dirname(__file__))
    pkg_dir = os.path.join(dirname, 'tests', 'pkg')
    for sub_command_config in each_sub_command_config(pkg_dir):
        assert sub_command_config.name == 'test-sub-cmd'
        assert sub_command_config.camel == 'TestSubCmd'
        assert sub_command_config.description == 'A sample sub command.'
        assert sub_command_config.commands == (
            'echo "Running test-sub-cmd"',
            'echo "  --setup-dir {setup_dir}"',
            'echo "  --home {home}"',
            'echo "  --name {name}"',
        )

# Generated at 2022-06-13 20:54:20.580974
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def _sort_key(cmd_cfg: SetupCfgCommandConfig) -> str:
        return '%s.%s' % (cmd_cfg.name, cmd_cfg.camel)

    temp = tempfile.TemporaryDirectory(prefix='flutils_test.')

# Generated at 2022-06-13 20:54:32.206557
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils._testing import (
        AssertPyPackageCommand,
        AssertPyPackageSetupDir,
        AssertPyPackageSetupFile,
        AssertPyPackageSetupCfgFile,
    )
    from flutils._testing._helper import with_temp_project
    import tempfile

    def gen_setup_cfg_file(path):
        with open(path, 'w') as f:
            f.write("[metadata]\n"
                    "name = flutils\n")
            f.write("\n")
            f.write("[setup.command.misc]\n"
                    "description = Miscellaneous stuff.\n"
                    "commands =\n"
                    "    echo test\n")
            f.write("\n")

# Generated at 2022-06-13 20:54:43.670317
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import parent_path

    class _TestCase(NamedTuple):
        setup_dir: str
        configs: Tuple[SetupCfgCommandConfig, ...]


# Generated at 2022-06-13 20:54:54.778143
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    parser = ConfigParser()
    parser.add_section('metadata')
    parser.set('metadata', 'name', 'project-name')
    parser.add_section('setup.command.init')
    parser.set(
        'setup.command.init',
        'commands',
        '\n'.join([
            'git init',
            'git add .',
            'git commit -m "Initial commit."'
        ])
    )
    path = os.path.join(os.path.dirname(__file__), 'setup.cfg')
    with open(path, 'w') as fo:
        parser.write(fo)
    try:
        for config in each_sub_command_config():
            assert isinstance(config, SetupCfgCommandConfig)
    finally:
        os.remove(path)



# Generated at 2022-06-13 20:54:59.105979
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    cwd = os.getcwd()
    try:
        os.chdir(os.path.dirname(__file__))
        a = list(each_sub_command_config())
        assert len(a) > 0
    finally:
        os.chdir(cwd)

# Generated at 2022-06-13 20:55:05.935543
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    p = Path(__file__).parent
    each_sub_command_config(p)
    setup_dir = _prep_setup_dir(p)
    assert setup_dir.endswith('tests')
    format_kwargs = {
        'setup_dir': setup_dir,
        'home': os.path.expanduser('~')
    }
    parser = ConfigParser()
    setup_cfg_path = os.path.join(format_kwargs['setup_dir'], 'setup.cfg')
    parser.read(setup_cfg_path)
    format_kwargs['name'] = _get_name(parser, setup_cfg_path)
    path = os.path.join(format_kwargs['setup_dir'], 'setup_commands.cfg')

# Generated at 2022-06-13 20:55:17.225513
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def _each_tuple_as_dict(
            g: Generator[SetupCfgCommandConfig, None, None]
    ) -> Generator[Dict[str, str], None, None]:
        for t in g:
            yield t._asdict()

    def _assert_equal_dicts(
            gen_a: Generator[Dict[str, str], None, None],
            gen_b: Generator[Dict[str, str], None, None]
    ) -> None:
        for d in gen_a:
            orig_d = {k: v for k, v in d.items()}
            expected = next(gen_b)

# Generated at 2022-06-13 20:55:26.186301
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """
    Test the output of the ``each_sub_command_config`` function.
    """
    from os import makedirs, mkdir
    from os.path import join, isdir

    from shutil import rmtree

    from tempfile import mkdtemp

    from unittest.mock import patch

    from flutils.sysutils import get_test_path

    with patch.object(ConfigParser, 'read') as mock_read:
        mock_read.return_value = None
        # Test 'raise'
        try:
            next(each_sub_command_config())
            assert False, "Expected exception was not raised."
        except FileNotFoundError as ex:
            assert ex.args == ("Unable to find the directory that contains "
                               "the 'setup.py' file.",)

    # Test setup.

# Generated at 2022-06-13 20:55:36.436433
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    out = list(each_sub_command_config())
    assert isinstance(out, list)

# Generated at 2022-06-13 20:55:47.349642
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    from pathlib import Path
    from typing import Callable
    from flutils.config import BASE_DIR

    # TODO: Add more test cases.
    README_RST = """\
Hello
=====

Flutils is a library that is used by other libraries and apps.
It provides a collection of general purpose utility functions and decorators.

"""

    def exec_setup_cfg_file(
            filename: str,
            command: str,
            setup_dir: Path,
            executor: Callable[[str, str], None],
    ) -> None:
        setup_cfg_path = setup_dir / filename

# Generated at 2022-06-13 20:55:53.180092
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    expected = SetupCfgCommandConfig('setup.command.hello', 'Hello', '', ())
    actual = next(each_sub_command_config(
        os.path.join(os.path.dirname(__file__), '..', 'testdata')
    ))
    assert actual == expected



# Generated at 2022-06-13 20:55:59.827734
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    cmds: List[Tuple[str, str]] = list(each_sub_command_config())
    assert len(cmds) >= 1
    for cmd in cmds:
        fst = cast(SetupCfgCommandConfig, cmd)
        assert fst.name
        assert fst.camel
        assert fst.description
        assert fst.commands

# Generated at 2022-06-13 20:56:12.542278
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    configs = list(each_sub_command_config())
    assert len(configs) == 3
    for config in configs:
        assert isinstance(config, SetupCfgCommandConfig)
        assert len(config.commands) >= 1
        assert isinstance(config.commands, tuple)
        for command in config.commands:
            assert isinstance(command, str)
    # Test each config

    # Check the 'bump' config
    config = configs[0]
    assert config.name == 'bump'
    assert config.camel == 'Bump'
    assert config.description.startswith('Bumps the ')
    assert isinstance(config.commands, tuple)
    assert len(config.commands) == 2
    assert config.commands[0] == "bumpversion"

# Generated at 2022-06-13 20:56:22.738587
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    fn = os.path.basename(__file__)
    test_dir = os.path.dirname(__file__)
    while len(test_dir) > 1 and fn != 'test':
        test_dir = os.path.dirname(test_dir)
        fn = os.path.basename(test_dir)
    test_dir = os.path.join(test_dir, 'test_package')
    if os.path.isfile(os.path.join(test_dir, 'setup.py')):
        for scc in each_sub_command_config(test_dir):
            print(scc)

if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:56:34.346958
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import unittest
    import unittest.mock as mock

    def _mock_path_exists(path):
        if path.endswith('setup.py'):
            return True
        if path.endswith('setup.cfg'):
            return True
        if path.endswith('setup_commands.cfg'):
            return True
        return False

    setup_cfg_commands_found = False

    class TestCase(unittest.TestCase):
        @mock.patch('os.path.exists', side_effect=_mock_path_exists)
        def test_each_sub_command_config(self, path_exists_mock):
            nonlocal setup_cfg_commands_found

# Generated at 2022-06-13 20:56:42.924198
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config():
        assert isinstance(config, SetupCfgCommandConfig)
        assert isinstance(config.name, str)
        assert isinstance(config.camel, str)
        assert isinstance(config.description, str)
        assert isinstance(config.commands, Tuple)
        for command in config.commands:
            assert isinstance(command, str)

# Generated at 2022-06-13 20:56:53.223042
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.dirname(__file__)
    configs = tuple(each_sub_command_config(setup_dir))
    assert len(configs) == 4
    assert configs[0].name == "coverage"
    assert configs[0].commands[0] == "pytest --cov=flutils"
    assert configs[1].name == "documentation"
    assert configs[1].commands[0] == "sphinx-build -a -b html docs docs/_build/html"
    assert configs[2].name == "package"
    assert configs[2].commands[0] == "python setup.py sdist bdist_wheel"
    assert configs[3].name == "test_package"

# Generated at 2022-06-13 20:56:59.796090
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    res = list(each_sub_command_config())
    assert len(res) > 0
    cmd_cfg = res[0]
    assert isinstance(cmd_cfg, SetupCfgCommandConfig)
    assert cmd_cfg.name
    assert cmd_cfg.camel
    assert isinstance(cmd_cfg.commands, tuple)
    assert len(cmd_cfg.commands) >= 1

# Generated at 2022-06-13 20:57:15.563164
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from io import StringIO
    from flutils.pytest.helpers import (
        assert_item_equals,
        assert_items_equals,
        assert_match,
        temp_chdir,
    )

    with temp_chdir(__file__, '__file__', 'data', 'setup_commands') as tmp:
        sub_cmds = [
            SetupCfgCommandConfig(
                'hello.world',
                'HelloWorld',
                'The hello command',
                ('echo "hello world";',)
            ),
            SetupCfgCommandConfig(
                'hello.user',
                'HelloUser',
                'The hello user command',
                ('echo "hello user";',)
            ),
        ]
        gen = each_sub_command_config()

# Generated at 2022-06-13 20:57:28.263976
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import tempfile

    with tempfile.TemporaryDirectory() as td:
        td = os.path.realpath(td)

# Generated at 2022-06-13 20:57:41.108069
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    import sys
    import tempfile

    # Ensure that setup.py is found
    cwd = os.getcwd()
    os.chdir('/')

    def cleanup():
        os.chdir(cwd)


# Generated at 2022-06-13 20:57:51.879571
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.testingutils import (
        _CALLED_FUNC_KEY,
        set_test_context,
        get_test_context,
        clear_test_context,
    )
    import functools
    import sys

    @functools.lru_cache()
    def _get_env(key: str) -> str:
        import os
        from flutils.envutils import get_env
        return get_env(key)

    set_test_context(
        {
            _CALLED_FUNC_KEY: 'each_sub_command_config',
            'filename': __file__,
            'exit_code': 0
        }
    )
    tc: Dict = get_test_context()
    _orig_exit = sys.exit

# Generated at 2022-06-13 20:57:53.354436
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for cfg in each_sub_command_config():
        print(cfg)

# Generated at 2022-06-13 20:57:56.886771
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    assert list(each_sub_command_config()) == []


if __name__ == '__main__':
    import sys
    import pytest

    errno = pytest.main(sys.argv)
    sys.exit(errno)

# Generated at 2022-06-13 20:58:08.361781
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.scripts.mk_sub_commands import each_sub_command_config

    for config in each_sub_command_config('./tests/fixtures/sub_commands'):
        assert config.name.startswith('sub_commands')
        assert config.camel.startswith('SubCommands')
        assert config.commands


if __name__ == '__main__':
    from flutils.scripts.mk_sub_commands import each_sub_command_config

    # -- Setup
    print('-- Setup')
    example_dir = './tests/fixtures/sub_commands'

    # -- Test functions
    print('-- Test functions')
    test_each_sub_command_config()

    # -- Test script
    print('-- Test script')
    # print('\n'.join

# Generated at 2022-06-13 20:58:16.094966
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    tests_dir = os.path.dirname(__file__)
    project_dir = os.path.join(tests_dir, 'project')

    for sc in each_sub_command_config(project_dir):
        commands = sc.commands
        assert commands

        sc_name = sc.name
        assert sc_name

        sc_camel = sc.camel
        assert sc_camel

        sc_desc = sc.description
        assert sc_desc


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:58:19.118096
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for x in each_sub_command_config(setup_dir='/flynt'):
        pass

if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:58:31.676845
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from unittest import TestCase
    from unittest.mock import (
        Mock,
        patch,
    )

    class SetupConfigTest(TestCase):
        @patch.object(ConfigParser, 'sections')
        def test_each_setup_cfg_command_section(self, configparser_section_mock):
            configparser_section_mock.return_value = (
                'setup.command.test', 'setup.command.test2',
                'setup.command.test3'
            )
            parser = ConfigParser()
            out = list(_each_setup_cfg_command_section(parser))

# Generated at 2022-06-13 20:58:51.421024
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    import sys
    from pathlib import Path
    from tempfile import TemporaryDirectory


# Generated at 2022-06-13 20:59:04.888327
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    dir_ = os.path.dirname(os.path.abspath(__file__))
    dir_ = os.path.dirname(dir_)
    setup_dir = os.path.join(dir_, 'tests', 'units', 'data')
    configs = list(each_sub_command_config(setup_dir))

    assert len(configs) == 3

    c = configs[0]
    assert c.name == 'command1'
    assert c.camel == 'Command1'
    assert c.description == 'This is test command 1.'
    assert len(c.commands) == 1
    assert c.commands[0] == 'echo command1'

    c = configs[1]
    assert c.name == 'command2'
    assert c.camel == 'Command2'
   

# Generated at 2022-06-13 20:59:15.575627
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import pathlib
    from itertools import chain
    from inspect import cleandoc as trim

    def _assert(
            expected: Optional[Union[str, Tuple[str, ...]]],
            actual: Union[str, Tuple[str, ...]]
    ) -> None:
        if expected is None:
            assert not actual, repr(actual)
        else:
            assert expected == actual, (actual, expected)

    setup_dir = pathlib.Path(__file__).parent.parent
    setup_cfg = setup_dir / 'setup.cfg'
    setup_commands_cfg = setup_dir / 'setup_commands.cfg'
    argv = sys.argv

# Generated at 2022-06-13 20:59:24.443240
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def print_command_config(config: SetupCfgCommandConfig) -> None:
        print(
            'name: {name}\ndescription: {description}\ncommands:\n  '
            .format(
                name=config.name,
                description=config.description
            ),
            end=''
        )
        print('\n  '.join(config.commands))
        print()
    for config in each_sub_command_config(__file__):
        print_command_config(config)



# Generated at 2022-06-13 20:59:37.730163
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    _setup_dir = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'lib', 'flutils', 'scripts', 'test_project'
    )
    assert _prep_setup_dir(_setup_dir) == _setup_dir
    assert list(_each_setup_cfg_command_section(_setup_cfg_parser())) == [
        ('setup.command.sphinx.build', 'sphinx.build'),
        ('setup.command.sphinx.quickstart', 'sphinx.quickstart'),
        ('setup.command.twine.upload_dist', 'twine.upload_dist'),
    ]

# Generated at 2022-06-13 20:59:39.562126
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    assert any(each_sub_command_config()) is True

# Generated at 2022-06-13 20:59:50.101321
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from pathlib import Path
    from tests.unit.commands.utils import (
        get_dev_dir,
        get_tests_dir,
    )
    from tests.unit.commands.utils import pkgs  # noqa
    dev_dir = get_dev_dir()
    tests_dir = get_tests_dir()
    if dev_dir in Path(__file__).parents:
        pkg = 'flutils'
        setup_dir = os.path.join(tests_dir, pkg)
    else:
        pkg = 'flutils-dev'
        setup_dir = dev_dir
    sub_commands = list(each_sub_command_config(setup_dir))
    assert len(sub_commands) == len(pkgs[pkg]['commands'])
    assert sub_commands

# Generated at 2022-06-13 20:59:52.895272
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    a = "abc"
    b = 0


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:00:01.618313
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    casepath = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..',
        '..',
        'case'
    )
    for scfg in each_sub_command_config(casepath):
        assert scfg.name == 'one'
        assert scfg.camel == 'One'
        assert scfg.description == 'The One Command'
        assert scfg.commands == ('echo 1', )
        break


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:00:15.189343
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    configs = list(each_sub_command_config())

# Generated at 2022-06-13 21:00:49.404836
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.testutils.fileutils import (
        write_data_to_temp_setup_files,
        write_data_to_setup_files,
    )
    from flutils.testutils.fileutils import get_test_data_path
    import tempfile
    import os
    import shutil

    # Using a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        setup_dir = os.path.join(temp_dir, 'test_package')
        # Writing the setup files to a temporary directory
        write_data_to_temp_setup_files(setup_dir)
        # Initializing the command structure
        _command_struct: Dict[str, SetupCfgCommandConfig] = {}
        # Reading the setup.cfg file

# Generated at 2022-06-13 21:00:53.716769
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config():
        if config.name == 'version':
            break
    else:
        raise AssertionError("Unable to find 'version' sub-command.")

# Generated at 2022-06-13 21:00:59.552327
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import contextlib
    with contextlib.redirect_stdout(None):
        import flutils.config
        dir_ = os.path.dirname(flutils.config.__file__)
        dir_ = os.path.join(dir_, '..')
        for config in each_sub_command_config(setup_dir=dir_):
            assert config is not None

# Generated at 2022-06-13 21:01:03.265362
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def _run() -> None:
        for c in each_sub_command_config():
            print(c)
    _run()

# Generated at 2022-06-13 21:01:07.642534
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    l = [
        i
        for i in each_sub_command_config(os.path.dirname(__file__))
    ]
    assert l[0].name == 'test.test_utils.test_each_sub_command_config'

# Generated at 2022-06-13 21:01:19.966026
# Unit test for function each_sub_command_config

# Generated at 2022-06-13 21:01:32.584630
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from tempfile import (
        TemporaryDirectory,
    )
    import textwrap
    from unittest import (
        TestCase,
        main,
    )

    def setup_test(test: TestCase, cfg_text: str):
        test.cfg_text = cfg_text
        test.parser = ConfigParser()
        test.setup_dir = TemporaryDirectory()
        tmp_dir = test.setup_dir.name

        cfg_path = os.path.join(tmp_dir, 'setup.cfg')
        with open(cfg_path, 'wb') as f:
            f.write(
                cfg_text.encode('utf-8')
            )


# Generated at 2022-06-13 21:01:46.799399
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils import logutils
    from flutils.pathutils import each_parent_dir

    def _each_test_paths() -> Generator[str, None, None]:
        test_dir = os.path.dirname(__file__)
        setup_dir = os.path.join(test_dir, '.test_data', 'each_sub_command')
        for path in each_parent_dir(test_dir):
            yield path
        yield setup_dir


# Generated at 2022-06-13 21:01:59.604153
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import inspect
    import pkg_resources
    from flutils.configutils import each_sub_command_config

    setup_cfg_path = pkg_resources.resource_filename(
        'flutils', 'tests/resources/setup.cfg'
    )
    expected = SetupCfgCommandConfig('name', 'NAME', '', tuple())

    real_each_sub_command_config = each_sub_command_config

    def each_sub_command_config(
            setup_dir: Optional[Union[os.PathLike, str]] = None
    ) -> Generator[SetupCfgCommandConfig, None, None]:
        if setup_dir is None:
            setup_dir = setup_cfg_path
        return real_each_sub_command_config(setup_dir)


# Generated at 2022-06-13 21:02:12.521786
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import pytest

    with pytest.raises(FileNotFoundError):
        each_sub_command_config()

    with pytest.raises(FileNotFoundError):
        each_sub_command_config('this/path/does/not/exist')

    with pytest.raises(FileNotFoundError):
        each_sub_command_config(__file__)

    with pytest.raises(FileNotFoundError):
        each_sub_command_config(os.path.dirname(__file__))

    for c in each_sub_command_config(
            os.path.dirname(os.path.dirname(__file__))
    ):
        assert c.name.startswith('setup.')
        assert c.camel.startswith('Setup')
        assert c.description
        assert c

# Generated at 2022-06-13 21:03:07.048208
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.paths import abspath_from_project_root
    path = abspath_from_project_root('./tests/cmds/setup_commands')
    path = abspath_from_project_root(path)
    assert os.path.isdir(path) is True
    expected = SetupCfgCommandConfig('foo', 'Foo', 'Foo long description.',
                                     ('foo command',
                                      'echo foo',))
    for idx, out in enumerate(each_sub_command_config(path)):
        assert out == expected
        assert idx == 0
        break
    else:
        raise RuntimeError("Expected output not found.")



# Generated at 2022-06-13 21:03:17.003688
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from pprint import pprint
    from pytest import fail
    data: List[SetupCfgCommandConfig] = []
    try:
        list(each_sub_command_config())
    except FileNotFoundError:
        pass
    else:
        data = [d for d in each_sub_command_config()]
        print("\nEach sub-command config of: %r\n" % os.getcwd())
        pprint(data)
        print("\n")

    if len(data) == 0:
        fail("The each_sub_command_config() function failed.")


if __name__ == '__main__':
    print("Running unit tests for %s" % __file__)
    test_each_sub_command_config()

# Generated at 2022-06-13 21:03:33.408786
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    format_kwargs = {
        'setup_dir': _prep_setup_dir(),
        'home': os.path.expanduser('~')
    }
    setup_cfg_path = os.path.join(format_kwargs['setup_dir'], 'setup.cfg')
    parser = ConfigParser()
    parser.read(setup_cfg_path)
    format_kwargs['name'] = _get_name(parser, setup_cfg_path)
    path = os.path.join(format_kwargs['setup_dir'], 'setup_commands.cfg')
    if os.path.isfile(path):
        parser = ConfigParser()
        parser.read(path)
    assert isinstance(
        list(_each_setup_cfg_command(parser, format_kwargs)), list
    )

# Generated at 2022-06-13 21:03:42.550346
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    data = []
    for setupCfgCommandConfig in each_sub_command_config():
        data.append(setupCfgCommandConfig)
    assert data[0] == SetupCfgCommandConfig(
        name='create_aliases',
        camel='CreateAliases',
        description='Creates the console aliases required by the CLI.',
        commands=(
            '~/dev/bin/flutils-cli-dev/(venv) $ flutils-create-aliases '
            '--fd-path ~/dev/flutils',
        ),
    )