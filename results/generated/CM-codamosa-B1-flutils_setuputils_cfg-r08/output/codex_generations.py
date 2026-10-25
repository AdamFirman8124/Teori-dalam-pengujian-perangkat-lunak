

# Generated at 2026-10-25 02:12:05.922087
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:12:49.432403
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 02:12:59.867902
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:13:23.435902
# Unit test for function each_sub_command_config
def test_each_sub_command_config():from pathlib import Path

# Generated at 2026-10-25 02:13:25.850327
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:13:28.396586
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:13:30.814344
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:13:33.232060
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:13:35.648006
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:13:38.062558
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:13:40.479068
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:13:42.890705
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:13:45.305377
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:13:58.972134
# Unit test for function each_sub_command_config
def test_each_sub_command_config():from tempfile import TemporaryDirectory


# Generated at 2026-10-25 02:14:15.757851
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:14:42.080497
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 02:14:44.501396
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:14:46.931379
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:14:59.072884
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 02:15:17.447682
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:15:43.924530
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 02:15:46.341841
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:15:48.756977
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:15:51.173156
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:16:01.844853
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:16:44.136795
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-25 02:17:01.032146
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:17:23.765038
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 02:17:40.194623
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:18:06.600961
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 02:18:18.204442
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:18:40.976620
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 02:18:52.066815
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile

    with tempfile.TemporaryDirectory() as setup_dir:
        setup_dir = os.path.realpath(setup_dir)

        with open(
            os.path.join(setup_dir, 'setup.py'),
            'w',
            encoding='utf-8',
        ) as setup_py:
            setup_py.write('from setuptools import setup\nsetup()\n')

        with open(
            os.path.join(setup_dir, 'setup.cfg'),
            'w',
            encoding='utf-8',
        ) as setup_cfg:
            setup_cfg.write(
                """
[metadata]
name = example-project

[setup.command.check-code]
name = {name}.check-code
description = Check {name} in {setup_dir}
command = echo checking {name}
commands =
    cd {setup_dir}
    echo {home}
""".lstrip()
            )

        actual = list(module_0.each_sub_command_config(setup_dir))

        assert actual == [
            SetupCfgCommandConfig(
                name='example-project.check-code',
                camel='ExampleProjectCheckCode',
                description='Check example-project in %s' % setup_dir,
                commands=(
                    'echo checking example-project',
                    'cd %s' % setup_dir,
                    'echo %s' % os.path.expanduser('~'),
                ),
            )
        ]

# Generated at 2026-10-25 02:18:54.484284
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:18:56.898922
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:19:23.047229
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-25 02:19:34.213297
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    from pathlib import Path
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as temp_dir:
        setup_dir = Path(temp_dir)

        (setup_dir / 'setup.py').write_text('', encoding='utf-8')
        (setup_dir / 'setup.cfg').write_text(
            '[metadata]\n'
            'name = sample_project\n',
            encoding='utf-8',
        )
        (setup_dir / 'setup_commands.cfg').write_text(
            '[setup.command.lint]\n'
            'name = {name}.lint-code\n'
            'description = Lint {name} from {setup_dir}\n'
            'commands =\n'
            '    echo Linting {name}\n'
            '    cd {setup_dir}\n'
            '\n'
            '[setup.command.release.build]\n'
            'description = Build a release for {name}\n'
            'command = python setup.py sdist\n',
            encoding='utf-8',
        )

        configs = list(module_0.each_sub_command_config(setup_dir))

        assert configs == [
            SetupCfgCommandConfig(
                name='sample_project.lint-code',
                camel='SampleProjectLintCode',
                description=(
                    f'Lint sample_project from {setup_dir.resolve()}'
                ),
                commands=(
                    'echo Linting sample_project',
                    f'cd {setup_dir.resolve()}',
                ),
            ),
            SetupCfgCommandConfig(
                name='release.build',
                camel='ReleaseBuild',
                description='Build a release for sample_project',
                commands=('python setup.py sdist',),
            ),
        ]

# Generated at 2026-10-25 02:19:59.208630
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-25 02:20:12.008522
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:20:37.816176
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-25 02:20:47.707831
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:20:50.351409
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:20:52.766231
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:20:55.181517
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:20:57.596722
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:21:00.012007
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:21:02.426579
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:21:27.804555
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 02:21:40.191916
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:21:58.104882
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 02:22:00.519654
# Unit test for function each_sub_command_config