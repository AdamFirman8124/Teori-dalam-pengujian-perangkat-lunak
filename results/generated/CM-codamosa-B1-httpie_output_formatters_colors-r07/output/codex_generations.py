

# Generated at 2026-10-24 22:28:23.365807
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    class StubEnvironment:
        def __init__(self, colors):
            self.colors = colors

    # Coloring disabled.
    formatter = ColorFormatter(
        env=StubEnvironment(colors=0),
        explicit_json=True,
        color_scheme=AUTO_STYLE,
    )
    assert formatter.enabled is False

    # Auto style always uses the standard terminal formatter and HTTP lexer.
    formatter = ColorFormatter(
        env=StubEnvironment(colors=256),
        explicit_json=True,
        color_scheme=AUTO_STYLE,
    )
    assert formatter.explicit_json is True
    assert isinstance(formatter.formatter, TerminalFormatter)
    assert not isinstance(formatter.formatter, Terminal256Formatter)
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)

    # Non-256-color terminals fall back to the standard formatter.
    formatter = ColorFormatter(
        env=StubEnvironment(colors=16),
        color_scheme='monokai',
    )
    assert formatter.explicit_json is False
    assert isinstance(formatter.formatter, TerminalFormatter)
    assert not isinstance(formatter.formatter, Terminal256Formatter)
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)

    # A custom style on a 256-color terminal uses the specialized components.
    formatter = ColorFormatter(
        env=StubEnvironment(colors=256),
        color_scheme='monokai',
    )
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert isinstance(formatter.http_lexer, SimplifiedHTTPLexer)

# Generated at 2026-10-24 22:28:34.235822
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    formatter = object.__new__(ColorFormatter)
    formatter.http_lexer = Mock(name='http_lexer')
    formatter.formatter = Mock(name='formatter')

    headers = 'Content-Type: application/json\r\n'

    with patch.object(
        pygments,
        'highlight',
        return_value='\n  highlighted headers  \n',
    ) as highlight:
        result = formatter.format_headers(headers)

    assert result == 'highlighted headers'
    highlight.assert_called_once_with(
        code=headers,
        lexer=formatter.http_lexer,
        formatter=formatter.formatter,
    )

# Generated at 2026-10-24 22:29:04.017779
# Unit test for constructor of class Solarized256Style
def test_Solarized256Style():style = Solarized256Style()


# Generated at 2026-10-24 22:29:18.454503
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # A valid Pygments style should be returned unchanged.
    assert (
        ColorFormatter.get_style_class('monokai')
        is pygments.styles.get_style_by_name('monokai')
    )

    # Unknown styles should fall back to the bundled Solarized style.
    assert (
        ColorFormatter.get_style_class('unknown-style')
        is Solarized256Style
    )

# Generated at 2026-10-24 22:29:49.483327
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():from unittest.mock import Mock, patch, sentinel


# Generated at 2026-10-24 22:29:51.901934
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 22:29:54.319764
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 22:29:56.735697
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 22:30:22.660938
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 22:30:43.550463
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = ColorFormatter.__new__(ColorFormatter)

# Generated at 2026-10-24 22:31:06.987450
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = ColorFormatter.__new__(ColorFormatter)

# Generated at 2026-10-24 22:31:18.570978
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():from unittest.mock import Mock, patch


# Generated at 2026-10-24 22:31:35.673186
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    # Coloring disabled.
    formatter = ColorFormatter(
        env=SimpleNamespace(colors=0),
        explicit_json=True,
    )
    assert formatter.enabled is False

    # Automatic style always uses Pygments' standard HTTP lexer and terminal
    # formatter, even when the terminal supports 256 colors.
    formatter = ColorFormatter(
        env=SimpleNamespace(colors=256),
        explicit_json=True,
        color_scheme=AUTO_STYLE,
    )
    assert formatter.explicit_json is True
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)
    assert type(formatter.formatter) is TerminalFormatter

    # Explicit styles are ignored when 256 colors are unavailable.
    formatter = ColorFormatter(
        env=SimpleNamespace(colors=16),
        color_scheme='monokai',
    )
    assert formatter.explicit_json is False
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)
    assert type(formatter.formatter) is TerminalFormatter

    # Explicit style with 256-color support uses the simplified lexer and
    # Terminal256Formatter.
    formatter = ColorFormatter(
        env=SimpleNamespace(colors=256),
        color_scheme='monokai',
    )
    assert formatter.explicit_json is False
    assert isinstance(formatter.http_lexer, SimplifiedHTTPLexer)
    assert isinstance(formatter.formatter, Terminal256Formatter)

# Generated at 2026-10-24 22:32:00.511833
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    expected_style = pygments.styles.get_style_by_name('monokai')
    assert ColorFormatter.get_style_class('monokai') is expected_style

    assert (
        ColorFormatter.get_style_class('nonexistent-style')
        is Solarized256Style
    )

# Generated at 2026-10-24 22:32:11.514139
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 22:32:32.804945
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = ColorFormatter.__new__(ColorFormatter)

# Generated at 2026-10-24 22:32:53.291245
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = ColorFormatter.__new__(ColorFormatter)

# Generated at 2026-10-24 22:32:55.713461
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 22:32:58.128566
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 22:33:00.547716
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 22:33:02.966333
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 22:33:29.227189
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 22:33:30.561558
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 22:33:50.227524
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():import sys
from types import SimpleNamespace
from unittest.mock import Mock, patch


def test_ColorFormatter_disables_colors_when_environment_has_no_color():
    env = SimpleNamespace(colors=0)

    formatter = ColorFormatter(env=env)

    assert formatter.enabled is False


def test_ColorFormatter_uses_terminal_formatter_for_auto_style():
    env = SimpleNamespace(colors=256)
    module = sys.modules[ColorFormatter.__module__]

    http_lexer = Mock()
    terminal_formatter = Mock()

    with (
        patch.object(
            module,
            'PygmentsHttpLexer',
            return_value=http_lexer,
        ) as lexer_class,
        patch.object(
            module,
            'TerminalFormatter',
            return_value=terminal_formatter,
        ) as formatter_class,
    ):
        formatter = ColorFormatter(
            env=env,
            explicit_json=True,
            color_scheme=AUTO_STYLE,
        )

    lexer_class.assert_called_once_with()
    formatter_class.assert_called_once_with()
    assert formatter.explicit_json is True
    assert formatter.http_lexer is http_lexer
    assert formatter.formatter is terminal_formatter


def test_ColorFormatter_uses_256_formatter_for_named_style():
    env = SimpleNamespace(colors=256)
    module = sys.modules[ColorFormatter.__module__]

    http_lexer = Mock()
    terminal_formatter = Mock()
    style_class = Mock()

    with (
        patch.object(
            module,
            'SimplifiedHTTPLexer',
            return_value=http_lexer,
        ) as lexer_class,
        patch.object(
            module,
            'Terminal256Formatter',
            return_value=terminal_formatter,
        ) as formatter_class,
        patch.object(
            ColorFormatter,
            'get_style_class',
            return_value=style_class,
        ) as get_style_class,
    ):
        formatter = ColorFormatter(
            env=env,
            explicit_json=False,
            color_scheme='monokai',
        )

    lexer_class.assert_called_once_with()
    get_style_class.assert_called_once_with('monokai')
    formatter_class.assert_called_once_with(style=style_class)
    assert formatter.explicit_json is False
    assert formatter.http_lexer is http_lexer
    assert formatter.formatter is terminal_formatter

# Generated at 2026-10-24 22:33:58.931223
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():from unittest.mock import Mock, patch


# Generated at 2026-10-24 22:34:01.958604
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 22:34:04.381489
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 22:34:05.764514
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 22:34:32.544772
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # 1. A style Pygments knows about resolves to that exact class.
    assert (
        ColorFormatter.get_style_class('fruity')
        is pygments.styles.get_style_by_name('fruity')
    )
    assert issubclass(
        ColorFormatter.get_style_class('monokai'), pygments.style.Style
    )

    # 2. The bundled "solarized" style is not registered with Pygments,
    #    so the lookup raises and we fall back to Solarized256Style.
    with pytest.raises(ClassNotFound):
        pygments.styles.get_style_by_name('solarized')
    assert ColorFormatter.get_style_class('solarized') is Solarized256Style

    # 3. An unknown style name also falls back.
    assert (
        ColorFormatter.get_style_class('definitely-not-a-style')
        is Solarized256Style
    )

# Generated at 2026-10-24 22:34:50.439014
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    # Coloring disabled.
    formatter = ColorFormatter(
        env=SimpleNamespace(colors=0),
        explicit_json=True,
    )
    assert formatter.enabled is False

    # Automatic style uses the standard HTTP lexer and terminal formatter.
    formatter = ColorFormatter(
        env=SimpleNamespace(colors=256),
        explicit_json=True,
        color_scheme=AUTO_STYLE,
    )
    assert formatter.explicit_json is True
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)
    assert isinstance(formatter.formatter, TerminalFormatter)

    # Terminals without 256-color support also use the standard formatter.
    formatter = ColorFormatter(
        env=SimpleNamespace(colors=16),
        color_scheme='custom',
    )
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)
    assert isinstance(formatter.formatter, TerminalFormatter)

    # A custom scheme on a 256-color terminal uses the simplified lexer
    # and Terminal256Formatter.
    with patch.object(
        ColorFormatter,
        'get_style_class',
        return_value=Solarized256Style,
    ) as get_style_class:
        formatter = ColorFormatter(
            env=SimpleNamespace(colors=256),
            color_scheme='custom',
        )

    get_style_class.assert_called_once_with('custom')
    assert formatter.explicit_json is False
    assert isinstance(formatter.http_lexer, SimplifiedHTTPLexer)
    assert isinstance(formatter.formatter, Terminal256Formatter)

# Generated at 2026-10-24 22:35:38.105326
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 22:35:53.310993
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from types import SimpleNamespace

# Generated at 2026-10-24 22:35:54.642227
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 22:36:28.536733
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():from httpie.output.formatters.colors import ColorFormatter

# Generated at 2026-10-24 22:36:52.090888
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # Returns the requested Pygments style when it exists.
    expected_style = pygments.styles.get_style_by_name('monokai')
    assert ColorFormatter.get_style_class('monokai') is expected_style

    # Falls back to the bundled Solarized style for unknown schemes.
    assert (
        ColorFormatter.get_style_class('nonexistent-color-scheme')
        is Solarized256Style
    )

# Generated at 2026-10-24 22:37:03.744355
# Unit test for function get_lexer
def test_get_lexer():
    # Known MIME types are resolved normally.
    lexer = module_0.get_lexer('application/json')
    assert lexer is not None
    assert lexer.name == 'JSON'

    lexer = module_0.get_lexer('text/plain')
    assert isinstance(lexer, TextLexer)

    # Structured syntax suffixes fall back to their underlying format.
    lexer = module_0.get_lexer('application/vnd.example+json')
    assert lexer is not None
    assert lexer.name == 'JSON'

    # Unknown MIME types have no lexer.
    assert module_0.get_lexer('application/x-unknown-httpie-format') is None

    # --json overrides an incorrect text/plain Content-Type when the body
    # contains valid JSON.
    lexer = module_0.get_lexer(
        mime='text/plain',
        explicit_json=True,
        body='{"success": true}',
    )
    assert lexer is not None
    assert lexer.name == 'JSON'

    # Invalid JSON retains the MIME type's original lexer.
    lexer = module_0.get_lexer(
        mime='text/plain',
        explicit_json=True,
        body='not valid json',
    )
    assert isinstance(lexer, TextLexer)

    # Without --json, valid JSON served as text remains plain text.
    lexer = module_0.get_lexer(
        mime='text/plain',
        explicit_json=False,
        body='{"success": true}',
    )
    assert isinstance(lexer, TextLexer)

# Generated at 2026-10-24 22:37:06.531464
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 22:37:08.953699
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 22:37:10.290160
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 22:37:20.872260
# Unit test for function get_lexer
def test_get_lexer():
    json_lexer_type = type(pygments.lexers.get_lexer_by_name('json'))

    # Resolve directly from the MIME type.
    lexer = module_0.get_lexer('application/json')
    assert isinstance(lexer, json_lexer_type)

    # Resolve a structured syntax suffix such as vendor-type+json.
    lexer = module_0.get_lexer('application/vnd.example+json')
    assert isinstance(lexer, json_lexer_type)

    # Unknown content types have no matching lexer.
    lexer = module_0.get_lexer('application/x-httpie-unknown')
    assert lexer is None

    # --json detects valid JSON despite an incorrect Content-Type.
    lexer = module_0.get_lexer(
        'application/x-httpie-unknown',
        explicit_json=True,
        body='{"result": true}',
    )
    assert isinstance(lexer, json_lexer_type)

    # Invalid JSON must not be treated as JSON.
    lexer = module_0.get_lexer(
        'application/x-httpie-unknown',
        explicit_json=True,
        body='not valid JSON',
    )
    assert lexer is None

# Generated at 2026-10-24 22:37:30.899421
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():from unittest.mock import Mock, patch


# Generated at 2026-10-24 22:37:40.422384
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():from unittest.mock import Mock, patch


# Generated at 2026-10-24 22:37:41.754335
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 22:38:10.669536
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():env = Environment(colors=256)

# Generated at 2026-10-24 22:38:18.937772
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():from unittest.mock import Mock, patch
