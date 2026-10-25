

# Generated at 2026-10-24 21:35:15.920933
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)
    assert vars(choices) == {}

# Generated at 2026-10-24 21:35:24.033969
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:35:25.471420
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():instance = _AuthTypeLazyChoices()
assert isinstance(instance, _AuthTypeLazyChoices)

# Generated at 2026-10-24 21:35:28.015825
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:35:30.434494
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:35:32.853040
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:35:35.272455
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:35:37.689999
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:35:40.109738
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:35:42.531819
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:35:44.950212
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:35:47.369444
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:35:49.787440
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:35:52.208743
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:35:54.648948
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:35:57.066268
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:35:59.484946
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:36:01.902436
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:36:04.318129
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:36:06.737093
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:36:09.154410
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:36:11.572992
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:36:13.992901
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:36:16.414822
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:36:18.828486
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:36:21.248343
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:36:23.664679
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:36:31.413324
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 21:36:32.757318
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

# Generated at 2026-10-24 21:36:38.990787
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 21:36:40.328622
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

# Generated at 2026-10-24 21:36:46.262098
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)
    assert vars(choices) == {}

# Generated at 2026-10-24 21:36:50.970737
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)
    assert vars(choices) == {}

# Generated at 2026-10-24 21:36:52.357543
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

# Generated at 2026-10-24 21:36:53.684498
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

# Generated at 2026-10-24 21:37:01.012437
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-24 21:37:03.430284
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:37:05.960142
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:37:08.374039
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:37:10.792821
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:37:13.208612
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:37:15.632589
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:37:18.050383
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:37:20.472343
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:37:22.889630
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:37:25.308819
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:37:27.730278
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:37:30.162788
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:37:39.408134
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():from unittest.mock import patch


# Generated at 2026-10-24 21:37:45.394683
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 21:37:46.727790
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

# Generated at 2026-10-24 21:37:48.056216
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

# Generated at 2026-10-24 21:37:55.284613
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-24 21:37:57.706236
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:00.126380
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:02.543017
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:05.131509
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:07.547139
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:09.964632
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:12.383943
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:14.799866
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:17.220423
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:19.640137
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:22.058544
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:24.477695
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:26.892504
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:29.314056
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:31.730481
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:34.148809
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:36.566505
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:38.986846
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:41.404583
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:43.820831
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:46.242182
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:48.659369
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:51.078707
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:53.496487
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:55.913760
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:38:58.332635
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:39:00.749727
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:39:03.167984
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:39:05.586053
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:39:08.011281
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:39:15.355918
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 21:39:20.475935
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)
    assert vars(choices) == {}

# Generated at 2026-10-24 21:39:29.575385
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
    ) as get_auth_plugin_mapping:
        choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)
    assert vars(choices) == {}
    get_auth_plugin_mapping.assert_not_called()

# Generated at 2026-10-24 21:39:30.902789
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

# Generated at 2026-10-24 21:39:33.583106
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:39:36.002940
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:39:38.422211
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:39:40.841221
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:39:43.256789
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:39:45.671857
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:39:48.091037
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:39:50.506858
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:39:52.923116
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:39:55.343002
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:39:57.754121
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:40:00.169919
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:40:02.586808
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:40:05.003150
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:40:07.420794
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:40:09.836493
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:40:16.262842
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-24 21:40:17.596009
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

# Generated at 2026-10-24 21:40:18.943228
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

# Generated at 2026-10-24 21:40:25.194534
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 21:40:26.519888
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

# Generated at 2026-10-24 21:40:35.973729
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
    ) as get_auth_plugin_mapping:
        choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)
    get_auth_plugin_mapping.assert_not_called()

# Generated at 2026-10-24 21:40:38.398487
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:40:40.814730
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:40:43.234372
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:40:45.653500
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:40:48.068510
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:40:50.489330
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:40:53.044843
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:40:55.463880
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:40:57.905501
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:41:00.322600
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:41:02.743577
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:41:05.160450
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:41:07.576412
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:41:09.994377
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:41:12.410029
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:41:14.826302
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:41:17.242391
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:41:19.658935
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:41:22.075888
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:41:24.495486
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:41:31.363304
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():from unittest.mock import patch


# Generated at 2026-10-24 21:41:36.321593
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 21:41:44.143997
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:41:45.768786
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():instance = _AuthTypeLazyChoices()
assert isinstance(instance, _AuthTypeLazyChoices)

# Generated at 2026-10-24 21:41:57.046602
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-24 21:42:03.625256
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:42:06.167342
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:42:08.586247
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:42:11.003570
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:42:13.420708
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:42:15.838232
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:42:19.496748
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:42:21.913859
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:42:24.332875
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:42:32.273275
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 21:42:33.709624
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

# Generated at 2026-10-24 21:42:41.692817
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 21:42:49.021911
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)
    assert choices.__dict__ == {}

# Generated at 2026-10-24 21:43:01.558018
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-24 21:43:03.977830
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:43:06.396019
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:43:08.812088
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:43:11.231532
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:43:13.647793
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:43:16.065483
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:43:18.484188
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:43:20.900215
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:43:23.317032
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:43:25.736411
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:43:28.157055
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:43:30.571252
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:43:36.781923
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:43:39.201133
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:43:41.619797
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:43:44.038187
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:43:46.452293
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:43:48.868342
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:43:51.285222
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:43:53.701612
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:43:56.119988
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:44:03.782337
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 21:44:05.121609
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

# Generated at 2026-10-24 21:44:06.454156
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

# Generated at 2026-10-24 21:44:11.692103
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 21:44:19.178955
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 21:44:24.503276
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)
    assert choices.__dict__ == {}

# Generated at 2026-10-24 21:44:26.921916
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:44:29.344456
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:44:31.758784
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:44:42.709861
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:44:45.127333
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:44:47.705622
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:44:50.121779
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:44:52.538750
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:44:54.955623
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:44:57.384193
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:44:59.800905
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:45:01.264515
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():instance = _AuthTypeLazyChoices()
assert isinstance(instance, _AuthTypeLazyChoices)

# Generated at 2026-10-24 21:45:09.048154
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 21:45:10.469625
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():instance = _AuthTypeLazyChoices()
assert isinstance(instance, _AuthTypeLazyChoices)

# Generated at 2026-10-24 21:45:11.916153
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