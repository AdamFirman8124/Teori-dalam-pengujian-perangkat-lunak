

# Generated at 2026-10-25 12:00:35.819129
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 12:00:38.231286
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 12:00:40.648005
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 12:00:43.061378
# Unit test for function is_valid_mime

# Generated at 2026-10-25 12:00:45.476003
# Unit test for function is_valid_mime

# Generated at 2026-10-25 12:00:47.888907
# Unit test for function is_valid_mime

# Generated at 2026-10-25 12:01:27.577712
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from httpie.plugins import FormatterPlugin

    class UpperCaseHeadersPlugin(FormatterPlugin):
        def module_0.format_headers(self, headers: str) -> str:
            return headers.upper()

    class AppendHeaderPlugin(FormatterPlugin):
        def module_0.format_headers(self, headers: str) -> str:
            return headers + '\nX-Injected: yes'

    class DisabledPlugin(FormatterPlugin):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.enabled = False

        def module_0.format_headers(self, headers: str) -> str:
            return 'SHOULD NOT APPEAR'

    headers = 'Content-Type: application/json\nContent-Length: 13'
    expected = headers.upper() + '\nX-INJECTED: YES'

    plugin_manager.register(UpperCaseHeadersPlugin)
    plugin_manager.register(AppendHeaderPlugin)
    plugin_manager.register(DisabledPlugin)
    try:
        formatting = Formatting(groups=['format'])

        # Disabled plugins must be excluded from enabled_plugins
        enabled_types = [type(p) for p in formatting.enabled_plugins]
        assert DisabledPlugin not in enabled_types
        assert UpperCaseHeadersPlugin in enabled_types
        assert AppendHeaderPlugin in enabled_types

        # All enabled plugins are applied in registration order
        result = formatting.format_headers(headers)
        assert result == expected
    finally:
        plugin_manager.unregister(UpperCaseHeadersPlugin)
        plugin_manager.unregister(AppendHeaderPlugin)
        plugin_manager.unregister(DisabledPlugin)

# Generated at 2026-10-25 12:01:29.994071
# Unit test for function is_valid_mime

# Generated at 2026-10-25 12:01:32.410235
# Unit test for function is_valid_mime

# Generated at 2026-10-25 12:01:34.823573
# Unit test for function is_valid_mime

# Generated at 2026-10-25 12:01:37.237543
# Unit test for function is_valid_mime

# Generated at 2026-10-25 12:01:39.651242
# Unit test for function is_valid_mime

# Generated at 2026-10-25 12:01:42.068171
# Unit test for function is_valid_mime

# Generated at 2026-10-25 12:01:44.483428
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 12:01:46.987845
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 12:01:49.323295
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 12:01:51.737685
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 12:01:53.181133
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import patch

# Generated at 2026-10-25 12:01:55.946512
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 12:01:57.482282
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import patch

# Generated at 2026-10-25 12:02:00.354967
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 12:02:01.709177
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import patch

# Generated at 2026-10-25 12:02:07.665684
# Unit test for function is_valid_mime
def test_is_valid_mime():
    # Valid MIME types -> True
    assert module_0.is_valid_mime('application/json') is not None
    assert module_0.is_valid_mime('text/plain') is not None
    assert module_0.is_valid_mime('image/png') is not None
    assert module_0.is_valid_mime('application/vnd.api+json') is not None  # subtype with +
    assert module_0.is_valid_mime('text/html; charset=utf-8') is not None  # with parameters

    # Invalid MIME types -> None (falsy)
    assert module_0.is_valid_mime('') is None
    assert module_0.is_valid_mime(None) is None
    assert module_0.is_valid_mime('noslash') is None
    assert module_0.is_valid_mime('too/many/slashes') is None
    assert module_0.is_valid_mime('/empty-type') is None
    assert module_0.is_valid_mime('empty-subtype/') is None

# Generated at 2026-10-25 12:02:10.678417
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 12:02:12.113378
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import patch

# Generated at 2026-10-25 12:02:15.109359
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 12:02:17.659867
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 12:02:20.312337
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 12:02:22.886502
# Unit test for function is_valid_mime

# Generated at 2026-10-25 12:02:25.548564
# Unit test for function is_valid_mime

# Generated at 2026-10-25 12:02:27.964802
# Unit test for function is_valid_mime

# Generated at 2026-10-25 12:02:30.382354
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 12:02:32.799826
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 12:02:35.212409
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 12:02:37.624815
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 12:02:40.041419
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 12:02:42.454532
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 12:02:44.885612
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 12:02:47.296405
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 12:02:49.711775
# Unit test for constructor of class Formatting

# Generated at 2026-10-25 12:02:52.124875
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 12:02:54.539432
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 12:03:12.645907
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 12:03:15.620941
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 12:03:17.171238
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import patch

# Generated at 2026-10-25 12:03:33.228403
# Unit test for constructor of class Formatting
def test_Formatting():from unittest.mock import Mock

import your_module  # replace with the module containing Formatting


def test_formatting_constructor_loads_only_enabled_plugins(monkeypatch):
    env = object()

    enabled_plugin = Mock()
    enabled_plugin.enabled = True

    disabled_plugin = Mock()
    disabled_plugin.enabled = False

    enabled_formatter = Mock(return_value=enabled_plugin)
    disabled_formatter = Mock(return_value=disabled_plugin)

    grouped_formatters = {
        "headers": [enabled_formatter],
        "body": [disabled_formatter],
    }

    monkeypatch.setattr(
        your_module.plugin_manager,
        "get_formatters_grouped",
        Mock(return_value=grouped_formatters),
    )

    formatting = your_module.Formatting(
        groups=["headers", "body"],
        env=env,
        option=True,
    )

    your_module.plugin_manager.get_formatters_grouped.assert_called_once_with()

    enabled_formatter.assert_called_once_with(
        env=env,
        option=True,
    )
    disabled_formatter.assert_called_once_with(
        env=env,
        option=True,
    )

    assert formatting.enabled_plugins == [enabled_plugin]

# Generated at 2026-10-25 12:04:20.824192
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 12:04:23.238063
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 12:05:03.646946
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 12:05:51.269489
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 12:06:03.860258
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():formatting = Formatting(groups=[])

# Generated at 2026-10-25 12:06:13.689262
# Unit test for method format_headers of class Formatting

# Generated at 2026-10-25 12:06:26.192763
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():formatter = Formatting(groups=[])

# Generated at 2026-10-25 12:06:48.128439
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 12:06:53.116185
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():formatting = Formatting(groups=[])

# Generated at 2026-10-25 12:07:52.405061
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 12:08:41.042826
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():assert Conversion.get_converter("not-a-mime") is None

# Generated at 2026-10-25 12:08:44.730007
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 12:08:56.608211
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():assert Conversion.get_converter("not-a-valid-mime") is None

# Generated at 2026-10-25 12:08:59.680815
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 12:09:01.114489
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():formatting = Formatting(groups=[])

# Generated at 2026-10-25 12:09:38.877411
# Unit test for method get_converter of class Conversion

# Generated at 2026-10-25 12:10:25.401231
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():assert Conversion.get_converter("not-a-valid-mime") is None

# Generated at 2026-10-25 12:10:28.667520
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 12:10:30.101019
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():formatting = Formatting(groups=[])

# Generated at 2026-10-25 12:10:34.605990
# Unit test for method format_body of class Formatting

# Generated at 2026-10-25 12:10:37.166729
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():formatting = Formatting(groups=[])