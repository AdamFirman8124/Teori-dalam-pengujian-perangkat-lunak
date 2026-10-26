

# Generated at 2026-10-25 06:20:51.509060
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:20:53.919564
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:20:56.334202
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:20:58.751500
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-25 06:21:01.484171
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-25 06:21:03.857813
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-25 06:21:06.271787
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-25 06:21:08.741858
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-25 06:21:11.112604
# Unit test for constructor of class SetupCfgCommandConfig

# Generated at 2026-10-25 06:21:28.872106
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:21:44.037901
# Unit test for constructor of class SetupCfgCommandConfig
def test_SetupCfgCommandConfig():
    # positional construction
    cfg = SetupCfgCommandConfig(
        'my.command',
        'MyCommand',
        'My description',
        ('echo hi', 'ls -l'),
    )
    assert cfg.name == 'my.command'
    assert cfg.camel == 'MyCommand'
    assert cfg.description == 'My description'
    assert cfg.commands == ('echo hi', 'ls -l')

    # field access by index + tuple behaviour
    assert cfg[0] == 'my.command'
    assert cfg[1] == 'MyCommand'
    assert cfg[2] == 'My description'
    assert cfg[3] == ('echo hi', 'ls -l')
    assert len(cfg) == 4
    assert tuple(cfg) == (
        'my.command',
        'MyCommand',
        'My description',
        ('echo hi', 'ls -l'),
    )

    # keyword construction equals positional construction
    cfg_kw = SetupCfgCommandConfig(
        name='my.command',
        camel='MyCommand',
        description='My description',
        commands=('echo hi', 'ls -l'),
    )
    assert cfg_kw == cfg
    assert cfg_kw.name == cfg.name
    assert cfg_kw.camel == cfg.camel
    assert cfg_kw.description == cfg.description
    assert cfg_kw.commands == cfg.commands

    # NamedTuple metadata
    assert SetupCfgCommandConfig._fields == (
        'name', 'camel', 'description', 'commands'
    )
    assert cfg._asdict() == {
        'name': 'my.command',
        'camel': 'MyCommand',
        'description': 'My description',
        'commands': ('echo hi', 'ls -l'),
    }

    # _replace creates a new instance
    cfg2 = cfg._replace(description='Other')
    assert cfg2.description == 'Other'
    assert cfg2.name == cfg.name
    assert cfg2.camel == cfg.camel
    assert cfg2.commands == cfg.commands
    assert cfg.description == 'My description'  # original unchanged

    # immutable
    try:
        cfg.name = 'changed'  # type: ignore
    except AttributeError:
        pass
    else:
        raise AssertionError('SetupCfgCommandConfig should be immutable')

    # missing / extra args must fail
    try:
        SetupCfgCommandConfig('a', 'b', 'c')  # type: ignore
    except TypeError:
        pass
    else:
        raise AssertionError('expected TypeError for missing arg')

    try:
        SetupCfgCommandConfig('a', 'b', 'c', ('d',), 'e')  # type: ignore
    except TypeError:
        pass
    else:
        raise AssertionError('expected TypeError for extra arg')

# Generated at 2026-10-25 06:21:46.453446
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:21:48.868245
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:21:51.282599
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:21:53.696182
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:21:56.112150
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:21:59.090667
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:22:01.505321
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:22:04.290137
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:22:06.704255
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:22:09.320733
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:22:11.736453
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:22:14.150719
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:22:16.565800
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:22:18.980031
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:22:21.393924
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:22:23.808870
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:22:26.224117
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:22:28.638994
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:22:31.050676
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:22:33.464935
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:22:35.879754
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:22:38.297497
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:22:47.423040
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 06:23:05.242419
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:23:08.192291
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:23:10.835668
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:23:13.476603
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:23:16.105236
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:23:18.520236
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:23:20.945194
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:23:23.352376
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:23:25.779762
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:23:28.183635
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:23:30.601473
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:23:33.015935
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:23:35.455641
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:23:37.867241
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:23:40.281858
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:23:42.748563
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:23:45.163571
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:23:47.578418
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:23:50.016577
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:23:52.420038
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:23:54.834510
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:23:57.672275
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 06:24:00.628238
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:24:03.700422
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:24:06.670399
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:24:09.658043
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:24:12.661973
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:24:15.559915
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:24:18.325076
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:24:21.110925
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:24:23.749670
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:24:26.162476
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:24:28.713418
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:24:31.133712
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:24:33.551865
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:24:36.444440
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 06:24:39.150167
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:24:42.112546
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:24:45.286941
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:24:48.272345
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:24:51.530573
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:24:54.443440
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:24:57.117588
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:24:59.561827
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:25:01.975857
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:25:04.669465
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:25:07.083310
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:25:09.499376
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:25:11.931655
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:25:14.335360
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:25:16.751568
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:25:19.172447
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:25:21.584238
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:25:24.000049
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:25:26.658160
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:25:29.078122
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:25:31.488564
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:25:33.904657
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:25:36.320536
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:25:38.734261
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:25:41.150253
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:25:44.062393
# Unit test for function each_sub_command_config
def test_each_sub_command_config():import tempfile

# Generated at 2026-10-25 06:25:47.568871
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:25:50.410637
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:25:53.229901
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:25:56.084185
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:25:58.918347
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:26:01.881871
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:26:04.664031
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:26:07.721086
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:26:10.877812
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:26:13.211009
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:26:15.625162
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:26:18.039774
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:26:20.456222
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:26:22.868560
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:26:28.041422
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:26:30.455076
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:26:32.869585
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:26:35.300831
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:26:37.718924
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:26:40.131537
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:26:42.698909
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:26:45.052506
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:26:47.465631
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:26:49.881468
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:26:52.295077
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:26:54.710968
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:26:57.126055
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:26:59.541662
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:27:01.955326
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:27:04.368656
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:27:06.785376
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:27:09.197117
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:27:11.613100
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:27:14.029457
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:27:16.440330
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:27:18.899371
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:27:21.285717
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:27:23.701140
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:27:26.158964
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:27:28.572867
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:27:30.986024
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:27:33.399124
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:27:35.811707
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:27:38.223849
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:27:47.454823
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:27:50.718224
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:27:53.700077
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:27:56.964245
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:28:00.122807
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:28:03.125481
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:28:06.090678
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:28:09.183301
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:28:12.544528
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:28:15.556439
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:28:36.017377
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:28:38.864221
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:28:41.882315
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:28:44.561654
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:28:46.981243
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:28:49.819941
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:28:52.234673
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:28:54.648497
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:28:57.064220
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:28:59.534040
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:29:01.948675
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:29:04.362428
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:29:06.775916
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:29:09.190500
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:29:11.604740
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:29:14.017352
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:29:16.433789
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:29:18.852535
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:29:21.260128
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:29:23.679671
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:29:26.290518
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:29:29.128633
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:30:02.622053
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:30:05.596530
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:30:08.379940
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:30:11.532736
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:30:14.825760
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:30:17.694817
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:30:20.647821
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:30:23.514018
# Unit test for function each_sub_command_config
def test_each_sub_command_config():
    import tempfile
    import shutil


# Generated at 2026-10-25 06:30:26.039476
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:30:28.455496
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:30:30.873129
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:30:33.432433
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:30:35.849432
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 06:30:38.265257
# Unit test for function each_sub_command_config