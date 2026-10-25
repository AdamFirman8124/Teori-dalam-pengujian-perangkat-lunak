

# Generated at 2026-10-25 03:39:52.887142
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 03:40:16.920213
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 03:40:19.444747
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 03:40:21.859461
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 03:40:24.275070
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 03:40:26.689656
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-25 03:40:29.104313
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-25 03:40:31.518758
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-25 03:40:33.933445
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-25 03:40:36.347635
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-25 03:40:38.763764
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-25 03:40:41.183106
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 03:40:43.593269
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 03:41:08.394098
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-25 03:41:22.400096
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os
from textwrap import dedent


def test_each_sub_command_config(tmp_path):
    # _prep_setup_dir requires both files to exist.
    (tmp_path / 'setup.py').write_text('', encoding='utf-8')
    (tmp_path / 'setup.cfg').write_text(
        dedent(
            """
            [metadata]
            name = example-project

            [setup.command.should-not-be-used]
            command = ignored command
            """
        ).strip(),
        encoding='utf-8',
    )

    # When present, setup_commands.cfg supplies the command sections.
    (tmp_path / 'setup_commands.cfg').write_text(
        dedent(
            """
            [setup.command.run-tests]
            name = {name}.test-suite
            description = Run tests for {name} in {setup_dir}
            command = python -m pytest
            commands =
                echo {name}

                cd {setup_dir}
                echo {home}
            """
        ).strip(),
        encoding='utf-8',
    )

    setup_dir = os.path.realpath(str(tmp_path))

    result = list(module_0.each_sub_command_config(tmp_path))

    assert result == [
        SetupCfgCommandConfig(
            name='example-project.test-suite',
            camel='ExampleProjectTestSuite',
            description=(
                f'Run tests for example-project in {setup_dir}'
            ),
            commands=(
                'python -m pytest',
                'echo example-project',
                f'cd {setup_dir}',
                f"echo {os.path.expanduser('~')}",
            ),
        )
    ]

# Generated at 2026-10-25 03:41:39.071728
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 03:41:41.490668
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 03:41:43.906699
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 03:42:00.888589
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with TemporaryDirectory() as tmp:
        project_dir = Path(tmp).resolve()

        (project_dir / 'setup.py').write_text('', encoding='utf-8')
        (project_dir / 'setup.cfg').write_text(
            """
[metadata]
name = sample-project

[setup.command.ignored]
command = this-command-should-not-be-returned
""".strip(),
            encoding='utf-8',
        )
        (project_dir / 'setup_commands.cfg').write_text(
            """
[setup.command.quality-check]
name = {name}.verify-all
description = Check {name} in {setup_dir}
command =
    echo {name}
    cd {setup_dir}
commands =
    echo {home}
""".strip(),
            encoding='utf-8',
        )

        result = list(module_0.each_sub_command_config(project_dir))

        assert result == [
            SetupCfgCommandConfig(
                name='sample-project.verify-all',
                camel='SampleProjectVerifyAll',
                description=f'Check sample-project in {project_dir}',
                commands=(
                    'echo sample-project',
                    f'cd {project_dir}',
                    f"echo {os.path.expanduser('~')}",
                ),
            )
        ]

# Generated at 2026-10-25 03:42:27.097973
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-25 03:42:42.354284
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 03:43:09.379683
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-25 03:43:20.977802
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 03:43:47.040929
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile


# Generated at 2026-10-25 03:44:03.642941
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    from textwrap import dedent

    with tempfile.TemporaryDirectory() as setup_dir:
        setup_dir = os.path.realpath(setup_dir)

        # Both files are required by _validate_setup_dir().
        with open(os.path.join(setup_dir, 'setup.py'), 'w') as file:
            file.write('')

        with open(os.path.join(setup_dir, 'setup.cfg'), 'w') as file:
            file.write(dedent(
                """
                [metadata]
                name = demo-project
                """
            ))

        with open(
            os.path.join(setup_dir, 'setup_commands.cfg'), 'w'
        ) as file:
            file.write(dedent(
                """
                [setup.command.build-docs]
                name = docs.{name}
                description = Build documentation for {name} in {setup_dir}
                command = echo Preparing documentation
                commands =
                    python -m sphinx {setup_dir}
                    echo {home}

                [setup.command.empty]
                description = This section has no commands

                [unrelated.section]
                command = echo This section must be ignored
                """
            ))

        result = list(module_0.each_sub_command_config(setup_dir))

        assert result == [
            SetupCfgCommandConfig(
                name='docs.demo-project',
                camel='DocsDemoProject',
                description=(
                    f'Build documentation for demo-project in {setup_dir}'
                ),
                commands=(
                    'echo Preparing documentation',
                    f'python -m sphinx {setup_dir}',
                    f"echo {os.path.expanduser('~')}",
                ),
            )
        ]

# Generated at 2026-10-25 03:44:28.218415
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-25 03:44:46.514726
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 03:45:13.702814
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-25 03:45:34.971603
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    with tempfile.TemporaryDirectory() as setup_dir:
        setup_cfg_path = os.path.join(setup_dir, 'setup.cfg')
        setup_py_path = os.path.join(setup_dir, 'setup.py')

        with open(setup_py_path, 'w', encoding='utf-8') as file:
            file.write('')

        with open(setup_cfg_path, 'w', encoding='utf-8') as file:
            file.write(
                """
[metadata]
name = demo_project

[setup.command.test-unit]
name = {name}.unit-tests
description = Run tests for {name} from {setup_dir}
command = python -m pytest
commands =
    echo {home}
    echo done

[setup.command.clean-cache]
description = Clean the project cache
command = clean {setup_dir}

[setup.command.invalid]
name = not a valid command
command = this-command-should-be-ignored

[setup.command.empty]
description = This section has no commands
""".lstrip()
            )

        real_setup_dir = os.path.realpath(setup_dir)

        result = list(module_0.each_sub_command_config(setup_dir))

        assert result == [
            SetupCfgCommandConfig(
                name='demo_project.unit-tests',
                camel='DemoProjectUnitTests',
                description=(
                    f'Run tests for demo_project from {real_setup_dir}'
                ),
                commands=(
                    'python -m pytest',
                    f"echo {os.path.expanduser('~')}",
                    'echo done',
                ),
            ),
            SetupCfgCommandConfig(
                name='clean-cache',
                camel='CleanCache',
                description='Clean the project cache',
                commands=(f'clean {real_setup_dir}',),
            ),
        ]

# Generated at 2026-10-25 03:46:01.549146
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 03:46:22.979643
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as tmp_dir:
        setup_dir = Path(tmp_dir)
        setup_realpath = os.path.realpath(str(setup_dir))
        home = os.path.expanduser('~')

        # Required by _validate_setup_dir().
        (setup_dir / 'setup.py').write_text('', encoding='utf-8')

        (setup_dir / 'setup.cfg').write_text(
            """
[metadata]
name = demo-pkg

[setup.command.lint-code]
description = Lint {name}
commands =
    python -m ruff check {setup_dir}
    echo {home}

[setup.command.no-commands]
description = This section should be ignored

[unrelated]
command = ignored
""".strip(),
            encoding='utf-8',
        )

        assert list(module_0.each_sub_command_config(setup_dir)) == [
            SetupCfgCommandConfig(
                name='lint-code',
                camel='LintCode',
                description='Lint demo-pkg',
                commands=(
                    f'python -m ruff check {setup_realpath}',
                    f'echo {home}',
                ),
            )
        ]

        # When present, setup_commands.cfg supplies the command sections,
        # while metadata.name still comes from setup.cfg.
        (setup_dir / 'setup_commands.cfg').write_text(
            """
[setup.command.build-docs]
description = Build documentation for {name}
command = python -m build {setup_dir}
commands =
    echo {name}
""".strip(),
            encoding='utf-8',
        )

        assert list(module_0.each_sub_command_config(str(setup_dir))) == [
            SetupCfgCommandConfig(
                name='build-docs',
                camel='BuildDocs',
                description='Build documentation for demo-pkg',
                commands=(
                    f'python -m build {setup_realpath}',
                    'echo demo-pkg',
                ),
            )
        ]

# Generated at 2026-10-25 03:46:48.532990
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 03:46:58.765471
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 03:47:25.917069
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-25 03:47:49.376695
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os
from pathlib import Path


def test_each_sub_command_config(tmp_path: Path) -> None:
    (tmp_path / 'setup.py').write_text('', encoding='utf-8')

    # Metadata is always read from setup.cfg.
    (tmp_path / 'setup.cfg').write_text(
        '[metadata]\n'
        'name = demo-project\n'
        '\n'
        '[setup.command.from-main-config]\n'
        'command = should-not-be-returned\n',
        encoding='utf-8',
    )

    # When present, command definitions are read from setup_commands.cfg.
    (tmp_path / 'setup_commands.cfg').write_text(
        '[setup.command.build-docs]\n'
        'description = Build docs for {name} in {setup_dir}\n'
        'command = python -m build\n'
        'commands =\n'
        '    echo {name}\n'
        '    cd {setup_dir}\n'
        '\n'
        '[setup.command.release]\n'
        'name = release-{name}\n'
        'description = Release {name}\n'
        'command = echo {home}\n'
        '\n'
        '[setup.command.not valid]\n'
        'command = this-command-is-skipped\n',
        encoding='utf-8',
    )

    setup_dir = os.path.realpath(str(tmp_path))

    result = list(module_0.each_sub_command_config(tmp_path))

    assert result == [
        SetupCfgCommandConfig(
            name='build-docs',
            camel='BuildDocs',
            description=f'Build docs for demo-project in {setup_dir}',
            commands=(
                'python -m build',
                'echo demo-project',
                f'cd {setup_dir}',
            ),
        ),
        SetupCfgCommandConfig(
            name='release-demo-project',
            camel='ReleaseDemoProject',
            description='Release demo-project',
            commands=(f"echo {os.path.expanduser('~')}",),
        ),
    ]

# Generated at 2026-10-25 03:48:00.929040
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 03:48:27.602148
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-25 03:48:37.195322
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 03:49:03.343945
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os

# Generated at 2026-10-25 03:49:15.577249
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 03:49:39.943584
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import os