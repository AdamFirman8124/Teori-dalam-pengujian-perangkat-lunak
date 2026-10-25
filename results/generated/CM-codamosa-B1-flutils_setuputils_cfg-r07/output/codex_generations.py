

# Generated at 2026-10-24 20:36:08.436412
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 20:36:10.853490
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 20:36:13.273075
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 20:36:15.848020
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 20:36:18.274753
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 20:36:20.699010
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 20:36:23.115843
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-24 20:36:25.529012
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-24 20:36:28.106356
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-24 20:36:30.524707
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 20:36:33.083113
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 20:36:35.501478
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 20:36:37.920859
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-24 20:36:40.332978
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-24 20:36:42.750009
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-24 20:36:45.168385
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 20:36:47.584802
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 20:36:59.262936
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile


# Generated at 2026-10-24 20:37:21.603255
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

# Generated at 2026-10-24 20:37:32.761938
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 20:37:34.195726
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

# Generated at 2026-10-24 20:37:42.726700
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 20:37:45.243902
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 20:37:47.768248
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 20:37:57.274196
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 20:37:58.566779
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

# Generated at 2026-10-24 20:38:09.013175
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 20:38:10.359367
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

# Generated at 2026-10-24 20:38:19.353960
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 20:38:20.788572
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

# Generated at 2026-10-24 20:38:29.592348
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 20:38:30.926614
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

# Generated at 2026-10-24 20:38:41.965740
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 20:38:43.639933
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

# Generated at 2026-10-24 20:38:54.170023
# Unit test for function each_sub_command_config
def test_each_sub_command_config():from pathlib import Path

# Generated at 2026-10-24 20:38:55.808805
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

# Generated at 2026-10-24 20:39:07.995762
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 20:39:09.655935
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

# Generated at 2026-10-24 20:39:18.828522
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 20:39:20.159486
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

# Generated at 2026-10-24 20:39:34.004163
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 20:39:35.426816
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

# Generated at 2026-10-24 20:39:43.015703
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 20:39:44.335217
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

# Generated at 2026-10-24 20:39:58.951759
# Unit test for function each_sub_command_config
def test_each_sub_command_config():from pathlib import Path

# Generated at 2026-10-24 20:40:03.499212
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

# Generated at 2026-10-24 20:40:15.270471
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 20:40:16.940199
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

# Generated at 2026-10-24 20:40:24.486689
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 20:40:25.867820
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

# Generated at 2026-10-24 20:40:36.675320
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 20:40:38.134784
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

# Generated at 2026-10-24 20:40:47.015152
# Unit test for function each_sub_command_config
def test_each_sub_command_config():from pathlib import Path

# Generated at 2026-10-24 20:40:48.452124
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

# Generated at 2026-10-24 20:40:58.180388
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 20:40:59.835332
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

# Generated at 2026-10-24 20:41:09.778043
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 20:41:11.394315
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

# Generated at 2026-10-24 20:41:21.345675
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 20:41:22.964105
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

# Generated at 2026-10-24 20:41:31.558949
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 20:41:32.995899
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

# Generated at 2026-10-24 20:41:41.547867
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 20:41:42.971597
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

# Generated at 2026-10-24 20:41:51.833651
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 20:41:53.258730
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

# Generated at 2026-10-24 20:42:02.791775
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 20:42:04.225892
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

# Generated at 2026-10-24 20:42:14.650411
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 20:42:15.979066
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

# Generated at 2026-10-24 20:42:25.703372
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 20:42:27.024617
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

# Generated at 2026-10-24 20:42:41.498021
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 20:42:43.918048
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 20:42:46.335771
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 20:42:48.756637
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 20:42:51.173541
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 20:43:27.272747
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 20:43:38.549895
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 20:43:39.895110
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

# Generated at 2026-10-24 20:43:49.491775
# Unit test for function each_sub_command_config
def test_each_sub_command_config():from pathlib import Path

# Generated at 2026-10-24 20:43:52.028470
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 20:43:54.444467
# Unit test for function each_sub_command_config

# Generated at 2026-10-24 20:44:23.282998
# Unit test for function each_sub_command_config
def test_each_sub_command_config():from pathlib import Path

# Generated at 2026-10-24 20:44:24.613716
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

# Generated at 2026-10-24 20:44:36.903413
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 20:44:38.339338
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

# Generated at 2026-10-24 20:44:44.788885
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile


# Generated at 2026-10-24 20:44:46.149438
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

# Generated at 2026-10-24 20:44:55.340503
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 20:44:56.788976
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

# Generated at 2026-10-24 20:45:07.932644
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-24 20:45:09.259542
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

# Generated at 2026-10-24 20:45:20.833894
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 20:45:22.293428
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

# Generated at 2026-10-24 20:45:31.706133
# Unit test for function each_sub_command_config
def test_each_sub_command_config():tempfile = __import__('tempfile')

# Generated at 2026-10-24 20:45:33.057763
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

# Generated at 2026-10-24 20:45:43.186718
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 20:45:44.556859
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

# Generated at 2026-10-24 20:45:54.318700
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-24 20:46:06.506403
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

# Generated at 2026-10-24 20:46:07.854989
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

# Generated at 2026-10-24 20:46:19.920301
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile