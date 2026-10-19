

# Generated at 2022-06-13 20:54:03.111356
# Unit test for function each_sub_command_config
def test_each_sub_command_config():

    import tempfile

    # Without a setup.cfg file.
    with tempfile.TemporaryDirectory() as temp_dir:
        setup_dir = os.path.join(temp_dir, 'test_each_sub_command_config')
        os.mkdir(setup_dir)
        setup_py_path = os.path.join(setup_dir, 'setup.py')
        with open(setup_py_path, 'w') as fd:
            fd.write('')
        with pytest.raises(FileNotFoundError):
            next(each_sub_command_config(temp_dir))

    with tempfile.TemporaryDirectory() as temp_dir:
        setup_dir = os.path.join(temp_dir, 'test_each_sub_command_config')

# Generated at 2022-06-13 20:54:08.645457
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    path = os.path.join(os.path.dirname(__file__), 'fixtures', 'setup_commands')
    yield from each_sub_command_config(path)

# vim: set ts=4 sw=4 tw=79 filetype=python et :

# Generated at 2022-06-13 20:54:12.365010
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    try:
        print('\nFunction each_sub_command_config():')
        print('\nCalling each_sub_command_config():')
        for config in each_sub_command_config():
            print('    Command: %r' % config.name)
            print('    Description: %r' % config.description)
            print()
            print('    Commands:')
            for cmd in config.commands:
                print('        %s' % cmd)
        print('-' * 100)
    except Exception as e:
        print('    Exception raised: %s' % e)
    print('Done!\n')


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:54:14.140128
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # TODO: Write unit test for function each_sub_command_config
    pass

# Generated at 2022-06-13 20:54:24.948929
# Unit test for function each_sub_command_config
def test_each_sub_command_config():

    def do_test(
            setup_dir: Optional[Union[os.PathLike, str]],
            expected: Tuple[SetupCfgCommandConfig, ...]
    ) -> None:
        out = tuple(each_sub_command_config(setup_dir))
        assert out == expected

    setup_dir = os.path.join(
        os.path.dirname(__file__),
        'fixtures',
        'commands'
    )

# Generated at 2022-06-13 20:54:26.462250
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for x in each_sub_command_config():
        print(x)



# Generated at 2022-06-13 20:54:38.902021
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config."""
    import sys
    import unittest
    from tempfile import TemporaryDirectory
    from shutil import rmtree
    import pathlib
    import io
    from unittest.mock import patch, Mock

    class TestCase(unittest.TestCase):
        def test(self):
            with TemporaryDirectory() as tmp_dir:
                path = os.path.join(tmp_dir, 'setup.cfg')
                with open(path, 'w') as fd:
                    fd.write("[metadata]\n\n")
                    fd.write("name = project_name\n\n")
                    fd.write("[setup.command.test]\n\n")
                    fd.write("commands = pytest\n\n")
                    f

# Generated at 2022-06-13 20:54:52.140364
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    dirname = os.path.dirname(__file__)
    filename = 'setup.cfg'
    setup_cfg_path = os.path.join(dirname, filename)
    parser = ConfigParser()
    parser.read(setup_cfg_path)
    format_kwargs: Dict[str, str] = {
        'setup_dir': _prep_setup_dir(),
        'home': os.path.expanduser('~')
    }
    format_kwargs['name'] = _get_name(parser, setup_cfg_path)
    path = os.path.join(format_kwargs['setup_dir'], 'setup_commands.cfg')
    if os.path.isfile(path):
        parser = ConfigParser()
        parser.read(path)

# Generated at 2022-06-13 20:55:02.789357
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import unittest
    import io
    from typing import Any

    cfg_text = """
[setup.command.foo]
name = {name}-foo
description = Runs the foo command
command = 
    python setup.py foo
    python setup.py foo
    python setup.py foo

[setup.command.bar]
name = {name}-bar
description = Runs the bar command
command = 
    python setup.py bar
    python setup.py bar
    python setup.py bar

[setup.command.baz]
name = {name}-baz
description = Runs the baz command
command = 
    python setup.py baz
    python setup.py baz
    python setup.py baz
    """


# Generated at 2022-06-13 20:55:08.389503
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for sc in each_sub_command_config('tests/test_project'):
        print(sc)
        assert sc.name == 'test'
        assert sc.camel == 'TestCommand'
        assert sc.description == 'the test command'
        assert sc.commands == ('echo "test"',)
        break
    return


# Generated at 2022-06-13 20:55:24.516672
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config():
        assert type(config) is SetupCfgCommandConfig
        assert type(config.name) is str
        assert type(config.camel) is str
        assert type(config.description) is str
        assert type(config.commands) is tuple
        for cmd in config.commands:
            assert type(cmd) is str

# Generated at 2022-06-13 20:55:31.587185
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    path = os.path.join('/', 'tmp', '__pycache__')
    path = os.path.join(path, 'foo')
    if os.path.exists(path) is False:
        os.makedirs(path)
    path = os.path.join(path, '__setup_commands__.py')
    if os.path.isfile(path):
        os.remove(path)
    path = os.path.join('/', 'tmp', '__setup_commands__')
    if os.path.exists(path) is False:
        os.makedirs(path)
    path = os.path.join(path, 'setup.py')
    with open(path, 'w') as wh:
        wh.write('#')

# Generated at 2022-06-13 20:55:33.613290
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    next(each_sub_command_config(os.path.join(
        os.path.dirname(__file__), '..', '..')))

# Generated at 2022-06-13 20:55:39.636455
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.dirname(os.path.dirname(__file__))
    for cmd in each_sub_command_config(setup_dir):
        print(cmd.name)
        print(cmd.camel)
        print(cmd.description)
        print(cmd.commands)
        print()


if __name__ == "__main__":
    test_each_sub_command_config()

# Generated at 2022-06-13 20:55:43.954666
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.dirname(__file__)
    setup_dir = os.path.join(setup_dir, 'mock_setup')
    configs = list(each_sub_command_config(setup_dir))
    assert len(configs) == 1
    assert setup_dir in configs[0].commands[0]

if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:55:58.763413
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    this_dir = os.path.abspath(os.path.dirname(__file__))
    src_dir = os.path.abspath(os.path.join(this_dir, '..', 'src'))
    src_setup_cfg = os.path.abspath(os.path.join(src_dir, 'setup.cfg'))
    actual = list(
        each_sub_command_config(setup_dir=src_setup_cfg)
    )

# Generated at 2022-06-13 20:56:12.102774
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def _test(
            cwd: os.PathLike,
            setup_dir: Optional[Union[os.PathLike, str]] = None,
            setup_cfg_data: Optional[str] = None,
            setup_cmd_data: Optional[str] = None
    ) -> Generator[None, None, None]:
        with TemporaryDirectory() as tmp:
            # Create the setup.cfg file
            if setup_cfg_data is None:
                setup_cfg_data = (
                    """\
                    [metadata]
                    name = "testing_project"
                    """
                )
            setup_cfg_file = os.path.join(tmp, 'setup.cfg')
            with open(setup_cfg_file, 'wt') as out:
                out.write(setup_cfg_data)


# Generated at 2022-06-13 20:56:18.812634
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # noinspection PyUnresolvedReferences
    import flutils.testing as fltt

    def _assert_command(
            config: SetupCfgCommandConfig,
            name: str,
            camel: str,
            description: str,
            commands: Optional[Iterable[str]],
    ):
        if commands is not None:
            commands = tuple(commands)
        assert config.name == name
        assert config.camel == camel
        assert config.description == description
        assert config.commands == commands


# Generated at 2022-06-13 20:56:23.188448
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    configs: List[SetupCfgCommandConfig] = list(each_sub_command_config())
    assert len(configs) > 0
    assert all(c.description for c in configs)
    assert all(c.commands for c in configs)

# Generated at 2022-06-13 20:56:34.706526
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Test the function each_sub_command_config."""
    from flutils.pathutils import temporary_directory
    from pathlib import Path
    from subprocess import CalledProcessError
    from unittest import TestCase

    class EachSubCommandConfigTestCase(TestCase):

        def test_each_sub_command_config(self):
            """Test the function each_sub_command_config."""
            with temporary_directory() as d:
                expected = []
                name = 'test_project'
                d = Path(d)
                d = d.joinpath(name)
                d.mkdir()
                d = d.absolute()
                (d / 'setup.py').touch(0o600)
                setup_cfg = d / 'setup.cfg'
                setup_cfg.touch(0o600)
                parser = ConfigParser

# Generated at 2022-06-13 20:56:51.901959
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    entries = tuple(each_sub_command_config(setup_dir='.'))

# Generated at 2022-06-13 20:57:03.613106
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.realpath(os.path.join(path, '../test_data/testproj'))
    path = os.path.realpath(os.path.join(path, 'setup.cfg'))
    parser = ConfigParser()
    parser.read(path)
    format_kwargs = {
        'name': _get_name(parser, path),
        'setup_dir': os.path.dirname(path),
        'home': os.path.expanduser('~')
    }
    out = list(_each_setup_cfg_command(parser, format_kwargs))
    assert out[0].name == "test"
    assert out[0].camel == "Test"

# Generated at 2022-06-13 20:57:11.418517
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from os import path

    from flutils.pathutils import get_repository_root

    root = get_repository_root()
    setup_cfg = path.join(root, 'setup.cfg')
    setup_commands = path.join(root, 'setup_commands.cfg')

    parser = ConfigParser()
    parser.read(setup_cfg)
    name = _get_name(parser, setup_cfg)

    parser = ConfigParser()
    parser.read(setup_commands)
    format_kwargs = {'name': name}
    setup_commands = list(_each_setup_cfg_command(parser, format_kwargs))

    assert len(setup_commands) > 0



# Generated at 2022-06-13 20:57:25.583477
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from sys import stdout, stderr
    from textwrap import dedent

    val: List[SetupCfgCommandConfig] = list(each_sub_command_config())
    stderr.write(
        "There are %r sub commands.\n"
        % len(val)
    )

# Generated at 2022-06-13 20:57:33.322374
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.realpath(
        os.path.join(os.path.dirname(__file__), '..')
    )
    for command_config in each_sub_command_config(setup_dir):
        assert isinstance(command_config.name, str)
        assert isinstance(command_config.camel, str)
        assert isinstance(command_config.description, str)
        assert isinstance(command_config.commands, tuple)
        assert all(isinstance(command, str) for command in command_config.commands)



# Generated at 2022-06-13 20:57:43.669526
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from unittest.mock import patch

    def fake_is_file(path):
        if os.path.basename(path) == 'setup.cfg':
            return True
        return False

    def fake_read():
        parser = ConfigParser()
        section = 'metadata'
        parser.add_section(section)
        parser.set(section, 'name', 'foo')
        section = 'setup.command.bar'
        parser.add_section(section)
        parser.set(section, 'command', 'echo -n {}')
        section = 'setup.command.baz'
        parser.add_section(section)
        parser.set(section, 'name', 'Baz')
        parser.set(section, 'description', 'This bar {}')

# Generated at 2022-06-13 20:57:56.252323
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import textwrap
    import unittest

    class TestEachSubCommandConfig(unittest.TestCase):
        def test_each_sub_command_config(self):
            test_setup_cfg = """
                [metadata]
                name = flutils
                version = 0.1.0
                project_urls =
                    Foo = https://foo.com/
                    Bar = https://bar.com/

                [options]
                packages =
                    flutils
                zip_safe = False
                package_dir =
                    = src
            """
            test_setup_cfg = textwrap.dedent(test_setup_cfg).strip()

# Generated at 2022-06-13 20:58:00.447369
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for info in each_sub_command_config(setup_dir='/Users/chill/projects/jottalib'):
        print(info)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:58:12.512046
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for cmd_cfg in each_sub_command_config('tests/data/pysetup'):
        assert cmd_cfg.name == 'run'
        assert cmd_cfg.camel == 'Run'
        assert cmd_cfg.description == ''
        assert cmd_cfg.commands == (
            'pytest',
        )
    for cmd_cfg in each_sub_command_config('tests/data/pysetup2'):
        assert cmd_cfg.name == 'run'
        assert cmd_cfg.camel == 'Run'
        assert cmd_cfg.description == ''
        assert cmd_cfg.commands == (
            'pytest',
        )


if __name__ == '__main__':
    import sys
    sys.exit(test_each_sub_command_config())

# Generated at 2022-06-13 20:58:23.014962
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    the_dir = os.path.dirname(__file__)
    for cfg in each_sub_command_config(the_dir):  # noqa
        assert isinstance(cfg, SetupCfgCommandConfig)
        assert isinstance(cfg.name, str)
        assert isinstance(cfg.camel, str)
        assert isinstance(cfg.description, str)
        assert isinstance(cfg.commands, tuple)
        for cmd in cfg.commands:  # noqa
            assert isinstance(cmd, str)

# Generated at 2022-06-13 20:58:40.773837
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Generated at 2022-06-13 20:58:50.445894
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil

    def _create_setup_dir(**kwargs):
        """Creates a temporary directory for testing
        ``each_sub_command_config()``.
        """

# Generated at 2022-06-13 20:59:04.481813
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from io import StringIO
    import tempfile

    config_str = """
    [metadata]
    name = flutils-test

    [setup.command.test]
    command = 
        echo Running pytest
        pytest -vv
    description = Runs pytest on the main package
    name = Run pytest
    """

    with tempfile.TemporaryDirectory() as tmpdir:
        cfg_file = os.path.join(tmpdir, 'setup.cfg')
        with open(cfg_file, 'w') as out:
            out.write(config_str)
        with open(os.path.join(tmpdir, 'setup.py'), 'w') as out:
            out.write('\n')

# Generated at 2022-06-13 20:59:15.314700
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import unittest.mock

    def fake_each_setup_cfg_command(
            parser: ConfigParser,
            format_kwargs: Dict[str, str]
    ) -> Generator[SetupCfgCommandConfig, None, None]:
        for command in ('one', 'two'):
            yield SetupCfgCommandConfig(
                '%s.%s' % (format_kwargs['name'], command),
                '%s%sCommand' % (format_kwargs['name'],
                                 command.title().replace('-', '')),
                'The description for command %s.' % command,
                ('%s_command' % command, )
            )

# Generated at 2022-06-13 20:59:22.350351
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import pathlib
    cwd = pathlib.Path.cwd()
    expected = SetupCfgCommandConfig(
        name='init',
        camel='Init',
        description='Initializes the project.',
        commands=('python3 {}/setup.py init --help'.format(cwd),)
    )
    for actual in each_sub_command_config():
        assert actual == expected
        return
    raise AssertionError('Did not iterate over the expected value.')

# Generated at 2022-06-13 20:59:27.138711
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    cmd_name = '.'.join(__name__.split('.')[:-1])
    for cmd in each_sub_command_config(os.path.dirname(__file__)):  # noqa
        assert cmd.name == cmd_name



# Generated at 2022-06-13 20:59:32.167168
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    list(each_sub_command_config())
    list(each_sub_command_config(os.path.dirname(__file__)))

if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:59:34.587219
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    results = tuple(each_sub_command_config())
    assert len(results) > 0

# Generated at 2022-06-13 20:59:41.834417
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for cfg in each_sub_command_config('tests/data/test_package'):
        assert cfg.name == 'test_command'
        assert cfg.camel == 'TestCommand'
        assert cfg.description == 'test command'
        assert cfg.commands == (
            'cd ~/test_project_dir && python -m test_package.test_command',
            'echo TEST COMMAND'
        )

# Generated at 2022-06-13 20:59:55.847099
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_cfg = '''
[metadata]
name = test_setup_cfg_parse
description = Our test project.

[setup.command.test.one]
name = {name}.test_one
description = Description for "test_one" setup command.
command = echo "Test setup command 'one'."
'''
    setup_dir = os.path.abspath('test')
    try:
        os.makedirs(setup_dir)
    except FileExistsError:
        pass
    setup_cfg_path = os.path.join(setup_dir, 'setup.cfg')
    with open(setup_cfg_path, 'w') as fh:
        fh.write(setup_cfg)
    res = list(each_sub_command_config(setup_dir))
    assert len(res) == 1
   

# Generated at 2022-06-13 21:00:15.036977
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """
    Test the function each_sub_command_config
    """
    file_path = os.path.dirname(__file__)
    setup_cfg_path = os.path.join(file_path, 'test_data', 'setup.cfg')
    parser = ConfigParser()
    parser.read(setup_cfg_path)
    format_kwargs = {
        'setup_dir': os.path.realpath(file_path),
        'home': os.path.expanduser('~')
    }
    format_kwargs['name'] = _get_name(parser, setup_cfg_path)
    path = os.path.join(file_path, 'test_data', 'setup_commands.cfg')
    if os.path.isfile(path):
        parser = ConfigParser()
        parser.read

# Generated at 2022-06-13 21:00:20.029498
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for expected, actual in zip(
            (
                ('test_b', 'TestB', 'Test b command.', ('echo B',)),
                ('test_a', 'TestA', 'Test a command.', ('echo A',)),
            ),
            each_sub_command_config('test_setup')):
        assert isinstance(actual, SetupCfgCommandConfig)
        assert expected == actual

# Generated at 2022-06-13 21:00:29.435025
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    path, repo = os.path.split(os.path.dirname(__file__))
    _, package_name = os.path.split(path)

    for config in each_sub_command_config(path):
        assert hasattr(config, 'name')
        assert hasattr(config, 'camel')
        assert hasattr(config, 'description')
        assert hasattr(config, 'commands')

        expected = '%s.%s' % (
            package_name,
            ''.join([s.capitalize() for s in config.name.split('-')])
        )
        assert config.camel == expected



# Generated at 2022-06-13 21:00:36.961751
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    import pprint
    from flutils.pathutils import parent_directory, safe_makedirs

    def _create_files():
        nonlocal this_dir, setup_cfg_path, setup_commands_cfg_path
        this_dir = parent_directory(os.path.realpath(__file__))
        this_dir = os.path.join(this_dir, '..', '..', 'this_project')
        this_dir = os.path.realpath(this_dir)

        safe_makedirs(this_dir, exist_ok=True)

        setup_cfg_path = os.path.join(this_dir, 'setup.cfg')

# Generated at 2022-06-13 21:00:41.899785
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.join(os.path.dirname(__file__), '..')
    for cmd_config in each_sub_command_config(setup_dir):
        print(cmd_config)


if __name__ == '__main__':
    # test_each_sub_command_config()
    pass

# Generated at 2022-06-13 21:00:52.263346
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    cur_dir = os.path.dirname(__file__)
    root_setup_dir = os.path.join(cur_dir, '..', '..', '..')
    root_setup_dir = os.path.realpath(root_setup_dir)
    root_setup_dir = os.path.join(root_setup_dir, 'test', 'data')
    root_setup_dir = os.path.join(root_setup_dir, 'demopkg')
    cmd_config: List[SetupCfgCommandConfig] = list(
        each_sub_command_config(root_setup_dir)
    )

# Generated at 2022-06-13 21:01:03.812846
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    import sys
    import unittest

    import tempfile

    class TestFunctions(unittest.TestCase):

        def test_each_sub_command_config(self):
            # Get the path to this file.
            setup_dir = os.path.dirname(os.path.abspath(__file__))

            # Create the temporary setup commands file.
            with tempfile.NamedTemporaryFile(
                mode='w',
                    suffix='.cfg',
                    delete=False
            ) as fp:
                print("""[setup.command.test]
name = {name}
description = This is a test
command =
    echo "Hello, World!"

""", file=fp)
            self.addCleanup(os.remove, fp.name)

            # Test that the setup commands file

# Generated at 2022-06-13 21:01:12.722751
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import pprint
    from flutils.pathutils import here
    for config in each_sub_command_config(here(__file__)):
        pprint.pprint('Name')
        pprint.pprint(config.name)
        pprint.pprint('Camel')
        pprint.pprint(config.camel)
        pprint.pprint('Description')
        pprint.pprint(config.description)
        pprint.pprint('Commands')
        pprint.pprint(config.commands)
        print()


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:01:20.916830
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    assert list(each_sub_command_config(
        setup_dir='flutils/tests/data/flutils/project1'
    )) == [
        SetupCfgCommandConfig(
            'deploy_production',
            'DeployProduction',
            'Deploy to the production server.',
            (
                'pipenv run fab -f fabfile.py production all',
            )
        ),
        SetupCfgCommandConfig(
            'run_tests',
            'RunTests',
            'Run the unit tests.',
            (
                'pipenv run pytest',
            )
        )
    ]

# Generated at 2022-06-13 21:01:33.220273
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.dirname(os.path.dirname(__file__))
    assert(os.path.isdir(setup_dir))
    # Note that the '--name' and '--description' options are ignored, as
    # they are set in the setup_commands.cfg file.
    for cfg in each_sub_command_config(setup_dir):
        assert(cfg.name)
        assert(cfg.camel)
        assert(cfg.description)
        for command in cfg.commands:
            assert(command)
    # Invalid setup_dir
    with pytest.raises(NotADirectoryError):
        list(each_sub_command_config('/tmp/pytest-of-root/'))
    # Missing setup_commands.cfg file

# Generated at 2022-06-13 21:01:55.330876
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    cur_dir = os.path.dirname(__file__)
    setup_cfg_path = os.path.join(cur_dir, 'setup.cfg')
    parser = ConfigParser()
    parser.read(setup_cfg_path)

    format_kwargs: Dict[str, str] = {
        'setup_dir': cur_dir,
        'home': os.path.expanduser('~')
    }
    format_kwargs['name'] = _get_name(parser, setup_cfg_path)
    path = os.path.join(format_kwargs['setup_dir'], 'setup_commands.cfg')
    if os.path.isfile(path):
        parser = ConfigParser()
        parser.read(path)


# Generated at 2022-06-13 21:02:03.660935
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.dirname(__file__)
    n = os.path.basename(setup_dir)
    for config in each_sub_command_config(setup_dir):
        assert config.name
        assert config.camel
        assert config.description
        assert config.commands
        assert config.commands[0].startswith('python setup.py')
        assert config.commands[0].endswith(n)

# Generated at 2022-06-13 21:02:05.973905
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for result in each_sub_command_config('tests/data/setup_project'):
        print(result)



# Generated at 2022-06-13 21:02:13.648804
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    results = list(each_sub_command_config())
    assert isinstance(results, list)
    for result in results:
        assert isinstance(result, SetupCfgCommandConfig)
        assert isinstance(result.name, str)
        assert isinstance(result.camel, str)
        assert isinstance(result.description, str)
        assert isinstance(result.commands, tuple)
        for command in result.commands:
            assert isinstance(command, str)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:02:25.747530
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    import pprint
    from flutils.pathutils import each_find_dir
    from flutils.logutils import setup_logging

    log = setup_logging(level='debug')

    def test(setup_dir: str) -> None:
        log.info('')
        log.info('setup_dir: %s', setup_dir)
        try:
            for config in each_sub_command_config(setup_dir):
                log.info('')
                log.info('  Config:')
                log.info(
                    pprint.pformat(config, indent=4, width=80)
                )
        except Exception as e:
            log.error('Error: %s', e, exc_info=True)


# Generated at 2022-06-13 21:02:37.986010
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    r"""Tests function each_sub_command_config()."""
    from os import path
    from pathlib import Path
    from tempfile import TemporaryDirectory
    from unittest.mock import patch

    setup_dir = TemporaryDirectory()

# Generated at 2022-06-13 21:02:45.542687
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import tempfile
    with tempfile.TemporaryDirectory() as temp_dir:
        setup_py_file = """
        import os
        import setuptools
        setuptools.setup(name='Test_Package')
        """.strip()
        temp_py_file = os.path.join(temp_dir, 'setup.py')
        with open(temp_py_file, 'w') as stream:
            stream.write(setup_py_file)
        sys.path.insert(0, temp_dir)
        yield from each_sub_command_config()

# Generated at 2022-06-13 21:02:49.388410
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    config = set(each_sub_command_config())
    assert config == {
        SetupCfgCommandConfig('test', 'Test', 'test', ('echo foo',)),
        SetupCfgCommandConfig('other.test', 'OtherTest', 'test', ('pwd',)),
    }

# Generated at 2022-06-13 21:02:57.994850
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from os.path import dirname, join
    import sys
    for cfg in each_sub_command_config():
        assert cfg.name
        assert cfg.camel
        assert cfg.description
        assert isinstance(cfg.commands, (tuple, ))
    for cfg in each_sub_command_config():
        for cmd in cfg.commands:
            assert cmd
    if sys.platform == 'win32':
        for cfg in each_sub_command_config(join('c:', 'dev', 'flutils')):
            assert cfg.name
            assert cfg.camel
            assert cfg.description
            assert isinstance(cfg.commands, (tuple, ))

# Generated at 2022-06-13 21:03:11.004955
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # Current module's directory.
    setup_dir = os.path.realpath(os.path.dirname(__file__))

    # Verify that the current directory's setup.cfg file is read.
    cfgs = list(
        each_sub_command_config(setup_dir=setup_dir)
    )
    assert cfgs
    cc = cfgs[0]
    assert cc.camel == 'SetupPy3'
    assert isinstance(cc.description, str)
    assert isinstance(cc.commands, tuple)
    assert isinstance(cc.commands[0], str)

    # Verify that the current directory's setup_commands.cfg file is read.
    setup_commands_cfg = os.path.join(setup_dir, 'setup_commands.cfg')

# Generated at 2022-06-13 21:03:39.018569
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os.path as osp
    from flutils.testutils import TEST_BASE_DIR
    each_sub_command_config(TEST_BASE_DIR)
    each_sub_command_config(osp.join(TEST_BASE_DIR, 'testpkg'))
    each_sub_command_config()