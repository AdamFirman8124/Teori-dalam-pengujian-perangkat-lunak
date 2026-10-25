

# Generated at 2026-10-24 22:41:58.164960
# Unit test for constructor of class Conversion
def test_Conversion():
    conversion = Conversion()

    assert isinstance(conversion, Conversion)

# Generated at 2026-10-24 22:42:13.524337
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch


# Generated at 2026-10-24 22:42:15.946807
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 22:42:18.366199
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 22:42:20.942535
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 22:42:46.892471
# Unit test for constructor of class Formatting
def test_Formatting():
    env = MagicMock(spec=Environment)

    enabled_plugin_1 = MagicMock()
    enabled_plugin_1.enabled = True

    disabled_plugin = MagicMock()
    disabled_plugin.enabled = False

    enabled_plugin_2 = MagicMock()
    enabled_plugin_2.enabled = True

    enabled_plugin_class_1 = MagicMock(return_value=enabled_plugin_1)
    disabled_plugin_class = MagicMock(return_value=disabled_plugin)
    enabled_plugin_class_2 = MagicMock(return_value=enabled_plugin_2)

    available_plugins = {
        "group_a": [enabled_plugin_class_1, disabled_plugin_class],
        "group_b": [enabled_plugin_class_2],
    }

    with patch.object(
        plugin_manager,
        "get_formatters_grouped",
        return_value=available_plugins,
    ):
        formatting = Formatting(
            groups=["group_a", "group_b"],
            env=env,
            option="value",
        )

    enabled_plugin_class_1.assert_called_once_with(
        env=env,
        option="value",
    )
    disabled_plugin_class.assert_called_once_with(
        env=env,
        option="value",
    )
    enabled_plugin_class_2.assert_called_once_with(
        env=env,
        option="value",
    )

    assert formatting.enabled_plugins == [
        enabled_plugin_1,
        enabled_plugin_2,
    ]

# Generated at 2026-10-24 22:43:11.588860
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = 'application/json'

    unsupported = MagicMock()
    unsupported.supports.return_value = False

    supported = MagicMock()
    supported.supports.return_value = True
    converter = supported.return_value

    unused = MagicMock()
    unused.supports.return_value = True

    with patch.object(
        plugin_manager,
        'get_converters',
        return_value=[unsupported, supported, unused],
    ) as get_converters:
        result = Conversion.get_converter(mime)

    assert result is converter
    get_converters.assert_called_once_with()
    unsupported.supports.assert_called_once_with(mime)
    unsupported.assert_not_called()
    supported.supports.assert_called_once_with(mime)
    supported.assert_called_once_with(mime)
    unused.supports.assert_not_called()
    unused.assert_not_called()

    # Invalid MIME types should not query the plugin registry.
    with patch.object(plugin_manager, 'get_converters') as get_converters:
        assert Conversion.get_converter('invalid-mime') is None
        assert Conversion.get_converter('') is None

    get_converters.assert_not_called()

# Generated at 2026-10-24 22:43:27.647306
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch


# Generated at 2026-10-24 22:43:44.147819
# Unit test for constructor of class Formatting
def test_Formatting():
    """Unit test for Formatting.__init__."""
    from unittest.mock import MagicMock, patch

    mock_env = MagicMock()

    def make_cls(enabled=True):
        instance = MagicMock()
        instance.enabled = enabled
        cls = MagicMock(return_value=instance)
        return cls, instance

    # 1. empty groups -> no plugins instantiated
    with patch.object(plugin_manager, "get_formatters_grouped",
                      return_value={"a": [make_cls(True)[0]]}):
        f = Formatting(groups=[], env=mock_env)
        assert f.enabled_plugins == []

    # 2. filters out disabled plugins, keeps enabled ones in order
    cls_a, inst_a = make_cls(enabled=True)
    cls_b, inst_b = make_cls(enabled=False)
    cls

# Generated at 2026-10-24 22:44:10.762022
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import patch


# Generated at 2026-10-24 22:44:28.721183
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 22:44:31.534726
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 22:44:34.324147
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 22:45:01.564318
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Environment()
    created_plugins = []

    class EnabledFormatter:
        def __init__(self, env, **kwargs):
            self.env = env
            self.kwargs = kwargs
            self.enabled = True
            created_plugins.append(self)

    class DisabledFormatter:
        def __init__(self, env, **kwargs):
            self.env = env
            self.kwargs = kwargs
            self.enabled = False
            created_plugins.append(self)

    available_plugins = {
        'test-group': [EnabledFormatter, DisabledFormatter],
    }

    with patch.object(
        plugin_manager,
        'get_formatters_grouped',
        return_value=available_plugins,
    ) as get_formatters:
        formatting = Formatting(
            groups=['test-group'],
            env=env,
            option='value',
        )

    get_formatters.assert_called_once_with()
    assert len(created_plugins) == 2

    for plugin in created_plugins:
        assert plugin.env is env
        assert plugin.kwargs == {'option': 'value'}

    assert formatting.enabled_plugins == [created_plugins[0]]
    assert isinstance(formatting.enabled_plugins[0], EnabledFormatter)

# Generated at 2026-10-24 22:45:24.608451
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import Mock


# Generated at 2026-10-24 22:45:50.921487
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    mime = "application/json"
    expected_converter = Mock()

    unsupported_converter_class = Mock()
    unsupported_converter_class.supports.return_value = False

    supported_converter_class = Mock()
    supported_converter_class.supports.return_value = True
    supported_converter_class.return_value = expected_converter

    unused_converter_class = Mock()

    with patch.object(
        plugin_manager,
        "get_converters",
        return_value=[
            unsupported_converter_class,
            supported_converter_class,
            unused_converter_class,
        ],
    ) as get_converters:
        result = Conversion.get_converter(mime)

    assert result is expected_converter
    get_converters.assert_called_once_with()

    unsupported_converter_class.supports.assert_called_once_with(mime)
    unsupported_converter_class.assert_not_called()

    supported_converter_class.supports.assert_called_once_with(mime)
    supported_converter_class.assert_called_once_with(mime)

    # Conversion stops searching after finding the first supporting converter.
    unused_converter_class.supports.assert_not_called()
    unused_converter_class.assert_not_called()

# Generated at 2026-10-24 22:46:14.779420
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():calls = []


# Generated at 2026-10-24 22:46:41.098408
# Unit test for constructor of class Formatting
def test_Formatting():
    from unittest.mock import Mock, patch, call

    env = Mock()
    enabled_formatter_1 = Mock(enabled=True)
    disabled_formatter = Mock(enabled=False)
    enabled_formatter_2 = Mock(enabled=True)

    formatter_class_1 = Mock(return_value=enabled_formatter_1)
    formatter_class_2 = Mock(return_value=disabled_formatter)
    formatter_class_3 = Mock(return_value=enabled_formatter_2)

    available_plugins = {
        'group_1': [formatter_class_1, formatter_class_2],
        'group_2': [formatter_class_3],
    }

    with patch.object(
        plugin_manager,
        'get_formatters_grouped',
        return_value=available_plugins,
    ) as get_formatters:
        formatting = Formatting(
            groups=['group_1', 'group_2'],
            env=env,
            option='value',
        )

    get_formatters.assert_called_once_with()
    assert formatter_class_1.call_args_list == [
        call(env=env, option='value')
    ]
    assert formatter_class_2.call_args_list == [
        call(env=env, option='value')
    ]
    assert formatter_class_3.call_args_list == [
        call(env=env, option='value')
    ]

    assert formatting.enabled_plugins == [
        enabled_formatter_1,
        enabled_formatter_2,
    ]

# Generated at 2026-10-24 22:47:04.711571
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import Mock, sentinel


def test_Formatting(monkeypatch):
    enabled_plugin_1 = Mock(enabled=True)
    disabled_plugin = Mock(enabled=False)
    enabled_plugin_2 = Mock(enabled=True)

    enabled_cls_1 = Mock(return_value=enabled_plugin_1)
    disabled_cls = Mock(return_value=disabled_plugin)
    enabled_cls_2 = Mock(return_value=enabled_plugin_2)
    unused_cls = Mock()

    get_formatters_grouped = Mock(return_value={
        'group_1': [enabled_cls_1, disabled_cls],
        'group_2': [enabled_cls_2],
        'unused_group': [unused_cls],
    })
    monkeypatch.setattr(
        plugin_manager,
        'get_formatters_grouped',
        get_formatters_grouped,
    )

    formatting = Formatting(
        groups=['group_1', 'group_2'],
        env=sentinel.env,
        option='value',
    )

    get_formatters_grouped.assert_called_once_with()
    enabled_cls_1.assert_called_once_with(
        env=sentinel.env,
        option='value',
    )
    disabled_cls.assert_called_once_with(
        env=sentinel.env,
        option='value',
    )
    enabled_cls_2.assert_called_once_with(
        env=sentinel.env,
        option='value',
    )
    unused_cls.assert_not_called()

    assert formatting.enabled_plugins == [
        enabled_plugin_1,
        enabled_plugin_2,
    ]

# Generated at 2026-10-24 22:47:28.201480
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():calls = []


# Generated at 2026-10-24 22:47:51.855744
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    first_processor = Mock()
    first_processor.format_body.return_value = "formatted once"

    second_processor = Mock()
    second_processor.format_body.return_value = "formatted twice"

    formatting = Formatting.__new__(Formatting)
    formatting.enabled_plugins = [first_processor, second_processor]

    result = formatting.format_body("original content", "application/json")

    assert result == "formatted twice"
    first_processor.format_body.assert_called_once_with(
        "original content", "application/json"
    )
    second_processor.format_body.assert_called_once_with(
        "formatted once", "application/json"
    )

    first_processor.reset_mock()
    second_processor.reset_mock()

    # Invalid MIME types must leave the content unchanged and skip processors.
    result = formatting.format_body("original content", "invalid-mime")

    assert result == "original content"
    first_processor.format_body.assert_not_called()
    second_processor.format_body.assert_not_called()

# Generated at 2026-10-24 22:48:16.533915
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Mock(spec=Environment)

    enabled_plugin = Mock(enabled=True)
    disabled_plugin = Mock(enabled=False)
    another_enabled_plugin = Mock(enabled=True)

    enabled_cls = Mock(return_value=enabled_plugin)
    disabled_cls = Mock(return_value=disabled_plugin)
    another_enabled_cls = Mock(return_value=another_enabled_plugin)

    available_plugins = {
        'group_a': [enabled_cls, disabled_cls],
        'group_b': [another_enabled_cls],
    }

    with patch.object(
        plugin_manager,
        'get_formatters_grouped',
        return_value=available_plugins,
    ) as get_formatters_grouped:
        formatting = Formatting(
            groups=['group_a', 'group_b'],
            env=env,
            option='value',
        )

    get_formatters_grouped.assert_called_once_with()
    enabled_cls.assert_called_once_with(env=env, option='value')
    disabled_cls.assert_called_once_with(env=env, option='value')
    another_enabled_cls.assert_called_once_with(env=env, option='value')

    assert formatting.enabled_plugins == [
        enabled_plugin,
        another_enabled_plugin,
    ]

# Generated at 2026-10-24 22:48:43.576311
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 22:48:45.001074
# Unit test for constructor of class Formatting
def test_Formatting():created = []


# Generated at 2026-10-24 22:49:02.930953
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

# Generated at 2026-10-24 22:49:19.620290
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():import unittest
from unittest import mock

from httpie.plugins import ConverterPlugin
from httpie.plugins.registry import plugin_manager

from httpie.plugins.builtin import Conversion  # adjust import to your module path


class DummyConverter(ConverterPlugin):
    @classmethod
    def supports(cls, mime):
        return mime == 'application/json'

    def convert(self, content_bytes):
        return content_bytes


class TestConversionGetConverter(unittest.TestCase):

    @mock.patch.object(plugin_manager, 'get_converters')
    def test_returns_matching_converter(self, mock_get_converters):
        mock_get_converters.return_value = [DummyConverter]

        converter = Conversion.get_converter('application/json')

        self.assertIsInstance(converter, DummyConverter)
        self.assertEqual(converter.mime, 'application/json')

    @mock.patch.object(plugin_manager, 'get_converters')
    def test_returns_none_when_no_converter_supports_mime(self, mock_get_converters):
        mock_get_converters.return_value = [DummyConverter]

        converter = Conversion.get_converter('application/xml')

        self.assertIsNone(converter)

    @mock.patch.object(plugin_manager, 'get_converters')
    def test_returns_none_for_invalid_mime(self, mock_get_converters):
        mock_get_converters.return_value = [DummyConverter]

        self.assertIsNone(Conversion.get_converter('not-a-mime'))
        self.assertIsNone(Conversion.get_converter(''))
        self.assertIsNone(Conversion.get_converter(None))

    @mock.patch.object(plugin_manager, 'get_converters')
    def test_returns_first_supporting_converter(self, mock_get_converters):
        class OtherConverter(DummyConverter):
            @classmethod
            def supports(cls, mime):
                return True

        mock_get_converters.return_value = [DummyConverter, OtherConverter]

        converter = Conversion.get_converter('application/json')

        self.assertIsInstance(converter, DummyConverter)
        self.assertNotIsInstance(converter, OtherConverter)


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-10-24 22:49:42.887902
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():calls = []


# Generated at 2026-10-24 22:50:00.685878
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

# Generated at 2026-10-24 22:50:24.636751
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import Mock


# Generated at 2026-10-24 22:50:42.482082
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 22:50:45.267086
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 22:50:48.189745
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 22:51:13.175240
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Mock(spec=Environment)

    enabled_plugin_1 = Mock()
    enabled_plugin_1.enabled = True

    disabled_plugin = Mock()
    disabled_plugin.enabled = False

    enabled_plugin_2 = Mock()
    enabled_plugin_2.enabled = True

    enabled_class_1 = Mock(return_value=enabled_plugin_1)
    disabled_class = Mock(return_value=disabled_plugin)
    enabled_class_2 = Mock(return_value=enabled_plugin_2)

    available_plugins = {
        "group-1": [enabled_class_1, disabled_class],
        "group-2": [enabled_class_2],
    }

    with patch.object(
        plugin_manager,
        "get_formatters_grouped",
        return_value=available_plugins,
    ) as get_formatters:
        formatting = Formatting(
            groups=["group-1", "group-2"],
            env=env,
            option="value",
        )

    get_formatters.assert_called_once_with()
    enabled_class_1.assert_called_once_with(env=env, option="value")
    disabled_class.assert_called_once_with(env=env, option="value")
    enabled_class_2.assert_called_once_with(env=env, option="value")

    # Only enabled plugins are retained, preserving group/plugin order.
    assert formatting.enabled_plugins == [
        enabled_plugin_1,
        enabled_plugin_2,
    ]

# Generated at 2026-10-24 22:51:36.734238
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():calls = []


# Generated at 2026-10-24 22:52:02.224450
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import Mock


def test_Formatting(monkeypatch):
    env = Mock(spec=Environment)

    enabled_plugin = Mock(enabled=True)
    disabled_plugin = Mock(enabled=False)
    another_enabled_plugin = Mock(enabled=True)

    enabled_cls = Mock(return_value=enabled_plugin)
    disabled_cls = Mock(return_value=disabled_plugin)
    another_enabled_cls = Mock(return_value=another_enabled_plugin)

    get_formatters_grouped = Mock(return_value={
        'group_a': [enabled_cls, disabled_cls],
        'group_b': [another_enabled_cls],
    })
    monkeypatch.setattr(
        plugin_manager,
        'get_formatters_grouped',
        get_formatters_grouped,
    )

    formatting = Formatting(
        groups=['group_a', 'group_b'],
        env=env,
        custom_option='value',
    )

    get_formatters_grouped.assert_called_once_with()
    enabled_cls.assert_called_once_with(env=env, custom_option='value')
    disabled_cls.assert_called_once_with(env=env, custom_option='value')
    another_enabled_cls.assert_called_once_with(
        env=env,
        custom_option='value',
    )

    assert formatting.enabled_plugins == [
        enabled_plugin,
        another_enabled_plugin,
    ]