

# Generated at 2026-10-25 01:01:01.080668
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:01:03.495652
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:01:05.912079
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:01:08.338134
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:01:10.753259
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:01:13.168695
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:01:15.586672
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:01:17.999939
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:01:20.416043
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:01:22.831007
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:01:25.246407
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:01:27.675449
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:01:30.092073
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:01:32.509381
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:01:34.924844
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:01:37.341309
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:01:52.746366
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-25 01:02:00.632140
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:02:06.390704
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():from unittest.mock import patch


# Generated at 2026-10-25 01:02:21.005271
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

# Generated at 2026-10-25 01:02:23.553385
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:02:25.968044
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:02:28.382161
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:02:30.797742
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:02:33.213333
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:02:35.629027
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:02:38.042671
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:02:47.223500
# Unit test for method __iter__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___iter__():from unittest.mock import patch


# Generated at 2026-10-25 01:02:48.598885
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

# Generated at 2026-10-25 01:02:55.928820
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:03:01.300778
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():from unittest.mock import patch


# Generated at 2026-10-25 01:03:08.831064
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:03:11.248763
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:03:13.666572
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:03:16.080185
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:03:18.652659
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:03:21.175958
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:03:23.591526
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:03:26.005391
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:03:28.420813
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:03:30.835904
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:03:33.252328
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:03:35.667087
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:03:38.244079
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:03:40.655821
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:03:43.072842
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:03:45.490895
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:03:51.526397
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():from unittest.mock import patch


# Generated at 2026-10-25 01:03:52.864653
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

# Generated at 2026-10-25 01:04:10.066266
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

# Generated at 2026-10-25 01:04:11.500899
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

# Generated at 2026-10-25 01:04:18.258063
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:04:20.773861
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:04:23.191061
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:04:25.607005
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:04:28.022189
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:04:30.439130
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:04:32.853158
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:04:35.268204
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:04:37.683162
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:04:40.098142
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:04:42.512842
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:04:54.210520
# Unit test for constructor of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices():obj = _AuthTypeLazyChoices()

# Generated at 2026-10-25 01:04:55.546680
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

# Generated at 2026-10-25 01:05:03.213635
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:05:08.025043
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():from unittest.mock import patch


# Generated at 2026-10-25 01:05:09.404775
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

# Generated at 2026-10-25 01:05:15.149784
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    from unittest.mock import patch

    auth_plugins = {
        'basic': object(),
        'digest': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=auth_plugins,
    ) as get_auth_plugin_mapping:
        choices = _AuthTypeLazyChoices()

        assert 'basic' in choices
        assert 'unknown' not in choices
        assert get_auth_plugin_mapping.call_count == 2

# Generated at 2026-10-25 01:05:20.824355
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:05:23.342141
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:05:25.758497
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:05:28.172877
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:05:30.587115
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:05:33.003556
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:05:35.416400
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:05:37.832693
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:05:40.247601
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:05:42.664378
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:05:45.081831
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:05:47.498599
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:05:49.914249
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:05:52.328963
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:05:54.744808
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:05:57.159923
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:05:59.574225
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:06:01.989737
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:06:04.406075
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:06:06.820690
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:06:09.235029
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:06:11.649373
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:06:14.064437
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:06:16.479395
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:06:17.813860
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

# Generated at 2026-10-25 01:06:19.194077
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

# Generated at 2026-10-25 01:06:20.542747
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

# Generated at 2026-10-25 01:06:21.902851
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

# Generated at 2026-10-25 01:06:27.591020
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:06:33.862997
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():from unittest.mock import patch


# Generated at 2026-10-25 01:06:35.228854
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

# Generated at 2026-10-25 01:06:36.569300
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

# Generated at 2026-10-25 01:06:38.346473
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

# Generated at 2026-10-25 01:06:39.692421
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

# Generated at 2026-10-25 01:06:41.071812
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

# Generated at 2026-10-25 01:06:42.475946
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

# Generated at 2026-10-25 01:06:48.479393
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:06:50.899359
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:06:53.314279
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:06:55.729271
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:06:58.145980
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:07:00.561427
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:07:02.976748
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:07:05.404045
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:07:07.819146
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:07:10.233839
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:07:12.649475
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:07:15.071368
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:07:17.487246
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:07:19.907684
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:07:25.138191
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():choices = _AuthTypeLazyChoices()

# Generated at 2026-10-25 01:07:26.491618
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

# Generated at 2026-10-25 01:07:28.478711
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

# Generated at 2026-10-25 01:07:29.823824
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

# Generated at 2026-10-25 01:07:31.147646
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

# Generated at 2026-10-25 01:07:32.474696
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

# Generated at 2026-10-25 01:07:40.606579
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    choices = _AuthTypeLazyChoices()
    auth_plugins = {'basic': object(), 'digest': object()}

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=auth_plugins,
    ) as get_mapping:
        assert 'basic' in choices
        assert 'digest' in choices
        assert 'unknown' not in choices

    assert get_mapping.call_count == 3

# Generated at 2026-10-25 01:07:42.035809
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

# Generated at 2026-10-25 01:07:48.487161
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():
    auth_plugins = {
        'basic': object(),
        'digest': object(),
    }

    with patch.object(
        plugin_manager,
        'get_auth_plugin_mapping',
        return_value=auth_plugins,
    ) as get_auth_plugin_mapping:
        choices = _AuthTypeLazyChoices()

        assert 'basic' in choices
        assert 'digest' in choices
        assert 'unknown' not in choices

    assert get_auth_plugin_mapping.call_count == 3

# Generated at 2026-10-25 01:07:49.818982
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

# Generated at 2026-10-25 01:07:51.154733
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

# Generated at 2026-10-25 01:07:53.704977
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:07:56.234463
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:07:58.759213
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:08:04.680467
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:08:07.094504
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:08:09.511980
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:08:12.032655
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:08:14.448635
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:08:16.868989
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:08:19.297317
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:08:21.717405
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:08:29.225394
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():from unittest.mock import patch


# Generated at 2026-10-25 01:08:30.676218
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

# Generated at 2026-10-25 01:08:36.511403
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:08:42.760312
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():from unittest.mock import patch


# Generated at 2026-10-25 01:08:50.235622
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:08:58.666654
# Unit test for method __contains__ of class _AuthTypeLazyChoices
def test__AuthTypeLazyChoices___contains__():from unittest.mock import patch


# Generated at 2026-10-25 01:09:00.037869
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

# Generated at 2026-10-25 01:09:02.712020
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:09:05.122185
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:09:07.537143
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:09:10.060241
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:09:12.474309
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:09:14.889381
# Unit test for method __iter__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:09:17.315382
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:09:19.741325
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:09:22.155500
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:09:29.042991
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

# Generated at 2026-10-25 01:09:30.477587
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

# Generated at 2026-10-25 01:09:31.802965
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

# Generated at 2026-10-25 01:09:33.126025
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

# Generated at 2026-10-25 01:09:34.450583
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

# Generated at 2026-10-25 01:09:35.788789
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

# Generated at 2026-10-25 01:09:37.110736
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

# Generated at 2026-10-25 01:09:38.439394
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

# Generated at 2026-10-25 01:09:39.781846
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

# Generated at 2026-10-25 01:09:41.102247
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

# Generated at 2026-10-25 01:09:59.107444
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:10:01.523696
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:10:03.950792
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:10:06.376319
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:10:08.948177
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:10:11.363251
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:10:13.778237
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:10:16.348234
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:10:18.763818
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:10:21.288878
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:10:23.706118
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:10:26.122195
# Unit test for constructor of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:10:28.537351
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:10:30.952754
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:10:33.367129
# Unit test for method __contains__ of class _AuthTypeLazyChoices

# Generated at 2026-10-25 01:10:34.784491
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

# Generated at 2026-10-25 01:10:36.525183
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

# Generated at 2026-10-25 01:10:37.959089
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

# Generated at 2026-10-25 01:10:39.392876
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

# Generated at 2026-10-25 01:10:40.826711
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