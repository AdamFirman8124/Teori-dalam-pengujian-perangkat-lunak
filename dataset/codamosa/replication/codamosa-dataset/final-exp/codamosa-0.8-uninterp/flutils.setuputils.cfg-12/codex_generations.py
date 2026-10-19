

# Generated at 2022-06-13 20:54:00.717105
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # GIVEN:
    # WHEN:
    # First pass (no setup_dir specified)
    configs: List[SetupCfgCommandConfig] = list(each_sub_command_config())
    # Second pass (use the setup_dir from the first pass)
    setup_dir = os.path.dirname(configs[0].description)
    configs2 = list(each_sub_command_config(setup_dir))
    # THEN:
    assert setup_dir == os.path.dirname(configs2[0].description)
    assert configs == configs2

# Generated at 2022-06-13 20:54:07.241415
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import pathlib
    main_dir = pathlib.Path('.')
    exts_dir = pathlib.Path('flutils/exts/setup_commands')
    if exts_dir.exists():
        main_dir = pathlib.Path('.').absolute().parent
        exts_dir = exts_dir.absolute()
    else:
        exts_dir = main_dir / exts_dir

    path = pathlib.Path(main_dir)

    setup_dir = None
    for p in path.parents:
        if p.name == 'source':
            setup_dir = p
            break
    if setup_dir is None:
        for p in path.parents:
            if p.name == 'dist':
                setup_dir = p / 'source'
                break

    assert each_sub_command

# Generated at 2022-06-13 20:54:21.470500
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # Note: self.assertEqual is a unittest.TestCase assert method
    # Note: self.assertRaisesRegex is a unittest.TestCase assert method
    import unittest
    from unittest.mock import patch

    class TestEachSubCommandConfig(unittest.TestCase):

        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_call(self):
            with patch('os.path.dirname', return_value=str):
                with self.assertRaisesRegex(
                        FileNotFoundError,
                        '^Unable to find the directory that contains the '
                        "'setup.py' file.$"
                ):
                    each_sub_command_config()  # type: ignore


# Generated at 2022-06-13 20:54:32.644369
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import logging
    import pprint
    import sys
    log_filename = os.path.join('flutils', 'logs', 'tests', 'test.log')
    log_filename = os.path.join(os.path.expanduser('~'), log_filename)
    logging.basicConfig(
        format='%(levelname)s:%(asctime)s:%(name)s:%(message)s',
        level=logging.DEBUG,
        filename=log_filename
    )
    logger = logging.getLogger(__file__)
    logger.info('\n\n')
    logger.info('Started function test for function each_sub_command_config')


# Generated at 2022-06-13 20:54:40.618799
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys

    try:
        test_path = os.path.abspath(os.path.join(__file__, '..', '..'))
        sys.path.insert(0, test_path)
        import flutils_test  # noqa: F401

        for cmd in each_sub_command_config():
            print(cmd)
    finally:
        sys.path.remove(test_path)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:54:52.518347
# Unit test for function each_sub_command_config
def test_each_sub_command_config():

    setup_cfg = StringIO("""
[metadata]
name = test-project
[setup.command.test-command]
name = Test Command
description = Runs the Test Command
command = echo "Test Command"
""")
    setup_dir = tempfile.mkdtemp(prefix='test_')

    with open(os.path.join(setup_dir, 'setup.cfg'), 'w') as file:
        file.write(setup_cfg.getvalue())

    with open(os.path.join(setup_dir, 'setup.py'), 'w') as file:
        file.write('')


# Generated at 2022-06-13 20:55:05.104446
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    here = os.path.dirname(__file__)
    sdir = os.path.join(here, 'tests', 'test_data')
    results = list(each_sub_command_config(sdir))
    assert len(results) == 1
    result = results[0]
    assert result.name == 'cleandir'
    assert result.camel == 'CleanDir'
    assert result.description == 'Removes the "dist" directory.'
    assert result.commands == ('rm -rf dist',)


if __name__ == "__main__":
    test_each_sub_command_config()

# Generated at 2022-06-13 20:55:16.325896
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile

    def temp_config(name: str) -> str:
        with tempfile.NamedTemporaryFile(delete=False) as fp:
            text = f'''
[metadata]
name={name}

[setup.command.clean.py]
description=Cleanup {name}
command=
    python -m flutils.cleanup.remove_pyc
    python -m flutils.cleanup.remove_egg_info

[setup.command.clean.test]
description=Cleanup {name} Test Suite
command=
    python setup.py clean -a

[setup.command.build]
description=Build {name}
command=python setup.py build
'''
            fp.write(text.encode('utf-8'))
        return fp.name


# Generated at 2022-06-13 20:55:27.233356
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import json

    def assert_output(expected: str, lines: List[str]) -> None:
        lines = list(filter(len, map(lambda x: x.strip(), lines)))
        assert lines == expected.splitlines()

    here = os.path.dirname(__file__)
    here = os.path.realpath(here)
    results = []
    for config in each_sub_command_config(setup_dir=here):
        results.append(json.dumps(config._asdict()))

# Generated at 2022-06-13 20:55:32.876605
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for cfg in each_sub_command_config():
        assert isinstance(cfg.name, str), cfg.name
        assert isinstance(cfg.camel, str), cfg.camel
        assert isinstance(cfg.description, str), cfg.description
        assert isinstance(cfg.commands, tuple), cfg.commands
        assert tuple(map(str, cfg.commands)) == cfg.commands

# Generated at 2022-06-13 20:55:58.636261
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import dirname
    from flutils.strutils import to_str
    # root_dir = dirname(__file__, '..', '..', '..', '..', '..')  # flutils
    root_dir = dirname(__file__, '..', '..', '..', '..', '..', '..')  # flutils
    root_dir = dirname(root_dir, '..', '..', '..', '..')  # flutils-project
    # root_dir = dirname(__file__, '..', '..', '..', '..')  # flutils-dev
    setup_dir = os.path.join(root_dir, 'src', 'flutils')

# Generated at 2022-06-13 20:56:12.104459
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    if sys.version_info[:2] == (3, 6):
        print(
            "WARNING: Skipping unit test because Python version is 3.6."
        )
        return
    elif sys.version_info[:2] == (2, 7):
        print(
            "WARNING: Skipping unit test because Python version is 2.7."
        )
        return
    dirname = os.path.dirname
    parent = None
    for pname in ('flutils', 'setup_utils'):
        parent = os.path.join(dirname(dirname(__file__)), pname)
        if os.path.isfile(os.path.join(parent, 'setup.py')):
            break
    if parent is None:
        raise ValueError("Unable to find the setup.py file.")

# Generated at 2022-06-13 20:56:14.106011
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for sub_command_config in each_sub_command_config():
        print(sub_command_config)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:56:26.125540
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import time

    existing_path = os.path.join(os.path.dirname(__file__), '..', 'setup.py')
    if os.path.isfile(existing_path):
        print()
        print(
            "  To run the unit test for each_sub_command_config(), please "
            "move the file {!r} to another directory that does NOT contain "
            "a file named setup.py. Then re-run this file.".format(
                existing_path
            )
        )
        print()
        time.sleep(1)
        sys.exit()

# Generated at 2022-06-13 20:56:28.209937
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config():
        assert type(config) is SetupCfgCommandConfig



# Generated at 2022-06-13 20:56:34.438720
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)), '..', '..'
        )
    )
    for cmd in each_sub_command_config(setup_dir):
        print(cmd)
    assert True


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:56:48.895297
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import pytest
    from flutils.config import each_sub_command_config

    pytest.importorskip('pytest')
    try:
        import pytest_runner
    except ImportError:
        pass

    test_dir = os.path.dirname(__file__)
    path = os.path.join(test_dir, '../../setup.py')
    path = os.path.realpath(path)
    if os.path.isfile(path) is False:
        assert False

    test_configs = tuple(each_sub_command_config(test_dir))

    assert len(test_configs) == 4

    config = test_configs[0]
    assert config.name == 'coverage.run'
    assert config.camel == 'CoverageRun'

# Generated at 2022-06-13 20:56:51.502703
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    paths = each_sub_command_config()
    for path in paths:
        print(path)

# Generated at 2022-06-13 20:56:59.298675
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    itr = each_sub_command_config()
    assert itr
    for i in itr: pass
    with pytest.raises(FileNotFoundError):
        itr = each_sub_command_config('/tmp')  # noqa: F841
    with pytest.raises(LookupError):
        itr = each_sub_command_config('./')


# Generated at 2022-06-13 20:57:11.999270
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    out = list(each_sub_command_config(setup_dir='../..'))

# Generated at 2022-06-13 20:57:29.296012
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    test_commands = [
        SetupCfgCommandConfig(
            name='name',
            camel='Name',
            description='Description',
            commands=('echo "{setup_dir}"',)
        )
    ]
    with mock.patch.object(os.path, 'exists', return_value=True) as mock_obj:
        with mock.patch.object(os, 'path') as mock_meth:
            mock_meth.isdir.return_value = True
            mock_meth.basename.return_value = 'setup.py'
            results = [rc for rc in each_sub_command_config()]
        mock_obj.assert_called_once_with('setup.py')
    mock_meth.isdir.assert_called_once_with(
        'setup.py'
    )


# Generated at 2022-06-13 20:57:41.760662
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    import tempfile
    import unittest

    cwd = os.getcwd()
    setup_dir = tempfile.mkdtemp()
    setup_cfg_path = os.path.join(setup_dir, 'setup.cfg')

# Generated at 2022-06-13 20:57:52.404310
# Unit test for function each_sub_command_config

# Generated at 2022-06-13 20:58:04.540538
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    dirname = os.path.dirname(__file__)
    paths: List[str] = [
        os.path.join(dirname, '..', '..', '..', 'foo'),
        os.path.join(dirname, '..'),
        os.path.join(dirname, '..', '..'),
        os.path.join(dirname, 'setup'),
    ]
    for path in paths:
        configs = [c for c in each_sub_command_config(path)]
        assert configs[0].name == 'flsetup.project_commands.foo'
        assert configs[1].name == 'flsetup.project_commands.egg_info'
        assert configs[2].name == 'flsetup.project_commands.install'
        assert len(configs) == 3

# Generated at 2022-06-13 20:58:07.793909
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for cmd in each_sub_command_config('/home/mitch/.git_template'):
        print(cmd)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:58:17.570280
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # This will only work, if it is ran from the project's directory
    import itertools
    import sys
    from flutils.datautils import get_first_file_w_name
    from flutils.pathutils import get_top_path

    top_path = get_top_path()
    cfg_path = get_first_file_w_name(top_path, 'setup_commands.cfg')
    if not cfg_path:
        sys.exit(0)
    assert os.path.splitext(os.path.basename(cfg_path)) == ('setup_commands',
                                                            '.cfg')

    parser = ConfigParser()
    parser.read(cfg_path)


# Generated at 2022-06-13 20:58:20.752822
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for command in each_sub_command_config(__file__):
        print(command)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:58:32.485230
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from tempfile import TemporaryDirectory
    from textwrap import dedent

    with TemporaryDirectory(prefix='flutils') as setup_dir:
        setup_cfg_path = os.path.join(setup_dir, 'setup.cfg')

# Generated at 2022-06-13 20:58:45.042227
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from . import __path__
    from .setup import setup_dir as _setup_dir
    actual = list(each_sub_command_config())

# Generated at 2022-06-13 20:58:52.143191
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    path = os.path.dirname(__file__)
    path = os.path.join(path, '..')
    configs = list(each_sub_command_config(path))
    assert configs
    command_names = [config.name for config in configs]
    assert 'dev.build' in command_names
    assert 'dev.clean' in command_names
    assert 'dev.run' in command_names
    assert 'dev.lint' in command_names
    assert 'dev.tox' in command_names
    assert 'dev.test' in command_names
    for config in configs:
        for cmd in config.commands:
            assert type(cmd) is str
        assert type(config.name) is str
        assert type(config.camel) is str

# Generated at 2022-06-13 20:59:08.111359
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil

    with tempfile.TemporaryDirectory(dir='.') as tmpdir:
        tmpdir = os.path.realpath(tmpdir)
        setup_file = os.path.join(tmpdir, 'setup.py')
        with open(setup_file, 'w') as fh:
            fh.write('pass\n')

        setup_cfg_file = os.path.join(tmpdir, 'setup.cfg')
        with open(setup_cfg_file, 'w') as fh:
            fh.write(
                '[metadata]\n'
                'name = test_package\n'
            )

        extract_dir = os.path.join(tmpdir, 'extract_dir')
        os.mkdir(extract_dir)
        setup_commands_file

# Generated at 2022-06-13 20:59:16.858056
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.pathutils import is_file_writable as isf
    from flutils.testutils import (
        compare_sequences,
        compare_strings,
        filter_error_copy,
        filter_error_stack,
        filter_env_vars,
        get_test_data_path,
        is_test_data_file,
        load_test_data_file,
        replace_test_data,
    )

    setup_cfg = get_test_data_path('', 'setup.cfg')
    setup_dir = get_test_data_path('', 'setup_commands')
    test_data_file = get_test_data_path('setup_commands', 'test.data')

    def _this_func():
        return each_sub_command_config(setup_dir)

    path

# Generated at 2022-06-13 20:59:23.153491
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os.path as p
    import unittest

    class Test(unittest.TestCase):
        def test(self):
            out = list(each_sub_command_config())
            self.assertTrue(len(out) > 0)

    unittest.main()

# Generated at 2022-06-13 20:59:28.510163
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import flutils.setuputils

    configs = list(flutils.setuputils.each_sub_command_config())

    assert len(configs) == 1

    config = configs[0]

    assert config.commands == ('echo "Hello, world!"', )


if __name__ == '__main__':
    import sys
    sys.exit(test_each_sub_command_config())

# Generated at 2022-06-13 20:59:40.709429
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from shutil import rmtree
    from tempfile import mkdtemp
    from textwrap import dedent

    setup_py = dedent("""\
            from setuptools import setup

            setup(
                name='setup-command-test',
                version='1.0.0',
                description='Test for setup_command.each_sub_command_config',
                author='Wes Turner',
                author_email='wes@wrd.nu',
                packages=['setupcommandtest'],
                package_dir={'': 'src'},
            )
        """)


# Generated at 2022-06-13 20:59:50.329678
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for cmd in each_sub_command_config():
        assert cmd.name
        assert cmd.camel
        assert cmd.description
        assert len(cmd.commands) >= 1
        assert cmd.commands[-1]
        assert cmd.commands[-1].strip()[-1] != '\\'
    print('Function: each_sub_command_config()')
    print('UniTests: PASSED')


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:00:00.996858
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    from pprint import pprint
    from flutils.pathutils import each_dir


    def print_setup_dir(setup_dir):
        print('%r:' % setup_dir)
        for x in each_sub_command_config(setup_dir):
            pprint(x)
        print()


    def go():
        print_setup_dir(None)
        print_setup_dir('.')
        print_setup_dir(os.getcwd())
        print_setup_dir(os.path.dirname(__file__))
        for setup_dir in each_dir(os.path.dirname(__file__)):
            print_setup_dir(setup_dir)

    go()

# Generated at 2022-06-13 21:00:04.769163
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    pass


if __name__ == '__main__':
    from sys import exit
    exit(test_each_sub_command_config())

# Generated at 2022-06-13 21:00:10.753968
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from pprint import pprint
    # from flutils.scriptutils import each_sub_command_config
    for sub_command_config in each_sub_command_config():
        pprint(sub_command_config._asdict())


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:00:15.553031
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for sc in each_sub_command_config(sys.argv[1]):
        print(sc)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:00:34.754906
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    output = list(each_sub_command_config())
    assert output
    names = set()
    titles = set()
    for item in output:
        assert item.name
        assert isinstance(item.camel, str)
        assert item.description
        assert isinstance(item.commands, tuple)
        assert len(item.commands) > 0
        names.add(item.name)
        titles.add(item.camel)
    assert len(names) == len(titles)



# Generated at 2022-06-13 21:00:38.818107
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for scc in each_sub_command_config(__file__):
        print(scc)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:00:42.493428
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.config import each_sub_command_config

    for cmd in each_sub_command_config():
        print(cmd)

# Generated at 2022-06-13 21:00:51.154436
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    each_sub_command_config('/home/some/dev/python/flutils/tests/data/setup-test2')
    each_sub_command_config('/home/some/dev/python/flutils/tests/data/setup-test')
    each_sub_command_config('/home/some/dev/python/flutils/tests/data/setup-test3')
    each_sub_command_config('/home/some/dev/python/flutils/tests/data/flutils')
    each_sub_command_config('/home/some/dev/python/flutils/tests/data/setup-test4')

# Generated at 2022-06-13 21:01:03.099498
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """This is a unit test for the
    :func:`flutils.setuputils.each_sub_command_config` function.

    """
    from pathlib import Path
    from unittest import TestCase

    class ListSubCommandConfigTestCase(TestCase):
        """A unit test case for testing the
        :func:`flutils.setuputils.list_sub_commands` function.

        """

        def test_case_01(self):
            """The file, setup_commands.cfg, is in the same directory as
            setup.py.

            """
            setup_dir = Path(__file__).parent.parent.parent / 'test' / 'data'
            setup_cfg_filename = setup_dir / 'setup.cfg'
            setup_cfg_filename.exists()

# Generated at 2022-06-13 21:01:11.984641
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # Must be run from project root directory
    # For example, C:\Users\bob\Documents\GitHub\flutils
    project_root = os.path.dirname(os.path.dirname(__file__))
    setup_dir = os.path.join(project_root, 'tests', 'test_pypackage')
    for sub_cmd in each_sub_command_config(setup_dir):
        print(sub_cmd)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:01:16.171603
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    project_root = os.path.dirname(os.path.dirname(__file__))
    for cmd in each_sub_command_config(project_root):
        assert isinstance(cmd, SetupCfgCommandConfig)
        assert cmd.name
        assert cmd.camel
        assert cmd.description
        assert cmd.commands

# Generated at 2022-06-13 21:01:24.273171
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import pathlib
    import shutil

    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Create the project's setup.py file
    fpath = pathlib.Path(temp_dir) / 'setup.py'
    with fpath.open('w') as f:
        f.write('#')

    # Create the project's setup.cfg file
    fpath = pathlib.Path(temp_dir) / 'setup.cfg'
    with fpath.open('w') as f:
        f.write('[metadata]\nname = b\n')
        f.write('[setup.command.a]\ncommands = foo\n')
        f.write('[setup.command.b]\ncommands = bar\n')

    # Create the project's setup

# Generated at 2022-06-13 21:01:32.545213
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import inspect
    this_file = inspect.getfile(inspect.currentframe())
    this_dir = os.path.dirname(this_file)
    for cfg in each_sub_command_config(this_dir):
        assert isinstance(cfg, SetupCfgCommandConfig)
        assert isinstance(cfg.commands, tuple)


if __name__ == '__main__':
    import sys
    sys.exit(test_each_sub_command_config())

# Generated at 2022-06-13 21:01:35.912209
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    config = list(each_sub_command_config())
    assert len(config) >= 1
    assert config[0].name == 'flutils'

# Generated at 2022-06-13 21:02:09.692065
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # TODO: Move this to a file.
    import json
    import pprint
    import textwrap
    from tempfile import TemporaryDirectory

    from flutils.pathutils import clean_path

    from .testutils import (
        assert_each_sub_command_config,
        assert_not_each_sub_command_config,
    )

    with TemporaryDirectory() as td:
        # A 'setup.py' file is needed.
        path = os.path.join(td, 'setup.py')
        with open(path, 'w') as fh:
            fh.write(
                textwrap.dedent(
                    """\
                    from setuptools import setup

                    setup()
                    """
                )
            )
        # A 'setup_commands.cfg' file is needed.

# Generated at 2022-06-13 21:02:16.836077
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config(setup_dir='setup.py'):
        print(config.name)
        print(config.camel)
        print(config.description)
        print(config.commands)
        print()


if __name__ == "__main__":
    test_each_sub_command_config()

# Generated at 2022-06-13 21:02:27.037305
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # Arrange
    kwargs = {
        'setup_dir': '/Users/vitaly/projects/fl_project_deploy'
    }
    # Act
    gen = each_sub_command_config(**kwargs)
    # Assert
    first = next(gen)
    assert first.name == 'fl-project-deploy'
    assert first.camel == 'FlProjectDeploy'
    assert first.description == (
        'Deploy the %(name)s project'
        % kwargs
    )
    assert first.commands == (
        'pip uninstall %(name)s -y' % kwargs,
        'python setup.py sdist',
        'pip install %(name)s' % kwargs,
    )



# Generated at 2022-06-13 21:02:33.217276
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def _test_one(setup_dir: str) -> None:
        gen = each_sub_command_config(setup_dir)
        for i, cfg in enumerate(gen):
            print(i, cfg)

    _test_one(os.path.expanduser('~'))

# Generated at 2022-06-13 21:02:45.500522
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    project_root = os.path.realpath(
        os.path.join(os.path.dirname(__file__), '..', '..')
    )
    setup_cfg_path = os.path.join(project_root, 'setup.cfg')
    cfg_setup_commands_path = os.path.join(
        project_root, 'setup_commands.cfg'
    )
    calc_out = []
    for cmd in each_sub_command_config(project_root):
        calc_out.append(cmd)
    expect_out = []
    with open(cfg_setup_commands_path, encoding='utf8') as fo:
        for line in fo:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            expect_out

# Generated at 2022-06-13 21:02:49.343094
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    iter_obj = each_sub_command_config(
        os.path.dirname(os.path.dirname(__file__))
    )
    try:
        next(iter_obj)
    except StopIteration:
        assert False, "At least one sub command configuration expected."

# Generated at 2022-06-13 21:02:54.813332
# Unit test for function each_sub_command_config
def test_each_sub_command_config():  # noqa: D102, D103
    for config in each_sub_command_config():
        if config.name == 'dev_build':
            assert config.camel == 'DevBuild'
            assert config.description == 'Builds the project for development.'
            assert config.commands == (
                'py setup.py build',
            )
        elif config.name == 'dev_install':
            assert config.camel == 'DevInstall'
            assert config.description == (
                'Installs the project for development.'
            )
            assert config.commands == (
                'py setup.py install',
            )

# Generated at 2022-06-13 21:02:56.571407
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for _ in each_sub_command_config():
        break

# Generated at 2022-06-13 21:03:09.916186
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from tempfile import mkdtemp
    from flutils.commonutils import file_encoding_utils
    from flutils.pyutils import (
        copy_anything,
        create_dir,
    )

    print()

    # Test nested
    # TODO: Test nested virtual environment

    # Prepare
    tmp_dir = mkdtemp()
    res_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'res', 'setup_commands')
    )
    test_dir = os.path.join(tmp_dir, 'setup_commands')
    copy_anything(res_dir, test_dir)
    for sub_dir in ('b', 'd'):
        sub_dir = os.path.join(test_dir, sub_dir)
        create

# Generated at 2022-06-13 21:03:19.004348
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Validates that the generator function,
    :func:`each_sub_command_config`, works as expected.  This function
    implements a unit test as it validates that the function's
    ``setup.cfg`` config file works as expected.
    """
    setup_dir = os.path.dirname(__file__)
    setup_dir = os.path.join(setup_dir, '_test_setup')
    for setup_cfg in each_sub_command_config(setup_dir):
        assert setup_cfg.name == 'sub_command.subsub_command'
        assert setup_cfg.camel == 'SubSubCommand'
        assert setup_cfg.description == 'This is the setup_cfg test.'