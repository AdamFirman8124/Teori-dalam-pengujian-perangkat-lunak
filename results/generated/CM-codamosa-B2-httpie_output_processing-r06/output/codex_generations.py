

# Generated at 2026-11-03 05:38:06.568309
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():from unittest.mock import patch


# Generated at 2026-11-03 05:41:53.001516
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from unittest.mock import patch

    class UpperPlugin:
        def __init__(self, env=None, **kwargs):
            self.env = env
            self.enabled = True

        def module_0.format_headers(self, headers):
            return headers.upper()

    class SuffixPlugin:
        def __init__(self, env=None, **kwargs):
            self.env = env
            self.enabled = True

        def module_0.format_headers(self, headers):
            return headers + '\n'

    class DisabledPlugin:
        def __init__(self, env=None, **kwargs):
            self.enabled = False

        def module_0.format_headers(self, headers):
            raise AssertionError('disabled plugin should not be invoked')

    headers = 'Content-Type: application/json'

    # Plugins within a single group are applied in order; disabled ones are skipped
    groups = {'group': [UpperPlugin, DisabledPlugin, SuffixPlugin]}
    with patch.object(plugin_manager, 'get_formatters_grouped', return_value=groups):
        formatting = Formatting(['group'], env=Environment())
        assert len(formatting.enabled_plugins) == 2
        assert formatting.format_headers(headers) == headers.upper() + '\n'

    # Plugins from multiple groups are applied in group order
    groups = {'g1': [UpperPlugin], 'g2': [SuffixPlugin]}
    with patch.object(plugin_manager, 'get_formatters_grouped', return_value=groups):
        formatting = Formatting(['g1', 'g2'], env=Environment())
        assert formatting.format_headers(headers) == 'CONTENT-TYPE: APPLICATION/JSON\n'

    # No enabled plugins -> headers returned unchanged
    groups = {'empty': []}
    with patch.object(plugin_manager, 'get_formatters_grouped', return_value=groups):
        formatting = Formatting(['empty'], env=Environment())
        assert formatting.format_headers(headers) == headers

    # Extra kwargs are passed through to plugin constructors
    captured = {}

    class KwargPlugin:
        def __init__(self, env=None, **kwargs):
            captured.update(kwargs)
            self.enabled = True

        def module_0.format_headers(self, headers):
            return headers

    groups = {'g': [KwargPlugin]}
    with patch.object(plugin_manager, 'get_formatters_grouped', return_value=groups):
        Formatting(['g'], env=Environment(), sort_headers=True)
        assert captured == {'sort_headers': True}