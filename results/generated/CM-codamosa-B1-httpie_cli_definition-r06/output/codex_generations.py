

# Generated at 2026-10-25 10:24:53.139842
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

# Generated at 2026-10-25 10:24:54.572413
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

# Generated at 2026-10-25 10:24:57.644962
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

# Generated at 2026-10-25 10:25:14.746298
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 10:25:16.216545
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()

    fake_mapping = {
        'basic': MagicMock(),
        'digest': MagicMock(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping
    ) as mock_get_mapping:
        # Present keys -> True
        assert ('basic' in choices) is True
        assert ('digest' in choices) is True

        # Absent keys -> False
        assert ('bearer' in choices) is False
        assert ('' in choices) is False
        assert ('BASIC' in choices) is False

        # Delegates to plugin_manager on each check (lazy, no caching)
        assert mock_get_mapping.call_count == 5

    # Empty mapping -> everything False
    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value={}
    ):
        assert ('basic' in choices) is False

    # Reflects updated mapping (proves laziness)
    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value={'bearer': MagicMock()}
    ):
        assert ('bearer' in choices) is True
        assert ('basic' in choices) is False

# Generated at 2026-10-25 10:25:17.567119
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

# Generated at 2026-10-25 10:25:20.166455
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:25:22.581023
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:25:24.996493
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:25:27.410993
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:25:29.825995
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:25:32.243124
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:25:34.654056
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:25:37.071121
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:25:39.486247
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:25:41.899933
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:25:44.314077
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:25:47.097126
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from httpie.plugins.registry import plugin_manager

    # Concrete setup: register a known auth plugin so the expected
    # output is deterministic.

# Generated at 2026-10-25 10:25:48.522486
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

# Generated at 2026-10-25 10:25:51.978777
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

# Generated at 2026-10-25 10:25:53.317981
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

# Generated at 2026-10-25 10:25:54.684907
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 10:25:56.118463
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

# Generated at 2026-10-25 10:25:57.658727
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 10:25:59.290927
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

# Generated at 2026-10-25 10:26:12.504500
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 10:26:13.887686
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

# Generated at 2026-10-25 10:26:15.246523
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

# Generated at 2026-10-25 10:26:16.698220
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 10:26:23.355090
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

# Generated at 2026-10-25 10:26:25.995668
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:26:28.758738
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:26:31.424476
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:26:34.088063
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:26:36.502817
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:26:38.916944
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:26:41.583197
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:26:43.997759
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:26:46.412207
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:26:48.826357
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:27:05.645736
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

# Generated at 2026-10-25 10:27:07.180799
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

# Generated at 2026-10-25 10:27:08.618379
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

# Generated at 2026-10-25 10:27:25.204507
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 10:27:27.621896
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:27:30.042967
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:27:32.655156
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:27:35.070295
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:27:37.483913
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:27:40.151895
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:27:42.820351
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:27:45.241993
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:27:47.657227
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:27:50.072114
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:28:16.303888
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

# Generated at 2026-10-25 10:28:18.865422
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

# Generated at 2026-10-25 10:28:23.507089
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

# Generated at 2026-10-25 10:28:24.904973
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 10:28:26.456695
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 10:28:31.357622
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

# Generated at 2026-10-25 10:28:32.835207
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

# Generated at 2026-10-25 10:28:37.485176
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

# Generated at 2026-10-25 10:28:53.989128
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 10:28:55.521791
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 10:29:12.090698
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()

    fake_mapping = {
        'basic': MagicMock(),
        'digest': MagicMock(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping
    ) as mock_get_mapping:
        # Present keys -> True
        assert ('basic' in choices) is True
        assert ('digest' in choices) is True

        # Absent keys -> False
        assert ('bearer' in choices) is False
        assert ('' in choices) is False
        assert ('BASIC' in choices) is False

        # Delegates to plugin_manager on each check (lazy, no caching)
        assert mock_get_mapping.call_count == 5

    # Empty mapping -> everything False
    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value={}
    ):
        assert ('basic' in choices) is False

    # Reflects updated mapping (proves laziness)
    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value={'bearer': MagicMock()}
    ):
        assert ('bearer' in choices) is True
        assert ('basic' in choices) is False

# Generated at 2026-10-25 10:29:13.545455
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

# Generated at 2026-10-25 10:29:31.877918
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 10:29:33.409142
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

# Generated at 2026-10-25 10:29:34.751502
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

# Generated at 2026-10-25 10:29:36.174515
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

# Generated at 2026-10-25 10:29:39.350321
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

# Generated at 2026-10-25 10:29:42.787349
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 10:29:44.253601
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

# Generated at 2026-10-25 10:29:46.786915
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:29:49.202366
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:29:51.931562
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:29:59.846691
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

# Generated at 2026-10-25 10:30:01.250547
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

# Generated at 2026-10-25 10:30:02.684214
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 10:30:04.233239
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

# Generated at 2026-10-25 10:30:05.972547
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

# Generated at 2026-10-25 10:30:07.390791
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

# Generated at 2026-10-25 10:30:18.568367
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

# Generated at 2026-10-25 10:30:41.507241
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 10:30:43.925766
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:30:46.339594
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:30:49.015394
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:30:51.403625
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:30:53.844826
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:30:56.236467
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:30:58.651255
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:31:01.066363
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:31:03.483331
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:31:05.897072
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:31:08.321960
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:31:10.736246
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:31:13.182787
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:31:15.599063
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:31:18.017706
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:31:22.302343
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:31:24.719906
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:31:27.305561
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:31:29.708391
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:31:32.127990
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:31:34.546343
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:31:36.964087
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:31:39.381529
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:31:53.812408
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-25 10:31:55.337588
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

# Generated at 2026-10-25 10:31:56.712434
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

# Generated at 2026-10-25 10:31:58.413551
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

# Generated at 2026-10-25 10:32:02.936936
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 10:32:04.457978
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

# Generated at 2026-10-25 10:32:05.881493
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 10:32:07.941592
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 10:32:16.710141
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:32:19.130137
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:32:22.274415
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:32:24.689955
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:32:27.394123
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:32:30.014871
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:32:32.433288
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:32:34.853419
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:32:37.264621
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:32:39.937975
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:32:42.356390
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:32:44.771904
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:32:47.186410
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:32:49.605541
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:32:52.019530
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:32:54.438987
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:32:56.855959
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:32:59.276055
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:33:01.688098
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:33:04.103084
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:33:06.521653
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:33:08.938166
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:33:11.353898
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:33:13.769863
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:33:16.183984
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:33:18.599368
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:33:21.016124
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:33:23.433818
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:33:25.848170
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:33:28.330100
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:33:38.227238
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:33:40.712218
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:33:43.068310
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:33:45.482378
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:33:47.899865
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:33:50.315297
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:33:52.728436
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:33:55.167597
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:33:57.581873
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:34:00.001065
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:34:02.418259
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:34:04.830836
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:34:07.278167
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:34:09.660675
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:34:12.078131
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:34:14.496230
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:34:16.951352
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:34:19.364441
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:34:21.779374
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:34:24.193584
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:34:26.612916
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:34:29.031041
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:34:31.445294
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:34:33.859877
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:34:36.274696
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:34:38.692190
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:34:41.110372
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:34:43.528455
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:34:45.938535
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 10:34:48.354070
# Unit test for method __iter__ of class _AuthTypeLazyChoices