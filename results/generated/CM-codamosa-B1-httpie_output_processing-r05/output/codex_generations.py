

# Generated at 2026-10-24 20:30:49.431325
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:30:52.071441
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:30:54.857755
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:31:18.078119
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():calls = []


# Generated at 2026-10-24 20:31:36.203098
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.plugins import FormatterPlugin

    class DummyFormatterPlugin(FormatterPlugin):
        group_name = 'format'

        def module_0.format_headers(self, headers: str) -> str:
            return headers + '\nX-Dummy-Header: dummy_value'

    original_plugins = list(plugin_manager)
    plugin_manager.register(DummyFormatterPlugin)
    try:
        formatting = Formatting(groups=['format'], env=Environment())
        assert len(formatting.enabled_plugins) == 1
        assert isinstance(formatting.enabled_plugins[0], DummyFormatterPlugin)

        headers = 'Content-Type: application/json\nContent-Length: 42'
        expected = headers + '\nX-Dummy-Header: dummy_value'
        assert formatting.format_headers(headers) == expected

        # With no groups enabled, headers must pass through unchanged.
        assert Formatting(groups=[], env=Environment()).format_headers(headers) == headers

        # Only enabled plugins are chained.
        class DisabledFormatterPlugin(DummyFormatterPlugin):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.enabled = False

        plugin_manager.register(DisabledFormatterPlugin)
        try:
            formatting = Formatting(groups=['format'], env=Environment())
            assert len(formatting.enabled_plugins) == 1  # disabled plugin excluded
            assert formatting.format_headers(headers) == expected
        finally:
            plugin_manager.unregister(DisabledFormatterPlugin)
    finally:
        plugin_manager.unregister(DummyFormatterPlugin)

    assert list(plugin_manager) == original_plugins

# Generated at 2026-10-24 20:31:38.624009
# Unit test for constructor of class Conversion

# Generated at 2026-10-24 20:31:41.041361
# Unit test for constructor of class Conversion

# Generated at 2026-10-24 20:31:43.457429
# Unit test for constructor of class Conversion

# Generated at 2026-10-24 20:31:46.052407
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:31:48.466265
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:31:50.882639
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:31:53.300056
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:31:55.716421
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:31:58.134278
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:32:00.553246
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 20:32:02.969589
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 20:32:05.387298
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 20:32:07.806196
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:32:10.223190
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:32:12.639065
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:32:15.054634
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 20:32:17.473060
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 20:32:19.888888
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 20:32:22.304942
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 20:32:24.724984
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 20:32:27.197764
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 20:32:29.564108
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 20:32:31.980715
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 20:32:34.400067
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 20:32:36.816455
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 20:32:39.233863
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 20:32:41.648352
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 20:32:44.064892
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 20:32:46.480917
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 20:32:48.896078
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 20:32:51.314850
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:32:53.732023
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:32:56.150911
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:32:58.567647
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:33:00.986592
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:33:03.402729
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:33:05.850146
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:33:08.234499
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:33:10.650156
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:33:13.065515
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 20:33:15.482451
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 20:33:17.898226
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 20:33:20.314854
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:33:22.732498
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:33:25.148690
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:33:27.564333
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:33:29.986316
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:33:32.405270
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:33:34.822583
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:33:37.239049
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:33:39.658758
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:33:42.074000
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:33:44.490902
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:33:46.908863
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:33:49.327161
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:33:51.744382
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:33:57.620530
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():result = Conversion.get_converter("invalid-mime")

# Generated at 2026-10-24 20:34:23.627470
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    unsupported_converter = Mock()
    unsupported_converter.supports.return_value = False

    expected_converter = Mock()
    supported_converter = Mock(return_value=expected_converter)
    supported_converter.supports.return_value = True

    with patch.object(
        plugin_manager,
        "get_converters",
        return_value=[unsupported_converter, supported_converter],
    ) as get_converters:
        result = Conversion.get_converter("application/json")

    assert result is expected_converter
    get_converters.assert_called_once_with()
    unsupported_converter.supports.assert_called_once_with("application/json")
    supported_converter.supports.assert_called_once_with("application/json")
    supported_converter.assert_called_once_with("application/json")

# Generated at 2026-10-24 20:34:26.205456
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:34:28.625771
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:34:31.043817
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:34:33.459744
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 20:34:35.877770
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 20:34:38.293830
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 20:34:40.709348
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 20:34:43.126151
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 20:34:45.545261
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 20:34:47.960840
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:34:50.378255
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:34:52.796423
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:34:55.212371
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:34:57.632837
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:35:00.052922
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:35:02.469997
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:35:04.886085
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:35:07.314024
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:35:09.755862
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:35:12.171980
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:35:14.590225
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:35:17.005033
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:35:19.420525
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:35:21.840614
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:35:24.256131
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 20:35:26.672317
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 20:35:29.089169
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 20:35:31.505421
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:35:33.922444
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:35:36.340214
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:35:46.776310
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import MagicMock, patch


# Generated at 2026-10-24 20:36:17.497243
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import Mock


def test_Conversion_get_converter(monkeypatch):
    mime = "application/json"
    converter_instance = Mock(spec=ConverterPlugin)

    unsupported_converter = Mock()
    unsupported_converter.supports.return_value = False

    supported_converter = Mock()
    supported_converter.supports.return_value = True
    supported_converter.return_value = converter_instance

    get_converters = Mock(
        return_value=[unsupported_converter, supported_converter]
    )
    monkeypatch.setattr(plugin_manager, "get_converters", get_converters)

    result = Conversion.get_converter(mime)

    assert result is converter_instance
    get_converters.assert_called_once_with()
    unsupported_converter.supports.assert_called_once_with(mime)
    supported_converter.supports.assert_called_once_with(mime)
    supported_converter.assert_called_once_with(mime)

    # Invalid MIME types should not query the plugin registry.
    get_converters.reset_mock()
    assert Conversion.get_converter("invalid-mime") is None
    get_converters.assert_not_called()

# Generated at 2026-10-24 20:36:19.916887
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:36:22.335513
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:36:24.751667
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:36:27.170561
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:36:29.591067
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:36:32.007342
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:36:34.424444
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:36:36.842283
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:36:39.258442
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:36:41.673396
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:36:44.088503
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:36:46.506542
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:36:58.047344
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import Mock, patch, sentinel


# Generated at 2026-10-24 20:37:21.603156
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    first_plugin = Mock()
    first_plugin.format_body.return_value = "formatted by first"

    second_plugin = Mock()
    second_plugin.format_body.return_value = "formatted by second"

    formatting = Formatting.__new__(Formatting)
    formatting.enabled_plugins = [first_plugin, second_plugin]

    result = formatting.format_body("original content", "application/json")

    assert result == "formatted by second"
    first_plugin.format_body.assert_called_once_with(
        "original content", "application/json"
    )
    second_plugin.format_body.assert_called_once_with(
        "formatted by first", "application/json"
    )

    # Invalid MIME types should leave the content unchanged and skip plugins.
    first_plugin.reset_mock()
    second_plugin.reset_mock()

    result = formatting.format_body("original content", "invalid-mime")

    assert result == "original content"
    first_plugin.format_body.assert_not_called()
    second_plugin.format_body.assert_not_called()

# Generated at 2026-10-24 20:37:47.608977
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 20:37:59.949755
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import patch


# Generated at 2026-10-24 20:38:23.647828
# Unit test for constructor of class Formatting
def test_Formatting():
    enabled_plugin = Mock()
    enabled_plugin.enabled = True

    disabled_plugin = Mock()
    disabled_plugin.enabled = False

    enabled_plugin_class = Mock(return_value=enabled_plugin)
    disabled_plugin_class = Mock(return_value=disabled_plugin)

    available_plugins = {
        'format': [enabled_plugin_class, disabled_plugin_class],
    }

    with patch.object(
        plugin_manager,
        'get_formatters_grouped',
        return_value=available_plugins,
    ):
        formatting = Formatting(
            groups=['format'],
            env=sentinel.environment,
            custom_option='value',
        )

    enabled_plugin_class.assert_called_once_with(
        env=sentinel.environment,
        custom_option='value',
    )
    disabled_plugin_class.assert_called_once_with(
        env=sentinel.environment,
        custom_option='value',
    )
    assert formatting.enabled_plugins == [enabled_plugin]

# Generated at 2026-10-24 20:38:40.037512
# Unit test for constructor of class Formatting
def test_Formatting():import pytest

# Replace `your_module` with the module containing Formatting.
from your_module import Formatting


def test_formatting_constructor(monkeypatch):
    class EnabledFormatter:
        def __init__(self, env, **kwargs):
            self.env = env
            self.kwargs = kwargs
            self.enabled = True

    class DisabledFormatter:
        def __init__(self, env, **kwargs):
            self.env = env
            self.kwargs = kwargs
            self.enabled = False

    formatter_groups = {
        "test": [
            EnabledFormatter,
            DisabledFormatter,
        ]
    }

    monkeypatch.setattr(
        "your_module.plugin_manager.get_formatters_grouped",
        lambda: formatter_groups,
    )

    env = object()
    formatting = Formatting(
        groups=["test"],
        env=env,
        color=True,
    )

    # Only enabled plugins should be registered.
    assert len(formatting.enabled_plugins) == 1

    plugin = formatting.enabled_plugins[0]
    assert isinstance(plugin, EnabledFormatter)
    assert plugin.env is env
    assert plugin.kwargs == {"color": True}

# Generated at 2026-10-24 20:39:09.012448
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Mock(spec=Environment)

    enabled_formatter_1 = Mock(enabled=True)
    disabled_formatter = Mock(enabled=False)
    enabled_formatter_2 = Mock(enabled=True)

    formatter_class_1 = Mock(return_value=enabled_formatter_1)
    formatter_class_2 = Mock(return_value=disabled_formatter)
    formatter_class_3 = Mock(return_value=enabled_formatter_2)

    available_plugins = {
        "group_1": [formatter_class_1, formatter_class_2],
        "group_2": [formatter_class_3],
    }

    with patch.object(
        plugin_manager,
        "get_formatters_grouped",
        return_value=available_plugins,
    ) as get_formatters:
        formatting = Formatting(
            groups=["group_1", "group_2"],
            env=env,
            option="value",
        )

    get_formatters.assert_called_once_with()

    formatter_class_1.assert_called_once_with(env=env, option="value")
    formatter_class_2.assert_called_once_with(env=env, option="value")
    formatter_class_3.assert_called_once_with(env=env, option="value")

    assert formatting.enabled_plugins == [
        enabled_formatter_1,
        enabled_formatter_2,
    ]

# Generated at 2026-10-24 20:39:27.881398
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.plugins import FormatterPlugin

    class DummyFormatterPlugin(FormatterPlugin):
        group_name = 'format'

        def module_0.format_headers(self, headers: str) -> str:
            return headers + '\nX-Dummy-Header: dummy_value'

    original_plugins = list(plugin_manager)
    plugin_manager.register(DummyFormatterPlugin)
    try:
        formatting = Formatting(groups=['format'], env=Environment())
        assert len(formatting.enabled_plugins) == 1
        assert isinstance(formatting.enabled_plugins[0], DummyFormatterPlugin)

        headers = 'Content-Type: application/json\nContent-Length: 42'
        expected = headers + '\nX-Dummy-Header: dummy_value'
        assert formatting.format_headers(headers) == expected

        # With no groups enabled, headers must pass through unchanged.
        assert Formatting(groups=[], env=Environment()).format_headers(headers) == headers

        # Only enabled plugins are chained.
        class DisabledFormatterPlugin(DummyFormatterPlugin):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.enabled = False

        plugin_manager.register(DisabledFormatterPlugin)
        try:
            formatting = Formatting(groups=['format'], env=Environment())
            assert len(formatting.enabled_plugins) == 1  # disabled plugin excluded
            assert formatting.format_headers(headers) == expected
        finally:
            plugin_manager.unregister(DisabledFormatterPlugin)
    finally:
        plugin_manager.unregister(DummyFormatterPlugin)

    assert list(plugin_manager) == original_plugins

# Generated at 2026-10-24 20:39:49.771511
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():calls = []


# Generated at 2026-10-24 20:40:07.693117
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:40:10.560001
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:40:13.530300
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 20:40:29.375189
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import Mock

import your_module  # Replace with the module containing Formatting


def test_formatting_constructor(monkeypatch):
    env = object()

    enabled_plugin = Mock()
    enabled_plugin.enabled = True

    disabled_plugin = Mock()
    disabled_plugin.enabled = False

    enabled_formatter = Mock(return_value=enabled_plugin)
    disabled_formatter = Mock(return_value=disabled_plugin)

    grouped_formatters = {
        "json": [enabled_formatter],
        "other": [disabled_formatter],
    }

    get_formatters_grouped = Mock(return_value=grouped_formatters)
    monkeypatch.setattr(
        your_module.plugin_manager,
        "get_formatters_grouped",
        get_formatters_grouped,
    )

    formatting = your_module.Formatting(
        groups=["json", "other"],
        env=env,
        option=True,
    )

    get_formatters_grouped.assert_called_once_with()

    enabled_formatter.assert_called_once_with(
        env=env,
        option=True,
    )
    disabled_formatter.assert_called_once_with(
        env=env,
        option=True,
    )

    assert formatting.enabled_plugins == [enabled_plugin]

# Generated at 2026-10-24 20:40:44.966285
# Unit test for constructor of class Formatting
def test_Formatting():from types import SimpleNamespace
from unittest.mock import Mock

def test_Formatting(monkeypatch):
    env = object()

    enabled_plugin = SimpleNamespace(enabled=True)
    disabled_plugin = SimpleNamespace(enabled=False)

    enabled_formatter = Mock(return_value=enabled_plugin)
    disabled_formatter = Mock(return_value=disabled_plugin)

    monkeypatch.setattr(
        plugin_manager,
        "get_formatters_grouped",
        lambda: {
            "default": [
                enabled_formatter,
                disabled_formatter,
            ]
        },
    )

    formatting = Formatting(
        groups=["default"],
        env=env,
        option="value",
    )

    enabled_formatter.assert_called_once_with(
        env=env,
        option="value",
    )
    disabled_formatter.assert_called_once_with(
        env=env,
        option="value",
    )

    assert formatting.enabled_plugins == [enabled_plugin]

# Generated at 2026-10-24 20:41:01.452591
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