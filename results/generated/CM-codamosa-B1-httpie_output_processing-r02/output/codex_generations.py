

# Generated at 2026-10-24 21:16:49.169963
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    first_plugin = Mock()
    first_plugin.format_body.return_value = "formatted once"

    second_plugin = Mock()
    second_plugin.format_body.return_value = "formatted twice"

    formatting = Formatting.__new__(Formatting)
    formatting.enabled_plugins = [first_plugin, second_plugin]

    result = formatting.format_body("original content", "application/json")

    assert result == "formatted twice"
    first_plugin.format_body.assert_called_once_with(
        "original content", "application/json"
    )
    second_plugin.format_body.assert_called_once_with(
        "formatted once", "application/json"
    )

    first_plugin.reset_mock()
    second_plugin.reset_mock()

    result = formatting.format_body("original content", "invalid-mime")

    assert result == "original content"
    first_plugin.format_body.assert_not_called()
    second_plugin.format_body.assert_not_called()

# Generated at 2026-10-24 21:16:51.694108
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:16:54.111705
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:16:56.527569
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:16:58.945948
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 21:17:01.510011
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 21:17:03.928588
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 21:17:13.267833
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import Mock, patch


# Generated at 2026-10-24 21:17:19.920587
# Unit test for function is_valid_mime
def test_is_valid_mime():
    valid_mimes = [
        "text/plain",
        "application/json",
        "image/svg+xml",
        "application/vnd.api+json",
        "*/*",
    ]

    invalid_mimes = [
        None,
        "",
        "text",
        "text/",
        "/plain",
        "text/plain/extra",
    ]

    for mime in valid_mimes:
        assert bool(module_0.is_valid_mime(mime)), f"Expected {mime!r} to be valid"

    for mime in invalid_mimes:
        assert not module_0.is_valid_mime(mime), f"Expected {mime!r} to be invalid"

# Generated at 2026-10-24 21:17:21.240266
# Unit test for function is_valid_mime
def test_is_valid_mime():import re


# Generated at 2026-10-24 21:17:37.739453
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    p1 = Mock()
    p1.format_body.return_value = "step1"
    p2 = Mock()
    p2.format_body.return_value = "step2"
    fmt = make_formatting([p1, p2])

    # 1. valid mime -> every plugin runs, output chains plugin-to-plugin
    assert fmt.format_body("raw", "application/json") == "step2"
    p1.format_body.assert_called_once_with("raw", "application/json")
    p2.format_body.assert_called_once_with("step1", "application/json")

    # 2. invalid mime -> plugins skipped, content untouched
    p1.reset_mock()
    p2.reset_mock()
    assert fmt.format_body("raw", "not-a-mime") == "raw"
    p1.format_body.assert_not_called()
    p2.format_body.assert_not_called()

    # 3. empty mime -> also invalid
    assert fmt.format_body("raw", "") == "raw"
    p1.format_body.assert_not_called()

    # 4. no enabled plugins + valid mime -> passthrough
    assert make_formatting([]).format_body("raw", "application/json") == "raw"

# Generated at 2026-10-24 21:17:40.165327
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 21:17:42.583297
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 21:17:45.001327
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 21:17:47.416061
# Unit test for function is_valid_mime

# Generated at 2026-10-24 21:17:49.835310
# Unit test for function is_valid_mime

# Generated at 2026-10-24 21:17:52.250922
# Unit test for function is_valid_mime

# Generated at 2026-10-24 21:17:54.673547
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:17:57.085897
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:17:59.506544
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:18:01.926544
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 21:18:04.342541
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 21:18:06.758583
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 21:18:09.172527
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 21:18:11.988562
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 21:18:14.704104
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 21:18:24.023283
# Unit test for function is_valid_mime
def test_is_valid_mime():
    valid_mimes = [
        "application/json",
        "text/plain",
        "image/svg+xml",
        "application/vnd.api+json",
    ]
    invalid_mimes = [
        None,
        "",
        "application",
        "/json",
        "application/",
        "application/json/extra",
    ]

    for mime in valid_mimes:
        assert module_0.is_valid_mime(mime), f"Expected {mime!r} to be valid"

    for mime in invalid_mimes:
        assert not module_0.is_valid_mime(mime), f"Expected {mime!r} to be invalid"

# Generated at 2026-10-24 21:18:25.364119
# Unit test for function is_valid_mime
def test_is_valid_mime():import re


# Generated at 2026-10-24 21:18:43.524222
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

# Generated at 2026-10-24 21:18:45.943663
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:18:48.361636
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:18:50.781030
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:18:53.198806
# Unit test for function is_valid_mime

# Generated at 2026-10-24 21:18:55.617506
# Unit test for function is_valid_mime

# Generated at 2026-10-24 21:18:58.035490
# Unit test for function is_valid_mime

# Generated at 2026-10-24 21:19:00.456353
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 21:19:02.873165
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 21:19:05.292402
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 21:19:07.710182
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 21:19:10.126718
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 21:19:12.543867
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 21:19:14.960461
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:19:17.381013
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:19:19.798667
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:19:22.214630
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:19:24.634949
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:19:27.056747
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:19:54.032753
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import Mock, call


def test_Formatting(monkeypatch):
    env = Mock()
    enabled_plugin_1 = Mock(enabled=True)
    disabled_plugin = Mock(enabled=False)
    enabled_plugin_2 = Mock(enabled=True)

    formatter_1 = Mock(return_value=enabled_plugin_1)
    formatter_2 = Mock(return_value=disabled_plugin)
    formatter_3 = Mock(return_value=enabled_plugin_2)

    get_formatters_grouped = Mock(return_value={
        "group_1": [formatter_1, formatter_2],
        "group_2": [formatter_3],
    })
    monkeypatch.setattr(
        plugin_manager,
        "get_formatters_grouped",
        get_formatters_grouped,
    )

    formatting = Formatting(
        groups=["group_1", "group_2"],
        env=env,
        option="value",
    )

    get_formatters_grouped.assert_called_once_with()
    assert formatter_1.call_args_list == [call(env=env, option="value")]
    assert formatter_2.call_args_list == [call(env=env, option="value")]
    assert formatter_3.call_args_list == [call(env=env, option="value")]
    assert formatting.enabled_plugins == [
        enabled_plugin_1,
        enabled_plugin_2,
    ]

# Generated at 2026-10-24 21:20:20.965170
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import Mock


def test_Formatting(monkeypatch):
    env = Mock(spec=Environment)

    enabled_formatter_1 = Mock()
    enabled_formatter_1.enabled = True

    disabled_formatter = Mock()
    disabled_formatter.enabled = False

    enabled_formatter_2 = Mock()
    enabled_formatter_2.enabled = True

    formatter_class_1 = Mock(return_value=enabled_formatter_1)
    formatter_class_2 = Mock(return_value=disabled_formatter)
    formatter_class_3 = Mock(return_value=enabled_formatter_2)

    get_formatters_grouped = Mock(return_value={
        "group_1": [formatter_class_1, formatter_class_2],
        "group_2": [formatter_class_3],
    })
    monkeypatch.setattr(
        plugin_manager,
        "get_formatters_grouped",
        get_formatters_grouped,
    )

    formatting = Formatting(
        groups=["group_1", "group_2"],
        env=env,
        option="value",
    )

    get_formatters_grouped.assert_called_once_with()
    formatter_class_1.assert_called_once_with(env=env, option="value")
    formatter_class_2.assert_called_once_with(env=env, option="value")
    formatter_class_3.assert_called_once_with(env=env, option="value")

    assert formatting.enabled_plugins == [
        enabled_formatter_1,
        enabled_formatter_2,
    ]

# Generated at 2026-10-24 21:20:23.488815
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:20:25.906359
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:20:28.509190
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Environment()
    formatting = Formatting(['formatting'], env=env)
    assert isinstance(formatting.enabled_plugins, list)
    # format_headers should pass headers through each enabled plugin unchanged
    # when the input is already normalized (single header, trailing newline).
    assert formatting.format_headers('X-Test: 1\n') == 'X-Test: 1\n'
    # format_body with an invalid/empty mime must return content untouched.
    assert formatting.format_body('<html></html>', '') == '<html></html>'
    assert formatting.format_body('<html></html>', 'not-a-mime') == '<html></html>'
    # A valid mime goes through the plugin chain; with no matching formatters
    # the content is returned as-is.
    assert formatting.format_body('plain text', 'text/plain') == 'plain text'

# Generated at 2026-10-24 21:20:42.727934
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:20:44.063519
# Unit test for constructor of class Formatting
def test_Formatting():created = []


# Generated at 2026-10-24 21:21:00.457120
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

# Generated at 2026-10-24 21:21:16.874347
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

# Generated at 2026-10-24 21:21:19.293642
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:21:21.709208
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:21:24.129378
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:21:26.546572
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 21:21:28.961518
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 21:21:31.383322
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 21:21:33.801254
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:21:36.219229
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:21:38.635846
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:21:41.083612
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 21:21:43.469683
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 21:21:45.886897
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 21:21:48.307942
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:21:50.726711
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:21:53.147357
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:22:18.830480
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:22:21.476592
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:22:24.006000
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:22:26.424108
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:22:28.843344
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:22:31.260102
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:22:33.679481
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 21:22:36.098789
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 21:22:38.687071
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 21:22:41.107324
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 21:22:43.523476
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 21:22:45.945475
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 21:22:48.365760
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 21:22:50.783934
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 21:22:53.199902
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 21:22:55.618536
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:22:58.036518
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:23:00.453830
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:23:02.876021
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:23:05.293102
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:23:07.711964
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:23:33.718057
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import Mock


def test_Formatting(monkeypatch):
    env = Mock()
    enabled_plugin_1 = Mock(enabled=True)
    disabled_plugin = Mock(enabled=False)
    enabled_plugin_2 = Mock(enabled=True)

    formatter_1 = Mock(return_value=enabled_plugin_1)
    formatter_2 = Mock(return_value=disabled_plugin)
    formatter_3 = Mock(return_value=enabled_plugin_2)

    get_formatters_grouped = Mock(return_value={
        "group_1": [formatter_1, formatter_2],
        "group_2": [formatter_3],
    })
    monkeypatch.setattr(
        plugin_manager,
        "get_formatters_grouped",
        get_formatters_grouped,
    )

    formatting = Formatting(
        groups=["group_1", "group_2"],
        env=env,
        option="value",
    )

    get_formatters_grouped.assert_called_once_with()
    formatter_1.assert_called_once_with(env=env, option="value")
    formatter_2.assert_called_once_with(env=env, option="value")
    formatter_3.assert_called_once_with(env=env, option="value")

    assert formatting.enabled_plugins == [
        enabled_plugin_1,
        enabled_plugin_2,
    ]

# Generated at 2026-10-24 21:23:58.468295
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import MagicMock


def test_Formatting(monkeypatch):
    env = MagicMock(spec=Environment)

    enabled_plugin_1 = MagicMock()
    enabled_plugin_1.enabled = True

    disabled_plugin = MagicMock()
    disabled_plugin.enabled = False

    enabled_plugin_2 = MagicMock()
    enabled_plugin_2.enabled = True

    formatter_1 = MagicMock(return_value=enabled_plugin_1)
    formatter_2 = MagicMock(return_value=disabled_plugin)
    formatter_3 = MagicMock(return_value=enabled_plugin_2)

    get_formatters = MagicMock(return_value={
        "group_1": [formatter_1, formatter_2],
        "group_2": [formatter_3],
    })
    monkeypatch.setattr(
        plugin_manager,
        "get_formatters_grouped",
        get_formatters,
    )

    formatting = Formatting(
        groups=["group_1", "group_2"],
        env=env,
        option="value",
    )

    get_formatters.assert_called_once_with()
    formatter_1.assert_called_once_with(env=env, option="value")
    formatter_2.assert_called_once_with(env=env, option="value")
    formatter_3.assert_called_once_with(env=env, option="value")

    assert formatting.enabled_plugins == [
        enabled_plugin_1,
        enabled_plugin_2,
    ]

# Generated at 2026-10-24 21:24:00.889055
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:24:03.307375
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:24:05.724341
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:24:08.313858
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    from unittest.mock import patch
    from httpie.plugins.registry import plugin_manager

    class JSONConverter:
        def __init__(self, mime):
            self.mime = mime

        @classmethod
        def supports(cls, mime):
            return mime == "application/json"

    class NeverConverter:
        def __init__(self, mime):
            self.mime = mime

        @classmethod
        def supports(cls, mime):
            return False

    with patch.object(plugin_manager, "get_converters", return_value=[NeverConverter, JSONConverter]):
        converter = Conversion.get_converter("application/json")
        assert isinstance(converter, JSONConverter)
        assert converter.mime == "application/json"

        assert Conversion.get_converter("text/plain") is None
        assert Conversion.get_converter("application/xml") is None

        assert Conversion.get_converter("not-a-mime") is None
        assert Conversion.get_converter("") is None
        assert Conversion.get_converter(None) is None

# Generated at 2026-10-24 21:24:36.966456
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch


# Generated at 2026-10-24 21:24:39.387578
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 21:24:41.968746
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 21:24:44.386136
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 21:24:46.802701
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:24:49.222792
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:24:51.644061
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:24:54.184451
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:24:56.607045
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:24:59.019375
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:25:01.435919
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:25:03.853280
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:25:06.272088
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:25:08.686883
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:25:11.104423
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:25:13.689472
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Environment()
    formatting = Formatting(['formatting'], env=env)
    assert isinstance(formatting.enabled_plugins, list)
    # format_headers should pass headers through each enabled plugin unchanged
    # when the input is already normalized (single header, trailing newline).
    assert formatting.format_headers('X-Test: 1\n') == 'X-Test: 1\n'
    # format_body with an invalid/empty mime must return content untouched.
    assert formatting.format_body('<html></html>', '') == '<html></html>'
    assert formatting.format_body('<html></html>', 'not-a-mime') == '<html></html>'
    # A valid mime goes through the plugin chain; with no matching formatters
    # the content is returned as-is.
    assert formatting.format_body('plain text', 'text/plain') == 'plain text'

# Generated at 2026-10-24 21:25:30.382690
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

# Generated at 2026-10-24 21:25:56.019476
# Unit test for constructor of class Formatting
def test_Formatting():
    env = Mock(spec=Environment)

    enabled_plugin = Mock(enabled=True)
    disabled_plugin = Mock(enabled=False)

    enabled_plugin_class = Mock(return_value=enabled_plugin)
    disabled_plugin_class = Mock(return_value=disabled_plugin)

    available_plugins = {
        "format": [enabled_plugin_class, disabled_plugin_class]
    }

    with patch.object(
        plugin_manager,
        "get_formatters_grouped",
        return_value=available_plugins,
    ) as get_formatters:
        formatting = Formatting(
            groups=["format"],
            env=env,
            option="value",
        )

    get_formatters.assert_called_once_with()
    enabled_plugin_class.assert_called_once_with(env=env, option="value")
    disabled_plugin_class.assert_called_once_with(env=env, option="value")

    # Only enabled plugins should be retained, in registration order.
    assert formatting.enabled_plugins == [enabled_plugin]

# Generated at 2026-10-24 21:25:58.439590
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:26:01.009774
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:26:03.434012
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:26:05.849471
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:26:08.266287
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:26:10.682644
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:26:13.100305
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 21:26:15.519488
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 21:26:17.936136
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 21:26:20.353286
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:26:22.768613
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:26:25.187859
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 21:26:27.601288
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:26:30.019930
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 21:26:32.438764
# Unit test for method get_converter of class Conversion