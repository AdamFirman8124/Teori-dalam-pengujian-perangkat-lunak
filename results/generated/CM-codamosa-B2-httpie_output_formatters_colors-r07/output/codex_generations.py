

# Generated at 2026-10-25 08:47:42.658673
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:48:23.925294
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:48:38.263926
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from httpie.context import Environment

# 256-color terminal + explicit style: uses Terminal256Formatter and the
# simplified HTTP lexer, and stores explicit_json.
env_256 = Environment(colors=256)
cf_256 = ColorFormatter(
    env=env_256,
    explicit_json=True,
    color_scheme='solarized',
)
assert cf_256.enabled is True
assert cf_256.explicit_json is True
assert isinstance(cf_256.formatter, Terminal256Formatter)
assert isinstance(cf_256.http_lexer, SimplifiedHTTPLexer)

# 16-color terminal (auto style): falls back to the plain terminal
# formatter and the stock Pygments HTTP lexer.
env_16 = Environment(colors=16)
cf_16 = ColorFormatter(env=env_16, color_scheme=AUTO_STYLE)
assert cf_16.enabled is True
assert cf_16.explicit_json is False
assert isinstance(cf_16.formatter, TerminalFormatter)
assert isinstance(cf_16.http_lexer, PygmentsHttpLexer)

# No colors: formatter disables itself and does no setup.
env_0 = Environment(colors=0)
cf_0 = ColorFormatter(env=env_0, color_scheme=DEFAULT_STYLE)
assert cf_0.enabled is False

# get_style_class resolves known styles by name...
assert ColorFormatter.get_style_class('monokai') is \
    pygments.styles.get_style_by_name('monokai')
# ...and falls back to the bundled Solarized style for unknown names.
assert ColorFormatter.get_style_class('no-such-style-xyz') is \
    Solarized256Style

# The bundled Solarized style is registered as an available choice.
assert SOLARIZED_STYLE in AVAILABLE_STYLES
assert AUTO_STYLE in AVAILABLE_STYLES

# Generated at 2026-10-25 08:48:40.682814
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:48:43.102101
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:48:45.517786
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:48:47.935730
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:48:50.351753
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:48:52.768383
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:48:55.186116
# Unit test for function get_lexer

# Generated at 2026-10-25 08:48:57.698396
# Unit test for function get_lexer

# Generated at 2026-10-25 08:49:00.098053
# Unit test for function get_lexer

# Generated at 2026-10-25 08:49:02.522483
# Unit test for constructor of class Solarized256Style

# Generated at 2026-10-25 08:49:04.934142
# Unit test for constructor of class Solarized256Style

# Generated at 2026-10-25 08:49:07.353043
# Unit test for constructor of class Solarized256Style

# Generated at 2026-10-25 08:49:09.816299
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:49:12.237390
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:49:14.653119
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:49:17.069369
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:49:19.656976
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:49:21.903589
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:49:24.322992
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 08:49:26.740364
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 08:49:29.158159
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 08:49:31.577665
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:49:33.992787
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:49:36.437375
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:49:38.858290
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 08:49:41.272869
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 08:49:43.692685
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 08:49:46.109713
# Unit test for function get_lexer

# Generated at 2026-10-25 08:49:48.525437
# Unit test for function get_lexer

# Generated at 2026-10-25 08:49:50.944289
# Unit test for function get_lexer

# Generated at 2026-10-25 08:49:53.361865
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:49:55.804511
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:49:58.221694
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:50:00.640952
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:50:03.056702
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:50:05.479187
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:50:07.897133
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:50:10.313117
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:50:12.730422
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:50:15.147636
# Unit test for function get_lexer

# Generated at 2026-10-25 08:50:17.568500
# Unit test for function get_lexer

# Generated at 2026-10-25 08:50:19.982188
# Unit test for function get_lexer

# Generated at 2026-10-25 08:50:22.398917
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:50:24.857553
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:50:27.272552
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:50:29.687483
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:50:32.104716
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:50:34.523974
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:50:36.941156
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:50:39.357204
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:50:41.774357
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:50:44.192038
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:50:46.609979
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:50:49.027319
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:50:51.443676
# Unit test for function get_lexer

# Generated at 2026-10-25 08:50:53.859112
# Unit test for function get_lexer

# Generated at 2026-10-25 08:50:56.277957
# Unit test for function get_lexer

# Generated at 2026-10-25 08:50:58.695830
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:51:01.111301
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:51:03.526368
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:51:25.276878
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:52:19.139911
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():from types import SimpleNamespace

# Generated at 2026-10-25 08:52:40.522940
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:52:42.940833
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:52:45.357069
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:52:48.181880
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:52:50.599716
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:52:53.019364
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:52:55.439653
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:52:57.854814
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:53:00.274984
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:53:02.802675
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 08:53:05.221705
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 08:53:07.639460
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 08:53:10.054718
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:53:12.470605
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:53:14.889026
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:53:17.308348
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:53:19.724805
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:53:22.142932
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:53:24.558442
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:53:26.976944
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:53:29.487154
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:53:31.863888
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:53:34.283068
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:53:51.609138
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:54:04.095336
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

# Generated at 2026-10-25 08:54:06.514177
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:54:08.930878
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:54:11.347109
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:54:13.764908
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:54:16.180523
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:54:18.597966
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:54:21.012588
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:54:23.458206
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:54:26.062749
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:54:28.479720
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:54:30.899110
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:54:33.341331
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:54:36.136568
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:54:38.552779
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:54:40.968647
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:54:54.997778
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

# Generated at 2026-10-25 08:54:56.430226
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

# Generated at 2026-10-25 08:55:13.734172
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:55:16.392711
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:55:18.814216
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:55:21.236481
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 08:55:23.654594
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 08:55:26.073228
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 08:55:28.498147
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:55:30.918599
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:55:33.337480
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:55:35.754112
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:55:38.168351
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:55:40.592603
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:55:43.013577
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:55:45.427312
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:55:47.929919
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:55:50.346711
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:55:52.765982
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:55:55.183137
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:55:57.598989
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:56:00.014579
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:56:02.432255
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:56:04.846285
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:56:07.261792
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:56:09.683933
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:56:12.101841
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:56:14.523776
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:56:16.937681
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:56:19.358899
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:56:21.775425
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:56:24.193918
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:56:26.609888
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:56:29.026655
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:56:31.450671
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 08:56:33.010544
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

# Generated at 2026-10-25 08:57:21.848017
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:57:23.638658
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():from httpie.output.formatters.colors import ColorFormatter