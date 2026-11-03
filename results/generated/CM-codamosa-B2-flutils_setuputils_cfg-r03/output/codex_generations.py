

# Generated at 2026-11-02 23:18:28.314670
# Unit test for function each_sub_command_config

# Generated at 2026-11-02 23:20:26.061532
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-11-02 23:25:23.639667
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil

    setup_dir = tempfile.mkdtemp()
    try:
        # Create setup.py
        with open(os.path.join(setup_dir, 'setup.py'), 'w') as f:
            f.write('')

        # Create setup.cfg with metadata and command sections
        setup_cfg_content = (
            '[metadata]\n'
            'name = test_project\n'
            '\n'
            '[setup.command.build]\n'
            'command = echo building {name}\n'
            'description = Build the {name} project\n'
            '\n'
            '[setup.command.test]\n'
            'commands =\n'
            '    echo test one\n'
            '    echo test two\n'
        )
        with open(os.path.join(setup_dir, 'setup.cfg'), 'w') as f:
            f.write(setup_cfg_content)

        configs = list(module_0.each_sub_command_config(setup_dir))

        assert len(configs) == 2

        build_config = configs[0]
        assert isinstance(build_config, SetupCfgCommandConfig)
        assert build_config.name == 'build'
        assert build_config.camel == 'Build'
        assert build_config.description == 'Build the test_project project'
        assert build_config.commands == ('echo building test_project',)

        test_config = configs[1]
        assert isinstance(test_config, SetupCfgCommandConfig)
        assert test_config.name == 'test'
        assert test_config.camel == 'Test'
        assert test_config.description == ''
        assert test_config.commands == ('echo test one', 'echo test two')

        # Test that setup_commands.cfg overrides setup.cfg commands
        setup_commands_cfg_content = (
            '[setup.command.deploy]\n'
            'command = echo deploying\n'
            'description = Deploy the project\n'
        )
        with open(os.path.join(setup_dir, 'setup_commands.cfg'), 'w') as f:
            f.write(setup_commands_cfg_content)

        configs = list(module_0.each_sub_command_config(setup_dir))
        assert len(configs) == 1

        deploy_config = configs[0]
        assert isinstance(deploy_config, SetupCfgCommandConfig)
        assert deploy_config.name == 'deploy'
        assert deploy_config.camel == 'Deploy'
        assert deploy_config.description == 'Deploy the project'
        assert deploy_config.commands == ('echo deploying',)
    finally:
        shutil.rmtree(setup_dir)