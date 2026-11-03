

# Generated at 2026-11-02 00:40:15.838941
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from unittest.mock import patch

    from httpie.cli.definition import _AuthTypeLazyChoices
    from httpie.plugins import plugin_manager

    fake_mapping = {
        'digest': 'DigestAuthPlugin',
        'bearer': 'BearerAuthPlugin',
        'basic': 'BasicAuthPlugin',
    }

    with patch.object(plugin_manager, 'get_auth_plugin_mapping',
                      return_value=fake_mapping):
        choices = _AuthTypeLazyChoices()

        result = choices.__iter__()

        # __iter__ must return an iterator
        assert iter(result) is result

        # Keys must be yielded in sorted order
        assert list(result) == ['basic', 'bearer', 'digest']

        # Iterating again yields the same sorted keys
        assert list(choices) == sorted(fake_mapping.keys())

# Generated at 2026-11-02 00:41:21.373798
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():"""
    _AuthTypeLazyChoices.__contains__ should report membership based on the
    auth plugin types currently registered with the plugin manager.
    """

# Generated at 2026-11-02 00:42:34.404056
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from unittest import mock
    from httpie.plugins import plugin_manager

    fake_mapping = {
        'digest': object,
        'basic': object,
        'bearer': object,
    }

    with mock.patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        choices = _AuthTypeLazyChoices()

        result = list(choices)
        assert result == sorted(fake_mapping.keys())
        assert result == ['basic', 'bearer', 'digest']

        # Iterating again should yield a fresh, sorted iterator
        result2 = list(iter(choices))
        assert result2 == ['basic', 'bearer', 'digest']
        assert result2 is not result

# Generated at 2026-11-02 00:43:55.690129
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    assert isinstance(auth_type_lazy_choices, _AuthTypeLazyChoices)

    mapping = plugin_manager.get_auth_plugin_mapping()
    expected = sorted(mapping.keys())

    # __iter__ yields all registered auth plugin types, sorted
    assert list(auth_type_lazy_choices) == expected

    # __contains__ reflects the auth plugin mapping
    for auth_type in mapping:
        assert auth_type in auth_type_lazy_choices
    assert 'non-existent-auth-type' not in auth_type_lazy_choices

# Generated at 2026-11-02 00:45:28.772043
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    """Unit test for method __contains__ of class _AuthTypeLazyChoices"""
    from httpie.plugins.registry import plugin_manager

    instance = _AuthTypeLazyChoices()

    # Auth types provided by built-in plugins should be recognized.
    assert 'basic' in instance
    assert 'digest' in instance

    # Unknown auth types should not be recognized.
    assert 'definitely-not-an-auth-type' not in instance
    assert '' not in instance

    # Every key of the auth plugin mapping must be contained.
    for auth_type in plugin_manager.get_auth_plugin_mapping():
        assert auth_type in instance

# Generated at 2026-11-02 00:46:43.797533
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from httpie.plugins import plugin_manager

    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Every registered auth type must be recognized as a valid choice
    for auth_type in plugin_manager.get_auth_plugin_mapping():
        assert auth_type in auth_type_lazy_choices

    # Built-in auth types
    assert 'basic' in auth_type_lazy_choices
    assert 'digest' in auth_type_lazy_choices

    # Unregistered/invalid auth types must not be accepted
    assert 'invalid_auth_type' not in auth_type_lazy_choices
    assert '' not in auth_type_lazy_choices
    assert None not in auth_type_lazy_choices

# Generated at 2026-11-02 00:48:08.147584
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
# nonce:ea89a2e6
    from unittest.mock import patch

    from httpie.cli.definition import _AuthTypeLazyChoices
    from httpie.plugins.registry import plugin_manager

    lazy_choices = _AuthTypeLazyChoices()
    fake_mapping = {
        'basic': object(),
        'digest': object(),
        'apikey-header': object(),
    }

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=fake_mapping
    ):
        # Items present in the auth plugin mapping are contained.
        assert 'basic' in lazy_choices
        assert 'digest' in lazy_choices
        assert 'apikey-header' in lazy_choices

        # Items absent from the mapping are not contained.
        assert 'nonexistent-plugin' not in lazy_choices
        assert '' not in lazy_choices

# Generated at 2026-11-02 00:49:17.537025
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    """
    Test that __iter__ of _AuthTypeLazyChoices returns an iterator
    over the sorted keys of the auth plugin mapping.
    """
    auth_type_lazy_choices = _AuthTypeLazyChoices()

    expected = sorted(plugin_manager.get_auth_plugin_mapping().keys())

    result = auth_type_lazy_choices.__iter__()

    # __iter__ must return an iterator object
    assert iter(result) is result

    # Iterating yields exactly the sorted auth plugin types
    assert list(result) == expected

    # iter() on the instance produces the same (fresh) contents
    assert list(iter(auth_type_lazy_choices)) == expected

    # Contents are sorted
    assert list(auth_type_lazy_choices) == sorted(auth_type_lazy_choices)