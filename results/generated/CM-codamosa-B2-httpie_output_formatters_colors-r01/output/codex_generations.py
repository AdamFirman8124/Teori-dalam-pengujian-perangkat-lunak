

# Generated at 2026-11-02 00:27:57.335170
# Unit test for constructor of class Solarized256Style
def test_Solarized256Style():
    style = Solarized256Style()

    # Constructor should work without arguments
    assert style is not None

    # Check inherited style metadata
    assert Solarized256Style.background_color == '#1c1c1c'
    assert Solarized256Style.BASE03 == '#1c1c1c'
    assert Solarized256Style.GREEN == '#5f8700'
    assert Solarized256Style.BLUE == '#0087ff'

    # Style mapping should contain expected token entries
    assert pygments.token.Keyword in Solarized256Style.styles
    assert Solarized256Style.styles[pygments.token.Keyword] == '#5f8700'
    assert Solarized256Style.styles[pygments.token.String] == '#00afaf'
    assert Solarized256Style.styles[pygments.token.Number] == '#00afaf'
    assert Solarized256Style.styles[pygments.token.Comment] == '#4e4e4e'
    assert Solarized256Style.styles[pygments.token.Token] == '#8a8a8a'

    # Generic styling values
    assert Solarized256Style.styles[pygments.token.Generic.Emph] == 'italic'
    assert Solarized256Style.styles[pygments.token.Generic.Strong] == 'bold'

    # Should be usable through Pygments' style lookup mechanism
    assert issubclass(Solarized256Style, pygments.style.Style)
    assert pygments.styles.STYLE_MAP is not None

# Generated at 2026-11-02 00:29:10.733013
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-11-02 00:30:25.808484
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-11-02 00:31:47.209592
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-11-02 00:32:14.794980
# Unit test for constructor of class Solarized256Style
def test_Solarized256Style():
    style = Solarized256Style()
    assert isinstance(style, pygments.style.Style)
    assert style.background_color == "#1c1c1c"
    assert style.styles[pygments.token.Keyword] == "#5f8700"
    assert style.styles[pygments.token.Keyword.Constant] == "#d75f00"
    assert style.styles[pygments.token.Keyword.Reserved] == "#0087ff"
    assert style.styles[pygments.token.Name.Attribute] == "#8a8a8a"
    assert style.styles[pygments.token.Name.Exception] == "#af8700"
    assert style.styles[pygments.token.Name.Function] == "#0087ff"
    assert style.styles[pygments.token.String] == "#00afaf"
    assert style.styles[pygments.token.Number] == "#00afaf"
    assert style.styles[pygments.token.Operator] == "#8a8a8a"
    assert style.styles[pygments.token.Comment] == "#4e4e4e"
    assert style.styles[pygments.token.Generic.Strong] == 'bold'
    assert style.styles[pygments.token.Generic.Emph] == 'italic'
    assert style.styles[pygments.token.Token] == "#8a8a8a"
    assert style.styles[pygments.token.Token.Other] == "#d75f00"
    # style_for_token resolves inherited/split tokens too
    assert style.style_for_token(pygments.token.Keyword)['color'] == '#5f8700'
    assert style.style_for_token(pygments.token.Name.Function)['color'] == '#0087ff'
    assert style.style_for_token(pygments.token.Generic.Strong)['bold'] is True

# Generated at 2026-11-02 00:32:40.758338
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    env = Mock(colors=256)
    color_formatter = ColorFormatter(env=env, color_scheme=SOLARIZED_STYLE)
    headers = 'HTTP/1.1 200 OK\nContent-Type: application/json'

    with patch.object(pygments, 'highlight', return_value='colored headers\n') as highlight_mock:
        result = color_formatter.format_headers(headers)

    highlight_mock.assert_called_once_with(
        code=headers,
        lexer=color_formatter.http_lexer,
        formatter=color_formatter.formatter,
    )
    # Trailing newline added by pygments must be stripped
    assert result == 'colored headers'

# Generated at 2026-11-02 00:33:46.101191
# Unit test for function get_lexer

# Generated at 2026-11-02 00:34:16.104061
# Unit test for function get_lexer
def test_get_lexer():from pygments.lexers.data import JsonLexer

# Generated at 2026-11-02 00:34:32.009112
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():
    # Test with 256 colors -> uses SimplifiedHTTPLexer + Terminal256Formatter
    env = Environment(colors=256)
    formatter = ColorFormatter(env=env, color_scheme=SOLARIZED_STYLE)
    headers = 'HTTP/1.1 200 OK\r\nContent-Type: application/json\r\n\r\n'
    result = formatter.format_headers(headers)
    assert 'Content-Type' in result
    assert 'application/json' in result
    assert '\x1b[' in result  # ANSI escape sequences present

    # Test with non-256 colors -> uses PygmentsHttpLexer + TerminalFormatter
    env = Environment(colors=True)
    formatter = ColorFormatter(env=env)
    headers = 'HTTP/1.1 404 Not Found\r\nServer: nginx\r\n\r\n'
    result = formatter.format_headers(headers)
    assert 'Server' in result
    assert 'nginx' in result

    # Result should be stripped of surrounding whitespace
    assert result == result.strip()

# Generated at 2026-11-02 00:36:00.938963
# Unit test for method format_body of class ColorFormatter