

# Generated at 2026-10-25 01:47:13.757619
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

# Generated at 2026-10-25 01:47:22.746136
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.explicit_json = True

    expected_lexer = object()
    module = sys.modules[ColorFormatter.__module__]

    with patch.object(
        module,
        'get_lexer',
        return_value=expected_lexer,
    ) as mocked_get_lexer:
        result = formatter.get_lexer_for_body(
            mime='application/json',
            body='{"status": "ok"}',
        )

    assert result is expected_lexer
    mocked_get_lexer.assert_called_once_with(
        mime='application/json',
        explicit_json=True,
        body='{"status": "ok"}',
    )

# Generated at 2026-10-25 01:47:31.859112
# Unit test for constructor of class Solarized256Style
def test_Solarized256Style():
    style = Solarized256Style()

    assert isinstance(style, Solarized256Style)
    assert isinstance(style, pygments.style.Style)
    assert style.background_color == "#1c1c1c"

    assert style.styles[pygments.token.Keyword] == "#5f8700"
    assert style.styles[pygments.token.Name.Function] == "#0087ff"
    assert style.styles[pygments.token.String] == "#00afaf"
    assert style.styles[pygments.token.Generic.Emph] == "italic"
    assert style.styles[pygments.token.Generic.Strong] == "bold"

# Generated at 2026-10-25 01:47:49.447900
# Unit test for constructor of class Solarized256Style
def test_Solarized256Style():
    style = Solarized256Style()

    assert isinstance(style, Solarized256Style)
    assert isinstance(style, pygments.style.Style)

    assert style.background_color == "#1c1c1c"

    assert style.styles[pygments.token.Keyword] == style.GREEN
    assert style.styles[pygments.token.Keyword.Reserved] == style.BLUE
    assert style.styles[pygments.token.Name.Attribute] == style.BASE1
    assert style.styles[pygments.token.Name.Exception] == style.YELLOW
    assert style.styles[pygments.token.String] == style.CYAN
    assert style.styles[pygments.token.Number] == style.CYAN
    assert style.styles[pygments.token.Operator] == style.BASE1
    assert style.styles[pygments.token.Comment] == style.BASE01
    assert style.styles[pygments.token.Generic.Emph] == "italic"
    assert style.styles[pygments.token.Generic.Strong] == "bold"

# Generated at 2026-10-25 01:47:51.972607
# Unit test for constructor of class Solarized256Style

# Generated at 2026-10-25 01:47:54.386984
# Unit test for constructor of class Solarized256Style

# Generated at 2026-10-25 01:47:57.007456
# Unit test for constructor of class Solarized256Style

# Generated at 2026-10-25 01:47:59.425782
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 01:48:01.841773
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 01:48:04.259672
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 01:48:06.677169
# Unit test for function get_lexer

# Generated at 2026-10-25 01:48:13.229566
# Unit test for function get_lexer
def test_get_lexer():lexer = module_0.get_lexer(
        mime='application/json',
        explicit_json=False,
        body='{"ok": true}',
    )

# Generated at 2026-10-25 01:48:42.514139
# Unit test for function get_lexer
def test_get_lexer():json_lexer_type = type(pygments.lexers.get_lexer_by_name('json'))


# Generated at 2026-10-25 01:48:53.722346
# Unit test for function get_lexer
def test_get_lexer():json_lexer_type = type(pygments.lexers.get_lexer_by_name('json'))

# Generated at 2026-10-25 01:48:56.146367
# Unit test for function get_lexer

# Generated at 2026-10-25 01:48:58.558414
# Unit test for function get_lexer

# Generated at 2026-10-25 01:49:00.975043
# Unit test for function get_lexer

# Generated at 2026-10-25 01:49:03.391360
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 01:49:05.805001
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 01:49:08.222479
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 01:49:10.639376
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 01:49:21.734383
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from httpie.context import Environment

    # 256-color terminal + bundled 'solarized' scheme

# Generated at 2026-10-25 01:49:29.523475
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()

    assert isinstance(lexer, pygments.lexer.RegexLexer)
    assert lexer.name == 'HTTP'
    assert lexer.aliases == ['http']
    assert lexer.filenames == ['*.http']
    assert 'root' in lexer.tokens

    # Verify that construction initializes the compiled lexer rules.
    assert 'root' in lexer._tokens
    assert lexer._tokens['root']

# Generated at 2026-10-25 01:49:42.129916
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    # Default construction should not require arguments.
    lexer = SimplifiedHTTPLexer()

    assert isinstance(lexer, Lexer)
    assert isinstance(lexer, pygments.lexer.RegexLexer)
    assert isinstance(lexer, SimplifiedHTTPLexer)

    # Class-level configuration.
    assert SimplifiedHTTPLexer.name == 'HTTP'
    assert SimplifiedHTTPLexer.aliases == ['http']
    assert SimplifiedHTTPLexer.filenames == ['*.http']
    assert 'root' in SimplifiedHTTPLexer.tokens
    assert len(SimplifiedHTTPLexer.tokens['root']) == 3

    # Options are passed through to `pygments.lexer.Lexer`.
    lexer_opts = SimplifiedHTTPLexer(
        stripnl=False,
        ensurenl=False,
        tabsize=4,
        encoding='utf-8'
    )
    assert lexer_opts.stripnl is False
    assert lexer_opts.ensurenl is False
    assert lexer_opts.tabsize == 4
    assert lexer_opts.encoding == 'utf-8'
    assert lexer_opts.options['encoding'] == 'utf-8'

# Generated at 2026-10-25 01:49:50.725373
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 01:50:00.139232
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from types import SimpleNamespace


# Generated at 2026-10-25 01:50:02.900908
# Unit test for function get_lexer

# Generated at 2026-10-25 01:50:05.328341
# Unit test for function get_lexer

# Generated at 2026-10-25 01:50:07.900100
# Unit test for function get_lexer

# Generated at 2026-10-25 01:50:10.435052
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 01:50:20.409649
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 01:50:35.796872
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():formatter = ColorFormatter.__new__(ColorFormatter)

# Generated at 2026-10-25 01:50:43.451428
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from unittest.mock import Mock, patch

    color_formatter = ColorFormatter.__new__(ColorFormatter)
    color_formatter.http_lexer = Mock()
    color_formatter.formatter = Mock()

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
        lexer=color_formatter.http_lexer,
        formatter=color_formatter.formatter,
    )

# Generated at 2026-10-25 01:50:44.800749
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

# Generated at 2026-10-25 01:51:01.176906
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from unittest.mock import patch, sentinel

    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.explicit_json = True

    mime = 'application/problem+json'
    body = '{"message": "Not found"}'

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

# Generated at 2026-10-25 01:51:03.849692
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 01:51:06.263835
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 01:51:08.682841
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 01:51:11.098113
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 01:51:13.740735
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 01:51:16.157647
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 01:51:27.393513
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from unittest.mock import Mock, patch, sentinel

    color_formatter = object.__new__(ColorFormatter)
    color_formatter.formatter = sentinel.formatter
    color_formatter.get_lexer_for_body = Mock(
        return_value=sentinel.lexer
    )

    body = '{"message": "success"}'
    mime = 'application/json'
    highlighted_body = '<highlighted body>'

    # A recognized lexer causes the body to be highlighted.
    with patch.object(
        pygments,
        'highlight',
        return_value=highlighted_body,
    ) as highlight:
        result = color_formatter.format_body(body, mime)

    assert result == highlighted_body
    color_formatter.get_lexer_for_body.assert_called_once_with(mime, body)
    highlight.assert_called_once_with(
        code=body,
        lexer=sentinel.lexer,
        formatter=sentinel.formatter,
    )

    # Without a suitable lexer, the original body is returned unchanged.
    color_formatter.get_lexer_for_body.reset_mock()
    color_formatter.get_lexer_for_body.return_value = None

    with patch.object(pygments, 'highlight') as highlight:
        result = color_formatter.format_body(body, 'application/octet-stream')

    assert result == body
    color_formatter.get_lexer_for_body.assert_called_once_with(
        'application/octet-stream',
        body,
    )
    highlight.assert_not_called()

# Generated at 2026-10-25 01:51:36.574886
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.explicit_json = True

    lexer = formatter.get_lexer_for_body(
        mime='text/plain',
        body='{"message": "hello"}',
    )

    assert lexer is not None
    assert 'json' in lexer.aliases

# Generated at 2026-10-25 01:51:37.925493
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 01:51:43.455241
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():env = type('EnvironmentStub', (), {'colors': 0})()

# Generated at 2026-10-25 01:51:44.889264
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

# Generated at 2026-10-25 01:51:46.224016
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

# Generated at 2026-10-25 01:51:47.561368
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 01:51:52.821674
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():env = Environment(colors=0)

# Generated at 2026-10-25 01:52:02.401427
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from unittest.mock import patch

    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.explicit_json = True

    expected_lexer = object()
    mime = 'application/json'
    body = '{"message": "ok"}'

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

# Generated at 2026-10-25 01:52:11.513474
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 01:52:14.037095
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 01:52:16.452157
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 01:52:18.866044
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 01:52:21.282023
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 01:52:23.697156
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 01:52:26.290112
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 01:53:10.807848
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():import re


# Generated at 2026-10-25 01:53:13.361247
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 01:53:15.775662
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 01:53:18.191016
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-25 01:53:20.604561
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 01:53:23.018983
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 01:53:25.433145
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 01:53:35.174918
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.http_lexer = sentinel.http_lexer
    formatter.formatter = sentinel.formatter

    headers = 'HTTP/1.1 200 OK\r\nContent-Type: application/json'
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

# Generated at 2026-10-25 01:53:43.060009
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():from unittest.mock import Mock, patch


# Unit tests for ColorFormatter.format_body
def test_ColorFormatter_format_body_highlights_when_lexer_is_available():
    color_formatter = ColorFormatter.__new__(ColorFormatter)
    color_formatter.formatter = Mock()

    lexer = Mock()
    color_formatter.get_lexer_for_body = Mock(return_value=lexer)

    with patch.object(
        pygments,
        'highlight',
        return_value='highlighted body',
    ) as highlight:
        result = color_formatter.format_body(
            body='{"key": "value"}',
            mime='application/json',
        )

    color_formatter.get_lexer_for_body.assert_called_once_with(
        'application/json',
        '{"key": "value"}',
    )
    highlight.assert_called_once_with(
        code='{"key": "value"}',
        lexer=lexer,
        formatter=color_formatter.formatter,
    )
    assert result == 'highlighted body'


def test_ColorFormatter_format_body_returns_original_body_without_lexer():
    color_formatter = ColorFormatter.__new__(ColorFormatter)
    color_formatter.formatter = Mock()
    color_formatter.get_lexer_for_body = Mock(return_value=None)

    with patch.object(pygments, 'highlight') as highlight:
        result = color_formatter.format_body(
            body='unrecognized content',
            mime='application/x-unknown',
        )

    color_formatter.get_lexer_for_body.assert_called_once_with(
        'application/x-unknown',
        'unrecognized content',
    )
    highlight.assert_not_called()
    assert result == 'unrecognized content'

# Generated at 2026-10-25 01:53:51.969515
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
            body='{"status": "ok"}',
        )

    assert result is sentinel.lexer
    mock_get_lexer.assert_called_once_with(
        mime='application/json',
        explicit_json=True,
        body='{"status": "ok"}',
    )

# Generated at 2026-10-25 01:54:00.878370
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.explicit_json = True
    expected_lexer = Mock(spec=Lexer)

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

# Generated at 2026-10-25 01:54:02.309638
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-25 01:54:09.277907
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from types import SimpleNamespace


# Generated at 2026-10-25 01:54:18.501182
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.http_lexer = Mock()
    formatter.formatter = Mock()

    headers = 'Content-Type: application/json'

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

# Generated at 2026-10-25 01:54:21.068296
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 01:54:23.484175
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 01:54:25.902042
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 01:54:28.315718
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 01:54:30.730215
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 01:54:33.143737
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-25 01:54:35.558970
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 01:54:37.987194
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 01:54:40.401105
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 01:54:43.047778
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-25 01:55:06.108550
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from pygments.formatters import NullFormatter


# Generated at 2026-10-25 01:55:15.149368
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    color_formatter = ColorFormatter.__new__(ColorFormatter)
    color_formatter.http_lexer = object()
    color_formatter.formatter = object()

    headers = 'HTTP/1.1 200 OK\r\nContent-Type: application/json'
    highlighted_headers = '\n  highlighted headers  \n'

    with patch.object(
        pygments,
        'highlight',
        return_value=highlighted_headers,
    ) as mock_highlight:
        result = color_formatter.format_headers(headers)

    assert result == 'highlighted headers'
    mock_highlight.assert_called_once_with(
        code=headers,
        lexer=color_formatter.http_lexer,
        formatter=color_formatter.formatter,
    )

# Generated at 2026-10-25 01:55:29.357250
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    color_formatter = ColorFormatter.__new__(ColorFormatter)
    color_formatter.formatter = sentinel.terminal_formatter

    body = '{"status": "ok"}'
    mime = 'application/json'
    highlighted_body = '\x1b[32m{"status": "ok"}\x1b[0m\n'

    with patch.object(
        color_formatter,
        'get_lexer_for_body',
        side_effect=[sentinel.lexer, None],
    ) as get_lexer, patch.object(
        pygments,
        'highlight',
        return_value=highlighted_body,
    ) as highlight:
        # A recognized body is highlighted.
        assert color_formatter.format_body(body, mime) == highlighted_body

        # A body without a matching lexer is returned unchanged.
        assert color_formatter.format_body(body, mime) == body

    assert get_lexer.call_args_list == [
        call(mime, body),
        call(mime, body),
    ]
    highlight.assert_called_once_with(
        code=body,
        lexer=sentinel.lexer,
        formatter=sentinel.terminal_formatter,
    )

# Generated at 2026-10-25 01:55:41.128881
# Unit test for function get_lexer
def test_get_lexer():json_lexer_class = pygments.lexers.get_lexer_by_name('json').__class__


# Generated at 2026-10-25 01:55:43.547277
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-25 01:55:52.800825
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():lexer = SimplifiedHTTPLexer()

# Generated at 2026-10-25 01:56:07.034850
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-25 01:56:17.172455
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-25 01:56:29.563947
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():from pygments.formatter import Formatter


# Generated at 2026-10-25 01:56:41.441849
# Unit test for function get_lexer
def test_get_lexer():json_lexer = module_0.get_lexer('application/json')

# Generated at 2026-10-25 01:56:43.862050
# Unit test for function get_lexer

# Generated at 2026-10-25 01:56:50.336481
# Unit test for function get_lexer
def test_get_lexer():lexer = module_0.get_lexer(
        mime='text/plain',
        explicit_json=True,
        body='{"success": true}',
    )

# Generated at 2026-10-25 01:56:59.669661
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from unittest.mock import patch, sentinel

    formatter = object.__new__(ColorFormatter)
    formatter.explicit_json = True

    with patch(
        f'{ColorFormatter.__module__}.get_lexer',
        return_value=sentinel.lexer,
    ) as mocked_get_lexer:
        result = formatter.get_lexer_for_body(
            mime='application/json',
            body='{"message": "ok"}',
        )

    assert result is sentinel.lexer
    mocked_get_lexer.assert_called_once_with(
        mime='application/json',
        explicit_json=True,
        body='{"message": "ok"}',
    )

# Generated at 2026-10-25 01:57:09.910205
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.formatter = Mock(name='formatter')

    body = '{"message": "ok"}'
    mime = 'application/json'
    lexer = Mock(name='lexer')

    # A recognized MIME type should highlight the body.
    formatter.get_lexer_for_body = Mock(return_value=lexer)

    with patch.object(
        pygments,
        'highlight',
        return_value='highlighted body',
    ) as highlight:
        result = formatter.format_body(body, mime)

    assert result == 'highlighted body'
    formatter.get_lexer_for_body.assert_called_once_with(mime, body)
    highlight.assert_called_once_with(
        code=body,
        lexer=lexer,
        formatter=formatter.formatter,
    )

    # An unrecognized MIME type should return the body unchanged.
    formatter.get_lexer_for_body.reset_mock(return_value=True)
    formatter.get_lexer_for_body.return_value = None

    with patch.object(pygments, 'highlight') as highlight:
        result = formatter.format_body(body, 'application/unknown')

    assert result == body
    formatter.get_lexer_for_body.assert_called_once_with(
        'application/unknown',
        body,
    )
    highlight.assert_not_called()

# Generated at 2026-10-25 01:57:18.818053
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.explicit_json = True

    with patch(
        f'{ColorFormatter.__module__}.get_lexer',
        return_value=sentinel.lexer,
    ) as mocked_get_lexer:
        result = formatter.get_lexer_for_body(
            mime='application/json',
            body='{"status": "ok"}',
        )

    assert result is sentinel.lexer
    mocked_get_lexer.assert_called_once_with(
        mime='application/json',
        explicit_json=True,
        body='{"status": "ok"}',
    )