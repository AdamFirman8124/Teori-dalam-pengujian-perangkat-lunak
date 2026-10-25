

# Generated at 2026-10-24 10:45:12.821069
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

# Generated at 2026-10-24 10:45:44.161321
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch

# Generated at 2026-10-24 10:46:02.980387
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:46:05.398196
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:46:07.816642
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:46:10.236194
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:46:12.654358
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:46:30.337458
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:46:47.488831
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:46:49.906572
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:46:52.321607
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:46:54.740436
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:46:57.156650
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:46:59.577803
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:47:01.994448
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:47:04.410973
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:47:06.969244
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:47:09.384889
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:47:11.801696
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:47:14.219527
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:47:16.642576
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:47:19.055744
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:47:21.473727
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:47:23.889879
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:47:26.352195
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:47:28.770226
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:47:31.187047
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:47:33.610715
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:47:36.039809
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:47:38.457652
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:47:40.877884
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:47:43.297386
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:47:45.715681
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:47:56.763079
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():assert Conversion.get_converter("invalid-mime-no-slash") is None

# Generated at 2026-10-24 10:48:35.911181
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:48:38.332425
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:48:40.753394
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:48:43.175154
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:48:45.791628
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:48:48.201791
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:48:50.619080
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:48:53.036707
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:48:55.454572
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:48:57.874221
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:49:00.292661
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:49:02.711368
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:49:05.129467
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:49:07.548675
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:49:09.963618
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:49:12.381201
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:49:14.796431
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:49:17.213791
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:49:19.630515
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:49:22.048067
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:49:24.467151
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:49:26.882231
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:49:29.297587
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:49:31.716820
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:49:34.136585
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:49:36.554945
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:49:38.973102
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:49:41.390903
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:49:43.806216
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:49:46.224058
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:49:48.638027
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:49:51.054604
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:49:53.479731
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:49:55.896486
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:49:58.316403
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:50:00.734132
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:50:03.266224
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:50:05.685311
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:50:08.102134
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:50:10.521822
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:50:12.940098
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:50:15.358667
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:50:17.779596
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:50:20.197440
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:50:22.614061
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:50:25.032357
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:50:27.447986
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:50:29.869915
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:50:32.285850
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:50:34.706694
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:50:37.124636
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:50:39.553614
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:50:41.972129
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:50:44.388182
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:50:46.806652
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:50:49.225046
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:50:51.641951
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:51:08.151017
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

# Generated at 2026-10-24 10:51:09.585412
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

# Generated at 2026-10-24 10:51:11.017498
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

# Generated at 2026-10-24 10:51:13.988160
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:51:24.028608
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():formatter = Formatting(groups=[])

# Generated at 2026-10-24 10:51:26.450478
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:51:28.864965
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:51:31.281527
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:51:33.701130
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:51:36.121199
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:51:38.539260
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:51:40.958991
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:51:43.374990
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:51:45.791271
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:51:48.210541
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:51:50.628355
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:51:53.047420
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:51:55.463066
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:51:57.880464
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:52:00.296214
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:52:02.710669
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:52:05.126085
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:52:07.542964
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:52:09.961164
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:52:12.376178
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:52:14.794286
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:52:17.210873
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:52:19.626796
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:52:22.042922
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:52:24.463525
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:52:26.876969
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:52:29.295364
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:52:32.102480
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:52:34.517719
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:52:36.932109
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:52:39.348223
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:52:41.763013
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:53:02.531795
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:53:03.966367
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

# Generated at 2026-10-24 10:53:05.414239
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

# Generated at 2026-10-24 10:53:06.773962
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

# Generated at 2026-10-24 10:53:08.153091
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

# Generated at 2026-10-24 10:53:09.750139
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:53:11.135278
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():assert Conversion.get_converter("invalid-mime-no-slash") is None

# Generated at 2026-10-24 10:53:12.483132
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

# Generated at 2026-10-24 10:53:15.169285
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch

# Generated at 2026-10-24 10:53:17.682766
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:53:20.097124
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:53:22.600999
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:53:27.543535
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:53:29.961134
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:53:32.609677
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:53:35.031983
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:53:37.453461
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:53:40.084857
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:53:42.504284
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:53:44.925685
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:53:47.345722
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:53:49.765733
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:53:52.186749
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:53:54.603628
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:53:57.024478
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:53:59.443017
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:54:01.862792
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:54:04.283038
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:54:06.704454
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:54:09.123998
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:54:11.547060
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:54:13.965927
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:54:16.383777
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 10:54:18.803973
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:54:21.221905
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:54:23.643877
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 10:54:26.062706
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:54:28.481977
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:54:30.901278
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 10:54:33.318996
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:54:35.737748
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 10:54:38.155470
# Unit test for method format_body of class Formatting