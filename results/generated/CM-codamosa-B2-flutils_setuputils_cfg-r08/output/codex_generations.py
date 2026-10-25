

# Generated at 2026-10-24 23:33:16.005481
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:33:24.745583
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:33:26.107171
# Unit test for constructor of class SetupCfgCommandConfig
def test_SetupCfgCommandConfig():
    name = 'my.command'
    camel = 'MyCommand'
    description = 'Does a thing.'
    commands = ('echo hello', 'echo world')

    config = SetupCfgCommandConfig(name, camel, description, commands)

    # field values
    assert config.name == name
    assert config.camel == camel
    assert config.description == description
    assert config.commands == commands

    # tuple semantics
    assert isinstance(config, tuple)
    assert config == (name, camel, description, commands)
    assert config._fields == ('name', 'camel', 'description', 'commands')
    assert len(config) == 4

    # keyword construction produces the same value
    assert SetupCfgCommandConfig(
        name=name,
        camel=camel,
        description=description,
        commands=commands,
    ) == config

    # empty commands is allowed
    empty = SetupCfgCommandConfig('n', 'N', '', ())
    assert empty.commands == ()

    # commands must be a tuple, not a list, to compare equal
    assert config.commands != ['echo hello', 'echo world']

    # immutable
    with pytest.raises(AttributeError):
        config.name = 'other'

# Generated at 2026-10-24 23:33:27.463905
# Unit test for constructor of class SetupCfgCommandConfig
def test_SetupCfgCommandConfig():
    name = 'my.command'
    camel = 'MyCommand'
    description = 'Does a thing.'
    commands = ('echo hello', 'echo world')

    config = SetupCfgCommandConfig(name, camel, description, commands)

    # field values
    assert config.name == name
    assert config.camel == camel
    assert config.description == description
    assert config.commands == commands

    # tuple semantics
    assert isinstance(config, tuple)
    assert config == (name, camel, description, commands)
    assert config._fields == ('name', 'camel', 'description', 'commands')
    assert len(config) == 4

    # keyword construction produces the same value
    assert SetupCfgCommandConfig(
        name=name,
        camel=camel,
        description=description,
        commands=commands,
    ) == config

    # empty commands is allowed
    empty = SetupCfgCommandConfig('n', 'N', '', ())
    assert empty.commands == ()

    # commands must be a tuple, not a list, to compare equal
    assert config.commands != ['echo hello', 'echo world']

    # immutable
    with pytest.raises(AttributeError):
        config.name = 'other'

# Generated at 2026-10-24 23:33:28.797013
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 2

    assert configs[0].name == 'test'
    assert configs[0].camel == 'test'
    assert configs[0].description == ''
    assert configs[0].commands == ('python -m pytest', 'python -m flake8')

    assert configs[1].name == 'docs.my_pkg'
    assert configs[1].camel == 'docsMyPkg'
    assert configs[1].description == 'Build the docs for my_pkg'
    assert configs[1].commands == ('sphinx-build -b html docs docs/_build/html',)


def test_each_sub_command_config_setup_commands_cfg():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        # setup_commands.cfg, when present, replaces setup.cfg entirely
        # for command sections (but 'name' still comes from setup.cfg).
        _write(os.path.join(tmp, 'setup_commands.cfg'), (
            '[setup.command.lint]\n'
            'commands =\n'
            '    python -m my_pkg_lint\n'
        ))
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 1
    assert configs[0].name == 'lint'
    assert configs[0].commands == ('python -m my_pkg_lint',)


def test_each_sub_command_config_missing_name():
    import pytest
    from configparser import DuplicateError  # noqa: F401  (unused; see note)

    with TemporaryDirectory() as tmp:
        _write(os.path.join(tmp, 'setup.py'), '')
        _write(os.path.join(tmp, 'setup.cfg'), '[setup.command.test]\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(tmp))

# Generated at 2026-10-24 23:33:40.292647
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 23:33:41.624022
# Unit test for constructor of class SetupCfgCommandConfig
def test_SetupCfgCommandConfig():
    name = 'my.command'
    camel = 'MyCommand'
    description = 'Does a thing.'
    commands = ('echo hello', 'echo world')

    config = SetupCfgCommandConfig(name, camel, description, commands)

    # field values
    assert config.name == name
    assert config.camel == camel
    assert config.description == description
    assert config.commands == commands

    # tuple semantics
    assert isinstance(config, tuple)
    assert config == (name, camel, description, commands)
    assert config._fields == ('name', 'camel', 'description', 'commands')
    assert len(config) == 4

    # keyword construction produces the same value
    assert SetupCfgCommandConfig(
        name=name,
        camel=camel,
        description=description,
        commands=commands,
    ) == config

    # empty commands is allowed
    empty = SetupCfgCommandConfig('n', 'N', '', ())
    assert empty.commands == ()

    # commands must be a tuple, not a list, to compare equal
    assert config.commands != ['echo hello', 'echo world']

    # immutable
    with pytest.raises(AttributeError):
        config.name = 'other'

# Generated at 2026-10-24 23:33:42.957187
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 2

    assert configs[0].name == 'test'
    assert configs[0].camel == 'test'
    assert configs[0].description == ''
    assert configs[0].commands == ('python -m pytest', 'python -m flake8')

    assert configs[1].name == 'docs.my_pkg'
    assert configs[1].camel == 'docsMyPkg'
    assert configs[1].description == 'Build the docs for my_pkg'
    assert configs[1].commands == ('sphinx-build -b html docs docs/_build/html',)


def test_each_sub_command_config_setup_commands_cfg():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        # setup_commands.cfg, when present, replaces setup.cfg entirely
        # for command sections (but 'name' still comes from setup.cfg).
        _write(os.path.join(tmp, 'setup_commands.cfg'), (
            '[setup.command.lint]\n'
            'commands =\n'
            '    python -m my_pkg_lint\n'
        ))
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 1
    assert configs[0].name == 'lint'
    assert configs[0].commands == ('python -m my_pkg_lint',)


def test_each_sub_command_config_missing_name():
    import pytest
    from configparser import DuplicateError  # noqa: F401  (unused; see note)

    with TemporaryDirectory() as tmp:
        _write(os.path.join(tmp, 'setup.py'), '')
        _write(os.path.join(tmp, 'setup.cfg'), '[setup.command.test]\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(tmp))

# Generated at 2026-10-24 23:33:55.541657
# Unit test for function each_sub_command_config
def test_each_sub_command_config():from pathlib import Path

# Generated at 2026-10-24 23:33:56.874884
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 2

    assert configs[0].name == 'test'
    assert configs[0].camel == 'test'
    assert configs[0].description == ''
    assert configs[0].commands == ('python -m pytest', 'python -m flake8')

    assert configs[1].name == 'docs.my_pkg'
    assert configs[1].camel == 'docsMyPkg'
    assert configs[1].description == 'Build the docs for my_pkg'
    assert configs[1].commands == ('sphinx-build -b html docs docs/_build/html',)


def test_each_sub_command_config_setup_commands_cfg():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        # setup_commands.cfg, when present, replaces setup.cfg entirely
        # for command sections (but 'name' still comes from setup.cfg).
        _write(os.path.join(tmp, 'setup_commands.cfg'), (
            '[setup.command.lint]\n'
            'commands =\n'
            '    python -m my_pkg_lint\n'
        ))
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 1
    assert configs[0].name == 'lint'
    assert configs[0].commands == ('python -m my_pkg_lint',)


def test_each_sub_command_config_missing_name():
    import pytest
    from configparser import DuplicateError  # noqa: F401  (unused; see note)

    with TemporaryDirectory() as tmp:
        _write(os.path.join(tmp, 'setup.py'), '')
        _write(os.path.join(tmp, 'setup.cfg'), '[setup.command.test]\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(tmp))

# Generated at 2026-10-24 23:33:59.515507
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:34:02.057042
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:34:04.477304
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:34:07.002586
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:34:09.419520
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:34:11.837382
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:34:14.254046
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:34:16.669438
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:34:19.087361
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:34:21.504980
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:34:34.249460
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 23:34:35.578500
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 2

    assert configs[0].name == 'test'
    assert configs[0].camel == 'test'
    assert configs[0].description == ''
    assert configs[0].commands == ('python -m pytest', 'python -m flake8')

    assert configs[1].name == 'docs.my_pkg'
    assert configs[1].camel == 'docsMyPkg'
    assert configs[1].description == 'Build the docs for my_pkg'
    assert configs[1].commands == ('sphinx-build -b html docs docs/_build/html',)


def test_each_sub_command_config_setup_commands_cfg():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        # setup_commands.cfg, when present, replaces setup.cfg entirely
        # for command sections (but 'name' still comes from setup.cfg).
        _write(os.path.join(tmp, 'setup_commands.cfg'), (
            '[setup.command.lint]\n'
            'commands =\n'
            '    python -m my_pkg_lint\n'
        ))
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 1
    assert configs[0].name == 'lint'
    assert configs[0].commands == ('python -m my_pkg_lint',)


def test_each_sub_command_config_missing_name():
    import pytest
    from configparser import DuplicateError  # noqa: F401  (unused; see note)

    with TemporaryDirectory() as tmp:
        _write(os.path.join(tmp, 'setup.py'), '')
        _write(os.path.join(tmp, 'setup.cfg'), '[setup.command.test]\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(tmp))

# Generated at 2026-10-24 23:34:44.589707
# Unit test for function each_sub_command_config
def test_each_sub_command_config():from pathlib import Path

# Generated at 2026-10-24 23:34:45.919941
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 2

    assert configs[0].name == 'test'
    assert configs[0].camel == 'test'
    assert configs[0].description == ''
    assert configs[0].commands == ('python -m pytest', 'python -m flake8')

    assert configs[1].name == 'docs.my_pkg'
    assert configs[1].camel == 'docsMyPkg'
    assert configs[1].description == 'Build the docs for my_pkg'
    assert configs[1].commands == ('sphinx-build -b html docs docs/_build/html',)


def test_each_sub_command_config_setup_commands_cfg():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        # setup_commands.cfg, when present, replaces setup.cfg entirely
        # for command sections (but 'name' still comes from setup.cfg).
        _write(os.path.join(tmp, 'setup_commands.cfg'), (
            '[setup.command.lint]\n'
            'commands =\n'
            '    python -m my_pkg_lint\n'
        ))
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 1
    assert configs[0].name == 'lint'
    assert configs[0].commands == ('python -m my_pkg_lint',)


def test_each_sub_command_config_missing_name():
    import pytest
    from configparser import DuplicateError  # noqa: F401  (unused; see note)

    with TemporaryDirectory() as tmp:
        _write(os.path.join(tmp, 'setup.py'), '')
        _write(os.path.join(tmp, 'setup.cfg'), '[setup.command.test]\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(tmp))

# Generated at 2026-10-24 23:34:55.551908
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 23:34:56.883915
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 2

    assert configs[0].name == 'test'
    assert configs[0].camel == 'test'
    assert configs[0].description == ''
    assert configs[0].commands == ('python -m pytest', 'python -m flake8')

    assert configs[1].name == 'docs.my_pkg'
    assert configs[1].camel == 'docsMyPkg'
    assert configs[1].description == 'Build the docs for my_pkg'
    assert configs[1].commands == ('sphinx-build -b html docs docs/_build/html',)


def test_each_sub_command_config_setup_commands_cfg():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        # setup_commands.cfg, when present, replaces setup.cfg entirely
        # for command sections (but 'name' still comes from setup.cfg).
        _write(os.path.join(tmp, 'setup_commands.cfg'), (
            '[setup.command.lint]\n'
            'commands =\n'
            '    python -m my_pkg_lint\n'
        ))
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 1
    assert configs[0].name == 'lint'
    assert configs[0].commands == ('python -m my_pkg_lint',)


def test_each_sub_command_config_missing_name():
    import pytest
    from configparser import DuplicateError  # noqa: F401  (unused; see note)

    with TemporaryDirectory() as tmp:
        _write(os.path.join(tmp, 'setup.py'), '')
        _write(os.path.join(tmp, 'setup.cfg'), '[setup.command.test]\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(tmp))

# Generated at 2026-10-24 23:35:05.787951
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:35:08.208602
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:35:10.628194
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:35:13.043150
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:35:15.462097
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:35:17.880997
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:35:20.300744
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:35:22.718001
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:35:25.135716
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:35:27.555355
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:35:29.973297
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:35:32.391835
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:35:34.832589
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:35:37.254594
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:35:39.671150
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:35:42.090208
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:35:44.507663
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:35:46.925434
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:35:49.342168
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:35:51.756652
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:35:54.174792
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:35:56.592480
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:35:59.008647
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:01.424623
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:03.841831
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:06.258366
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:08.676849
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:11.099669
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:13.516807
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:15.932244
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:18.351914
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:20.768718
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:23.186336
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:25.604369
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:28.023418
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:30.440264
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:32.857424
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:35.274284
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:37.694257
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:40.111763
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:42.528099
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:44.943949
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:47.362582
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:49.777237
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:52.196061
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:54.613571
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:57.029272
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:36:59.448140
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:01.864380
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:04.281665
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:06.697787
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:09.115698
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:11.533201
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:13.949552
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:16.368342
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:18.784637
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:21.201870
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:23.620013
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:26.034344
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:28.450900
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:30.868141
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:33.283570
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:35.699419
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:38.116572
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:40.539497
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:42.956362
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:45.374612
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:47.791970
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:50.212125
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:52.629066
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:55.045233
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:57.463764
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:37:59.880951
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:38:02.298684
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:38:04.714899
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:38:07.134032
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:38:09.550825
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:38:11.965488
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:38:14.383113
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:38:16.800827
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:38:19.218537
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:38:21.636413
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:38:24.084565
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:38:26.469976
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:38:28.887188
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:38:31.305057
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:38:33.720415
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:38:36.138156
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:38:38.554487
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:38:40.972885
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:38:43.388920
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:38:45.806309
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:38:48.224650
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:38:50.639548
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:38:53.058868
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:38:55.477171
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:38:57.900762
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:39:01.251753
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:39:03.668314
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:39:06.083696
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:39:07.471104
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 2

    assert configs[0].name == 'test'
    assert configs[0].camel == 'test'
    assert configs[0].description == ''
    assert configs[0].commands == ('python -m pytest', 'python -m flake8')

    assert configs[1].name == 'docs.my_pkg'
    assert configs[1].camel == 'docsMyPkg'
    assert configs[1].description == 'Build the docs for my_pkg'
    assert configs[1].commands == ('sphinx-build -b html docs docs/_build/html',)


def test_each_sub_command_config_setup_commands_cfg():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        # setup_commands.cfg, when present, replaces setup.cfg entirely
        # for command sections (but 'name' still comes from setup.cfg).
        _write(os.path.join(tmp, 'setup_commands.cfg'), (
            '[setup.command.lint]\n'
            'commands =\n'
            '    python -m my_pkg_lint\n'
        ))
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 1
    assert configs[0].name == 'lint'
    assert configs[0].commands == ('python -m my_pkg_lint',)


def test_each_sub_command_config_missing_name():
    import pytest
    from configparser import DuplicateError  # noqa: F401  (unused; see note)

    with TemporaryDirectory() as tmp:
        _write(os.path.join(tmp, 'setup.py'), '')
        _write(os.path.join(tmp, 'setup.cfg'), '[setup.command.test]\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(tmp))

# Generated at 2026-10-24 23:39:15.339966
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:39:16.794271
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 2

    assert configs[0].name == 'test'
    assert configs[0].camel == 'test'
    assert configs[0].description == ''
    assert configs[0].commands == ('python -m pytest', 'python -m flake8')

    assert configs[1].name == 'docs.my_pkg'
    assert configs[1].camel == 'docsMyPkg'
    assert configs[1].description == 'Build the docs for my_pkg'
    assert configs[1].commands == ('sphinx-build -b html docs docs/_build/html',)


def test_each_sub_command_config_setup_commands_cfg():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        # setup_commands.cfg, when present, replaces setup.cfg entirely
        # for command sections (but 'name' still comes from setup.cfg).
        _write(os.path.join(tmp, 'setup_commands.cfg'), (
            '[setup.command.lint]\n'
            'commands =\n'
            '    python -m my_pkg_lint\n'
        ))
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 1
    assert configs[0].name == 'lint'
    assert configs[0].commands == ('python -m my_pkg_lint',)


def test_each_sub_command_config_missing_name():
    import pytest
    from configparser import DuplicateError  # noqa: F401  (unused; see note)

    with TemporaryDirectory() as tmp:
        _write(os.path.join(tmp, 'setup.py'), '')
        _write(os.path.join(tmp, 'setup.cfg'), '[setup.command.test]\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(tmp))

# Generated at 2026-10-24 23:39:27.788081
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:39:29.114860
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 2

    assert configs[0].name == 'test'
    assert configs[0].camel == 'test'
    assert configs[0].description == ''
    assert configs[0].commands == ('python -m pytest', 'python -m flake8')

    assert configs[1].name == 'docs.my_pkg'
    assert configs[1].camel == 'docsMyPkg'
    assert configs[1].description == 'Build the docs for my_pkg'
    assert configs[1].commands == ('sphinx-build -b html docs docs/_build/html',)


def test_each_sub_command_config_setup_commands_cfg():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        # setup_commands.cfg, when present, replaces setup.cfg entirely
        # for command sections (but 'name' still comes from setup.cfg).
        _write(os.path.join(tmp, 'setup_commands.cfg'), (
            '[setup.command.lint]\n'
            'commands =\n'
            '    python -m my_pkg_lint\n'
        ))
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 1
    assert configs[0].name == 'lint'
    assert configs[0].commands == ('python -m my_pkg_lint',)


def test_each_sub_command_config_missing_name():
    import pytest
    from configparser import DuplicateError  # noqa: F401  (unused; see note)

    with TemporaryDirectory() as tmp:
        _write(os.path.join(tmp, 'setup.py'), '')
        _write(os.path.join(tmp, 'setup.cfg'), '[setup.command.test]\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(tmp))

# Generated at 2026-10-24 23:39:37.149503
# Unit test for function each_sub_command_config
def test_each_sub_command_config():from pathlib import Path

# Generated at 2026-10-24 23:39:38.582779
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 2

    assert configs[0].name == 'test'
    assert configs[0].camel == 'test'
    assert configs[0].description == ''
    assert configs[0].commands == ('python -m pytest', 'python -m flake8')

    assert configs[1].name == 'docs.my_pkg'
    assert configs[1].camel == 'docsMyPkg'
    assert configs[1].description == 'Build the docs for my_pkg'
    assert configs[1].commands == ('sphinx-build -b html docs docs/_build/html',)


def test_each_sub_command_config_setup_commands_cfg():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        # setup_commands.cfg, when present, replaces setup.cfg entirely
        # for command sections (but 'name' still comes from setup.cfg).
        _write(os.path.join(tmp, 'setup_commands.cfg'), (
            '[setup.command.lint]\n'
            'commands =\n'
            '    python -m my_pkg_lint\n'
        ))
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 1
    assert configs[0].name == 'lint'
    assert configs[0].commands == ('python -m my_pkg_lint',)


def test_each_sub_command_config_missing_name():
    import pytest
    from configparser import DuplicateError  # noqa: F401  (unused; see note)

    with TemporaryDirectory() as tmp:
        _write(os.path.join(tmp, 'setup.py'), '')
        _write(os.path.join(tmp, 'setup.cfg'), '[setup.command.test]\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(tmp))

# Generated at 2026-10-24 23:39:49.744272
# Unit test for function each_sub_command_config
def test_each_sub_command_config():from pathlib import Path

# Generated at 2026-10-24 23:39:52.300272
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:39:54.684148
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:39:57.104833
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:39:59.523608
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:40:01.945327
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:40:04.548208
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:40:06.964244
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:40:09.385332
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:40:11.803261
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:40:14.222841
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:40:16.639208
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:40:19.058191
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:40:21.472713
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:40:23.889113
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:40:26.305913
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:40:31.358404
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:40:33.775566
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:40:36.194802
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:40:38.615495
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:40:41.033469
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:40:43.451350
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:40:45.865624
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:40:48.282356
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:40:50.698502
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:40:53.118669
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:40:55.538250
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:40:57.952344
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:41:00.369185
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:41:02.784770
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:41:05.199380
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:41:07.618180
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:41:16.170190
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:41:17.506097
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 2

    assert configs[0].name == 'test'
    assert configs[0].camel == 'test'
    assert configs[0].description == ''
    assert configs[0].commands == ('python -m pytest', 'python -m flake8')

    assert configs[1].name == 'docs.my_pkg'
    assert configs[1].camel == 'docsMyPkg'
    assert configs[1].description == 'Build the docs for my_pkg'
    assert configs[1].commands == ('sphinx-build -b html docs docs/_build/html',)


def test_each_sub_command_config_setup_commands_cfg():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        # setup_commands.cfg, when present, replaces setup.cfg entirely
        # for command sections (but 'name' still comes from setup.cfg).
        _write(os.path.join(tmp, 'setup_commands.cfg'), (
            '[setup.command.lint]\n'
            'commands =\n'
            '    python -m my_pkg_lint\n'
        ))
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 1
    assert configs[0].name == 'lint'
    assert configs[0].commands == ('python -m my_pkg_lint',)


def test_each_sub_command_config_missing_name():
    import pytest
    from configparser import DuplicateError  # noqa: F401  (unused; see note)

    with TemporaryDirectory() as tmp:
        _write(os.path.join(tmp, 'setup.py'), '')
        _write(os.path.join(tmp, 'setup.cfg'), '[setup.command.test]\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(tmp))

# Generated at 2026-10-24 23:41:26.330176
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:41:27.677654
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 2

    assert configs[0].name == 'test'
    assert configs[0].camel == 'test'
    assert configs[0].description == ''
    assert configs[0].commands == ('python -m pytest', 'python -m flake8')

    assert configs[1].name == 'docs.my_pkg'
    assert configs[1].camel == 'docsMyPkg'
    assert configs[1].description == 'Build the docs for my_pkg'
    assert configs[1].commands == ('sphinx-build -b html docs docs/_build/html',)


def test_each_sub_command_config_setup_commands_cfg():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        # setup_commands.cfg, when present, replaces setup.cfg entirely
        # for command sections (but 'name' still comes from setup.cfg).
        _write(os.path.join(tmp, 'setup_commands.cfg'), (
            '[setup.command.lint]\n'
            'commands =\n'
            '    python -m my_pkg_lint\n'
        ))
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 1
    assert configs[0].name == 'lint'
    assert configs[0].commands == ('python -m my_pkg_lint',)


def test_each_sub_command_config_missing_name():
    import pytest
    from configparser import DuplicateError  # noqa: F401  (unused; see note)

    with TemporaryDirectory() as tmp:
        _write(os.path.join(tmp, 'setup.py'), '')
        _write(os.path.join(tmp, 'setup.cfg'), '[setup.command.test]\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(tmp))

# Generated at 2026-10-24 23:41:38.908035
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:41:40.243941
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 2

    assert configs[0].name == 'test'
    assert configs[0].camel == 'test'
    assert configs[0].description == ''
    assert configs[0].commands == ('python -m pytest', 'python -m flake8')

    assert configs[1].name == 'docs.my_pkg'
    assert configs[1].camel == 'docsMyPkg'
    assert configs[1].description == 'Build the docs for my_pkg'
    assert configs[1].commands == ('sphinx-build -b html docs docs/_build/html',)


def test_each_sub_command_config_setup_commands_cfg():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        # setup_commands.cfg, when present, replaces setup.cfg entirely
        # for command sections (but 'name' still comes from setup.cfg).
        _write(os.path.join(tmp, 'setup_commands.cfg'), (
            '[setup.command.lint]\n'
            'commands =\n'
            '    python -m my_pkg_lint\n'
        ))
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 1
    assert configs[0].name == 'lint'
    assert configs[0].commands == ('python -m my_pkg_lint',)


def test_each_sub_command_config_missing_name():
    import pytest
    from configparser import DuplicateError  # noqa: F401  (unused; see note)

    with TemporaryDirectory() as tmp:
        _write(os.path.join(tmp, 'setup.py'), '')
        _write(os.path.join(tmp, 'setup.cfg'), '[setup.command.test]\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(tmp))

# Generated at 2026-10-24 23:41:55.290958
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 23:41:56.645518
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 2

    assert configs[0].name == 'test'
    assert configs[0].camel == 'test'
    assert configs[0].description == ''
    assert configs[0].commands == ('python -m pytest', 'python -m flake8')

    assert configs[1].name == 'docs.my_pkg'
    assert configs[1].camel == 'docsMyPkg'
    assert configs[1].description == 'Build the docs for my_pkg'
    assert configs[1].commands == ('sphinx-build -b html docs docs/_build/html',)


def test_each_sub_command_config_setup_commands_cfg():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        # setup_commands.cfg, when present, replaces setup.cfg entirely
        # for command sections (but 'name' still comes from setup.cfg).
        _write(os.path.join(tmp, 'setup_commands.cfg'), (
            '[setup.command.lint]\n'
            'commands =\n'
            '    python -m my_pkg_lint\n'
        ))
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 1
    assert configs[0].name == 'lint'
    assert configs[0].commands == ('python -m my_pkg_lint',)


def test_each_sub_command_config_missing_name():
    import pytest
    from configparser import DuplicateError  # noqa: F401  (unused; see note)

    with TemporaryDirectory() as tmp:
        _write(os.path.join(tmp, 'setup.py'), '')
        _write(os.path.join(tmp, 'setup.cfg'), '[setup.command.test]\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(tmp))

# Generated at 2026-10-24 23:42:05.424845
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 23:42:14.035592
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 2

    assert configs[0].name == 'test'
    assert configs[0].camel == 'test'
    assert configs[0].description == ''
    assert configs[0].commands == ('python -m pytest', 'python -m flake8')

    assert configs[1].name == 'docs.my_pkg'
    assert configs[1].camel == 'docsMyPkg'
    assert configs[1].description == 'Build the docs for my_pkg'
    assert configs[1].commands == ('sphinx-build -b html docs docs/_build/html',)


def test_each_sub_command_config_setup_commands_cfg():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        # setup_commands.cfg, when present, replaces setup.cfg entirely
        # for command sections (but 'name' still comes from setup.cfg).
        _write(os.path.join(tmp, 'setup_commands.cfg'), (
            '[setup.command.lint]\n'
            'commands =\n'
            '    python -m my_pkg_lint\n'
        ))
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 1
    assert configs[0].name == 'lint'
    assert configs[0].commands == ('python -m my_pkg_lint',)


def test_each_sub_command_config_missing_name():
    import pytest
    from configparser import DuplicateError  # noqa: F401  (unused; see note)

    with TemporaryDirectory() as tmp:
        _write(os.path.join(tmp, 'setup.py'), '')
        _write(os.path.join(tmp, 'setup.cfg'), '[setup.command.test]\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(tmp))

# Generated at 2026-10-24 23:42:26.122007
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:42:27.454829
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 2

    assert configs[0].name == 'test'
    assert configs[0].camel == 'test'
    assert configs[0].description == ''
    assert configs[0].commands == ('python -m pytest', 'python -m flake8')

    assert configs[1].name == 'docs.my_pkg'
    assert configs[1].camel == 'docsMyPkg'
    assert configs[1].description == 'Build the docs for my_pkg'
    assert configs[1].commands == ('sphinx-build -b html docs docs/_build/html',)


def test_each_sub_command_config_setup_commands_cfg():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        # setup_commands.cfg, when present, replaces setup.cfg entirely
        # for command sections (but 'name' still comes from setup.cfg).
        _write(os.path.join(tmp, 'setup_commands.cfg'), (
            '[setup.command.lint]\n'
            'commands =\n'
            '    python -m my_pkg_lint\n'
        ))
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 1
    assert configs[0].name == 'lint'
    assert configs[0].commands == ('python -m my_pkg_lint',)


def test_each_sub_command_config_missing_name():
    import pytest
    from configparser import DuplicateError  # noqa: F401  (unused; see note)

    with TemporaryDirectory() as tmp:
        _write(os.path.join(tmp, 'setup.py'), '')
        _write(os.path.join(tmp, 'setup.cfg'), '[setup.command.test]\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(tmp))

# Generated at 2026-10-24 23:42:36.250179
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile


# Generated at 2026-10-24 23:42:37.583428
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 2

    assert configs[0].name == 'test'
    assert configs[0].camel == 'test'
    assert configs[0].description == ''
    assert configs[0].commands == ('python -m pytest', 'python -m flake8')

    assert configs[1].name == 'docs.my_pkg'
    assert configs[1].camel == 'docsMyPkg'
    assert configs[1].description == 'Build the docs for my_pkg'
    assert configs[1].commands == ('sphinx-build -b html docs docs/_build/html',)


def test_each_sub_command_config_setup_commands_cfg():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        # setup_commands.cfg, when present, replaces setup.cfg entirely
        # for command sections (but 'name' still comes from setup.cfg).
        _write(os.path.join(tmp, 'setup_commands.cfg'), (
            '[setup.command.lint]\n'
            'commands =\n'
            '    python -m my_pkg_lint\n'
        ))
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 1
    assert configs[0].name == 'lint'
    assert configs[0].commands == ('python -m my_pkg_lint',)


def test_each_sub_command_config_missing_name():
    import pytest
    from configparser import DuplicateError  # noqa: F401  (unused; see note)

    with TemporaryDirectory() as tmp:
        _write(os.path.join(tmp, 'setup.py'), '')
        _write(os.path.join(tmp, 'setup.cfg'), '[setup.command.test]\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(tmp))

# Generated at 2026-10-24 23:42:46.283627
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:42:47.735785
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 2

    assert configs[0].name == 'test'
    assert configs[0].camel == 'test'
    assert configs[0].description == ''
    assert configs[0].commands == ('python -m pytest', 'python -m flake8')

    assert configs[1].name == 'docs.my_pkg'
    assert configs[1].camel == 'docsMyPkg'
    assert configs[1].description == 'Build the docs for my_pkg'
    assert configs[1].commands == ('sphinx-build -b html docs docs/_build/html',)


def test_each_sub_command_config_setup_commands_cfg():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        # setup_commands.cfg, when present, replaces setup.cfg entirely
        # for command sections (but 'name' still comes from setup.cfg).
        _write(os.path.join(tmp, 'setup_commands.cfg'), (
            '[setup.command.lint]\n'
            'commands =\n'
            '    python -m my_pkg_lint\n'
        ))
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 1
    assert configs[0].name == 'lint'
    assert configs[0].commands == ('python -m my_pkg_lint',)


def test_each_sub_command_config_missing_name():
    import pytest
    from configparser import DuplicateError  # noqa: F401  (unused; see note)

    with TemporaryDirectory() as tmp:
        _write(os.path.join(tmp, 'setup.py'), '')
        _write(os.path.join(tmp, 'setup.cfg'), '[setup.command.test]\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(tmp))

# Generated at 2026-10-24 23:43:03.076541
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:43:04.410326
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 2

    assert configs[0].name == 'test'
    assert configs[0].camel == 'test'
    assert configs[0].description == ''
    assert configs[0].commands == ('python -m pytest', 'python -m flake8')

    assert configs[1].name == 'docs.my_pkg'
    assert configs[1].camel == 'docsMyPkg'
    assert configs[1].description == 'Build the docs for my_pkg'
    assert configs[1].commands == ('sphinx-build -b html docs docs/_build/html',)


def test_each_sub_command_config_setup_commands_cfg():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        # setup_commands.cfg, when present, replaces setup.cfg entirely
        # for command sections (but 'name' still comes from setup.cfg).
        _write(os.path.join(tmp, 'setup_commands.cfg'), (
            '[setup.command.lint]\n'
            'commands =\n'
            '    python -m my_pkg_lint\n'
        ))
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 1
    assert configs[0].name == 'lint'
    assert configs[0].commands == ('python -m my_pkg_lint',)


def test_each_sub_command_config_missing_name():
    import pytest
    from configparser import DuplicateError  # noqa: F401  (unused; see note)

    with TemporaryDirectory() as tmp:
        _write(os.path.join(tmp, 'setup.py'), '')
        _write(os.path.join(tmp, 'setup.cfg'), '[setup.command.test]\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(tmp))

# Generated at 2026-10-24 23:43:13.829584
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:43:15.222171
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 2

    assert configs[0].name == 'test'
    assert configs[0].camel == 'test'
    assert configs[0].description == ''
    assert configs[0].commands == ('python -m pytest', 'python -m flake8')

    assert configs[1].name == 'docs.my_pkg'
    assert configs[1].camel == 'docsMyPkg'
    assert configs[1].description == 'Build the docs for my_pkg'
    assert configs[1].commands == ('sphinx-build -b html docs docs/_build/html',)


def test_each_sub_command_config_setup_commands_cfg():
    with TemporaryDirectory() as tmp:
        _make_setup_dir(tmp)
        # setup_commands.cfg, when present, replaces setup.cfg entirely
        # for command sections (but 'name' still comes from setup.cfg).
        _write(os.path.join(tmp, 'setup_commands.cfg'), (
            '[setup.command.lint]\n'
            'commands =\n'
            '    python -m my_pkg_lint\n'
        ))
        configs = list(module_0.each_sub_command_config(tmp))

    assert len(configs) == 1
    assert configs[0].name == 'lint'
    assert configs[0].commands == ('python -m my_pkg_lint',)


def test_each_sub_command_config_missing_name():
    import pytest
    from configparser import DuplicateError  # noqa: F401  (unused; see note)

    with TemporaryDirectory() as tmp:
        _write(os.path.join(tmp, 'setup.py'), '')
        _write(os.path.join(tmp, 'setup.cfg'), '[setup.command.test]\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(tmp))

# Generated at 2026-10-24 23:43:33.285049
# Unit test for function each_sub_command_config