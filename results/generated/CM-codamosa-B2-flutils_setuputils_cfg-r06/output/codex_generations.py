

# Generated at 2026-10-24 23:11:54.444214
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

# Generated at 2026-10-24 23:11:55.805985
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

# Generated at 2026-10-24 23:12:06.248908
# Unit test for function each_sub_command_config
def test_each_sub_command_config():from pathlib import Path

# Generated at 2026-10-24 23:12:07.593285
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

# Generated at 2026-10-24 23:12:08.925598
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

# Generated at 2026-10-24 23:12:18.538284
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile


# Generated at 2026-10-24 23:12:19.970573
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

# Generated at 2026-10-24 23:12:30.006565
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:12:31.339227
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

# Generated at 2026-10-24 23:12:43.732883
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile


# Generated at 2026-10-24 23:12:45.095024
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

# Generated at 2026-10-24 23:12:54.581884
# Unit test for function each_sub_command_config
def test_each_sub_command_config():from pathlib import Path

# Generated at 2026-10-24 23:12:56.016535
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

# Generated at 2026-10-24 23:13:05.334137
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile


# Generated at 2026-10-24 23:13:06.686290
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

# Generated at 2026-10-24 23:13:15.362450
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 23:13:16.823074
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

# Generated at 2026-10-24 23:13:28.015514
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 23:13:29.346683
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

# Generated at 2026-10-24 23:13:39.228634
# Unit test for function each_sub_command_config
def test_each_sub_command_config():from pathlib import Path

# Generated at 2026-10-24 23:13:40.586643
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

# Generated at 2026-10-24 23:13:53.769229
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 23:13:55.112273
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

# Generated at 2026-10-24 23:14:04.828281
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 23:14:06.184823
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

# Generated at 2026-10-24 23:14:16.373126
# Unit test for function each_sub_command_config
def test_each_sub_command_config():from pathlib import Path

# Generated at 2026-10-24 23:14:18.038676
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

# Generated at 2026-10-24 23:14:29.712143
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:14:31.044994
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

# Generated at 2026-10-24 23:14:41.496639
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:14:42.824848
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

# Generated at 2026-10-24 23:14:53.059353
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:14:54.392723
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

# Generated at 2026-10-24 23:15:02.996265
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:15:04.328616
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

# Generated at 2026-10-24 23:15:16.918780
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:15:19.339508
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:15:21.761103
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:15:24.183357
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:15:26.598248
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:15:29.017590
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:15:42.416002
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 23:15:43.741681
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

# Generated at 2026-10-24 23:15:53.169596
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile


# Generated at 2026-10-24 23:15:54.517860
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

# Generated at 2026-10-24 23:16:06.378368
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 23:16:08.799809
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:16:11.385932
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:16:13.807125
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:16:16.223059
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:16:18.643786
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:16:21.059894
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:16:23.477461
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:16:25.895554
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:16:28.325508
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:16:30.743789
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:16:33.160383
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:16:35.578651
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:16:37.996326
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:16:40.416885
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:16:42.833885
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:16:45.433502
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile

    with tempfile.TemporaryDirectory() as setup_dir:
        # Create required files: setup.py and setup.cfg
        open(os.path.join(setup_dir, 'setup.py'), 'w').close()
        setup_cfg_path = os.path.join(setup_dir, 'setup.cfg')
        with open(setup_cfg_path, 'w') as f:
            f.write(
                '[metadata]\n'
                'name = test_pkg\n'
                '\n'
                '[setup.command.build]\n'
                'commands =\n'
                '    echo building {name}\n'
                '    echo home is {home}\n'
                '    \n'
                '    echo dir is {setup_dir}\n'
                '\n'
                '[setup.command.run-tests]\n'
                'name = my_test\n'
                'description = Runs tests for {name}\n'
                'command = echo testing {name}\n'
            )

        results = list(module_0.each_sub_command_config(setup_dir))

        # Two valid command sections were found
        assert len(results) == 2

        build = results[0]
        assert build.name == 'build'
        assert build.camel == 'Build'
        assert build.description == ''
        assert build.commands == [
            'echo building test_pkg',
            'echo home is %s' % os.path.expanduser('~'),
            'echo dir is %s' % os.path.realpath(setup_dir),
        ]

        test_cmd = results[1]
        assert test_cmd.name == 'my_test'
        assert test_cmd.camel == 'MyTest'
        assert test_cmd.description == 'Runs tests for test_pkg'
        assert test_cmd.commands == ['echo testing test_pkg']

        # setup_commands.cfg overrides setup.cfg commands
        with open(os.path.join(setup_dir, 'setup_commands.cfg'), 'w') as f:
            f.write(
                '[setup.command.build]\n'
                'commands = echo overridden {name}\n'
            )

        results = list(module_0.each_sub_command_config(setup_dir))
        assert len(results) == 1
        assert results[0].name == 'build'
        assert results[0].commands == ['echo overridden test_pkg']

        # Missing 'name' option in [metadata] raises LookupError
        with open(setup_cfg_path, 'w') as f:
            f.write('[metadata]\n')
        try:
            list(module_0.each_sub_command_config(setup_dir))
        except LookupError:
            pass
        else:
            raise AssertionError('Expected LookupError for missing name option')

        # Missing [metadata] section raises LookupError
        with open(setup_cfg_path, 'w') as f:
            f.write('[other]\nfoo = bar\n')
        try:
            list(module_0.each_sub_command_config(setup_dir))
        except LookupError:
            pass
        else:
            raise AssertionError('Expected LookupError for missing metadata section')

    # Non-existent setup_dir raises FileNotFoundError
    try:
        list(module_0.each_sub_command_config('/does/not/exist'))
    except FileNotFoundError:
        pass
    else:
        raise AssertionError('Expected FileNotFoundError for bad setup_dir')

# Generated at 2026-10-24 23:16:46.764499
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

# Generated at 2026-10-24 23:16:54.763549
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:16:56.095508
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

# Generated at 2026-10-24 23:17:04.236294
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile


# Generated at 2026-10-24 23:17:05.570137
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

# Generated at 2026-10-24 23:17:14.644222
# Unit test for function each_sub_command_config
def test_each_sub_command_config():from pathlib import Path

# Generated at 2026-10-24 23:17:15.987199
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

# Generated at 2026-10-24 23:17:27.581320
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 23:17:30.007398
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:17:32.424295
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:17:34.841609
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:17:37.263995
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:17:39.678810
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:17:42.094384
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:17:44.511919
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:17:46.929109
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:17:49.349237
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:17:51.766919
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:17:54.182819
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:17:56.599815
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:17:59.015447
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:18:01.436079
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:18:03.856202
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:18:05.197719
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

# Generated at 2026-10-24 23:18:17.860732
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:18:19.199042
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

# Generated at 2026-10-24 23:18:28.496293
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:18:29.945131
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

# Generated at 2026-10-24 23:18:40.389943
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 23:18:42.809372
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:18:45.230056
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:18:47.650260
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:18:50.176296
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:18:52.592006
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:18:55.007980
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:18:57.426831
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:18:59.853553
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:19:02.271264
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:19:04.691473
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:19:07.107840
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:19:09.530637
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:19:12.322156
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:19:14.738355
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:19:17.153508
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:19:19.571237
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:19:21.990684
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:19:24.411049
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:19:26.829437
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:19:29.252495
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:19:55.449130
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile


# Generated at 2026-10-24 23:19:56.807331
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

# Generated at 2026-10-24 23:20:07.326490
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:20:09.746191
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:20:12.163959
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:20:14.710930
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:20:17.124855
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:20:19.542509
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:20:21.958296
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:20:24.376280
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:20:26.791157
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:20:29.376220
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:20:31.802213
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:20:34.212653
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:20:36.631351
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:20:38.009020
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

# Generated at 2026-10-24 23:20:46.749967
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:20:48.098307
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

# Generated at 2026-10-24 23:20:57.606499
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:20:58.942217
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

# Generated at 2026-10-24 23:21:09.023321
# Unit test for function each_sub_command_config
def test_each_sub_command_config():from pathlib import Path

# Generated at 2026-10-24 23:21:10.357486
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

# Generated at 2026-10-24 23:21:20.440680
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:21:22.861274
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:21:25.391795
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:21:27.808081
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:21:30.226163
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:21:32.642528
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:21:35.218949
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:21:37.633319
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:21:40.051275
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:21:42.466621
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 23:21:43.807537
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

# Generated at 2026-10-24 23:21:52.393265
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 23:21:54.149362
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

# Generated at 2026-10-24 23:22:05.525489
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile