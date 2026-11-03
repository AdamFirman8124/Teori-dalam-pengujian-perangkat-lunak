

# Generated at 2026-11-02 07:00:09.073011
# Unit test for constructor of class SetupCfgCommandConfig
def test_SetupCfgCommandConfig():
    config = SetupCfgCommandConfig(
        name='build',
        camel='Build',
        description='Run the build command',
        commands=('python setup.py build',)
    )
    assert config.name == 'build'
    assert config.camel == 'Build'
    assert config.description == 'Run the build command'
    assert config.commands == ('python setup.py build',)

    # Ensure it behaves like a tuple
    assert len(config) == 4
    assert tuple(config) == (
        'build', 'Build', 'Run the build command',
        ('python setup.py build',)
    )
    assert config[0] == 'build'
    assert config[-1] == ('python setup.py build',)

    # Ensure equality works between instances
    config2 = SetupCfgCommandConfig(
        name='build',
        camel='Build',
        description='Run the build command',
        commands=('python setup.py build',)
    )
    assert config == config2

    # Ensure fields are exposed
    assert config._fields == ('name', 'camel', 'description', 'commands')

    # Ensure empty commands tuple is allowed
    config3 = SetupCfgCommandConfig(
        name='test',
        camel='Test',
        description='',
        commands=()
    )
    assert config3.commands == ()
    assert config3 != config

# Generated at 2026-11-02 07:02:14.735714
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import types

    with tempfile.TemporaryDirectory() as tmp_dir:
        # Create the required setup.py and setup.cfg files
        setup_py_path = os.path.join(tmp_dir, 'setup.py')
        with open(setup_py_path, 'w') as f:
            f.write('# setup.py\n')

        setup_cfg_path = os.path.join(tmp_dir, 'setup.cfg')
        setup_cfg_content = (
            '[metadata]\n'
            'name = test_package\n'
            '\n'
            '[setup.command.test]\n'
            'commands =\n'
            '    echo hello\n'
            '    echo world\n'
        )
        with open(setup_cfg_path, 'w') as f:
            f.write(setup_cfg_content)

        # Test with explicit setup_dir
        gen = module_0.each_sub_command_config(tmp_dir)
        assert isinstance(gen, types.GeneratorType)
        results = list(gen)

        assert len(results) == 1
        config = results[0]
        assert isinstance(config, SetupCfgCommandConfig)
        assert config.name == 'test'
        assert config.camel == 'Test'
        assert config.description == ''
        assert config.commands == ('echo hello', 'echo world')

        # Test with PathLike setup_dir
        results = list(module_0.each_sub_command_config(os.PathLike(tmp_dir)))
        assert len(results) == 1

        # Test with format kwargs in commands
        setup_cfg_content = (
            '[metadata]\n'
            'name = test_package\n'
            '\n'
            '[setup.command.build]\n'
            'name = {name}-build\n'
            'description = Build the {name} package in {setup_dir}\n'
            'commands =\n'
            '    echo building from {setup_dir}\n'
            '    echo home is {home}\n'
        )
        with open(setup_cfg_path, 'w') as f:
            f.write(setup_cfg_content)

        results = list(module_0.each_sub_command_config(tmp_dir))
        assert len(results) == 1
        config = results[0]
        assert config.name == 'test_package-build'
        assert config.camel == 'TestPackageBuild'
        assert config.description == (
            'Build the test_package package in %s' % os.path.realpath(tmp_dir)
        )
        assert config.commands == (
            'echo building from %s' % os.path.realpath(tmp_dir),
            'echo home is %s' % os.path.expanduser('~')
        )

        # Test with setup_commands.cfg override
        setup_commands_cfg_path = os.path.join(tmp_dir, 'setup_commands.cfg')
        setup_commands_cfg_content = (
            '[setup.command.custom-cmd]\n'
            'description = A custom command\n'
            'commands =\n'
            '    echo custom\n'
        )
        with open(setup_commands_cfg_path, 'w') as f:
            f.write(setup_commands_cfg_content)

        results = list(module_0.each_sub_command_config(tmp_dir))
        assert len(results) == 1
        config = results[0]
        assert config.name == 'custom-cmd'
        assert config.camel == 'CustomCmd'
        assert config.description == 'A custom command'
        assert config.commands == ('echo custom',)

        os.remove(setup_commands_cfg_path)

        # Test missing setup.py
        os.remove(setup_py_path)
        try:
            list(module_0.each_sub_command_config(tmp_dir))
            assert False, 'Expected FileNotFoundError'
        except FileNotFoundError as e:
            assert 'does NOT contain a setup.py file' in str(e)

        # Restore setup.py, remove setup.cfg
        with open(setup_py_path, 'w') as f:
            f.write('# setup.py\n')
        os.remove(setup_cfg_path)
        try:
            list(module_0.each_sub_command_config(tmp_dir))
            assert False, 'Expected FileNotFoundError'
        except FileNotFoundError as e:
            assert 'does NOT contain a setup.cfg file' in str(e)

        # Test setup_dir does not exist
        try:
            list(module_0.each_sub_command_config(os.path.join(tmp_dir, 'nonexistent')))
            assert False, 'Expected FileNotFoundError'
        except FileNotFoundError as e:
            assert 'does NOT exist' in str(e)

        # Test setup_dir is not a directory
        try:
            list(module_0.each_sub_command_config(setup_py_path))
            assert False, 'Expected NotADirectoryError'
        except NotADirectoryError as e:
            assert 'is NOT a directory' in str(e)

        # Test missing metadata section
        with open(setup_cfg_path, 'w') as f:
            f.write('[other]\nname = foo\n')
        try:
            list(module_0.each_sub_command_config(tmp_dir))
            assert False, 'Expected LookupError'
        except LookupError as e:
            assert "is missing the 'metadata' section" in str(e)

        # Test missing name option
        with open(setup_cfg_path, 'w') as f:
            f.write('[metadata]\nversion = 1.0\n')
        try:
            list(module_0.each_sub_command_config(tmp_dir))
            assert False, 'Expected LookupError'
        except LookupError as e:
            assert "is missing the 'name' option" in str(e)

        # Test empty name option
        with open(setup_cfg_path, 'w') as f:
            f.write('[metadata]\nname =\n')
        try:
            list(module_0.each_sub_command_config(tmp_dir))
            assert False, 'Expected LookupError'
        except LookupError as e:
            assert "'name' option is not set" in str(e)

# Generated at 2026-11-02 07:03:09.091663
# Unit test for constructor of class SetupCfgCommandConfig
def test_SetupCfgCommandConfig():
    obj = SetupCfgCommandConfig(
        name='test',
        camel='Test',
        description='a test description',
        commands=('a', 'b')
    )
    assert obj.name == 'test'
    assert obj.camel == 'Test'
    assert obj.description == 'a test description'
    assert obj.commands == ('a', 'b')
    assert obj._fields == ('name', 'camel', 'description', 'commands')

# Generated at 2026-11-02 07:04:31.225332
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    setup_dir = tempfile.mkdtemp()
    try:
        # setup.py missing -> FileNotFoundError
        with pytest.raises(FileNotFoundError):
            list(module_0.each_sub_command_config(setup_dir))

        # setup.cfg missing -> FileNotFoundError
        open(os.path.join(setup_dir, 'setup.py'), 'w').close()
        with pytest.raises(FileNotFoundError):
            list(module_0.each_sub_command_config(setup_dir))

        # 'metadata' section missing -> LookupError
        with open(os.path.join(setup_dir, 'setup.cfg'), 'w') as f:
            f.write('[options]\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(setup_dir))

        # 'name' option missing -> LookupError
        with open(os.path.join(setup_dir, 'setup.cfg'), 'w') as f:
            f.write('[metadata]\nversion = 1.0.0\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(setup_dir))

        # 'name' option empty -> LookupError
        with open(os.path.join(setup_dir, 'setup.cfg'), 'w') as f:
            f.write('[metadata]\nname =\n')
        with pytest.raises(LookupError):
            list(module_0.each_sub_command_config(setup_dir))

        # valid, but no command sections -> empty generator
        with open(os.path.join(setup_dir, 'setup.cfg'), 'w') as f:
            f.write('[metadata]\nname = test_package\n')
        assert list(module_0.each_sub_command_config(setup_dir)) == []

        # command sections present
        with open(os.path.join(setup_dir, 'setup.cfg'), 'w') as f:
            f.write(
                '[metadata]\n'
                'name = test_package\n'
                '\n'
                '[setup.command.build]\n'
                'command =\n'
                '    python -m build\n'
                '\n'
                '[setup.command.test]\n'
                'name = run-tests\n'
                'description = Run tests for {name}.\n'
                'commands =\n'
                '    pytest\n'
                '    flake8\n'
            )
        result = list(module_0.each_sub_command_config(setup_dir))
        assert len(result) == 2
        assert all(isinstance(x, SetupCfgCommandConfig) for x in result)
        assert result[0] == SetupCfgCommandConfig(
            'build', 'Build', '', ('python -m build',)
        )
        assert result[1] == SetupCfgCommandConfig(
            'run-tests',
            'RunTests',
            'Run tests for test_package.',
            ('pytest', 'flake8'),
        )

        # setup_commands.cfg overrides setup.cfg commands
        with open(os.path.join(setup_dir, 'setup_commands.cfg'), 'w') as f:
            f.write(
                '[setup.command.build-docs]\n'
                'command =\n'
                '    sphinx-build docs docs/_build/html\n'
            )
        result = list(module_0.each_sub_command_config(setup_dir))
        assert result == [
            SetupCfgCommandConfig(
                'build-docs',
                'BuildDocs',
                '',
                ('sphinx-build docs docs/_build/html',),
            )
        ]
        os.remove(os.path.join(setup_dir, 'setup_commands.cfg'))
    finally:
        shutil.rmtree(setup_dir)

    # setup_dir does not exist -> FileNotFoundError
    with pytest.raises(FileNotFoundError):
        list(module_0.each_sub_command_config(os.path.join('path', 'does', 'not', 'exist')))

    # setup_dir is a file -> NotADirectoryError
    fd, path = tempfile.mkstemp()
    os.close(fd)
    try:
        with pytest.raises(NotADirectoryError):
            list(module_0.each_sub_command_config(path))
    finally:
        os.remove(path)

    # os.PathLike input is accepted
    setup_dir = tempfile.mkdtemp()
    try:
        open(os.path.join(setup_dir, 'setup.py'), 'w').close()
        with open(os.path.join(setup_dir, 'setup.cfg'), 'w') as f:
            f.write('[metadata]\nname = test_package\n')
        assert list(module_0.each_sub_command_config(pathlib.Path(setup_dir))) == []
        # realpath is returned
        assert list(module_0.each_sub_command_config(
            os.path.join(setup_dir, 'nested', '..')
        )) == []
    finally:
        shutil.rmtree(setup_dir)

# Generated at 2026-11-02 07:09:29.959922
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil

    setup_dir = tempfile.mkdtemp()
    try:
        with open(os.path.join(setup_dir, 'setup.py'), 'w') as f:
            f.write('# setup.py\n')

        setup_cfg_path = os.path.join(setup_dir, 'setup.cfg')
        with open(setup_cfg_path, 'w') as f:
            f.write(
                '[metadata]\n'
                'name = test_project\n'
                '\n'
                '[setup.command.build]\n'
                'description = Build the project\n'
                'commands =\n'
                '    python setup.py build\n'
                '    python setup.py bdist_wheel\n'
                '\n'
                '[setup.command.test]\n'
                'name = test\n'
                'description = Run tests\n'
                'command =\n'
                '    python -m pytest tests/\n'
            )

        configs = list(module_0.each_sub_command_config(setup_dir))

        assert len(configs) == 2

        build_config = configs[0]
        assert build_config.name == 'build'
        assert build_config.camel == 'Build'
        assert build_config.description == 'Build the project'
        assert build_config.commands == (
            'python setup.py build',
            'python setup.py bdist_wheel',
        )

        test_config = configs[1]
        assert test_config.name == 'test'
        assert test_config.camel == 'Test'
        assert test_config.description == 'Run tests'
        assert test_config.commands == ('python -m pytest tests/',)
    finally:
        shutil.rmtree(setup_dir)