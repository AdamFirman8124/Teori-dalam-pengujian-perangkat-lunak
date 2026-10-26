

# Generated at 2026-10-25 06:09:31.562657
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:09:34.114041
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:09:36.448314
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:09:38.863990
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:09:41.317172
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:09:43.720308
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:09:46.136554
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:09:48.553243
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:09:50.968764
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:09:53.383717
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:09:55.799630
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:09:58.215456
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:09:59.590198
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

# Generated at 2026-10-25 06:10:00.953426
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

# Generated at 2026-10-25 06:10:02.362904
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

# Generated at 2026-10-25 06:10:03.715535
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

# Generated at 2026-10-25 06:10:05.066970
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

# Generated at 2026-10-25 06:10:06.479116
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

# Generated at 2026-10-25 06:10:07.910638
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

# Generated at 2026-10-25 06:10:09.345412
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

# Generated at 2026-10-25 06:10:10.688987
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

# Generated at 2026-10-25 06:10:12.094021
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

# Generated at 2026-10-25 06:10:13.543704
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

# Generated at 2026-10-25 06:10:16.091182
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:10:18.693234
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:10:21.108875
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:10:23.523288
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:10:26.142301
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:10:28.568037
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:10:30.987058
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:10:33.402091
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:10:35.820748
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:10:38.243468
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:10:40.874487
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:10:43.289614
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:10:45.705517
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:10:48.376503
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:10:50.790996
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:10:53.206479
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:10:55.623118
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:10:58.037877
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:11:00.453858
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:11:02.868496
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:11:05.285733
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:11:07.701124
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:11:10.115984
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:11:12.573945
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:11:15.017324
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:11:17.432184
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:11:19.846861
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:11:21.260808
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

# Generated at 2026-10-25 06:11:22.925283
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

# Generated at 2026-10-25 06:11:36.090813
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

# Generated at 2026-10-25 06:11:38.141348
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

# Generated at 2026-10-25 06:11:39.475292
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

# Generated at 2026-10-25 06:11:40.809864
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

# Generated at 2026-10-25 06:11:42.155703
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

# Generated at 2026-10-25 06:11:43.511492
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

# Generated at 2026-10-25 06:11:44.994794
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

# Generated at 2026-10-25 06:11:47.529863
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:11:49.944219
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:11:52.388269
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:11:54.962343
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:11:57.377958
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:11:59.956312
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:12:02.367375
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:12:04.782451
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:12:07.198489
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:12:08.752955
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

# Generated at 2026-10-25 06:12:10.185248
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

# Generated at 2026-10-25 06:12:11.692822
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

# Generated at 2026-10-25 06:12:13.122428
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

# Generated at 2026-10-25 06:12:14.589476
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

# Generated at 2026-10-25 06:12:16.018101
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

# Generated at 2026-10-25 06:12:17.558371
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

# Generated at 2026-10-25 06:12:18.992008
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

# Generated at 2026-10-25 06:12:20.630824
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

# Generated at 2026-10-25 06:12:22.064203
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

# Generated at 2026-10-25 06:12:23.497426
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

# Generated at 2026-10-25 06:12:25.032937
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

# Generated at 2026-10-25 06:12:26.468320
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

# Generated at 2026-10-25 06:12:27.798877
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

# Generated at 2026-10-25 06:12:30.414494
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:12:32.912902
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:12:35.309657
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:12:37.725700
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:12:40.159564
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:12:42.570342
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:12:44.988584
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:12:47.406580
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:12:49.821591
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:12:52.236574
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:12:54.649662
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:12:57.066742
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:12:59.483217
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:13:01.897864
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:13:04.317147
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:13:06.730604
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:13:09.149326
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:13:11.563858
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:13:13.978687
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:13:16.394632
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:13:25.078362
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

# Generated at 2026-10-25 06:13:26.474857
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

# Generated at 2026-10-25 06:13:27.907429
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

# Generated at 2026-10-25 06:13:29.353908
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

# Generated at 2026-10-25 06:13:30.775066
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

# Generated at 2026-10-25 06:13:32.209098
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

# Generated at 2026-10-25 06:13:33.642466
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

# Generated at 2026-10-25 06:13:35.074032
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

# Generated at 2026-10-25 06:13:36.416126
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

# Generated at 2026-10-25 06:13:40.297211
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:13:42.711619
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:13:45.127199
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:13:47.542900
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:13:50.197644
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:13:52.615518
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:13:55.302079
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:13:57.718089
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:14:00.135229
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:14:02.564219
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:14:04.978217
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:14:07.391225
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:14:09.812224
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:14:12.220200
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:14:14.643222
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:14:17.057237
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:14:19.470967
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:14:21.887228
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:14:24.301222
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:14:26.716221
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:14:29.135643
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:14:31.552646
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:14:33.963650
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:14:36.384653
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:14:40.616492
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

# Generated at 2026-10-25 06:14:42.029284
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

# Generated at 2026-10-25 06:14:46.895475
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

# Generated at 2026-10-25 06:14:48.229217
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

# Generated at 2026-10-25 06:14:49.609557
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

# Generated at 2026-10-25 06:14:50.960725
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

# Generated at 2026-10-25 06:14:52.375142
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

# Generated at 2026-10-25 06:14:53.716094
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

# Generated at 2026-10-25 06:14:55.058918
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

# Generated at 2026-10-25 06:14:56.470714
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

# Generated at 2026-10-25 06:14:57.882356
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

# Generated at 2026-10-25 06:14:59.230819
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

# Generated at 2026-10-25 06:15:11.167948
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:15:13.590042
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:15:16.005873
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:15:18.422784
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:15:20.839690
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:15:23.251698
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:15:25.667439
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:15:28.081646
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:15:30.497473
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:15:33.036712
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:15:35.449213
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:15:37.864697
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:15:40.279808
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:15:42.698650
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:15:45.114108
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:15:47.530033
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:15:49.943872
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:15:52.358516
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:15:54.777272
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:15:57.229209
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:15:59.648464
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:16:02.061781
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:16:04.479022
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:16:06.896912
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:16:09.312585
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:16:14.308462
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:16:32.626160
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:16:34.064782
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

# Generated at 2026-10-25 06:16:52.713791
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

# Generated at 2026-10-25 06:16:54.070944
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

# Generated at 2026-10-25 06:16:55.578105
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

# Generated at 2026-10-25 06:16:56.989937
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

# Generated at 2026-10-25 06:16:58.443990
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

# Generated at 2026-10-25 06:16:59.793285
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

# Generated at 2026-10-25 06:17:01.211281
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

# Generated at 2026-10-25 06:17:02.743953
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

# Generated at 2026-10-25 06:17:04.233840
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

# Generated at 2026-10-25 06:17:05.712894
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

# Generated at 2026-10-25 06:17:43.382922
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:17:45.794145
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:17:48.211340
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 06:17:51.112729
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

# Generated at 2026-10-25 06:17:52.717862
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

# Generated at 2026-10-25 06:17:54.672394
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

# Generated at 2026-10-25 06:17:56.045891
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

# Generated at 2026-10-25 06:17:57.838807
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

# Generated at 2026-10-25 06:17:59.200931
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

# Generated at 2026-10-25 06:18:00.554339
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

# Generated at 2026-10-25 06:18:02.036727
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

# Generated at 2026-10-25 06:18:03.573644
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

# Generated at 2026-10-25 06:19:07.752176
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

# Generated at 2026-10-25 06:19:09.296996
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

# Generated at 2026-10-25 06:19:10.729953
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

# Generated at 2026-10-25 06:19:12.164539
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

# Generated at 2026-10-25 06:19:13.598376
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

# Generated at 2026-10-25 06:19:14.930743
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

# Generated at 2026-10-25 06:19:16.362644
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

# Generated at 2026-10-25 06:19:17.796458
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

# Generated at 2026-10-25 06:19:19.203563
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

# Generated at 2026-10-25 06:19:20.663663
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