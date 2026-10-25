

# Generated at 2026-10-24 06:21:52.106816
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    expected_style = pygments.styles.get_style_by_name('monokai')
    assert ColorFormatter.get_style_class('monokai') is expected_style

    # Unknown styles fall back to the bundled Solarized style.
    assert (
        ColorFormatter.get_style_class('nonexistent-style')
        is Solarized256Style
    )

# Generated at 2026-10-24 06:21:54.603887
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 06:21:57.110181
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 06:21:59.602654
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 06:22:02.019210
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 06:22:04.436599
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 06:22:20.053079
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():import re

# Generated at 2026-10-24 06:22:31.498603
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:22:42.465779
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():formatter = ColorFormatter.__new__(ColorFormatter)

# Generated at 2026-10-24 06:22:51.298331
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():formatter = ColorFormatter.__new__(ColorFormatter)

# Generated at 2026-10-24 06:22:53.715506
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 06:22:56.133169
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 06:22:58.548731
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 06:23:00.963100
# Unit test for function get_lexer

# Generated at 2026-10-24 06:23:03.376411
# Unit test for function get_lexer

# Generated at 2026-10-24 06:23:05.793506
# Unit test for function get_lexer

# Generated at 2026-10-24 06:23:08.206575
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 06:23:10.619784
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 06:23:13.040935
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 06:23:15.456163
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 06:23:26.385350
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():# No colors: plugin must be disabled
    formatter = ColorFormatter(Environment(colors=0))
    assert formatter.enabled is False

    # 256 colors + solarized: 256-color formatter and simplified HTTP lexer
    formatter = ColorFormatter(Environment(colors=256), color_scheme='solarized')
    assert formatter.enabled is True
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert isinstance(formatter.http_lexer, SimplifiedHTTPLexer)
    assert formatter.formatter.style is Solarized256Style

    # Unknown style name falls back to the bundled Solarized256Style
    formatter = ColorFormatter(Environment(colors=256), color_scheme='no-such-style')
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert formatter.formatter.style is Solarized256Style

    # Non-256 colors: plain terminal formatter and stock Pygments HTTP lexer
    formatter = ColorFormatter(Environment(colors=1), color_scheme='auto')
    assert isinstance(formatter.formatter, TerminalFormatter)
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)

    # explicit_json flag is stored for later use by format_body
    formatter = ColorFormatter(Environment(colors=256), explicit_json=True)
    assert formatter.explicit_json is True
    formatter = ColorFormatter(Environment(colors=256))
    assert formatter.explicit_json is False

# Generated at 2026-10-24 06:23:36.773883
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()

    assert isinstance(lexer, pygments.lexer.RegexLexer)
    assert lexer.name == 'HTTP'
    assert lexer.aliases == ['http']
    assert lexer.filenames == ['*.http']
    assert 'root' in lexer.tokens
    assert len(lexer.tokens['root']) == 3

# Generated at 2026-10-24 06:23:45.456323
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from unittest.mock import patch

    color_formatter = ColorFormatter.__new__(ColorFormatter)
    color_formatter.http_lexer = object()
    color_formatter.formatter = object()

    headers = 'Content-Type: application/json\r\nX-Test: value'
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

# Generated at 2026-10-24 06:24:12.183938
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 06:24:14.686319
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 06:24:17.099819
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 06:24:19.519383
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 06:24:25.096963
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = object.__new__(ColorFormatter)

# Generated at 2026-10-24 06:24:30.921628
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():formatter = ColorFormatter.__new__(ColorFormatter)

# Generated at 2026-10-24 06:24:47.812711
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.formatter = Mock()

    lexer = Mock(spec=Lexer)
    formatter.get_lexer_for_body = Mock(return_value=lexer)

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
        lexer=lexer,
        formatter=formatter.formatter,
    )

# Generated at 2026-10-24 06:24:57.546251
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from unittest.mock import Mock


def test_ColorFormatter_format_headers(monkeypatch):
    color_formatter = ColorFormatter.__new__(ColorFormatter)
    color_formatter.http_lexer = Mock()
    color_formatter.formatter = Mock()

    highlight = Mock(return_value="\n  highlighted headers  \n")
    monkeypatch.setattr(pygments, "highlight", highlight)

    headers = "Content-Type: application/json"
    result = color_formatter.format_headers(headers)

    assert result == "highlighted headers"
    highlight.assert_called_once_with(
        code=headers,
        lexer=color_formatter.http_lexer,
        formatter=color_formatter.formatter,
    )

# Generated at 2026-10-24 06:25:00.058635
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 06:25:02.472848
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 06:25:04.889049
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 06:25:07.304465
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:25:09.853312
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:25:12.266738
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:25:14.681834
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 06:25:17.096890
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 06:25:19.511503
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 06:25:21.925922
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:25:24.343318
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:25:26.757727
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:25:29.171526
# Unit test for function get_lexer

# Generated at 2026-10-24 06:25:35.232466
# Unit test for function get_lexer
def test_get_lexer():lexer = module_0.get_lexer(mime='application/json', body='{"key": "value"}')

# Generated at 2026-10-24 06:25:46.085532
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from unittest.mock import Mock, patch

    color_formatter = ColorFormatter.__new__(ColorFormatter)
    color_formatter.formatter = Mock(name='formatter')

    body = '{"message": "success"}'
    mime = 'application/json'
    lexer = Mock(name='lexer')
    highlighted_body = '\x1b[32m{"message": "success"}\x1b[0m'

    with patch.object(
        color_formatter,
        'get_lexer_for_body',
        return_value=lexer,
    ) as get_lexer, patch.object(
        pygments,
        'highlight',
        return_value=highlighted_body,
    ) as highlight:
        result = color_formatter.format_body(body, mime)

    assert result == highlighted_body
    get_lexer.assert_called_once_with(mime, body)
    highlight.assert_called_once_with(
        code=body,
        lexer=lexer,
        formatter=color_formatter.formatter,
    )

    # An unrecognized MIME type should leave the body unchanged.
    with patch.object(
        color_formatter,
        'get_lexer_for_body',
        return_value=None,
    ), patch.object(pygments, 'highlight') as highlight:
        result = color_formatter.format_body(body, 'unknown/unknown')

    assert result == body
    highlight.assert_not_called()

# Generated at 2026-10-24 06:25:57.129963
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    from unittest.mock import Mock, patch

    headers = 'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n'
    highlighted_headers = '\n  highlighted headers  \n'

    color_formatter = object.__new__(ColorFormatter)
    color_formatter.http_lexer = Mock(name='http_lexer')
    color_formatter.formatter = Mock(name='formatter')

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

# Generated at 2026-10-24 06:26:14.153964
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    from unittest.mock import patch

    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.formatter = terminal_formatter = object()

    body = '{"message": "success"}'
    mime = 'application/json'
    lexer = object()

    # A recognized MIME type is syntax-highlighted.
    with (
        patch.object(
            formatter,
            'get_lexer_for_body',
            return_value=lexer,
        ) as get_lexer,
        patch.object(
            pygments,
            'highlight',
            return_value='highlighted body',
        ) as highlight,
    ):
        result = formatter.format_body(body, mime)

    assert result == 'highlighted body'
    get_lexer.assert_called_once_with(mime, body)
    highlight.assert_called_once_with(
        code=body,
        lexer=lexer,
        formatter=terminal_formatter,
    )

    # An unrecognized MIME type leaves the body unchanged.
    with (
        patch.object(
            formatter,
            'get_lexer_for_body',
            return_value=None,
        ),
        patch.object(pygments, 'highlight') as highlight,
    ):
        result = formatter.format_body(body, 'application/unknown')

    assert result == body
    highlight.assert_not_called()

# Generated at 2026-10-24 06:26:16.718320
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:26:19.133131
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:26:21.699708
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:26:24.114156
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 06:26:26.529283
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 06:26:28.947192
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 06:26:31.364295
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 06:26:33.781728
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 06:26:36.194510
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 06:26:38.608860
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 06:26:41.024218
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 06:26:43.436994
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 06:26:45.851618
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 06:26:48.268528
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 06:26:50.682106
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 06:26:53.096883
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 06:26:55.516890
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 06:26:57.936836
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 06:27:00.351311
# Unit test for function get_lexer

# Generated at 2026-10-24 06:27:10.448726
# Unit test for function get_lexer
def test_get_lexer():lexer = module_0.get_lexer(
        mime='application/json',
        explicit_json=False,
        body='{"message": "ok"}',
    )

# Generated at 2026-10-24 06:27:20.292198
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()

    assert isinstance(lexer, pygments.lexer.RegexLexer)
    assert lexer.name == 'HTTP'
    assert lexer.aliases == ['http']
    assert lexer.filenames == ['*.http']
    assert 'root' in lexer.tokens
    assert len(lexer.tokens['root']) == 3

# Generated at 2026-10-24 06:27:31.864561
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    from unittest.mock import patch

    expected_style = pygments.style.Style

    # Returns the style resolved by Pygments.
    with patch.object(
        pygments.styles,
        'get_style_by_name',
        return_value=expected_style,
    ) as get_style_by_name:
        result = ColorFormatter.get_style_class('fruity')

    assert result is expected_style
    get_style_by_name.assert_called_once_with('fruity')

    # Falls back to the bundled Solarized style when resolution fails.
    with patch.object(
        pygments.styles,
        'get_style_by_name',
        side_effect=ClassNotFound('unknown style'),
    ):
        result = ColorFormatter.get_style_class('unknown-style')

    assert result is Solarized256Style

# Generated at 2026-10-24 06:27:47.478689
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    from unittest.mock import patch, sentinel

    with patch.object(
        pygments.styles,
        'get_style_by_name',
        return_value=sentinel.style_class,
    ) as get_style:
        result = ColorFormatter.get_style_class('monokai')

        assert result is sentinel.style_class
        get_style.assert_called_once_with('monokai')

    with patch.object(
        pygments.styles,
        'get_style_by_name',
        side_effect=ClassNotFound('unknown style'),
    ):
        result = ColorFormatter.get_style_class('unknown-style')

        assert result is Solarized256Style

# Generated at 2026-10-24 06:27:49.900335
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 06:27:52.463284
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 06:27:54.883276
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 06:27:57.298438
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 06:27:59.717499
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 06:28:02.132676
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 06:28:04.552386
# Unit test for function get_lexer

# Generated at 2026-10-24 06:28:11.391546
# Unit test for function get_lexer
def test_get_lexer():lexer = module_0.get_lexer(
        mime='text/plain',
        explicit_json=True,
        body='{"status": "ok"}',
    )

# Generated at 2026-10-24 06:28:38.488205
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 06:28:39.858579
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():# No colors: plugin must be disabled
    formatter = ColorFormatter(Environment(colors=0))
    assert formatter.enabled is False

    # 256 colors + solarized: 256-color formatter and simplified HTTP lexer
    formatter = ColorFormatter(Environment(colors=256), color_scheme='solarized')
    assert formatter.enabled is True
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert isinstance(formatter.http_lexer, SimplifiedHTTPLexer)
    assert formatter.formatter.style is Solarized256Style

    # Unknown style name falls back to the bundled Solarized256Style
    formatter = ColorFormatter(Environment(colors=256), color_scheme='no-such-style')
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert formatter.formatter.style is Solarized256Style

    # Non-256 colors: plain terminal formatter and stock Pygments HTTP lexer
    formatter = ColorFormatter(Environment(colors=1), color_scheme='auto')
    assert isinstance(formatter.formatter, TerminalFormatter)
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)

    # explicit_json flag is stored for later use by format_body
    formatter = ColorFormatter(Environment(colors=256), explicit_json=True)
    assert formatter.explicit_json is True
    formatter = ColorFormatter(Environment(colors=256))
    assert formatter.explicit_json is False

# Generated at 2026-10-24 06:28:42.388337
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:28:44.804646
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:28:47.222968
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:28:49.643548
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 06:28:52.064410
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 06:28:54.483269
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 06:28:56.897536
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 06:28:59.312179
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 06:29:01.727233
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 06:29:04.143094
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:29:06.557987
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:29:08.972673
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:29:11.389527
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:29:13.804508
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:29:16.218553
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:29:18.633620
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 06:29:43.551486
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 06:29:44.866948
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():import re

# Generated at 2026-10-24 06:29:54.721501
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():import sys
from unittest.mock import Mock


def test_ColorFormatter_get_lexer_for_body(monkeypatch):
    expected_lexer = Mock(spec=Lexer)
    mocked_get_lexer = Mock(return_value=expected_lexer)

    monkeypatch.setattr(
        sys.modules[ColorFormatter.__module__],
        'get_lexer',
        mocked_get_lexer,
    )

    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.explicit_json = True

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

# Generated at 2026-10-24 06:30:05.157275
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    from unittest.mock import patch

    class TestStyle(pygments.style.Style):
        styles = {}

    with patch.object(
        pygments.styles,
        'get_style_by_name',
        return_value=TestStyle,
    ) as get_style:
        assert ColorFormatter.get_style_class('known-style') is TestStyle
        get_style.assert_called_once_with('known-style')

    with patch.object(
        pygments.styles,
        'get_style_by_name',
        side_effect=ClassNotFound('Unknown style'),
    ) as get_style:
        assert (
            ColorFormatter.get_style_class('unknown-style')
            is Solarized256Style
        )
        get_style.assert_called_once_with('unknown-style')

# Generated at 2026-10-24 06:30:07.575721
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 06:30:09.990277
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 06:30:12.421378
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 06:30:14.826212
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 06:30:17.240213
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 06:30:19.655074
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 06:30:22.069155
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 06:30:24.487779
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 06:30:28.709078
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():result = ColorFormatter.get_style_class("nonexistent-color-scheme")

# Generated at 2026-10-24 06:30:36.292783
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from unittest.mock import Mock


def test_ColorFormatter_format_headers(monkeypatch):
    formatter = ColorFormatter.__new__(ColorFormatter)
    formatter.http_lexer = Mock(name='http_lexer')
    formatter.formatter = Mock(name='formatter')

    highlight = Mock(return_value='\nformatted headers\n')
    monkeypatch.setattr(pygments, 'highlight', highlight)

    headers = 'Content-Type: application/json\r\n'

    result = formatter.format_headers(headers)

    assert result == 'formatted headers'
    highlight.assert_called_once_with(
        code=headers,
        lexer=formatter.http_lexer,
        formatter=formatter.formatter,
    )

# Generated at 2026-10-24 06:30:55.166733
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    # Coloring disabled.
    formatter = ColorFormatter(
        env=SimpleNamespace(colors=0),
        explicit_json=True,
    )
    assert formatter.enabled is False
    assert not hasattr(formatter, 'formatter')
    assert not hasattr(formatter, 'http_lexer')

    # Automatic style uses the standard terminal formatter, even with
    # 256-color support.
    formatter = ColorFormatter(
        env=SimpleNamespace(colors=256),
        explicit_json=True,
        color_scheme=AUTO_STYLE,
    )
    assert formatter.explicit_json is True
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)
    assert type(formatter.formatter) is TerminalFormatter

    # A selected style with 256-color support uses the custom HTTP lexer
    # and the 256-color formatter.
    formatter = ColorFormatter(
        env=SimpleNamespace(colors=256),
        explicit_json=False,
        color_scheme=SOLARIZED_STYLE,
    )
    assert formatter.explicit_json is False
    assert isinstance(formatter.http_lexer, SimplifiedHTTPLexer)
    assert isinstance(formatter.formatter, Terminal256Formatter)

    # Terminals without 256-color support always use TerminalFormatter.
    formatter = ColorFormatter(
        env=SimpleNamespace(colors=16),
        color_scheme=SOLARIZED_STYLE,
    )
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)
    assert type(formatter.formatter) is TerminalFormatter

# Generated at 2026-10-24 06:31:07.120179
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 06:31:09.637669
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 06:31:12.145322
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 06:31:14.558294
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:31:16.975925
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:31:19.394740
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:31:21.806419
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:31:24.221038
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:31:26.643870
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 06:31:29.061285
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 06:31:31.474353
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 06:31:33.888458
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 06:31:44.794227
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():expected_style = pygments.styles.get_style_by_name('fruity')

# Generated at 2026-10-24 06:32:00.800869
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    formatter = object.__new__(ColorFormatter)
    formatter.explicit_json = True

    mime = 'application/json'
    body = '{"status": "ok"}'

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