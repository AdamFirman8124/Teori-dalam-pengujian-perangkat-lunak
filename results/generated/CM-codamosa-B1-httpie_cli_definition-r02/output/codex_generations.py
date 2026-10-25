

# Generated at 2026-10-24 01:27:08.563392
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 01:27:20.165715
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    with patch.object(plugin_manager, 'get_auth_plugin_mapping') as get_mapping:
        choices = _AuthTypeLazyChoices()

        assert isinstance(choices, _AuthTypeLazyChoices)
        get_mapping.assert_not_called()  # Choices are loaded lazily.

# Generated at 2026-10-24 01:27:29.336055
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 01:28:03.130616
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

# Generated at 2026-10-24 01:28:13.664210
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 01:28:15.100550
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

# Generated at 2026-10-24 01:28:55.159260
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:29:02.112088
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)
    assert choices.__dict__ == {}

# Generated at 2026-10-24 01:29:07.435962
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 01:29:20.337811
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 01:29:29.861588
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():from unittest.mock import Mock


def test__AuthTypeLazyChoices(monkeypatch):
    get_auth_plugin_mapping = Mock(
        return_value={
            'digest': object(),
            'basic': object(),
        }
    )
    monkeypatch.setattr(
        plugin_manager,
        'get_auth_plugin_mapping',
        get_auth_plugin_mapping,
    )

    choices = _AuthTypeLazyChoices()

    # Construction must remain lazy.
    get_auth_plugin_mapping.assert_not_called()

    assert isinstance(choices, _AuthTypeLazyChoices)
    assert list(choices) == ['basic', 'digest']
    assert 'basic' in choices
    assert 'unknown' not in choices

# Generated at 2026-10-24 01:29:31.254864
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:29:41.495321
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    auth_plugins = {
        'zeta': object(),
        'alpha': object(),
        'middle': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=auth_plugins,
    ) as get_auth_plugin_mapping:
        result = list(iter(_AuthTypeLazyChoices()))

    assert result == ['alpha', 'middle', 'zeta']
    get_auth_plugin_mapping.assert_called_once_with()

# Generated at 2026-10-24 01:29:47.434055
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 01:29:48.868373
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:29:50.201140
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:29:55.945021
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 01:30:03.551761
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
    ) as get_auth_plugin_mapping:
        choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)
    get_auth_plugin_mapping.assert_not_called()

# Generated at 2026-10-24 01:30:27.308436
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    from unittest.mock import patch

    plugin_mapping = {
        'oauth': object(),
        'basic': object(),
        'digest': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=plugin_mapping,
    ) as get_mapping:
        result = list(_AuthTypeLazyChoices().__iter__())

    assert result == ['basic', 'digest', 'oauth']
    get_mapping.assert_called_once_with()

# Generated at 2026-10-24 01:30:34.682694
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 01:30:49.221610
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 01:30:50.861107
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

# Generated at 2026-10-24 01:31:01.584195
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    choices = _AuthTypeLazyChoices()
    auth_plugins = {
        'token': object(),
        'basic': object(),
        'digest': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=auth_plugins,
    ):
        assert list(iter(choices)) == ['basic', 'digest', 'token']

# Generated at 2026-10-24 01:31:10.626585
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)
    assert choices.__dict__ == {}

# Generated at 2026-10-24 01:31:11.955084
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:31:17.038298
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 01:31:22.667057
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 01:31:23.994761
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

# Generated at 2026-10-24 01:31:33.663962
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 01:31:34.991606
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

# Generated at 2026-10-24 01:31:45.133811
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 01:32:05.830738
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 01:32:11.793909
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 01:32:24.593587
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 01:32:25.884391
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

# Generated at 2026-10-24 01:32:27.218300
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:32:33.568071
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 01:32:34.895960
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:32:36.222082
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:32:43.706287
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    from unittest.mock import patch

    with patch.object(plugin_manager, 'get_auth_plugin_mapping') as get_mapping:
        choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)
    get_mapping.assert_not_called()

# Generated at 2026-10-24 01:32:45.040554
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:32:46.470510
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:32:47.903882
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:32:58.595246
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 01:32:59.929250
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

# Generated at 2026-10-24 01:33:01.257272
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:33:02.574646
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:33:14.016031
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 01:33:15.350052
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:33:20.980074
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 01:33:22.321112
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:33:23.630013
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:33:33.787674
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 01:33:35.113132
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

# Generated at 2026-10-24 01:33:42.722116
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 01:33:44.394531
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:33:45.761109
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:33:47.199151
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:33:59.933688
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 01:34:01.324983
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

# Generated at 2026-10-24 01:34:10.545665
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-24 01:34:25.090502
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-24 01:34:26.515059
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:34:28.155206
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:34:38.806124
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 01:34:40.129761
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

# Generated at 2026-10-24 01:34:47.613724
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 01:34:49.045517
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:34:57.045050
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)
    assert choices.__dict__ == {}

# Generated at 2026-10-24 01:35:06.451538
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 01:35:07.776376
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

# Generated at 2026-10-24 01:35:15.565508
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)
    assert choices.__dict__ == {}

# Generated at 2026-10-24 01:35:16.879226
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:35:27.959376
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 01:35:29.287812
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

# Generated at 2026-10-24 01:35:39.936461
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 01:35:50.176518
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 01:35:55.207111
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 01:36:05.096306
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 01:36:06.553683
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

# Generated at 2026-10-24 01:36:18.018893
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    auth_plugins = {
        'zeta': object(),
        'basic': object(),
        'digest': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=auth_plugins,
    ) as get_auth_plugin_mapping:
        result = list(_AuthTypeLazyChoices())

    assert result == ['basic', 'digest', 'zeta']
    get_auth_plugin_mapping.assert_called_once_with()

# Generated at 2026-10-24 01:36:24.571986
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:36:26.005458
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices

# Generated at 2026-10-24 01:36:36.460814
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 01:36:37.771984
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

# Generated at 2026-10-24 01:36:45.370396
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 01:36:54.894597
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-24 01:36:56.327245
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

# Generated at 2026-10-24 01:37:02.779675
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    choices = _AuthTypeLazyChoices()

    assert isinstance(choices, _AuthTypeLazyChoices)

# Generated at 2026-10-24 01:37:04.102666
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = parser._option_string_actions['--auth-type'].choices

    # Known auth plugin names are accepted
    assert 'basic' in choices
    assert 'digest' in choices

    # Unknown auth types are rejected
    assert 'unknown-auth-type' not in choices