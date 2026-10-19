

# Generated at 2022-06-13 20:54:02.354893
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config."""
    import sys
    import unittest.mock as mock
    path = os.path.dirname(__file__)
    path = os.path.join(path, 'fixtures', 'setup_cfg_sub_commands')
    path = os.path.realpath(path)
    with mock.patch.object(sys, 'argv', [__file__, 'develop']):
        with mock.patch.object(sys, 'path', [path]):
            setup_dir = os.path.dirname(__file__)
            setup_dir = os.path.join(setup_dir, 'fixtures')
            setup_dir = os.path.join(setup_dir, 'setup_cfg_sub_commands')

# Generated at 2022-06-13 20:54:16.903811
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import flutils.config.setup_cfg
    from flutils.strutils import fmt_cmd_line
    cb = flutils.config.setup_cfg.each_sub_command_config()
    for config in cb:
        if config.camel == 'Main':
            assert config.name == 'flutils.config'
            assert config.commands == (
                'python -m flutils.config setup',
                'pip install -e {setup_dir}'
            )
        else:
            assert config.camel == 'Lint'
            assert config.name == 'flutils.config.lint'

# Generated at 2022-06-13 20:54:30.701461
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from tempfile import TemporaryDirectory
    from pkg_resources import resource_string
    from io import BytesIO

    with TemporaryDirectory(prefix='setup_') as tmpdirname:
        tmpdirname = os.path.realpath(tmpdirname)

        with open(os.path.join(tmpdirname, 'setup.py'), 'wb') as ofile:
            ofile.write(b'setup()')

        with open(os.path.join(tmpdirname, 'setup.cfg'), 'wb') as ofile:
            ofile.write(resource_string(__name__, 'setup.cfg'))


# Generated at 2022-06-13 20:54:36.107578
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir)
    )
    out = list(each_sub_command_config(setup_dir))
    assert len(out) >= 50


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:54:44.604348
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import unittest
    from unittest.mock import patch

    class TestSetupCfgCommands(unittest.TestCase):
        def test_setup_cfg_commands(self):
            from flutils.testutils import temp_change_dir
            from flutils.setuputils import writable_setup_cfg_file

            with temp_change_dir() as tmp:
                setup_cfg_path = writable_setup_cfg_file()
                parser = ConfigParser()
                parser.read(setup_cfg_path)
                parser.add_section('metadata')
                parser.set('metadata', 'name', 'flutils')
                with open(setup_cfg_path, 'w') as fp:
                    parser.write(fp)

# Generated at 2022-06-13 20:54:55.406937
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    ######################################################################
    # Test exception when the setup directory is not given
    try:
        list(each_sub_command_config())
    except FileNotFoundError as err:
        assert str(err).endswith(
            "Unable to find the directory that contains the 'setup.py' file."
        )
    else:
        raise Exception('Expected an exception.')

    ######################################################################
    # Test exception when the setup directory does not exist
    try:
        list(each_sub_command_config(__file__))
    except FileNotFoundError as err:
        assert str(err).endswith(
            "The given 'setup_dir' of %r does NOT exist." % __file__
        )
    else:
        raise Exception('Expected an exception.')

    ######################################################################


# Generated at 2022-06-13 20:55:04.298670
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import io
    import sys

    current_dir = os.path.realpath(
        os.path.dirname(os.path.abspath(__file__))
    )
    test_dir = os.path.join(current_dir, 'data', 'test_package')


# Generated at 2022-06-13 20:55:15.397350
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import pytest
    cwd = os.getcwd()

# Generated at 2022-06-13 20:55:26.475056
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = '/home/wheeler/Projects/flutils'
    setup_dir = os.path.realpath(setup_dir)

    paths = (
        '/home/wheeler/Projects/flutils/setup.py',
        '/home/wheeler/Projects/flutils/setup.cfg',
        '/home/wheeler/Projects/flutils/setup_commands.cfg'
    )
    for path in paths:
        assert os.path.isfile(path), '%r does not exist.' % path

    for conf in each_sub_command_config(setup_dir=setup_dir):
        assert (isinstance(conf, SetupCfgCommandConfig) is True)
        assert (isinstance(conf.name, str) is True)
        assert (isinstance(conf.camel, str) is True)

# Generated at 2022-06-13 20:55:35.355866
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from pprint import pprint
    from flutils.config import ConfigSection

    def process(command_config: SetupCfgCommandConfig) -> ConfigSection:
        section = ConfigSection(command_config.name)
        section.description = command_config.description
        cmd = ConfigSection('command')
        cmd.configure_args = [
            '--%s' % command_config.camel,
            '--%s-desc' % command_config.camel,
        ]
        cmd.command = [
            'python',
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                'scripts',
                '%s.py' % command_config.camel.lower()
            ),
        ]

# Generated at 2022-06-13 20:55:57.702425
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    script_dir = os.path.dirname(__file__)
    script_dir = os.path.abspath(script_dir)
    project_dir = os.path.normpath(
        os.path.join(script_dir, '..', '..', '..', '..')
    )

# Generated at 2022-06-13 20:56:03.942180
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for config in each_sub_command_config(
            os.path.dirname(os.path.abspath(__file__))
    ):
        print(config)

if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:56:16.933902
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    configs = list(each_sub_command_config(os.path.join(os.path.dirname(__file__), 'test_package')))
    assert len(configs) == 2
    assert configs[0].name == 'test_package.test_command1'
    assert configs[0].camel == 'TestPackageTestCommand1'
    assert configs[0].description == 'A test sub-command that has a short desription.'
    assert configs[1].name == 'test_package.test.command2'
    assert configs[1].camel == 'TestPackageTestCommand2'
    assert configs[1].description == 'A test sub-command that has a long description.\nThis one.'



# Generated at 2022-06-13 20:56:23.925419
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def iter_(setup_dir: Optional[str] = None
              ) -> Generator[SetupCfgCommandConfig, None, None]:
        for item in each_sub_command_config(setup_dir):
            yield item

    # TODO: Add a unit test for this function
    setup_dir = _prep_setup_dir()
    for item in iter_(setup_dir):
        print('item:', item)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:56:35.236385
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    os.system('rm -rf /tmp/test_each_sub_command_config')
    setup_dir = '/tmp/test_each_sub_command_config'
    os.makedirs(setup_dir)
    os.makedirs(os.path.join(setup_dir, 'subpackage'))
    with open(os.path.join(setup_dir, 'setup.py'), 'w') as f:
        f.write('#!/usr/bin/python\n')
    with open(os.path.join(setup_dir, 'setup.cfg'), 'w') as f:
        f.write('[metadata]\n')
        f.write('name=test_each_sub_command_config\n')

# Generated at 2022-06-13 20:56:46.411723
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_cfg_path = os.path.join(os.path.dirname(__file__), 'setup.cfg')
    parser = ConfigParser()
    parser.read(setup_cfg_path)
    name = _get_name(parser, setup_cfg_path)
    setup_dir = os.path.dirname(setup_cfg_path)
    format_kwargs = {
        'name': name,
        'setup_dir': setup_dir,
        'home': os.path.expanduser('~')
    }
    path = os.path.join(setup_dir, 'setup_commands.cfg')
    if os.path.isfile(path):
        parser = ConfigParser()
        parser.read(path)


# Generated at 2022-06-13 20:56:48.934108
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for _ in each_sub_command_config(os.path.dirname(__file__)):
        break


# Generated at 2022-06-13 20:57:03.763759
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from textwrap import dedent
    from flutils.fileutils import create_temp_file

    with create_temp_file(prefix='setup_cfg_') as fd:
        fd.write(dedent('''\
            [metadata]
            name = test
            [setup.command.a]
            name = Test A
            description = Test description A
            command = echo "TEST A"
            [setup.command.b]
            name = Test B
            description = Test description B
            commands = echo "TEST B"
            echo "TEST B"
        ''').encode())
        fd.seek(0)

        config: List[SetupCfgCommandConfig] = list(each_sub_command_config(
            fd.name
        ))
        assert len(config) == 2

# Generated at 2022-06-13 20:57:11.487261
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    import unittest

    def _check_commands(name, desc, *commands) -> SetupCfgCommandConfig:
        return SetupCfgCommandConfig(
            name, name.replace(' ', '_').replace('-', '_'), desc, commands
        )

    class EachSubCommandConfigTestCase(unittest.TestCase):
        root_path = os.path.realpath(
            os.path.join(os.path.dirname(__file__), '..')
        )
        setup_path = os.path.join(root_path, 'setup.py')


# Generated at 2022-06-13 20:57:24.397271
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = '/home/matt/Projects/flutils'
    configs = list(each_sub_command_config(setup_dir))
    assert len(configs) > 0
    for config in configs:
        assert config.name
        assert config.camel
        assert config.description
        assert len(config.commands) > 0
        # print('name:', config.name)
        # print('camel:', config.camel)
        # print('description:', config.description)
        # print('commands:', config.commands)
        # print('')


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 20:57:42.798522
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    import sys
    import pytest
    root_dir = os.path.realpath(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
    )
    sys.path.insert(0, root_dir)
    try:
        from flutils.inspectutils import (
            get_func_defaults,
            get_func_params,
        )
    finally:
        del sys.path[0]
    from flutils.formatutils import (
        format_doc_string,
        format_title,
    )
    from flutils.setuputils import (
        each_sub_command_config,
        _get_name,
        _validate_setup_dir,
        _prep_setup_dir,
    )

    func_

# Generated at 2022-06-13 20:57:47.468019
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    out = list(each_sub_command_config(
        setup_dir=os.path.dirname(os.path.dirname(__file__))
    ))
    assert len(out) == 2

# Generated at 2022-06-13 20:57:55.861599
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    path = os.path.join(
        os.path.dirname(__file__), '..', '..', 'flutils', 'tests'
    )
    actual = list(each_sub_command_config(path))
    actual = tuple(sorted(actual, key=lambda x: str(x)))

# Generated at 2022-06-13 20:58:00.606630
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    from .templates import (
        setup_cfg_content,
        setup_command_cfg_content,
        setup_py_content
    )

    name = 'mypkg'
    with tempfile.TemporaryDirectory() as temp_dir:
        path = os.path.join(temp_dir, 'setup.py')
        with open(path, 'wt') as fp:
            fp.write(setup_py_content)

        path = os.path.join(temp_dir, 'setup.cfg')
        with open(path, 'wt') as fp:
            fp.write(setup_cfg_content)

        path = os.path.join(temp_dir, 'setup_commands.cfg')

# Generated at 2022-06-13 20:58:09.024469
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    file_path = os.path.join(os.path.dirname(__file__), 'setup.cfg')
    parser = ConfigParser()
    parser.read(file_path)
    configs = set(each_sub_command_config('./'))
    expected_configs = set(_each_setup_cfg_command(parser, {
        'setup_dir': os.path.realpath('./'),
        'home': os.path.expanduser('~'),
        'name': 'pysetupcfg'
    }))
    assert configs == expected_configs

# Generated at 2022-06-13 20:58:18.166889
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from pytest import main
    from flutils.setuputils import each_sub_command_config
    from flutils.files import each_dir_files

    setup_dir = os.path.dirname(__file__)
    for cmd in each_sub_command_config(setup_dir):
        for cmd_arg in cmd.commands:
            assert isinstance(cmd_arg, str)
            assert len(cmd_arg) > 0

    setup_dir = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        'setup_commands_parent'
    ))
    for cmd in each_sub_command_config(setup_dir):
        for cmd_arg in cmd.commands:
            assert isinstance(cmd_arg, str)

# Generated at 2022-06-13 20:58:29.005314
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    output = []

    # pylint: disable=invalid-name
    # noinspection PyShadowingNames
    def _setup_dir(path):
        # type: (str) -> None
        output.append(each_sub_command_config(path))

    with pytest.raises(FileNotFoundError):
        _setup_dir('/this/path/does/NOT/exist')
    assert len(output) == 0

    with pytest.raises(NotADirectoryError):
        _setup_dir(__file__)
    assert len(output) == 0

    with pytest.raises(FileNotFoundError):
        _setup_dir(os.path.dirname(__file__))
    assert len(output) == 0

    with pytest.raises(FileNotFoundError):
        _setup_

# Generated at 2022-06-13 20:58:40.630403
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def _get_commands(setup_dir: Optional[str] = None) -> List[str]:
        return list(
            map(
                lambda x: x.name,
                each_sub_command_config(setup_dir)
            )
        )

    setup_dir = os.path.join(os.getcwd(), 'flutils', 'tests', 'setup_cfg')
    out = _get_commands()
    exp = ['compile-the-messages', 'sdist', 'test']
    assert out == exp

    out = _get_commands(setup_dir)
    exp = [
        'compile-the-messages', 'coverage-html', 'coverage-report',
        'custom-command', 'sdist', 'test-coverage', 'test-with-test-command',
    ]

# Generated at 2022-06-13 20:58:46.816972
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.strings import normalize_path, regex_path_replace
    import re
    path = normalize_path(__file__)
    path, _ = regex_path_replace(path, re.compile(r'\.py$'), '/')
    path += '../../../../..'
    for config in each_sub_command_config(path):
        print(config)



# Generated at 2022-06-13 20:59:00.346193
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import os
    import tempfile
    import unittest

    from flutils.objutils import get_caller_class_name

    class TestEachSubCommandConfig(unittest.TestCase):

        def test_1(self):
            with tempfile.TemporaryDirectory() as base:
                setup_dir = os.path.join(base, 'setup_dir')
                os.mkdir(setup_dir)
                path = os.path.join(setup_dir, 'setup_commands.cfg')

# Generated at 2022-06-13 20:59:16.352991
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Docstring"""
    res = []
    for x in each_sub_command_config():
        res.append(x)
    if len(res) != 1:
        raise ValueError(
            "Expected a single result; %r" % res
        )
    res = res[0]
    expected = SetupCfgCommandConfig(
        'test.test_fl', 'TestTestFl', '',
        ('echo 1', 'echo 2', 'echo 3')
    )
    if res != expected:
        raise ValueError(
            "Expected: %r; got: %r" % (expected, res)
        )

# Generated at 2022-06-13 20:59:27.585821
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from . import __file__ as test_mod_file_path
    from flutils.pathutils import (
        absolute_path,
        get_parent_dir,
    )
    from flutils.strutils import (
        endswith,
        startswith,
    )

    test_mod_dir = os.path.dirname(test_mod_file_path)
    assert endswith(test_mod_dir, 'test_config')
    root_dir = get_parent_dir(test_mod_dir)
    assert endswith(root_dir, 'flutils')
    setup_dir = get_parent_dir(root_dir)
    assert endswith(setup_dir, '')
    assert startswith(setup_dir, 'flutils-')
    os.chdir(test_mod_dir)

# Generated at 2022-06-13 20:59:40.094346
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import pathlib
    import pytest

    import flutils.setuputils

    testpath = pathlib.Path(
        __file__
    ).parent.parent.joinpath(
        'testdata',
        'setuputils',
        'setup.cfg'
    )

    name = flutils.setuputils.get_project_name(str(testpath))

    subcmds = list(
        flutils.setuputils.each_sub_command_config(
            str(testpath)
        )
    )

    assert len(subcmds) == 3

    assert subcmds[0].name == 'test_1'
    test_1_commands = subcmds[0].commands
    assert len(test_1_commands) == 2

# Generated at 2022-06-13 20:59:50.605759
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.fileutils import (
        generate_unique_name,
        touch
    )
    from flutils.processutils import run_cmd
    from shutil import rmtree

    def _test(commands: List[str]) -> None:
        cmds = list(each_sub_command_config())
        assert len(cmds) == len(commands)
        for cmd, expected in zip(cmds, commands):
            assert cmd.name == expected[0]
            assert cmd.camel == expected[1]
            assert cmd.description == expected[2]
            assert len(cmd.commands) == len(expected[3])
            for cmd_, expected_ in zip(cmd.commands, expected[3]):
                assert cmd_ == expected_

    tmp = generate_unique_name(os.getcwd())

# Generated at 2022-06-13 21:00:01.998867
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    import json
    import collections
    import io
    from io import StringIO
    from flutils.pathutils import splitext
    from flutils.testutils import (
        TestBase,
        test_method
    )

    class TestEachSubCommandConfig(TestBase):

        @test_method
        def test_invalid_setup_dir(self):
            """Test to ensure it correctly handles the given setup_dir not
            existing.
            """
            setup_dir = self.rand_str
            with self.assertRaises(FileNotFoundError):
                each_sub_command_config(setup_dir)

        @test_method
        def test_invalid_setup_dir_2(self):
            """Test to ensure it correctly handles the given setup_dir not
            existing.
            """
            setup_dir

# Generated at 2022-06-13 21:00:12.172777
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    for i, config in enumerate(
            each_sub_command_config(setup_dir='{}/setup/setup.py'.format(
                os.path.dirname(__file__)))):
        assert config.camel == 'AddHashbang'
        assert config.name == 'add-hashbang'
        assert config.description == 'Adds an executable hashbang to '
        assert config.commands == ('{sudo} true',)
        break
    assert i == 0
    print('TEST: test_each_sub_command_config - Success')



# Generated at 2022-06-13 21:00:16.608976
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    dir_path = os.path.dirname(__file__)
    for config in each_sub_command_config(os.path.join(dir_path, 'mock')):
        print(config)


if __name__ == '__main__':
    exit(test_each_sub_command_config())

# Generated at 2022-06-13 21:00:19.471775
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import pathlib
    curr_dir = pathlib.Path(__file__).parent
    each_sub_command_config(curr_dir)
    each_sub_command_config(curr_dir.parent)

# Generated at 2022-06-13 21:00:28.943670
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import doctest
    from .testutils import relative_to_function_path

    dir_path = relative_to_function_path(__file__, '../..')
    exprs = [
        'each_sub_command_config()',
        'each_sub_command_config("%s")' % dir_path,
        'each_sub_command_config("%s/../..")' % dir_path
    ]
    for expr in exprs:
        doctest.run_docstring_examples(
            locals()['each_sub_command_config'],
            globals(),
            expr
        )



# Generated at 2022-06-13 21:00:40.913186
# Unit test for function each_sub_command_config
def test_each_sub_command_config():

    def _test_sub_command_config(
            setup_cfg_dir: str,
            expected_values: Dict[str, str]
    ) -> None:
        for config in each_sub_command_config(setup_cfg_dir):
            if config.name not in expected_values:
                continue
            values = expected_values[config.name]
            object_values = (config.camel, config.description)
            if values == object_values:
                continue
            raise AssertionError(
                "The given 'setup_cfg_dir' of %r has an incorrect "
                "value of %r for its config of %r."
                % (setup_cfg_dir, object_values, config.name)
            )

# Generated at 2022-06-13 21:01:07.038542
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = os.path.realpath(
        os.path.join(os.path.dirname(__file__), '..', '..', '..')
    )
    for scc in each_sub_command_config(setup_dir):
        assert isinstance(scc, SetupCfgCommandConfig)
    for scc in each_sub_command_config():
        assert isinstance(scc, SetupCfgCommandConfig)

# Generated at 2022-06-13 21:01:14.957206
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    def my_test_func() -> None:
        for conf in each_sub_command_config():
            assert isinstance(conf.name, str)
            assert isinstance(conf.camel, str)
            assert isinstance(conf.description, str)
            assert isinstance(conf.commands, tuple)
            for cmd in conf.commands:
                assert cmd is not None
                assert isinstance(cmd, str)
    my_test_func()



# Generated at 2022-06-13 21:01:19.822507
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Check to see if each_sub_command_config returns something."""
    res = list(each_sub_command_config())
    assert res[0].description != ''
    assert res[0].name != ''
    assert res[0].commands != ()

# Generated at 2022-06-13 21:01:32.449757
# Unit test for function each_sub_command_config

# Generated at 2022-06-13 21:01:36.901012
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.configutils import each_sub_command_config
    for config in each_sub_command_config():
        print(f'{config.camel} - {config.name}')

# Generated at 2022-06-13 21:01:50.276380
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config"""
    import sys
    import unittest
    import warnings
    from flutils.sysutils import (
        chdir,
        get_project_root_dir,
    )

    from .setup_commands_test_generate_cmds import get_setup_cfg

    class SetupCfgCommandsTestCase(unittest.TestCase):
        """Test case for function each_sub_command_config"""

        def setUp(self):
            self._orig_wd = os.getcwd()
            self._test_dir = os.path.join(
                get_project_root_dir('tests', 'test_data'),
                'test_setup_commands'
            )
            os.makedirs(self._test_dir, exist_ok=True)
           

# Generated at 2022-06-13 21:01:58.982330
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    os.chdir(os.path.join('tests', 'setup_cfg_command_config'))

# Generated at 2022-06-13 21:02:03.349362
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    print()
    for config in each_sub_command_config():
        print(config)
    print()


if __name__ == '__main__':
    test_each_sub_command_config()
    print()

# Generated at 2022-06-13 21:02:14.005050
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    """Unit test for function each_sub_command_config."""
    from flutils.configutils import ConfigFile

    config = ConfigFile()
    config.section = 'metadata'
    config.name = 'test'
    config.description = 'Test package'

    config.section = 'setup.command.bdist_egg'
    config.name = 'bdist_egg'
    config.commands = """
        python setup.py -q bdist_egg
    """

    config.section = 'setup.command.bdist_wheel'
    config.name = 'bdist_wheel'
    config.commands = """
        python setup.py -q bdist_wheel
    """

    config.section = 'setup.command.sdist'
    config.name = 'sdist'

# Generated at 2022-06-13 21:02:22.498406
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import sys
    sys.path.insert(0, os.path.dirname(__file__))
    import setup as setup_module
    setup_dir = os.path.dirname(setup_module.__file__)
    setup_dir = os.path.dirname(setup_dir)
    del sys.path[0]
    print(list(each_sub_command_config(setup_dir)))


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 21:02:44.303715
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    dir_path = os.path.realpath(
        os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')
    )
    return tuple(each_sub_command_config(setup_dir=dir_path))

# Generated at 2022-06-13 21:02:47.614876
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    path = os.path.dirname(__file__)
    path = os.path.join(path, 'data', 'setup_commands')
    for sc in each_sub_command_config(path):
        print(sc)

# Generated at 2022-06-13 21:02:52.160835
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    # noinspection PyUnresolvedReferences
    from flutils.testing import each_setup_cfg_command_config

    for config in each_setup_cfg_command_config():
        print(config)


if __name__ == '__main__':
    import sys
    sys.exit(test_each_sub_command_config())

# Generated at 2022-06-13 21:02:58.338716
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import pprint

    for config in each_sub_command_config(
            os.path.join(os.path.dirname(__file__), '..')
    ):
        pprint.pprint(config)


if __name__ == '__main__':
    test_each_sub_command_config()

# Generated at 2022-06-13 21:03:11.232635
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from flutils.gendocs import setup_command_config
    from flutils.gendocs.gen import (
        CommandConfig,
        each_command_config,
    )
    from pprint import pprint
    from tempfile import mkdtemp
    import shutil

    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

    def _create_setup_cfg(tmp_dir: str) -> str:

        setup_cfg = os.path.join(tmp_dir, 'setup.cfg')
        setup_cmds_cfg = os.path.join(tmp_dir, 'setup_commands.cfg')

        parser = ConfigParser()
        parser.add_section('metadata')
        parser.set('metadata', 'name', 'test_app')


# Generated at 2022-06-13 21:03:15.691661
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from .commands import setup_commands

    for setup_cfg_command_config in each_sub_command_config():
        assert setup_cfg_command_config.name in setup_commands


# Generated at 2022-06-13 21:03:23.721668
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    actual = list(each_sub_command_config('../../'))
    assert len(actual) == 2
    assert actual[0].name == 'travis.yml'
    assert actual[0].camel == 'TravisYml'
    assert actual[0].description == (
        'Generate the `.travis.yml` file to be used with Travis CI.'
    )
    assert actual[0].commands == (
        'rm -rf .travis.yml',
        'make_travis_yml.py > .travis.yml',
        'cat .travis.yml'
    )

    assert actual[1].name == 'docs.pdf'
    assert actual[1].camel == 'DocsPdf'

# Generated at 2022-06-13 21:03:34.730144
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    cwd = os.getcwd()