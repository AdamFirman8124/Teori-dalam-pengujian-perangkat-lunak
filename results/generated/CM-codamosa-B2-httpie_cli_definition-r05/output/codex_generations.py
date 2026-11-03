

# Generated at 2026-11-03 06:02:12.395032
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    """
    Test the constructor of class _AuthTypeLazyChoices, along with its
    __contains__ and __iter__ methods.
    """
    choices = _AuthTypeLazyChoices()
    assert choices is not None

    # __contains__ should reflect the auth plugin mapping
    assert 'basic' in choices
    assert 'digest' in choices
    assert 'nonexistent' not in choices

    # __iter__ should yield the sorted auth plugin type names
    assert list(choices) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

    # Works with argparse-style membership checks
    assert all(str(item) == item for item in choices)

# Generated at 2026-11-03 06:03:18.649500
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    auth_plugin_mapping = plugin_manager.get_auth_plugin_mapping()

    # All registered auth plugin types should be recognized.
    for auth_type in auth_plugin_mapping:
        assert auth_type in auth_type_lazy_choices
        assert auth_type_lazy_choices.__contains__(auth_type)

    # Unknown auth types should not be recognized.
    assert 'nonexistent-auth-type' not in auth_type_lazy_choices
    assert not auth_type_lazy_choices.__contains__('nonexistent-auth-type')
    assert '' not in auth_type_lazy_choices

    # The built-in plugins should always be available.
    assert 'basic' in auth_type_lazy_choices
    assert 'digest' in auth_type_lazy_choices

# Generated at 2026-11-03 06:04:43.742644
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from httpie.plugins.registry import plugin_manager

    auth_type_lazy_choices = _AuthTypeLazyChoices()
    auth_plugin_mapping = plugin_manager.get_auth_plugin_mapping()

    # Auth types registered with the plugin manager should be contained
    for auth_type in auth_plugin_mapping:
        assert auth_type in auth_type_lazy_choices
        assert auth_type_lazy_choices.__contains__(auth_type) is True

    # Auth types not registered should not be contained
    assert 'nonexistent_auth_type' not in auth_type_lazy_choices
    assert auth_type_lazy_choices.__contains__('nonexistent_auth_type') is False

# Generated at 2026-11-03 06:06:10.269938
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()

    # All registered auth plugin prefixes should be contained.
    mapping = plugin_manager.get_auth_plugin_mapping()
    for prefix in mapping:
        assert prefix in choices

    # Unknown auth types should not be contained.
    assert 'nonexistent-auth-type' not in choices
    assert '' not in choices

# Generated at 2026-11-03 06:07:31.167404
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = plugin_manager.get_auth_plugin_mapping()

    # Every registered auth plugin type must be recognized as a valid choice.
    for auth_type in mapping:
        assert auth_type in choices

    # Built-in auth types are always registered.
    assert 'basic' in choices
    assert 'digest' in choices

    # Unregistered auth types must not be recognized.
    assert 'definitely-not-a-registered-auth-type' not in choices