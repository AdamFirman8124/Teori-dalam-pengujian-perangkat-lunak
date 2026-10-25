

# Generated at 2026-10-24 10:33:45.715643
# Unit test for constructor of class Solarized256Style
def test_Solarized256Style():
    style = Solarized256Style()

    assert isinstance(style, pygments.style.Style)

    # class constants
    assert Solarized256Style.BASE03 == "#1c1c1c"
    assert Solarized256Style.BASE02 == "#262626"
    assert Solarized256Style.BASE01 == "#4e4e4e"
    assert Solarized256Style.GREEN == "#5f8700"
    assert Solarized256Style.CYAN == "#00afaf"
    assert Solarized256Style.BLUE == "#0087ff"

    # constructor initializes background from BASE03
    assert Solarized256Style.background_color == Solarized256Style.BASE03
    assert style.background_color == "#1c1c1c"

    # style mapping is preserved
    assert Solarized256Style.styles[pygments.token.Keyword] == Solarized256Style.GREEN
    assert Solarized256Style.styles[pygments.token.String] == Solarized256Style.CYAN
    assert Solarized256Style.styles[pygments.token.Number] == Solarized256Style.CYAN
    assert Solarized256Style.styles[pygments.token.Name.Attribute] == Solarized256Style.BASE1
    assert Solarized256Style.styles[pygments.token.Name.Exception] == Solarized256Style.YELLOW
    assert Solarized256Style.styles[pygments.token.Operator] == Solarized256Style.BASE1

# Generated at 2026-10-24 10:34:37.642734
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:34:52.171956
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from httpie.context import Environment


# Generated at 2026-10-24 10:34:55.037814
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:34:56.358710
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from httpie.context import Environment


# Generated at 2026-10-24 10:35:16.832925
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:35:19.253411
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:35:21.871814
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:35:24.288282
# Unit test for function get_lexer

# Generated at 2026-10-24 10:35:26.722291
# Unit test for function get_lexer

# Generated at 2026-10-24 10:35:29.356852
# Unit test for function get_lexer

# Generated at 2026-10-24 10:35:31.771893
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:35:34.455220
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:35:36.876537
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:35:39.296174
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 10:35:41.715791
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 10:35:44.132488
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 10:35:46.562381
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:35:48.983021
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:36:22.591425
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():from httpie.context import Environment

# Generated at 2026-10-24 10:36:51.676225
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:36:54.625124
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():from httpie.context import Environment

# Generated at 2026-10-24 10:37:30.380953
# Unit test for function get_lexer
def test_get_lexer():
    import pygments.lexers
    from pygments.lexers.special import TextLexer

    lexer = module_0.get_lexer("application/json")
    assert type(lexer).__name__ == "JsonLexer"

    lexer = module_0.get_lexer("text/html")
    assert type(lexer).__name__ == "HtmlLexer"

    lexer = module_0.get_lexer("application/xml")
    assert type(lexer).__name__ == "XmlLexer"

    lexer = module_0.get_lexer("text/css")
    assert type(lexer).__name__ == "CssLexer"

    lexer = module_0.get_lexer("text/x-python")
    assert type(lexer).__name__ == "PythonLexer"

    lexer = module_0.get_lexer("text/plain")
    assert isinstance(lexer, TextLexer)

    lexer = module_0.get_lexer("application/vnd.example+json")
    assert type(lexer).__name__ == "JsonLexer"

    lexer = module_0.get_lexer("application/foo+json")
    assert type(lexer).__name__ == "JsonLexer"

    lexer = module_0.get_lexer("application/x-unknown-xyz")
    assert lexer is None

    lexer = module_0.get_lexer("image/png")
    assert lexer is None

    lexer = module_0.get_lexer("text/plain", explicit_json=True, body='{"a": 1}')
    assert type(lexer).__name__ == "JsonLexer"

    lexer = module_0.get_lexer("text/plain", explicit_json=True, body="[1, 2, 3]")
    assert type(lexer).__name__ == "JsonLexer"

    lexer = module_0.get_lexer("text/plain", explicit_json=True, body="not json")
    assert isinstance(lexer, TextLexer)

    lexer = module_0.get_lexer("text/plain", explicit_json=True, body="")
    assert isinstance(lexer, TextLexer)

    lexer = module_0.get_lexer("text/plain", explicit_json=False, body='{"a": 1}')
    assert isinstance(lexer, TextLexer)

    lexer = module_0.get_lexer("application/json", explicit_json=False, body="not json")
    assert type(lexer).__name__ == "JsonLexer"

# Generated at 2026-10-24 10:38:18.326067
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 10:38:49.625341
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():env = type('E', (), {'colors': 256})()

# Generated at 2026-10-24 10:38:52.136553
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 10:38:54.556763
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 10:38:56.980190
# Unit test for constructor of class SimplifiedHTTPLexer

# Generated at 2026-10-24 10:38:59.402432
# Unit test for function get_lexer

# Generated at 2026-10-24 10:39:31.854169
# Unit test for function get_lexer

# Generated at 2026-10-24 10:39:47.296734
# Unit test for function get_lexer
def test_get_lexer():from pygments.lexers.data import JsonLexer

# Generated at 2026-10-24 10:40:09.204571
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    assert lexer.name == 'HTTP'
    assert lexer.aliases == ['http']
    assert lexer.filenames == ['*.http']

    # Constructor must accept the standard Pygments lexer options.
    lexer = SimplifiedHTTPLexer(stripnl=False, ensurenl=False, tabsize=2)
    assert lexer.stripnl is False
    assert lexer.ensurenl is False
    assert lexer.tabsize == 2

    # Sanity check: the lexer is usable and emits the expected header token.
    tokens = list(lexer.get_tokens('Content-Type: application/json'))
    assert tokens[0][0] is pygments.token.Name.Attribute

# Generated at 2026-10-24 10:40:29.888942
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:41:05.208603
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:41:28.154118
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from httpie.context import Environment


# Generated at 2026-10-24 10:41:29.898271
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:41:32.639807
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():from httpie.context import Environment

# Generated at 2026-10-24 10:41:51.001448
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:41:53.419450
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:41:55.836513
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:41:58.256956
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:42:00.676385
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:42:03.097120
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:42:05.518368
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:42:08.396857
# Unit test for method format_body of class ColorFormatter
def test_ColorFormatter_format_body():from httpie.context import Environment

# Generated at 2026-10-24 10:42:41.986125
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 10:42:53.117855
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():assert ColorFormatter.get_style_class("default").__name__ == "DefaultStyle"

# Generated at 2026-10-24 10:42:55.687066
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:42:58.212227
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:43:00.637207
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 10:43:03.058186
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:43:05.491370
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:43:07.922715
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 10:43:15.066952
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()
    assert lexer is not None
    assert lexer.name == 'HTTP'
    assert 'http' in lexer.aliases
    assert '*.http' in lexer.filenames
    assert isinstance(lexer, pygments.lexer.RegexLexer)
    assert 'root' in lexer.tokens
    assert len(lexer.tokens['root']) == 3

# Generated at 2026-10-24 10:43:17.931042
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 10:43:34.297802
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():from httpie.context import Environment
