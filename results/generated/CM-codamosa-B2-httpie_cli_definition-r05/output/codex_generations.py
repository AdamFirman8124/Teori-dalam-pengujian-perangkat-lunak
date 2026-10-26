

# Generated at 2026-10-25 14:08:17.644456
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 14:08:27.289089
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:09:03.564498
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():from unittest.mock import patch

# Generated at 2026-10-25 14:09:12.882984
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:09:14.294354
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from httpie.cli.definition import _AuthTypeLazyChoices
    from httpie.plugins.registry import plugin_manager

    choices = _AuthTypeLazyChoices()

    # Built-in auth types must always be recognized.
    assert 'basic' in choices
    assert 'digest' in choices

    # Every registered plugin auth type must be recognized too.
    for key in plugin_manager.get_auth_plugin_mapping():
        assert key in choices

    # Unknown auth types must be rejected.
    assert 'definitely-not-an-auth-type' not in choices

# Generated at 2026-10-25 14:09:24.418733
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from unittest.mock import patch

    auth_plugins = {
        'basic': object(),
        'digest': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=auth_plugins,
    ) as get_auth_plugin_mapping:
        choices = _AuthTypeLazyChoices()

        assert 'basic' in choices
        assert 'bearer' not in choices
        assert get_auth_plugin_mapping.call_count == 2

# Generated at 2026-10-25 14:09:36.392675
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    auth_plugins = plugin_manager.get_auth_plugin_mapping()

    for auth_type in auth_plugins:
        assert choices.__contains__(auth_type) is True

    missing_auth_type = object()
    assert choices.__contains__(missing_auth_type) is False

# Generated at 2026-10-25 14:09:44.072713
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:09:45.506117
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from httpie.cli.definition import _AuthTypeLazyChoices
    from httpie.plugins.registry import plugin_manager

    choices = _AuthTypeLazyChoices()

    # Built-in auth types must always be recognized.
    assert 'basic' in choices
    assert 'digest' in choices

    # Every registered plugin auth type must be recognized too.
    for key in plugin_manager.get_auth_plugin_mapping():
        assert key in choices

    # Unknown auth types must be rejected.
    assert 'definitely-not-an-auth-type' not in choices

# Generated at 2026-10-25 14:09:46.938627
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'bearer': object(),
    }

    with mock.patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        choices = _AuthTypeLazyChoices()

        result = iter(choices)
        assert iter(result) is result  # returns an iterator
        assert list(result) == ['basic', 'bearer', 'digest']  # sorted keys
        assert list(choices) == ['basic', 'bearer', 'digest']  # re-iterable

# Generated at 2026-10-25 14:09:57.688724
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from unittest.mock import patch

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

        assert 'basic' in choices
        assert 'digest' in choices
        assert 'unknown' not in choices

# Generated at 2026-10-25 14:10:07.770037
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from unittest.mock import patch

    choices = _AuthTypeLazyChoices()
    plugin_mapping = {
        'basic': object(),
        'digest': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=plugin_mapping,
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'unknown' not in choices

    assert get_mapping.call_count == 3

# Generated at 2026-10-25 14:10:18.443661
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    auth_plugins = {
        'z-auth': object(),
        'a-auth': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=auth_plugins,
    ):
        choices = _AuthTypeLazyChoices()

        assert list(iter(choices)) == ['a-auth', 'z-auth']

# Generated at 2026-10-25 14:10:20.863805
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:10:23.413861
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:10:25.831043
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:10:27.217957
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 14:10:28.607340
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 14:10:43.505290
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 14:10:45.043832
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 14:10:57.821436
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:10:59.888882
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from httpie.cli.definition import _AuthTypeLazyChoices
    from httpie.plugins.registry import plugin_manager

    choices = _AuthTypeLazyChoices()

    # Built-in auth types must always be recognized.
    assert 'basic' in choices
    assert 'digest' in choices

    # Every registered plugin auth type must be recognized too.
    for key in plugin_manager.get_auth_plugin_mapping():
        assert key in choices

    # Unknown auth types must be rejected.
    assert 'definitely-not-an-auth-type' not in choices

# Generated at 2026-10-25 14:11:11.031354
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from unittest.mock import patch

    choices = _AuthTypeLazyChoices()
    auth_plugins = {
        'basic': object(),
        'digest': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=auth_plugins,
    ):
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'unknown' not in choices

# Generated at 2026-10-25 14:11:13.613583
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:11:16.029061
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:11:18.449131
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:11:20.867073
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:11:23.282215
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:11:25.703812
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:11:28.120280
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:11:29.468760
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-25 14:11:41.157130
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:11:47.402836
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-25 14:11:54.160354
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:12:01.975563
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-25 14:12:11.470846
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_plugins = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=auth_plugins,
    ) as get_auth_plugin_mapping:
        choices = _AuthTypeLazyChoices()

        assert 'basic' in choices
        assert 'unknown' not in choices

    assert get_auth_plugin_mapping.call_count == 2

# Generated at 2026-10-25 14:12:20.785308
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    auth_plugins = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=auth_plugins,
    ) as get_auth_plugin_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'unknown' not in choices

    assert get_auth_plugin_mapping.call_count == 3

# Generated at 2026-10-25 14:12:28.107707
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:12:50.276328
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():from unittest.mock import patch


# Generated at 2026-10-25 14:12:51.647711
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 14:12:52.992162
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 14:12:55.398074
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 14:13:06.702243
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:13:16.044638
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():from unittest.mock import patch


# Generated at 2026-10-25 14:13:25.496495
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:13:41.887105
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():from unittest.mock import patch


# Generated at 2026-10-25 14:13:54.277175
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:14:04.004945
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-25 14:14:05.438276
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 14:14:06.871378
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    # Assumes class is defined in httpie/cli/definition.py
    # alongside `plugin_manager` - adjust import if your layout differs.
    from httpie.cli.definition import _AuthTypeLazyChoices

    choices = _AuthTypeLazyChoices()

    # 1. Returns sorted keys of the current mapping.
    fake_mapping = {"digest": "DigestPlugin", "basic": "BasicPlugin", "bearer": "BearerPlugin"}
    with patch(
        "httpie.cli.definition.plugin_manager.get_auth_plugin_mapping",
        return_value=fake_mapping,
    ) as mock_get:
        result = choices.__iter__()

        # Must be an iterator, not a list.
        assert iter(result) is result
        assert list(result) == ["basic", "bearer", "digest"]
        mock_get.assert_called_once_with()

    # 2. list() protocol / multiple iterations give fresh iterators.

# Generated at 2026-10-25 14:14:17.057272
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:14:33.806561
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from httpie.cli.definition import _AuthTypeLazyChoices
    from httpie.plugins.registry import plugin_manager

    choices = _AuthTypeLazyChoices()

    # Built-in auth types must always be recognized.
    assert 'basic' in choices
    assert 'digest' in choices

    # Every registered plugin auth type must be recognized too.
    for key in plugin_manager.get_auth_plugin_mapping():
        assert key in choices

    # Unknown auth types must be rejected.
    assert 'definitely-not-an-auth-type' not in choices

# Generated at 2026-10-25 14:14:43.539630
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:14:50.086432
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-25 14:14:57.569824
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:15:20.941071
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from httpie.cli.definition import _AuthTypeLazyChoices
    from httpie.plugins.registry import plugin_manager

    choices = _AuthTypeLazyChoices()

    # Built-in auth types must always be recognized.
    assert 'basic' in choices
    assert 'digest' in choices

    # Every registered plugin auth type must be recognized too.
    for key in plugin_manager.get_auth_plugin_mapping():
        assert key in choices

    # Unknown auth types must be rejected.
    assert 'definitely-not-an-auth-type' not in choices

# Generated at 2026-10-25 14:15:23.356415
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:15:25.772428
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:15:28.187539
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:15:30.604463
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:15:33.022111
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:15:35.436444
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:15:37.850727
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:15:40.268798
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:15:42.686199
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:15:51.731303
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from unittest.mock import patch

    auth_plugins = {
        'basic': object(),
        'digest': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=auth_plugins,
    ) as get_auth_plugin_mapping:
        choices = _AuthTypeLazyChoices()

        assert 'basic' in choices
        assert 'digest' in choices
        assert 'unknown' not in choices

        assert get_auth_plugin_mapping.call_count == 3

# Generated at 2026-10-25 14:15:53.164378
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 14:15:54.598233
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 14:16:05.041253
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:16:14.360138
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-25 14:16:26.750249
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:16:33.713763
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-25 14:16:36.308089
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:16:52.557747
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-25 14:16:59.094715
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:17:04.844361
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():from unittest.mock import patch


# Generated at 2026-10-25 14:17:10.170062
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:17:15.391802
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():from unittest.mock import patch


# Generated at 2026-10-25 14:17:21.022975
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:17:22.467504
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from httpie.cli.definition import _AuthTypeLazyChoices
    from httpie.plugins.registry import plugin_manager

    choices = _AuthTypeLazyChoices()

    # Built-in auth types must always be recognized.
    assert 'basic' in choices
    assert 'digest' in choices

    # Every registered plugin auth type must be recognized too.
    for key in plugin_manager.get_auth_plugin_mapping():
        assert key in choices

    # Unknown auth types must be rejected.
    assert 'definitely-not-an-auth-type' not in choices

# Generated at 2026-10-25 14:17:23.889140
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'bearer': object(),
    }

    with mock.patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        choices = _AuthTypeLazyChoices()

        result = iter(choices)
        assert iter(result) is result  # returns an iterator
        assert list(result) == ['basic', 'bearer', 'digest']  # sorted keys
        assert list(choices) == ['basic', 'bearer', 'digest']  # re-iterable

# Generated at 2026-10-25 14:17:25.344789
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 14:17:40.275582
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 14:17:53.309682
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-25 14:18:04.449827
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 14:18:11.180598
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-25 14:18:20.685593
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'bearer': object(),
    }

    with mock.patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        choices = _AuthTypeLazyChoices()

        result = iter(choices)
        assert iter(result) is result  # returns an iterator
        assert list(result) == ['basic', 'bearer', 'digest']  # sorted keys
        assert list(choices) == ['basic', 'bearer', 'digest']  # re-iterable