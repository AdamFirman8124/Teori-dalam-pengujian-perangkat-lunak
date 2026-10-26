

# Generated at 2026-10-25 11:08:50.461859
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 11:08:52.875725
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 11:08:55.291797
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 11:08:57.709457
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 11:09:00.132543
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 11:09:02.552488
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 11:09:05.620216
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 11:09:17.396550
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 11:09:20.297771
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 11:09:35.419057
# Unit test for function get_lexer
def test_get_lexer():lexer = module_0.get_lexer('application/json')

# Generated at 2026-10-25 11:09:44.024878
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from unittest.mock import Mock, patch

    color_formatter = ColorFormatter.__new__(ColorFormatter)
    color_formatter.http_lexer = Mock(name='http_lexer')
    color_formatter.formatter = Mock(name='formatter')

    with patch.object(
        pygments,
        'highlight',
        return_value='\n  highlighted headers  \n',
    ) as highlight:
        result = color_formatter.format_headers('Content-Type: application/json')

    assert result == 'highlighted headers'
    highlight.assert_called_once_with(
        code='Content-Type: application/json',
        lexer=color_formatter.http_lexer,
        formatter=color_formatter.formatter,
    )

# Generated at 2026-10-25 11:09:53.134416
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from unittest.mock import Mock, patch

# Generated at 2026-10-25 11:10:19.349124
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # Returns the requested Pygments style when it exists.
    expected_style = pygments.styles.get_style_by_name('fruity')
    assert ColorFormatter.get_style_class('fruity') is expected_style

    # Falls back to the bundled Solarized style for unknown schemes.
    assert (
        ColorFormatter.get_style_class('__nonexistent_style__')
        is Solarized256Style
    )

# Generated at 2026-10-25 11:10:40.853907
# Unit test for function get_lexer
def test_get_lexer():json_lexer = module_0.get_lexer('application/json')

# Generated at 2026-10-25 11:10:52.424925
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from unittest.mock import Mock, patch

    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.formatter = Mock(name='formatter')
    formatter.get_lexer_for_body = Mock()

    body = '{"message": "ok"}'
    mime = 'application/json'
    lexer = Mock(name='lexer')
    highlighted_body = '\x1b[32m{"message": "ok"}\x1b[0m\n'

    with patch.object(
        pygments,
        'highlight',
        return_value=highlighted_body,
    ) as highlight:
        # A recognized body is syntax-highlighted.
        formatter.get_lexer_for_body.return_value = lexer

        result = formatter.format_body(body, mime)

        assert result == highlighted_body
        formatter.get_lexer_for_body.assert_called_once_with(mime, body)
        highlight.assert_called_once_with(
            code=body,
            lexer=lexer,
            formatter=formatter.formatter,
        )

        # An unrecognized body is returned unchanged.
        formatter.get_lexer_for_body.reset_mock()
        formatter.get_lexer_for_body.return_value = None
        highlight.reset_mock()

        result = formatter.format_body(body, 'application/octet-stream')

        assert result == body
        formatter.get_lexer_for_body.assert_called_once_with(
            'application/octet-stream',
            body,
        )
        highlight.assert_not_called()

# Generated at 2026-10-25 11:11:03.002812
# Unit test for function get_lexer
def test_get_lexer():json_lexer_type = type(pygments.lexers.get_lexer_by_name('json'))


# Generated at 2026-10-25 11:11:14.534151
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from unittest.mock import Mock, call, patch, sentinel

    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.formatter = sentinel.formatter
    formatter.get_lexer_for_body = Mock(
        side_effect=[sentinel.lexer, None]
    )

    with patch.object(
        pygments,
        'highlight',
        return_value='highlighted body',
    ) as highlight:
        # A recognized MIME type is syntax-highlighted.
        result = formatter.format_body(
            body='{"message": "ok"}',
            mime='application/json',
        )

        assert result == 'highlighted body'
        highlight.assert_called_once_with(
            code='{"message": "ok"}',
            lexer=sentinel.lexer,
            formatter=sentinel.formatter,
        )

        # An unrecognized MIME type leaves the body unchanged.
        highlight.reset_mock()
        result = formatter.format_body(
            body='plain body',
            mime='application/octet-stream',
        )

        assert result == 'plain body'
        highlight.assert_not_called()

    assert formatter.get_lexer_for_body.call_args_list == [
        call('application/json', '{"message": "ok"}'),
        call('application/octet-stream', 'plain body'),
    ]

# Generated at 2026-10-25 11:11:27.350043
# Unit test for function get_lexer
def test_get_lexer():json_lexer = module_0.get_lexer('application/json')

# Generated at 2026-10-25 11:11:50.078597
# Unit test for function get_lexer
def test_get_lexer():json_lexer = module_0.get_lexer('application/json')

# Generated at 2026-10-25 11:12:00.316830
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from unittest.mock import Mock, patch

    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.formatter = Mock()
    lexer = Mock()
    body = '{"message": "ok"}'
    mime = 'application/json'
    highlighted_body = '<highlighted body>'

    with (
        patch.object(
            formatter,
            'get_lexer_for_body',
            return_value=lexer,
        ) as get_lexer_for_body,
        patch.object(
            pygments,
            'highlight',
            return_value=highlighted_body,
        ) as highlight,
    ):
        result = formatter.format_body(body=body, mime=mime)

    get_lexer_for_body.assert_called_once_with(mime, body)
    highlight.assert_called_once_with(
        code=body,
        lexer=lexer,
        formatter=formatter.formatter,
    )
    assert result == highlighted_body

# Generated at 2026-10-25 11:12:18.542565
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

# Generated at 2026-10-25 11:12:28.791665
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from unittest.mock import Mock, patch, sentinel

    color_formatter = ColorFormatter.__new__(ColorFormatter)
    color_formatter.formatter = sentinel.formatter
    color_formatter.get_lexer_for_body = Mock(return_value=sentinel.lexer)

    with patch.object(
        pygments,
        'highlight',
        return_value='highlighted body',
    ) as highlight:
        result = color_formatter.format_body(
            body='{"key": "value"}',
            mime='application/json',
        )

    assert result == 'highlighted body'
    color_formatter.get_lexer_for_body.assert_called_once_with(
        'application/json',
        '{"key": "value"}',
    )
    highlight.assert_called_once_with(
        code='{"key": "value"}',
        lexer=sentinel.lexer,
        formatter=sentinel.formatter,
    )

# Generated at 2026-10-25 11:12:40.137202
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from unittest.mock import patch, sentinel

    color_formatter = ColorFormatter.__new__(ColorFormatter)
    color_formatter.http_lexer = sentinel.http_lexer
    color_formatter.formatter = sentinel.formatter

    headers = 'HTTP/1.1 200 OK\r\nContent-Type: application/json'
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
        lexer=sentinel.http_lexer,
        formatter=sentinel.formatter,
    )

# Generated at 2026-10-25 11:12:48.240505
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from unittest.mock import Mock, patch

    color_formatter = object.__new__(ColorFormatter)
    color_formatter.http_lexer = Mock()
    color_formatter.formatter = Mock()

    headers = 'HTTP/1.1 200 OK\nContent-Type: application/json'
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

# Generated at 2026-10-25 11:12:50.789031
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 11:12:53.207825
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 11:12:55.794161
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 11:12:58.212255
# Unit test for function get_lexer

# Generated at 2026-10-25 11:13:00.628157
# Unit test for function get_lexer

# Generated at 2026-10-25 11:13:03.053480
# Unit test for function get_lexer

# Generated at 2026-10-25 11:13:05.466433
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 11:13:07.887266
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 11:13:10.304543
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 11:13:23.904871
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from types import SimpleNamespace


# Generated at 2026-10-25 11:13:47.222289
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

# Generated at 2026-10-25 11:13:59.716568
# Unit test for function get_lexer
def test_get_lexer():json_lexer_type = type(
        pygments.lexers.get_lexer_by_name('json')
    )


# Generated at 2026-10-25 11:14:16.719048
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 11:14:18.114242
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

# Generated at 2026-10-25 11:14:31.880620
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from types import SimpleNamespace

# Generated at 2026-10-25 11:14:48.675847
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from types import SimpleNamespace


# Generated at 2026-10-25 11:15:00.645794
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.formatter = Mock()

    body = '{"message": "success"}'
    mime = 'application/json'
    lexer = Mock()
    highlighted_body = '<highlighted body>'

    # A recognized lexer causes the body to be highlighted.
    with (
        patch.object(
            formatter,
            'get_lexer_for_body',
            return_value=lexer,
        ) as get_lexer,
        patch.object(
            pygments,
            'highlight',
            return_value=highlighted_body,
        ) as highlight,
    ):
        result = formatter.format_body(body, mime)

    assert result == highlighted_body
    get_lexer.assert_called_once_with(mime, body)
    highlight.assert_called_once_with(
        code=body,
        lexer=lexer,
        formatter=formatter.formatter,
    )

    # Without a suitable lexer, the original body is returned unchanged.
    with (
        patch.object(
            formatter,
            'get_lexer_for_body',
            return_value=None,
        ) as get_lexer,
        patch.object(pygments, 'highlight') as highlight,
    ):
        result = formatter.format_body(body, 'application/octet-stream')

    assert result == body
    get_lexer.assert_called_once_with('application/octet-stream', body)
    highlight.assert_not_called()

# Generated at 2026-10-25 11:15:10.477688
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from unittest.mock import Mock, patch, sentinel

    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.http_lexer = sentinel.http_lexer
    formatter.formatter = sentinel.formatter

    highlighted = '\n\x1b[34mHTTP/1.1 200 OK\x1b[0m\n'
    headers = 'HTTP/1.1 200 OK'

    with patch.object(
        pygments,
        'highlight',
        Mock(return_value=highlighted),
    ) as mock_highlight:
        result = formatter.format_headers(headers)

    assert result == highlighted.strip()
    mock_highlight.assert_called_once_with(
        code=headers,
        lexer=sentinel.http_lexer,
        formatter=sentinel.formatter,
    )

# Generated at 2026-10-25 11:15:19.795604
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.formatter = sentinel.formatter
    formatter.get_lexer_for_body = Mock(return_value=sentinel.lexer)

    with patch.object(
        pygments,
        'highlight',
        return_value='highlighted body',
    ) as highlight:
        result = formatter.format_body(
            body='{"message": "hello"}',
            mime='application/json',
        )

    assert result == 'highlighted body'
    formatter.get_lexer_for_body.assert_called_once_with(
        'application/json',
        '{"message": "hello"}',
    )
    highlight.assert_called_once_with(
        code='{"message": "hello"}',
        lexer=sentinel.lexer,
        formatter=sentinel.formatter,
    )

# Generated at 2026-10-25 11:15:27.911564
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():lexer = SimplifiedHTTPLexer()


# Generated at 2026-10-25 11:15:46.521510
# Unit test for function get_lexer
def test_get_lexer():json_lexer_type = type(pygments.lexers.get_lexer_by_name('json'))


# Generated at 2026-10-25 11:15:58.807380
# Unit test for function get_lexer
def test_get_lexer():lexer = module_0.get_lexer('application/json')

# Generated at 2026-10-25 11:16:11.097995
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from types import SimpleNamespace


# Generated at 2026-10-25 11:16:20.313660
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from unittest.mock import patch, sentinel

    color_formatter = ColorFormatter.__new__(ColorFormatter)
    color_formatter.http_lexer = sentinel.http_lexer
    color_formatter.formatter = sentinel.formatter

    headers = 'Content-Type: application/json\r\n'

    with patch.object(
        pygments,
        'highlight',
        return_value='\n  highlighted headers  \n',
    ) as highlight:
        result = color_formatter.format_headers(headers)

    assert result == 'highlighted headers'
    highlight.assert_called_once_with(
        code=headers,
        lexer=sentinel.http_lexer,
        formatter=sentinel.formatter,
    )

# Generated at 2026-10-25 11:16:32.497856
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 11:16:35.077887
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

# Generated at 2026-10-25 11:16:38.621293
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 11:16:41.509883
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 11:16:43.048354
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 11:16:57.875633
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 11:17:17.077896
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():from pygments.formatters.other import NullFormatter


# Generated at 2026-10-25 11:17:51.038387
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():lexer = SimplifiedHTTPLexer()


# Generated at 2026-10-25 11:17:59.422463
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    from unittest.mock import patch

    expected_style = pygments.styles.get_style_by_name('monokai')

    with patch.object(
        pygments.styles,
        'get_style_by_name',
        return_value=expected_style,
    ) as get_style:
        assert ColorFormatter.get_style_class('monokai') is expected_style
        get_style.assert_called_once_with('monokai')

    with patch.object(
        pygments.styles,
        'get_style_by_name',
        side_effect=ClassNotFound,
    ):
        assert (
            ColorFormatter.get_style_class('unknown-style')
            is Solarized256Style
        )

# Generated at 2026-10-25 11:18:07.424949
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    headers = 'HTTP/1.1 200 OK\nContent-Type: application/json'
    lexer = Mock(spec=Lexer)
    formatter = Mock()

    color_formatter = ColorFormatter.__new__(ColorFormatter)
    color_formatter.http_lexer = lexer
    color_formatter.formatter = formatter

    with patch.object(
        pygments,
        'highlight',
        return_value='\n  highlighted headers  \n',
    ) as highlight:
        result = color_formatter.format_headers(headers)

    assert result == 'highlighted headers'
    highlight.assert_called_once_with(
        code=headers,
        lexer=lexer,
        formatter=formatter,
    )

# Generated at 2026-10-25 11:18:18.073057
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from types import SimpleNamespace


# Generated at 2026-10-25 11:18:37.221955
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from types import SimpleNamespace


# Generated at 2026-10-25 11:18:47.228812
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from unittest.mock import Mock, patch

    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.formatter = Mock()

    body = '{"message": "success"}'
    mime = 'application/json'
    lexer = Mock()
    highlighted_body = '\x1b[32m{"message": "success"}\x1b[0m'

    formatter.get_lexer_for_body = Mock(return_value=lexer)

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
        lexer=lexer,
        formatter=formatter.formatter,
    )

    # If no lexer is available, the body should remain unchanged.
    formatter.get_lexer_for_body.reset_mock(return_value=True)
    formatter.get_lexer_for_body.return_value = None

    with patch.object(pygments, 'highlight') as highlight:
        result = formatter.format_body(body, 'application/octet-stream')

    assert result == body
    highlight.assert_not_called()

# Generated at 2026-10-25 11:19:08.857412
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():import sys