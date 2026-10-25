

# Generated at 2026-10-25 04:36:41.182102
# Unit test for constructor of class Conversion
def test_Conversion():
    conversion = Conversion()

    assert conversion is not None
    assert isinstance(conversion, Conversion)

# Generated at 2026-10-25 04:36:47.538503
# Unit test for constructor of class Conversion
def test_Conversion():
    conversion = Conversion()

    assert isinstance(conversion, Conversion)

# Generated at 2026-10-25 04:36:55.821894
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    from unittest.mock import Mock, call

    first_processor = Mock()
    first_processor.format_body.return_value = "formatted once"

    second_processor = Mock()
    second_processor.format_body.return_value = "formatted twice"

    formatting = Formatting.__new__(Formatting)
    formatting.enabled_plugins = [first_processor, second_processor]

    result = formatting.format_body("original content", "application/json")

    assert result == "formatted twice"
    assert first_processor.format_body.call_args_list == [
        call("original content", "application/json")
    ]
    assert second_processor.format_body.call_args_list == [
        call("formatted once", "application/json")
    ]

# Generated at 2026-10-25 04:36:58.789195
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 04:37:10.659025
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():formatting = Formatting.__new__(Formatting)


class AddPrefix:
    def module_0.format_headers(self, headers):
        return "prefix:" + headers


class AddSuffix:
    def module_0.format_headers(self, headers):
        return headers + ":suffix"


formatting.enabled_plugins = [AddPrefix(), AddSuffix()]

assert formatting.format_headers("Content-Type: application/json") == (
    "prefix:Content-Type: application/json:suffix"
)

# Generated at 2026-10-25 04:37:24.992227
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 04:37:27.769395
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 04:37:54.804218
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from httpie.plugins.base import BaseFormatter


# Generated at 2026-10-25 04:38:06.093744
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import Mock


# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter(monkeypatch):
    mime = "application/json"
    converter_instance = object()

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
    unsupported_converter.supports.assert_called_once_with(mime)
    supported_converter.supports.assert_called_once_with(mime)
    supported_converter.assert_called_once_with(mime)

    # Invalid MIME types should not query the plugin registry.
    get_converters.reset_mock()

    assert Conversion.get_converter("invalid-mime") is None
    get_converters.assert_not_called()

    # Return None when no converter supports the MIME type.
    unsupported_converter.supports.reset_mock()
    get_converters.return_value = [unsupported_converter]

    assert Conversion.get_converter("text/plain") is None
    unsupported_converter.supports.assert_called_once_with("text/plain")

# Generated at 2026-10-25 04:38:08.820084
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 04:38:11.234040
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 04:38:13.649303
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 04:38:16.064518
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 04:38:18.480003
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 04:38:20.894934
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 04:38:23.311099
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 04:38:25.725272
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 04:38:32.081533
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 04:38:57.064756
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import MagicMock, patch


# Generated at 2026-10-25 04:39:04.654740
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    first_plugin = Mock()
    first_plugin.format_body.return_value = "formatted by first"

    second_plugin = Mock()
    second_plugin.format_body.return_value = "formatted by second"

    formatting = Formatting.__new__(Formatting)
    formatting.enabled_plugins = [first_plugin, second_plugin]

    result = formatting.format_body("original content", "application/json")

    first_plugin.format_body.assert_called_once_with(
        "original content", "application/json"
    )
    second_plugin.format_body.assert_called_once_with(
        "formatted by first", "application/json"
    )
    assert result == "formatted by second"

# Generated at 2026-10-25 04:39:41.198242
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 04:40:22.773312
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 04:40:25.537524
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 04:40:51.137685
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import MagicMock, patch


# Generated at 2026-10-25 04:41:15.409946
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import Mock, patch


# Generated at 2026-10-25 04:41:17.980074
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 04:41:20.618027
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 04:41:23.140357
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 04:41:25.657358
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 04:41:28.072638
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 04:41:34.863857
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 04:41:53.729637
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 04:41:56.485683
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 04:41:59.234777
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 04:42:22.171465
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import Mock, patch


# Generated at 2026-10-25 04:42:24.588462
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 04:42:27.003765
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 04:42:29.419408
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 04:42:31.833637
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 04:42:34.247824
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 04:42:36.664548
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 04:42:45.810226
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 04:43:06.408271
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import patch

# Generated at 2026-10-25 04:43:32.213717
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import Mock, call, patch


# Generated at 2026-10-25 04:43:34.631023
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 04:43:37.045386
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 04:43:39.592175
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 04:43:48.598329
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

    # Invalid MIME types must leave the content unchanged.
    result = formatting.format_body("original content", "invalid-mime")

    assert result == "original content"
    first_plugin.format_body.assert_not_called()
    second_plugin.format_body.assert_not_called()

# Generated at 2026-10-25 04:43:56.687498
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
    assert first_plugin.format_body.call_args_list == [
        call("original content", "application/json")
    ]
    assert second_plugin.format_body.call_args_list == [
        call("formatted once", "application/json")
    ]

    first_plugin.reset_mock()
    second_plugin.reset_mock()

    # Invalid MIME types should leave the content unchanged and skip plugins.
    result = formatting.format_body("original content", "invalid-mime")

    assert result == "original content"
    first_plugin.format_body.assert_not_called()
    second_plugin.format_body.assert_not_called()

# Generated at 2026-10-25 04:44:05.699120
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import Mock


def test_Conversion_get_converter(monkeypatch):
    mime = 'application/json'
    converter_instance = Mock(spec=ConverterPlugin)

    unsupported_converter = Mock()
    unsupported_converter.supports.return_value = False

    supported_converter = Mock()
    supported_converter.supports.return_value = True
    supported_converter.return_value = converter_instance

    get_converters = Mock(
        return_value=[unsupported_converter, supported_converter]
    )
    monkeypatch.setattr(
        plugin_manager,
        'get_converters',
        get_converters,
    )

    result = Conversion.get_converter(mime)

    assert result is converter_instance
    get_converters.assert_called_once_with()
    unsupported_converter.supports.assert_called_once_with(mime)
    unsupported_converter.assert_not_called()
    supported_converter.supports.assert_called_once_with(mime)
    supported_converter.assert_called_once_with(mime)

    # Invalid MIME types should not inspect the converter registry.
    get_converters.reset_mock()

    assert Conversion.get_converter('invalid-mime') is None
    get_converters.assert_not_called()

# Generated at 2026-10-25 04:44:08.545745
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 04:44:29.473739
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 04:44:31.998281
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 04:44:34.413130
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 04:44:36.950973
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 04:44:39.365811
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 04:44:50.543215
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 04:44:51.982600
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import patch

# Generated at 2026-10-25 04:44:59.359973
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    first_plugin = Mock()
    first_plugin.format_body.return_value = "first formatted"

    second_plugin = Mock()
    second_plugin.format_body.return_value = "second formatted"

    formatting = Formatting.__new__(Formatting)
    formatting.enabled_plugins = [first_plugin, second_plugin]

    result = formatting.format_body("original content", "application/json")

    assert result == "second formatted"
    first_plugin.format_body.assert_called_once_with(
        "original content", "application/json"
    )
    second_plugin.format_body.assert_called_once_with(
        "first formatted", "application/json"
    )

# Generated at 2026-10-25 04:45:02.223511
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 04:45:15.535486
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from unittest.mock import Mock

formatter = Formatting.__new__(Formatting)

first = Mock()
first.format_headers.side_effect = lambda headers: headers + "\nFirst"

second = Mock()
second.format_headers.side_effect = lambda headers: headers + "\nSecond"

formatter.enabled_plugins = [first, second]

result = formatter.format_headers("Content-Type: application/json")

assert result == "Content-Type: application/json\nFirst\nSecond"
first.format_headers.assert_called_once_with("Content-Type: application/json")
second.format_headers.assert_called_once_with("Content-Type: application/json\nFirst")

# Generated at 2026-10-25 04:45:40.641884
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import patch


# Generated at 2026-10-25 04:45:51.079606
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    first_processor = Mock()
    first_processor.format_body.return_value = '{"formatted": true}'

    second_processor = Mock()
    second_processor.format_body.return_value = 'FINAL'

    formatting = Formatting.__new__(Formatting)
    formatting.enabled_plugins = [first_processor, second_processor]

    result = formatting.format_body('{"formatted":false}', 'application/json')

    assert result == 'FINAL'
    first_processor.format_body.assert_called_once_with(
        '{"formatted":false}',
        'application/json',
    )
    second_processor.format_body.assert_called_once_with(
        '{"formatted": true}',
        'application/json',
    )


def test_Formatting_format_body_with_invalid_mime():
    processor = Mock()

    formatting = Formatting.__new__(Formatting)
    formatting.enabled_plugins = [processor]

    result = formatting.format_body('unchanged content', 'invalid-mime')

    assert result == 'unchanged content'
    processor.format_body.assert_not_called()

# Generated at 2026-10-25 04:45:53.933955
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 04:46:15.439847
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 04:46:36.537500
# Unit test for method format_headers of class Formatting