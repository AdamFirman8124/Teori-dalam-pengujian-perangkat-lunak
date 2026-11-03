

# Generated at 2026-11-01 22:17:07.154743
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    assert lexer.name == 'HTTP'
    assert 'http' in lexer.aliases
    assert '*.http' in lexer.filenames
    assert 'root' in lexer.tokens

    # Should be able to tokenize a simple request/response without errors
    request_tokens = list(lexer.get_tokens('GET / HTTP/1.1'))
    assert ('Token.Name.Function', 'GET') in request_tokens

    response_tokens = list(lexer.get_tokens('HTTP/1.1 200 OK'))
    assert ('Token.Keyword.Reserved', 'HTTP') in response_tokens

# Generated at 2026-11-01 22:17:47.706024
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = mock.Mock(colors=256)
    color_formatter = ColorFormatter(env=env, color_scheme='solarized')
    headers = 'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n'
    result = color_formatter.format_headers(headers)
    assert isinstance(result, str)
    assert '200' in result
    assert 'application/json' in result
    assert not result.endswith('\n')  # output is stripped
    assert '\x1b[' in result  # ANSI color codes applied


def test_ColorFormatter_format_headers_auto_style():
    env = mock.Mock(colors=16)
    color_formatter = ColorFormatter(env=env, color_scheme='auto')
    headers = 'HTTP/1.1 404 Not Found\r\nServer: HTTPie\r\n'
    result = color_formatter.format_headers(headers)
    assert '404' in result
    assert 'Server' in result
    assert '\x1b[' in result


def test_ColorFormatter_format_headers_default_scheme_256():
    env = mock.Mock(colors=256)
    color_formatter = ColorFormatter(env=env)
    headers = 'HTTP/1.1 500 Internal Server Error\nX-Custom: value\n'
    result = color_formatter.format_headers(headers)
    assert '500' in result
    assert 'X-Custom' in result


def test_ColorFormatter_format_headers_disabled():
    env = mock.Mock(colors=0)
    color_formatter = ColorFormatter(env=env)
    assert color_formatter.enabled is False

# Generated at 2026-11-01 22:19:09.308049
# Unit test for constructor of class Solarized256Style
def test_Solarized256Style():
    style = Solarized256Style()

    # It should be a proper Pygments style instance
    assert isinstance(style, Solarized256Style)
    assert isinstance(style, pygments.style.Style)

    # Background color should be Solarized's dark base03
    assert style.background_color == Solarized256Style.BASE03
    assert style.background_color == '#1c1c1c'

    # Key token types should map to the expected Solarized colors
    styles = Solarized256Style.styles
    assert styles[pygments.token.Keyword] == Solarized256Style.GREEN
    assert styles[pygments.token.Keyword.Constant] == Solarized256Style.ORANGE
    assert styles[pygments.token.Keyword.Declaration] == Solarized256Style.BLUE
    assert styles[pygments.token.Keyword.Reserved] == Solarized256Style.BLUE
    assert styles[pygments.token.Keyword.Type] == Solarized256Style.RED
    assert styles[pygments.token.Name.Attribute] == Solarized256Style.BASE1
    assert styles[pygments.token.Name.Exception] == Solarized256Style.YELLOW
    assert styles[pygments.token.Name.Function] == Solarized256Style.BLUE
    assert styles[pygments.token.String] == Solarized256Style.CYAN
    assert styles[pygments.token.Number] == Solarized256Style.CYAN
    assert styles[pygments.token.Operator] == Solarized256Style.BASE1
    assert styles[pygments.token.Comment] == Solarized256Style.BASE01
    assert styles[pygments.token.Token] == Solarized256Style.BASE1

    # Generic text modifiers
    assert styles[pygments.token.Generic.Emph] == 'italic'
    assert styles[pygments.token.Generic.Strong] == 'bold'
    assert styles[pygments.token.Generic.Error] == Solarized256Style.RED

    # All palette constants should be well-formed 6-digit hex colors
    for color in (
        Solarized256Style.BASE03,
        Solarized256Style.BASE02,
        Solarized256Style.BASE01,
        Solarized256Style.BASE00,
        Solarized256Style.BASE0,
        Solarized256Style.BASE1,
        Solarized256Style.BASE2,
        Solarized256Style.BASE3,
        Solarized256Style.YELLOW,
        Solarized256Style.ORANGE,
        Solarized256Style.RED,
        Solarized256Style.MAGENTA,
        Solarized256Style.VIOLET,
        Solarized256Style.BLUE,
        Solarized256Style.CYAN,
        Solarized256Style.GREEN,
    ):
        assert color.startswith('#')
        assert len(color) == 7

# Generated at 2026-11-01 22:20:24.367869
# Unit test for constructor of class Solarized256Style
def test_Solarized256Style():
    style = Solarized256Style()
    assert isinstance(style, Solarized256Style)
    assert isinstance(style, pygments.style.Style)
    assert style.background_color == Solarized256Style.BASE03
    assert Solarized256Style.background_color == '#1c1c1c'
    assert Solarized256Style.BASE03 == '#1c1c1c'
    assert Solarized256Style.GREEN == '#5f8700'
    assert Solarized256Style.RED == '#af0000'
    assert Solarized256Style.BLUE == '#0087ff'
    assert Solarized256Style.CYAN == '#00afaf'
    assert pygments.token.Keyword in Solarized256Style.styles
    assert Solarized256Style.styles[pygments.token.Keyword] == Solarized256Style.GREEN
    assert Solarized256Style.styles[pygments.token.String] == Solarized256Style.CYAN
    assert Solarized256Style.styles[pygments.token.Number] == Solarized256Style.CYAN
    assert Solarized256Style.styles[pygments.token.Name.Exception] == Solarized256Style.YELLOW
    assert Solarized256Style.styles[pygments.token.Name.Function] == Solarized256Style.BLUE
    assert Solarized256Style.styles[pygments.token.Generic.Strong] == 'bold'
    assert Solarized256Style.styles[pygments.token.Generic.Emph] == 'italic'
    assert Solarized256Style.styles[pygments.token.Token] == Solarized256Style.BASE1

# Generated at 2026-11-01 22:21:41.282511
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # Styles bundled with Pygments resolve to the corresponding Pygments class
    for style_name in ('default', 'monokai', 'fruity'):
        assert ColorFormatter.get_style_class(style_name) is \
            pygments.styles.get_style_by_name(style_name)

    # 'solarized' is not a native Pygments style: verify that it is unknown
    # to Pygments and that the fallback Solarized256Style is used.
    try:
        pygments.styles.get_style_by_name(SOLARIZED_STYLE)
    except ClassNotFound:
        assert ColorFormatter.get_style_class(SOLARIZED_STYLE) is Solarized256Style
    else:
        assert ColorFormatter.get_style_class(SOLARIZED_STYLE) is \
            pygments.styles.get_style_by_name(SOLARIZED_STYLE)

    # Completely unknown styles fall back to Solarized256Style
    assert ColorFormatter.get_style_class('no-such-style-xyz') is Solarized256Style
    assert issubclass(ColorFormatter.get_style_class('no-such-style-xyz'),
                      pygments.style.Style)

# Generated at 2026-11-01 22:23:55.939152
# Unit test for method format_body of class ColorFormatter