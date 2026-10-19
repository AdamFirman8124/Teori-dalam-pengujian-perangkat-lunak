

# Generated at 2022-06-13 20:53:55.618463
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from os.path import dirname
    from pprint import pprint
    from inspect import currentframe
    frame = currentframe()
    pprint(
        list(each_sub_command_config(setup_dir=dirname(frame.f_code.co_filename)))
    )

# Generated at 2022-06-13 20:54:04.119323
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.join(
        os.path.dirname(__file__),
        '../../../flutils/tests/test_project'
    )
    print(setup_dir)
    for s in each_sub_command_config(setup_dir):
        print(s)
    print()
    for s in each_sub_command_config():
        print(s)

if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:54:18.458578
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Test function: each_sub_command_config()"""
    import subprocess
    from os import makedirs
    from os.path import (
        abspath,
        basename,
        exists,
        isdir,
        join,
    )
    from shutil import rmtree

    # Create a temporary directory
    tmp_dir = abspath(join('.tmp', basename(__file__)))
    if isdir(tmp_dir):
        rmtree(tmp_dir)
    makedirs(tmp_dir)

    # Create a temporary setup.cfg
    setup_cfg_path = join(tmp_dir, 'setup.cfg')

# Generated at 2022-06-13 20:54:31.229754
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # No setup.py in this directory, so an exception will be raised
    with pytest.raises(FileNotFoundError):
        for _ in each_sub_command_config():
            pass
    here = os.path.dirname(os.path.abspath(__file__))
    here = os.path.join(here, 'setup_py_test')
    for sub_command_config in each_sub_command_config(here):
        assert isinstance(sub_command_config, SetupCfgCommandConfig)
        assert isinstance(sub_command_config.name, str)
        assert isinstance(sub_command_config.camel, str)
        assert isinstance(sub_command_config.description, str)
        assert isinstance(sub_command_config.commands, tuple)

# Generated at 2022-06-13 20:54:37.935056
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import unittest
    import pprint

    class TestEachSubCommandConfig(unittest.TestCase):
        """Tests for function each_sub_command_config."""

        def test_success(self):
            """Verifies positive results."""
            pprint.pprint(list(each_sub_command_config()))

    unittest.main(argv=['Next'], exit=False)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:54:51.597118
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile

    tf = tempfile.TemporaryDirectory()

# Generated at 2022-06-13 20:55:02.752083
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def _test(
            setup_dir: Optional[str],
            setup_dir_path: Optional[str],
            setup_dir_exists: bool,
            setup_dir_is_dir: bool,
            setup_dir_contains_setup_py: bool,
            setup_dir_contains_setup_cfg: bool,
            setup_dir_contains_setup_commands_cfg: bool,
            setup_cfg_metadata_name: str
    ) -> None:
        def _mock_exists(path: str) -> bool:
            if path == setup_dir_path:
                return setup_dir_exists
            elif path == os.path.join(setup_dir_path, 'setup.py'):
                return setup_dir_contains_setup_py

# Generated at 2022-06-13 20:55:14.699783
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import pathlib
    tdir = pathlib.Path(__file__).parent
    tdir = tdir.joinpath('data', 'setup_cfg_cmds')
    cmds = list(each_sub_command_config(setup_dir=tdir))
    assert len(cmds) == 4
    # Check the structure
    for cmd in cmds:
        assert hasattr(cmd, 'name')
        assert len(cmd.name) > 0
        assert hasattr(cmd, 'camel')
        assert len(cmd.camel) > 0
        assert hasattr(cmd, 'description')
        assert len(cmd.description) > 0
        assert hasattr(cmd, 'commands')
        assert isinstance(cmd.commands, tuple)
        assert len(cmd.commands) > 0
    # Check the values
   

# Generated at 2022-06-13 20:55:25.921804
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import textwrap
    from unittest.mock import patch
    from pprint import pformat

    # Unit test the basic funtionality
    setup_cfg = textwrap.dedent("""\
        [metadata]
        name = my_package
        version = 0.0.1

        [options]
        packages = find:
        install_requires =
        python_requires = >=3.5
    """)
    setup_cfg_path = 'setup.cfg'
    setup_cfg_dir = 'tests/unit/pysetupcommand/my_package'

# Generated at 2022-06-13 20:55:32.079160
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from ..scripts.test_scripts import setup_dir as test_setup_dir

    for config in each_sub_command_config(
        setup_dir=test_setup_dir
    ):
        assert isinstance(config.name, str)
        assert isinstance(config.camel, str)
        assert isinstance(config.description, str)
        assert isinstance(config.commands, tuple)
        for cmd in config.commands:
            assert isinstance(cmd, str)

# Generated at 2022-06-13 20:55:49.468830
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from unittest.mock import patch

    from flutils.setuputils import _get_name
    from flutils.testutils import patch_fs

    with patch.object(
            _get_name,
            side_effect=LookupError()
    ):
        with patch_fs({
            'setup.cfg': '\n',
            'setup.py': '\n'
        }):
            with pytest.raises(LookupError):
                tuple(each_sub_command_config())


# Generated at 2022-06-13 20:56:01.964022
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.abspath('tests/setup.py')

# Generated at 2022-06-13 20:56:09.915512
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    path = os.path.dirname(__file__)
    path = os.path.dirname(path)
    path = os.path.dirname(path)
    for config in each_sub_command_config(path):
        assert isinstance(config.name, str)
        assert isinstance(config.camel, str)
        assert isinstance(config.description, str)
        assert isinstance(config.commands, tuple)
        for cmd in config.commands:
            assert isinstance(cmd, str)



# Generated at 2022-06-13 20:56:13.803087
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    cmd_config: SetupCfgCommandConfig
    for cmd_config in each_sub_command_config():
        print(cmd_config)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:56:25.603608
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def out(out_gen) -> List[SetupCfgCommandConfig]:
        out: List[SetupCfgCommandConfig] = []
        for item in out_gen:
            out.append(item)
        return out
    # setup_commands.cfg contains both camel and underscore-formatted names
    # for the same command
    assert out(each_sub_command_config(setup_dir='tests')) == [
        SetupCfgCommandConfig(
            'info.cmd',
            'InfoCmd',
            'Basic info command.',
            ('echo Basic command.',)
        ),
        SetupCfgCommandConfig(
            'version.v',
            'VersionV',
            'Basic version command.',
            ('echo Basic version command.',)
        )
    ]
    # setup_commands.cfg contains only underscore-formatted names

# Generated at 2022-06-13 20:56:32.648965
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config('./pysetuptools_custom_commands'):
        assert config.name.isidentifier()
        assert config.camel.isidentifier()
        assert len(config.description)


if __name__ == '__main__':
    import pytest
    pytest.main(['--color=auto', '-q', '--pdb', '--pdbcls=IPython.terminal.debugger:Pdb'])

# Generated at 2022-06-13 20:56:39.991271
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import get_setup_dir
    import os
    for command in each_sub_command_config(setup_dir=get_setup_dir()):
        setup_dir = os.path.join(os.path.dirname(__file__), '_test-project')
        if command.name.startswith('test.'):
            assert each_sub_command_config(
                setup_dir=setup_dir
            ) is not None

# Generated at 2022-06-13 20:56:51.036239
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from pathlib import Path

    from flutils.testutils import TempCWD

    with TempCWD(as_path=True) as temp_cwd:
        setup_cfg = Path(__file__).parent / 'data/setup.cfg'
        setup_cfg.copy(temp_cwd / setup_cfg.name)
        setup_commands_cfg = Path(__file__).parent / 'data/setup_commands.cfg'
        setup_commands_cfg.copy(temp_cwd / setup_commands_cfg.name)
        setup_py = Path(__file__).parent / 'data/setup.py'
        setup_py.copy(temp_cwd / setup_py.name)

        names = [x.name for x in each_sub_command_config(temp_cwd)]

# Generated at 2022-06-13 20:57:02.993322
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for cmd in each_sub_command_config(
            os.path.join(os.path.dirname(__file__), '..')
    ):
        if cmd.name in ('build-directory', 'build', 'build_directory'):
            break
    assert cmd.name == 'build-directory'
    assert cmd.camel == 'BuildDirectory'
    assert cmd.description == 'Build directory structure on local system'

# Generated at 2022-06-13 20:57:08.158675
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    paths = os.path.abspath(__file__)
    src_dir = os.path.dirname(paths)
    print(src_dir)
    for config in each_sub_command_config(os.path.dirname(src_dir)):
        print('===========================')
        print(config.name)
        print(config.camel)
        print(config.description)
        print(config.commands)
    

# Generated at 2022-06-13 20:57:28.349488
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import pathlib
    import random
    import string
    import shutil
    import tempfile

    import pytest

    test_dir = os.path.realpath(os.path.dirname(__file__))
    test_dir = os.path.join(test_dir, '..', 'test-dir')
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    os.makedirs(test_dir, exist_ok=True)
    with open(os.path.join(test_dir, 'setup.py'), mode='w') as f:
        f.write(
            '#!/usr/bin/env python3.7\n\n'
            'from setuptools import setup\n'
            'setup()'
        )
   

# Generated at 2022-06-13 20:57:39.821337
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import subprocess
    import tempfile


# Generated at 2022-06-13 20:57:52.601265
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Test function ``each_sub_command_config``."""
    assert isinstance(each_sub_command_config, collections.abc.Callable)
    flutils_updater_setup_dir = os.path.realpath(
        os.path.join(
            os.path.dirname(__file__),
            os.path.pardir,
            os.path.pardir,
            os.path.pardir
        )
    )
    configs = list(each_sub_command_config(flutils_updater_setup_dir))

# Generated at 2022-06-13 20:57:53.250900
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    pass

# Generated at 2022-06-13 20:57:58.596469
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import io
    import unittest
    import tempfile

    try:
        from StringIO import StringIO
    except ImportError:
        from io import StringIO


# Generated at 2022-06-13 20:58:10.231826
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from textwrap import dedent
    from tempfile import mkdtemp
    from shutil import rmtree

    name = 'some.package'
    temp_dir = mkdtemp()

# Generated at 2022-06-13 20:58:18.572073
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    print('Testing function "each_sub_command_config"...')
    print(
        "The following command lines should be in the setup.cfg file:\n"
        "  [console_scripts]\n"
        "  flutils-setup-sub-commands = "
        "flutils.setup_utils:print_sub_commands"
    )

    for cfg in each_sub_command_config(setup_dir=None):
        print()
        print('Name:', cfg.name)
        print('Camel:', cfg.camel)
        print('Description:', cfg.description)
        print('Commands:')
        if cfg.commands:
            for command in cfg.commands:
                print('  ', command, sep='')

# Generated at 2022-06-13 20:58:31.246417
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.join('tests', 'command', 'sample_app')
    sub_commands = []
    for sub_command in each_sub_command_config(setup_dir):
        sub_commands.append(sub_command)
    assert len(sub_commands) == 3
    assert len(sub_commands[0].commands) == 1
    assert sub_commands[0].commands[0] == 'echo "cmd1 args: $@"'
    assert len(sub_commands[1].commands) == 1
    assert sub_commands[1].commands[0] == 'echo "cmd2 args: $@"'
    assert len(sub_commands[2].commands) == 2

# Generated at 2022-06-13 20:58:39.881608
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import each_dir_path_exists
    import pprint
    setup_dir = '/Users/jasonrichardsmith/Projects/flutils/nsis'
    for sub_command in each_sub_command_config(setup_dir):
        pprint.pprint(sub_command.__dict__)
    assert each_dir_path_exists(setup_dir)
    assert setup_dir.endswith('nsis')

# Run unit test when called directly
if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:58:50.009100
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import get_module_filename

    setup_cfg_path = os.path.join(
        os.path.dirname(get_module_filename()),
        'setup.cfg'
    )
    assert os.path.isfile(setup_cfg_path) is True, setup_cfg_path

    parser = ConfigParser()
    parser.read(setup_cfg_path)
    format_kwargs = {
        'setup_dir': os.path.dirname(setup_cfg_path),
        'home': os.path.expanduser('~'),
        'name': _get_name(parser, setup_cfg_path)
    }

    vals: List[SetupCfgCommandConfig] = list(
        _each_setup_cfg_command(parser, format_kwargs)
    )
   

# Generated at 2022-06-13 20:59:15.922094
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # Test with NO setup dir
    itr = each_sub_command_config()
    cmds = list(itr)
    del itr
    if len(cmds) < 1:
        raise ValueError("Must have more than 1 'setup.command.*' commands")
    for cmd in cmds:
        if not isinstance(cmd.name, str):
            raise TypeError("The 'name' MUST be a str type")
        if not isinstance(cmd.camel, str):
            raise TypeError("The 'camel' MUST be a str type")
        if not isinstance(cmd.description, str):
            raise TypeError("The 'description' MUST be a str type")
        if not isinstance(cmd.commands, tuple):
            raise TypeError("The 'commands' MUST be a tuple type")

# Generated at 2022-06-13 20:59:28.139788
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    out = list(each_sub_command_config(r'd:\workspaces\flutils-dev'))

# Generated at 2022-06-13 20:59:37.296744
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.config import DIR_PATH
    from flutils.pathutils import get_basename
    dir_path = DIR_PATH
    for x in each_sub_command_config(dir_path):
        name_ = get_basename(dir_path)
        if x.name.replace(name_ + '.', '') == 'help':
            assert x.camel == 'CommandHelp'
            assert x.description == \
                   "Shows the help message and exit."
            assert x.commands == ('--help', '-h')
            break

# Generated at 2022-06-13 20:59:42.524535
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    configs = list(each_sub_command_config('../'))
    assert configs
    names = [c.name for c in configs]
    assert 'flutils.logutils.set_logger' in names
    assert 'flutils.osutils.copy_file' in names
    assert 'flutils.osutils.remove_path' in names

# Generated at 2022-06-13 20:59:56.531713
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import pathlib
    from os.path import expanduser
    from pytest import fixture

    @fixture(scope='module')
    def setup_dir(tmpdir_module: pathlib.Path) -> str:
        setup_cfg = tmpdir_module / 'setup.cfg'
        setup_cfg.write_text(
            ''
            '[metadata]\n'
            'name = sample\n'
        )
        setup_cmds = tmpdir_module / 'setup_commands.cfg'

# Generated at 2022-06-13 21:00:07.421132
# Unit test for function each_sub_command_config

# Generated at 2022-06-13 21:00:16.421959
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    cwd = os.getcwd()
    try:
        path = os.path.join(cwd, '..', '..', 'tests', 'setup_commands')
        os.chdir(path)
        for config in each_sub_command_config():
            print(config.name)
            print(config.camel)
            print(config.description)
            print(config.commands)
    finally:
        os.chdir(cwd)


if __name__ == '__main__':
    import sys
    sys.exit(test_each_sub_command_config())

# Generated at 2022-06-13 21:00:27.400318
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import unittest.mock
    import sys

    mock_parser = unittest.mock.MagicMock()

    class MockParser(object):
        def __contains__(self, value):
            return value == 'setup.command.test'

        @property
        def options(self):
            return mock_parser.options

        @property
        def sections(self):
            return mock_parser.sections

        def get(self, section, option):
            if section == 'setup.command.test':
                return ' '.join(sys.argv)
            if section == 'metadata':
                return 'pretend_project'
            return ''

    parser = MockParser()
    mock_parser.options.return_value = ['command', 'name', 'description']

# Generated at 2022-06-13 21:00:32.662113
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    cwd = os.path.dirname(__file__)
    cwd = os.path.join(cwd, 'res', 'test')

    for sub_cmd_cfg in each_sub_command_config(cwd):
        assert isinstance(sub_cmd_cfg, SetupCfgCommandConfig)

# Generated at 2022-06-13 21:00:44.022824
# Unit test for function each_sub_command_config

# Generated at 2022-06-13 21:01:09.672067
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    func = each_sub_command_config

    results = list(func(setup_dir='fltestutils/test/testproj1'))
    assert len(results) == 1
    assert results[0].name == 'mytestproj.test1'
    assert results[0].camel == 'Mytestproj_Test1'
    assert results[0].description == (
        'Runs one of the varous tests for MyTestProj.'
    )
    assert results[0].commands == ('echo command 1', 'echo command 2')

    results = list(func(setup_dir='fltestutils/test/testproj2'))
    assert len(results) == 0

    results = list(
        func(setup_dir='fltestutils/test/testproj3')
    )

# Generated at 2022-06-13 21:01:17.926398
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'flutils')
    )
    assert os.path.isfile(os.path.join(setup_dir, 'setup.py'))
    assert os.path.isfile(os.path.join(setup_dir, 'setup.cfg'))
    assert os.path.isfile(os.path.join(setup_dir, 'setup_commands.cfg'))
    found = False
    for sub_command_config in each_sub_command_config(setup_dir):
        if sub_command_config.camel != 'Test':
            continue
        assert sub_command_config.name == 'test'
        assert sub_command_config.description == ('Run the test suite.')

# Generated at 2022-06-13 21:01:27.177709
# Unit test for function each_sub_command_config

# Generated at 2022-06-13 21:01:33.500777
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_cfg_path = os.path.join('tests', 'data', 'setup_commands.cfg')
    for sub_command_config in each_sub_command_config(setup_cfg_path):
        assert sub_command_config.name
        assert sub_command_config.camel
        assert sub_command_config.description
        assert sub_command_config.commands

# Generated at 2022-06-13 21:01:37.017336
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for sc in each_sub_command_config():
        print(sc)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:01:38.836336
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config():
        print(config)

# Generated at 2022-06-13 21:01:49.187858
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from click.testing import CliRunner
    from pathlib import Path
    from flutils.configutils import (
        each_sub_command_config,
        setup_cfg_parser,
    )
    from flutils.pathutils import each_file_in_dir

    cwd = os.getcwd()
    setup_dir = os.path.dirname(os.path.dirname(__file__))
    os.chdir(setup_dir)

# Generated at 2022-06-13 21:01:58.437823
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    _ = None
    def cb_test():
        commands: Dict[str, str] = {}
        for command in each_sub_command_config(_):
            assert isinstance(command, SetupCfgCommandConfig)
            commands[command.name] = command.description

# Generated at 2022-06-13 21:02:09.449342
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # main_func_setup_dir
    #     found NO SETUP.PY FILE
    c = each_sub_command_config(os.path.dirname(__file__))
    for i in c:
        assert False

    # main_func_setup_dir
    #     Found SETUP.PY FILE
    c = each_sub_command_config(os.path.dirname(__file__))
    for i in c:
        assert False

    # main_func_setup_dir
    #     found NO SETUP.PY FILE
    c = each_sub_command_config(os.path.dirname(__file__))
    for i in c:
        assert False


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:02:16.652950
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config."""
    # version_py_path = os.path.join(os.path.dirname(__file__), 'version.py')
    config = list(each_sub_command_config())
    assert len(config) > 0
    for cfg in config:
        print(cfg)

# Generated at 2022-06-13 21:02:48.189735
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    cmds_itr = each_sub_command_config('../flutils')
    commands = list(cmds_itr)

    assert len(commands) == 2

    flutils_doc_cmds = set(
        '''
        python setup_commands.py -s ../flutils/src/flutils/docs_gen.py docs_gen
        '''.strip().splitlines()
    )
    for x in commands:
        if x.camel == 'FlutilsDocsGen':
            assert set(x.commands) == flutils_doc_cmds
            flutils_doc_cmds = None
            break


# Generated at 2022-06-13 21:02:55.812645
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with pytest.raises(LookupError):
        list(each_sub_command_config('/no/such/dir'))
    with pytest.raises(LookupError):
        list(each_sub_command_config('/etc'))
    with pytest.raises(FileNotFoundError):
        list(each_sub_command_config())
    with pytest.raises(FileNotFoundError):
        list(each_sub_command_config('.'))
    with pytest.raises(FileNotFoundError):
        list(each_sub_command_config('./tests/'))


# Generated at 2022-06-13 21:03:09.192091
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    script_dir = os.path.dirname(__file__)
    script_dir = os.path.realpath(script_dir)
    test_dir = os.path.join(script_dir, 'test_project')
    test_dir = os.path.realpath(test_dir)
    for i, command in enumerate(each_sub_command_config(test_dir)):
        if i == 0:
            assert command.name == 'test_project.clean'
            assert command.camel == 'TestProjectClean'
            assert command.description == 'cleans test project.'
            assert command.commands == ('rm -rf *.egg-info',)
        elif i == 1:
            assert command.name == 'test_project.sdist'
            assert command.camel == 'TestProjectSDist'

# Generated at 2022-06-13 21:03:17.602026
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    filepath = os.path.realpath(__file__)
    setup_dir = os.path.dirname(os.path.dirname(filepath))
    g = each_sub_command_config(setup_dir)
    config = next(g)
    assert isinstance(config, SetupCfgCommandConfig)
    assert config.name == 'test'
    assert config.commands == (
        "echo 'Running flutils unit tests'",
        "echo 'Running Pyflakes unit tests'",
        "pyflakes flutils/test.py flutils/test_setup_cfg_parser.py"
    )


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:03:22.801571
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from pprint import pprint
    pprint(list(each_sub_command_config()))


__all__ = (
    'each_sub_command_config',
    'SetupCfgCommandConfig',
)



# Generated at 2022-06-13 21:03:34.124481
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import unittest

    class TestSetupCfg(unittest.TestCase):

        def test_each_sub_command_config(self):
            from importlib import resources

            with resources.path(
                    'flutils.setuputils.tests.example',
                    'setup.cfg'
            ) as setup_cfg_path:
                setup_dir = os.path.dirname(setup_cfg_path)
                for cfg in each_sub_command_config(setup_dir):
                    self.assertIsInstance(cfg, SetupCfgCommandConfig)
                    self.assertIsInstance(cfg.name, str)
                    self.assertTrue(cfg.name)
                    self.assertIsInstance(cfg.camel, str)
                    self.assertTrue(cfg.camel)
                    self.assertIsInstance(cfg.description, str)
