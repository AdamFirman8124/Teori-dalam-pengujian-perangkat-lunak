

# Generated at 2026-11-01 19:21:19.754903
# Unit test for function each_sub_command_config

# Generated at 2026-11-01 19:21:40.638993
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

    # Scenario 1: commands defined directly in setup.cfg

# Generated at 2026-11-01 19:21:59.479365
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os
from pathlib import Path

import pytest


def _make_project(
        tmp_path,
        setup_cfg=None,
        commands_cfg=None,
        with_setup_py=True,
):
    setup_dir = tmp_path / 'proj'
    setup_dir.mkdir()
    if with_setup_py:
        (setup_dir / 'setup.py').write_text('# setup.py\n')
    if setup_cfg is not None:
        (setup_dir / 'setup.cfg').write_text(setup_cfg)
    if commands_cfg is not None:
        (setup_dir / 'setup_commands.cfg').write_text(commands_cfg)
    return setup_dir


METADATA = '[metadata]\nname = my_pkg\n'


def test_each_sub_command_config_basic(tmp_path):
    setup_dir = _make_project(
        tmp_path,
        setup_cfg=(
            METADATA +
            '[setup.command.build_html]\n'
            'commands =\n'
            '    echo one\n'
            '    echo two\n'
        ),
    )
    results = list(module_0.each_sub_command_config(str(setup_dir)))
    assert len(results) == 1
    cfg = results[0]
    assert isinstance(cfg, SetupCfgCommandConfig)
    assert cfg.name == 'build_html'
    assert cfg.camel == 'BuildHtml'
    assert cfg.description == ''
    assert cfg.commands == ('echo one', 'echo two')


def test_each_sub_command_config_name_description_formatting(tmp_path):
    setup_dir = _make_project(
        tmp_path,
        setup_cfg=(
            METADATA +
            '[setup.command.run_tests]\n'
            'name = test-{name}\n'
            'description = Tests for {name}\n'
            'command = echo {name}\n'
        ),
    )
    results = list(module_0.each_sub_command_config(str(setup_dir)))
    assert len(results) == 1
    cfg = results[0]
    assert cfg.name == 'test-my_pkg'
    assert cfg.camel == 'TestMyPkg'
    assert cfg.description == 'Tests for my_pkg'
    assert cfg.commands == ('echo my_pkg',)


def test_each_sub_command_config_setup_dir_and_home_formatting(tmp_path):
    setup_dir = _make_project(
        tmp_path,
        setup_cfg=(
            METADATA +
            '[setup.command.listing]\n'
            'commands =\n'
            '    ls {setup_dir}\n'
            '    ls {home}\n'
        ),
    )
    results = list(module_0.each_sub_command_config(str(setup_dir)))
    real = os.path.realpath(str(setup_dir))
    assert results[0].commands == (
        'ls %s' % real,
        'ls %s' % os.path.expanduser('~'),
    )


def test_each_sub_command_config_commands_file_override(tmp_path):
    setup_dir = _make_project(
        tmp_path,
        setup_cfg=METADATA,
        commands_cfg=(
            '[setup.command.from_file]\n'
            'commands =\n'
            '    echo from_commands_file\n'
        ),
    )
    results = list(module_0.each_sub_command_config(str(setup_dir)))
    assert len(results) == 1
    assert results[0].name == 'from_file'
    assert results[0].commands == ('echo from_commands_file',)


def test_each_sub_command_config_multiple_sections_order(tmp_path):
    setup_dir = _make_project(
        tmp_path,
        setup_cfg=(
            METADATA +
            '[setup.command.alpha]\n'
            'command = echo alpha\n'
            '\n'
            '[setup.command.beta]\n'
            'command = echo beta\n'
        ),
    )
    results = list(module_0.each_sub_command_config(Path(setup_dir)))
    assert [cfg.name for cfg in results] == ['alpha', 'beta']


def test_each_sub_command_config_skips_invalid_and_empty(tmp_path):
    setup_dir = _make_project(
        tmp_path,
        setup_cfg=(
            METADATA +
            '[setup.command.]\n'
            'command = echo empty\n'
            '\n'
            '[setup.command.bad-name!]\n'
            'command = echo bad\n'
            '\n'
            '[setup.command.good_one]\n'
            'command = echo good\n'
            '\n'
            '[other.section]\n'
            'command = echo other\n'
        ),
    )
    results = list(module_0.each_sub_command_config(str(setup_dir)))
    assert [cfg.name for cfg in results] == ['good_one']


def test_each_sub_command_config_no_command_sections(tmp_path):
    setup_dir = _make_project(tmp_path, setup_cfg=METADATA)
    assert list(module_0.each_sub_command_config(str(setup_dir))) == []


def test_each_sub_command_config_dotted_command_name(tmp_path):
    setup_dir = _make_project(
        tmp_path,
        setup_cfg=(
            METADATA +
            '[setup.command.docs.build]\n'
            'command = echo docs\n'
        ),
    )
    results = list(module_0.each_sub_command_config(str(setup_dir)))
    assert len(results) == 1
    assert results[0].name == 'docs.build'
    assert results[0].camel == 'DocsBuild'


def test_each_sub_command_config_missing_setup_dir(tmp_path):
    with pytest.raises(FileNotFoundError):
        list(module_0.each_sub_command_config(str(tmp_path / 'does_not_exist')))


def test_each_sub_command_config_not_a_directory(tmp_path):
    file_path = tmp_path / 'afile.txt'
    file_path.write_text('hello')
    with pytest.raises(NotADirectoryError):
        list(module_0.each_sub_command_config(str(file_path)))


def test_each_sub_command_config_missing_setup_py(tmp_path):
    setup_dir = tmp_path / 'proj'
    setup_dir.mkdir()
    (setup_dir / 'setup.cfg').write_text(METADATA)
    with pytest.raises(FileNotFoundError):
        list(module_0.each_sub_command_config(str(setup_dir)))


def test_each_sub_command_config_missing_setup_cfg(tmp_path):
    setup_dir = tmp_path / 'proj'
    setup_dir.mkdir()
    (setup_dir / 'setup.py').write_text('# setup.py\n')
    with pytest.raises(FileNotFoundError):
        list(module_0.each_sub_command_config(str(setup_dir)))


def test_each_sub_command_config_missing_metadata_section(tmp_path):
    setup_dir = _make_project(tmp_path, setup_cfg='[other]\nfoo = bar\n')
    with pytest.raises(LookupError):
        list(module_0.each_sub_command_config(str(setup_dir)))


def test_each_sub_command_config_missing_name_option(tmp_path):
    setup_dir = _make_project(tmp_path, setup_cfg='[metadata]\nversion = 1.0\n')
    with pytest.raises(LookupError):
        list(module_0.each_sub_command_config(str(setup_dir)))


def test_each_sub_command_config_empty_name_option(tmp_path):
    setup_dir = _make_project(tmp_path, setup_cfg='[metadata]\nname =\n')
    with pytest.raises(LookupError):
        list(module_0.each_sub_command_config(str(setup_dir)))

# Generated at 2026-11-01 19:22:15.963288
# Unit test for constructor of class SetupCfgCommandConfig
def test_SetupCfgCommandConfig():
    # Test construction with positional arguments
    name = 'build_docs'
    camel = 'BuildDocs'
    description = 'Builds the documentation.'
    commands = ('make html', 'make latex')

    config = SetupCfgCommandConfig(name, camel, description, commands)

    assert config.name == name
    assert config.camel == camel
    assert config.description == description
    assert config.commands == commands

    # Test construction with keyword arguments
    config = SetupCfgCommandConfig(
        name=name,
        camel=camel,
        description=description,
        commands=commands,
    )

    assert config.name == name
    assert config.camel == camel
    assert config.description == description
    assert config.commands == commands

    # Verify the named tuple's fields
    assert config._fields == ('name', 'camel', 'description', 'commands')

    # Verify _asdict conversion
    expected_dict = {
        'name': name,
        'camel': camel,
        'description': description,
        'commands': commands,
    }
    assert config._asdict() == expected_dict

    # Verify immutability
    try:
        config.name = 'new_name'  # type: ignore[misc]
        raised = False
    except AttributeError:
        raised = True
    assert raised is True

    # Verify equality between instances with identical values
    other = SetupCfgCommandConfig(name, camel, description, commands)
    assert config == other

    # Verify empty commands tuple is allowed
    config = SetupCfgCommandConfig(name, camel, description, ())
    assert config.commands == ()

# Generated at 2026-11-01 19:24:00.514621
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile

    # Standard usage with a proper setup.cfg
    with tempfile.TemporaryDirectory() as tmp_dir:
        with open(os.path.join(tmp_dir, 'setup.py'), 'w') as f:
            f.write('')
        with open(os.path.join(tmp_dir, 'setup.cfg'), 'w') as f:
            f.write(
                '[metadata]\n'
                'name = my_pkg\n'
                '\n'
                '[setup.command.build]\n'
                'commands =\n'
                '    echo building {name}\n'
                '    echo in {setup_dir}\n'
                '\n'
                '[setup.command.run-tests]\n'
                'name = run tests\n'
                'description = Runs the tests for {name}.\n'
                'commands =\n'
                '    pytest\n'
            )

        results = list(module_0.each_sub_command_config(tmp_dir))

        assert len(results) == 2

        build = results[0]
        assert isinstance(build, SetupCfgCommandConfig)
        assert build.name == 'build'
        assert build.camel == 'Build'
        assert build.description == ''
        assert build.commands == (
            'echo building my_pkg',
            'echo in %s' % os.path.realpath(tmp_dir),
        )

        run_tests = results[1]
        assert isinstance(run_tests, SetupCfgCommandConfig)
        assert run_tests.name == 'run tests'
        assert run_tests.camel == 'RunTests'
        assert run_tests.description == 'Runs the tests for my_pkg.'
        assert run_tests.commands == ('pytest',)

        # A setup_commands.cfg file replaces the parsed setup.cfg contents
        with open(os.path.join(tmp_dir, 'setup_commands.cfg'), 'w') as f:
            f.write(
                '[setup.command.clean]\n'
                'commands =\n'
                '    rm -rf build\n'
            )
        results = list(module_0.each_sub_command_config(tmp_dir))
        assert len(results) == 1
        clean = results[0]
        assert isinstance(clean, SetupCfgCommandConfig)
        assert clean.name == 'clean'
        assert clean.camel == 'Clean'
        assert clean.commands == ('rm -rf build',)

    # Accepts os.PathLike arguments
    with tempfile.TemporaryDirectory() as tmp_dir:
        with open(os.path.join(tmp_dir, 'setup.py'), 'w') as f:
            f.write('')
        with open(os.path.join(tmp_dir, 'setup.cfg'), 'w') as f:
            f.write('[metadata]\nname = other_pkg\n')
        results = list(each_sub_command_config.__wrapped__(tmp_dir)) \
            if hasattr(each_sub_command_config, '__wrapped__') \
            else list(module_0.each_sub_command_config(tmp_dir))
        assert results == []

    # Non-existent setup_dir raises FileNotFoundError
    bad_dir = os.path.join(tmp_dir, 'does_not_exist')
    try:
        list(module_0.each_sub_command_config(bad_dir))
    except FileNotFoundError:
        pass
    else:
        raise AssertionError('FileNotFoundError was not raised')

    # Missing setup.py raises FileNotFoundError
    with tempfile.TemporaryDirectory() as tmp_dir:
        with open(os.path.join(tmp_dir, 'setup.cfg'), 'w') as f:
            f.write('[metadata]\nname = my_pkg\n')
        try:
            list(module_0.each_sub_command_config(tmp_dir))
        except FileNotFoundError:
            pass
        else:
            raise AssertionError('FileNotFoundError was not raised')

    # Missing setup.cfg raises FileNotFoundError
    with tempfile.TemporaryDirectory() as tmp_dir:
        with open(os.path.join(tmp_dir, 'setup.py'), 'w') as f:
            f.write('')
        try:
            list(module_0.each_sub_command_config(tmp_dir))
        except FileNotFoundError:
            pass
        else:
            raise AssertionError('FileNotFoundError was not raised')

    # setup_dir pointing at a file raises NotADirectoryError
    with tempfile.TemporaryDirectory() as tmp_dir:
        file_path = os.path.join(tmp_dir, 'a_file.txt')
        with open(file_path, 'w') as f:
            f.write('')
        try:
            list(module_0.each_sub_command_config(file_path))
        except NotADirectoryError:
            pass
        else:
            raise AssertionError('NotADirectoryError was not raised')

    # Missing 'metadata' section raises LookupError
    with tempfile.TemporaryDirectory() as tmp_dir:
        with open(os.path.join(tmp_dir, 'setup.py'), 'w') as f:
            f.write('')
        with open(os.path.join(tmp_dir, 'setup.cfg'), 'w') as f:
            f.write('[bdist]\n')
        try:
            list(module_0.each_sub_command_config(tmp_dir))
        except LookupError:
            pass
        else:
            raise AssertionError('LookupError was not raised')

    # Missing 'name' option in 'metadata' section raises LookupError
    with tempfile.TemporaryDirectory() as tmp_dir:
        with open(os.path.join(tmp_dir, 'setup.py'), 'w') as f:
            f.write('')
        with open(os.path.join(tmp_dir, 'setup.cfg'), 'w') as f:
            f.write('[metadata]\nversion = 1.0\n')
        try:
            list(module_0.each_sub_command_config(tmp_dir))
        except LookupError:
            pass
        else:
            raise AssertionError('LookupError was not raised')

    # Empty 'name' option raises LookupError
    with tempfile.TemporaryDirectory() as tmp_dir:
        with open(os.path.join(tmp_dir, 'setup.py'), 'w') as f:
            f.write('')
        with open(os.path.join(tmp_dir, 'setup.cfg'), 'w') as f:
            f.write('[metadata]\nname =\n')
        try:
            list(module_0.each_sub_command_config(tmp_dir))
        except LookupError:
            pass
        else:
            raise AssertionError('LookupError was not raised')

    # Sections without commands or non-identifier names are skipped
    with tempfile.TemporaryDirectory() as tmp_dir:
        with open(os.path.join(tmp_dir, 'setup.py'), 'w') as f:
            f.write('')
        with open(os.path.join(tmp_dir, 'setup.cfg'), 'w') as f:
            f.write(
                '[metadata]\n'
                'name = my_pkg\n'
                '\n'
                '[setup.command.no_cmds]\n'
                'description = nothing here\n'
                '\n'
                '[setup.command.bad-name-section]\n'
                'commands =\n'
                '    echo hi\n'
                '\n'
                '[other.section]\n'
                'commands =\n'
                '    echo ignored\n'
            )
        results = list(module_0.each_sub_command_config(tmp_dir))
        assert results == []

# Generated at 2026-11-01 19:24:42.501596
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = tempfile.mkdtemp()
    try:
        with open(os.path.join(setup_dir, 'setup.py'), 'w') as f:
            f.write('# setup.py\n')
        with open(os.path.join(setup_dir, 'setup.cfg'), 'w') as f:
            f.write(
                '[metadata]\n'
                'name = test_package\n'
                '\n'
                '[setup.command.docs]\n'
                'description = Build docs for {name}.\n'
                'commands =\n'
                '    echo building docs\n'
                '\n'
                '    echo done\n'
                '\n'
                '[setup.command.run-tests]\n'
                'command =\n'
                '    pytest -v\n'
            )

        result = list(module_0.each_sub_command_config(setup_dir))

        assert len(result) == 2

        docs = result[0]
        assert isinstance(docs, SetupCfgCommandConfig)
        assert docs.name == 'docs'
        assert docs.camel == 'Docs'
        assert docs.description == 'Build docs for test_package.'
        assert docs.commands == ('echo building docs', 'echo done')

        run_tests = result[1]
        assert isinstance(run_tests, SetupCfgCommandConfig)
        assert run_tests.name == 'run-tests'
        assert run_tests.camel == 'RunTests'
        assert run_tests.description == ''
        assert run_tests.commands == ('pytest -v',)
    finally:
        shutil.rmtree(setup_dir)


def test_each_sub_command_config_setup_commands_cfg():
    setup_dir = tempfile.mkdtemp()
    try:
        with open(os.path.join(setup_dir, 'setup.py'), 'w') as f:
            f.write('# setup.py\n')
        with open(os.path.join(setup_dir, 'setup.cfg'), 'w') as f:
            f.write('[metadata]\nname = test_package\n')
        with open(
                os.path.join(setup_dir, 'setup_commands.cfg'), 'w'
        ) as f:
            f.write(
                '[setup.command.lint]\n'
                'name = flake8_{name}\n'
                'commands =\n'
                '    flake8 .\n'
            )

        result = list(module_0.each_sub_command_config(setup_dir))

        assert len(result) == 1
        cfg = result[0]
        assert isinstance(cfg, SetupCfgCommandConfig)
        assert cfg.name == 'flake8_test_package'
        assert cfg.camel == 'Flake8TestPackage'
        assert cfg.description == ''
        assert cfg.commands == ('flake8 .',)
    finally:
        shutil.rmtree(setup_dir)


def test_each_sub_command_config_skips_invalid_identifiers():
    setup_dir = tempfile.mkdtemp()
    try:
        with open(os.path.join(setup_dir, 'setup.py'), 'w') as f:
            f.write('# setup.py\n')
        with open(os.path.join(setup_dir, 'setup.cfg'), 'w') as f:
            f.write(
                '[metadata]\n'
                'name = test_package\n'
                '\n'
                '[setup.command.123bad]\n'
                'command = echo nope\n'
                '\n'
                '[setup.command.okay]\n'
                'command = echo yes\n'
            )

        result = list(module_0.each_sub_command_config(setup_dir))

        assert len(result) == 1
        assert result[0].name == 'okay'
        assert result[0].commands == ('echo yes',)
    finally:
        shutil.rmtree(setup_dir)

# Generated at 2026-11-01 19:26:55.208969
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as tmp_dir:
        setup_dir = Path(tmp_dir)
        (setup_dir / 'setup.py').write_text('')
        (setup_dir / 'setup.cfg').write_text(
            '[metadata]\n'
            'name = test_package\n'
            '\n'
            '[setup.command.test]\n'
            'commands =\n'
            '    echo hello\n'
            '    echo world\n'
            'description = A test command\n'
        )
        configs = list(module_0.each_sub_command_config(str(setup_dir)))
        assert len(configs) == 1
        config = configs[0]
        assert isinstance(config, SetupCfgCommandConfig)
        assert config.name == 'test'
        assert config.camel == 'Test'
        assert config.description == 'A test command'
        assert config.commands == ('echo hello', 'echo world')


def test_each_sub_command_config_with_setup_commands_cfg():
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as tmp_dir:
        setup_dir = Path(tmp_dir)
        (setup_dir / 'setup.py').write_text('')
        (setup_dir / 'setup.cfg').write_text(
            '[metadata]\n'
            'name = test_package\n'
        )
        (setup_dir / 'setup_commands.cfg').write_text(
            '[setup.command.build]\n'
            'commands =\n'
            '    echo building {name}\n'
            'name = custom build\n'
            'description = Builds the {name} package\n'
        )
        configs = list(module_0.each_sub_command_config(str(setup_dir)))
        assert len(configs) == 1
        config = configs[0]
        assert config.name == 'custom build'
        assert config.camel == 'CustomBuild'
        assert config.description == 'Builds the test_package package'
        assert config.commands == ('echo building test_package',)


def test_each_sub_command_config_missing_metadata_section():
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as tmp_dir:
        setup_dir = Path(tmp_dir)
        (setup_dir / 'setup.py').write_text('')
        (setup_dir / 'setup.cfg').write_text(
            '[other]\n'
            'name = test_package\n'
        )
        try:
            list(module_0.each_sub_command_config(str(setup_dir)))
        except LookupError as e:
            assert "missing the 'metadata' section" in str(e)
        else:
            raise AssertionError('LookupError not raised')


def test_each_sub_command_config_missing_name_option():
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as tmp_dir:
        setup_dir = Path(tmp_dir)
        (setup_dir / 'setup.py').write_text('')
        (setup_dir / 'setup.cfg').write_text(
            '[metadata]\n'
            'version = 1.0\n'
        )
        try:
            list(module_0.each_sub_command_config(str(setup_dir)))
        except LookupError as e:
            assert "missing the 'name' option" in str(e)
        else:
            raise AssertionError('LookupError not raised')


def test_each_sub_command_config_empty_name():
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as tmp_dir:
        setup_dir = Path(tmp_dir)
        (setup_dir / 'setup.py').write_text('')
        (setup_dir / 'setup.cfg').write_text(
            '[metadata]\n'
            'name =\n'
        )
        try:
            list(module_0.each_sub_command_config(str(setup_dir)))
        except LookupError as e:
            assert "'name' option is not set" in str(e)
        else:
            raise AssertionError('LookupError not raised')


def test_each_sub_command_config_no_commands():
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as tmp_dir:
        setup_dir = Path(tmp_dir)
        (setup_dir / 'setup.py').write_text('')
        (setup_dir / 'setup.cfg').write_text(
            '[metadata]\n'
            'name = test_package\n'
            '\n'
            '[setup.command.empty]\n'
            'description = No commands here\n'
        )
        configs = list(module_0.each_sub_command_config(str(setup_dir)))
        assert len(configs) == 0


def test_each_sub_command_config_invalid_setup_dir():
    try:
        list(module_0.each_sub_command_config('/nonexistent/path/that/does/not/exist'))
    except FileNotFoundError:
        pass
    else:
        raise AssertionError('FileNotFoundError not raised')


def test_each_sub_command_config_setup_dir_not_directory():
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as tmp_dir:
        file_path = Path(tmp_dir) / 'afile.txt'
        file_path.write_text('')
        try:
            list(module_0.each_sub_command_config(str(file_path)))
        except NotADirectoryError:
            pass
        else:
            raise AssertionError('NotADirectoryError not raised')


def test_each_sub_command_config_missing_setup_py():
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as tmp_dir:
        (Path(tmp_dir) / 'setup.cfg').write_text('')
        try:
            list(module_0.each_sub_command_config(tmp_dir))
        except FileNotFoundError as e:
            assert 'setup.py' in str(e)
        else:
            raise AssertionError('FileNotFoundError not raised')


def test_each_sub_command_config_missing_setup_cfg():
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as tmp_dir:
        (Path(tmp_dir) / 'setup.py').write_text('')
        try:
            list(module_0.each_sub_command_config(tmp_dir))
        except FileNotFoundError as e:
            assert 'setup.cfg' in str(e)
        else:
            raise AssertionError('FileNotFoundError not raised')


def test_each_sub_command_config_pathlike():
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as tmp_dir:
        setup_dir = Path(tmp_dir)
        (setup_dir / 'setup.py').write_text('')
        (setup_dir / 'setup.cfg').write_text(
            '[metadata]\n'
            'name = test_package\n'
            '\n'
            '[setup.command.multi.word.cmd]\n'
            'commands =\n'
            '    echo multi\n'
        )
        configs = list(module_0.each_sub_command_config(setup_dir))
        assert len(configs) == 1
        config = configs[0]
        assert config.name == 'multi.word.cmd'
        assert config.camel == 'MultiWordCmd'
        assert config.commands == ('echo multi',)

# Generated at 2026-11-01 19:28:46.218457
# Unit test for function each_sub_command_config

# Generated at 2026-11-01 19:29:03.714886
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import shutil