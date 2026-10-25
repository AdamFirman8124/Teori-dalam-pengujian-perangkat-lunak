

# Generated at 2026-10-24 19:12:56.574322
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:13:14.267873
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:13:16.683404
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:13:19.102240
# Unit test for function is_valid_mime

# Generated at 2026-10-24 19:13:30.360071
# Unit test for function is_valid_mime
def test_is_valid_mime():import re


# Generated at 2026-10-24 19:13:46.356309
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import Mock, patch

import pytest

# Replace `your_module` with the module containing Conversion.
from your_module import Conversion


class SupportedConverter:
    def __init__(self, mime):
        self.mime = mime

    @classmethod
    def supports(cls, mime):
        return mime == "application/json"


class UnsupportedConverter:
    @classmethod
    def supports(cls, mime):
        return False


def test_get_converter_returns_matching_converter():
    with patch("your_module.plugin_manager.get_converters") as get_converters:
        get_converters.return_value = [
            UnsupportedConverter,
            SupportedConverter,
        ]

        converter = Conversion.get_converter("application/json")

    assert isinstance(converter, SupportedConverter)
    assert converter.mime == "application/json"
    get_converters.assert_called_once_with()


def test_get_converter_returns_none_when_no_converter_matches():
    with patch("your_module.plugin_manager.get_converters") as get_converters:
        get_converters.return_value = [UnsupportedConverter]

        converter = Conversion.get_converter("application/json")

    assert converter is None


@pytest.mark.parametrize("mime", [None, "", "application", "/json", "application/"])
def test_get_converter_returns_none_for_invalid_mime(mime):
    with patch("your_module.plugin_manager.get_converters") as get_converters:
        converter = Conversion.get_converter(mime)

    assert converter is None
    get_converters.assert_not_called()

# Generated at 2026-10-24 19:14:04.148858
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:14:06.682490
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:14:09.106272
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:14:11.528083
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:14:14.120749
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:14:16.537958
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:14:18.954807
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:14:21.370717
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:14:23.787643
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:14:26.202558
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:14:28.621655
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:14:31.035874
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:14:33.452172
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:14:35.871005
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:14:38.290536
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:14:40.711022
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:14:43.128958
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:14:45.768218
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():formatter = Formatting(groups=[])

# Generated at 2026-10-24 19:15:02.821103
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import patch


# Generated at 2026-10-24 19:15:05.240789
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:15:07.658926
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:15:10.076020
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:15:12.492643
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:15:14.909119
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:15:17.327387
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:15:19.745727
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:15:22.163750
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:15:24.580328
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:15:36.415546
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

# Generated at 2026-10-24 19:15:53.106057
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

# Generated at 2026-10-24 19:16:10.802355
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:16:13.223662
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:16:15.820208
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:16:18.237107
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:16:20.651635
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:16:23.070734
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:16:25.508095
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:16:27.948025
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:16:30.395507
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:16:32.812152
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:16:35.228468
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:16:37.647093
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:16:40.065146
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:16:42.481409
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:16:44.899883
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:16:47.318720
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:16:49.738598
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:16:52.155971
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:16:54.572627
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:16:56.990257
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:16:59.408120
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:17:01.824040
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:17:04.256656
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:17:06.670669
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:17:09.088840
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:17:11.504469
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:17:13.923838
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:17:16.336472
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:17:18.752889
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:17:21.171626
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:17:23.585422
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:17:26.001513
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:17:28.896842
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:17:46.570867
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:17:48.984003
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:17:51.498697
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:17:53.916688
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:17:56.334772
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:17:58.749655
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:18:01.165833
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:18:03.584519
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:18:06.000612
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:18:08.417589
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:18:10.834612
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:18:13.254571
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:18:15.672721
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:18:18.089476
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:18:20.504689
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:18:22.920604
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:18:25.338910
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:18:27.753186
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:18:30.176612
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:18:32.590679
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:18:35.009096
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:18:37.428910
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:18:39.847320
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:18:42.263229
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:18:44.683140
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:18:47.098649
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:18:49.514834
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:18:52.126152
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:18:54.543800
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:18:56.960690
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:18:59.376243
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:19:01.795734
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:19:04.214432
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:19:06.635272
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:19:09.055583
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:19:11.481113
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:19:13.899465
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:19:16.314262
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:19:38.694388
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:19:41.112492
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:19:43.531693
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:19:46.052990
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:19:48.467536
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:19:50.885809
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:19:53.304922
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-24 19:19:55.721577
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:19:58.139067
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:20:00.555140
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:20:02.971181
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:20:05.386888
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:20:07.806820
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:20:10.221577
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:20:12.638891
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:20:15.057452
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:20:17.473674
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:20:19.891436
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:20:22.307875
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:20:25.889669
# Unit test for method format_body of class Formatting

# Generated at 2026-10-24 19:20:28.507951
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():formatter = Formatting(groups=[])

# Generated at 2026-10-24 19:20:44.943302
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

# Generated at 2026-10-24 19:21:02.645141
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:21:05.059922
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:21:07.630418
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:21:10.049243
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:21:12.463557
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:21:15.036034
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:21:17.454695
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:21:19.874792
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:21:22.292760
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:21:24.708465
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:21:27.123152
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:21:29.656804
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

# Generated at 2026-10-24 19:21:47.514909
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

# Generated at 2026-10-24 19:22:05.434605
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

# Generated at 2026-10-24 19:22:07.855919
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:22:10.271762
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:22:12.795950
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:22:15.211812
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:22:17.628865
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:22:20.042742
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:22:26.432602
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:22:28.853864
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:22:31.272855
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-24 19:22:33.691670
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:22:36.107711
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:22:38.522926
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:22:40.940983
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:22:43.392534
# Unit test for constructor of class Formatting

# Generated at 2026-10-24 19:22:45.775878
# Unit test for constructor of class Formatting