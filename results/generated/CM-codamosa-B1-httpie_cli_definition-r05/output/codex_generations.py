

# Generated at 2026-10-24 22:02:36.253687
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

# Generated at 2026-10-24 22:02:37.630736
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

# Generated at 2026-10-24 22:02:39.062451
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

# Generated at 2026-10-24 22:02:48.484004
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:02:49.915579
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():instance = _AuthTypeLazyChoices()
assert isinstance(instance, _AuthTypeLazyChoices)

# Generated at 2026-10-24 22:02:56.360213
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 22:03:00.790304
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 22:03:05.505951
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 22:03:13.856799
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 22:03:16.397101
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:03:18.931279
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:03:21.351657
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:03:23.767216
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:03:26.185342
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:03:28.606736
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:03:31.025601
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:03:33.444163
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:03:35.864882
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:03:38.283070
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:03:40.700933
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:03:43.119709
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:03:45.538199
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:03:47.956625
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:03:50.372598
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:03:52.789661
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:03:55.205746
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:03:57.621333
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:04:00.244932
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_type = _AuthTypeLazyChoices()
    assert auth_type is not None

# Generated at 2026-10-24 22:04:07.741943
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():expected = sorted(plugin_manager.get_auth_plugin_mapping().keys())

# Generated at 2026-10-24 22:04:13.168435
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-24 22:04:14.498259
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

# Generated at 2026-10-24 22:04:17.042336
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_type = _AuthTypeLazyChoices()
    assert auth_type is not None

# Generated at 2026-10-24 22:04:26.895162
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 22:04:32.624109
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 22:04:40.783479
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-24 22:04:45.425633
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 22:04:47.846197
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:04:50.265384
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:04:52.680760
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:04:55.099908
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:04:57.515584
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:04:59.934477
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:05:02.352014
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:05:04.768915
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:05:07.186153
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:05:09.601412
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:05:12.021146
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:05:14.437983
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:05:16.851826
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:05:19.269106
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:05:21.681034
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:05:24.098963
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:05:26.514091
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:05:28.932271
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:05:31.349340
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:05:38.578499
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-24 22:05:44.612301
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 22:05:53.520927
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-24 22:05:58.231725
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 22:05:59.561712
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

# Generated at 2026-10-24 22:06:05.072422
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 22:06:06.428123
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

# Generated at 2026-10-24 22:06:08.960915
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:06:11.380659
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:06:13.800184
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:06:16.219366
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:06:18.795531
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:06:21.214695
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:06:23.634703
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:06:26.053038
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:06:28.471811
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:06:30.887872
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:06:33.304977
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:06:34.787192
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():instance = _AuthTypeLazyChoices()
assert isinstance(instance, _AuthTypeLazyChoices)

# Generated at 2026-10-24 22:06:39.908487
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 22:06:41.234976
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

# Generated at 2026-10-24 22:06:47.281269
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 22:06:48.607337
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

# Generated at 2026-10-24 22:06:49.940968
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

# Generated at 2026-10-24 22:06:57.726606
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-24 22:07:05.068252
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-24 22:07:06.413971
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

# Generated at 2026-10-24 22:07:07.745148
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

# Generated at 2026-10-24 22:07:10.273291
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:07:12.795654
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:07:15.213541
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:07:17.634140
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:07:20.050488
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:07:22.470558
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:07:25.032027
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:07:27.450407
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:07:29.867458
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:07:32.286602
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:07:34.702122
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:07:37.120318
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:07:39.537684
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:07:41.954386
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:07:44.372612
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:07:46.787944
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:07:53.717986
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 22:07:59.425083
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 22:08:08.282934
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-24 22:08:13.912797
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 22:08:15.353807
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

# Generated at 2026-10-24 22:08:22.415332
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 22:08:23.745026
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

# Generated at 2026-10-24 22:08:29.806034
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 22:08:31.223114
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

# Generated at 2026-10-24 22:08:41.355765
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:08:43.884198
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:08:46.302913
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:08:48.723919
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:08:51.141229
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:08:59.480650
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():from unittest.mock import patch


# Generated at 2026-10-24 22:09:04.502724
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 22:09:15.148647
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-24 22:09:16.559371
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

# Generated at 2026-10-24 22:09:23.342981
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:09:24.773203
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():instance = _AuthTypeLazyChoices()
assert isinstance(instance, _AuthTypeLazyChoices)

# Generated at 2026-10-24 22:09:26.112977
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

# Generated at 2026-10-24 22:09:27.483074
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

# Generated at 2026-10-24 22:09:28.811775
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

# Generated at 2026-10-24 22:09:30.200469
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

# Generated at 2026-10-24 22:09:31.533360
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

# Generated at 2026-10-24 22:09:38.700028
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 22:09:41.120135
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:09:43.540057
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:09:45.961364
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:09:59.385296
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():from unittest.mock import patch


# Generated at 2026-10-24 22:10:07.883555
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 22:10:13.319129
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 22:10:18.840272
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 22:10:25.189433
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 22:10:30.881458
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 22:10:33.302496
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:10:35.728974
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:10:38.140249
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:10:40.557943
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:10:42.979089
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:10:45.399879
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:10:47.816849
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:10:50.237314
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:10:52.655986
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:10:55.068366
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 22:11:03.386451
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 22:11:19.870724
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 22:11:25.961466
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 22:11:32.261653
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 22:11:33.597626
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

# Generated at 2026-10-24 22:11:34.925115
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

# Generated at 2026-10-24 22:11:42.553558
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 22:11:51.516129
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_plugins = {
        'digest': object(),
        'basic': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=auth_plugins,
    ) as get_auth_plugin_mapping:
        choices = _AuthTypeLazyChoices()

        # Construction should not eagerly load the plugin mapping.
        get_auth_plugin_mapping.assert_not_called()

        assert isinstance(choices, _AuthTypeLazyChoices)
        assert list(choices) == ['basic', 'digest']
        assert 'basic' in choices
        assert 'unknown' not in choices

# Generated at 2026-10-24 22:11:58.476250
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-24 22:12:06.258317
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 22:12:07.692362
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

# Generated at 2026-10-24 22:12:30.939101
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

# Generated at 2026-10-24 22:12:39.437065
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)