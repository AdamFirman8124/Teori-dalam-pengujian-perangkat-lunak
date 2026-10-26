

# Generated at 2026-10-25 08:48:38.602675
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'bearer': object(),
    }

    with mock.patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        choices = _AuthTypeLazyChoices()

        result = iter(choices)
        assert iter(result) is result  # returns an iterator
        assert list(result) == ['basic', 'bearer', 'digest']  # sorted keys
        assert list(choices) == ['basic', 'bearer', 'digest']  # re-iterable

# Generated at 2026-10-25 08:48:41.021400
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:48:43.676696
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:48:46.296121
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:48:48.920795
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:48:51.343195
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:48:53.760218
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:48:56.177988
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:48:58.855851
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:01.279211
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:03.698086
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:06.117399
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:08.618943
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:10.999102
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:13.421857
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:15.832499
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:18.252516
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:20.672073
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:23.093412
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:25.508067
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:27.925798
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:30.342037
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:32.758141
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:35.177008
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:37.592490
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:40.010064
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:42.429111
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:44.845559
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:47.262125
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:49.681776
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:52.098527
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:54.607607
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:57.018921
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:49:59.436226
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:50:01.852936
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:50:04.274054
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:50:06.693162
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:50:09.110618
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:50:11.527683
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:50:13.948300
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:50:16.365392
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:50:18.783478
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:50:21.199112
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:50:23.654402
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:50:26.075955
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:50:28.507635
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:50:30.924791
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:50:33.343752
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:50:35.763652
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:50:38.344116
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:50:40.761591
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:50:43.179217
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:50:45.596811
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:50:48.014006
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:50:50.432838
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:50:52.851330
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:50:55.268166
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:50:57.686285
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:51:00.106629
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:51:02.523339
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:51:04.938364
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:51:43.904570
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()

    fake_mapping = {
        'basic': MagicMock(),
        'digest': MagicMock(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping
    ) as mock_get_mapping:
        # Present keys -> True
        assert ('basic' in choices) is True
        assert ('digest' in choices) is True

        # Absent keys -> False
        assert ('bearer' in choices) is False
        assert ('' in choices) is False
        assert ('BASIC' in choices) is False

        # Delegates to plugin_manager on each check (lazy, no caching)
        assert mock_get_mapping.call_count == 5

    # Empty mapping -> everything False
    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value={}
    ):
        assert ('basic' in choices) is False

    # Reflects updated mapping (proves laziness)
    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value={'bearer': MagicMock()}
    ):
        assert ('bearer' in choices) is True
        assert ('basic' in choices) is False

# Generated at 2026-10-25 08:51:45.349262
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()

    fake_mapping = {
        'basic': MagicMock(),
        'digest': MagicMock(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping
    ) as mock_get_mapping:
        # Present keys -> True
        assert ('basic' in choices) is True
        assert ('digest' in choices) is True

        # Absent keys -> False
        assert ('bearer' in choices) is False
        assert ('' in choices) is False
        assert ('BASIC' in choices) is False

        # Delegates to plugin_manager on each check (lazy, no caching)
        assert mock_get_mapping.call_count == 5

    # Empty mapping -> everything False
    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value={}
    ):
        assert ('basic' in choices) is False

    # Reflects updated mapping (proves laziness)
    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value={'bearer': MagicMock()}
    ):
        assert ('bearer' in choices) is True
        assert ('basic' in choices) is False

# Generated at 2026-10-25 08:51:46.782004
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 08:51:48.240325
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'bearer': object(),
    }

    with mock.patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        choices = _AuthTypeLazyChoices()

        result = iter(choices)
        assert iter(result) is result  # returns an iterator
        assert list(result) == ['basic', 'bearer', 'digest']  # sorted keys
        assert list(choices) == ['basic', 'bearer', 'digest']  # re-iterable

# Generated at 2026-10-25 08:51:49.651974
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 08:51:51.087189
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'bearer': object(),
    }

    with mock.patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        choices = _AuthTypeLazyChoices()

        result = iter(choices)
        assert iter(result) is result  # returns an iterator
        assert list(result) == ['basic', 'bearer', 'digest']  # sorted keys
        assert list(choices) == ['basic', 'bearer', 'digest']  # re-iterable

# Generated at 2026-10-25 08:51:52.624208
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 08:51:56.002052
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 08:51:58.550158
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:52:00.968992
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:52:03.409550
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:52:05.824791
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:52:08.238951
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:52:10.659376
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:52:13.077389
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:52:15.496887
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:52:17.909020
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:52:20.489039
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    auth_type_lazy_choices = _AuthTypeLazyChoices()
    with mock.patch(
        'httpie.plugins.plugin_manager',
        **{
            'get_auth_plugin_mapping.return_value': {
                'plugin1': None,
                'plugin2': None,
            }
        }
    ):
        assert list(auth_type_lazy_choices) == ['plugin1', 'plugin2']

# Generated at 2026-10-25 08:52:21.839115
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 08:52:23.215088
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'bearer': object(),
    }

    with mock.patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        choices = _AuthTypeLazyChoices()

        result = iter(choices)
        assert iter(result) is result  # returns an iterator
        assert list(result) == ['basic', 'bearer', 'digest']  # sorted keys
        assert list(choices) == ['basic', 'bearer', 'digest']  # re-iterable

# Generated at 2026-10-25 08:52:24.677778
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'bearer': object(),
    }

    with mock.patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        choices = _AuthTypeLazyChoices()

        result = iter(choices)
        assert iter(result) is result  # returns an iterator
        assert list(result) == ['basic', 'bearer', 'digest']  # sorted keys
        assert list(choices) == ['basic', 'bearer', 'digest']  # re-iterable

# Generated at 2026-10-25 08:52:26.207321
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 08:52:27.662204
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'bearer': object(),
    }

    with mock.patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        choices = _AuthTypeLazyChoices()

        result = iter(choices)
        assert iter(result) is result  # returns an iterator
        assert list(result) == ['basic', 'bearer', 'digest']  # sorted keys
        assert list(choices) == ['basic', 'bearer', 'digest']  # re-iterable

# Generated at 2026-10-25 08:52:29.125184
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 08:52:30.610254
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'bearer': object(),
    }

    with mock.patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        choices = _AuthTypeLazyChoices()

        result = iter(choices)
        assert iter(result) is result  # returns an iterator
        assert list(result) == ['basic', 'bearer', 'digest']  # sorted keys
        assert list(choices) == ['basic', 'bearer', 'digest']  # re-iterable

# Generated at 2026-10-25 08:52:32.045010
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 08:52:33.476471
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'bearer': object(),
    }

    with mock.patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        choices = _AuthTypeLazyChoices()

        result = iter(choices)
        assert iter(result) is result  # returns an iterator
        assert list(result) == ['basic', 'bearer', 'digest']  # sorted keys
        assert list(choices) == ['basic', 'bearer', 'digest']  # re-iterable

# Generated at 2026-10-25 08:52:49.978566
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 08:52:52.398740
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:52:55.089328
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:52:57.504834
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:52:59.925825
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:53:02.343347
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:53:04.933435
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:53:07.352353
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:53:09.771921
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:53:12.188029
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:53:14.604431
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:53:17.023187
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:53:19.466308
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:53:21.884800
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:53:24.299848
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:53:26.718714
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:53:29.135606
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:53:31.553119
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:53:33.969377
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:53:42.702061
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from unittest import mock

    import httpie.cli.definition as definition

    choices = definition._AuthTypeLazyChoices()
    fake_mapping = {"basic": object(), "custom-auth": object()}

    with mock.patch.object(
        definition.plugin_manager,
        "get_auth_plugin_mapping",
        return_value=fake_mapping,
    ) as mock_get_mapping:
        assert "basic" in choices
        assert "custom-auth" in choices
        assert "digest" not in choices
        assert "unknown-auth" not in choices
        assert "" not in choices
        assert None not in choices

    mock_get_mapping.assert_called()

# Generated at 2026-10-25 08:53:59.292215
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 08:54:00.825686
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'bearer': object(),
    }

    with mock.patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        choices = _AuthTypeLazyChoices()

        result = iter(choices)
        assert iter(result) is result  # returns an iterator
        assert list(result) == ['basic', 'bearer', 'digest']  # sorted keys
        assert list(choices) == ['basic', 'bearer', 'digest']  # re-iterable

# Generated at 2026-10-25 08:54:02.257761
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'bearer': object(),
    }

    with mock.patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        choices = _AuthTypeLazyChoices()

        result = iter(choices)
        assert iter(result) is result  # returns an iterator
        assert list(result) == ['basic', 'bearer', 'digest']  # sorted keys
        assert list(choices) == ['basic', 'bearer', 'digest']  # re-iterable

# Generated at 2026-10-25 08:54:03.757783
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'bearer': object(),
    }

    with mock.patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        choices = _AuthTypeLazyChoices()

        result = iter(choices)
        assert iter(result) is result  # returns an iterator
        assert list(result) == ['basic', 'bearer', 'digest']  # sorted keys
        assert list(choices) == ['basic', 'bearer', 'digest']  # re-iterable

# Generated at 2026-10-25 08:54:06.284333
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:54:09.121311
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:54:11.538914
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:54:13.967869
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:54:16.384562
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:54:18.800625
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:54:21.216375
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:54:23.634618
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:54:26.230901
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:54:28.651180
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:54:31.068270
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:54:33.484294
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:54:35.904594
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:54:38.323799
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:54:40.740531
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:54:57.233679
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()

    fake_mapping = {
        'basic': MagicMock(),
        'digest': MagicMock(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping
    ) as mock_get_mapping:
        # Present keys -> True
        assert ('basic' in choices) is True
        assert ('digest' in choices) is True

        # Absent keys -> False
        assert ('bearer' in choices) is False
        assert ('' in choices) is False
        assert ('BASIC' in choices) is False

        # Delegates to plugin_manager on each check (lazy, no caching)
        assert mock_get_mapping.call_count == 5

    # Empty mapping -> everything False
    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value={}
    ):
        assert ('basic' in choices) is False

    # Reflects updated mapping (proves laziness)
    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value={'bearer': MagicMock()}
    ):
        assert ('bearer' in choices) is True
        assert ('basic' in choices) is False

# Generated at 2026-10-25 08:54:58.690015
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'bearer': object(),
    }

    with mock.patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        choices = _AuthTypeLazyChoices()

        result = iter(choices)
        assert iter(result) is result  # returns an iterator
        assert list(result) == ['basic', 'bearer', 'digest']  # sorted keys
        assert list(choices) == ['basic', 'bearer', 'digest']  # re-iterable

# Generated at 2026-10-25 08:55:00.115796
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 08:55:01.653493
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 08:55:03.190611
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 08:55:04.724582
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 08:55:07.440813
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 08:55:09.027905
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 08:55:17.008162
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 08:55:19.680080
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:55:22.100946
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:55:24.516870
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:55:26.956991
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:55:29.637902
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:55:32.059518
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:55:34.477038
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:55:36.893602
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:55:39.312877
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:55:41.756419
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:55:44.158325
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:55:46.647976
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:55:49.035140
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:55:51.452259
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:55:53.867331
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:55:56.315365
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:55:58.701167
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:56:01.121118
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:56:03.537890
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:56:05.955364
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:56:08.373334
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:56:14.529200
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:56:16.946275
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:56:19.364321
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:56:21.783622
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:56:24.204630
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:56:26.624872
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:56:29.041495
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:56:31.465007
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:56:47.756027
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-25 08:56:56.268107
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    mapping = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value=mapping
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'bearer' not in choices
        assert '' not in choices
        assert get_mapping.call_count == 4


def test__AuthTypeLazyChoices_is_lazy():
    """Mapping is re-read on every check, so late-registered plugins count."""
    choices = _AuthTypeLazyChoices()

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={}
    ):
        assert 'basic' not in choices

    with patch.object(
        plugin_manager, 'get_auth_plugin_mapping', return_value={'basic': 1}
    ):
        assert 'basic' in choices

# Generated at 2026-10-25 08:57:01.869773
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 08:57:03.406339
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 08:57:08.685462
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():
    mapping = {'basic': object(), 'digest': object(), 'custom': object()}

    with patch(
        'httpie.cli.argparser.plugin_manager.get_auth_plugin_mapping',
        return_value=mapping,
    ):
        # Constructor takes no arguments.
        choices = _AuthTypeLazyChoices()

        # __contains__ delegates to the plugin mapping.
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'nope' not in choices

        # __iter__ returns plugin names, sorted.
        assert list(choices) == ['basic', 'custom', 'digest']

        # Lazy: nothing is snapshotted at construction time.
        mapping['later'] = object()
        assert 'later' in choices
        assert list(choices) == ['basic', 'custom', 'digest', 'later']

# Generated at 2026-10-25 08:57:25.248854
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()

    fake_mapping = {
        'basic': MagicMock(),
        'digest': MagicMock(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping
    ) as mock_get_mapping:
        # Present keys -> True
        assert ('basic' in choices) is True
        assert ('digest' in choices) is True

        # Absent keys -> False
        assert ('bearer' in choices) is False
        assert ('' in choices) is False
        assert ('BASIC' in choices) is False

        # Delegates to plugin_manager on each check (lazy, no caching)
        assert mock_get_mapping.call_count == 5

    # Empty mapping -> everything False
    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value={}
    ):
        assert ('basic' in choices) is False

    # Reflects updated mapping (proves laziness)
    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value={'bearer': MagicMock()}
    ):
        assert ('bearer' in choices) is True
        assert ('basic' in choices) is False

# Generated at 2026-10-25 08:57:27.792570
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:57:30.208767
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:57:32.875622
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:57:35.294007
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:58:17.030991
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from httpie.cli.definition import _AuthTypeLazyChoices
    from httpie.plugins.registry import plugin_manager

    choices = _AuthTypeLazyChoices()

    # Built-in auth types must always be recognized.
    assert 'basic' in choices
    assert 'digest' in choices

    # Every registered plugin auth type must be recognized too.
    for key in plugin_manager.get_auth_plugin_mapping():
        assert key in choices

    # Unknown auth types must be rejected.
    assert 'definitely-not-an-auth-type' not in choices

# Generated at 2026-10-25 08:58:26.656200
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'bearer': object(),
    }

    with mock.patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        choices = _AuthTypeLazyChoices()

        result = iter(choices)
        assert iter(result) is result  # returns an iterator
        assert list(result) == ['basic', 'bearer', 'digest']  # sorted keys
        assert list(choices) == ['basic', 'bearer', 'digest']  # re-iterable

# Generated at 2026-10-25 08:58:28.191731
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'bearer': object(),
    }

    with mock.patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        choices = _AuthTypeLazyChoices()

        result = iter(choices)
        assert iter(result) is result  # returns an iterator
        assert list(result) == ['basic', 'bearer', 'digest']  # sorted keys
        assert list(choices) == ['basic', 'bearer', 'digest']  # re-iterable

# Generated at 2026-10-25 08:58:30.611716
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:58:33.030756
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:58:35.772493
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 08:58:40.264679
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():
    fake_mapping = {
        'digest': object(),
        'basic': object(),
        'bearer': object(),
    }

    with mock.patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=fake_mapping,
    ):
        choices = _AuthTypeLazyChoices()

        result = iter(choices)
        assert iter(result) is result  # returns an iterator
        assert list(result) == ['basic', 'bearer', 'digest']  # sorted keys
        assert list(choices) == ['basic', 'bearer', 'digest']  # re-iterable