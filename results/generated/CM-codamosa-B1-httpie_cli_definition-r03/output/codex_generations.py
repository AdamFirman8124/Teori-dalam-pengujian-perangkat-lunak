

# Generated at 2026-10-25 07:32:42.322100
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:32:44.747821
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:32:47.173792
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:32:49.586928
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:32:52.001895
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:32:54.438459
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:32:56.852909
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:32:59.270497
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:33:01.696382
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:33:04.111994
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:33:06.597121
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:33:09.006976
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:33:10.404521
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

# Generated at 2026-10-25 07:33:11.852953
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

# Generated at 2026-10-25 07:33:13.239662
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

# Generated at 2026-10-25 07:33:14.617468
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

# Generated at 2026-10-25 07:33:16.062103
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

# Generated at 2026-10-25 07:33:17.484821
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

# Generated at 2026-10-25 07:33:18.884843
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

# Generated at 2026-10-25 07:33:20.352422
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

# Generated at 2026-10-25 07:33:21.796449
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

# Generated at 2026-10-25 07:33:23.218852
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

# Generated at 2026-10-25 07:33:24.567864
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

# Generated at 2026-10-25 07:33:25.983977
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

# Generated at 2026-10-25 07:33:27.416419
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

# Generated at 2026-10-25 07:33:28.850058
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

# Generated at 2026-10-25 07:33:30.283930
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

# Generated at 2026-10-25 07:33:31.719785
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

# Generated at 2026-10-25 07:33:33.153719
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

# Generated at 2026-10-25 07:33:34.577672
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

# Generated at 2026-10-25 07:33:36.048189
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

# Generated at 2026-10-25 07:33:37.398077
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

# Generated at 2026-10-25 07:33:40.048190
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:33:42.590146
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:33:44.964330
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:33:47.377201
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:33:49.791649
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:33:52.206334
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:33:54.623877
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:33:57.036660
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:33:59.451145
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:34:01.870862
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:34:04.281428
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:34:06.695336
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:34:09.111235
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:34:11.527453
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:34:13.943770
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:34:34.789282
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from unittest import mock

    import httpie.cli.definition as definition

    choices = definition._AuthTypeLazyChoices()
    fake_mapping = {"basic": object(), "custom-auth": object()}

    with mock.patch.object(
        definition.plugin_manager,
        "get_auth_plugin_mapping",
        return_value=fake_mapping,
    ) as mock_get_mapping:
        assert "basic" in choices
        assert "custom-auth" in choices
        assert "digest" not in choices
        assert "unknown-auth" not in choices
        assert "" not in choices
        assert None not in choices

    mock_get_mapping.assert_called()

# Generated at 2026-10-25 07:34:36.233782
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

# Generated at 2026-10-25 07:34:37.664022
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

# Generated at 2026-10-25 07:34:39.303466
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

# Generated at 2026-10-25 07:34:40.736550
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

# Generated at 2026-10-25 07:34:42.169882
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

# Generated at 2026-10-25 07:34:43.604280
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

# Generated at 2026-10-25 07:34:45.040995
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

# Generated at 2026-10-25 07:34:46.381736
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

# Generated at 2026-10-25 07:34:47.834885
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

# Generated at 2026-10-25 07:34:49.234137
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

# Generated at 2026-10-25 07:34:51.652837
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:34:54.410965
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:34:56.943398
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:34:59.358371
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:35:01.772594
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:35:04.403008
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:35:06.820785
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:35:09.234789
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:35:11.652636
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:35:14.072065
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:35:16.485681
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:35:18.899551
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:35:21.316798
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:35:23.730896
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:35:26.146588
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:35:28.563724
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:35:30.980634
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:35:33.396139
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:35:35.810454
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:35:38.228922
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:35:40.644305
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:35:43.062018
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:35:45.478990
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:35:47.893641
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:35:50.390512
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:35:52.798852
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:35:55.217321
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:35:57.630351
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:00.049553
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:02.465993
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:04.885157
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:07.377209
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:09.788192
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:12.207394
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:14.625028
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:17.037985
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:19.455162
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:21.873172
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:24.290515
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:26.709829
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:29.129383
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:31.548005
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:33.962694
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:36.379401
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:38.798656
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:41.211999
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:43.629216
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:46.047253
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:48.463403
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:50.942541
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:53.319281
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:55.736901
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:36:58.151201
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:37:00.565735
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:37:02.994628
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:37:05.412910
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:37:07.826624
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:37:10.243935
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:37:30.089151
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:37:38.004781
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from httpie.plugins.registry import plugin_manager

    # Concrete setup: register a known auth plugin so the expected
    # output is deterministic.

# Generated at 2026-10-25 07:37:40.414655
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:37:42.829121
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:37:45.415344
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:37:47.829444
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:37:50.243774
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:37:52.662456
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:37:55.078286
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:37:57.490806
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:37:59.904486
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:38:02.317622
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:38:04.732475
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:38:07.146345
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:38:09.563546
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:38:11.979610
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:38:14.395344
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:38:24.375867
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    from unittest.mock import patch

    choices = _AuthTypeLazyChoices()
    mapping = {
        'basic': object(),
        'digest': object(),
        'bearer': object(),
    }

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ) as get_auth_plugin_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' in choices
        assert 'unknown' not in choices
        assert list(choices) == ['basic', 'bearer', 'digest']
        assert get_auth_plugin_mapping.call_count == 5

# Generated at 2026-10-25 07:38:26.050080
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

# Generated at 2026-10-25 07:38:27.399075
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

# Generated at 2026-10-25 07:38:28.760711
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

# Generated at 2026-10-25 07:38:30.128782
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

# Generated at 2026-10-25 07:38:31.470844
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

# Generated at 2026-10-25 07:38:32.814872
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

# Generated at 2026-10-25 07:38:34.159034
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

# Generated at 2026-10-25 07:38:35.532325
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

# Generated at 2026-10-25 07:38:38.065031
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:38:40.478642
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:38:42.892649
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:38:45.536140
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:38:47.953515
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:38:50.367175
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:38:53.054727
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:38:55.483044
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:38:57.918553
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:39:00.346187
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:39:02.776088
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:39:05.189650
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:39:07.698729
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:39:10.115467
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:39:12.531125
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:39:14.945588
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:39:17.359731
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:39:19.776965
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:39:22.194730
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:39:24.610619
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:39:27.086865
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:39:29.501151
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:39:31.923896
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:39:44.737128
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch

# Generated at 2026-10-25 07:39:46.094233
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

# Generated at 2026-10-25 07:39:47.526583
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

# Generated at 2026-10-25 07:39:48.913126
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

# Generated at 2026-10-25 07:39:53.329856
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:39:55.743616
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:39:58.159498
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:00.573063
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:02.986813
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:05.400174
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:07.814902
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:10.228155
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:12.642191
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:15.099294
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:17.511131
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:19.924951
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:22.544538
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:24.960339
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:27.374715
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:29.789131
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:32.204266
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:34.622313
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:37.032020
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:39.446152
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:41.862764
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:44.280369
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:46.690429
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:49.099725
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:51.516151
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:53.933356
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:56.343854
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:40:58.760239
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:41:01.190015
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:41:03.602943
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:41:10.626510
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:41:13.039351
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:41:15.453512
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:41:17.903474
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:41:20.317737
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:41:22.731437
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:41:25.145302
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:41:27.559945
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:41:29.974614
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:41:32.389487
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:41:34.803546
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:41:37.233347
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:41:39.632775
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:41:42.047055
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:41:44.461218
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:41:46.875996
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:41:49.289512
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:41:51.703372
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:41:54.146312
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:41:56.563929
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:41:58.976830
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:42:01.391675
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:42:03.806774
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:42:06.221173
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:42:08.634077
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:42:11.150803
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:42:13.557616
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:42:15.969469
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:42:18.386640
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:42:20.802436
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:42:34.709654
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:42:37.127233
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:42:39.642628
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:42:42.039827
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:42:44.454666
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 07:42:46.869656
# Unit test for constructor of class _AuthTypeLazyChoices