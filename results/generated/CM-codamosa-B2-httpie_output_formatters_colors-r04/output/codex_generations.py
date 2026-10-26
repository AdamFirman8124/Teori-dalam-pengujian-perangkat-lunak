

# Generated at 2026-10-25 14:08:44.198065
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 14:08:54.039243
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 14:09:21.076680
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():formatter = ColorFormatter.__new__(ColorFormatter)

# Generated at 2026-10-25 14:09:23.496121
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 14:09:24.933283
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 14:09:26.279044
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 14:09:40.921350
# Unit test for constructor of class Solarized256Style
def test_Solarized256Style():
    # Act: constructor requires no arguments
    style = Solarized256Style()

    # Assert: instance created correctly
    assert isinstance(style, pygments.style.Style)
    assert isinstance(style, Solarized256Style)

    # Assert: palette constants defined
    assert Solarized256Style.BASE03 == "#1c1c1c"
    assert Solarized256Style.BASE02 == "#262626"
    assert Solarized256Style.BASE01 == "#4e4e4e"
    assert Solarized256Style.BASE00 == "#585858"
    assert Solarized256Style.BASE0 == "#808080"
    assert Solarized256Style.BASE1 == "#8a8a8a"
    assert Solarized256Style.BASE2 == "#d7d7af"
    assert Solarized256Style.BASE3 == "#ffffd7"
    assert Solarized256Style.YELLOW == "#af8700"
    assert Solarized256Style.ORANGE == "#d75f00"
    assert Solarized256Style.RED == "#af0000"
    assert Solarized256Style.MAGENTA == "#af005f"
    assert Solarized256Style.VIOLET == "#5f5faf"
    assert Solarized256Style.BLUE == "#0087ff"
    assert Solarized256Style.CYAN == "#00afaf"
    assert Solarized256Style.GREEN == "#5f8700"

    # Assert: background and key mappings
    assert style.background_color == Solarized256Style.BASE03
    assert Solarized256Style.styles[pygments.token.Keyword] == Solarized256Style.GREEN
    assert Solarized256Style.styles[pygments.token.Keyword.Reserved] == Solarized256Style.BLUE
    assert Solarized256Style.styles[pygments.token.Name.Attribute] == Solarized256Style.BASE1
    assert Solarized256Style.styles[pygments.token.Name.Exception] == Solarized256Style.YELLOW
    assert Solarized256Style.styles[pygments.token.String] == Solarized256Style.CYAN
    assert Solarized256Style.styles[pygments.token.Number] == Solarized256Style.CYAN
    assert Solarized256Style.styles[pygments.token.Operator] == Solarized256Style.BASE1
    assert Solarized256Style.styles[pygments.token.Comment] == Solarized256Style.BASE01

# Generated at 2026-10-25 14:09:57.489071
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():import json

import pytest

# Adjust this import to wherever the module lives in your tree
# (e.g. httpie/output/formatters/colors.py or httpie/plugins/...)
from httpie.output.formatters.colors import ColorFormatter
from httpie.context import Environment


def make_formatter(explicit_json=False):
    return ColorFormatter(
        env=Environment(colors=256),
        explicit_json=explicit_json,
        color_scheme='solarized',
    )


def test_json_body_is_colorized():
    body = json.dumps({'status': 'ok', 'count': 3})
    result = make_formatter().format_body(body, 'application/json')
    assert result != body
    assert '\x1b[' in result  # contains ANSI escape codes


def test_plain_text_body_unchanged():
    body = 'just some plain text'
    result = make_formatter().format_body(body, 'text/plain')
    assert result == body


def test_explicit_json_with_wrong_content_type():
    body = '{"a": 1}'
    result = make_formatter(explicit_json=True).format_body(body, 'text/plain')
    assert result != body
    assert '\x1b[' in result


def test_explicit_json_invalid_body_unchanged():
    body = 'not json {'
    result = make_formatter(explicit_json=True).format_body(body, 'text/plain')
    assert result == body


def test_xml_body_is_colorized():
    body = '<root><item>1</item></root>'
    result = make_formatter().format_body(body, 'application/xml')
    assert result != body
    assert '\x1b[' in result

# Generated at 2026-10-25 14:10:00.251429
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    # 256 colors + auto style -> simplified lexer and terminal256 formatter
    env = Environment(colors=256)
    formatter = ColorFormatter(env=env)
    assert formatter.enabled
    assert formatter.explicit_json is False
    assert isinstance(formatter.http_lexer, SimplifiedHTTPLexer)
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert ColorFormatter.get_style_class(AUTO_STYLE) is Solarized256Style

    # 256 colors + explicit_json -> flag is stored
    formatter = ColorFormatter(env=Environment(colors=256), explicit_json=True)
    assert formatter.explicit_json is True

    # 256 colors + known pygments style -> resolved by name
    formatter = ColorFormatter(env=Environment(colors=256), color_scheme='monokai')
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert ColorFormatter.get_style_class('monokai') is \
        pygments.styles.get_style_by_name('monokai')

    # 256 colors + unknown style -> falls back to Solarized256Style
    assert ColorFormatter.get_style_class('no-such-style') is Solarized256Style

    # Fewer than 256 colors -> plain terminal formatter and stock HTTP lexer
    env = Environment(colors=16)
    formatter = ColorFormatter(env=env)
    assert formatter.enabled
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)
    assert isinstance(formatter.formatter, TerminalFormatter)

    # No colors -> formatter disabled
    env = Environment(colors=False)
    formatter = ColorFormatter(env=env)
    assert not formatter.enabled

# Generated at 2026-10-25 14:10:16.733870
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():import json

import pytest

# Adjust this import to wherever the module lives in your tree
# (e.g. httpie/output/formatters/colors.py or httpie/plugins/...)
from httpie.output.formatters.colors import ColorFormatter
from httpie.context import Environment


def make_formatter(explicit_json=False):
    return ColorFormatter(
        env=Environment(colors=256),
        explicit_json=explicit_json,
        color_scheme='solarized',
    )


def test_json_body_is_colorized():
    body = json.dumps({'status': 'ok', 'count': 3})
    result = make_formatter().format_body(body, 'application/json')
    assert result != body
    assert '\x1b[' in result  # contains ANSI escape codes


def test_plain_text_body_unchanged():
    body = 'just some plain text'
    result = make_formatter().format_body(body, 'text/plain')
    assert result == body


def test_explicit_json_with_wrong_content_type():
    body = '{"a": 1}'
    result = make_formatter(explicit_json=True).format_body(body, 'text/plain')
    assert result != body
    assert '\x1b[' in result


def test_explicit_json_invalid_body_unchanged():
    body = 'not json {'
    result = make_formatter(explicit_json=True).format_body(body, 'text/plain')
    assert result == body


def test_xml_body_is_colorized():
    body = '<root><item>1</item></root>'
    result = make_formatter().format_body(body, 'application/xml')
    assert result != body
    assert '\x1b[' in result

# Generated at 2026-10-25 14:10:19.268635
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 14:10:21.685422
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 14:10:24.233648
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 14:10:26.847850
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from unittest.mock import Mock

    # 256-color terminal so the 256-color formatter path is exercised
    env = Mock(colors=256)
    color_formatter = ColorFormatter(
        env=env,
        explicit_json=True,
        color_scheme='monokai',
    )

    # 1. Known JSON mime type -> body is highlighted with the JSON lexer
    json_body = json.dumps({'foo': 'bar', 'baz': [1, 2, 3]})
    result = color_formatter.format_body(json_body, 'application/json')
    assert 'foo' in result
    assert 'bar' in result
    assert result != json_body  # escape codes added

    # 2. Subtype-suffix mime type (e.g. application/vnd.api+json)
    result = color_formatter.format_body(json_body, 'application/vnd.api+json')
    assert 'foo' in result
    assert 'bar' in result

    # 3. Wrong Content-Type but --json given and body parses as JSON
    #    -> falls back to the JSON lexer
    result = color_formatter.format_body(json_body, 'text/plain')
    assert 'foo' in result
    assert 'bar' in result

    # 4. Wrong Content-Type, body NOT valid JSON, no --json fallback possible
    #    -> returned (highlighted as plain text) without crashing
    text_body = 'Just some plain text.'
    result = color_formatter.format_body(text_body, 'text/plain')
    assert 'Just some plain text.' in result

    # 5. Unknown mime type with non-JSON body -> body returned intact
    result = color_formatter.format_body(text_body, 'application/x-unknown')
    assert 'Just some plain text.' in result

# Generated at 2026-10-25 14:11:10.540918
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from unittest.mock import Mock

    # 256-color terminal so the 256-color formatter path is exercised
    env = Mock(colors=256)
    color_formatter = ColorFormatter(
        env=env,
        explicit_json=True,
        color_scheme='monokai',
    )

    # 1. Known JSON mime type -> body is highlighted with the JSON lexer
    json_body = json.dumps({'foo': 'bar', 'baz': [1, 2, 3]})
    result = color_formatter.format_body(json_body, 'application/json')
    assert 'foo' in result
    assert 'bar' in result
    assert result != json_body  # escape codes added

    # 2. Subtype-suffix mime type (e.g. application/vnd.api+json)
    result = color_formatter.format_body(json_body, 'application/vnd.api+json')
    assert 'foo' in result
    assert 'bar' in result

    # 3. Wrong Content-Type but --json given and body parses as JSON
    #    -> falls back to the JSON lexer
    result = color_formatter.format_body(json_body, 'text/plain')
    assert 'foo' in result
    assert 'bar' in result

    # 4. Wrong Content-Type, body NOT valid JSON, no --json fallback possible
    #    -> returned (highlighted as plain text) without crashing
    text_body = 'Just some plain text.'
    result = color_formatter.format_body(text_body, 'text/plain')
    assert 'Just some plain text.' in result

    # 5. Unknown mime type with non-JSON body -> body returned intact
    result = color_formatter.format_body(text_body, 'application/x-unknown')
    assert 'Just some plain text.' in result

# Generated at 2026-10-25 14:11:12.959564
# Unit test for function get_lexer

# Generated at 2026-10-25 14:11:15.372733
# Unit test for function get_lexer

# Generated at 2026-10-25 14:11:17.791432
# Unit test for function get_lexer

# Generated at 2026-10-25 14:11:20.382326
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 14:11:23.035788
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 14:11:25.453673
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 14:11:27.872659
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 14:11:30.673958
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from httpie.plugins import FormatterPlugin  # noqa: F401  (already imported at module level)


# Generated at 2026-10-25 14:11:40.030802
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    assert isinstance(lexer, pygments.lexer.RegexLexer)
    assert isinstance(lexer, Lexer)
    assert lexer.name == 'HTTP'
    assert 'http' in lexer.aliases
    assert '*.http' in lexer.filenames
    assert 'root' in lexer.tokens
    assert len(lexer.tokens['root']) == 3
    lexer2 = SimplifiedHTTPLexer(stripnl=False, ensurenl=False, tabsize=4)
    assert lexer2.stripnl is False
    assert lexer2.ensurenl is False
    assert lexer2.tabsize == 4
    req_tokens = list(lexer.get_tokens('GET /index.html HTTP/1.1'))
    assert (pygments.token.Name.Function, 'GET') in req_tokens
    assert (pygments.token.Name.Namespace, '/index.html') in req_tokens
    assert (pygments.token.Keyword.Reserved, 'HTTP') in req_tokens
    assert (pygments.token.Operator, '/') in req_tokens
    assert (pygments.token.Number, '1.1') in req_tokens
    resp_tokens = list(lexer.get_tokens('HTTP/1.1 200 OK'))
    assert (pygments.token.Keyword.Reserved, 'HTTP') in resp_tokens
    assert (pygments.token.Operator, '/') in resp_tokens
    assert (pygments.token.Number, '1.1') in resp_tokens
    assert (pygments.token.Number, '200') in resp_tokens
    assert (pygments.token.Name.Exception, 'OK') in resp_tokens
    hdr_tokens = list(lexer.get_tokens('Content-Type: application/json'))
    assert (pygments.token.Name.Attribute, 'Content-Type') in hdr_tokens
    assert (pygments.token.Operator, ':') in hdr_tokens
    assert (pygments.token.String, 'application/json') in hdr_tokens
    empty_tokens = [t for t in lexer.get_tokens('') if t[1] != '\n']
    assert empty_tokens == []
    combined = 'POST /api HTTP/1.0'
    vals = ''.join(v for _, v in lexer.get_tokens(combined))
    assert combined in vals

# Generated at 2026-10-25 14:11:53.548301
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from unittest.mock import patch

    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.explicit_json = True

    expected_lexer = object()

    with patch(
        f'{ColorFormatter.__module__}.get_lexer',
        return_value=expected_lexer,
    ) as mocked_get_lexer:
        result = formatter.get_lexer_for_body(
            mime='application/json',
            body='{"success": true}',
        )

    assert result is expected_lexer
    mocked_get_lexer.assert_called_once_with(
        mime='application/json',
        explicit_json=True,
        body='{"success": true}',
    )

# Generated at 2026-10-25 14:11:55.287908
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 14:12:01.328325
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from httpie.plugins import FormatterPlugin  # noqa: F401  (already imported at module level)


# Generated at 2026-10-25 14:12:28.452891
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter(
        env=MockEnvironment(colors=256),
        color_scheme='solarized',
    )

    # JSON content type -> JSON lexer
    lexer = formatter.get_lexer_for_body('application/json', '{"a": 1}')
    assert isinstance(lexer, pygments.lexers.JsonLexer)

    # JSON with structured syntax suffix (+json) -> JSON lexer
    lexer = formatter.get_lexer_for_body('application/hal+json', '{"a": 1}')
    assert isinstance(lexer, pygments.lexers.JsonLexer)

    # XML content type -> XML lexer
    lexer = formatter.get_lexer_for_body('application/xml', '<a></a>')
    assert isinstance(lexer, pygments.lexers.XmlLexer)

    # Unknown content type with no matching lexer -> None
    lexer = formatter.get_lexer_for_body('xxx/xxx', 'xxx')
    assert lexer is None

    # Text content type falls back to TextLexer
    lexer = formatter.get_lexer_for_body('text/plain', 'xxx')
    assert isinstance(lexer, TextLexer)


# Fixtures / helpers
from unittest.mock import Mock

from httpie.context import Environment


class MockEnvironment(Environment):
    colors = 256
    stdin_isatty = True
    stdout_isatty = True

# Generated at 2026-10-25 14:12:42.494521
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 14:12:43.895928
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 14:12:48.536807
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 14:12:49.968847
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():import json

import pytest

# Adjust this import to wherever the module lives in your tree
# (e.g. httpie/output/formatters/colors.py or httpie/plugins/...)
from httpie.output.formatters.colors import ColorFormatter
from httpie.context import Environment


def make_formatter(explicit_json=False):
    return ColorFormatter(
        env=Environment(colors=256),
        explicit_json=explicit_json,
        color_scheme='solarized',
    )


def test_json_body_is_colorized():
    body = json.dumps({'status': 'ok', 'count': 3})
    result = make_formatter().format_body(body, 'application/json')
    assert result != body
    assert '\x1b[' in result  # contains ANSI escape codes


def test_plain_text_body_unchanged():
    body = 'just some plain text'
    result = make_formatter().format_body(body, 'text/plain')
    assert result == body


def test_explicit_json_with_wrong_content_type():
    body = '{"a": 1}'
    result = make_formatter(explicit_json=True).format_body(body, 'text/plain')
    assert result != body
    assert '\x1b[' in result


def test_explicit_json_invalid_body_unchanged():
    body = 'not json {'
    result = make_formatter(explicit_json=True).format_body(body, 'text/plain')
    assert result == body


def test_xml_body_is_colorized():
    body = '<root><item>1</item></root>'
    result = make_formatter().format_body(body, 'application/xml')
    assert result != body
    assert '\x1b[' in result

# Generated at 2026-10-25 14:13:12.902371
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # A style that exists in Pygments is returned as-is
    assert ColorFormatter.get_style_class('monokai') is \
        pygments.styles.get_style_by_name('monokai')

    # 'solarized' is NOT registered with Pygments -> falls back
    assert ColorFormatter.get_style_class('solarized') is Solarized256Style

    # Unknown style -> falls back
    assert ColorFormatter.get_style_class('definitely-not-a-style') is Solarized256Style


def test_ColorFormatter_get_style_class_fallback_via_mock(mocker):
    # Force the ClassNotFound branch even for a real style name
    mocker.patch.object(
        pygments.styles,
        'get_style_by_name',
        side_effect=ClassNotFound('nope'),
    )
    assert ColorFormatter.get_style_class('monokai') is Solarized256Style

# Generated at 2026-10-25 14:13:25.496335
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    # 256 colors + auto style -> simplified lexer and terminal256 formatter
    env = Environment(colors=256)
    formatter = ColorFormatter(env=env)
    assert formatter.enabled
    assert formatter.explicit_json is False
    assert isinstance(formatter.http_lexer, SimplifiedHTTPLexer)
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert ColorFormatter.get_style_class(AUTO_STYLE) is Solarized256Style

    # 256 colors + explicit_json -> flag is stored
    formatter = ColorFormatter(env=Environment(colors=256), explicit_json=True)
    assert formatter.explicit_json is True

    # 256 colors + known pygments style -> resolved by name
    formatter = ColorFormatter(env=Environment(colors=256), color_scheme='monokai')
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert ColorFormatter.get_style_class('monokai') is \
        pygments.styles.get_style_by_name('monokai')

    # 256 colors + unknown style -> falls back to Solarized256Style
    assert ColorFormatter.get_style_class('no-such-style') is Solarized256Style

    # Fewer than 256 colors -> plain terminal formatter and stock HTTP lexer
    env = Environment(colors=16)
    formatter = ColorFormatter(env=env)
    assert formatter.enabled
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)
    assert isinstance(formatter.formatter, TerminalFormatter)

    # No colors -> formatter disabled
    env = Environment(colors=False)
    formatter = ColorFormatter(env=env)
    assert not formatter.enabled

# Generated at 2026-10-25 14:13:46.529324
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    from unittest.mock import patch

    class ExistingStyle(pygments.style.Style):
        styles = {}

    with patch.object(
        pygments.styles,
        'get_style_by_name',
        return_value=ExistingStyle,
    ) as get_style_by_name:
        result = ColorFormatter.get_style_class('existing-style')

        assert result is ExistingStyle
        get_style_by_name.assert_called_once_with('existing-style')

    with patch.object(
        pygments.styles,
        'get_style_by_name',
        side_effect=ClassNotFound,
    ) as get_style_by_name:
        result = ColorFormatter.get_style_class('unknown-style')

        assert result is Solarized256Style
        get_style_by_name.assert_called_once_with('unknown-style')

# Generated at 2026-10-25 14:13:47.886620
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter(
        env=MockEnvironment(colors=256),
        color_scheme='solarized',
    )

    # JSON content type -> JSON lexer
    lexer = formatter.get_lexer_for_body('application/json', '{"a": 1}')
    assert isinstance(lexer, pygments.lexers.JsonLexer)

    # JSON with structured syntax suffix (+json) -> JSON lexer
    lexer = formatter.get_lexer_for_body('application/hal+json', '{"a": 1}')
    assert isinstance(lexer, pygments.lexers.JsonLexer)

    # XML content type -> XML lexer
    lexer = formatter.get_lexer_for_body('application/xml', '<a></a>')
    assert isinstance(lexer, pygments.lexers.XmlLexer)

    # Unknown content type with no matching lexer -> None
    lexer = formatter.get_lexer_for_body('xxx/xxx', 'xxx')
    assert lexer is None

    # Text content type falls back to TextLexer
    lexer = formatter.get_lexer_for_body('text/plain', 'xxx')
    assert isinstance(lexer, TextLexer)


# Fixtures / helpers
from unittest.mock import Mock

from httpie.context import Environment


class MockEnvironment(Environment):
    colors = 256
    stdin_isatty = True
    stdout_isatty = True

# Generated at 2026-10-25 14:13:50.898758
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter(
        env=MockEnvironment(colors=256),
        color_scheme='solarized',
    )

    # JSON content type -> JSON lexer
    lexer = formatter.get_lexer_for_body('application/json', '{"a": 1}')
    assert isinstance(lexer, pygments.lexers.JsonLexer)

    # JSON with structured syntax suffix (+json) -> JSON lexer
    lexer = formatter.get_lexer_for_body('application/hal+json', '{"a": 1}')
    assert isinstance(lexer, pygments.lexers.JsonLexer)

    # XML content type -> XML lexer
    lexer = formatter.get_lexer_for_body('application/xml', '<a></a>')
    assert isinstance(lexer, pygments.lexers.XmlLexer)

    # Unknown content type with no matching lexer -> None
    lexer = formatter.get_lexer_for_body('xxx/xxx', 'xxx')
    assert lexer is None

    # Text content type falls back to TextLexer
    lexer = formatter.get_lexer_for_body('text/plain', 'xxx')
    assert isinstance(lexer, TextLexer)


# Fixtures / helpers
from unittest.mock import Mock

from httpie.context import Environment


class MockEnvironment(Environment):
    colors = 256
    stdin_isatty = True
    stdout_isatty = True

# Generated at 2026-10-25 14:13:59.515762
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # A known Pygments style is resolved normally.
    expected_style = pygments.styles.get_style_by_name('default')
    assert ColorFormatter.get_style_class('default') is expected_style

    # An unknown style falls back to the bundled Solarized style.
    assert (
        ColorFormatter.get_style_class('definitely-not-a-valid-style')
        is Solarized256Style
    )

# Generated at 2026-10-25 14:14:16.647062
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():import json

import pytest

# Adjust this import to wherever the module lives in your tree
# (e.g. httpie/output/formatters/colors.py or httpie/plugins/...)
from httpie.output.formatters.colors import ColorFormatter
from httpie.context import Environment


def make_formatter(explicit_json=False):
    return ColorFormatter(
        env=Environment(colors=256),
        explicit_json=explicit_json,
        color_scheme='solarized',
    )


def test_json_body_is_colorized():
    body = json.dumps({'status': 'ok', 'count': 3})
    result = make_formatter().format_body(body, 'application/json')
    assert result != body
    assert '\x1b[' in result  # contains ANSI escape codes


def test_plain_text_body_unchanged():
    body = 'just some plain text'
    result = make_formatter().format_body(body, 'text/plain')
    assert result == body


def test_explicit_json_with_wrong_content_type():
    body = '{"a": 1}'
    result = make_formatter(explicit_json=True).format_body(body, 'text/plain')
    assert result != body
    assert '\x1b[' in result


def test_explicit_json_invalid_body_unchanged():
    body = 'not json {'
    result = make_formatter(explicit_json=True).format_body(body, 'text/plain')
    assert result == body


def test_xml_body_is_colorized():
    body = '<root><item>1</item></root>'
    result = make_formatter().format_body(body, 'application/xml')
    assert result != body
    assert '\x1b[' in result

# Generated at 2026-10-25 14:14:18.751635
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 14:14:21.616703
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from httpie.plugins import FormatterPlugin  # noqa: F401  (already imported at module level)


# Generated at 2026-10-25 14:14:23.062921
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # A style that exists in Pygments is returned as-is
    assert ColorFormatter.get_style_class('monokai') is \
        pygments.styles.get_style_by_name('monokai')

    # 'solarized' is NOT registered with Pygments -> falls back
    assert ColorFormatter.get_style_class('solarized') is Solarized256Style

    # Unknown style -> falls back
    assert ColorFormatter.get_style_class('definitely-not-a-style') is Solarized256Style


def test_ColorFormatter_get_style_class_fallback_via_mock(mocker):
    # Force the ClassNotFound branch even for a real style name
    mocker.patch.object(
        pygments.styles,
        'get_style_by_name',
        side_effect=ClassNotFound('nope'),
    )
    assert ColorFormatter.get_style_class('monokai') is Solarized256Style

# Generated at 2026-10-25 14:14:25.918497
# Unit test for function get_lexer

# Generated at 2026-10-25 14:14:30.426948
# Unit test for function get_lexer
def test_get_lexer():lexer = module_0.get_lexer(mime='application/json', explicit_json=False, body='{"a": 1}')

# Generated at 2026-10-25 14:14:32.679533
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 14:14:35.460908
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from httpie.plugins import FormatterPlugin  # noqa: F401  (already imported at module level)


# Generated at 2026-10-25 14:14:49.368837
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    formatter = object.__new__(ColorFormatter)
    formatter.formatter = sentinel.formatter
    formatter.get_lexer_for_body = Mock(return_value=sentinel.lexer)

    body = '{"message": "success"}'
    mime = 'application/json'
    highlighted_body = '\x1b[32m{"message": "success"}\x1b[0m'

    with patch.object(
        pygments,
        'highlight',
        return_value=highlighted_body,
    ) as highlight:
        result = formatter.format_body(body, mime)

    assert result == highlighted_body
    formatter.get_lexer_for_body.assert_called_once_with(mime, body)
    highlight.assert_called_once_with(
        code=body,
        lexer=sentinel.lexer,
        formatter=sentinel.formatter,
    )

    # If no lexer is available, the body should be returned unchanged.
    formatter.get_lexer_for_body.reset_mock(return_value=True)
    formatter.get_lexer_for_body.return_value = None

    with patch.object(pygments, 'highlight') as highlight:
        result = formatter.format_body(body, 'application/octet-stream')

    assert result == body
    formatter.get_lexer_for_body.assert_called_once_with(
        'application/octet-stream',
        body,
    )
    highlight.assert_not_called()

# Generated at 2026-10-25 14:14:52.342884
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    # 256 colors + auto style -> simplified lexer and terminal256 formatter
    env = Environment(colors=256)
    formatter = ColorFormatter(env=env)
    assert formatter.enabled
    assert formatter.explicit_json is False
    assert isinstance(formatter.http_lexer, SimplifiedHTTPLexer)
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert ColorFormatter.get_style_class(AUTO_STYLE) is Solarized256Style

    # 256 colors + explicit_json -> flag is stored
    formatter = ColorFormatter(env=Environment(colors=256), explicit_json=True)
    assert formatter.explicit_json is True

    # 256 colors + known pygments style -> resolved by name
    formatter = ColorFormatter(env=Environment(colors=256), color_scheme='monokai')
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert ColorFormatter.get_style_class('monokai') is \
        pygments.styles.get_style_by_name('monokai')

    # 256 colors + unknown style -> falls back to Solarized256Style
    assert ColorFormatter.get_style_class('no-such-style') is Solarized256Style

    # Fewer than 256 colors -> plain terminal formatter and stock HTTP lexer
    env = Environment(colors=16)
    formatter = ColorFormatter(env=env)
    assert formatter.enabled
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)
    assert isinstance(formatter.formatter, TerminalFormatter)

    # No colors -> formatter disabled
    env = Environment(colors=False)
    formatter = ColorFormatter(env=env)
    assert not formatter.enabled

# Generated at 2026-10-25 14:15:05.958180
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from unittest.mock import Mock, sentinel

    color_formatter = ColorFormatter.__new__(ColorFormatter)
    color_formatter.formatter = sentinel.formatter

    # Recognized MIME type: syntax highlighting is applied.
    lexer = sentinel.lexer
    color_formatter.get_lexer_for_body = Mock(return_value=lexer)

    original_highlight = pygments.highlight
    pygments.highlight = Mock(return_value='highlighted body')
    try:
        result = color_formatter.format_body(
            body='{"answer": 42}',
            mime='application/json',
        )

        assert result == 'highlighted body'
        color_formatter.get_lexer_for_body.assert_called_once_with(
            'application/json',
            '{"answer": 42}',
        )
        pygments.highlight.assert_called_once_with(
            code='{"answer": 42}',
            lexer=lexer,
            formatter=sentinel.formatter,
        )

        # Unrecognized MIME type: the original body is returned unchanged.
        pygments.highlight.reset_mock()
        color_formatter.get_lexer_for_body.reset_mock()
        color_formatter.get_lexer_for_body.return_value = None

        result = color_formatter.format_body(
            body='plain text',
            mime='application/octet-stream',
        )

        assert result == 'plain text'
        color_formatter.get_lexer_for_body.assert_called_once_with(
            'application/octet-stream',
            'plain text',
        )
        pygments.highlight.assert_not_called()
    finally:
        pygments.highlight = original_highlight

# Generated at 2026-10-25 14:15:08.375022
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 14:15:10.796255
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 14:15:13.208822
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 14:15:15.716375
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 14:15:18.343978
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 14:15:20.764087
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 14:15:23.179167
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 14:15:25.592959
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 14:15:28.006385
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 14:15:30.420261
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 14:15:32.834014
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 14:15:35.304783
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 14:15:37.685497
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 14:15:40.099960
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 14:15:42.515668
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 14:15:46.510647
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    # 256 colors + auto style -> simplified lexer and terminal256 formatter
    env = Environment(colors=256)
    formatter = ColorFormatter(env=env)
    assert formatter.enabled
    assert formatter.explicit_json is False
    assert isinstance(formatter.http_lexer, SimplifiedHTTPLexer)
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert ColorFormatter.get_style_class(AUTO_STYLE) is Solarized256Style

    # 256 colors + explicit_json -> flag is stored
    formatter = ColorFormatter(env=Environment(colors=256), explicit_json=True)
    assert formatter.explicit_json is True

    # 256 colors + known pygments style -> resolved by name
    formatter = ColorFormatter(env=Environment(colors=256), color_scheme='monokai')
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert ColorFormatter.get_style_class('monokai') is \
        pygments.styles.get_style_by_name('monokai')

    # 256 colors + unknown style -> falls back to Solarized256Style
    assert ColorFormatter.get_style_class('no-such-style') is Solarized256Style

    # Fewer than 256 colors -> plain terminal formatter and stock HTTP lexer
    env = Environment(colors=16)
    formatter = ColorFormatter(env=env)
    assert formatter.enabled
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)
    assert isinstance(formatter.formatter, TerminalFormatter)

    # No colors -> formatter disabled
    env = Environment(colors=False)
    formatter = ColorFormatter(env=env)
    assert not formatter.enabled

# Generated at 2026-10-25 14:15:49.187008
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    # 256 colors + auto style -> simplified lexer and terminal256 formatter
    env = Environment(colors=256)
    formatter = ColorFormatter(env=env)
    assert formatter.enabled
    assert formatter.explicit_json is False
    assert isinstance(formatter.http_lexer, SimplifiedHTTPLexer)
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert ColorFormatter.get_style_class(AUTO_STYLE) is Solarized256Style

    # 256 colors + explicit_json -> flag is stored
    formatter = ColorFormatter(env=Environment(colors=256), explicit_json=True)
    assert formatter.explicit_json is True

    # 256 colors + known pygments style -> resolved by name
    formatter = ColorFormatter(env=Environment(colors=256), color_scheme='monokai')
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert ColorFormatter.get_style_class('monokai') is \
        pygments.styles.get_style_by_name('monokai')

    # 256 colors + unknown style -> falls back to Solarized256Style
    assert ColorFormatter.get_style_class('no-such-style') is Solarized256Style

    # Fewer than 256 colors -> plain terminal formatter and stock HTTP lexer
    env = Environment(colors=16)
    formatter = ColorFormatter(env=env)
    assert formatter.enabled
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)
    assert isinstance(formatter.formatter, TerminalFormatter)

    # No colors -> formatter disabled
    env = Environment(colors=False)
    formatter = ColorFormatter(env=env)
    assert not formatter.enabled

# Generated at 2026-10-25 14:16:02.893086
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from unittest.mock import Mock, patch, sentinel

    formatter = object.__new__(ColorFormatter)
    formatter.formatter = sentinel.pygments_formatter
    formatter.get_lexer_for_body = Mock(return_value=sentinel.lexer)

    body = '{"message": "ok"}'
    mime = 'application/json'
    highlighted_body = '\x1b[32m{"message": "ok"}\x1b[0m'

    with patch.object(
        pygments,
        'highlight',
        return_value=highlighted_body,
    ) as highlight:
        result = formatter.format_body(body, mime)

    assert result == highlighted_body
    formatter.get_lexer_for_body.assert_called_once_with(mime, body)
    highlight.assert_called_once_with(
        code=body,
        lexer=sentinel.lexer,
        formatter=sentinel.pygments_formatter,
    )

    # If no lexer is available, the original body must be returned unchanged.
    formatter.get_lexer_for_body.reset_mock(return_value=True)
    formatter.get_lexer_for_body.return_value = None

    with patch.object(pygments, 'highlight') as highlight:
        result = formatter.format_body(body, 'application/octet-stream')

    assert result == body
    formatter.get_lexer_for_body.assert_called_once_with(
        'application/octet-stream',
        body,
    )
    highlight.assert_not_called()

# Generated at 2026-10-25 14:16:04.324521
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # A style that exists in Pygments is returned as-is
    assert ColorFormatter.get_style_class('monokai') is \
        pygments.styles.get_style_by_name('monokai')

    # 'solarized' is NOT registered with Pygments -> falls back
    assert ColorFormatter.get_style_class('solarized') is Solarized256Style

    # Unknown style -> falls back
    assert ColorFormatter.get_style_class('definitely-not-a-style') is Solarized256Style


def test_ColorFormatter_get_style_class_fallback_via_mock(mocker):
    # Force the ClassNotFound branch even for a real style name
    mocker.patch.object(
        pygments.styles,
        'get_style_by_name',
        side_effect=ClassNotFound('nope'),
    )
    assert ColorFormatter.get_style_class('monokai') is Solarized256Style

# Generated at 2026-10-25 14:16:05.758966
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 14:16:09.520513
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from httpie.plugins import FormatterPlugin  # noqa: F401  (already imported at module level)


# Generated at 2026-10-25 14:16:11.596667
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 14:16:17.637467
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from httpie.plugins import FormatterPlugin  # noqa: F401  (already imported at module level)


# Generated at 2026-10-25 14:16:27.572699
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # Returns the requested Pygments style when it exists.
    expected_style = pygments.styles.get_style_by_name('default')
    assert ColorFormatter.get_style_class('default') is expected_style

    # Falls back to the bundled Solarized style for unknown schemes.
    assert (
        ColorFormatter.get_style_class('nonexistent-style')
        is Solarized256Style
    )

# Generated at 2026-10-25 14:16:57.880434
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.explicit_json = True

    mime = 'text/plain'
    body = '{"message": "Hello"}'
    expected_lexer = object()

    with patch(
        f'{ColorFormatter.__module__}.get_lexer',
        return_value=expected_lexer,
    ) as mocked_get_lexer:
        result = formatter.get_lexer_for_body(mime, body)

    assert result is expected_lexer
    mocked_get_lexer.assert_called_once_with(
        mime=mime,
        explicit_json=True,
        body=body,
    )

# Generated at 2026-10-25 14:17:08.633024
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.explicit_json = True

    mime = 'application/json'
    body = '{"message": "success"}'

    with patch(
        f'{ColorFormatter.__module__}.get_lexer',
        return_value=sentinel.lexer,
    ) as mocked_get_lexer:
        result = formatter.get_lexer_for_body(mime, body)

    assert result is sentinel.lexer
    mocked_get_lexer.assert_called_once_with(
        mime=mime,
        explicit_json=True,
        body=body,
    )

# Generated at 2026-10-25 14:17:11.603954
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 14:17:17.550042
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from httpie.plugins import FormatterPlugin  # noqa: F401  (already imported at module level)


# Generated at 2026-10-25 14:17:21.045261
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    assert isinstance(lexer, pygments.lexer.RegexLexer)
    assert isinstance(lexer, Lexer)
    assert lexer.name == 'HTTP'
    assert 'http' in lexer.aliases
    assert '*.http' in lexer.filenames
    assert 'root' in lexer.tokens
    assert len(lexer.tokens['root']) == 3
    lexer2 = SimplifiedHTTPLexer(stripnl=False, ensurenl=False, tabsize=4)
    assert lexer2.stripnl is False
    assert lexer2.ensurenl is False
    assert lexer2.tabsize == 4
    req_tokens = list(lexer.get_tokens('GET /index.html HTTP/1.1'))
    assert (pygments.token.Name.Function, 'GET') in req_tokens
    assert (pygments.token.Name.Namespace, '/index.html') in req_tokens
    assert (pygments.token.Keyword.Reserved, 'HTTP') in req_tokens
    assert (pygments.token.Operator, '/') in req_tokens
    assert (pygments.token.Number, '1.1') in req_tokens
    resp_tokens = list(lexer.get_tokens('HTTP/1.1 200 OK'))
    assert (pygments.token.Keyword.Reserved, 'HTTP') in resp_tokens
    assert (pygments.token.Operator, '/') in resp_tokens
    assert (pygments.token.Number, '1.1') in resp_tokens
    assert (pygments.token.Number, '200') in resp_tokens
    assert (pygments.token.Name.Exception, 'OK') in resp_tokens
    hdr_tokens = list(lexer.get_tokens('Content-Type: application/json'))
    assert (pygments.token.Name.Attribute, 'Content-Type') in hdr_tokens
    assert (pygments.token.Operator, ':') in hdr_tokens
    assert (pygments.token.String, 'application/json') in hdr_tokens
    empty_tokens = [t for t in lexer.get_tokens('') if t[1] != '\n']
    assert empty_tokens == []
    combined = 'POST /api HTTP/1.0'
    vals = ''.join(v for _, v in lexer.get_tokens(combined))
    assert combined in vals

# Generated at 2026-10-25 14:17:33.130021
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.formatter = Mock(name='formatter')

    body = '{"message": "success"}'
    mime = 'application/json'
    lexer = Mock(name='lexer')

    formatter.get_lexer_for_body = Mock(return_value=lexer)

    with patch.object(
        pygments,
        'highlight',
        return_value='highlighted body',
    ) as highlight:
        result = formatter.format_body(body, mime)

    formatter.get_lexer_for_body.assert_called_once_with(mime, body)
    highlight.assert_called_once_with(
        code=body,
        lexer=lexer,
        formatter=formatter.formatter,
    )
    assert result == 'highlighted body'


def test_ColorFormatter_format_body_returns_original_when_no_lexer():
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.formatter = Mock(name='formatter')

    body = 'unrecognized content'
    mime = 'application/octet-stream'
    formatter.get_lexer_for_body = Mock(return_value=None)

    with patch.object(pygments, 'highlight') as highlight:
        result = formatter.format_body(body, mime)

    formatter.get_lexer_for_body.assert_called_once_with(mime, body)
    highlight.assert_not_called()
    assert result == body

# Generated at 2026-10-25 14:17:35.671042
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 14:17:38.085870
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 14:17:40.729344
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 14:18:07.412111
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = object.__new__(colors.ColorFormatter)
    formatter.explicit_json = True
    expected_lexer = Mock()

    with patch.object(
        colors,
        'get_lexer',
        return_value=expected_lexer,
    ) as mocked_get_lexer:
        result = formatter.get_lexer_for_body(
            mime='application/json',
            body='{"key": "value"}',
        )

    assert result is expected_lexer
    mocked_get_lexer.assert_called_once_with(
        mime='application/json',
        explicit_json=True,
        body='{"key": "value"}',
    )

# Generated at 2026-10-25 14:18:22.260746
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 14:18:25.335018
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from httpie.plugins import FormatterPlugin  # noqa: F401  (already imported at module level)
