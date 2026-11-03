

# Generated at 2026-11-02 08:36:30.933625
# Unit test for function each_sub_command_config

# Generated at 2026-11-02 08:37:32.585346
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile

    with tempfile.TemporaryDirectory() as setup_dir:
        with open(os.path.join(setup_dir, 'setup.py'), 'w') as f:
            f.write('# setup.py\n')
        with open(os.path.join(setup_dir, 'setup.cfg'), 'w') as f:
            f.write(
                '[metadata]\n'
                'name = my_pkg\n'
                '\n'
                '[setup.cfg]\n'
                'ignored = true\n'
                '\n'
                '[setup.command.test]\n'
                'command =\n'
                '    python -m pytest\n'
                'description = Run tests for {name}\n'
                '\n'
                '[setup.command.docs]\n'
                'name = build docs\n'
                'description = Build docs\n'
                'commands =\n'
                '    sphinx-build\n'
                '    {setup_dir}/make.py html\n'
            )

        result = list(module_0.each_sub_command_config(setup_dir))

        real_dir = os.path.realpath(setup_dir)
        assert result == [
            SetupCfgCommandConfig(
                'test',
                'Test',
                'Run tests for my_pkg',
                ('python -m pytest',),
            ),
            SetupCfgCommandConfig(
                'build docs',
                'BuildDocs',
                'Build docs',
                ('sphinx-build', real_dir + '/make.py html'),
            ),
        ]

# Generated at 2026-11-02 08:38:34.940277
# Unit test for constructor of class SetupCfgCommandConfig
def test_SetupCfgCommandConfig():
    # Test basic construction with all required fields
    config = SetupCfgCommandConfig(
        name='build',
        camel='Build',
        description='Build the project',
        commands=('python setup.py build', 'python setup.py bdist_wheel')
    )
    assert config.name == 'build'
    assert config.camel == 'Build'
    assert config.description == 'Build the project'
    assert config.commands == ('python setup.py build', 'python setup.py bdist_wheel')

    # Test construction with empty values
    config = SetupCfgCommandConfig(
        name='',
        camel='',
        description='',
        commands=()
    )
    assert config.name == ''
    assert config.camel == ''
    assert config.description == ''
    assert config.commands == ()

    # Test that it behaves like a tuple
    config = SetupCfgCommandConfig(
        name='test',
        camel='Test',
        description='Run tests',
        commands=('pytest',)
    )
    assert isinstance(config, tuple)
    assert len(config) == 4
    assert config[0] == 'test'
    assert config[1] == 'Test'
    assert config[2] == 'Run tests'
    assert config[3] == ('pytest',)

    # Test unpacking
    name, camel, description, commands = config
    assert name == 'test'
    assert camel == 'Test'
    assert description == 'Run tests'
    assert commands == ('pytest',)

    # Test field access via _fields and _asdict
    assert SetupCfgCommandConfig._fields == ('name', 'camel', 'description', 'commands')
    assert config._asdict() == {
        'name': 'test',
        'camel': 'Test',
        'description': 'Run tests',
        'commands': ('pytest',)
    }

    # Test _replace
    replaced = config._replace(name='lint')
    assert replaced.name == 'lint'
    assert replaced.camel == 'Test'
    assert replaced is not config

    # Test equality
    config2 = SetupCfgCommandConfig(
        name='test',
        camel='Test',
        description='Run tests',
        commands=('pytest',)
    )
    assert config == config2

    # Test that missing arguments raise TypeError
    try:
        SetupCfgCommandConfig(name='build')  # type: ignore
        assert False, "Expected TypeError"
    except TypeError:
        pass

# Generated at 2026-11-02 08:39:41.601753
# Unit test for constructor of class SetupCfgCommandConfig
def test_SetupCfgCommandConfig():
    config = SetupCfgCommandConfig(
        name='build',
        camel='build',
        description='Build the project.',
        commands=('python setup.py build', 'echo done')
    )
    assert config.name == 'build'
    assert config.camel == 'build'
    assert config.description == 'Build the project.'
    assert config.commands == ('python setup.py build', 'echo done')

    # Verify field types
    assert isinstance(config.name, str)
    assert isinstance(config.camel, str)
    assert isinstance(config.description, str)
    assert isinstance(config.commands, tuple)

    # Verify NamedTuple behavior
    assert len(config) == 4
    assert config._fields == ('name', 'camel', 'description', 'commands')

    # Verify empty commands tuple is allowed
    config = SetupCfgCommandConfig(
        name='test',
        camel='test',
        description='',
        commands=()
    )
    assert config.commands == ()

# Generated at 2026-11-02 08:40:16.534729
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with tempfile.TemporaryDirectory() as tmpdir:
        open(os.path.join(tmpdir, 'setup.py'), 'w').close()
        with open(os.path.join(tmpdir, 'setup.cfg'), 'w') as f:
            f.write(
                '[metadata]\n'
                'name = test_project\n'
                '\n'
                '[setup.command.build]\n'
                'description = Build the project.\n'
                'commands =\n'
                '    python -m build\n'
                '\n'
                '    twine check dist/*\n'
            )
        result = list(module_0.each_sub_command_config(tmpdir))
        assert result == [
            SetupCfgCommandConfig(
                name='build',
                camel='Build',
                description='Build the project.',
                commands=('python -m build', 'twine check dist/*')
            )
        ]


def test_each_sub_command_config_name_option_and_format_kwargs():
    with tempfile.TemporaryDirectory() as tmpdir:
        open(os.path.join(tmpdir, 'setup.py'), 'w').close()
        with open(os.path.join(tmpdir, 'setup.cfg'), 'w') as f:
            f.write(
                '[metadata]\n'
                'name = test_project\n'
                '\n'
                '[setup.command.build.docs]\n'
                'name = docs.{name}\n'
                'description = Docs for {name} in {setup_dir}.\n'
                'commands =\n'
                '    cd {setup_dir}\n'
                '    echo {home}\n'
                '    echo {name}\n'
            )
        result = list(module_0.each_sub_command_config(tmpdir))
        setup_dir = os.path.realpath(tmpdir)
        assert result == [
            SetupCfgCommandConfig(
                name='docs.test_project',
                camel='DocsTestProject',
                description=(
                    'Docs for test_project in %s.' % setup_dir
                ),
                commands=(
                    'cd %s' % setup_dir,
                    'echo %s' % os.path.expanduser('~'),
                    'echo test_project'
                )
            )
        ]


def test_each_sub_command_config_setup_commands_cfg_override():
    with tempfile.TemporaryDirectory() as tmpdir:
        open(os.path.join(tmpdir, 'setup.py'), 'w').close()
        with open(os.path.join(tmpdir, 'setup.cfg'), 'w') as f:
            f.write(
                '[metadata]\n'
                'name = test_project\n'
                '\n'
                '[setup.command.one]\n'
                'commands = echo one\n'
            )
        with open(os.path.join(tmpdir, 'setup_commands.cfg'), 'w') as f:
            f.write(
                '[setup.command.two]\n'
                'commands = echo two\n'
            )
        result = list(module_0.each_sub_command_config(tmpdir))
        assert result == [
            SetupCfgCommandConfig(
                name='two',
                camel='Two',
                description='',
                commands=('echo two',)
            )
        ]


def test_each_sub_command_config_no_command_sections():
    with tempfile.TemporaryDirectory() as tmpdir:
        open(os.path.join(tmpdir, 'setup.py'), 'w').close()
        with open(os.path.join(tmpdir, 'setup.cfg'), 'w') as f:
            f.write(
                '[metadata]\n'
                'name = test_project\n'
            )
        result = list(module_0.each_sub_command_config(tmpdir))
        assert result == []


def test_each_sub_command_config_invalid_command_name():
    with tempfile.TemporaryDirectory() as tmpdir:
        open(os.path.join(tmpdir, 'setup.py'), 'w').close()
        with open(os.path.join(tmpdir, 'setup.cfg'), 'w') as f:
            f.write(
                '[metadata]\n'
                'name = test_project\n'
                '\n'
                '[setup.command.1bad-name]\n'
                'commands = echo one\n'
            )
        result = list(module_0.each_sub_command_config(tmpdir))
        assert result == []


def test_each_sub_command_config_setup_dir_does_not_exist():
    with pytest.raises(FileNotFoundError):
        list(module_0.each_sub_command_config('does_not_exist_dir'))


def test_each_sub_command_config_setup_dir_not_a_directory():
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'afile.txt')
        open(path, 'w').close()
        with pytest.raises(NotADirectoryError):
            list(module_0.each_sub_command_config(path))


def test_each_sub_command_config_missing_setup_py():
    with tempfile.TemporaryDirectory() as tmpdir:
        with pytest.raises(FileNotFoundError):
            list(module_0.each_sub_command_config(tmpdir))


def test_each_sub_command_config_missing_setup_cfg():
    with tempfile.TemporaryDirectory() as tmpdir:
        open(os.path.join(tmpdir, 'setup.py'), 'w').close()
        with pytest.raises(FileNotFoundError):
            list(module_0.each_sub_command_config(tmpdir))


def test_each_sub_command_config_missing_metadata_section():
    with tempfile.TemporaryDirectory() as tmpdir:
        open(os.path.join(tmpdir, 'setup.py'), 'w').close()
        with open(os.path.join(tmpdir, 'setup.cfg'), 'w') as f:
            f.write('[options]\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(tmpdir))


def test_each_sub_command_config_missing_name_option():
    with tempfile.TemporaryDirectory() as tmpdir:
        open(os.path.join(tmpdir, 'setup.py'), 'w').close()
        with open(os.path.join(tmpdir, 'setup.cfg'), 'w') as f:
            f.write('[metadata]\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(tmpdir))


def test_each_sub_command_config_empty_name_option():
    with tempfile.TemporaryDirectory() as tmpdir:
        open(os.path.join(tmpdir, 'setup.py'), 'w').close()
        with open(os.path.join(tmpdir, 'setup.cfg'), 'w') as f:
            f.write('[metadata]\nname = \n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(tmpdir))

# Generated at 2026-11-02 08:40:43.352333
# Unit test for constructor of class SetupCfgCommandConfig
def test_SetupCfgCommandConfig():
    config = SetupCfgCommandConfig(
        name='build',
        camel='Build',
        description='Run the build command',
        commands=('python setup.py build', 'echo done')
    )

    assert config.name == 'build'
    assert config.camel == 'Build'
    assert config.description == 'Run the build command'
    assert config.commands == ('python setup.py build', 'echo done')

    # Test as a tuple
    assert len(config) == 4
    assert config[0] == 'build'
    assert config[1] == 'Build'
    assert config[2] == 'Run the build command'
    assert config[3] == ('python setup.py build', 'echo done')

    # Test equality
    config2 = SetupCfgCommandConfig(
        name='build',
        camel='Build',
        description='Run the build command',
        commands=('python setup.py build', 'echo done')
    )
    assert config == config2

    # Test _fields and _asdict
    assert config._fields == ('name', 'camel', 'description', 'commands')
    assert config._asdict() == {
        'name': 'build',
        'camel': 'Build',
        'description': 'Run the build command',
        'commands': ('python setup.py build', 'echo done')
    }

    # Test _replace
    config3 = config._replace(name='test')
    assert config3.name == 'test'
    assert config3.camel == 'Build'
    assert config3.commands == ('python setup.py build', 'echo done')

    # Test empty commands tuple
    config4 = SetupCfgCommandConfig(
        name='clean',
        camel='Clean',
        description='Clean build artifacts',
        commands=()
    )
    assert config4.commands == ()
    assert config4.name == 'clean'

# Generated at 2026-11-02 08:41:07.976868
# Unit test for function each_sub_command_config

# Generated at 2026-11-02 08:41:27.501959
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-11-02 08:43:21.359245
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import shutil