

# Generated at 2026-11-01 19:32:06.000999
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from unittest.mock import Mock
    from httpie.context import Environment
    from httpie.plugins import FormatterPlugin

# Generated at 2026-11-01 19:32:42.967244
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # A valid built-in Pygments style name returns the matching style class.
    assert ColorFormatter.get_style_class('default') \
        is pygments.styles.get_style_by_name('default')
    assert ColorFormatter.get_style_class('monokai') \
        is pygments.styles.get_style_by_name('monokai')

    # An unknown style name falls back to the bundled Solarized256Style.
    assert ColorFormatter.get_style_class('nonexistent-style') \
        is Solarized256Style

# Generated at 2026-11-01 19:34:37.097377
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():
    # 256-color environment, Solarized scheme
    env = Environment(colors=256)
    formatter = ColorFormatter(env=env, explicit_json=False, color_scheme='solarized')

    # A recognized JSON body gets syntax highlighted
    json_body = '{"name": "john", "age": 30}'
    result = formatter.format_body(json_body, 'application/json')
    assert result != json_body
    assert '\x1b[' in result
    assert '"name"' in result

    # XML is also recognized and highlighted
    xml_body = '<note><to>Tove</to></note>'
    result_xml = formatter.format_body(xml_body, 'application/xml')
    assert result_xml != xml_body
    assert '<note>' in result_xml

    # An unrecognized mime type leaves the body untouched
    plain_body = 'just some plain text'
    assert formatter.format_body(plain_body, 'text/x-not-a-real-thing') == plain_body

    # Explicit JSON: valid JSON body with wrong content type is still highlighted
    json_formatter = ColorFormatter(env=env, explicit_json=True, color_scheme='solarized')
    result = json_formatter.format_body('{"a": 1}', 'text/x-not-a-real-thing')
    assert result != '{"a": 1}'
    assert '\x1b[' in result

    # Explicit JSON: invalid JSON body with wrong content type is left untouched
    bad_body = '{oops'
    assert json_formatter.format_body(bad_body, 'text/x-not-a-real-thing') == bad_body

    # Non-256-color environment falls back to the plain terminal formatter
    term_formatter = ColorFormatter(env=Environment(colors=8), color_scheme=AUTO_STYLE)
    result = term_formatter.format_body('{"key": "value"}', 'application/json')
    assert result != '{"key": "value"}'
    assert '\x1b[' in result

# Generated at 2026-11-01 19:36:03.364554
# Unit test for constructor of class Solarized256Style
def test_Solarized256Style():
    style = Solarized256Style()
    assert style.background_color == '#1c1c1c'
    expected_colors = {
        pygments.token.Keyword: '#5f8700',
        pygments.token.Keyword.Constant: '#d75f00',
        pygments.token.Keyword.Declaration: '#0087ff',
        pygments.token.Keyword.Namespace: '#d75f00',
        pygments.token.Keyword.Reserved: '#0087ff',
        pygments.token.Keyword.Type: '#af0000',
        pygments.token.Name.Attribute: '#8a8a8a',
        pygments.token.Name.Builtin: '#0087ff',
        pygments.token.Name.Class: '#0087ff',
        pygments.token.Name.Constant: '#d75f00',
        pygments.token.Name.Exception: '#af8700',
        pygments.token.Name.Function: '#0087ff',
        pygments.token.Name.Tag: '#0087ff',
        pygments.token.Name.Variable: '#0087ff',
        pygments.token.String: '#00afaf',
        pygments.token.String.Escape: '#af0000',
        pygments.token.Number: '#00afaf',
        pygments.token.Operator: '#8a8a8a',
        pygments.token.Operator.Word: '#5f8700',
        pygments.token.Comment: '#4e4e4e',
        pygments.token.Comment.Preproc: '#5f8700',
        pygments.token.Generic.Deleted: '#00afaf',
        pygments.token.Generic.Error: '#af0000',
        pygments.token.Generic.Heading: '#d75f00',
        pygments.token.Generic.Inserted: '#5f8700',
        pygments.token.Generic.Subheading: '#d75f00',
        pygments.token.Token: '#8a8a8a',
        pygments.token.Token.Other: '#d75f00',
    }
    for token, color in expected_colors.items():
        assert token in style.styles
        assert style.styles[token] == color
    # Special (non-color) style values
    assert style.styles[pygments.token.Generic.Emph] == 'italic'
    assert style.styles[pygments.token.Generic.Strong] == 'bold'
    # The style should be usable by Pygments for actual highlighting.
    highlighted = pygments.highlight(
        code='{"key": "value"}',
        lexer=pygments.lexers.get_lexer_by_name('json'),
        formatter=Terminal256Formatter(style=Solarized256Style),
    )
    assert highlighted

# Generated at 2026-11-01 19:36:44.670186
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    env = Environment(colors=256)

    # Default formatter (no --json flag)
    formatter = ColorFormatter(env=env)

    # Well-known mime type resolves through the mimetype table
    lexer = formatter.get_lexer_for_body('application/json', '{"foo": ["bar", 42]}')
    assert lexer is not None
    assert isinstance(lexer, pygments.lexers.JsonLexer)

    lexer = formatter.get_lexer_for_body('text/html', '<html><body>hello</body></html>')
    assert isinstance(lexer, pygments.lexers.HtmlLexer)

    # Structured syntax suffix (+json) falls back to the JSON lexer
    lexer = formatter.get_lexer_for_body(
        'application/vnd.error+json', '{"message": "oops"}'
    )
    assert isinstance(lexer, pygments.lexers.JsonLexer)

    # Completely unknown mime type with unrecognizable body -> no lexer
    assert formatter.get_lexer_for_body('foo/bar', 'nothing to see here') is None

    # Formatter with explicit --json flag
    json_formatter = ColorFormatter(env=env, explicit_json=True)

    # Valid JSON body served with a bogus content type -> JSON lexer
    lexer = json_formatter.get_lexer_for_body('foo/bar', '{"valid": true}')
    assert isinstance(lexer, pygments.lexers.JsonLexer)

    # Invalid JSON body with a bogus content type -> still no lexer
    assert json_formatter.get_lexer_for_body('foo/bar', 'not json at all {') is None

    # Already-correct JSON content type is untouched even with --json
    lexer = json_formatter.get_lexer_for_body('application/json', '{"a": 1}')
    assert isinstance(lexer, pygments.lexers.JsonLexer)

    # Empty body never triggers the explicit-json fallback
    assert json_formatter.get_lexer_for_body('foo/bar', '') is None

# Generated at 2026-11-01 19:38:09.864097
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from httpie.context import Environment

    # Colors disabled -> processor disabled, early return
    env = Environment(colors=0)
    formatter = ColorFormatter(env=env)
    assert formatter.enabled is False

    # Auto style always uses the Pygments HTTP lexer + terminal formatter
    env = Environment(colors=256)
    formatter = ColorFormatter(env=env, color_scheme=AUTO_STYLE, explicit_json=True)
    assert formatter.enabled is True
    assert formatter.explicit_json is True
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)
    assert isinstance(formatter.formatter, TerminalFormatter)

    # Fewer than 256 colors -> same as auto style
    env = Environment(colors=1)
    formatter = ColorFormatter(env=env, color_scheme=SOLARIZED_STYLE)
    assert formatter.enabled is True
    assert isinstance(formatter.http_lexer, PygmentsHttpLexer)
    assert isinstance(formatter.formatter, TerminalFormatter)

    # 256 colors + supported style -> simplified HTTP lexer + 256 formatter
    env = Environment(colors=256)
    formatter = ColorFormatter(env=env, color_scheme=SOLARIZED_STYLE)
    assert isinstance(formatter.http_lexer, SimplifiedHTTPLexer)
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert formatter.formatter.style is Solarized256Style

    # 256 colors + known pygments style -> resolved via pygments
    env = Environment(colors=256)
    formatter = ColorFormatter(env=env, color_scheme='monokai')
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert formatter.formatter.style is pygments.styles.get_style_by_name('monokai')

    # 256 colors + unknown style -> falls back to Solarized256Style
    env = Environment(colors=256)
    formatter = ColorFormatter(env=env, color_scheme='no-such-style')
    assert isinstance(formatter.formatter, Terminal256Formatter)
    assert formatter.formatter.style is Solarized256Style

    # explicit_json defaults to False
    env = Environment(colors=256)
    formatter = ColorFormatter(env=env)
    assert formatter.explicit_json is False

# Generated at 2026-11-01 19:39:50.489345
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():
    from unittest.mock import Mock

    # Colors disabled in the environment -> plugin disabled, early return
    env = Mock(colors=False)
    color_formatter = ColorFormatter(env)
    assert color_formatter.enabled is False
    assert not hasattr(color_formatter, 'formatter')
    assert not hasattr(color_formatter, 'http_lexer')

    # Auto style -> pygments HTTP lexer + plain terminal formatter
    env = Mock(colors=256)
    color_formatter = ColorFormatter(env, color_scheme=AUTO_STYLE)
    assert color_formatter.enabled is True
    assert color_formatter.explicit_json is False
    assert isinstance(color_formatter.http_lexer, PygmentsHttpLexer)
    assert isinstance(color_formatter.formatter, TerminalFormatter)

    # explicit_json flag is stored on the instance
    env = Mock(colors=256)
    color_formatter = ColorFormatter(env, explicit_json=True, color_scheme=AUTO_STYLE)
    assert color_formatter.explicit_json is True

    # 256 colors with a known non-auto style -> simplified lexer + 256 formatter
    env = Mock(colors=256)
    color_formatter = ColorFormatter(env, color_scheme='monokai')
    assert isinstance(color_formatter.http_lexer, SimplifiedHTTPLexer)
    assert isinstance(color_formatter.formatter, Terminal256Formatter)

    # Unknown style with 256 colors falls back to Solarized256Style
    env = Mock(colors=256)
    color_formatter = ColorFormatter(env, color_scheme='no-such-style')
    assert isinstance(color_formatter.http_lexer, SimplifiedHTTPLexer)
    assert isinstance(color_formatter.formatter, Terminal256Formatter)
    assert ColorFormatter.get_style_class('no-such-style') is Solarized256Style

    # Fewer than 256 colors -> plain terminal formatter even for non-auto styles
    env = Mock(colors=8)
    color_formatter = ColorFormatter(env, color_scheme='monokai')
    assert isinstance(color_formatter.http_lexer, PygmentsHttpLexer)
    assert isinstance(color_formatter.formatter, TerminalFormatter)

# Generated at 2026-11-01 19:40:20.804737
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    env = Environment(colors=256)

    # Without --json: mime types are resolved normally
    formatter = ColorFormatter(env=env, explicit_json=False)

    # Recognized mime type -> corresponding lexer
    lexer = formatter.get_lexer_for_body('application/json', '{"foo": "bar"}')
    assert isinstance(lexer, pygments.lexers.JsonLexer)

    lexer = formatter.get_lexer_for_body('text/html', '<html><body>hi</body></html>')
    assert isinstance(lexer, pygments.lexers.HtmlLexer)

    # Structured syntax suffix (+json) falls back to the JSON lexer
    lexer = formatter.get_lexer_for_body('application/vnd.api+json', '{"foo": "bar"}')
    assert isinstance(lexer, pygments.lexers.JsonLexer)

    # Unrecognized mime type -> no lexer
    assert formatter.get_lexer_for_body('unknown/type', 'blah') is None

    # With --json: valid JSON body with a wrong/unknown content type
    # still gets highlighted as JSON
    formatter = ColorFormatter(env=env, explicit_json=True)
    lexer = formatter.get_lexer_for_body('text/plain', '{"foo": "bar"}')
    assert isinstance(lexer, pygments.lexers.JsonLexer)

    # With --json: non-JSON body with an unrecognized content type
    # yields no lexer
    assert formatter.get_lexer_for_body('unknown/type', 'this is not json {') is None