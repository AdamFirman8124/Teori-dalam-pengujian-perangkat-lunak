

# Generated at 2026-11-02 20:07:53.843997
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    with patch('httpie.cli.definition.plugin_manager.get_auth_plugin_mapping') as get_auth_plugin_mapping:
        get_auth_plugin_mapping.return_value = {
            'digest': object(),
            'basic': object(),
            'bearer': object(),
        }
        choices = _AuthTypeLazyChoices()
        result = choices.__iter__()
        # __iter__ must return an iterator over the sorted plugin mapping keys
        assert iter(result) is result
        assert list(result) == ['basic', 'bearer', 'digest']

# Generated at 2026-11-02 20:09:22.748955
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    # Constructor should return a usable instance without any setup
    assert choices is not None
    assert isinstance(choices, _AuthTypeLazyChoices)

    auth_plugin_mapping = plugin_manager.get_auth_plugin_mapping()

    # __contains__ should reflect the plugin manager's auth plugin mapping
    for item in auth_plugin_mapping:
        assert item in choices

    # __iter__ should yield the mapping keys in sorted order
    assert list(choices) == sorted(auth_plugin_mapping.keys())

    # Unknown auth types should not be contained
    assert 'definitely-not-an-auth-type' not in choices

# Generated at 2026-11-02 20:10:51.658927
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
# nonce:89a031fe
    """Test method __iter__ of class _AuthTypeLazyChoices."""
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    expected = sorted(plugin_manager.get_auth_plugin_mapping().keys())
    assert list(auth_type_lazy_choices.__iter__()) == expected
    assert list(auth_type_lazy_choices) == expected
    assert list(iter(auth_type_lazy_choices)) == expected

# Generated at 2026-11-02 20:12:39.257676
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    """Unit test for method __iter__ of class _AuthTypeLazyChoices"""
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    actual = list(auth_type_lazy_choices.__iter__())
    expected = sorted(plugin_manager.get_auth_plugin_mapping().keys())
    assert actual == expected
    # The returned items should be in sorted order
    assert actual == sorted(actual)
    # __iter__ should return an iterator
    assert iter(auth_type_lazy_choices) is not None
    assert list(iter(auth_type_lazy_choices)) == expected

# Generated at 2026-11-02 20:14:27.332956
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    # __contains__ should reflect the registered auth plugin mapping.
    mapping_keys = plugin_manager.get_auth_plugin_mapping().keys()
    for key in mapping_keys:
        assert key in choices

    # Builtin auth types are always available.
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types should not be contained.
    assert 'definitely-not-an-auth-type' not in choices

    # __iter__ should yield the plugin names in sorted order.
    assert list(choices) == sorted(mapping_keys)

# Generated at 2026-11-02 20:16:16.038599
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    '''
    Test __iter__ method of _AuthTypeLazyChoices class.

    It should return an iterator over the sorted keys of the
    auth plugin mapping provided by the plugin manager.
    '''
    instance = _AuthTypeLazyChoices()
    result = instance.__iter__()

    assert result is not None
    assert iter(result) is result  # An actual iterator is returned.

    expected = sorted(plugin_manager.get_auth_plugin_mapping().keys())
    assert list(result) == expected

    # Iterating twice yields the same sorted plugin types.
    assert list(instance) == expected