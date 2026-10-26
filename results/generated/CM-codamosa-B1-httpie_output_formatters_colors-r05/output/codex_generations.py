

# Generated at 2026-10-25 11:06:36.736342
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 11:06:39.150399
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 11:06:41.566152
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 11:06:58.541700
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 11:07:01.514020
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

# Generated at 2026-10-25 11:07:10.628003
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from unittest.mock import Mock


def test_ColorFormatter_format_headers(monkeypatch):
    formatter = object.__new__(ColorFormatter)
    formatter.http_lexer = Mock()
    formatter.formatter = Mock()

    highlight = Mock(return_value='\n  highlighted headers  \n')
    monkeypatch.setattr(pygments, 'highlight', highlight)

    result = formatter.format_headers('HTTP/1.1 200 OK\r\nContent-Type: text/plain')

    assert result == 'highlighted headers'
    highlight.assert_called_once_with(
        code='HTTP/1.1 200 OK\r\nContent-Type: text/plain',
        lexer=formatter.http_lexer,
        formatter=formatter.formatter,
    )

# Generated at 2026-10-25 11:07:22.107142
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from types import SimpleNamespace


# Generated at 2026-10-25 11:07:31.353214
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 11:07:33.915727
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 11:07:36.548071
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 11:07:38.966806
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 11:07:41.618445
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 11:07:44.033406
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 11:07:46.446988
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 11:07:58.351434
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():lexer = SimplifiedHTTPLexer()

# Generated at 2026-10-25 11:08:13.398750
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 11:08:16.237341
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

# Generated at 2026-10-25 11:08:31.300263
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

# Generated at 2026-10-25 11:08:42.933928
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from unittest.mock import Mock, sentinel, patch

    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.formatter = sentinel.formatter
    formatter.get_lexer_for_body = Mock(return_value=sentinel.lexer)

    with patch.object(
        pygments,
        'highlight',
        return_value='highlighted body',
    ) as highlight:
        result = formatter.format_body(
            body='{"message": "ok"}',
            mime='application/json',
        )

    assert result == 'highlighted body'
    formatter.get_lexer_for_body.assert_called_once_with(
        'application/json',
        '{"message": "ok"}',
    )
    highlight.assert_called_once_with(
        code='{"message": "ok"}',
        lexer=sentinel.lexer,
        formatter=sentinel.formatter,
    )


def test_ColorFormatter_format_body_without_lexer_returns_original_body():
    from unittest.mock import Mock, sentinel, patch

    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.formatter = sentinel.formatter
    formatter.get_lexer_for_body = Mock(return_value=None)

    with patch.object(pygments, 'highlight') as highlight:
        result = formatter.format_body(
            body='plain text',
            mime='application/octet-stream',
        )

    assert result == 'plain text'
    formatter.get_lexer_for_body.assert_called_once_with(
        'application/octet-stream',
        'plain text',
    )
    highlight.assert_not_called()

# Generated at 2026-10-25 11:08:45.535031
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 11:08:47.953529
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 11:08:50.368922
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 11:08:52.784622
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 11:08:55.206371
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 11:08:57.624562
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 11:09:00.039478
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 11:09:02.457665
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 11:09:28.558749
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():from pygments.formatters import NullFormatter


# Generated at 2026-10-25 11:09:35.933483
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():lexer = SimplifiedHTTPLexer()


# Generated at 2026-10-25 11:09:42.792085
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # A valid Pygments style is resolved normally.
    expected_style = pygments.styles.get_style_by_name('fruity')
    assert ColorFormatter.get_style_class('fruity') is expected_style

    # An unknown style falls back to the bundled Solarized style.
    assert (
        ColorFormatter.get_style_class('nonexistent-style')
        is Solarized256Style
    )

# Generated at 2026-10-25 11:09:55.973758
# Unit test for function get_lexer
def test_get_lexer():lexer = module_0.get_lexer('application/json')

# Generated at 2026-10-25 11:10:00.184790
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 11:10:02.841004
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 11:10:05.254819
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 11:10:12.909466
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():default_style = pygments.styles.get_style_by_name('default')

# Generated at 2026-10-25 11:10:25.900477
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.formatter = sentinel.formatter

    body = '{"message": "ok"}'
    mime = 'application/json'
    highlighted_body = '<highlighted>'

    with patch.object(
        formatter,
        'get_lexer_for_body',
        return_value=sentinel.lexer,
    ) as get_lexer, patch.object(
        pygments,
        'highlight',
        return_value=highlighted_body,
    ) as highlight:
        result = formatter.format_body(body, mime)

    assert result == highlighted_body
    get_lexer.assert_called_once_with(mime, body)
    highlight.assert_called_once_with(
        code=body,
        lexer=sentinel.lexer,
        formatter=sentinel.formatter,
    )

    # If no lexer recognizes the MIME type, the body remains unchanged.
    with patch.object(
        formatter,
        'get_lexer_for_body',
        return_value=None,
    ) as get_lexer, patch.object(pygments, 'highlight') as highlight:
        result = formatter.format_body(body, 'application/octet-stream')

    assert result == body
    get_lexer.assert_called_once_with('application/octet-stream', body)
    highlight.assert_not_called()

# Generated at 2026-10-25 11:10:38.601792
# Unit test for function get_lexer
def test_get_lexer():json_lexer_type = type(pygments.lexers.get_lexer_by_name('json'))


# Generated at 2026-10-25 11:10:57.238287
# Unit test for function get_lexer

# Generated at 2026-10-25 11:11:40.547983
# Unit test for function get_lexer
def test_get_lexer():lexer = module_0.get_lexer(mime='application/json', explicit_json=False, body='{"a": 1}')

# Generated at 2026-10-25 11:11:50.588525
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from unittest.mock import Mock, patch, sentinel

    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.formatter = sentinel.formatter

    # A recognized MIME type is highlighted.
    formatter.get_lexer_for_body = Mock(return_value=sentinel.lexer)

    with patch.object(
        pygments,
        'highlight',
        return_value='highlighted body',
    ) as highlight:
        result = formatter.format_body(
            body='{"key": "value"}',
            mime='application/json',
        )

    assert result == 'highlighted body'
    formatter.get_lexer_for_body.assert_called_once_with(
        'application/json',
        '{"key": "value"}',
    )
    highlight.assert_called_once_with(
        code='{"key": "value"}',
        lexer=sentinel.lexer,
        formatter=sentinel.formatter,
    )

    # An unrecognized MIME type leaves the body unchanged.
    formatter.get_lexer_for_body = Mock(return_value=None)

    with patch.object(pygments, 'highlight') as highlight:
        result = formatter.format_body(
            body='plain body',
            mime='application/octet-stream',
        )

    assert result == 'plain body'
    formatter.get_lexer_for_body.assert_called_once_with(
        'application/octet-stream',
        'plain body',
    )
    highlight.assert_not_called()

# Generated at 2026-10-25 11:12:03.212120
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from types import SimpleNamespace


# Generated at 2026-10-25 11:12:05.788417
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 11:12:08.430457
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 11:12:10.845100
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 11:12:21.411304
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():from unittest.mock import Mock, sentinel


def test_ColorFormatter_format_body(monkeypatch):
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.formatter = sentinel.formatter
    formatter.get_lexer_for_body = Mock(return_value=sentinel.lexer)

    highlight = Mock(return_value='highlighted body')
    monkeypatch.setattr(pygments, 'highlight', highlight)

    result = formatter.format_body(
        body='{"success": true}',
        mime='application/json',
    )

    assert result == 'highlighted body'
    formatter.get_lexer_for_body.assert_called_once_with(
        'application/json',
        '{"success": true}',
    )
    highlight.assert_called_once_with(
        code='{"success": true}',
        lexer=sentinel.lexer,
        formatter=sentinel.formatter,
    )

# Generated at 2026-10-25 11:12:24.379424
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 11:12:27.283830
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 11:12:28.786528
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 11:12:35.951781
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    color_formatter = ColorFormatter.__new__(ColorFormatter)
    color_formatter.http_lexer = sentinel.http_lexer
    color_formatter.formatter = sentinel.formatter

    headers = 'HTTP/1.1 200 OK\r\nContent-Type: application/json'

    with patch(
        'pygments.highlight',
        return_value='\n  highlighted headers  \n',
    ) as highlight:
        result = color_formatter.format_headers(headers)

    assert result == 'highlighted headers'
    highlight.assert_called_once_with(
        code=headers,
        lexer=sentinel.http_lexer,
        formatter=sentinel.formatter,
    )

# Generated at 2026-10-25 11:12:42.671014
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():lexer = SimplifiedHTTPLexer()


# Generated at 2026-10-25 11:12:45.686115
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 11:12:47.089321
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 11:12:48.487755
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 11:12:50.939029
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 11:12:53.362338
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 11:12:55.895782
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 11:12:58.314831
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 11:13:00.733547
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 11:13:03.154474
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 11:13:05.577391
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 11:13:07.992888
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 11:13:10.409458
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 11:13:23.559056
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():from unittest.mock import Mock, patch, sentinel


# Generated at 2026-10-25 11:13:26.540652
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 11:13:28.284257
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 11:13:29.712373
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 11:13:36.450945
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # A known Pygments style should be resolved normally.
    expected_style = pygments.styles.get_style_by_name('default')
    assert ColorFormatter.get_style_class('default') is expected_style

    # An unavailable style should fall back to the bundled Solarized style.
    assert (
        ColorFormatter.get_style_class('nonexistent-style')
        is Solarized256Style
    )

# Generated at 2026-10-25 11:13:46.411258
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from unittest.mock import Mock, patch

    color_formatter = ColorFormatter.__new__(ColorFormatter)
    color_formatter.formatter = Mock()

    lexer = Mock(spec=Lexer)
    body = '{"message": "ok"}'
    mime = 'application/json'
    highlighted_body = '<highlighted body>'

    with (
        patch.object(
            color_formatter,
            'get_lexer_for_body',
            return_value=lexer,
        ) as get_lexer,
        patch.object(
            pygments,
            'highlight',
            return_value=highlighted_body,
        ) as highlight,
    ):
        result = color_formatter.format_body(body, mime)

    assert result == highlighted_body
    get_lexer.assert_called_once_with(mime, body)
    highlight.assert_called_once_with(
        code=body,
        lexer=lexer,
        formatter=color_formatter.formatter,
    )

    # If no lexer matches, the original body must be returned unchanged.
    with (
        patch.object(
            color_formatter,
            'get_lexer_for_body',
            return_value=None,
        ),
        patch.object(pygments, 'highlight') as highlight,
    ):
        result = color_formatter.format_body(body, 'unknown/type')

    assert result == body
    highlight.assert_not_called()

# Generated at 2026-10-25 11:13:49.273458
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 11:13:50.626378
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 11:13:52.329415
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 11:14:02.096290
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    color_formatter = object.__new__(ColorFormatter)
    color_formatter.http_lexer = object()
    color_formatter.formatter = object()

    headers = 'Content-Type: application/json\r\n'
    highlighted = '\n  highlighted headers  \n'

    with patch.object(
        pygments,
        'highlight',
        return_value=highlighted,
    ) as mock_highlight:
        result = color_formatter.format_headers(headers)

    assert result == 'highlighted headers'
    mock_highlight.assert_called_once_with(
        code=headers,
        lexer=color_formatter.http_lexer,
        formatter=color_formatter.formatter,
    )

# Generated at 2026-10-25 11:14:18.600666
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

# Generated at 2026-10-25 11:14:28.203163
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 11:14:36.030280
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():formatter = ColorFormatter.__new__(ColorFormatter)

# Generated at 2026-10-25 11:14:53.524774
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from pygments.formatter import Formatter


# Generated at 2026-10-25 11:15:03.345668
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from unittest.mock import Mock, patch

    color_formatter = object.__new__(ColorFormatter)
    color_formatter.http_lexer = Mock()
    color_formatter.formatter = Mock()

    headers = 'Content-Type: application/json\r\n'
    highlighted = '\n  highlighted headers  \n'

    with patch.object(
        pygments,
        'highlight',
        return_value=highlighted,
    ) as highlight:
        result = color_formatter.format_headers(headers)

    assert result == 'highlighted headers'
    highlight.assert_called_once_with(
        code=headers,
        lexer=color_formatter.http_lexer,
        formatter=color_formatter.formatter,
    )

# Generated at 2026-10-25 11:15:19.800291
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

# Generated at 2026-10-25 11:15:36.300496
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

# Generated at 2026-10-25 11:15:40.919897
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 11:15:42.408084
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 11:15:43.744304
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 11:15:54.608823
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():from unittest.mock import Mock, sentinel


# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body(monkeypatch):
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.formatter = sentinel.formatter

    highlight = Mock(return_value='highlighted body')
    monkeypatch.setattr(pygments, 'highlight', highlight)

    # A recognized MIME type causes the body to be highlighted.
    formatter.get_lexer_for_body = Mock(return_value=sentinel.lexer)

    result = formatter.format_body(
        body='{"key": "value"}',
        mime='application/json',
    )

    assert result == 'highlighted body'
    formatter.get_lexer_for_body.assert_called_once_with(
        'application/json',
        '{"key": "value"}',
    )
    highlight.assert_called_once_with(
        code='{"key": "value"}',
        lexer=sentinel.lexer,
        formatter=sentinel.formatter,
    )

    # An unrecognized MIME type returns the body unchanged.
    formatter.get_lexer_for_body.reset_mock(return_value=True)
    formatter.get_lexer_for_body.return_value = None
    highlight.reset_mock()

    result = formatter.format_body(
        body='plain body',
        mime='application/octet-stream',
    )

    assert result == 'plain body'
    formatter.get_lexer_for_body.assert_called_once_with(
        'application/octet-stream',
        'plain body',
    )
    highlight.assert_not_called()

# Generated at 2026-10-25 11:16:14.659067
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

# Generated at 2026-10-25 11:16:31.511499
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

# Generated at 2026-10-25 11:16:49.597336
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