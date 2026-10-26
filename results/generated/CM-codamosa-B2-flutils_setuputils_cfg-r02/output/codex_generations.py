

# Generated at 2026-10-25 11:46:44.883124
# Unit test for constructor of class SetupCfgCommandConfig
def test_SetupCfgCommandConfig():
    config = SetupCfgCommandConfig(
        name='build',
        camel='Build',
        description='Builds the project.',
        commands=('python setup.py build', 'python setup.py bdist_wheel')
    )

    # Verify each field is stored and typed correctly
    assert config.name == 'build'
    assert config.camel == 'Build'
    assert config.description == 'Builds the project.'
    assert config.commands == ('python setup.py build', 'python setup.py bdist_wheel')

    # NamedTuple behavior: immutable and tuple-compatible
    assert tuple(config) == (
        'build',
        'Build',
        'Builds the project.',
        ('python setup.py build', 'python setup.py bdist_wheel')
    )
    assert config._fields == ('name', 'camel', 'description', 'commands')

    try:
        config.name = 'other'  # type: ignore[misc]
        raise AssertionError('SetupCfgCommandConfig should be immutable')
    except AttributeError:
        pass

# Generated at 2026-10-25 11:46:47.299165
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-25 11:46:49.715493
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-25 11:46:52.132332
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-25 11:46:54.546787
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:46:56.959772
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:46:59.613308
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:47:02.028456
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:47:04.442729
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:47:07.445649
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 11:47:08.893555
# Unit test for constructor of class SetupCfgCommandConfig
def test_SetupCfgCommandConfig():
    config = SetupCfgCommandConfig(
        name='build',
        camel='Build',
        description='Builds the project.',
        commands=('python setup.py build', 'python setup.py bdist_wheel')
    )

    # Verify each field is stored and typed correctly
    assert config.name == 'build'
    assert config.camel == 'Build'
    assert config.description == 'Builds the project.'
    assert config.commands == ('python setup.py build', 'python setup.py bdist_wheel')

    # NamedTuple behavior: immutable and tuple-compatible
    assert tuple(config) == (
        'build',
        'Build',
        'Builds the project.',
        ('python setup.py build', 'python setup.py bdist_wheel')
    )
    assert config._fields == ('name', 'camel', 'description', 'commands')

    try:
        config.name = 'other'  # type: ignore[misc]
        raise AssertionError('SetupCfgCommandConfig should be immutable')
    except AttributeError:
        pass

# Generated at 2026-10-25 11:47:36.562524
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:47:39.917910
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 11:48:01.075724
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:48:03.494297
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:48:05.911410
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:48:08.324461
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:48:10.829316
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:48:13.241417
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:48:15.685399
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:48:18.070144
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:48:20.484126
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:48:23.010909
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:48:25.419503
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:48:27.836430
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:48:30.251832
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:48:32.666614
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:48:35.080305
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:48:37.493399
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:48:40.079803
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 11:48:59.134964
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:49:01.550665
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:49:03.964821
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:49:06.381147
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:49:08.794050
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:49:11.206820
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:49:13.620893
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:49:16.036157
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:49:18.478123
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:49:20.888559
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:49:23.302849
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:49:25.716129
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:49:28.129691
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:49:30.543504
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:49:32.958589
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:49:35.373391
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:49:38.133839
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:49:40.548712
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:49:42.961984
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:49:45.730062
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 11:50:17.266818
# Unit test for function each_sub_command_config
def test_each_sub_command_config():from pathlib import Path
from textwrap import dedent


def test_each_sub_command_config(tmp_path: Path) -> None:
    setup_dir = tmp_path.resolve()

    (setup_dir / 'setup.py').write_text('', encoding='utf-8')

    (setup_dir / 'setup.cfg').write_text(
        dedent(
            """
            [metadata]
            name = demo-project

            [setup.command.ignored]
            command = echo ignored
            """
        ).strip(),
        encoding='utf-8',
    )

    # When present, setup_commands.cfg supplies the command sections.
    (setup_dir / 'setup_commands.cfg').write_text(
        dedent(
            """
            [setup.command.quality.check]
            name = {name}.lint-check
            description = Run checks for {name} in {setup_dir}
            command =
                python -m compileall {setup_dir}
            commands =
                echo {home}
                echo {name}
            """
        ).strip(),
        encoding='utf-8',
    )

    result = list(module_0.each_sub_command_config(setup_dir))

    assert result == [
        SetupCfgCommandConfig(
            name='demo-project.lint-check',
            camel='DemoProjectLintCheck',
            description=f'Run checks for demo-project in {setup_dir}',
            commands=(
                f'python -m compileall {setup_dir}',
                f"echo {os.path.expanduser('~')}",
                'echo demo-project',
            ),
        )
    ]

# Generated at 2026-10-25 11:50:29.024191
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:50:31.625095
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:50:34.237104
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:50:37.037998
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:50:39.456270
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:50:42.254381
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:50:44.674462
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:50:47.085141
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:50:49.935009
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 11:50:53.023296
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:50:56.075308
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 11:51:03.585726
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:51:13.382141
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 11:51:22.905601
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:51:26.283852
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 11:51:28.896789
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:51:31.311284
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:51:33.949574
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:51:36.365001
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:51:39.131249
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:51:41.545713
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:51:43.960362
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:51:46.374977
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:51:49.124858
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:51:51.539252
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:51:53.957801
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:51:56.370879
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:51:59.172981
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:52:02.041493
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 11:52:05.419469
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:52:08.293455
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 11:52:11.345681
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:52:17.385351
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 11:52:35.284856
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:52:37.702448
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:52:40.332787
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:52:43.064960
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:52:45.479248
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:52:47.899455
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:52:50.562851
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:52:53.010180
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:52:55.391604
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:52:57.806952
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:53:00.219530
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:53:02.633758
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:53:05.048138
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:53:07.463294
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:53:09.879007
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:53:12.292942
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:53:14.706752
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:53:17.121221
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:53:19.567916
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:53:21.951259
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:53:32.442389
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 11:53:50.167302
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:53:52.581245
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:53:55.154061
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:53:57.568976
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:53:59.984188
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:54:02.400119
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:54:04.816051
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:54:07.231377
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:54:09.647480
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:54:12.062301
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:54:14.942581
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:54:17.356633
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:54:19.769966
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:54:22.187142
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:54:24.599945
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:54:27.505148
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:54:29.920217
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:54:32.335490
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:54:34.750079
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:54:37.163892
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:54:39.579717
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:54:41.995327
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:54:44.409711
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:54:46.823931
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:54:49.240283
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:54:51.654784
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:54:54.073278
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:54:56.486141
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:54:58.899319
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:55:01.314942
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:55:03.727677
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:55:06.141781
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:55:08.648322
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:55:11.062919
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:55:13.478315
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:55:15.893421
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:55:18.309312
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:55:20.723631
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:55:23.138729
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:55:25.554483
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:55:27.968077
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:55:30.391774
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:55:32.799879
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:55:35.217883
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:55:37.628855
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:55:41.720737
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:55:44.134962
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:55:46.548596
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:55:48.989395
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:55:51.405196
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:55:53.821090
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:55:56.235130
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:55:58.649917
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:56:01.069317
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:56:03.486567
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:56:05.954962
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:56:08.367737
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:56:10.782958
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:56:13.200125
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:56:15.612131
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:56:18.025637
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:56:20.440341
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:56:22.855211
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:56:25.267911
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:56:27.680442
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:56:30.093765
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:56:32.507132
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:56:34.921175
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:56:37.337903
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:56:39.750643
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:56:42.163608
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 11:56:44.581124
# Unit test for function each_sub_command_config