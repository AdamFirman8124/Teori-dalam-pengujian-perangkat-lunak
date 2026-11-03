

# Generated at 2026-11-01 23:47:49.771925
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    """
    Test that _AuthTypeLazyChoices can be instantiated and that it lazily
    exposes the auth plugin mapping via __iter__ and __contains__.
    """
    fake_mapping = {
        'digest': object,
        'basic': object,
        'custom': object,
    }
    with patch.object(plugin_manager, 'get_auth_plugin_mapping',
                      return_value=fake_mapping):
        choices = _AuthTypeLazyChoices()

        # Constructor produces an instance of the class
        assert isinstance(choices, _AuthTypeLazyChoices)

        # __iter__ yields sorted auth type names
        assert list(choices) == ['basic', 'custom', 'digest']

        # __contains__ delegates to the plugin mapping
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'custom' in choices
        assert 'unknown' not in choices

# Generated at 2026-11-01 23:48:14.753929
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from unittest.mock import patch

    from httpie.cli.argtypes import _AuthTypeLazyChoices
    from httpie.plugins.builtin import BasicAuthPlugin
    from httpie.plugins.registry import plugin_manager

    choices = _AuthTypeLazyChoices()

    # Built-in auth plugin types are accepted.
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected.
    assert 'invalid-auth-type' not in choices

    # The lookup is lazy: it reflects the plugins registered at call time.
    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value={'basic': BasicAuthPlugin},
    ):
        assert 'basic' in choices
        assert 'digest' not in choices

# Generated at 2026-11-01 23:49:16.396918
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from unittest.mock import patch
    from httpie.plugins.registry import plugin_manager
    from httpie.cli.definition import _AuthTypeLazyChoices

    fake_mapping = {
        'digest': object,
        'basic': object,
        'bearer': object,
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        choices = _AuthTypeLazyChoices()
        iterator = choices.__iter__()

        # Must return an iterator, not a sequence
        assert iter(iterator) is iterator
        assert hasattr(iterator, '__next__')

        result = list(iterator)

    # Keys must be returned in sorted order regardless of insertion order
    assert result == sorted(fake_mapping.keys())
    assert result == ['basic', 'bearer', 'digest']


# Unit test for method __iter__ of class _AuthTypeLazyChoices (real plugin registry)
def test__AuthTypeLazyChoices___iter__with_real_plugins():
    from httpie.plugins.registry import plugin_manager
    from httpie.cli.definition import _AuthTypeLazyChoices

    choices = _AuthTypeLazyChoices()
    result = list(choices)
    expected = sorted(plugin_manager.get_auth_plugin_mapping().keys())

    assert result == expected
    assert len(result) > 0

# Generated at 2026-11-01 23:50:26.543132
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    auth_plugin_mapping = plugin_manager.get_auth_plugin_mapping()

    # __contains__ should recognize every registered auth plugin name
    for plugin_name in auth_plugin_mapping:
        assert plugin_name in auth_type_lazy_choices

    # Default plugins should be available
    assert 'basic' in auth_type_lazy_choices
    assert 'digest' in auth_type_lazy_choices

    # Unknown plugin names should not be recognized
    assert 'nonexistent-auth-plugin' not in auth_type_lazy_choices
    assert '' not in auth_type_lazy_choices

    # __iter__ should yield the plugin names in sorted order
    assert list(auth_type_lazy_choices) == sorted(auth_plugin_mapping.keys())

# Generated at 2026-11-01 23:51:41.935619
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    auth_plugin_mapping = plugin_manager.get_auth_plugin_mapping()

    # __iter__ should yield the same keys as the plugin mapping, sorted
    assert list(iter(auth_type_lazy_choices)) == sorted(auth_plugin_mapping.keys())

    # __contains__ should accept any registered auth plugin type
    for auth_type in auth_plugin_mapping:
        assert auth_type in auth_type_lazy_choices

    # Unregistered auth types should not be contained
    assert 'invalid_auth_type' not in auth_type_lazy_choices

# Generated at 2026-11-01 23:52:44.480612
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    """
    Test the constructor of _AuthTypeLazyChoices.

    The instance should be created successfully and lazily reflect
    the currently registered auth plugin types.
    """
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

    mapping = plugin_manager.get_auth_plugin_mapping()

    # __contains__ delegates to the plugin manager mapping
    for item in mapping:
        assert item in choices

    assert 'non-existent-auth-type' not in choices

    # __iter__ yields sorted auth plugin type names
    assert list(iter(choices)) == sorted(mapping.keys())

    # Iterating twice keeps working (lazy, not consumed once)
    assert list(iter(choices)) == sorted(mapping.keys())


# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test_AuthTypeLazyChoices___contains__():
    """Test _AuthTypeLazyChoices.__contains__."""
    choices = _AuthTypeLazyChoices()

    plugin_types = list(plugin_manager.get_auth_plugin_mapping().keys())
    assert plugin_types, 'Expected at least one registered auth plugin'

    for plugin_type in plugin_types:
        assert plugin_type in choices

    assert 'unknown-auth-type' not in choices


# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test_AuthTypeLazyChoices___iter__():
    """Test _AuthTypeLazyChoices.__iter__."""
    choices = _AuthTypeLazyChoices()

    expected = sorted(plugin_manager.get_auth_plugin_mapping().keys())
    actual = list(choices)

    assert actual == expected
    assert actual == sorted(actual)

# Generated at 2026-11-01 23:54:44.826713
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    '''Test for method __contains__ of class _AuthTypeLazyChoices.'''
    choices = _AuthTypeLazyChoices()

    # Every registered auth plugin type should be recognized as a valid choice.
    mapping = plugin_manager.get_auth_plugin_mapping()
    assert mapping  # sanity check: at least the built-in plugins are loaded
    for auth_type in mapping:
        assert auth_type in choices

    # Built-in auth types must be present.
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types and non-string values must not be recognized.
    assert 'unknown-auth-type' not in choices
    assert '' not in choices
    assert None not in choices
    assert 123 not in choices

# Generated at 2026-11-01 23:56:22.488413
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from unittest.mock import patch

    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'zeta': object(),
        'alpha': object(),
    }

    with patch.object(plugin_manager, 'get_auth_plugin_mapping',
                      return_value=fake_mapping):
        choices = _AuthTypeLazyChoices()

        # __iter__ should return an iterator over the sorted mapping keys
        iterator = choices.__iter__()
        assert iter(iterator) is iterator  # it is a proper iterator

        result = list(iterator)
        assert result == sorted(fake_mapping.keys())
        assert result == ['alpha', 'basic', 'digest', 'zeta']

        # A fresh iteration re-sorts from the (current) mapping
        assert list(choices) == ['alpha', 'basic', 'digest', 'zeta']

    # Without mocking, it must match the real plugin manager mapping
    assert list(_AuthTypeLazyChoices()) == sorted(
        plugin_manager.get_auth_plugin_mapping().keys()
    )