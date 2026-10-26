

# Generated at 2026-10-25 09:26:17.217903
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

# Generated at 2026-10-25 09:26:18.651249
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

# Generated at 2026-10-25 09:26:20.188400
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

# Generated at 2026-10-25 09:26:28.263027
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

# Generated at 2026-10-25 09:26:30.800016
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:26:33.262644
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:26:35.669795
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:26:38.086813
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:26:40.496900
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:26:42.911294
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:26:45.717343
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:26:48.134047
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:26:50.550224
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:26:54.757794
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:26:57.552593
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:27:04.120182
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:27:07.219188
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:27:10.163312
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:27:13.027841
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:27:15.633671
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:27:18.353671
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:27:20.772456
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:27:23.191592
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:27:25.607558
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:27:28.021559
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:27:30.433970
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:27:32.850973
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:27:35.481012
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:27:37.897075
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:27:40.310156
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:27:42.724704
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:27:45.469584
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:27:47.891447
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:27:50.309113
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:27:52.722771
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:27:55.137993
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:27:57.549484
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:28:00.024226
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:28:04.234426
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:28:28.597486
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:28:31.655139
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:28:54.709205
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:28:57.579179
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:28:59.995118
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:29:02.408698
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:29:06.120129
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:29:09.251566
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:29:14.170149
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:29:17.137923
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:29:20.105194
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:29:23.202021
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:29:26.951554
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:29:29.711163
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:29:32.126817
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:29:34.542431
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:29:36.955626
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:29:39.369902
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:29:41.785118
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:29:44.199825
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:29:46.939116
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:29:49.353556
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:29:51.768442
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:29:54.183761
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:29:56.598547
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:29:59.012817
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:30:01.428954
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:30:03.841719
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:30:06.255414
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:30:08.678769
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:30:11.096455
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:30:13.509282
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:30:15.922319
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:30:18.349319
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:30:20.762861
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:30:23.177475
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:30:25.590121
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:30:28.005516
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:30:30.422564
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:30:33.350076
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:30:39.362517
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:31:09.062181
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:31:12.233999
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:31:15.202624
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:31:18.075807
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:31:20.491271
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:31:23.186556
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:31:25.601455
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:31:28.014374
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:31:30.744602
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:31:33.159789
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:31:35.576973
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:31:37.989255
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:31:40.403880
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:31:42.818961
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:31:45.343027
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:31:47.757657
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:31:50.170554
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:31:52.824627
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:31:55.566736
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:31:58.341290
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:32:01.568751
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:32:04.414589
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:32:07.272932
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:32:09.836357
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:32:12.251329
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:32:14.666307
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:32:17.081372
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:32:19.495736
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:32:21.913566
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:32:24.327333
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:32:26.740611
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:32:29.153968
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:32:31.568236
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:32:33.983268
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:32:36.398397
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:32:38.813577
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:32:41.580636
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:32:43.999588
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:32:46.417666
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:32:48.835562
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:32:51.244411
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:32:53.657953
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:32:56.095960
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:32:58.511934
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:00.927990
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:03.340558
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:05.754524
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:08.467520
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:10.884225
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:13.299694
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:15.714770
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:18.128908
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:20.544341
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:22.959651
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:25.375754
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:27.793628
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:30.209566
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:32.647499
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:35.034723
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:37.447851
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:39.863408
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:42.277363
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:44.690728
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:47.106573
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:49.519807
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:51.935554
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:54.349789
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:56.767046
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:33:59.187624
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:34:01.601466
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:34:04.015956
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:34:06.428713
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:34:08.845631
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:34:11.327675
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:34:13.677445
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:34:16.094265
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:34:18.506388
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:34:22.334628
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:34:24.749041
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:34:27.164459
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:34:29.578690
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:34:31.992538
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:34:34.406594
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:34:36.821483
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:34:39.236938
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:34:41.654199
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:34:44.068017
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:34:46.480951
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:34:48.895770
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:34:51.311871
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:34:53.726161
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:34:56.141374
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:34:58.556189
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:35:00.958458
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:35:03.373193
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:35:05.786974
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:35:08.200652
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:35:10.615031
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:35:13.030098
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:35:15.447932
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:35:17.860996
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:35:20.275720
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:35:22.690177
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:35:25.108654
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:35:27.519608
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:35:29.938196
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:35:32.359392
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:35:38.954386
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:35:41.369783
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:35:43.783169
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:35:46.197052
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:35:48.611632
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:35:51.025635
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:35:53.439829
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:35:55.854728
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:35:58.267576
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:36:00.684010
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:36:03.099132
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:36:05.555270
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:36:07.970016
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:36:10.383640
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:36:12.798355
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:36:15.213793
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:36:17.628475
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 09:36:20.043040
# Unit test for function each_sub_command_config