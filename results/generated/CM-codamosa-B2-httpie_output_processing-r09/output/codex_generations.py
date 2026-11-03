

# Generated at 2026-11-01 23:11:29.688057
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    class DummyConverter(ConverterPlugin):
        @classmethod
        def supports(cls, mime):
            return mime == 'application/json'

        def convert(self, body):
            return body

    # Valid mime with a supporting converter registered
    with mock.patch.object(plugin_manager, 'get_converters', return_value=[DummyConverter]):
        converter = Conversion.get_converter('application/json')
        assert converter is not None
        assert isinstance(converter, DummyConverter)
        assert converter.mime == 'application/json'

        # Valid mime but no converter supports it
        assert Conversion.get_converter('text/plain') is None

    # No converters registered at all
    with mock.patch.object(plugin_manager, 'get_converters', return_value=[]):
        assert Conversion.get_converter('application/json') is None

    # Invalid mimes return None without touching plugins
    with mock.patch.object(plugin_manager, 'get_converters') as m:
        assert Conversion.get_converter('invalid-mime') is None
        assert Conversion.get_converter('') is None
        assert Conversion.get_converter(None) is None
        assert not m.called

# Generated at 2026-11-01 23:12:20.145338
# Unit test for method get_converter of class Conversion
def test_Conversion_get_converter():
    # Case 1: invalid or missing mime -> None, plugin manager never queried
    with patch.object(plugin_manager, 'get_converters') as mock_get_converters:
        assert Conversion.get_converter('not-a-mime') is None
        assert Conversion.get_converter('a/b/c') is None
        assert Conversion.get_converter('') is None
        assert Conversion.get_converter(None) is None
        mock_get_converters.assert_not_called()

    # Case 2: valid mime, but no registered converter supports it -> None
    unsupported = MagicMock()
    unsupported.supports.return_value = False
    with patch.object(plugin_manager, 'get_converters', return_value=[unsupported]):
        assert Conversion.get_converter('application/json') is None
        unsupported.supports.assert_called_once_with('application/json')

    # Case 3: valid mime and a converter supports it -> converter instance
    matching = MagicMock()
    matching.supports.return_value = True
    instance = MagicMock()
    matching.return_value = instance
    with patch.object(plugin_manager, 'get_converters', return_value=[unsupported, matching]):
        converter = Conversion.get_converter('text/plain')
        assert converter is instance
        matching.supports.assert_called_once_with('text/plain')
        matching.assert_called_once_with('text/plain')

    # Case 4: the first supporting converter wins
    second_matching = MagicMock()
    second_matching.supports.return_value = True
    second_instance = MagicMock()
    second_matching.return_value = second_instance
    with patch.object(plugin_manager, 'get_converters',
                      return_value=[matching, second_matching]):
        assert Conversion.get_converter('text/plain') is instance

# Generated at 2026-11-01 23:12:59.457616
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from unittest import mock

    class UpperCaseFormatter:
        def __init__(self, env=None, **kwargs):
            self.env = env
            self.kwargs = kwargs
            self.enabled = True

        def module_0.format_headers(self, headers):
            return headers.upper()

    class SuffixFormatter:
        def __init__(self, env=None, **kwargs):
            self.env = env
            self.kwargs = kwargs
            self.enabled = True

        def module_0.format_headers(self, headers):
            return headers + '|suffix'

    class DisabledFormatter:
        def __init__(self, env=None, **kwargs):
            self.enabled = False

        def module_0.format_headers(self, headers):
            raise AssertionError('disabled formatter must not be invoked')

    grouped = {
        'upper': [UpperCaseFormatter],
        'suffix': [SuffixFormatter],
        'disabled': [DisabledFormatter],
        'chain': [UpperCaseFormatter, SuffixFormatter],
    }

    with mock.patch.object(plugin_manager, 'get_formatters_grouped',
                           return_value=grouped):
        # Single active formatter
        formatting = Formatting(groups=['upper'])
        assert len(formatting.enabled_plugins) == 1
        assert isinstance(formatting.enabled_plugins[0], UpperCaseFormatter)
        assert formatting.format_headers(
            'Content-Type: application/json'
        ) == 'CONTENT-TYPE: APPLICATION/JSON'

        # Empty headers string passes through
        assert formatting.format_headers('') == ''

        # Multiple formators chained in group order
        chain = Formatting(groups=['chain'])
        assert len(chain.enabled_plugins) == 2
        assert chain.format_headers('x-header: value') == 'X-HEADER: VALUE|suffix'

        # Disabled formatters are skipped entirely
        disabled = Formatting(groups=['disabled'])
        assert disabled.enabled_plugins == []
        assert disabled.format_headers('untouched') == 'untouched'

# Generated at 2026-11-01 23:13:17.169867
# Unit test for constructor of class Formatting
def test_Formatting():
    # Empty groups should result in no enabled plugins
    formatting = Formatting(groups=[])
    assert formatting.enabled_plugins == []

    # Each group's plugins should be instantiated (may all be disabled by default)
    formatting = Formatting(groups=['formatting'])
    assert isinstance(formatting.enabled_plugins, list)
    for plugin in formatting.enabled_plugins:
        assert plugin.enabled is True

    # Unknown group should raise KeyError
    with pytest.raises(KeyError):
        Formatting(groups=['nonexistent_group'])

# Generated at 2026-11-01 23:14:07.981608
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    calls = []

    class EnabledFormatter:
        enabled = True

        def __init__(self, env=None, **kwargs):
            self.env = env
            self.kwargs = kwargs

        def module_0.format_headers(self, headers):
            calls.append(headers)
            return headers + '\nX-Mock: yes'

    class DisabledFormatter:
        enabled = False

        def __init__(self, env=None, **kwargs):
            pass

        def module_0.format_headers(self, headers):
            raise AssertionError('disabled formatter must not be invoked')

    with patch.object(plugin_manager, 'get_formatters_grouped') as grouped:
        grouped.return_value = {
            'headers': [EnabledFormatter, DisabledFormatter],
            'format': [],
        }

        formatting = Formatting(['headers', 'format'], env=Environment(), sort_headers=True)

        # Only enabled plugins are instantiated and kept
        assert len(formating.enabled_plugins) == 1 if False else len(formatting.enabled_plugins) == 1
        assert isinstance(formatting.enabled_plugins[0], EnabledFormatter)
        assert formatting.enabled_plugins[0].kwargs == {'sort_headers': True}

        headers = 'Content-Type: text/plain'
        assert formatting.format_headers(headers) == headers + '\nX-Mock: yes'
        assert calls == [headers]

        grouped.assert_called_once_with()


def test_Formatting_format_headers_multiple_plugins_chained():
    class Upper:
        enabled = True

        def __init__(self, env=None, **kwargs):
            pass

        def module_0.format_headers(self, headers):
            return headers.upper()

    class Bracket:
        enabled = True

        def __init__(self, env=None, **kwargs):
            pass

        def module_0.format_headers(self, headers):
            return '[{}]'.format(headers)

    with patch.object(plugin_manager, 'get_formatters_grouped',
                      return_value={'g1': [Upper], 'g2': [Bracket]}):
        formatting = Formatting(['g1', 'g2'])
        # Plugins are applied in group order, output of one feeds the next
        assert formatting.format_headers('a: b') == '[A: B]'


def test_Formatting_format_headers_no_plugins():
    with patch.object(plugin_manager, 'get_formatters_grouped', return_value={'g': []}):
        formatting = Formatting(['g'])
        # With no plugins enabled, headers pass through unchanged
        assert formatting.format_headers('A: b') == 'A: b'

# Generated at 2026-11-01 23:15:32.344858
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    from httpie.plugins import FormatterPlugin

    class PrefixFormatter(FormatterPlugin):
        group_name = 'utest_prefix'

        def module_0.format_body(self, content, mime):
            return 'P:' + content

    class SuffixFormatter(FormatterPlugin):
        group_name = 'utest_suffix'

        def module_0.format_body(self, content, mime):
            return content + ':S'

    plugin_manager.register(PrefixFormatter, SuffixFormatter)

# Generated at 2026-11-01 23:17:12.192512
# Unit test for constructor of class Formatting
def test_Formatting():
    class FakeFormatter:
        enabled = True

        def __init__(self, env=None, **kwargs):
            self.env = env
            self.kwargs = kwargs

    class DisabledFormatter(FakeFormatter):
        enabled = False

    fake_groups = {
        'format': [FakeFormatter, DisabledFormatter],
        'colors': [FakeFormatter],
    }

    env = Environment()
    with patch.object(plugin_manager, 'get_formatters_grouped', return_value=fake_groups):
        formatting = Formatting(groups=['format', 'colors'], env=env, pretty=True, foo='bar')

        assert isinstance(formatting, Formatting)
        assert len(formatting.enabled_plugins) == 2
        assert all(p.enabled for p in formatting.enabled_plugins)
        assert all(isinstance(p, FakeFormatter) for p in formatting.enabled_plugins)
        assert formatting.enabled_plugins[0].env is env
        assert formatting.enabled_plugins[0].kwargs == {'pretty': True, 'foo': 'bar'}

        # Empty groups should produce no enabled plugins
        empty_formatting = Formatting(groups=[], env=env)
        assert empty_formatting.enabled_plugins == []

        # Unknown group should raise KeyError
        try:
            Formatting(groups=['nonexistent_group'])
            raised = False
        except KeyError:
            raised = True
        assert raised

# Generated at 2026-11-01 23:17:52.527907
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    groups = {'upper': [UpperCaseFormatter], 'suffix': [SuffixFormatter]}

    with patch.object(plugin_manager, 'get_formatters_grouped', return_value=groups):
        # Valid mime: a single enabled plugin transforms the content
        formatting = Formatting(['upper'], env=Environment())
        assert len(formatting.enabled_plugins) == 1
        assert formatting.format_body('body', 'application/json') == 'BODY'

        # Multiple groups: plugins are applied in order, chaining the content
        formatting = Formatting(['upper', 'suffix'], env=Environment())
        assert len(formatting.enabled_plugins) == 2
        assert formatting.format_body('body', 'text/plain') == 'BODY<text/plain>'

        # Invalid mime: content returned unchanged (plugins must not run,
        # otherwise the uppercase transformation would be visible)
        assert formatting.format_body('body', 'invalid') == 'body'
        assert formatting.format_body('body', 'no-slash') == 'body'
        assert formatting.format_body('body', 'trailing/') == 'body'
        assert formatting.format_body('body', '') == 'body'
        assert formatting.format_body('body', None) == 'body'

    # Disabled plugins are not instantiated and therefore not applied
    try:
        UpperCaseFormatter.enabled = False
        with patch.object(plugin_manager, 'get_formatters_grouped', return_value=groups):
            formatting = Formatting(['upper'], env=Environment())
            assert len(formatting.enabled_plugins) == 0
            assert formatting.format_body('body', 'application/json') == 'body'
    finally:
        UpperCaseFormatter.enabled = True

# Generated at 2026-11-01 23:18:32.360849
# Unit test for method format_headers of class Formatting
def test_Formatting_format_headers():
    from unittest.mock import patch

    class FormatterA:
        def __init__(self, *args, **kwargs):
            self.enabled = True

        def module_0.format_headers(self, headers):
            return headers + '-A'

    class FormatterB:
        def __init__(self, *args, **kwargs):
            self.enabled = True

        def module_0.format_headers(self, headers):
            return headers + '-B'

    class DisabledFormatter:
        def __init__(self, *args, **kwargs):
            self.enabled = False

        def module_0.format_headers(self, headers):
            return headers + '-disabled'

    plugins = {
        'group1': [FormatterA],
        'group2': [DisabledFormatter, FormatterB],
    }

    with patch.object(plugin_manager, 'get_formatters_grouped', return_value=plugins):
        formatting = Formatting(['group1', 'group2'])

        # Only enabled plugins are collected, in group order
        assert len(formatting.enabled_plugins) == 2
        assert isinstance(formatting.enabled_plugins[0], FormatterA)
        assert isinstance(formatting.enabled_plugins[1], FormatterB)

        # Headers are piped through each enabled plugin in order
        assert formatting.format_headers('headers') == 'headers-A-B'

        # Empty input is still passed through the chain
        assert formatting.format_headers('') == '-A-B'

    # No groups -> no plugins -> headers returned unchanged
    with patch.object(plugin_manager, 'get_formatters_grouped', return_value=plugins):
        formatting = Formatting([])
        assert formatting.enabled_plugins == []
        assert formatting.format_headers('headers') == 'headers'

# Generated at 2026-11-01 23:19:14.254603
# Unit test for constructor of class Formatting
def test_Formatting():
    from httpie.plugins.base import BaseFormatter

    class DummyFormatter(BaseFormatter):
        group_name = 'dummy'

    class DisabledFormatter(BaseFormatter):
        group_name = 'disabled'

        @property
        def enabled(self):
            return False

    # Empty groups -> no plugins enabled
    formatting = Formatting(groups=[])
    assert isinstance(formatting, Formatting)
    assert formatting.enabled_plugins == []

    plugin_manager.register(DummyFormatter)
    plugin_manager.register(DisabledFormatter)
    try:
        # Plugins from requested groups get instantiated; only enabled ones kept
        formatting = Formatting(groups=['dummy', 'disabled'], env=Environment())
        assert len(formatting.enabled_plugins) == 1
        assert isinstance(formatting.enabled_plugins[0], DummyFormatter)
        assert formatting.enabled_plugins[0].env is not None

        # Extra kwargs are forwarded to the plugin constructors
        formatting = Formatting(
            groups=['dummy'],
            env=Environment(),
            sort_headers=True,
            pretty_options={'format': True},
        )
        assert len(formatting.enabled_plugins) == 1
        assert formatting.enabled_plugins[0].kwargs == {
            'sort_headers': True,
            'pretty_options': {'format': True},
        }
    finally:
        plugin_manager.unregister(DummyFormatter)
        plugin_manager.unregister(DisabledFormatter)

    # Requesting an unregistered group raises KeyError
    raised = False
    try:
        Formatting(groups=['nonexistent_group'])
    except KeyError:
        raised = True
    assert raised

# Generated at 2026-11-01 23:19:55.204906
# Unit test for method format_body of class Formatting
def test_Formatting_format_body():
    class UpperFormatter(FormatterPlugin):
        def module_0.format_body(self, content, mime):
            return content.upper()

    class SuffixFormatter(FormatterPlugin):
        def module_0.format_body(self, content, mime):
            return content + '!'

    with mock.patch.object(
        plugin_manager,
        'get_formatters_grouped',
        return_value={'format': [UpperFormatter, SuffixFormatter]},
    ):
        formatting = Formatting(groups=['format'])

    # Valid MIME: each enabled plugin is applied in order.
    assert formatting.format_body('data', 'text/plain') == 'DATA!'

    # Invalid MIME (no slash): content is returned unchanged.
    assert formatting.format_body('data', 'invalid-mime') == 'data'

    # Empty MIME: content is returned unchanged.
    assert formatting.format_body('data', '') == 'data'