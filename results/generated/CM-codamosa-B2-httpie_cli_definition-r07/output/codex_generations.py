

# Generated at 2026-10-25 09:38:07.823614
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:38:10.543457
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:38:13.146609
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:38:15.604521
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:38:18.020185
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:38:20.635295
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:38:23.050756
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:38:25.468554
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:38:27.887490
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:38:30.305954
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:38:32.717514
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:38:35.131348
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:38:37.547432
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:38:39.961679
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:38:42.377789
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:38:44.793411
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:38:47.207583
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:38:49.621823
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:38:52.037320
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:38:54.453046
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:38:56.866724
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:38:59.281510
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:39:01.697152
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:39:04.112617
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:39:05.637658
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

# Generated at 2026-10-25 09:39:07.067699
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

# Generated at 2026-10-25 09:39:08.477032
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

# Generated at 2026-10-25 09:39:09.935482
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

# Generated at 2026-10-25 09:39:11.469262
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

# Generated at 2026-10-25 09:39:12.921458
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

# Generated at 2026-10-25 09:39:15.872716
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

# Generated at 2026-10-25 09:39:17.202218
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

# Generated at 2026-10-25 09:39:33.690989
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

# Generated at 2026-10-25 09:39:36.334245
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:39:38.921424
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:39:41.457545
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:39:44.045974
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:39:46.461067
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:39:48.877952
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:39:51.291063
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:39:53.706725
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:39:56.124924
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:39:58.538819
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:40:00.956746
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:40:03.369045
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:40:05.788564
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:40:11.475315
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():instance = _AuthTypeLazyChoices()

# Generated at 2026-10-25 09:40:12.836377
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

# Generated at 2026-10-25 09:40:14.347395
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

# Generated at 2026-10-25 09:40:17.414718
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

# Generated at 2026-10-25 09:40:18.790868
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

# Generated at 2026-10-25 09:40:20.458009
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

# Generated at 2026-10-25 09:40:21.938739
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

# Generated at 2026-10-25 09:40:23.419831
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

# Generated at 2026-10-25 09:40:39.841204
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

# Generated at 2026-10-25 09:40:56.432089
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

# Generated at 2026-10-25 09:40:58.853615
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:41:01.266118
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:41:03.942516
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:41:06.356966
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:41:08.776532
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:41:11.190623
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:41:13.608559
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:41:16.020905
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:41:18.438830
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:41:31.892668
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    from unittest.mock import patch
    instance = _AuthTypeLazyChoices()
    assert isinstance(instance, _AuthTypeLazyChoices)
    fake_mapping = {'digest': object(), 'basic': object()}
    with patch.object(plugin_manager, 'get_auth_plugin_mapping', return_value=fake_mapping):
        assert 'basic' in instance
        assert 'digest' in instance
        assert 'unknown' not in instance
        assert list(iter(instance)) == ['basic', 'digest']
        assert list(instance) == sorted(fake_mapping.keys())

# Generated at 2026-10-25 09:41:33.293598
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

# Generated at 2026-10-25 09:41:50.399003
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

# Generated at 2026-10-25 09:41:51.737472
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

# Generated at 2026-10-25 09:42:16.197060
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

# Generated at 2026-10-25 09:42:35.143675
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

# Generated at 2026-10-25 09:42:36.490327
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

# Generated at 2026-10-25 09:42:37.909585
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

# Generated at 2026-10-25 09:42:39.343297
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

# Generated at 2026-10-25 09:42:41.595447
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

# Generated at 2026-10-25 09:42:43.028451
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

# Generated at 2026-10-25 09:42:44.462862
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

# Generated at 2026-10-25 09:42:45.895671
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

# Generated at 2026-10-25 09:42:47.220702
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

# Generated at 2026-10-25 09:42:51.843882
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

# Generated at 2026-10-25 09:43:15.079138
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

# Generated at 2026-10-25 09:43:17.494383
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:43:20.142338
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:43:22.558594
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:43:24.975600
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:43:27.393171
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:43:29.805965
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:43:32.221459
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:43:34.635976
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:43:37.053311
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:43:39.470339
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:43:41.884941
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:43:44.300433
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:43:46.712201
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:43:49.129689
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:43:51.544440
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:43:53.955927
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:43:56.370970
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:43:58.786070
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:01.201086
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:03.617637
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:06.102658
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:08.493122
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:10.907599
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:13.326083
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:15.742697
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:18.155377
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:20.570362
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:22.986645
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:25.403737
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:27.820671
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:30.235242
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:32.649103
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:35.065711
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:37.483046
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:39.901114
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:42.314537
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:44.732904
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:47.148283
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:49.567347
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:51.986162
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:54.400634
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:56.818083
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:44:59.230812
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:45:01.647310
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:45:04.064122
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:45:07.145392
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:45:09.560082
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:45:11.976438
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:45:14.392828
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:45:16.806661
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:45:19.220662
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:45:21.635358
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:45:24.051534
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:45:26.468578
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:45:29.025371
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

# Generated at 2026-10-25 09:45:30.374675
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

# Generated at 2026-10-25 09:45:31.754097
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

# Generated at 2026-10-25 09:45:33.883393
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

# Generated at 2026-10-25 09:45:38.499866
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

# Generated at 2026-10-25 09:45:39.865384
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

# Generated at 2026-10-25 09:45:41.307610
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

# Generated at 2026-10-25 09:45:45.198853
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

# Generated at 2026-10-25 09:45:46.633881
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

# Generated at 2026-10-25 09:46:06.394345
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

# Generated at 2026-10-25 09:46:09.055045
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:46:11.472098
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:46:13.885489
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:46:16.303526
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:46:18.716720
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:46:21.129742
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:46:23.547170
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:46:25.964875
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:46:28.381091
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:46:31.178071
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

# Generated at 2026-10-25 09:46:32.918459
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

# Generated at 2026-10-25 09:46:34.350339
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

# Generated at 2026-10-25 09:46:35.887441
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

# Generated at 2026-10-25 09:46:42.338372
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

# Generated at 2026-10-25 09:46:44.079559
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

# Generated at 2026-10-25 09:47:00.669310
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

# Generated at 2026-10-25 09:47:03.085163
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:47:05.498824
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:47:08.047516
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:47:10.808176
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:47:13.227353
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:47:15.644086
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:47:18.055692
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:47:20.475960
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:47:22.889907
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:47:25.308423
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:47:27.726503
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:47:30.139755
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:47:32.557782
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:47:34.969763
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:47:37.390491
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:47:39.807642
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:47:42.232095
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:47:44.645853
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:47:47.060161
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:47:49.478254
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:47:51.896783
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:48:07.219555
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:48:09.634134
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 09:48:12.048173
# Unit test for constructor of class _AuthTypeLazyChoices