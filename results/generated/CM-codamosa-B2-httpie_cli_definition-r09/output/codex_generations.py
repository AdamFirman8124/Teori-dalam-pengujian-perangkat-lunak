

# Generated at 2026-11-03 01:44:37.501630
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    auth_plugin_mapping = plugin_manager.get_auth_plugin_mapping()

    # __contains__ should accept every registered auth plugin type
    for auth_type in auth_plugin_mapping:
        assert auth_type in choices

    # __contains__ should reject unknown auth types
    assert 'invalid-auth-type' not in choices

    # __iter__ should yield the sorted auth plugin type keys
    assert list(choices) == sorted(auth_plugin_mapping.keys())

    # A fresh iterator should be produced on each iteration
    assert list(choices) == list(choices)

# Generated at 2026-11-03 01:46:09.252431
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()
    assert isinstance(choices, _AuthTypeLazyChoices)

    mapping = plugin_manager.get_auth_plugin_mapping()

    # __iter__ should yield all auth types, sorted
    assert list(choices) == sorted(mapping.keys())

    # __contains__ should accept known auth types
    for auth_type in mapping:
        assert auth_type in choices

    # __contains__ should reject unknown auth types
    assert 'non-existent-auth-type' not in choices

# Generated at 2026-11-03 01:47:47.369352
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from unittest.mock import patch

    # With the real plugin manager: should yield sorted auth plugin prefixes
    instance = _AuthTypeLazyChoices()
    expected = sorted(plugin_manager.get_auth_plugin_mapping().keys())
    iterator = instance.__iter__()
    # __iter__ must return an iterator
    assert iter(iterator) is iterator
    assert list(iterator) == expected
    # Repeated iteration yields fresh, identical results
    assert list(instance) == expected
    assert 'basic' in list(instance)

    # With a mocked plugin mapping: keys are returned in sorted order
    with patch(
        'httpie.cli.definition.plugin_manager.get_auth_plugin_mapping'
    ) as mock_get_mapping:
        mock_get_mapping.return_value = {
            'digest': 'DigestAuthPlugin',
            'basic': 'BasicAuthPlugin',
            'custom': 'CustomAuthPlugin',
        }
        choices = _AuthTypeLazyChoices()
        assert list(choices) == ['basic', 'custom', 'digest']
        mock_get_mapping.assert_called()

# Generated at 2026-11-03 01:49:23.608528
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from unittest import mock

    fake_mapping = {
        'digest': 'DigestAuthPlugin',
        'basic': 'BasicAuthPlugin',
        'auth': 'AuthPlugin',
    }

    with mock.patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping
    ):
        choices = _AuthTypeLazyChoices()

        # __iter__ must return an iterator
        iterator = choices.__iter__()
        assert iter(iterator) is iterator

        # Keys must be yielded in sorted order
        assert list(iterator) == ['auth', 'basic', 'digest']
        assert list(choices) == sorted(fake_mapping.keys())

        # Can be iterated multiple times (each call returns a fresh iterator)
        assert list(choices) == ['auth', 'basic', 'digest']

    # Without mocking, results must match the real plugin mapping, sorted
    actual_mapping = plugin_manager.get_auth_plugin_mapping()
    assert list(_AuthTypeLazyChoices()) == sorted(actual_mapping.keys())

# Generated at 2026-11-03 01:50:18.876594
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    """Test that __iter__ yields the sorted auth plugin type keys."""
    from unittest import mock

    auth_type_lazy_choices = _AuthTypeLazyChoices()

    mock_mapping = {
        'digest': object,
        'basic': object,
        'bearer': object,
    }

    with mock.patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=mock_mapping,
    ):
        result = list(auth_type_lazy_choices)

    assert result == sorted(mock_mapping.keys())
    assert result == ['basic', 'bearer', 'digest']

# Generated at 2026-11-03 01:51:55.262986
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()

    # Every registered auth plugin type should be recognized as a valid choice.
    mapping = plugin_manager.get_auth_plugin_mapping()
    for auth_type in mapping:
        assert auth_type in choices

    # Built-in auth plugin types.
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types should not be recognized.
    assert 'nonexistent-auth-type' not in choices
    assert '' not in choices

# Generated at 2026-11-03 01:52:43.599029
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    '''Test the constructor and dunder methods of _AuthTypeLazyChoices.'''
    mock_plugin_manager = Mock()
    mock_plugin_manager.get_auth_plugin_mapping.return_value = {
        'digest': 'DigestAuthPlugin',
        'basic': 'BasicAuthPlugin',
        'custom': 'CustomAuthPlugin',
    }

    with patch('httpie.cli.definition.plugin_manager', mock_plugin_manager):
        auth_type_lazy_choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin manager's auth plugin mapping
        assert 'basic' in auth_type_lazy_choices
        assert 'digest' in auth_type_lazy_choices
        assert 'custom' in auth_type_lazy_choices
        assert 'unknown' not in auth_type_lazy_choices

        # __iter__ yields the sorted auth type keys
        assert list(auth_type_lazy_choices) == ['basic', 'custom', 'digest']

        # The plugin manager was queried for the mapping
        assert mock_plugin_manager.get_auth_plugin_mapping.called

# Generated at 2026-11-03 01:53:53.899714
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    """Unit test for method __contains__ of class _AuthTypeLazyChoices."""
    from httpie.plugins import plugin_manager

    choices = _AuthTypeLazyChoices()

    # Built-in auth plugins must be recognized as valid choices.
    assert 'basic' in choices
    assert 'digest' in choices

    # Everything present in the plugin mapping should be contained.
    for name in plugin_manager.get_auth_plugin_mapping():
        assert name in choices

    # Unknown auth types must not be contained.
    assert 'non-existent-auth-type' not in choices