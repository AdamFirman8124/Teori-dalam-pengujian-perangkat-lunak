

# Generated at 2026-10-24 06:21:53.259082
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

# Generated at 2026-10-24 06:21:55.780730
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:21:58.292390
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:22:00.792162
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:22:03.217133
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:22:10.428378
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 06:22:11.739862
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 06:22:13.065424
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

# Generated at 2026-10-24 06:22:18.308532
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 06:22:19.628227
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

# Generated at 2026-10-24 06:22:26.300021
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():from unittest.mock import patch


# Generated at 2026-10-24 06:22:27.617142
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

# Generated at 2026-10-24 06:22:32.714555
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 06:22:34.185930
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

# Generated at 2026-10-24 06:22:38.980637
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 06:22:40.311851
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 06:22:49.648073
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:22:52.067587
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:22:54.485401
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:22:56.904786
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:22:59.320007
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:23:01.734783
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:23:04.148016
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:23:06.564515
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:23:08.978940
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:23:11.393595
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:23:13.815093
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:23:16.227241
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:23:17.623347
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 06:23:28.431905
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:23:29.748657
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

# Generated at 2026-10-24 06:23:31.068571
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

# Generated at 2026-10-24 06:23:35.726785
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 06:23:37.061959
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 06:23:38.369909
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 06:23:44.842222
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:23:46.162833
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

# Generated at 2026-10-24 06:23:52.418740
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:23:53.729609
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

# Generated at 2026-10-24 06:23:55.041306
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 06:24:02.604746
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
    ) as get_auth_plugin_mapping:
        assert list(_AuthTypeLazyChoices()) == ['basic', 'digest', 'oauth']

    get_auth_plugin_mapping.assert_called_once_with()

# Generated at 2026-10-24 06:24:09.382059
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:24:11.800369
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:24:14.215070
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:24:16.628480
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:24:19.045445
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:24:20.409477
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

# Generated at 2026-10-24 06:24:30.540894
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:24:31.847349
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

# Generated at 2026-10-24 06:24:33.167025
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 06:24:34.479707
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 06:24:40.240080
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:24:41.674280
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

# Generated at 2026-10-24 06:24:49.763529
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:24:51.071227
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

# Generated at 2026-10-24 06:24:52.570979
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 06:24:53.884438
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 06:24:56.447448
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:24:58.942357
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:25:01.358061
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:25:03.772462
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:25:06.190004
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:25:08.603827
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:25:11.364799
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:25:13.804488
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:25:16.219788
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:25:18.633481
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:25:21.050026
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:25:23.463153
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:25:25.878987
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:25:28.292738
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:25:35.232061
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 06:25:42.704747
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:25:44.028348
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

# Generated at 2026-10-24 06:25:45.348677
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

# Generated at 2026-10-24 06:25:50.400820
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 06:25:51.720617
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

# Generated at 2026-10-24 06:25:57.127942
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 06:26:05.030146
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from unittest.mock import patch

    mapping = {
        'oauth2': object(),
        'basic': object(),
        'digest': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=mapping,
    ) as get_auth_plugin_mapping:
        choices = _AuthTypeLazyChoices()

        assert list(choices.__iter__()) == ['basic', 'digest', 'oauth2']
        get_auth_plugin_mapping.assert_called_once_with()

# Generated at 2026-10-24 06:26:06.374447
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

# Generated at 2026-10-24 06:26:11.273784
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 06:26:13.695589
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:26:16.113156
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:26:18.625887
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:26:21.057259
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:26:23.457852
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:26:25.872730
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:26:28.288324
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:26:30.708784
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:26:33.122703
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:26:35.537296
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:26:37.952736
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:26:40.368710
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:26:42.782119
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:26:45.197377
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:26:47.614381
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:26:50.331916
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:26:52.749952
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:26:55.166830
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:26:57.584624
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:27:00.002970
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:27:14.265620
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from types import SimpleNamespace

# Generated at 2026-10-24 06:27:15.593580
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 06:27:16.912217
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

# Generated at 2026-10-24 06:27:22.288566
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 06:27:30.737625
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
    ) as get_mapping:
        choices = _AuthTypeLazyChoices()

        assert list(choices) == ['basic', 'digest', 'oauth']
        get_mapping.assert_called_once_with()

# Generated at 2026-10-24 06:27:32.062295
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

# Generated at 2026-10-24 06:27:39.646505
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():from unittest.mock import patch


# Generated at 2026-10-24 06:27:40.978699
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 06:27:42.412577
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 06:27:44.936760
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:27:47.512671
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:27:49.927854
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:27:52.475310
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:27:54.889680
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:27:57.304466
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:28:02.139571
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:28:04.552684
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:28:08.423413
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 06:28:15.202914
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:28:16.719234
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

# Generated at 2026-10-24 06:28:18.051088
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 06:28:19.434352
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 06:28:20.921719
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 06:28:22.353292
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 06:28:23.661723
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 06:28:32.302309
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from unittest.mock import patch

    mapping = {
        'oauth': object(),
        'basic': object(),
        'digest': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=mapping,
    ) as get_mapping:
        choices = _AuthTypeLazyChoices()

        assert list(choices) == ['basic', 'digest', 'oauth']
        get_mapping.assert_called_once_with()

# Generated at 2026-10-24 06:28:33.816967
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

# Generated at 2026-10-24 06:28:38.223213
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 06:28:39.703019
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

# Generated at 2026-10-24 06:28:42.287665
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:28:44.704276
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:28:53.881874
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:28:56.438929
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:28:58.854186
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:29:01.270396
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:29:03.685138
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:29:06.108756
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:29:08.512970
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:29:10.927757
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:29:13.341559
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:29:15.757421
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:29:18.183576
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:29:20.588195
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:29:21.890411
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 06:29:23.207015
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

# Generated at 2026-10-24 06:29:28.396206
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 06:29:29.722057
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

# Generated at 2026-10-24 06:29:34.539427
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 06:29:45.906632
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from unittest.mock import patch

    auth_plugins = {
        'oauth2': object(),
        'basic': object(),
        'digest': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=auth_plugins,
    ) as get_mapping:
        choices = _AuthTypeLazyChoices()

        assert list(choices) == ['basic', 'digest', 'oauth2']
        get_mapping.assert_called_once_with()

# Generated at 2026-10-24 06:29:47.338634
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

# Generated at 2026-10-24 06:29:52.151908
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 06:29:53.482503
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

# Generated at 2026-10-24 06:29:58.934070
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 06:30:11.454981
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:30:13.871634
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:30:16.285532
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:30:18.699490
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:30:21.118969
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:30:23.534271
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:30:30.858820
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():auth_type_lazy_choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 06:30:32.186338
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

# Generated at 2026-10-24 06:30:37.417062
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 06:30:38.733649
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

# Generated at 2026-10-24 06:30:44.146443
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 06:30:51.845593
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    auth_plugins = {
        'token': object(),
        'basic': object(),
        'digest': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=auth_plugins,
    ) as get_auth_plugin_mapping:
        result = list(_AuthTypeLazyChoices())

    assert result == ['basic', 'digest', 'token']
    get_auth_plugin_mapping.assert_called_once_with()

# Generated at 2026-10-24 06:30:53.185844
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

# Generated at 2026-10-24 06:30:57.792261
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 06:30:59.117268
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 06:31:00.442726
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

# Generated at 2026-10-24 06:31:05.174114
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 06:31:06.484695
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 06:31:32.232947
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:31:34.646901
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 06:31:42.334304
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()