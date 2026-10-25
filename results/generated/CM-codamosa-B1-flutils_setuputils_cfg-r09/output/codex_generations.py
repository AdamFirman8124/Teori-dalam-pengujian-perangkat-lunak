

# Generated at 2026-10-24 22:01:39.160942
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

# Generated at 2026-10-24 22:01:40.591656
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

# Generated at 2026-10-24 22:01:41.927290
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

# Generated at 2026-10-24 22:01:50.732994
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 22:01:52.055913
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

# Generated at 2026-10-24 22:01:53.425249
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

# Generated at 2026-10-24 22:02:03.120065
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 22:02:04.543183
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

# Generated at 2026-10-24 22:02:15.305724
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 22:02:16.742348
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

# Generated at 2026-10-24 22:02:19.162071
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:02:21.579922
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:02:24.097944
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:02:26.625278
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:02:29.042251
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:02:31.460964
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:02:40.599418
# Unit test for function each_sub_command_config
def test_each_sub_command_config():from pathlib import Path

# Generated at 2026-10-24 22:02:41.930787
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

# Generated at 2026-10-24 22:02:51.768343
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 22:02:53.093332
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

# Generated at 2026-10-24 22:03:01.692740
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 22:03:03.082815
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

# Generated at 2026-10-24 22:03:13.749736
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 22:03:15.106785
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

# Generated at 2026-10-24 22:03:17.531004
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:03:20.065799
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:03:22.483464
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:03:24.902544
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:03:27.317994
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:03:29.738156
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:03:32.156861
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:03:34.570113
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:03:36.990398
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:03:39.407535
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:03:41.826474
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:03:44.241122
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:03:46.658876
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:03:49.077187
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:03:51.494303
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:03:53.915609
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:03:56.335460
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:03:58.753570
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:04:08.469418
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 22:04:09.791686
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

# Generated at 2026-10-24 22:04:20.643637
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 22:04:22.095361
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

# Generated at 2026-10-24 22:04:32.918863
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile


# Generated at 2026-10-24 22:04:34.248768
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

# Generated at 2026-10-24 22:04:44.197234
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 22:04:46.619828
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:04:49.038951
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:04:51.459824
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:04:53.881366
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:04:56.299017
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:04:58.714731
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:05:01.133113
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:05:03.550614
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:05:05.966420
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:05:08.382296
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:05:10.801594
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:05:13.218007
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:05:15.632889
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:05:18.047992
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:05:20.462544
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:05:22.879171
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:05:25.298413
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:05:27.714077
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:05:30.127197
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:05:32.543277
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:05:43.767438
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile


# Generated at 2026-10-24 22:05:45.229928
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

# Generated at 2026-10-24 22:05:51.984844
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 22:05:53.313538
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

# Generated at 2026-10-24 22:06:03.856735
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 22:06:05.189771
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

# Generated at 2026-10-24 22:06:12.670041
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 22:06:15.096552
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:06:17.642733
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:06:20.061945
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:06:22.477958
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:06:24.897553
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:06:27.313167
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:06:29.730462
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:06:32.145642
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:06:41.546615
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 22:06:42.879137
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

# Generated at 2026-10-24 22:06:51.684643
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile


# Generated at 2026-10-24 22:06:53.127186
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

# Generated at 2026-10-24 22:07:02.918572
# Unit test for function each_sub_command_config
def test_each_sub_command_config():from pathlib import Path

# Generated at 2026-10-24 22:07:04.258309
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

# Generated at 2026-10-24 22:07:15.239752
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 22:07:17.663453
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:07:20.082313
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:07:22.500354
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:07:25.057914
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:07:27.473957
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:07:29.890494
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:07:32.307065
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:07:34.723450
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:07:37.143176
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:07:39.560657
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:07:41.979964
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:07:44.393829
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:07:46.811994
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:08:12.275242
# Unit test for function each_sub_command_config
def test_each_sub_command_config():from pathlib import Path

# Generated at 2026-10-24 22:08:13.616713
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

# Generated at 2026-10-24 22:08:24.357042
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 22:08:25.688451
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

# Generated at 2026-10-24 22:08:33.675899
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 22:08:36.118942
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

# Generated at 2026-10-24 22:08:44.810051
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 22:08:47.331935
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:08:49.752064
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:09:07.571906
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:09:08.908385
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

# Generated at 2026-10-24 22:09:18.938094
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 22:09:20.262180
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

# Generated at 2026-10-24 22:09:29.076685
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile


# Generated at 2026-10-24 22:09:30.509268
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

# Generated at 2026-10-24 22:09:39.314728
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 22:09:41.735361
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:09:44.153316
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:09:46.575282
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:09:48.995655
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:09:51.414279
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:10:02.662315
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 22:10:04.096806
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

# Generated at 2026-10-24 22:10:13.313235
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 22:10:14.654856
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

# Generated at 2026-10-24 22:10:23.243626
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 22:10:24.680205
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

# Generated at 2026-10-24 22:10:32.667668
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 22:10:38.172456
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:10:40.590214
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:10:43.010329
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:10:45.430134
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:10:47.847087
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:10:50.263209
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:10:52.680073
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:10:55.098637
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 22:11:22.541267
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 22:11:23.873348
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

# Generated at 2026-10-24 22:11:33.668737
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile