

# Generated at 2026-11-02 22:52:22.488081
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    instance = _AuthTypeLazyChoices()
    assert instance is not None
    # Built-in auth types should be recognized via __contains__
    assert 'basic' in instance
    assert 'digest' in instance
    assert 'nonexistent-auth-type' not in instance
    # __iter__ should yield sorted auth plugin mapping keys
    assert list(instance) == sorted(plugin_manager.get_auth_plugin_mapping().keys())

# Generated at 2026-11-02 23:00:46.779815
# Unit test for method __contains__ of class _AuthTypeLazyChoices