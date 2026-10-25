

# Generated at 2026-10-24 12:44:19.460452
# Unit test for constructor of class Solarized256Style
def test_Solarized256Style():
    style = Solarized256Style()

    # Constructor returns an instance of the style class
    assert isinstance(style, Solarized256Style)
    assert isinstance(style, pygments.style.Style)

    # Core style attributes are set
    assert style.background_color == Solarized256Style.BASE03
    assert isinstance(style.styles, dict)
    assert len(style.styles) > 0

    # Every mapped token resolves to a non-empty style string
    for token, value in style.styles.items():
        assert isinstance(token, pygments.token._Token)
        assert isinstance(value, str)
        assert value.strip() != ''

    # A few spot checks against the palette
    assert style.styles[pygments.token.Keyword] == Solarized256Style.GREEN
    assert style.styles[pygments.token.String] == Solarized256Style.CYAN
    assert style.styles[pygments.token.Name.Exception] == Solarized256Style.YELLOW


def test_Solarized256Style_via_pygments():
    # Pygments can look it up and instantiate it by class
    from pygments.formatters.terminal256 import Terminal256Formatter
    formatter = Terminal256Formatter(style=Solarized256Style)
    assert formatter.style is not None

    # It also round-trips through highlight() without error
    out = pygments.highlight('{"a": 1}',
                             pygments.lexers.get_lexer_by_name('json'),
                             formatter)
    assert out  # non-empty, contains ANSI escapes
    assert '\x1b[' in out


def test_get_style_class_fallback():
    # Known style resolves via pygments; unknown name falls back to Solarized256
    assert ColorFormatter.get_style_class('monokai') is not None
    assert ColorFormatter.get_style_class('no-such-style') is Solarized256Style
    assert ColorFormatter.get_style_class('solarized') is Solarized256Style

# Generated at 2026-10-24 12:44:37.256840
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 12:44:39.670992
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 12:44:42.087353
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 12:44:44.504340
# Unit test for constructor of class Solarized256Style

# Generated at 2026-10-24 12:44:46.922468
# Unit test for constructor of class Solarized256Style

# Generated at 2026-10-24 12:44:49.338248
# Unit test for constructor of class Solarized256Style

# Generated at 2026-10-24 12:44:51.757059
# Unit test for function get_lexer

# Generated at 2026-10-24 12:44:54.178072
# Unit test for function get_lexer

# Generated at 2026-10-24 12:44:56.592457
# Unit test for function get_lexer

# Generated at 2026-10-24 12:44:59.007877
# Unit test for constructor of class Solarized256Style

# Generated at 2026-10-24 12:45:01.423697
# Unit test for constructor of class Solarized256Style

# Generated at 2026-10-24 12:45:03.839479
# Unit test for constructor of class Solarized256Style

# Generated at 2026-10-24 12:45:06.256606
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 12:45:08.673466
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 12:45:10.051061
# Unit test for constructor of class ColorFormatter
def test_ColorFormatter():from httpie.context import Environment


# Generated at 2026-10-24 12:45:26.881908
# Unit test for method get_lexer_for_body of class ColorFormatter
def test_ColorFormatter_get_lexer_for_body():
    from unittest.mock import Mock
    from httpie.context import Environment

    env = Mock(colors=True, **{'colors': 256})
    formatter = ColorFormatter(env=env, explicit_json=False, color_scheme='solarized')

    # JSON body via correct Content-Type
    lexer = formatter.get_lexer_for_body('application/json', '{"a": 1}')
    assert lexer is not None
    assert lexer.aliases and 'json' in lexer.aliases

    # JSON body via vendor subtype with +json suffix: application/vnd.api+json
    lexer = formatter.get_lexer_for_body('application/vnd.api+json', '{"a": 1}')
    assert lexer is not None
    assert lexer.aliases and 'json' in lexer.aliases

    # Non-JSON body with unknown mime type -> no lexer
    lexer = formatter.get_lexer_for_body('application/octet-stream', '\x00\x01')
    assert lexer is None

    # Plain text falls back to TextLexer
    lexer = formatter.get_lexer_for_body('text/plain', 'hello')
    assert lexer is not None
    assert issubclass(lexer, TextLexer)

    # explicit_json=True overrides a wrong Content-Type when body parses as JSON
    formatter_json = ColorFormatter(env=env, explicit_json=True, color_scheme='solarized')
    lexer = formatter_json.get_lexer_for_body('text/plain', '{"a": 1}')
    assert lexer is not None
    assert lexer.aliases and 'json' in lexer.aliases

    # explicit_json=True but body is NOT valid JSON -> stays non-JSON lexer
    lexer = formatter_json.get_lexer_for_body('text/plain', 'just text')
    assert lexer is not None
    assert issubclass(lexer, TextLexer)

# Generated at 2026-10-24 12:45:47.012037
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    # A valid Pygments style should be returned normally.
    expected_style = pygments.styles.get_style_by_name('fruity')
    assert ColorFormatter.get_style_class('fruity') is expected_style

    # An unknown style should fall back to the bundled Solarized style.
    assert (
        ColorFormatter.get_style_class('nonexistent-style')
        is Solarized256Style
    )

# Generated at 2026-10-24 12:45:49.867038
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

# Generated at 2026-10-24 12:45:52.629532
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

# Generated at 2026-10-24 12:45:55.508987
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 12:46:22.440583
# Unit test for method format_headers of class ColorFormatter
def test_ColorFormatter_format_headers():formatter = ColorFormatter.__new__(ColorFormatter)

# Generated at 2026-10-24 12:47:17.122614
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 12:47:56.239886
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 12:48:57.884682
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 12:49:49.158865
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 12:49:50.539517
# Unit test for constructor of class SimplifiedHTTPLexer
def test_SimplifiedHTTPLexer():
    lexer = SimplifiedHTTPLexer()

    # Inherits Pygments constructor
    assert isinstance(lexer, pygments.lexer.RegexLexer)
    assert isinstance(lexer, Lexer)

    # Class configuration is preserved by constructor
    assert lexer.name == 'HTTP'
    assert 'http' in lexer.aliases
    assert '*.http' in lexer.filenames
    assert 'root' in lexer.tokens
    assert len(lexer.tokens['root']) == 3  # request-line, status-line, header

    # Default Lexer options
    assert lexer.stripnl is True
    assert lexer.stripall is False
    assert lexer.ensurenl is True
    assert lexer.tabsize == 8

    # Constructor accepts custom Lexer options
    custom = SimplifiedHTTPLexer(
        stripnl=False, stripall=True, ensurenl=False, tabsize=4
    )
    assert custom.stripnl is False
    assert custom.stripall is True
    assert custom.ensurenl is False
    assert custom.tabsize == 4

    # Instances are independent and usable
    assert lexer is not custom
    assert list(lexer.get_tokens('GET / HTTP/1.1'))

# Generated at 2026-10-24 12:49:53.373840
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 12:49:56.168438
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 12:49:59.016006
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 12:50:01.677321
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 12:50:04.186739
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 12:50:06.601796
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 12:50:09.104294
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 12:50:11.613627
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 12:50:14.118322
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 12:50:16.531443
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 12:50:18.944714
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 12:50:21.358772
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 12:50:23.773103
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 12:50:26.187248
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 12:50:28.600957
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 12:50:31.241632
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 12:50:34.141267
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 12:50:52.008386
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 12:50:55.030716
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 12:50:57.902141
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 12:51:22.682731
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 12:51:25.322965
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 12:51:27.739551
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 12:51:30.154016
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 12:51:33.123004
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 12:51:36.084474
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 12:51:38.952518
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 12:52:05.045453
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    import pygments.style
    import pygments.styles

    # 1. Known Pygments style: returns that style class.
    assert (
        ColorFormatter.get_style_class("default")
        is pygments.styles.get_style_by_name("default")
    )
    assert (
        ColorFormatter.get_style_class("fruity")
        is pygments.styles.get_style_by_name("fruity")
    )
    assert issubclass(
        ColorFormatter.get_style_class("monokai"),
        pygments.style.Style
    )

    # 2. Bundled/custom style name: falls back to Solarized256Style.
    assert ColorFormatter.get_style_class("solarized") is Solarized256Style
    assert ColorFormatter.get_style_class("auto") is Solarized256Style

    # 3. Unknown style: falls back to Solarized256Style.
    assert (
        ColorFormatter.get_style_class("no-such-style-xyz123")
        is Solarized256Style
    )

# Generated at 2026-10-24 12:52:26.942941
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 12:52:29.358244
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 12:52:31.772259
# Unit test for method get_lexer_for_body of class ColorFormatter

# Generated at 2026-10-24 12:52:34.394835
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 12:52:52.385483
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 12:52:55.357382
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 12:53:00.832751
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 12:53:04.055787
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 12:53:21.876738
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 12:53:24.386003
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 12:53:26.799272
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 12:53:29.217233
# Unit test for constructor of class ColorFormatter

# Generated at 2026-10-24 12:53:31.636114
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 12:53:34.056501
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 12:53:36.472842
# Unit test for method get_style_class of class ColorFormatter

# Generated at 2026-10-24 12:53:38.894239
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 12:53:41.306603
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 12:53:43.723719
# Unit test for method format_body of class ColorFormatter

# Generated at 2026-10-24 12:54:00.276842
# Unit test for method get_style_class of class ColorFormatter
def test_ColorFormatter_get_style_class():
    import pygments.style
    import pygments.styles

    # 1. Known Pygments style: returns that style class.
    assert (
        ColorFormatter.get_style_class("default")
        is pygments.styles.get_style_by_name("default")
    )
    assert (
        ColorFormatter.get_style_class("fruity")
        is pygments.styles.get_style_by_name("fruity")
    )
    assert issubclass(
        ColorFormatter.get_style_class("monokai"),
        pygments.style.Style
    )

    # 2. Bundled/custom style name: falls back to Solarized256Style.
    assert ColorFormatter.get_style_class("solarized") is Solarized256Style
    assert ColorFormatter.get_style_class("auto") is Solarized256Style

    # 3. Unknown style: falls back to Solarized256Style.
    assert (
        ColorFormatter.get_style_class("no-such-style-xyz123")
        is Solarized256Style
    )

# Generated at 2026-10-24 12:54:03.141391
# Unit test for method format_headers of class ColorFormatter

# Generated at 2026-10-24 12:54:06.110446
# Unit test for method format_headers of class ColorFormatter