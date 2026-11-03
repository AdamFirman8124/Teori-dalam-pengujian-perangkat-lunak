

# Generated at 2026-11-02 06:51:08.500593
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    # nonce:2f6f7b3d
    choices = _AuthTypeLazyChoices()

    # With no auth plugins registered, iteration should yield nothing.
    original_mapping = plugin_manager.get_auth_plugin_mapping
    try:
        plugin_manager.get_auth_plugin_mapping = lambda: {}
        assert list(choices) == []
        assert sorted(choices) == []

        # With auth plugins registered, iteration should yield sorted keys.
        fake_mapping = {
            'digest': object(),
            'basic': object(),
            'custom': object(),
        }
        plugin_manager.get_auth_plugin_mapping = lambda: fake_mapping
        assert list(choices) == sorted(fake_mapping.keys())
        assert list(choices) == ['basic', 'custom', 'digest']
    finally:
        plugin_manager.get_auth_plugin_mapping = original_mapping

# Generated at 2026-11-02 06:51:56.737005
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    lazy_choices = _AuthTypeLazyChoices()

    # All registered auth plugin types must be considered valid choices
    auth_plugin_mapping = plugin_manager.get_auth_plugin_mapping()
    assert len(auth_plugin_mapping) > 0
    for auth_type in auth_plugin_mapping:
        assert auth_type in lazy_choices

    # Built-in auth types are always available
    assert 'basic' in lazy_choices
    assert 'digest' in lazy_choices

    # Unknown auth types must not be contained
    assert 'nonexistent-auth-type' not in lazy_choices
    assert '' not in lazy_choices

# Generated at 2026-11-02 06:53:18.042602
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from httpie.cli.argparse import _AuthTypeLazyChoices
    from httpie.plugins.registry import plugin_manager

    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # __iter__ should return an iterator over the sorted auth plugin names
    result = auth_type_lazy_choices.__iter__()
    assert iter(result) is result  # it is an iterator

    expected = sorted(plugin_manager.get_auth_plugin_mapping().keys())
    assert list(result) == expected

    # Also verify via the iterable protocol and that content matches (sorted)
    assert set(auth_type_lazy_choices) == set(expected)
    assert list(auth_type_lazy_choices) == expected
    assert list(auth_type_lazy_choices) == sorted(list(auth_type_lazy_choices))

# Generated at 2026-11-02 06:55:52.258825
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    '''Test __contains__ of _AuthTypeLazyChoices.'''
    from httpie.plugins.registry import plugin_manager

    auth_type_lazy_choices = _AuthTypeLazyChoices()

    # Every registered auth plugin type should be contained.
    for auth_type in plugin_manager.get_auth_plugin_mapping():
        assert auth_type in auth_type_lazy_choices

    # Built-in plugin types in particular.
    assert 'basic' in auth_type_lazy_choices
    assert 'digest' in auth_type_lazy_choices

    # Unknown auth types should not be contained.
    assert 'nonexistent-auth-type' not in auth_type_lazy_choices

# Generated at 2026-11-02 06:57:14.380467
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()

    # Every registered auth plugin type should be recognized as contained
    for auth_type in plugin_manager.get_auth_plugin_mapping():
        assert auth_type in choices

    # Basic and digest are built-in plugins, so they must be contained
    assert 'basic' in choices
    assert 'digest' in choices

    # Unregistered/unknown auth types should not be contained
    assert 'nonexistent-auth-type' not in choices
    assert '' not in choices
    assert None not in choices

# Generated at 2026-11-02 06:59:20.999353
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    """
    Unit test for the constructor of class _AuthTypeLazyChoices.

    The class relies on the default object constructor; verify that an
    instance can be created and that its membership/iteration behaviour
    reflects the registered auth plugins.
    """
    choices = _AuthTypeLazyChoices()

    # Instance should be created successfully.
    assert choices is not None

    # __contains__ should report the built-in auth plugin types.
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types should not be contained.
    assert 'unknown-auth-type' not in choices

    # __iter__ should yield the sorted auth plugin mapping keys.
    expected = sorted(plugin_manager.get_auth_plugin_mapping().keys())
    assert list(choices) == expected
    # Iteration should be reproducible.
    assert list(choices) == expected