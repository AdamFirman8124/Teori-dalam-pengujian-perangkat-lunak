

# Generated at 2026-10-24 19:34:30.046839
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:34:32.465963
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:34:34.882733
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:34:37.297921
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:34:39.715702
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:34:42.131204
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:34:44.549748
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:34:46.966613
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:34:49.383061
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:34:51.800409
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:34:54.218795
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:34:56.635609
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:34:59.052652
# Unit test for constructor of class Conversion

# Generated at 2026-10-24 19:35:01.471079
# Unit test for constructor of class Conversion

# Generated at 2026-10-24 19:35:03.888455
# Unit test for constructor of class Conversion

# Generated at 2026-10-24 19:35:06.304119
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:35:08.728169
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:35:11.140335
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:35:13.557314
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:35:15.974364
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:35:18.392895
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:35:20.809594
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:35:23.227181
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:35:25.643390
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:35:28.061558
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:35:30.478028
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:35:32.895163
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:35:35.315738
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:35:37.730888
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:35:40.145443
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:35:42.563013
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:35:44.980759
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:35:47.399397
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:35:49.813308
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:35:52.231762
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:35:54.648250
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:35:57.063710
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:35:59.481699
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:36:01.900531
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:36:18.532056
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

# Generated at 2026-10-24 19:36:31.434098
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:36:32.759195
# Unit test for constructor of class Formatting
def test_Formatting():created = []


# Generated at 2026-10-24 19:36:49.169236
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

# Generated at 2026-10-24 19:36:51.688054
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:36:54.105886
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:36:56.522430
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:36:59.043034
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:37:01.459753
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:37:03.876442
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:37:06.489567
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

# Generated at 2026-10-24 19:37:24.480633
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

# Generated at 2026-10-24 19:37:41.082083
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

# Generated at 2026-10-24 19:37:57.540278
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

# Generated at 2026-10-24 19:37:59.958999
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:38:02.375116
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:38:04.794098
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:38:07.209218
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:38:08.538858
# Unit test for constructor of class Formatting
def test_Formatting():created = []


# Generated at 2026-10-24 19:38:22.540492
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import Mock

import your_module as module


def test_formatting_constructor(monkeypatch):
    env = Mock()

    enabled_plugin = Mock()
    enabled_plugin.enabled = True

    disabled_plugin = Mock()
    disabled_plugin.enabled = False

    enabled_plugin_class = Mock(return_value=enabled_plugin)
    disabled_plugin_class = Mock(return_value=disabled_plugin)

    get_formatters_grouped = Mock(
        return_value={
            "default": [
                enabled_plugin_class,
                disabled_plugin_class,
            ]
        }
    )
    monkeypatch.setattr(
        module.plugin_manager,
        "get_formatters_grouped",
        get_formatters_grouped,
    )

    formatting = module.Formatting(
        groups=["default"],
        env=env,
        color=True,
    )

    get_formatters_grouped.assert_called_once_with()

    enabled_plugin_class.assert_called_once_with(
        env=env,
        color=True,
    )
    disabled_plugin_class.assert_called_once_with(
        env=env,
        color=True,
    )

    assert formatting.enabled_plugins == [enabled_plugin]

# Generated at 2026-10-24 19:38:39.130217
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

# Generated at 2026-10-24 19:38:56.927539
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:38:59.350823
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:39:01.768314
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:39:04.289496
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:39:06.707820
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:39:09.125169
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:39:33.607271
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import Mock, call


# Generated at 2026-10-24 19:39:59.102788
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:40:01.525995
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:40:03.944027
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:40:06.361862
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:40:08.781274
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:40:11.398021
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

# Generated at 2026-10-24 19:40:29.212276
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

# Generated at 2026-10-24 19:40:44.940205
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():calls = []


# Generated at 2026-10-24 19:41:02.674389
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:41:05.089647
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:41:07.663601
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:41:10.076089
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:41:12.492962
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:41:14.911010
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:41:17.511117
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:41:19.930111
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:41:22.347929
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:41:46.012065
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():calls = []


# Generated at 2026-10-24 19:41:48.766091
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:41:51.299467
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:41:53.847984
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:41:56.369181
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:41:58.786105
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:42:01.300347
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:42:03.721709
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:42:06.135056
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:42:08.550550
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:42:10.966403
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:42:13.384308
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:42:15.798989
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:42:18.215543
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:42:20.634948
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:42:23.053092
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:42:25.469365
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:42:27.885370
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:42:30.305716
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:42:32.719589
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:42:44.073843
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import patch


# Generated at 2026-10-24 19:43:10.386242
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import Mock


# Unit test for constructor of class Formatting
def test_Formatting(monkeypatch):
    env = Mock(spec=Environment)

    enabled_plugin_1 = Mock(enabled=True)
    disabled_plugin = Mock(enabled=False)
    enabled_plugin_2 = Mock(enabled=True)

    formatter_class_1 = Mock(return_value=enabled_plugin_1)
    formatter_class_2 = Mock(return_value=disabled_plugin)
    formatter_class_3 = Mock(return_value=enabled_plugin_2)

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
        enabled_plugin_1,
        enabled_plugin_2,
    ]

# Generated at 2026-10-24 19:43:14.115388
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:43:16.532363
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:43:19.050166
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:43:21.467726
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:43:23.884646
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:43:26.300559
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:43:28.717206
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:43:31.134413
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:43:33.552397
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:43:35.973241
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:43:43.355834
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import patch


# Generated at 2026-10-24 19:44:09.370302
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:44:10.701560
# Unit test for constructor of class Formatting
def test_Formatting():created = []


# Generated at 2026-10-24 19:44:33.842991
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():calls = []
