

# Generated at 2026-10-24 20:58:20.190052
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:58:22.719717
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:58:25.246195
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:58:27.662500
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:58:30.077504
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:58:32.490758
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:58:34.908205
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:58:37.326608
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:58:39.742306
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:58:42.159818
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:58:48.465700
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():from unittest.mock import patch


# Generated at 2026-10-24 20:58:54.012258
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 20:58:55.358671
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()

    # Built-in auth types are recognized
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'nonexistent-auth' not in choices

    # A registered plugin's auth type becomes valid, then stops after removal
    plugin = AuthPlugin  # or any plugin class with `auth_type` set
    plugin.auth_type = 'test-custom'
    plugin_manager.register(plugin)
    try:
        assert 'test-custom' in choices
    finally:
        plugin_manager.unregister(plugin)
    assert 'test-custom' not in choices

# Generated at 2026-10-24 20:58:56.760841
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()

    # Built-in auth types are recognized
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'nonexistent-auth' not in choices

    # A registered plugin's auth type becomes valid, then stops after removal
    plugin = AuthPlugin  # or any plugin class with `auth_type` set
    plugin.auth_type = 'test-custom'
    plugin_manager.register(plugin)
    try:
        assert 'test-custom' in choices
    finally:
        plugin_manager.unregister(plugin)
    assert 'test-custom' not in choices

# Generated at 2026-10-24 20:59:03.010315
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 20:59:05.654397
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:59:08.078646
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:59:10.597760
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:59:13.151944
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:59:15.570610
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:59:17.991307
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:59:20.410997
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:59:22.826634
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:59:25.247882
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:59:27.669659
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:59:30.089148
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:59:32.507495
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:59:34.923612
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:59:37.342122
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:59:39.759241
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:59:42.177789
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:59:44.592524
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:59:47.010341
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:59:49.427654
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:59:51.844120
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:59:54.261385
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:59:56.678104
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 20:59:59.095531
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:00:01.512502
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:00:03.928155
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:00:06.344440
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:00:08.760279
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:00:17.562271
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-24 21:00:24.107449
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 21:00:25.445980
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()

    # Built-in auth types are recognized
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'nonexistent-auth' not in choices

    # A registered plugin's auth type becomes valid, then stops after removal
    plugin = AuthPlugin  # or any plugin class with `auth_type` set
    plugin.auth_type = 'test-custom'
    plugin_manager.register(plugin)
    try:
        assert 'test-custom' in choices
    finally:
        plugin_manager.unregister(plugin)
    assert 'test-custom' not in choices

# Generated at 2026-10-24 21:00:41.173896
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:00:46.942675
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():instance = _AuthTypeLazyChoices()
assert isinstance(instance, _AuthTypeLazyChoices)

# Generated at 2026-10-24 21:00:55.336216
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 21:00:57.981076
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:01:00.397358
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:01:02.814289
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:01:05.342127
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:01:07.760289
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:01:10.179598
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:01:13.812917
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_type = _AuthTypeLazyChoices()
    assert auth_type is not None

# Generated at 2026-10-24 21:01:15.197450
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()

    # Built-in auth types are recognized
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'nonexistent-auth' not in choices

    # A registered plugin's auth type becomes valid, then stops after removal
    plugin = AuthPlugin  # or any plugin class with `auth_type` set
    plugin.auth_type = 'test-custom'
    plugin_manager.register(plugin)
    try:
        assert 'test-custom' in choices
    finally:
        plugin_manager.unregister(plugin)
    assert 'test-custom' not in choices

# Generated at 2026-10-24 21:01:25.139353
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-24 21:01:30.053792
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 21:01:38.143778
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 21:01:39.484340
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()

    # Built-in auth types are recognized
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'nonexistent-auth' not in choices

    # A registered plugin's auth type becomes valid, then stops after removal
    plugin = AuthPlugin  # or any plugin class with `auth_type` set
    plugin.auth_type = 'test-custom'
    plugin_manager.register(plugin)
    try:
        assert 'test-custom' in choices
    finally:
        plugin_manager.unregister(plugin)
    assert 'test-custom' not in choices

# Generated at 2026-10-24 21:01:40.816362
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()

    # Built-in auth types are recognized
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'nonexistent-auth' not in choices

    # A registered plugin's auth type becomes valid, then stops after removal
    plugin = AuthPlugin  # or any plugin class with `auth_type` set
    plugin.auth_type = 'test-custom'
    plugin_manager.register(plugin)
    try:
        assert 'test-custom' in choices
    finally:
        plugin_manager.unregister(plugin)
    assert 'test-custom' not in choices

# Generated at 2026-10-24 21:01:48.895271
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:01:51.317334
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:01:53.735494
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:01:56.151616
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:01:58.568836
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:00.986314
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:03.403235
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:05.818809
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:08.237719
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:10.653465
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:13.072483
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:15.489796
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:17.905960
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:20.322104
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:22.741446
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:25.162208
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:27.578504
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:29.996774
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:32.414163
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:34.831843
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:37.247649
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:39.664964
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:42.082063
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:44.499180
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:46.917150
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:49.332874
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:51.752699
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:54.168365
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:56.585463
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:02:59.002142
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:03:01.417480
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:03:03.835366
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:03:06.251151
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:03:08.669989
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:03:11.086383
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:03:13.502649
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:03:15.919808
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:03:18.339450
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:03:20.754996
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:03:23.171431
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:03:25.588463
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:03:28.006557
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:03:31.388976
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:03:33.807270
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:03:36.222579
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:03:38.639985
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:03:41.055615
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:03:43.471815
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:03:45.889405
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:03:48.305302
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:03:50.721645
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:03:53.143514
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:03:55.562471
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:03:57.983379
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:04:00.402831
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:04:02.822706
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:04:05.237709
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:04:07.655282
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:04:10.075305
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:04:12.493466
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:04:14.910029
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:04:23.624478
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-24 21:04:29.060208
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 21:04:37.550822
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 21:04:46.203032
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_plugins = {
        'basic': object(),
        'digest': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=auth_plugins,
    ):
        choices = _AuthTypeLazyChoices()

        assert isinstance(choices, _AuthTypeLazyChoices)
        assert 'basic' in choices
        assert 'unknown' not in choices
        assert list(choices) == ['basic', 'digest']

# Generated at 2026-10-24 21:04:55.887191
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 21:05:03.330279
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 21:05:08.166927
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 21:05:15.539279
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-24 21:05:20.761690
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 21:05:28.038740
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)
    assert vars(choices) == {}

# Generated at 2026-10-24 21:05:36.941444
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-24 21:05:44.213102
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 21:05:49.435427
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 21:05:50.768730
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()

    # Built-in auth types are recognized
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'nonexistent-auth' not in choices

    # A registered plugin's auth type becomes valid, then stops after removal
    plugin = AuthPlugin  # or any plugin class with `auth_type` set
    plugin.auth_type = 'test-custom'
    plugin_manager.register(plugin)
    try:
        assert 'test-custom' in choices
    finally:
        plugin_manager.unregister(plugin)
    assert 'test-custom' not in choices

# Generated at 2026-10-24 21:06:08.487261
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 21:06:11.012790
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:06:13.536184
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:06:15.954979
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:06:18.371568
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:06:20.789698
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:06:23.206832
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:06:25.628793
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:06:31.506408
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():from unittest.mock import patch


# Generated at 2026-10-24 21:06:38.281450
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 21:06:39.714308
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()

    # Built-in auth types are recognized
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'nonexistent-auth' not in choices

    # A registered plugin's auth type becomes valid, then stops after removal
    plugin = AuthPlugin  # or any plugin class with `auth_type` set
    plugin.auth_type = 'test-custom'
    plugin_manager.register(plugin)
    try:
        assert 'test-custom' in choices
    finally:
        plugin_manager.unregister(plugin)
    assert 'test-custom' not in choices

# Generated at 2026-10-24 21:06:46.880467
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-24 21:06:54.355278
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-24 21:06:56.877613
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:06:59.295715
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:07:01.717368
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:07:04.252558
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:07:06.673138
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:07:09.091312
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:07:27.054418
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:07:29.469840
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:07:31.885934
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:07:34.301999
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:07:36.719668
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:07:39.138550
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:07:41.556686
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:07:43.974511
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:07:51.103720
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():from unittest.mock import patch


# Generated at 2026-10-24 21:07:52.433695
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()

    # Built-in auth types are recognized
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'nonexistent-auth' not in choices

    # A registered plugin's auth type becomes valid, then stops after removal
    plugin = AuthPlugin  # or any plugin class with `auth_type` set
    plugin.auth_type = 'test-custom'
    plugin_manager.register(plugin)
    try:
        assert 'test-custom' in choices
    finally:
        plugin_manager.unregister(plugin)
    assert 'test-custom' not in choices

# Generated at 2026-10-24 21:07:53.765177
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()

    # Built-in auth types are recognized
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'nonexistent-auth' not in choices

    # A registered plugin's auth type becomes valid, then stops after removal
    plugin = AuthPlugin  # or any plugin class with `auth_type` set
    plugin.auth_type = 'test-custom'
    plugin_manager.register(plugin)
    try:
        assert 'test-custom' in choices
    finally:
        plugin_manager.unregister(plugin)
    assert 'test-custom' not in choices

# Generated at 2026-10-24 21:08:02.215928
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-24 21:08:09.723437
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)
    assert list(choices) == sorted(
        plugin_manager.get_auth_plugin_mapping().keys()
    )