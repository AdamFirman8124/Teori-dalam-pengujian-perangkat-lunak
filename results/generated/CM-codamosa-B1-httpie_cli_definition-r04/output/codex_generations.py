

# Generated at 2026-10-24 07:09:49.178599
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 07:09:50.491982
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    target = f"{_AuthTypeLazyChoices.__module__}.plugin_manager.get_auth_plugin_mapping"

    with patch(target, return_value={"digest": object, "basic": object}) as mock_get:
        choices = _AuthTypeLazyChoices()  # constructor: no args, lazy
        mock_get.assert_not_called()

        assert isinstance(choices, _AuthTypeLazyChoices)
        assert list(choices) == ["basic", "digest"]
        assert "basic" in choices
        assert "missing" not in choices

    with pytest.raises(TypeError):
        _AuthTypeLazyChoices("basic")

# Generated at 2026-10-24 07:09:57.032371
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 07:10:02.666549
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:10:05.084951
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:10:07.503243
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:10:09.917543
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:10:12.337192
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:10:14.752360
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:10:17.310965
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:10:19.724853
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:10:22.142467
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:10:24.559189
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:10:26.975147
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:10:29.387783
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:10:31.803287
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:10:34.215852
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:10:36.630681
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:10:39.046482
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:10:41.473671
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:10:43.881491
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:10:46.297123
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:10:48.713333
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:10:51.129122
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:10:53.546970
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:10:55.961067
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:10:58.374004
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:10:59.743225
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 07:11:01.061787
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 07:11:02.401657
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 07:11:04.176948
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    target = f"{_AuthTypeLazyChoices.__module__}.plugin_manager.get_auth_plugin_mapping"

    with patch(target, return_value={"digest": object, "basic": object}) as mock_get:
        choices = _AuthTypeLazyChoices()  # constructor: no args, lazy
        mock_get.assert_not_called()

        assert isinstance(choices, _AuthTypeLazyChoices)
        assert list(choices) == ["basic", "digest"]
        assert "basic" in choices
        assert "missing" not in choices

    with pytest.raises(TypeError):
        _AuthTypeLazyChoices("basic")

# Generated at 2026-10-24 07:11:11.578287
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 07:11:18.135123
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from unittest.mock import patch

    auth_plugins = {
        'oauth': object(),
        'basic': object(),
        'digest': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=auth_plugins,
    ):
        choices = _AuthTypeLazyChoices()

        assert list(choices.__iter__()) == ['basic', 'digest', 'oauth']

# Generated at 2026-10-24 07:11:19.444248
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    target = f"{_AuthTypeLazyChoices.__module__}.plugin_manager.get_auth_plugin_mapping"

    with patch(target, return_value={"digest": object, "basic": object}) as mock_get:
        choices = _AuthTypeLazyChoices()  # constructor: no args, lazy
        mock_get.assert_not_called()

        assert isinstance(choices, _AuthTypeLazyChoices)
        assert list(choices) == ["basic", "digest"]
        assert "basic" in choices
        assert "missing" not in choices

    with pytest.raises(TypeError):
        _AuthTypeLazyChoices("basic")

# Generated at 2026-10-24 07:11:31.855186
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 07:11:34.274693
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:11:36.786937
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:11:39.199766
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:11:41.620958
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:11:44.038233
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:11:46.459841
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:11:48.878292
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:11:51.296901
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:11:53.710118
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:11:56.125102
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:11:58.540835
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:12:00.959167
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:12:03.370638
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:12:05.784904
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:12:08.197223
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:12:10.610422
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:12:13.024503
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:12:15.440942
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:12:17.854528
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:12:45.686745
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    import sys
    definition_module = sys.modules[_AuthTypeLazyChoices.__module__]

    class _FakePluginManager:
        def get_auth_plugin_mapping(self):
            return {'digest': object(), 'bearer': object(), 'basic': object()}

    original_plugin_manager = definition_module.plugin_manager
    definition_module.plugin_manager = _FakePluginManager()
    try:
        choices = _AuthTypeLazyChoices()
        assert 'digest' in choices
        assert 'basic' in choices
        assert 'bearer' in choices
        assert 'nonexistent' not in choices
        assert list(choices) == ['basic', 'bearer', 'digest']
    finally:
        definition_module.plugin_manager = original_plugin_manager

# Generated at 2026-10-24 07:12:57.053259
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    plugin_mapping = {
        'zulu': object(),
        'basic': object(),
        'digest': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=plugin_mapping,
    ) as get_auth_plugin_mapping:
        choices = _AuthTypeLazyChoices()

        assert list(iter(choices)) == ['basic', 'digest', 'zulu']
        get_auth_plugin_mapping.assert_called_once_with()

# Generated at 2026-10-24 07:13:11.490720
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    plugin_mapping = {
        'zulu': object(),
        'basic': object(),
        'digest': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=plugin_mapping,
    ) as get_mapping:
        result = list(iter(_AuthTypeLazyChoices()))

    assert result == ['basic', 'digest', 'zulu']
    get_mapping.assert_called_once_with()

# Generated at 2026-10-24 07:13:12.835787
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    target = f"{_AuthTypeLazyChoices.__module__}.plugin_manager.get_auth_plugin_mapping"

    with patch(target, return_value={"digest": object, "basic": object}) as mock_get:
        choices = _AuthTypeLazyChoices()  # constructor: no args, lazy
        mock_get.assert_not_called()

        assert isinstance(choices, _AuthTypeLazyChoices)
        assert list(choices) == ["basic", "digest"]
        assert "basic" in choices
        assert "missing" not in choices

    with pytest.raises(TypeError):
        _AuthTypeLazyChoices("basic")

# Generated at 2026-10-24 07:13:36.350795
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():instance = _AuthTypeLazyChoices()

# Generated at 2026-10-24 07:13:47.842695
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:13:49.285069
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from unittest.mock import patch
    from httpie.cli.definition import _AuthTypeLazyChoices, plugin_manager

    choices = _AuthTypeLazyChoices()
    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'bearer': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        assert list(choices) == ['basic', 'bearer', 'digest']
        assert list(iter(choices)) == sorted(fake_mapping)

# Generated at 2026-10-24 07:13:51.805532
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:13:54.222336
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:13:56.637624
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:13:59.055205
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:14:01.471564
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:14:03.992939
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:14:06.406697
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:14:08.820420
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:14:25.223228
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 07:14:26.542970
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 07:14:27.873082
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 07:14:29.183029
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    target = f"{_AuthTypeLazyChoices.__module__}.plugin_manager.get_auth_plugin_mapping"

    with patch(target, return_value={"digest": object, "basic": object}) as mock_get:
        choices = _AuthTypeLazyChoices()  # constructor: no args, lazy
        mock_get.assert_not_called()

        assert isinstance(choices, _AuthTypeLazyChoices)
        assert list(choices) == ["basic", "digest"]
        assert "basic" in choices
        assert "missing" not in choices

    with pytest.raises(TypeError):
        _AuthTypeLazyChoices("basic")

# Generated at 2026-10-24 07:14:45.615628
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    import sys
    definition_module = sys.modules[_AuthTypeLazyChoices.__module__]

    class _FakePluginManager:
        def get_auth_plugin_mapping(self):
            return {'digest': object(), 'bearer': object(), 'basic': object()}

    original_plugin_manager = definition_module.plugin_manager
    definition_module.plugin_manager = _FakePluginManager()
    try:
        choices = _AuthTypeLazyChoices()
        assert 'digest' in choices
        assert 'basic' in choices
        assert 'bearer' in choices
        assert 'nonexistent' not in choices
        assert list(choices) == ['basic', 'bearer', 'digest']
    finally:
        definition_module.plugin_manager = original_plugin_manager

# Generated at 2026-10-24 07:14:46.963996
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 07:14:49.482287
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:14:51.987452
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:14:54.492767
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:14:56.910397
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:14:59.328987
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:15:01.745089
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:15:04.159247
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:15:06.731820
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:15:09.148528
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:15:11.566762
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:15:13.982690
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:15:16.398651
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:15:18.812803
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:15:21.239204
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:15:23.650756
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:15:26.068430
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:15:28.484379
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:15:30.900305
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:15:33.319675
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:15:35.737404
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:16:04.346566
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():obj = _AuthTypeLazyChoices()

# Generated at 2026-10-24 07:16:12.855572
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:16:14.168891
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from unittest.mock import patch
    from httpie.cli.definition import _AuthTypeLazyChoices, plugin_manager

    choices = _AuthTypeLazyChoices()
    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'bearer': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        assert list(choices) == ['basic', 'bearer', 'digest']
        assert list(iter(choices)) == sorted(fake_mapping)

# Generated at 2026-10-24 07:16:15.487184
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 07:16:16.804021
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    target = f"{_AuthTypeLazyChoices.__module__}.plugin_manager.get_auth_plugin_mapping"

    with patch(target, return_value={"digest": object, "basic": object}) as mock_get:
        choices = _AuthTypeLazyChoices()  # constructor: no args, lazy
        mock_get.assert_not_called()

        assert isinstance(choices, _AuthTypeLazyChoices)
        assert list(choices) == ["basic", "digest"]
        assert "basic" in choices
        assert "missing" not in choices

    with pytest.raises(TypeError):
        _AuthTypeLazyChoices("basic")

# Generated at 2026-10-24 07:16:33.222941
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    import sys
    definition_module = sys.modules[_AuthTypeLazyChoices.__module__]

    class _FakePluginManager:
        def get_auth_plugin_mapping(self):
            return {'digest': object(), 'bearer': object(), 'basic': object()}

    original_plugin_manager = definition_module.plugin_manager
    definition_module.plugin_manager = _FakePluginManager()
    try:
        choices = _AuthTypeLazyChoices()
        assert 'digest' in choices
        assert 'basic' in choices
        assert 'bearer' in choices
        assert 'nonexistent' not in choices
        assert list(choices) == ['basic', 'bearer', 'digest']
    finally:
        definition_module.plugin_manager = original_plugin_manager

# Generated at 2026-10-24 07:16:34.545301
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    target = f"{_AuthTypeLazyChoices.__module__}.plugin_manager.get_auth_plugin_mapping"

    with patch(target, return_value={"digest": object, "basic": object}) as mock_get:
        choices = _AuthTypeLazyChoices()  # constructor: no args, lazy
        mock_get.assert_not_called()

        assert isinstance(choices, _AuthTypeLazyChoices)
        assert list(choices) == ["basic", "digest"]
        assert "basic" in choices
        assert "missing" not in choices

    with pytest.raises(TypeError):
        _AuthTypeLazyChoices("basic")

# Generated at 2026-10-24 07:16:51.039235
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    import sys
    definition_module = sys.modules[_AuthTypeLazyChoices.__module__]

    class _FakePluginManager:
        def get_auth_plugin_mapping(self):
            return {'digest': object(), 'bearer': object(), 'basic': object()}

    original_plugin_manager = definition_module.plugin_manager
    definition_module.plugin_manager = _FakePluginManager()
    try:
        choices = _AuthTypeLazyChoices()
        assert 'digest' in choices
        assert 'basic' in choices
        assert 'bearer' in choices
        assert 'nonexistent' not in choices
        assert list(choices) == ['basic', 'bearer', 'digest']
    finally:
        definition_module.plugin_manager = original_plugin_manager

# Generated at 2026-10-24 07:16:53.499981
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    target = f"{_AuthTypeLazyChoices.__module__}.plugin_manager.get_auth_plugin_mapping"

    with patch(target, return_value={"digest": object, "basic": object}) as mock_get:
        choices = _AuthTypeLazyChoices()  # constructor: no args, lazy
        mock_get.assert_not_called()

        assert isinstance(choices, _AuthTypeLazyChoices)
        assert list(choices) == ["basic", "digest"]
        assert "basic" in choices
        assert "missing" not in choices

    with pytest.raises(TypeError):
        _AuthTypeLazyChoices("basic")

# Generated at 2026-10-24 07:17:08.741296
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 07:17:10.064215
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 07:17:19.506988
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:17:20.823603
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from unittest.mock import patch
    from httpie.cli.definition import _AuthTypeLazyChoices, plugin_manager

    choices = _AuthTypeLazyChoices()
    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'bearer': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        assert list(choices) == ['basic', 'bearer', 'digest']
        assert list(iter(choices)) == sorted(fake_mapping)

# Generated at 2026-10-24 07:17:22.139780
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 07:17:23.487636
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 07:17:25.907512
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:17:28.431464
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:17:30.846058
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:17:33.362190
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:17:35.793918
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:17:38.212643
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:17:40.626103
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:17:42.016173
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from unittest.mock import patch
    from httpie.cli.definition import _AuthTypeLazyChoices, plugin_manager

    choices = _AuthTypeLazyChoices()
    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'bearer': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        assert list(choices) == ['basic', 'bearer', 'digest']
        assert list(iter(choices)) == sorted(fake_mapping)

# Generated at 2026-10-24 07:17:52.582610
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:17:53.905198
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from unittest.mock import patch
    from httpie.cli.definition import _AuthTypeLazyChoices, plugin_manager

    choices = _AuthTypeLazyChoices()
    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'bearer': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        assert list(choices) == ['basic', 'bearer', 'digest']
        assert list(iter(choices)) == sorted(fake_mapping)

# Generated at 2026-10-24 07:17:55.228224
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 07:18:07.142930
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:18:08.462622
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from unittest.mock import patch
    from httpie.cli.definition import _AuthTypeLazyChoices, plugin_manager

    choices = _AuthTypeLazyChoices()
    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'bearer': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        assert list(choices) == ['basic', 'bearer', 'digest']
        assert list(iter(choices)) == sorted(fake_mapping)

# Generated at 2026-10-24 07:18:09.867228
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 07:18:12.284798
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:18:15.061326
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:18:17.479141
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:18:19.895889
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:18:22.447049
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:18:24.862410
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:18:27.283787
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:18:29.794425
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:18:32.208868
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:18:34.623323
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:18:37.038564
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:18:39.454411
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:18:41.872145
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:18:44.285581
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:18:46.700955
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:18:49.116521
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:18:51.534880
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:18:53.948211
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:18:59.755430
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    for auth_type in plugin_manager.get_auth_plugin_mapping():
        assert auth_type in auth_type_lazy_choices
    assert 'non-existent-auth-type' not in auth_type_lazy_choices

# Generated at 2026-10-24 07:19:01.191396
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    target = f"{_AuthTypeLazyChoices.__module__}.plugin_manager.get_auth_plugin_mapping"

    with patch(target, return_value={"digest": object, "basic": object}) as mock_get:
        choices = _AuthTypeLazyChoices()  # constructor: no args, lazy
        mock_get.assert_not_called()

        assert isinstance(choices, _AuthTypeLazyChoices)
        assert list(choices) == ["basic", "digest"]
        assert "basic" in choices
        assert "missing" not in choices

    with pytest.raises(TypeError):
        _AuthTypeLazyChoices("basic")

# Generated at 2026-10-24 07:19:16.145531
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 07:19:22.583513
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 07:19:23.911353
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    target = f"{_AuthTypeLazyChoices.__module__}.plugin_manager.get_auth_plugin_mapping"

    with patch(target, return_value={"digest": object, "basic": object}) as mock_get:
        choices = _AuthTypeLazyChoices()  # constructor: no args, lazy
        mock_get.assert_not_called()

        assert isinstance(choices, _AuthTypeLazyChoices)
        assert list(choices) == ["basic", "digest"]
        assert "basic" in choices
        assert "missing" not in choices

    with pytest.raises(TypeError):
        _AuthTypeLazyChoices("basic")

# Generated at 2026-10-24 07:19:40.423947
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    import sys
    definition_module = sys.modules[_AuthTypeLazyChoices.__module__]

    class _FakePluginManager:
        def get_auth_plugin_mapping(self):
            return {'digest': object(), 'bearer': object(), 'basic': object()}

    original_plugin_manager = definition_module.plugin_manager
    definition_module.plugin_manager = _FakePluginManager()
    try:
        choices = _AuthTypeLazyChoices()
        assert 'digest' in choices
        assert 'basic' in choices
        assert 'bearer' in choices
        assert 'nonexistent' not in choices
        assert list(choices) == ['basic', 'bearer', 'digest']
    finally:
        definition_module.plugin_manager = original_plugin_manager

# Generated at 2026-10-24 07:19:50.955844
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:19:53.372447
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 07:19:55.789857
# Unit test for method __iter__ of class _AuthTypeLazyChoices