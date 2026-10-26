

# Generated at 2026-10-25 07:54:07.887273
# Unit test for constructor of class Solarized256Style
def test_Solarized256Style():
    style = Solarized256Style()

    assert isinstance(style, pygments.style.Style)
    assert style.background_color == "#1c1c1c"

    expected_palette = {
        "BASE03": "#1c1c1c",
        "BASE02": "#262626",
        "BASE01": "#4e4e4e",
        "BASE00": "#585858",
        "BASE0": "#808080",
        "BASE1": "#8a8a8a",
        "BASE2": "#d7d7af",
        "BASE3": "#ffffd7",
        "YELLOW": "#af8700",
        "ORANGE": "#d75f00",
        "RED": "#af0000",
        "MAGENTA": "#af005f",
        "VIOLET": "#5f5faf",
        "BLUE": "#0087ff",
        "CYAN": "#00afaf",
        "GREEN": "#5f8700",
    }

    for name, color in expected_palette.items():
        assert getattr(style, name) == color

    expected_token_styles = {
        pygments.token.Keyword: style.GREEN,
        pygments.token.Keyword.Constant: style.ORANGE,
        pygments.token.Keyword.Declaration: style.BLUE,
        pygments.token.Keyword.Namespace: style.ORANGE,
        pygments.token.Keyword.Reserved: style.BLUE,
        pygments.token.Keyword.Type: style.RED,
        pygments.token.Name.Attribute: style.BASE1,
        pygments.token.Name.Builtin: style.BLUE,
        pygments.token.Name.Class: style.BLUE,
        pygments.token.Name.Constant: style.ORANGE,
        pygments.token.Name.Exception: style.YELLOW,
        pygments.token.Name.Function: style.BLUE,
        pygments.token.String: style.CYAN,
        pygments.token.String.Escape: style.RED,
        pygments.token.Number: style.CYAN,
        pygments.token.Operator: style.BASE1,
        pygments.token.Comment: style.BASE01,
        pygments.token.Generic.Emph: "italic",
        pygments.token.Generic.Strong: "bold",
        pygments.token.Token: style.BASE1,
        pygments.token.Token.Other: style.ORANGE,
    }

    for token, expected_style in expected_token_styles.items():
        assert style.styles[token] == expected_style

# Generated at 2026-10-25 07:54:17.602154
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    color_formatter = ColorFormatter.__new__(ColorFormatter)
    color_formatter.formatter = sentinel.formatter

    body = '{"message": "ok"}'
    mime = 'application/json'

    # A matching lexer causes the body to be highlighted.
    color_formatter.get_lexer_for_body = Mock(
        return_value=sentinel.lexer
    )

    with patch.object(
        pygments,
        'highlight',
        return_value=sentinel.highlighted_body,
    ) as highlight:
        result = color_formatter.format_body(body, mime)

    assert result is sentinel.highlighted_body
    color_formatter.get_lexer_for_body.assert_called_once_with(mime, body)
    highlight.assert_called_once_with(
        code=body,
        lexer=sentinel.lexer,
        formatter=sentinel.formatter,
    )

    # Without a matching lexer, the original body is returned unchanged.
    color_formatter.get_lexer_for_body.reset_mock()
    color_formatter.get_lexer_for_body.return_value = None

    with patch.object(pygments, 'highlight') as highlight:
        result = color_formatter.format_body(body, mime)

    assert result == body
    color_formatter.get_lexer_for_body.assert_called_once_with(mime, body)
    highlight.assert_not_called()

# Generated at 2026-10-25 07:54:38.292624
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 07:54:40.706080
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 07:54:43.120680
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 07:54:45.533856
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 07:54:47.947591
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 07:54:50.360617
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 07:54:52.912509
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 07:54:55.319536
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 07:55:08.315200
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from httpie.context import Environment

# Generated at 2026-10-25 07:55:10.730985
# Unit test for function get_lexer

# Generated at 2026-10-25 07:55:17.324097
# Unit test for function get_lexer
def test_get_lexer():lexer = module_0.get_lexer(mime='application/json', explicit_json=False, body='{"ok": true}')

# Generated at 2026-10-25 07:55:27.871934
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.formatter = sentinel.formatter
    formatter.get_lexer_for_body = Mock(return_value=sentinel.lexer)

    body = '{"message": "success"}'
    mime = 'application/json'
    highlighted_body = '<highlighted body>'

    with patch.object(
        pygments,
        'highlight',
        return_value=highlighted_body,
    ) as highlight:
        result = formatter.format_body(body=body, mime=mime)

    assert result == highlighted_body
    formatter.get_lexer_for_body.assert_called_once_with(mime, body)
    highlight.assert_called_once_with(
        code=body,
        lexer=sentinel.lexer,
        formatter=sentinel.formatter,
    )

    # The original body should be returned unchanged when no lexer is found.
    formatter.get_lexer_for_body.reset_mock(return_value=True)
    formatter.get_lexer_for_body.return_value = None

    with patch.object(pygments, 'highlight') as highlight:
        result = formatter.format_body(body=body, mime='unknown/type')

    assert result == body
    formatter.get_lexer_for_body.assert_called_once_with(
        'unknown/type',
        body,
    )
    highlight.assert_not_called()

# Generated at 2026-10-25 07:55:38.112788
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.explicit_json = True

    mime = 'application/json'
    body = '{"message": "ok"}'

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

# Generated at 2026-10-25 07:55:40.532326
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 07:55:43.075689
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 07:55:45.487776
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 07:55:47.901683
# Unit test for function get_lexer

# Generated at 2026-10-25 07:55:50.323901
# Unit test for function get_lexer

# Generated at 2026-10-25 07:55:52.732261
# Unit test for function get_lexer

# Generated at 2026-10-25 07:55:55.145130
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 07:55:57.557878
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 07:56:07.707118
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from pygments.formatters.other import NullFormatter


# Generated at 2026-10-25 07:56:17.010526
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.explicit_json = True

    mime = 'application/json'
    body = '{"status": "ok"}'
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

# Generated at 2026-10-25 07:56:35.457276
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from types import SimpleNamespace
    from unittest.mock import patch

    # Formatting is disabled when the environment does not support colors.
    disabled = ColorFormatter(
        env=SimpleNamespace(colors=0),
        explicit_json=True,
        color_scheme=AUTO_STYLE,
    )
    assert disabled.enabled is False
    assert not hasattr(disabled, 'formatter')
    assert not hasattr(disabled, 'http_lexer')

    # Auto style always uses the standard HTTP lexer and terminal formatter.
    automatic = ColorFormatter(
        env=SimpleNamespace(colors=256),
        explicit_json=True,
        color_scheme=AUTO_STYLE,
    )
    assert automatic.explicit_json is True
    assert isinstance(automatic.http_lexer, PygmentsHttpLexer)
    assert isinstance(automatic.formatter, TerminalFormatter)

    # Non-256-color terminals also use the standard formatter.
    limited_color = ColorFormatter(
        env=SimpleNamespace(colors=16),
        color_scheme='monokai',
    )
    assert limited_color.explicit_json is False
    assert isinstance(limited_color.http_lexer, PygmentsHttpLexer)
    assert isinstance(limited_color.formatter, TerminalFormatter)

    # A custom scheme on a 256-color terminal uses the simplified lexer
    # and the 256-color formatter.
    with patch.object(
        ColorFormatter,
        'get_style_class',
        return_value=Solarized256Style,
    ) as get_style_class:
        custom = ColorFormatter(
            env=SimpleNamespace(colors=256),
            color_scheme=SOLARIZED_STYLE,
        )

    get_style_class.assert_called_once_with(SOLARIZED_STYLE)
    assert custom.explicit_json is False
    assert isinstance(custom.http_lexer, SimplifiedHTTPLexer)
    assert isinstance(custom.formatter, Terminal256Formatter)

# Generated at 2026-10-25 07:56:38.025337
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 07:56:40.442972
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 07:56:42.854720
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 07:56:45.271687
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 07:56:47.681743
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 07:56:50.100134
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 07:56:52.513423
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 07:56:54.929882
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 07:56:57.345227
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 07:56:59.760550
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 07:57:02.177391
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 07:57:04.589865
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 07:57:07.005918
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 07:57:09.419621
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 07:57:11.836331
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 07:57:14.250430
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 07:57:16.666287
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 07:57:23.297356
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = ColorFormatter.__new__(ColorFormatter)

# Generated at 2026-10-25 07:57:29.523814
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

# Generated at 2026-10-25 07:57:39.251626
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    color_formatter = ColorFormatter.__new__(ColorFormatter)
    color_formatter.http_lexer = Mock(spec=Lexer)
    color_formatter.formatter = Mock()

    headers = 'Content-Type: application/json\n'
    highlighted_headers = '  highlighted headers\n'

    with patch.object(
        pygments,
        'highlight',
        return_value=highlighted_headers,
    ) as highlight:
        result = color_formatter.format_headers(headers)

    assert result == 'highlighted headers'
    highlight.assert_called_once_with(
        code=headers,
        lexer=color_formatter.http_lexer,
        formatter=color_formatter.formatter,
    )

# Generated at 2026-10-25 07:57:41.816008
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 07:57:44.230756
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 07:57:46.644757
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 07:57:49.058798
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 07:57:51.480772
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 07:57:53.895139
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 07:57:56.308622
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 07:57:58.723343
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 07:58:01.137883
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 07:58:03.553068
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 07:58:05.969515
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 07:58:08.383322
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 07:58:10.801991
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 07:58:13.211684
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 07:58:15.627398
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 07:58:18.040966
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 07:58:20.454711
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 07:58:22.869998
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 07:58:25.283442
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 07:58:39.605769
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():formatter = ColorFormatter.__new__(ColorFormatter)

# Generated at 2026-10-25 07:58:49.109176
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 07:58:58.817717
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from unittest import mock

    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.formatter = mock.sentinel.formatter

    body = '{"message": "success"}'
    mime = 'application/json'
    lexer = mock.sentinel.lexer
    highlighted_body = mock.sentinel.highlighted_body

    # A recognized body type is syntax-highlighted.
    with mock.patch.object(
        formatter,
        'get_lexer_for_body',
        return_value=lexer,
    ) as get_lexer, mock.patch.object(
        pygments,
        'highlight',
        return_value=highlighted_body,
    ) as highlight:
        result = formatter.format_body(body, mime)

    assert result is highlighted_body
    get_lexer.assert_called_once_with(mime, body)
    highlight.assert_called_once_with(
        code=body,
        lexer=lexer,
        formatter=formatter.formatter,
    )

    # An unrecognized body type is returned unchanged.
    with mock.patch.object(
        formatter,
        'get_lexer_for_body',
        return_value=None,
    ) as get_lexer, mock.patch.object(pygments, 'highlight') as highlight:
        result = formatter.format_body(body, 'application/octet-stream')

    assert result == body
    get_lexer.assert_called_once_with('application/octet-stream', body)
    highlight.assert_not_called()

# Generated at 2026-10-25 07:59:01.234388
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 07:59:03.648175
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 07:59:06.062290
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 07:59:08.475972
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 07:59:11.172042
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 07:59:13.587734
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 07:59:15.999394
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 07:59:18.415791
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 07:59:21.010828
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 07:59:23.424854
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 07:59:25.839229
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 07:59:28.256713
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 07:59:30.669693
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 07:59:33.087419
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 07:59:35.568212
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 07:59:37.984855
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 07:59:40.399011
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 07:59:42.812567
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 07:59:45.434171
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 07:59:47.851422
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 07:59:50.264965
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 07:59:52.678044
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 07:59:55.097137
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 07:59:57.507015
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 07:59:59.921799
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:00:02.339003
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:00:04.754308
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:00:07.169069
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:00:09.582573
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:00:11.997970
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:00:14.412960
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:00:16.827004
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:00:19.239969
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:00:21.654779
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:00:24.069203
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:00:26.482314
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:00:34.615440
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():default_style = pygments.styles.get_style_by_name('default')


# Generated at 2026-10-25 08:00:35.987219
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

# Generated at 2026-10-25 08:00:37.326636
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

# Generated at 2026-10-25 08:00:46.235364
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = SimpleNamespace(colors=256)
    formatter = ColorFormatter(
        env=env,
        color_scheme=AUTO_STYLE,
    )
    headers = 'Content-Type: application/json\r\n'

    with patch.object(
        pygments,
        'highlight',
        return_value='\nhighlighted headers\n',
    ) as mock_highlight:
        result = formatter.format_headers(headers)

    assert result == 'highlighted headers'
    mock_highlight.assert_called_once_with(
        code=headers,
        lexer=formatter.http_lexer,
        formatter=formatter.formatter,
    )

# Generated at 2026-10-25 08:00:47.669172
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

# Generated at 2026-10-25 08:00:56.255142
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = object.__new__(ColorFormatter)
    formatter.explicit_json = True

    with patch(
        f'{ColorFormatter.__module__}.get_lexer',
        return_value=sentinel.lexer,
    ) as mock_get_lexer:
        result = formatter.get_lexer_for_body(
            mime='application/json',
            body='{"message": "ok"}',
        )

    assert result is sentinel.lexer
    mock_get_lexer.assert_called_once_with(
        mime='application/json',
        explicit_json=True,
        body='{"message": "ok"}',
    )

# Generated at 2026-10-25 08:00:58.883161
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:01:01.298093
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:01:03.711626
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:01:06.127388
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:01:08.545960
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:01:10.963134
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:01:13.544300
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:01:15.958880
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:01:18.373228
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:01:20.788114
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:01:23.202146
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:01:25.616618
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:01:28.048210
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:01:30.540797
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:01:32.957514
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:01:35.368217
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:01:37.783010
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:01:40.200295
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:01:42.614275
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:01:45.031316
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:01:47.446430
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 08:01:49.861584
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:01:52.277409
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:02:01.654840
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():formatter = ColorFormatter.__new__(ColorFormatter)

# Generated at 2026-10-25 08:02:14.710074
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    formatter = object.__new__(ColorFormatter)
    formatter.http_lexer = sentinel.http_lexer
    formatter.formatter = sentinel.formatter

    headers = 'HTTP/1.1 200 OK\nContent-Type: application/json'
    highlighted = '\n\x1b[34mhighlighted headers\x1b[0m\n'

    with patch.object(
        pygments,
        'highlight',
        return_value=highlighted,
    ) as mock_highlight:
        result = formatter.format_headers(headers)

    assert result == highlighted.strip()
    mock_highlight.assert_called_once_with(
        code=headers,
        lexer=sentinel.http_lexer,
        formatter=sentinel.formatter,
    )

# Generated at 2026-10-25 08:02:16.143095
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

# Generated at 2026-10-25 08:02:26.484852
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.http_lexer = sentinel.http_lexer
    formatter.formatter = sentinel.formatter
    headers = 'HTTP/1.1 200 OK\r\nContent-Type: application/json'

    with patch.object(
        pygments,
        'highlight',
        return_value='\n  highlighted headers  \n',
    ) as mock_highlight:
        result = formatter.format_headers(headers)

    assert result == 'highlighted headers'
    mock_highlight.assert_called_once_with(
        code=headers,
        lexer=sentinel.http_lexer,
        formatter=sentinel.formatter,
    )

# Generated at 2026-10-25 08:02:28.901494
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:02:31.315599
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:02:33.798897
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 08:02:36.162002
# Unit test for function get_lexer

# Generated at 2026-10-25 08:02:38.577734
# Unit test for function get_lexer

# Generated at 2026-10-25 08:02:40.991016
# Unit test for function get_lexer

# Generated at 2026-10-25 08:02:43.405383
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:02:45.819037
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:02:48.235586
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:02:50.648050
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:02:53.062225
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:02:55.477041
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:03:05.193295
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    # Bypass __init__ so this test only exercises module_0.get_lexer_for_body().
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

# Generated at 2026-10-25 08:03:31.714865
# Unit test for function get_lexer
def test_get_lexer():lexer = module_0.get_lexer('application/json')

# Generated at 2026-10-25 08:03:34.288900
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:03:36.702571
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:03:39.118988
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 08:03:41.936101
# Unit test for function get_lexer

# Generated at 2026-10-25 08:03:44.376335
# Unit test for function get_lexer

# Generated at 2026-10-25 08:03:46.790464
# Unit test for function get_lexer

# Generated at 2026-10-25 08:03:49.203264
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:03:51.618612
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 08:03:54.076106
# Unit test for constructor of class ColorFormatter