

# Generated at 2026-11-02 15:59:31.882745
# Unit test for constructor of class SetupCfgCommandConfig
def test_SetupCfgCommandConfig():
    name = 'build'
    camel = 'Build'
    description = 'Run the build command'
    commands = ('python setup.py build', 'python setup.py bdist_wheel')
    config = SetupCfgCommandConfig(name, camel, description, commands)
    assert config.name == name
    assert config.camel == camel
    assert config.description == description
    assert config.commands == commands
    assert isinstance(config, tuple)
    assert config == (name, camel, description, commands)

# Generated at 2026-11-02 16:01:10.584312
# Unit test for constructor of class SetupCfgCommandConfig
def test_SetupCfgCommandConfig():
    obj = SetupCfgCommandConfig(
        name='build',
        camel='Build',
        description='Build the project',
        commands=('python setup.py build',)
    )
    assert obj.name == 'build'
    assert obj.camel == 'Build'
    assert obj.description == 'Build the project'
    assert obj.commands == ('python setup.py build',)
    assert obj._fields == ('name', 'camel', 'description', 'commands')
    assert obj._asdict() == {
        'name': 'build',
        'camel': 'Build',
        'description': 'Build the project',
        'commands': ('python setup.py build',)
    }

# Generated at 2026-11-02 16:05:04.910905
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil

    tmp_dir = tempfile.mkdtemp()
    try:
        # Create setup.py
        with open(os.path.join(tmp_dir, 'setup.py'), 'w') as f:
            f.write('# setup.py\n')

        # Create setup.cfg
        setup_cfg_content = (
            '[metadata]\n'
            'name = test_project\n'
            '\n'
            '[setup.command.build]\n'
            'command = python setup.py build\n'
            '\n'
            '[setup.command.run_tests]\n'
            'name = Run Tests\n'
            'description = Run the test suite for {name}\n'
            'commands =\n'
            '    pytest {setup_dir}/tests/\n'
            '    flake8 {setup_dir}/\n'
        )
        with open(os.path.join(tmp_dir, 'setup.cfg'), 'w') as f:
            f.write(setup_cfg_content)

        real_dir = os.path.realpath(tmp_dir)
        configs = list(module_0.each_sub_command_config(tmp_dir))

        assert len(configs) == 2

        # Check first config
        assert configs[0].name == 'build'
        assert configs[0].camel == 'Build'
        assert configs[0].description == ''
        assert configs[0].commands == ('python setup.py build',)

        # Check second config
        assert configs[1].name == 'Run Tests'
        assert configs[1].camel == 'RunTests'
        assert configs[1].description == 'Run the test suite for test_project'
        assert configs[1].commands == (
            'pytest %s/tests/' % real_dir,
            'flake8 %s/' % real_dir,
        )
    finally:
        shutil.rmtree(tmp_dir)