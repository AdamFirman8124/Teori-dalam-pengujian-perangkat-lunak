

# Generated at 2026-10-24 12:03:13.757272
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:03:15.190257
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():formatter = Formatting(groups=[])

# Generated at 2026-10-24 12:03:17.934136
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch

# Generated at 2026-10-24 12:03:34.645893
# Unit test for constructor of class Conversion
def test_Conversion():
    # constructor: no args required, creates instance
    conv = Conversion()
    assert isinstance(conv, Conversion)
    assert hasattr(conv, "get_converter")
    assert hasattr(Conversion, "get_converter")

# Generated at 2026-10-24 12:03:37.160298
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:03:39.733561
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:03:42.290326
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:03:44.715906
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:03:47.136199
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:03:49.552084
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:03:52.503705
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch

# Generated at 2026-10-24 12:03:53.855395
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:03:55.206638
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():assert Conversion.get_converter("invalid-mime-no-slash") is None

# Generated at 2026-10-24 12:03:56.868723
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:03:58.406166
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():assert Conversion.get_converter("invalid-mime-no-slash") is None

# Generated at 2026-10-24 12:04:00.154191
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:04:01.601935
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():assert Conversion.get_converter("invalid-mime-no-slash") is None

# Generated at 2026-10-24 12:04:02.997793
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

# Generated at 2026-10-24 12:04:04.344755
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:04:05.716208
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():assert Conversion.get_converter("invalid-mime-no-slash") is None

# Generated at 2026-10-24 12:04:08.454644
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch

# Generated at 2026-10-24 12:04:10.076428
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

# Generated at 2026-10-24 12:04:12.796627
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch

# Generated at 2026-10-24 12:04:14.178535
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

# Generated at 2026-10-24 12:04:16.724748
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:04:19.351063
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:04:21.865908
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:04:24.283340
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:04:26.707202
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:04:29.126866
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:04:31.543224
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:04:33.960971
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:04:36.378730
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:04:38.799969
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:04:41.219676
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:04:43.637485
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:04:46.057754
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:04:48.472119
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:04:50.987289
# Unit test for constructor of class Formatting
def test_Formatting():from httpie.plugins import FormatterPlugin


# Generated at 2026-10-24 12:04:53.736890
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch

# Generated at 2026-10-24 12:05:10.187249
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

# Generated at 2026-10-24 12:05:11.978380
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

# Generated at 2026-10-24 12:05:15.827303
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:05:17.217635
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:05:18.569098
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():formatter = Formatting(groups=[])

# Generated at 2026-10-24 12:05:21.349022
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch

# Generated at 2026-10-24 12:05:37.934405
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:05:40.459314
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:05:42.877480
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:05:45.296482
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:05:47.716853
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:05:50.138040
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:05:52.555092
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:05:55.248553
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:05:56.660983
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():formatter = Formatting(groups=[])

# Generated at 2026-10-24 12:05:58.063428
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

# Generated at 2026-10-24 12:05:59.427020
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

# Generated at 2026-10-24 12:06:15.926701
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:06:17.349760
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():assert Conversion.get_converter("invalid-mime-no-slash") is None

# Generated at 2026-10-24 12:06:33.865448
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:06:36.287226
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:06:38.854357
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:06:41.271809
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:06:43.692566
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:06:46.113920
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:06:48.537604
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:06:50.960190
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:06:53.376764
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:06:55.800687
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:06:58.223532
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:07:00.637421
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:07:03.053988
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:07:05.471526
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:07:07.896677
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:07:10.316004
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:07:11.717152
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():assert Conversion.get_converter("invalid-mime-no-slash") is None

# Generated at 2026-10-24 12:07:28.223201
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:07:29.587354
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():assert Conversion.get_converter("invalid-mime-no-slash") is None

# Generated at 2026-10-24 12:07:30.943283
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

# Generated at 2026-10-24 12:07:33.365995
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:07:35.782225
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:07:38.342883
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:07:40.852192
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:07:43.268427
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:07:45.698640
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:07:48.118010
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:07:50.536527
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:07:52.957285
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:07:55.377737
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:07:57.795797
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:08:00.211415
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:08:02.636471
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:08:05.051748
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:08:07.473748
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:08:09.892264
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:08:12.311610
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:08:14.735991
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:08:17.152715
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:08:19.572386
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:08:21.990290
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:08:24.410634
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:08:26.825415
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:08:29.241048
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:08:31.657962
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:08:34.087797
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:08:36.506677
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:08:38.923347
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:08:41.341479
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:08:43.766434
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:08:46.186823
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:08:48.610319
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:08:51.029464
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:08:53.448156
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:08:55.864928
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:08:58.283750
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:09:00.703904
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:09:03.862275
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:09:22.266385
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:09:25.071354
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch

# Generated at 2026-10-24 12:09:27.945358
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:09:29.399454
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():formatter = Formatting(groups=[])

# Generated at 2026-10-24 12:09:32.084417
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:09:34.502008
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:09:36.920508
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:09:39.993512
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:09:42.414923
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:09:44.861915
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:09:47.412773
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:09:49.838437
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:09:52.257119
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:09:54.687676
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:09:57.120200
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:09:59.545634
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:10:01.971881
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:10:27.113533
# Unit test for constructor of class Formatting
def test_Formatting():from httpie.plugins import FormatterPlugin


# Generated at 2026-10-24 12:10:28.502695
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:10:31.006337
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:10:33.430046
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:10:35.849760
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:10:38.266847
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:10:40.681867
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:10:43.261283
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:10:45.684035
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:10:48.101506
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:10:50.522222
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:10:52.940957
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:10:55.360522
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:10:57.784999
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:11:00.197507
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:11:02.617657
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:11:05.036852
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:11:07.455829
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:11:09.874121
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 12:11:13.034277
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:11:15.465639
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:11:17.887174
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:11:20.304524
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:11:22.722723
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:11:25.141505
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:11:27.564190
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:11:29.978104
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:11:32.397298
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:12:09.516292
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:12:12.080357
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:12:14.496448
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:12:16.915968
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:12:19.333077
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:12:21.750728
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:12:24.168205
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:12:26.585113
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:12:29.003756
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:12:31.421215
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:12:33.852424
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:12:36.267498
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:12:38.700252
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:12:41.115906
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:12:43.531536
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 12:12:45.947731
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:12:48.362635
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:12:50.779867
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:12:53.197814
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:12:55.616320
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:12:58.034810
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:13:02.726758
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:13:05.145075
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:13:07.561012
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 12:13:09.979070
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:13:12.395092
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 12:13:14.812343
# Unit test for constructor of class Formatting