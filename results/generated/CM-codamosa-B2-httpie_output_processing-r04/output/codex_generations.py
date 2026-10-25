

# Generated at 2026-10-24 11:49:55.444611
# Unit test for function is_valid_mime
def test_is_valid_mime():
    valid = [
        "text/plain",
        "text/html",
        "application/json",
        "image/png",
        "a/b",
    ]
    for mime in valid:
        assert module_0.is_valid_mime(mime)

    invalid = [
        None,
        "",
        "text",
        "text/",
        "/html",
        "/",
        "text/html/extra",
        "text//html",
    ]
    for mime in invalid:
        assert not module_0.is_valid_mime(mime)

# Generated at 2026-10-24 11:49:58.125758
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch

# Generated at 2026-10-24 11:50:00.546157
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:50:02.964573
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:50:05.382935
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:50:07.809837
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:50:10.221957
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:50:12.640365
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:50:15.451252
# Unit test for constructor of class Conversion

# Generated at 2026-10-24 11:50:17.874117
# Unit test for constructor of class Conversion

# Generated at 2026-10-24 11:50:20.292127
# Unit test for constructor of class Conversion

# Generated at 2026-10-24 11:50:22.707735
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 11:50:25.124516
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 11:50:27.541978
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 11:50:29.957790
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:50:32.374377
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:50:34.791175
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:50:37.208337
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:50:39.627146
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:50:42.048067
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:50:44.464674
# Unit test for function is_valid_mime

# Generated at 2026-10-24 11:50:46.881435
# Unit test for function is_valid_mime

# Generated at 2026-10-24 11:50:49.301347
# Unit test for function is_valid_mime

# Generated at 2026-10-24 11:50:51.719561
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:50:54.136493
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:50:56.553426
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:50:58.971053
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 11:51:01.595607
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 11:51:04.459472
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 11:51:05.813348
# Unit test for constructor of class Formatting
def test_Formatting():
    mock_env = MagicMock()
    kwargs = {"opt": "value"}

    EnabledCls, enabled_inst = make_plugin_cls(enabled=True)
    DisabledCls, disabled_inst = make_plugin_cls(enabled=False)
    OtherEnabledCls, other_enabled_inst = make_plugin_cls(enabled=True)

    grouped = {
        "group1": [EnabledCls, DisabledCls],
        "group2": [OtherEnabledCls],
    }

    with patch.object(
        plugin_manager, "get_formatters_grouped", return_value=grouped
    ):
        # 1. filters by `enabled` and forwards env/kwargs
        f = Formatting(groups=["group1"], env=mock_env, **kwargs)
        assert f.enabled_plugins == [enabled_inst]
        EnabledCls.assert_called_once_with(env=mock_env, **kwargs)
        DisabledCls.assert_called_once_with(env=mock_env, **kwargs)

        # 2. empty groups -> no plugins
        f_empty = Formatting(groups=[], env=mock_env)
        assert f_empty.enabled_plugins == []

        # 3. preserves group order then declaration order
        EnabledCls.reset_mock()
        OtherEnabledCls.reset

# Generated at 2026-10-24 11:51:07.225017
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:51:08.662789
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():assert Conversion.get_converter("invalid-mime-no-slash") is None

# Generated at 2026-10-24 11:51:11.524059
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:51:35.386858
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:51:37.812234
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:51:40.431366
# Unit test for function is_valid_mime

# Generated at 2026-10-24 11:51:42.846932
# Unit test for function is_valid_mime

# Generated at 2026-10-24 11:51:45.638164
# Unit test for function is_valid_mime

# Generated at 2026-10-24 11:51:48.065979
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:51:50.495000
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:51:52.924744
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:51:55.485921
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:51:57.903489
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:52:00.322102
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:52:02.741267
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:52:05.154151
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:52:07.576388
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:52:09.994379
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:52:12.412077
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:52:14.832104
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:52:17.250999
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 11:52:19.668193
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 11:52:22.085103
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 11:52:24.503386
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 11:52:26.919646
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 11:52:29.337448
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 11:52:31.756059
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:52:34.172387
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:52:36.591617
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:52:39.008819
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:52:41.428645
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:52:43.849971
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:52:46.267169
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:52:48.680881
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:52:51.106493
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:52:53.521567
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:52:55.940286
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:53:21.031659
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:53:22.496746
# Unit test for constructor of class Formatting
def test_Formatting():
    mock_env = MagicMock()
    kwargs = {"opt": "value"}

    EnabledCls, enabled_inst = make_plugin_cls(enabled=True)
    DisabledCls, disabled_inst = make_plugin_cls(enabled=False)
    OtherEnabledCls, other_enabled_inst = make_plugin_cls(enabled=True)

    grouped = {
        "group1": [EnabledCls, DisabledCls],
        "group2": [OtherEnabledCls],
    }

    with patch.object(
        plugin_manager, "get_formatters_grouped", return_value=grouped
    ):
        # 1. filters by `enabled` and forwards env/kwargs
        f = Formatting(groups=["group1"], env=mock_env, **kwargs)
        assert f.enabled_plugins == [enabled_inst]
        EnabledCls.assert_called_once_with(env=mock_env, **kwargs)
        DisabledCls.assert_called_once_with(env=mock_env, **kwargs)

        # 2. empty groups -> no plugins
        f_empty = Formatting(groups=[], env=mock_env)
        assert f_empty.enabled_plugins == []

        # 3. preserves group order then declaration order
        EnabledCls.reset_mock()
        OtherEnabledCls.reset

# Generated at 2026-10-24 11:53:25.319711
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch

# Generated at 2026-10-24 11:53:28.097414
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:53:30.515018
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:53:33.032884
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:53:35.448523
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:53:37.866131
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:53:40.283458
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:53:42.701435
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:53:45.122097
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:53:47.542150
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:53:49.971948
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:53:52.390580
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:53:54.808341
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:53:57.228474
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:53:59.648206
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:54:02.063793
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:54:04.489113
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:54:06.907507
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:54:09.325683
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:54:11.755986
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:54:14.177760
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:54:16.597087
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:54:19.015360
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:54:48.923715
# Unit test for constructor of class Formatting
def test_Formatting():from httpie.plugins import FormatterPlugin


# Generated at 2026-10-24 11:54:51.685184
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch

# Generated at 2026-10-24 11:54:53.120597
# Unit test for constructor of class Formatting
def test_Formatting():
    mock_env = MagicMock()
    kwargs = {"opt": "value"}

    EnabledCls, enabled_inst = make_plugin_cls(enabled=True)
    DisabledCls, disabled_inst = make_plugin_cls(enabled=False)
    OtherEnabledCls, other_enabled_inst = make_plugin_cls(enabled=True)

    grouped = {
        "group1": [EnabledCls, DisabledCls],
        "group2": [OtherEnabledCls],
    }

    with patch.object(
        plugin_manager, "get_formatters_grouped", return_value=grouped
    ):
        # 1. filters by `enabled` and forwards env/kwargs
        f = Formatting(groups=["group1"], env=mock_env, **kwargs)
        assert f.enabled_plugins == [enabled_inst]
        EnabledCls.assert_called_once_with(env=mock_env, **kwargs)
        DisabledCls.assert_called_once_with(env=mock_env, **kwargs)

        # 2. empty groups -> no plugins
        f_empty = Formatting(groups=[], env=mock_env)
        assert f_empty.enabled_plugins == []

        # 3. preserves group order then declaration order
        EnabledCls.reset_mock()
        OtherEnabledCls.reset

# Generated at 2026-10-24 11:55:09.607139
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:55:11.044429
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():assert Conversion.get_converter("invalid-mime-no-slash") is None

# Generated at 2026-10-24 11:55:13.811126
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 11:55:16.398510
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 11:55:19.005660
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 11:55:21.734137
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:55:24.343876
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:55:25.706779
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():formatter = Formatting(groups=[])

# Generated at 2026-10-24 11:55:42.382698
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    from unittest.mock import MagicMock, patch

    # 1. Invalid MIME -> None, should not query registry
    for bad_mime in [None, "", "invalid", "text/", "/json", "text/html; charset=utf-8"]:
        with patch.object(plugin_manager, "get_converters") as mock_get:
            assert Conversion.get_converter(bad_mime) is None
            mock_get.assert_not_called()

    # 2. Valid MIME but no converters registered -> None
    with patch.object(plugin_manager, "get_converters", return_value=[]):
        assert Conversion.get_converter("application/json") is None

    # 3. Valid MIME but no converter supports it -> None
    mock_cls_unsupported = MagicMock()
    mock_cls_unsupported.supports.return_value = False
    with patch.object(plugin_manager, "get_converters", return_value=[mock_cls_unsupported]):
        assert Conversion.get_converter("application/json") is None
        mock_cls_unsupported.supports.assert_called_once_with("application/json")
        mock_cls_unsupported.assert_not_called()

    # 4. Valid MIME with supporting converter -> returns instance
    mock_instance = MagicMock(spec=ConverterPlugin)

# Generated at 2026-10-24 11:55:45.165246
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch

# Generated at 2026-10-24 11:55:47.923254
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:55:49.440028
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():formatter = Formatting(groups=[])

# Generated at 2026-10-24 11:56:05.964590
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:56:07.364490
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():assert Conversion.get_converter("invalid-mime-no-slash") is None

# Generated at 2026-10-24 11:56:24.016169
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:56:25.396408
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():assert Conversion.get_converter("invalid-mime-no-slash") is None

# Generated at 2026-10-24 11:56:28.458292
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch

# Generated at 2026-10-24 11:56:31.207164
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch

# Generated at 2026-10-24 11:56:34.248090
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch

# Generated at 2026-10-24 11:56:37.364898
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch

# Generated at 2026-10-24 11:56:40.540171
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch

# Generated at 2026-10-24 11:56:42.277385
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:56:43.621540
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():assert Conversion.get_converter("invalid-mime-no-slash") is None

# Generated at 2026-10-24 11:56:46.579334
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:56:48.118831
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():formatter = Formatting(groups=[])

# Generated at 2026-10-24 11:57:04.505883
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:57:05.910770
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():assert Conversion.get_converter("invalid-mime-no-slash") is None

# Generated at 2026-10-24 11:57:08.680568
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch

# Generated at 2026-10-24 11:57:10.132524
# Unit test for constructor of class Formatting
def test_Formatting():
    mock_env = MagicMock()
    kwargs = {"opt": "value"}

    EnabledCls, enabled_inst = make_plugin_cls(enabled=True)
    DisabledCls, disabled_inst = make_plugin_cls(enabled=False)
    OtherEnabledCls, other_enabled_inst = make_plugin_cls(enabled=True)

    grouped = {
        "group1": [EnabledCls, DisabledCls],
        "group2": [OtherEnabledCls],
    }

    with patch.object(
        plugin_manager, "get_formatters_grouped", return_value=grouped
    ):
        # 1. filters by `enabled` and forwards env/kwargs
        f = Formatting(groups=["group1"], env=mock_env, **kwargs)
        assert f.enabled_plugins == [enabled_inst]
        EnabledCls.assert_called_once_with(env=mock_env, **kwargs)
        DisabledCls.assert_called_once_with(env=mock_env, **kwargs)

        # 2. empty groups -> no plugins
        f_empty = Formatting(groups=[], env=mock_env)
        assert f_empty.enabled_plugins == []

        # 3. preserves group order then declaration order
        EnabledCls.reset_mock()
        OtherEnabledCls.reset

# Generated at 2026-10-24 11:57:13.909315
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch

# Generated at 2026-10-24 11:57:16.699020
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 11:57:19.202740
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 11:57:21.850944
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 11:57:24.380395
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 11:57:26.801093
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 11:57:29.524247
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 11:57:30.880414
# Unit test for constructor of class Formatting
def test_Formatting():
    mock_env = MagicMock()
    kwargs = {"opt": "value"}

    EnabledCls, enabled_inst = make_plugin_cls(enabled=True)
    DisabledCls, disabled_inst = make_plugin_cls(enabled=False)
    OtherEnabledCls, other_enabled_inst = make_plugin_cls(enabled=True)

    grouped = {
        "group1": [EnabledCls, DisabledCls],
        "group2": [OtherEnabledCls],
    }

    with patch.object(
        plugin_manager, "get_formatters_grouped", return_value=grouped
    ):
        # 1. filters by `enabled` and forwards env/kwargs
        f = Formatting(groups=["group1"], env=mock_env, **kwargs)
        assert f.enabled_plugins == [enabled_inst]
        EnabledCls.assert_called_once_with(env=mock_env, **kwargs)
        DisabledCls.assert_called_once_with(env=mock_env, **kwargs)

        # 2. empty groups -> no plugins
        f_empty = Formatting(groups=[], env=mock_env)
        assert f_empty.enabled_plugins == []

        # 3. preserves group order then declaration order
        EnabledCls.reset_mock()
        OtherEnabledCls.reset

# Generated at 2026-10-24 11:57:33.732121
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch

# Generated at 2026-10-24 11:57:35.135097
# Unit test for constructor of class Formatting
def test_Formatting():
    mock_env = MagicMock()
    kwargs = {"opt": "value"}

    EnabledCls, enabled_inst = make_plugin_cls(enabled=True)
    DisabledCls, disabled_inst = make_plugin_cls(enabled=False)
    OtherEnabledCls, other_enabled_inst = make_plugin_cls(enabled=True)

    grouped = {
        "group1": [EnabledCls, DisabledCls],
        "group2": [OtherEnabledCls],
    }

    with patch.object(
        plugin_manager, "get_formatters_grouped", return_value=grouped
    ):
        # 1. filters by `enabled` and forwards env/kwargs
        f = Formatting(groups=["group1"], env=mock_env, **kwargs)
        assert f.enabled_plugins == [enabled_inst]
        EnabledCls.assert_called_once_with(env=mock_env, **kwargs)
        DisabledCls.assert_called_once_with(env=mock_env, **kwargs)

        # 2. empty groups -> no plugins
        f_empty = Formatting(groups=[], env=mock_env)
        assert f_empty.enabled_plugins == []

        # 3. preserves group order then declaration order
        EnabledCls.reset_mock()
        OtherEnabledCls.reset

# Generated at 2026-10-24 11:57:51.601186
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:57:52.956976
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():assert Conversion.get_converter("invalid-mime-no-slash") is None

# Generated at 2026-10-24 11:57:54.366885
# Unit test for constructor of class Formatting
def test_Formatting():
    mock_env = MagicMock()
    kwargs = {"opt": "value"}

    EnabledCls, enabled_inst = make_plugin_cls(enabled=True)
    DisabledCls, disabled_inst = make_plugin_cls(enabled=False)
    OtherEnabledCls, other_enabled_inst = make_plugin_cls(enabled=True)

    grouped = {
        "group1": [EnabledCls, DisabledCls],
        "group2": [OtherEnabledCls],
    }

    with patch.object(
        plugin_manager, "get_formatters_grouped", return_value=grouped
    ):
        # 1. filters by `enabled` and forwards env/kwargs
        f = Formatting(groups=["group1"], env=mock_env, **kwargs)
        assert f.enabled_plugins == [enabled_inst]
        EnabledCls.assert_called_once_with(env=mock_env, **kwargs)
        DisabledCls.assert_called_once_with(env=mock_env, **kwargs)

        # 2. empty groups -> no plugins
        f_empty = Formatting(groups=[], env=mock_env)
        assert f_empty.enabled_plugins == []

        # 3. preserves group order then declaration order
        EnabledCls.reset_mock()
        OtherEnabledCls.reset

# Generated at 2026-10-24 11:57:55.752694
# Unit test for constructor of class Formatting
def test_Formatting():
    mock_env = MagicMock()
    kwargs = {"opt": "value"}

    EnabledCls, enabled_inst = make_plugin_cls(enabled=True)
    DisabledCls, disabled_inst = make_plugin_cls(enabled=False)
    OtherEnabledCls, other_enabled_inst = make_plugin_cls(enabled=True)

    grouped = {
        "group1": [EnabledCls, DisabledCls],
        "group2": [OtherEnabledCls],
    }

    with patch.object(
        plugin_manager, "get_formatters_grouped", return_value=grouped
    ):
        # 1. filters by `enabled` and forwards env/kwargs
        f = Formatting(groups=["group1"], env=mock_env, **kwargs)
        assert f.enabled_plugins == [enabled_inst]
        EnabledCls.assert_called_once_with(env=mock_env, **kwargs)
        DisabledCls.assert_called_once_with(env=mock_env, **kwargs)

        # 2. empty groups -> no plugins
        f_empty = Formatting(groups=[], env=mock_env)
        assert f_empty.enabled_plugins == []

        # 3. preserves group order then declaration order
        EnabledCls.reset_mock()
        OtherEnabledCls.reset

# Generated at 2026-10-24 11:57:58.660419
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:58:00.034066
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():formatter = Formatting(groups=[])

# Generated at 2026-10-24 11:58:06.055860
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 11:58:08.475201
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 11:58:10.896105
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 11:58:13.316625
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:58:15.737933
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:58:18.159558
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:58:20.582573
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:58:23.007625
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:58:25.421479
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:58:28.073428
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:58:30.491093
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:58:38.481193
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # An invalid MIME type must never yield a converter
    assert Conversion.get_converter('not-a-mime') is None
    assert Conversion.get_converter('') is None
    # A valid MIME type either returns a ConverterPlugin or None
    result = Conversion.get_converter('application/json')
    assert result is None or isinstance(result, ConverterPlugin)

# Generated at 2026-10-24 11:58:41.372151
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 11:58:42.805676
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():formatter = Formatting(groups=[])

# Generated at 2026-10-24 11:58:59.393938
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:59:00.826395
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():assert Conversion.get_converter("invalid-mime-no-slash") is None

# Generated at 2026-10-24 11:59:17.489552
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:59:18.953495
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():assert Conversion.get_converter("invalid-mime-no-slash") is None

# Generated at 2026-10-24 11:59:20.488260
# Unit test for constructor of class Formatting
def test_Formatting():
    mock_env = MagicMock()
    kwargs = {"opt": "value"}

    EnabledCls, enabled_inst = make_plugin_cls(enabled=True)
    DisabledCls, disabled_inst = make_plugin_cls(enabled=False)
    OtherEnabledCls, other_enabled_inst = make_plugin_cls(enabled=True)

    grouped = {
        "group1": [EnabledCls, DisabledCls],
        "group2": [OtherEnabledCls],
    }

    with patch.object(
        plugin_manager, "get_formatters_grouped", return_value=grouped
    ):
        # 1. filters by `enabled` and forwards env/kwargs
        f = Formatting(groups=["group1"], env=mock_env, **kwargs)
        assert f.enabled_plugins == [enabled_inst]
        EnabledCls.assert_called_once_with(env=mock_env, **kwargs)
        DisabledCls.assert_called_once_with(env=mock_env, **kwargs)

        # 2. empty groups -> no plugins
        f_empty = Formatting(groups=[], env=mock_env)
        assert f_empty.enabled_plugins == []

        # 3. preserves group order then declaration order
        EnabledCls.reset_mock()
        OtherEnabledCls.reset

# Generated at 2026-10-24 11:59:23.009392
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:59:25.590346
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:59:28.015399
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 11:59:30.437540
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:59:32.859815
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 11:59:35.513975
# Unit test for constructor of class Formatting
def test_Formatting():from httpie.plugins import FormatterPlugin
