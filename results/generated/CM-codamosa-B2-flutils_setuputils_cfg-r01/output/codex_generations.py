

# Generated at 2026-10-25 12:25:11.161355
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

# Generated at 2026-10-25 12:25:47.508693
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:26:04.450894
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:26:15.054428
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:26:27.138414
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

# Generated at 2026-10-25 12:27:01.750234
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:27:07.792014
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:27:10.865340
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:27:13.116935
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

# Generated at 2026-10-25 12:27:16.290264
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:27:20.900255
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:27:24.198840
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:28:01.485354
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:28:04.623449
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:28:08.830356
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:28:12.145333
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:28:21.054920
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:28:28.995358
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:28:32.169737
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:28:38.305184
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:28:44.368700
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:29:04.733925
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:29:07.153847
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:29:13.725142
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:29:18.295364
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:29:24.500368
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:29:32.078542
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:29:35.090260
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:29:39.652432
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:29:42.725864
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:29:46.001486
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:29:48.419185
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:29:50.832877
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:29:53.463064
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:29:55.875724
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:30:07.205061
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:30:10.472194
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:30:15.595535
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:30:18.665670
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:30:23.489820
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:30:28.915789
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:30:34.034231
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:30:38.736072
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:30:41.705978
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:30:51.843989
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:31:02.003846
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:31:17.239809
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:31:32.702614
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:31:52.755122
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:31:55.845714
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:31:58.505695
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:32:07.927942
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:32:15.914387
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:32:22.274753
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:32:25.643505
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:32:31.684812
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:32:35.780528
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:32:39.183604
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:33:09.255594
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:33:12.429059
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:33:15.399675
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:33:19.700970
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:33:35.902782
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:33:38.859915
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:33:43.249141
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:33:45.663331
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:33:48.076507
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:33:50.491466
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:33:52.905507
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:33:55.772028
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:33:58.187768
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:34:00.605189
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:34:03.015427
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:34:05.428235
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:34:07.841391
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:34:10.255247
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:34:12.669535
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:34:15.083872
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:34:17.497544
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:34:21.555788
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:34:25.836959
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:34:31.580518
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:34:34.466102
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:34:38.365355
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:34:44.725577
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:34:47.892760
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:34:50.851396
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:34:53.266982
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:34:58.120004
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:35:00.534681
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:35:03.248136
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:35:05.662584
# Unit test for function each_sub_command_config

# Generated at 2026-10-25 12:35:08.078191
# Unit test for function each_sub_command_config