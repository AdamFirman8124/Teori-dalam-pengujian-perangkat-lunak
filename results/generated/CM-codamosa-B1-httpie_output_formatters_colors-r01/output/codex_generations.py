

# Generated at 2026-10-25 12:37:49.962811
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:37:52.377100
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:37:54.848357
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:37:57.227648
# Unit test for constructor of class Solarized256Style

# Generated at 2026-10-25 12:37:59.643062
# Unit test for constructor of class Solarized256Style

# Generated at 2026-10-25 12:38:02.059147
# Unit test for constructor of class Solarized256Style

# Generated at 2026-10-25 12:38:13.192198
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

# Generated at 2026-10-25 12:38:14.733906
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:38:53.555856
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from httpie.plugins import FormatterPlugin  # noqa: F401  (already imported at module level)


# Generated at 2026-10-25 12:38:56.092149
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:38:58.740220
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:39:01.152946
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:39:03.567434
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 12:39:05.983492
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 12:39:08.394023
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 12:39:10.810703
# Unit test for function get_lexer

# Generated at 2026-10-25 12:39:13.225701
# Unit test for function get_lexer

# Generated at 2026-10-25 12:39:20.322533
# Unit test for function get_lexer
def test_get_lexer():lexer = module_0.get_lexer(mime='application/json', explicit_json=False, body='{"a": 1}')

# Generated at 2026-10-25 12:39:23.340378
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

# Generated at 2026-10-25 12:39:24.907758
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

# Generated at 2026-10-25 12:39:26.424964
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:39:32.603570
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from httpie.plugins import FormatterPlugin  # noqa: F401  (already imported at module level)


# Generated at 2026-10-25 12:39:35.018739
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 12:39:37.433937
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 12:39:39.846478
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 12:39:42.261825
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:39:44.675524
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:39:47.113399
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:39:49.528278
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:39:51.944754
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:39:54.360205
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:39:56.770756
# Unit test for function get_lexer

# Generated at 2026-10-25 12:39:59.185115
# Unit test for function get_lexer

# Generated at 2026-10-25 12:40:01.600916
# Unit test for function get_lexer

# Generated at 2026-10-25 12:40:04.012682
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:40:06.429658
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:40:08.845287
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:40:11.258752
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 12:40:13.671369
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 12:40:16.088929
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 12:40:18.500734
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:40:23.547898
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 12:40:28.169237
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 12:40:29.895760
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

# Generated at 2026-10-25 12:40:48.165762
# Unit test for function get_lexer

# Generated at 2026-10-25 12:40:50.872737
# Unit test for function get_lexer

# Generated at 2026-10-25 12:40:53.290452
# Unit test for function get_lexer

# Generated at 2026-10-25 12:40:55.706819
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 12:40:58.120981
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 12:41:00.566331
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 12:41:02.949538
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:41:05.363356
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:41:08.013043
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:41:10.426390
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:41:12.841373
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:41:15.255412
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:41:17.670144
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:41:20.085272
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:41:22.499091
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:41:24.914351
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 12:41:27.328634
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 12:41:29.745717
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 12:41:32.159368
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:41:34.574743
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:41:36.990216
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:41:39.404825
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 12:41:42.279325
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 12:41:45.121793
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 12:41:48.167479
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:41:49.566458
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 12:41:51.101477
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 12:42:07.707965
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

# Generated at 2026-10-25 12:42:10.124083
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:42:12.539215
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:42:14.953830
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:42:17.367106
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:42:19.781602
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:42:22.221103
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:42:24.634780
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:42:27.049655
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:42:29.463918
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:42:31.878587
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:42:34.297323
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:42:36.714696
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:42:39.129755
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:42:58.070172
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:42:59.661679
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 12:43:03.235681
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

# Generated at 2026-10-25 12:43:04.834521
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:43:14.251549
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from httpie.plugins import FormatterPlugin  # noqa: F401  (already imported at module level)


# Generated at 2026-10-25 12:43:15.785258
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

# Generated at 2026-10-25 12:43:18.324572
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:43:20.739214
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:43:23.155893
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:43:25.570400
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:43:27.985847
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:43:30.400125
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:43:32.814448
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:43:35.269203
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:43:37.970442
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:43:40.385317
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 12:43:42.800515
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 12:43:45.546188
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 12:43:47.053067
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

# Generated at 2026-10-25 12:43:48.434810
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

# Generated at 2026-10-25 12:44:04.832021
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:44:06.245834
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 12:44:07.806470
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 12:44:10.748352
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:44:13.160100
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:44:15.752335
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:44:18.167265
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:44:20.798863
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:44:23.214838
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:44:25.634569
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 12:44:28.047915
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 12:44:30.465786
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 12:44:33.034955
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 12:44:35.448628
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 12:44:37.863773
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 12:44:40.279001
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:44:42.692236
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:44:45.109558
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:44:47.524944
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:44:49.940455
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:44:52.352652
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:44:54.767277
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:44:57.181831
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:44:59.595783
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:45:02.012438
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:45:20.612855
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 12:45:29.417379
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # A real, bundled Pygments style resolves to its actual class.
    fruity = ColorFormatter.get_style_class('fruity')
    assert fruity is pygments.styles.get_style_by_name('fruity')
    assert issubclass(fruity, pygments.style.Style)
    assert 'fruity' in fruity.__name__.lower()

    # It is a staticmethod: callable on the class and on an instance-less ref.
    assert ColorFormatter.get_style_class('fruity') is fruity

    # Unknown style names fall back to the bundled Solarized256Style.
    assert ColorFormatter.get_style_class('definitely-not-a-real-style-xyz') is Solarized256Style
    assert ColorFormatter.get_style_class('') is Solarized256Style

    # 'auto' is httpie's own sentinel, not a Pygments style -> fallback.
    assert ColorFormatter.get_style_class(AUTO_STYLE) is Solarized256Style

    # The fallback is itself a usable Pygments style class.
    assert issubclass(Solarized256Style, pygments.style.Style)
    assert Solarized256Style.background_color == '#1c1c1c'

# Generated at 2026-10-25 12:45:46.323908
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

# Generated at 2026-10-25 12:45:49.186312
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

# Generated at 2026-10-25 12:45:51.733341
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 12:45:54.148854
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 12:45:56.565073
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 12:45:58.978785
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 12:46:01.490150
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 12:46:03.866044
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 12:46:07.408021
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:46:08.850635
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 12:46:10.379546
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 12:46:13.450005
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:46:14.986062
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 12:46:16.448368
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 12:46:19.287285
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

# Generated at 2026-10-25 12:46:20.805901
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:46:23.792773
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from httpie.plugins import FormatterPlugin  # noqa: F401  (already imported at module level)


# Generated at 2026-10-25 12:46:26.864984
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:46:28.299036
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 12:46:29.834842
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 12:46:31.268417
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:46:34.013092
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:46:36.429563
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:46:38.843909
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:46:41.257782
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:46:43.854294
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:46:46.272388
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:46:48.688847
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:46:51.100517
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 12:46:53.515683
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:46:55.929650
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:46:58.344178
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:47:00.757303
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:47:03.177041
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:47:05.592711
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:47:09.162637
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 12:47:11.797018
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 12:47:14.528869
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 12:47:19.908200
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

# Generated at 2026-10-25 12:47:21.342086
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

# Generated at 2026-10-25 12:47:22.776200
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

# Generated at 2026-10-25 12:47:24.209407
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

# Generated at 2026-10-25 12:47:25.744755
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

# Generated at 2026-10-25 12:47:42.444326
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # 1. Known Pygments style is returned as-is.
    assert (
        ColorFormatter.get_style_class("monokai")
        is pygments.styles.get_style_by_name("monokai")
    )
    assert issubclass(
        ColorFormatter.get_style_class("default"),
        pygments.style.Style
    )

    # 2. Bundled `solarized` is not a native Pygments style,
    # so it falls back to `Solarized256Style`.
    try:
        pygments.styles.get_style_by_name("solarized")
        has_native_solarized = True
    except ClassNotFound:
        has_native_solarized = False

    if not has_native_solarized:
        assert (
            ColorFormatter.get_style_class("solarized")
            is Solarized256Style
        )

    # 3. Unknown style name falls back to `Solarized256Style`.
    assert (
        ColorFormatter.get_style_class("no-such-style-xyz")
        is Solarized256Style
    )

# Generated at 2026-10-25 12:47:44.851694
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:47:47.265507
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 12:47:49.678905
# Unit test for method format_headers of class ColorFormatter