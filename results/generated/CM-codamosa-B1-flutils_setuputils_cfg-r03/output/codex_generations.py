

# Generated at 2026-10-25 04:03:25.510862
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

# Generated at 2026-10-25 04:03:39.115171
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:03:56.759933
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:03:59.176780
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:04:00.579377
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

# Generated at 2026-10-25 04:04:20.182141
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as setup_dir:
        real_setup_dir = os.path.realpath(setup_dir)
        home = os.path.expanduser('~')

        with open(
            os.path.join(setup_dir, 'setup.py'),
            'w',
            encoding='utf-8',
        ) as file:
            file.write('')

        with open(
            os.path.join(setup_dir, 'setup.cfg'),
            'w',
            encoding='utf-8',
        ) as file:
            file.write(
                '[metadata]\n'
                'name = demo-project\n'
                '\n'
                '[setup.command.quality-check]\n'
                'name = {name}.verify\n'
                'description = Verify {name} in {setup_dir}\n'
                'command = echo {home}\n'
                'commands =\n'
                '    python {setup_dir}/tools/check.py\n'
                '\n'
                '    python -m pytest\n'
                '\n'
                '[setup.command.invalid]\n'
                'name = not a valid command\n'
                'command = ignored\n'
                '\n'
                '[unrelated]\n'
                'command = ignored\n'
            )

        result = list(module_0.each_sub_command_config(setup_dir))

        assert result == [
            SetupCfgCommandConfig(
                name='demo-project.verify',
                camel='DemoProjectVerify',
                description=(
                    f'Verify demo-project in {real_setup_dir}'
                ),
                commands=(
                    f'echo {home}',
                    f'python {real_setup_dir}/tools/check.py',
                    'python -m pytest',
                ),
            )
        ]

        # A setup_commands.cfg file should replace command definitions
        # from setup.cfg while still using setup.cfg metadata.
        with open(
            os.path.join(setup_dir, 'setup_commands.cfg'),
            'w',
            encoding='utf-8',
        ) as file:
            file.write(
                '[setup.command.release]\n'
                'description = Release {name}\n'
                'command = python {setup_dir}/release.py\n'
            )

        result = list(module_0.each_sub_command_config(setup_dir))

        assert result == [
            SetupCfgCommandConfig(
                name='release',
                camel='Release',
                description='Release demo-project',
                commands=(
                    f'python {real_setup_dir}/release.py',
                ),
            )
        ]

# Generated at 2026-10-25 04:04:37.876639
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:04:40.426973
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:04:42.958003
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-25 04:04:45.372788
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-25 04:04:47.791002
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-25 04:04:50.202340
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:04:52.617526
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:04:55.032951
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:04:57.624497
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:05:00.040234
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:05:02.464532
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:05:04.878058
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:05:07.301570
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:05:09.717868
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:05:12.134200
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:05:22.538134
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-25 04:05:37.694244
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:05:55.492895
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:05:58.077854
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:00.493315
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:02.907302
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:05.322010
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:07.739161
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:10.155908
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:12.570770
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:14.982836
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:17.398695
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:19.823778
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:22.237061
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:24.653469
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:27.073674
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:29.491139
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:31.912300
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:34.329550
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:36.745274
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:39.163102
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:41.579822
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:43.994612
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:46.408722
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:48.825067
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:51.239316
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:53.653963
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:56.069020
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:06:58.485421
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:00.899189
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:03.314445
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:05.740374
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:08.165780
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:10.580639
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:13.006881
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:15.429084
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:17.846186
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:20.261167
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:22.676345
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:25.091148
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:27.506804
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:29.925210
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:32.342090
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:34.755895
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:37.171894
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:39.588313
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:42.008969
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:44.428563
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:46.851104
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:49.271714
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:51.686923
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:54.104570
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:56.522870
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:07:58.940956
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:08:01.373228
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:08:03.805357
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:08:06.222489
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:08:08.637310
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:08:11.051430
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:08:13.468082
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:08:15.883552
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:08:18.298462
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:08:20.712351
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:08:48.773781
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 04:08:59.988216
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:09:24.819120
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-25 04:09:43.364936
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:10:01.051005
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:10:03.470586
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:10:06.064829
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:10:08.479393
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:10:10.897977
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:10:13.312634
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:10:15.730691
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:10:18.145150
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:10:20.564202
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:10:22.978309
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:10:34.026712
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 04:10:52.169534
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with TemporaryDirectory() as setup_dir:
        setup_cfg_path = os.path.join(setup_dir, 'setup.cfg')
        setup_commands_cfg_path = os.path.join(
            setup_dir, 'setup_commands.cfg'
        )

        # Required by _validate_setup_dir().
        with open(os.path.join(setup_dir, 'setup.py'), 'w') as f:
            f.write('')

        with open(setup_cfg_path, 'w') as f:
            f.write(
                '[metadata]\n'
                'name = demo_project\n'
                '\n'
                '[setup.command.ignored]\n'
                'command = this-command-is-overridden\n'
            )

        with open(setup_commands_cfg_path, 'w') as f:
            f.write(
                '[setup.command.lint-code]\n'
                'name = {name}.quality-check\n'
                'description = Check {name} in {setup_dir}\n'
                'command = python -m ruff check {setup_dir}\n'
                'commands =\n'
                '    python -m pytest {setup_dir}\n'
                '    echo {home}\n'
                '\n'
                '[setup.command.build.docs]\n'
                'description = Build documentation\n'
                'command = python -m sphinx\n'
                '\n'
                '[setup.command.not valid]\n'
                'command = this-command-has-an-invalid-name\n'
            )

        real_setup_dir = os.path.realpath(setup_dir)

        result = list(module_0.each_sub_command_config(setup_dir))

        assert result == [
            SetupCfgCommandConfig(
                name='demo_project.quality-check',
                camel='DemoProjectQualityCheck',
                description='Check demo_project in %s' % real_setup_dir,
                commands=(
                    'python -m ruff check %s' % real_setup_dir,
                    'python -m pytest %s' % real_setup_dir,
                    'echo %s' % os.path.expanduser('~'),
                ),
            ),
            SetupCfgCommandConfig(
                name='build.docs',
                camel='BuildDocs',
                description='Build documentation',
                commands=('python -m sphinx',),
            ),
        ]

# Generated at 2026-10-25 04:11:08.960779
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with TemporaryDirectory() as temp_dir:
        setup_dir = Path(temp_dir)
        real_setup_dir = str(setup_dir.resolve())

        (setup_dir / 'setup.py').write_text('', encoding='utf-8')
        (setup_dir / 'setup.cfg').write_text(
            """
[metadata]
name = example-project

[setup.command.ignored]
command = this-command-is-overridden
""".strip(),
            encoding='utf-8',
        )
        (setup_dir / 'setup_commands.cfg').write_text(
            """
[setup.command.test-suite]
name = {name}.checks
description = Run checks for {name} from {setup_dir}
command = echo preparing
commands =
    python -m pytest {setup_dir}
    echo {home}
""".strip(),
            encoding='utf-8',
        )

        with patch('os.path.expanduser', return_value='/home/tester'):
            result = list(module_0.each_sub_command_config(setup_dir))

        assert result == [
            SetupCfgCommandConfig(
                name='example-project.checks',
                camel='ExampleProjectChecks',
                description=(
                    f'Run checks for example-project from {real_setup_dir}'
                ),
                commands=(
                    'echo preparing',
                    f'python -m pytest {real_setup_dir}',
                    'echo /home/tester',
                ),
            )
        ]

# Generated at 2026-10-25 04:11:11.377803
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:11:13.795074
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:11:16.210212
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:11:18.638446
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:11:21.052950
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:11:23.768701
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:11:33.255298
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 04:11:45.927811
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as setup_dir:
        setup_dir = os.path.realpath(setup_dir)

        with open(os.path.join(setup_dir, 'setup.py'), 'w') as f:
            f.write('from setuptools import setup\nsetup()\n')

        with open(os.path.join(setup_dir, 'setup.cfg'), 'w') as f:
            f.write(
                '[metadata]\n'
                'name = example-project\n'
                '\n'
                '[setup.command.run-tests]\n'
                'description = Run tests for {name}\n'
                'commands =\n'
                '    echo {home}\n'
                '    pytest {setup_dir}\n'
            )

        result = list(module_0.each_sub_command_config(setup_dir))

        assert result == [
            SetupCfgCommandConfig(
                name='run-tests',
                camel='RunTests',
                description='Run tests for example-project',
                commands=(
                    'echo %s' % os.path.expanduser('~'),
                    'pytest %s' % setup_dir,
                ),
            )
        ]

# Generated at 2026-10-25 04:11:57.197368
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:12:14.888932
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:12:17.422984
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:12:19.841856
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:12:22.254913
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:12:24.676247
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:12:38.460948
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile


# Generated at 2026-10-25 04:12:55.461501
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:12:57.986491
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:13:00.401535
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:13:02.816027
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:13:05.232183
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:13:07.647446
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:13:10.063905
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:13:12.477650
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:13:15.075491
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:13:17.489684
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:13:19.906851
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:13:22.324477
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:13:24.742198
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:13:27.151478
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 04:13:29.568587
# Unit test for function each_sub_command_config