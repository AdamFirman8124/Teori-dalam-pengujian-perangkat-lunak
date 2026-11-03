

# Generated at 2026-11-03 05:45:07.942415
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    from unittest.mock import patch

    class FakeFormatter:
        def __init__(self, env=None, **kwargs):
            self.env = env
            self.kwargs = kwargs
            self.enabled = True

        def format_headers(self, headers):
            return headers

        def module_0.format_body(self, content, mime):
            return content + '-formatted'

    class AnotherFormatter(FakeFormatter):
        def module_0.format_body(self, content, mime):
            return content + '-more'

    class DisabledFormatter(FakeFormatter):
        def __init__(self, env=None, **kwargs):
            super().__init__(env=env, **kwargs)
            self.enabled = False

    # Valid mime: enabled plugins are applied in order (chained)
    with patch.object(plugin_manager, 'get_formatters_grouped',
                      return_value={'group': [FakeFormatter, AnotherFormatter]}):
        formatting = Formatting(groups=['group'])
        assert formatting.format_body('body', 'application/json') == 'body-formatted-more'
        assert formatting.format_body('', 'text/plain') == '-formatted-more'

        # env and kwargs are forwarded to the plugin constructors
        formatting = Formatting(groups=['group'], env=None, foo='bar')
        assert formatting.enabled_plugins[0].kwargs == {'foo': 'bar'}
        assert formatting.enabled_plugins[0].env is None

    # Invalid / missing mime: content is returned unchanged, plugins skipped
    with patch.object(plugin_manager, 'get_formatters_grouped',
                      return_value={'group': [FakeFormatter]}):
        formatting = Formatting(groups=['group'])
        assert formatting.format_body('body', 'invalid') == 'body'
        assert formatting.format_body('body', 'a/b/c') == 'body'
        assert formatting.format_body('body', '') == 'body'
        assert formatting.format_body('body', None) == 'body'

    # Disabled plugins are not added and thus not applied
    with patch.object(plugin_manager, 'get_formatters_grouped',
                      return_value={'group': [DisabledFormatter]}):
        formatting = Formatting(groups=['group'])
        assert formatting.enabled_plugins == []
        assert formatting.format_body('body', 'application/json') == 'body'

    # Unknown group: no plugins enabled, content returned unchanged
    with patch.object(plugin_manager, 'get_formatters_grouped', return_value={}):
        formatting = Formatting(groups=['unknown'])
        assert formatting.format_body('body', 'application/json') == 'body'

# Generated at 2026-11-03 05:47:06.442079
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    class UpperCasingFormatter(FormatterPlugin):
        def module_0.format_headers(self, headers: str) -> str:
            return headers.upper()

    with patch.object(
        plugin_manager,
        'get_formatters_grouped',
        return_value={'formatting': [UpperCasingFormatter]},
    ):
        formatting = Formatting(groups=['formatting'])
        assert len(formatting.enabled_plugins) == 1
        assert formatting.format_headers('HTTP/1.1 200 OK') == 'HTTP/1.1 200 OK'.upper()


def test_Formatting_format_headers_no_plugins():
    with patch.object(plugin_manager, 'get_formatters_grouped', return_value={}):
        formatting = Formatting(groups=['formatting'])
        assert formatting.enabled_plugins == []
        assert formatting.format_headers('HTTP/1.1 200 OK') == 'HTTP/1.1 200 OK'


def test_Formatting_format_headers_disabled_plugin_skipped():
    class DisabledFormatter(FormatterPlugin):
        enabled = False

        def module_0.format_headers(self, headers: str) -> str:
            return headers.upper()

    with patch.object(
        plugin_manager,
        'get_formatters_grouped',
        return_value={'formatting': [DisabledFormatter]},
    ):
        formatting = Formatting(groups=['formatting'])
        assert formatting.enabled_plugins == []
        assert formatting.format_headers('HTTP/1.1 200 OK') == 'HTTP/1.1 200 OK'


def test_Formatting_format_headers_multiple_plugins_in_order():
    class AppendA(FormatterPlugin):
        def module_0.format_headers(self, headers: str) -> str:
            return headers + 'A'

    class AppendB(FormatterPlugin):
        def module_0.format_headers(self, headers: str) -> str:
            return headers + 'B'

    with patch.object(
        plugin_manager,
        'get_formatters_grouped',
        return_value={'formatting': [AppendA, AppendB]},
    ):
        formatting = Formatting(groups=['formatting'])
        assert formatting.format_headers('X') == 'XAB'

# nonce:cba76522

# Generated at 2026-11-03 05:50:49.047825
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():from httpie.plugins import FormatterPlugin


# Generated at 2026-11-03 05:51:59.037345
# Unit test for constructor of class Conversion
def test_Conversion():
    """
    Test that the Conversion class can be instantiated.

    Conversion only exposes static methods, but its constructor
    should still work without any arguments.
    """
    conversion = Conversion()
    assert conversion is not None
    assert isinstance(conversion, Conversion)